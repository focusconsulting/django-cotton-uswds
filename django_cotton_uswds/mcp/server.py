"""MCP server exposing USWDS component documentation and scaffolding tools."""

import re
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

from .component_map import component_tag, uswds_url
from .fetcher import fetch_uswds_guidance

COMPONENTS_DIR = Path(__file__).parent.parent / "templates" / "patterns" / "components"

mcp = FastMCP(
    "django-cotton-uswds",
    instructions=(
        "Provides documentation for USWDS (U.S. Web Design System) components "
        "as implemented in the django-cotton-uswds library. "
        "Use list_components to discover available components, "
        "get_component for full docs including USWDS design guidance, "
        "search_components to find components by functionality, "
        "and scaffold_form to generate a Django template for a form."
    ),
)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _load_md(name: str) -> str | None:
    """Return the markdown documentation for a component, or None."""
    comp_dir = COMPONENTS_DIR / name
    if not comp_dir.is_dir():
        return None

    md_file = comp_dir / f"{name}.md"
    if not md_file.exists():
        md_files = list(comp_dir.glob("*.md"))
        if not md_files:
            return None
        md_file = md_files[0]

    return md_file.read_text(encoding="utf-8")


def _extract_description(md: str) -> str:
    """Return the first descriptive paragraph from a component .md file."""
    lines = md.splitlines()
    in_content = False
    para_lines: list[str] = []

    for line in lines:
        if line.startswith("# "):
            in_content = True
            continue
        if not in_content:
            continue
        if not line.strip():
            if para_lines:
                break
            continue
        if line.startswith("#"):
            break
        para_lines.append(line.strip())

    return " ".join(para_lines)


def _all_components() -> list[dict[str, str]]:
    """Return metadata for every component found in the patterns directory."""
    results = []
    for comp_dir in sorted(COMPONENTS_DIR.iterdir()):
        if not comp_dir.is_dir():
            continue
        name = comp_dir.name
        md = _load_md(name)
        if md is None:
            continue
        results.append(
            {
                "name": name,
                "tag": component_tag(name),
                "description": _extract_description(md),
            }
        )
    return results


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------


@mcp.tool()
def list_components() -> str:
    """
    List all available USWDS components with their cotton tag name and a brief
    description. Call this first to discover what components exist before requesting
    full docs.
    """
    components = _all_components()
    lines = ["# Available USWDS Components\n"]
    for comp in components:
        lines.append(f"- **{comp['tag']}** (`{comp['name']}`): {comp['description']}")
    return "\n".join(lines)


@mcp.tool()
def get_component(name: str) -> str:
    """
    Get full documentation for a USWDS component.

    Returns the cotton API docs (props, slots, usage examples) from the local
    pattern library, combined with live USWDS design guidance (when to use,
    when not to use, usability and accessibility guidance).

    Args:
        name: Component name as listed by list_components, e.g. "alert",
              "button", "text_input", "radio_button".
    """
    md = _load_md(name)
    if md is None:
        return (
            f"Component '{name}' not found. "
            "Use list_components() to see all available components."
        )

    sections = [f"# Cotton API — `{component_tag(name)}`\n\n{md}"]

    url = uswds_url(name)
    if url:
        guidance = fetch_uswds_guidance(url)
        if guidance:
            sections.append(f"# USWDS Design Guidance\n\nSource: {url}\n\n{guidance}")
        else:
            sections.append(
                f"# USWDS Design Guidance\n\nSee: {url}\n\n"
                "(Could not fetch live guidance — check the USWDS docs directly.)"
            )
    else:
        sections.append(
            "# USWDS Design Guidance\n\n"
            "This is a custom extension component"
            " — no dedicated USWDS documentation page."
        )

    return "\n\n---\n\n".join(sections)


