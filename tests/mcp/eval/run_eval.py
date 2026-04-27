#!/usr/bin/env python3
"""
Eval harness: measures how much the MCP server improves Claude's answers
about USWDS components.

Usage:
    # Run both conditions and compare
    python tests/mcp/eval/run_eval.py --compare

    # Run only one condition
    python tests/mcp/eval/run_eval.py --with-mcp
    python tests/mcp/eval/run_eval.py --without-mcp

    # Save raw results to a file
    python tests/mcp/eval/run_eval.py --compare --output results.json

Requirements:
    pip install anthropic pyyaml mcp

Environment:
    ANTHROPIC_API_KEY must be set.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

try:
    import anthropic
    import yaml
except ImportError:
    print("Missing dependencies. Run: pip install anthropic pyyaml")
    sys.exit(1)

EVAL_DIR = Path(__file__).parent
QUESTIONS_FILE = EVAL_DIR / "questions.yaml"
JUDGE_PROMPT_FILE = EVAL_DIR / "judge_prompt.txt"

MODEL = "claude-sonnet-4-6"

SYSTEM_WITHOUT_MCP = (
    "You are a helpful assistant for Django developers building government websites. "
    "Answer questions about the USWDS (U.S. Web Design System) and the "
    "django-cotton-uswds library."
)

SYSTEM_WITH_MCP = (
    "You are a helpful assistant for Django developers building government websites. "
    "You have access to MCP tools that provide detailed documentation for USWDS "
    "components as implemented in the django-cotton-uswds library. "
    "Use list_components to discover components, get_component for full docs "
    "including USWDS design guidance, search_components to find components by "
    "use case, and scaffold_form to generate form templates. "
    "Always consult the tools before answering."
)


def load_questions() -> list[dict[str, Any]]:
    data = yaml.safe_load(QUESTIONS_FILE.read_text())
    return data["questions"]


def load_judge_prompt() -> str:
    return JUDGE_PROMPT_FILE.read_text()


def _call_mcp_tools(question: str) -> str:
    """
    Simulate MCP tool access by calling server functions directly and
    prepending the results to the question as context.

    In a production eval you would use a real MCP client; this approach
    avoids the transport overhead while testing the same knowledge.
    """
    # Import here so the module can be loaded without mcp installed during testing.
    from django_cotton_uswds.mcp.server import (
        get_component,
        list_components,
        scaffold_form,
        search_components,
    )

    q_lower = question.lower()

    context_parts: list[str] = []

    # Always include the component list.
    context_parts.append("=== MCP: list_components ===")
    context_parts.append(list_components())

    # Search for relevant components.
    search_terms = _extract_search_terms(q_lower)
    for term in search_terms:
        results = search_components(term)
        if "No components found" not in results:
            context_parts.append(f"=== MCP: search_components('{term}') ===")
            context_parts.append(results)

    # Fetch docs for components mentioned by name.
    mentioned = _extract_component_names(q_lower)
    for name in mentioned:
        docs = get_component(name)
        if "not found" not in docs.lower():
            context_parts.append(f"=== MCP: get_component('{name}') ===")
            context_parts.append(docs)

    # If the question asks to scaffold a form, call scaffold_form.
    if "scaffold" in q_lower or "generate" in q_lower or "template" in q_lower:
        fields = _extract_scaffold_fields(question)
        if fields:
            context_parts.append("=== MCP: scaffold_form ===")
            context_parts.append(scaffold_form(fields))

    context = "\n\n".join(context_parts)
    return f"<mcp_context>\n{context}\n</mcp_context>\n\nQuestion: {question}"


def _extract_search_terms(q: str) -> list[str]:
    """Pull out likely component-search terms from the question."""
    candidates = [
        "alert",
        "site alert",
        "modal",
        "button",
        "file",
        "navigation",
        "step indicator",
        "combo box",
        "select",
        "radio",
        "checkbox",
        "text input",
        "textarea",
        "date",
        "form",
    ]
    return [c for c in candidates if c in q]


def _extract_component_names(q: str) -> list[str]:
    """Extract component names that appear in the question."""
    all_names = [
        "alert",
        "site_alert",
        "button",
        "modal",
        "text_input",
        "textarea",
        "select",
        "radio_button",
        "checkbox",
        "file_input",
        "date_picker",
        "step_indicator",
        "combo_box",
        "side_nav",
        "in_page_nav",
        "breadcrumb",
        "pagination",
        "header",
        "footer",
    ]
    q_normalised = q.replace("-", "_").replace(" ", "_")
    return [n for n in all_names if n in q_normalised]


def _extract_scaffold_fields(question: str) -> list[dict[str, Any]]:
    """Crude extraction of field specs from a scaffold question."""
    import re

    fields = []
    pattern = re.compile(
        r"(\w[\w\s]+?)\s*\((text|email|textarea|select|radio|checkbox|file|date)"
        r"(?:,\s*(required))?\)",
        re.IGNORECASE,
    )
    for m in pattern.finditer(question):
        fields.append(
            {
                "name": m.group(1).strip().lower().replace(" ", "_"),
                "type": m.group(2).lower(),
                "label": m.group(1).strip().title(),
                "required": bool(m.group(3)),
            }
        )
    return fields


def get_answer(client: anthropic.Anthropic, question: str, *, with_mcp: bool) -> str:
    """Get Claude's answer to a question, with or without MCP context."""
    if with_mcp:
        user_content = _call_mcp_tools(question)
        system = SYSTEM_WITH_MCP
    else:
        user_content = question
        system = SYSTEM_WITHOUT_MCP

    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": user_content}],
    )
    return response.content[0].text


