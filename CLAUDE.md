# django-cotton-uswds — Claude Code Guide

USWDS (U.S. Web Design System) components as Django Cotton templates.
See [UBIQUITOUS_LANGUAGE.md](UBIQUITOUS_LANGUAGE.md) for canonical domain terms.

## Architecture

### Component system

Components live in `django_cotton_uswds/templates/cotton/<name>/index.html`.
Each declares its props at the top:

```html
<c-vars text="" variant="" :disabled="False" />
```

- `<c-vars>` with string defaults → string prop
- `<c-vars :disabled="False">` with `:` prefix → Python-typed (bool/int/list)
- `{{ slot }}` → default slot content from between the component's tags
- `{{ attrs }}` → passes undeclared attributes through to the root HTML element

Cotton tag name = directory name with `_` → `-` and `c-` prefix.
`radio_button/` → `<c-radio-button>`, `text_input/` → `<c-text-input>`.

### Pattern library

Every component has a corresponding entry in
`django_cotton_uswds/templates/patterns/components/<name>/`:

- `<name>.html` — renders the component with variant data injected
- `<name>.yaml` — variant definitions (prop values for the pattern library UI)
- `<name>.md` — human-readable docs: props table, slots, usage examples

The `.md` files are the source of truth for the MCP server documentation.

### Form rendering pipeline

```
Django Form field
  → USWDSFormRenderer (renderer.py)
    → templates/django/forms/widgets/<widget>.html
      → <c-form-group>, <c-label>, <c-error-message>, <c-text-input> etc.
```

`USWDSFormMixin` in `mixins.py` sets `default_renderer` on a per-form basis.
Global rendering: `FORM_RENDERER = "django_cotton_uswds.renderer.USWDSFormRenderer"`.

### MCP server

`django_cotton_uswds/mcp/` — exposes component docs to AI assistants via MCP.

- `server.py` — four tools: `list_components`, `get_component`, `search_components`, `scaffold_form`
- `fetcher.py` — fetches live USWDS guidance from designsystem.digital.gov, cached per process
- `component_map.py` — maps local component names to USWDS URL slugs

## Adding a new component

1. Create `django_cotton_uswds/templates/cotton/<name>/index.html`
   — declare props with `<c-vars>`, render USWDS HTML
2. Create `django_cotton_uswds/templates/patterns/components/<name>/`:
   - `<name>.html` — pattern library renderer
   - `<name>.yaml` — variant definitions
   - `<name>.md` — props table, slots, examples (follows the alert.md structure)
3. Add an entry to `django_cotton_uswds/mcp/component_map.py`
   — map the name to its USWDS URL slug, or `None` for custom components
4. Optionally override widget rendering in `templates/django/forms/widgets/`
   and wire up in `renderer.py`

## Testing

```bash
# Run all unit tests (no network, no Django DB)
uv run pytest tests/

# Run MCP unit tests only
uv run pytest tests/mcp/test_mcp.py -v

# Run the eval harness (requires ANTHROPIC_API_KEY)
uv run --extra eval python tests/mcp/eval/run_eval.py --compare --save-scores
```

Tests use `pytest-django`. The test settings are in `tests/settings.py`.
MCP unit tests mock `fetch_uswds_guidance` so no network access is needed.

## Key files

| Path | Purpose |
|------|---------|
| `django_cotton_uswds/renderer.py` | `USWDSFormRenderer` — bridges Django forms to Cotton |
| `django_cotton_uswds/mixins.py` | `USWDSFormMixin` — per-form opt-in |
| `django_cotton_uswds/mcp/server.py` | MCP tool definitions |
| `django_cotton_uswds/mcp/fetcher.py` | USWDS guidance fetcher |
| `django_cotton_uswds/mcp/component_map.py` | Component → USWDS URL mapping |
| `tests/mcp/test_mcp.py` | MCP unit tests |
| `tests/mcp/eval/run_eval.py` | Eval harness (measures MCP impact) |

## Running the demo

```bash
just install   # installs with demo dependencies
just demo      # runs dev server at http://127.0.0.1:8000/
just build     # builds static site into demo_project/dist/
```

## MCP server setup (for users of this library)

```json
// .claude/settings.json in the consumer project
{
  "mcpServers": {
    "uswds": {
      "command": "uvx",
      "args": ["--from", "django-cotton-uswds[mcp]", "django-cotton-uswds-mcp"]
    }
  }
}
```

Or during development of this library:
```bash
python -m django_cotton_uswds.mcp
```