@mcp.tool()
def search_components(query: str) -> str:
    """
    Search for USWDS components by functionality, keyword, or use case.

    Returns matching components with a short excerpt from their documentation.
    Useful when you know what you want to do but not which component to use.

    Args:
        query: Search terms, e.g. "file upload", "navigation", "error message",
               "date", "multi-step form".
    """
    query_terms = [t.lower() for t in re.split(r"\W+", query) if t]
    if not query_terms:
        return "Please provide a search query."

    results: list[tuple[int, str, list[str]]] = []

    for comp_dir in sorted(COMPONENTS_DIR.iterdir()):
        if not comp_dir.is_dir():
            continue
        name = comp_dir.name
        md = _load_md(name)
        if md is None:
            continue

        md_lower = md.lower()
        name_lower = name.replace("_", " ")

        score = 0
        excerpts: list[str] = []

        for term in query_terms:
            if term in name_lower:
                score += 3
            if term in md_lower:
                score += 1
                idx = md_lower.find(term)
                start = max(0, idx - 60)
                end = min(len(md), idx + 80)
                excerpt = md[start:end].replace("\n", " ").strip()
                excerpts.append(f"…{excerpt}…")

        if score > 0:
            results.append((score, name, excerpts))

    if not results:
        return f"No components found matching '{query}'."

    results.sort(key=lambda x: -x[0])
    lines = [f"# Search Results for '{query}'\n"]
    for _, name, excerpts in results[:8]:
        lines.append(f"## {component_tag(name)} (`{name}`)")
        if excerpts:
            lines.append(excerpts[0])
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# scaffold_form
# ---------------------------------------------------------------------------

_KNOWN_TYPES = {
    "text",
    "email",
    "number",
    "tel",
    "url",
    "password",
    "textarea",
    "select",
    "radio",
    "checkbox",
    "file",
    "date",
}


def _render_field(name: str, ftype: str, label: str, required: bool) -> str:
    req = ' required="true"' if required else ""

    if ftype in ("text", "email", "number", "tel", "url", "password"):
        type_attr = f' type="{ftype}"' if ftype != "text" else ""
        return f'<c-text-input name="{name}" label="{label}"{type_attr}{req} />'

    if ftype == "textarea":
        return f'<c-textarea name="{name}" label="{label}"{req}></c-textarea>'

    if ftype == "select":
        return (
            f'<c-select name="{name}" label="{label}"{req}>\n'
            f"    <!-- Populate with option tags or a choices loop -->\n"
            f"  </c-select>"
        )

    if ftype == "radio":
        return (
            f'<c-fieldset legend="{label}"{req}>\n'
            f'    <c-radio-button name="{name}" id="{name}_1" label="Option 1" value="1" />\n'  # noqa: E501
            f'    <c-radio-button name="{name}" id="{name}_2" label="Option 2" value="2" />\n'  # noqa: E501
            f"    <!-- Add more radio buttons as needed -->\n"
            f"  </c-fieldset>"
        )

    if ftype == "checkbox":
        return f'<c-checkbox name="{name}" id="{name}" label="{label}"{req} />'

    if ftype == "file":
        return f'<c-file-input name="{name}" label="{label}"{req} />'

    if ftype == "date":
        return f'<c-date-picker name="{name}" label="{label}"{req} />'

    # Fallback for unrecognised types
    return f'<c-text-input name="{name}" label="{label}"{req} />'


@mcp.tool()
def scaffold_form(fields: list[dict[str, Any]]) -> str:
    """
    Generate a Django template for a form using USWDS cotton components.

    Args:
        fields: List of field definitions. Each field is a dict with:
                - name (str): HTML name attribute for the field
                - type (str): one of text, email, number, tel, url, password,
                              textarea, select, radio, checkbox, file, date
                - label (str): human-readable field label
                - required (bool, optional): marks the field as required

    Example:
        [
          {"name": "full_name", "type": "text", "label": "Full name", "required": true},
          {"name": "agency",    "type": "select",  "label": "Agency"},
          {"name": "resume",    "type": "file",    "label": "Resume"}
        ]
    """
    if not fields:
        return "No fields provided. Pass a list of field definitions."

    unknown_types: list[str] = []
    rendered_fields: list[str] = []

    for field in fields:
        name = field.get("name", "field")
        ftype = str(field.get("type", "text")).lower()
        label = field.get("label", name.replace("_", " ").title())
        required = bool(field.get("required", False))

        if ftype not in _KNOWN_TYPES:
            unknown_types.append(ftype)
            ftype = "text"

        rendered_fields.append("  " + _render_field(name, ftype, label, required))

    csrf_line = "  {% csrf_token %}"
    submit_line = '  <c-button text="Submit" type="submit" />'

    lines = [
        "{% load cotton %}",
        "",
        '<c-form method="post">',
        csrf_line,
        "",
        *rendered_fields,
        "",
        submit_line,
        "</c-form>",
    ]

    output = "\n".join(lines)

    if unknown_types:
        output += (
            f"\n\n<!-- Note: unknown field type(s) {unknown_types!r} "
            "were rendered as text inputs. -->"
        )

    return f"```django\n{output}\n```"