def judge_answer(
    client: anthropic.Anthropic, question: str, answer: str
) -> dict[str, Any]:
    """Use Claude as a judge to score an answer."""
    prompt_template = load_judge_prompt()
    prompt = prompt_template.replace("{question}", question).replace("{answer}", answer)

    response = client.messages.create(
        model=MODEL,
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = response.content[0].text.strip()

    # Extract JSON even if the model adds surrounding text.
    import re

    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not match:
        return {"correctness": 0, "specificity": 0, "guidance": 0, "notes": raw}

    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return {"correctness": 0, "specificity": 0, "guidance": 0, "notes": raw}


def run_condition(
    client: anthropic.Anthropic,
    questions: list[dict[str, Any]],
    *,
    with_mcp: bool,
) -> list[dict[str, Any]]:
    label = "with-mcp" if with_mcp else "without-mcp"
    print(f"\n{'=' * 60}")
    print(f"Running condition: {label}")
    print("=" * 60)

    results = []
    for q in questions:
        print(f"\n[{q['id']}] {q['question'][:80]}...")
        answer = get_answer(client, q["question"], with_mcp=with_mcp)
        scores = judge_answer(client, q["question"], answer)
        scores["id"] = q["id"]
        scores["condition"] = label
        scores["answer_preview"] = answer[:200]
        results.append(scores)
        print(
            f"  correctness={scores['correctness']} "
            f"specificity={scores['specificity']} "
            f"guidance={scores['guidance']}  — {scores.get('notes', '')}"
        )

    return results


SCORES_FILE = EVAL_DIR / "SCORES.md"
_SCORES_ROW = (
    "| {date} | {model} | {condition}"
    " | {correctness:.2f} | {specificity:.2f} | {guidance:.2f} | {total:.2f} |"
)


def _mean(results: list[dict], dim: str) -> float:
    return sum(r[dim] for r in results) / len(results)


def append_scores(
    with_results: list[dict],
    without_results: list[dict],
    model: str,
) -> None:
    """Append a pair of rows (without-mcp / with-mcp) to SCORES.md."""
    from datetime import date

    today = date.today().isoformat()
    dims = ["correctness", "specificity", "guidance"]

    new_rows: list[str] = []
    pairs = [("without-mcp", without_results), ("with-mcp", with_results)]
    for condition, results in pairs:
        means = {d: _mean(results, d) for d in dims}
        total = sum(means.values())
        new_rows.append(
            _SCORES_ROW.format(
                date=today,
                model=model,
                condition=condition,
                total=total,
                **means,
            )
        )

    text = SCORES_FILE.read_text()
    # On first use replace the placeholder; otherwise append before the last blank line.
    placeholder = "| *(run `--compare --save-scores` to populate)* | | | | | | |"
    if placeholder in text:
        text = text.replace(placeholder, "\n".join(new_rows))
    else:
        text = text.rstrip("\n") + "\n" + "\n".join(new_rows) + "\n"

    SCORES_FILE.write_text(text)
    rel = SCORES_FILE.relative_to(EVAL_DIR.parent.parent.parent)
    print(f"\nScores appended to {rel}")


def print_comparison(with_results: list[dict], without_results: list[dict]) -> None:
    print(f"\n{'=' * 60}")
    print("COMPARISON: with-mcp vs without-mcp")
    print("=" * 60)

    dims = ["correctness", "specificity", "guidance"]
    headers = ["ID", *dims, "total"]
    fmt = "{:<8}" + "{:<14}" * len(headers[1:])

    print("\n  without-mcp:")
    print("  " + fmt.format(*headers))
    wo_totals: dict[str, float] = {d: 0.0 for d in dims}
    for r in without_results:
        row = [r["id"]] + [str(r[d]) for d in dims] + [str(sum(r[d] for d in dims))]
        print("  " + fmt.format(*row))
        for d in dims:
            wo_totals[d] += r[d]

    print("\n  with-mcp:")
    print("  " + fmt.format(*headers))
    w_totals: dict[str, float] = {d: 0.0 for d in dims}
    for r in with_results:
        row = [r["id"]] + [str(r[d]) for d in dims] + [str(sum(r[d] for d in dims))]
        print("  " + fmt.format(*row))
        for d in dims:
            w_totals[d] += r[d]

    n = len(with_results)
    print(f"\n  Mean scores (n={n}):")
    print(f"  {'Dimension':<16} {'without-mcp':>12} {'with-mcp':>10} {'delta':>8}")
    for d in dims:
        wo = wo_totals[d] / n
        w = w_totals[d] / n
        delta = w - wo
        sign = "+" if delta >= 0 else ""
        print(f"  {d:<16} {wo:>12.2f} {w:>10.2f} {sign}{delta:>7.2f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Eval harness for MCP server")
    parser.add_argument("--with-mcp", action="store_true")
    parser.add_argument("--without-mcp", action="store_true")
    parser.add_argument("--compare", action="store_true", help="Run both conditions")
    parser.add_argument("--output", help="Save raw results JSON to this file")
    parser.add_argument(
        "--save-scores",
        action="store_true",
        help="Append mean scores to tests/mcp/eval/SCORES.md (requires --compare)",
    )
    parser.add_argument(
        "--model", default=MODEL, help=f"Claude model (default: {MODEL})"
    )
    args = parser.parse_args()

    if not (args.with_mcp or args.without_mcp or args.compare):
        parser.print_help()
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    questions = load_questions()

    all_results: list[dict] = []

    if args.compare or args.without_mcp:
        without = run_condition(client, questions, with_mcp=False)
        all_results.extend(without)

    if args.compare or args.with_mcp:
        with_ = run_condition(client, questions, with_mcp=True)
        all_results.extend(with_)

    if args.compare:
        without_only = [r for r in all_results if r["condition"] == "without-mcp"]
        with_only = [r for r in all_results if r["condition"] == "with-mcp"]
        print_comparison(with_only, without_only)
        if args.save_scores:
            append_scores(with_only, without_only, args.model)

    if args.output:
        Path(args.output).write_text(json.dumps(all_results, indent=2))
        print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
