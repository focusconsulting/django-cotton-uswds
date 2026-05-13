# Eval Scores

Tracks the impact of the MCP server on answer quality over time.
Each row is a `--compare` run. Update this file when making significant
changes to the server and commit it alongside the change.

Scores are 1–5 per dimension (higher is better):
- **Correctness** — factually accurate per USWDS guidelines and the cotton API
- **Specificity** — names concrete components, props, or includes code
- **Guidance** — reflects USWDS design intent (when to use, accessibility)

Each `--compare` run produces two rows (without-mcp / with-mcp). The delta is the
difference between the two `Total` values for the same date.

## How to update

Run after any significant change to the MCP server, then commit the updated file:

```bash
ANTHROPIC_API_KEY=... uv run --extra eval python tests/mcp/eval/run_eval.py --compare --save-scores
git add tests/mcp/eval/SCORES.md
git commit -m "eval: update scores after <describe your change>"
```

This makes score changes visible in code review alongside the code that caused them.

---

## Results

| Date | Model | Condition | Correctness | Specificity | Guidance | Total |
|------|-------|-----------|-------------|-------------|----------|-------|
| 2026-04-27 | claude-sonnet-4-6 | without-mcp | 3.70 | 4.40 | 4.20 | 12.30 |
| 2026-04-27 | claude-sonnet-4-6 | with-mcp | 3.90 | 4.90 | 4.40 | 13.20 |
