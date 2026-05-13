# django-cotton-uswds MCP Server

An [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) server that gives AI assistants deep knowledge of USWDS components as implemented in this library. When connected, your AI assistant knows every component's props, slots, usage examples, and live design guidance from the official USWDS documentation — without you having to look anything up.

## What it does

The server exposes four tools:

| Tool | What it answers |
|------|----------------|
| `list_components` | "What components are available?" — returns all components with tags and descriptions |
| `get_component` | "How do I use `<c-alert>`?" — returns props, slots, examples, plus live USWDS guidance (when to use, accessibility, usability) fetched from designsystem.digital.gov |
| `search_components` | "What component handles file uploads?" — full-text search across component docs |
| `scaffold_form` | "Generate a form with name, email, and file fields" — returns a ready-to-use Django template |

### Two-layer documentation

`get_component` combines two sources:

1. **Local docs** (`templates/patterns/components/<name>/<name>.md`) — the cotton API: props, slots, and usage examples specific to this library
2. **Live USWDS guidance** (fetched from `designsystem.digital.gov`) — when to use, when not to use, usability notes, and accessibility requirements

The live fetch is cached for the lifetime of the server process. If the network is unavailable, the local docs are returned with a fallback link.

## Installation

The MCP server is an optional dependency. Install it alongside the library:

```bash
pip install "django-cotton-uswds[mcp]"
```

Or with uv:

```bash
uv add "django-cotton-uswds[mcp]"
```

## Configuration

### Claude Code

Add to `.claude/settings.json` in your Django project:

```json
{
  "mcpServers": {
    "uswds": {
      "command": "uvx",
      "args": ["--from", "django-cotton-uswds[mcp]", "django-cotton-uswds-mcp"]
    }
  }
}
```

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "uswds": {
      "command": "uvx",
      "args": ["--from", "django-cotton-uswds[mcp]", "django-cotton-uswds-mcp"]
    }
  }
}
```

### Other MCP clients

Run the server directly over stdio:

```bash
python -m django_cotton_uswds.mcp
```

## Usage examples

Once connected, you can ask your AI assistant things like:

- *"What USWDS component should I use to show a 4-step form progress?"* → `get_component("step_indicator")` with USWDS guidance on when to use it
- *"Should I use an alert or a site-alert for a login error?"* → `get_component` for both, with USWDS "when to use" guidance to distinguish them
- *"Scaffold a contact form with name, email, and message fields"* → `scaffold_form` returns a complete Django template
- *"How do I make a button that doesn't look like a button?"* → `search_components("unstyled button")` → `get_component("button")` with the `unstyled` variant

---

## For developers

### Project layout

```
django_cotton_uswds/mcp/
  __init__.py
  __main__.py       # entry point; calls mcp.run() (stdio transport)
  server.py         # tool definitions using FastMCP
  component_map.py  # maps local component names → USWDS URL slugs
  fetcher.py        # fetches + parses the Guidance section from USWDS pages
```

The server reads documentation from the existing pattern library files — no separate data to maintain:

```
django_cotton_uswds/templates/patterns/components/<name>/
  <name>.md         # source of truth for get_component local docs
  <name>.yaml       # variant data (not currently used by MCP, available if needed)
```

### Running locally

```bash
# Start the server (stdio — for manual MCP client testing)
python -m django_cotton_uswds.mcp

# Run all MCP unit tests (no network required)
uv run --extra test --extra mcp pytest tests/mcp/test_mcp.py -v

# Run the full test suite
uv run --extra test --extra mcp pytest tests/ --ignore=tests/mcp/eval -v
```

### Adding a new component

When a new component is added to the library, three things need updating in this package:

1. **Add a mapping in `component_map.py`**

   ```python
   # In COMPONENT_USWDS_SLUGS:
   "my_component": "my-component",   # matches the USWDS URL slug
   # or None if there is no USWDS page for this component
   "my_custom_component": None,
   ```

   The mapping drives both the USWDS guidance fetch and the tag name shown to the AI (`my_component` → `<c-my-component>`).

2. **The `.md` file is picked up automatically**

   As long as `templates/patterns/components/<name>/<name>.md` exists and follows the standard structure (see any existing `.md` for reference), `get_component` and `list_components` will include it with no code changes.

### Improving the USWDS guidance parser

The guidance parser lives in `fetcher.py`. It looks for an `<h2>Guidance</h2>` heading in the USWDS page HTML and extracts text until the next `<h2>`. If a component's guidance is not being extracted correctly:

1. Fetch the raw USWDS page and inspect the HTML structure
2. Check whether the heading text or structure differs from the expected pattern
3. Adjust the regex in `_extract_guidance()` and add a failing integration test first

```bash
# Verify a specific component's guidance fetch
USWDS_INTEGRATION=1 python -c "
from django_cotton_uswds.mcp.fetcher import fetch_uswds_guidance
print(fetch_uswds_guidance('https://designsystem.digital.gov/components/alert/'))
"
```

### Measuring impact with the eval harness

The eval harness in `tests/mcp/eval/` measures whether the MCP server actually improves the quality of AI answers. It asks Claude 10 realistic developer questions with and without MCP access, then scores each answer on Correctness, Specificity, and Guidance using a judge prompt.

```bash
# Install eval dependencies
uv run --extra eval python tests/mcp/eval/run_eval.py --compare

# Append mean scores to SCORES.md and commit alongside your change
uv run --extra eval python tests/mcp/eval/run_eval.py --compare --save-scores

# Save raw per-question JSON for deeper analysis
uv run --extra eval python tests/mcp/eval/run_eval.py --compare --output results.json
```

`tests/mcp/eval/SCORES.md` is the committed history of mean scores. Run `--compare --save-scores` before and after any significant change to the server and commit the updated file alongside your code change. This makes regressions visible in code review.

### Adding eval questions

Questions live in `tests/mcp/eval/questions.yaml`. Each has a `requires` field that classifies what kind of knowledge is needed:

- `guidance` — needs live USWDS "when to use / when not to" knowledge
- `api` — needs cotton component API knowledge from local `.md` files
- `scaffold` — exercises the `scaffold_form` tool

When adding a new tool or improving an existing one, add at least one question that specifically targets the new capability.
