"""Unit tests for MCP server, component map, and fetcher.

No network calls, no Django required.
"""

from unittest.mock import patch
from unittest.mock import patch as _patch
from urllib.error import URLError

import pytest

pytest.importorskip("mcp", reason="install the 'mcp' extra to run MCP tests")

from django_cotton_uswds.mcp.component_map import (
    COMPONENT_USWDS_SLUGS,
    component_tag,
    uswds_url,
)
from django_cotton_uswds.mcp.fetcher import clear_cache, fetch_uswds_guidance
from django_cotton_uswds.mcp.server import (
    COMPONENTS_DIR,
    _extract_description,
    _load_md,
    get_component,
    list_components,
    scaffold_form,
    search_components,
)

# ---------------------------------------------------------------------------
# component_map
# ---------------------------------------------------------------------------


def test_component_tag_multi_word():
    assert component_tag("radio_button") == "<c-radio-button>"
    assert component_tag("text_input") == "<c-text-input>"
    assert component_tag("button_group") == "<c-button-group>"


def test_uswds_url_standard():
    assert uswds_url("alert") == "https://designsystem.digital.gov/components/alert/"


def test_uswds_url_mapped():
    assert uswds_url("radio_button") == (
        "https://designsystem.digital.gov/components/radio-buttons/"
    )
    assert uswds_url("side_nav") == (
        "https://designsystem.digital.gov/components/side-navigation/"
    )


def test_uswds_url_none_for_custom():
    assert uswds_url("currency_input") is None
    assert uswds_url("input_group") is None
    assert uswds_url("label") is None


def test_component_map_covers_all_dirs():
    """Every component directory in patterns/ must have an entry in the map."""
    for comp_dir in COMPONENTS_DIR.iterdir():
        if comp_dir.is_dir():
            assert comp_dir.name in COMPONENT_USWDS_SLUGS, (
                f"Missing COMPONENT_USWDS_SLUGS entry for '{comp_dir.name}'"
            )


# ---------------------------------------------------------------------------
# _load_md / _extract_description
# ---------------------------------------------------------------------------


def test_load_md_known_component():
    md = _load_md("alert")
    assert md is not None
    assert "Props" in md


def test_load_md_unknown_component():
    assert _load_md("nonexistent_xyz") is None


def test_extract_description_returns_first_paragraph():
    md = "# Alert\n\nA contextual notification.\n\n## Props\n..."
    desc = _extract_description(md)
    assert desc == "A contextual notification."


# ---------------------------------------------------------------------------
# list_components
# ---------------------------------------------------------------------------


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    """Prevent any real network calls in unit tests."""
    monkeypatch.setattr(
        "django_cotton_uswds.mcp.server.fetch_uswds_guidance",
        lambda url: None,
    )


def test_list_components_includes_known():
    result = list_components()
    assert "<c-alert>" in result
    assert "<c-button>" in result
    assert "<c-text-input>" in result
    assert "<c-radio-button>" in result


def test_list_components_has_descriptions():
    result = list_components()
    # Every entry line should have a colon separating tag from description.
    entries = [line for line in result.splitlines() if line.startswith("- **")]
    for entry in entries:
        assert "): " in entry, f"Missing description in: {entry}"


# ---------------------------------------------------------------------------
# get_component
# ---------------------------------------------------------------------------


def test_get_component_returns_local_docs():
    result = get_component("alert")
    assert "Props" in result
    assert "type" in result
    assert "heading" in result
    assert ":rich" in result


def test_get_component_unknown():
    result = get_component("totally_nonexistent")
    assert "not found" in result.lower()


def test_get_component_shows_fallback_url_on_fetch_failure():
    result = get_component("alert")
    # fetch returns None (mocked above), so we expect the fallback URL message
    assert "designsystem.digital.gov" in result


def test_get_component_with_guidance():
    mock_guidance = "### When to Use\nUse for system status notifications."
    with patch(
        "django_cotton_uswds.mcp.server.fetch_uswds_guidance",
        return_value=mock_guidance,
    ):
        result = get_component("alert")
    assert "USWDS Design Guidance" in result
    assert "When to Use" in result
    assert "system status" in result


def test_get_component_custom_no_uswds_page():
    # currency_input has no USWDS page — should say so clearly.
    result = get_component("currency_input")
    assert "custom extension" in result.lower() or "no dedicated" in result.lower()


# ---------------------------------------------------------------------------
# search_components
# ---------------------------------------------------------------------------


def test_search_file_upload():
    result = search_components("file upload")
    assert "file_input" in result or "file-input" in result


def test_search_navigation():
    result = search_components("navigation")
    # side_nav, in_page_nav, breadcrumb, pagination all relate to navigation
    assert any(
        name in result
        for name in ["side_nav", "in_page_nav", "breadcrumb", "pagination"]
    )


def test_search_no_results():
    result = search_components("xyzzy_nonexistent_query_99999")
    assert "No components found" in result


def test_search_empty_query():
    result = search_components("")
    assert "provide a search query" in result.lower()


def test_search_returns_at_most_eight():
    # "input" matches many components — should be capped at 8.
    result = search_components("input")
    entries = [line for line in result.splitlines() if line.startswith("## ")]
    assert len(entries) <= 8


# ---------------------------------------------------------------------------
# scaffold_form
# ---------------------------------------------------------------------------


def test_scaffold_form_empty_fields():
    result = scaffold_form([])
    assert "No fields" in result


def test_scaffold_form_includes_csrf():
    result = scaffold_form([{"name": "q", "type": "text", "label": "Query"}])
    assert "csrf_token" in result


def test_scaffold_form_text_field():
    result = scaffold_form(
        [{"name": "full_name", "type": "text", "label": "Full name"}]
    )
    assert "c-text-input" in result
    assert 'name="full_name"' in result
    assert 'label="Full name"' in result


def test_scaffold_form_email_field():
    result = scaffold_form([{"name": "email", "type": "email", "label": "Email"}])
    assert 'type="email"' in result


def test_scaffold_form_required_attribute():
    result = scaffold_form(
        [{"name": "f", "type": "text", "label": "F", "required": True}]
    )
    assert 'required="true"' in result


def test_scaffold_form_not_required_by_default():
    result = scaffold_form([{"name": "f", "type": "text", "label": "F"}])
    assert 'required="true"' not in result


def test_scaffold_form_select():
    result = scaffold_form([{"name": "agency", "type": "select", "label": "Agency"}])
    assert "c-select" in result
    assert 'name="agency"' in result


def test_scaffold_form_radio():
    result = scaffold_form([{"name": "choice", "type": "radio", "label": "Pick one"}])
    assert "c-radio-button" in result
    assert "c-fieldset" in result


def test_scaffold_form_checkbox():
    result = scaffold_form([{"name": "agree", "type": "checkbox", "label": "I agree"}])
    assert "c-checkbox" in result


def test_scaffold_form_file():
    result = scaffold_form([{"name": "resume", "type": "file", "label": "Resume"}])
    assert "c-file-input" in result


def test_scaffold_form_date():
    result = scaffold_form([{"name": "dob", "type": "date", "label": "Date of birth"}])
    assert "c-date-picker" in result


def test_scaffold_form_textarea():
    result = scaffold_form(
        [{"name": "message", "type": "textarea", "label": "Message"}]
    )
    assert "c-textarea" in result


def test_scaffold_form_unknown_type_falls_back():
    result = scaffold_form([{"name": "f", "type": "color_picker", "label": "Color"}])
    assert "c-text-input" in result
    assert "color_picker" in result  # note in output


def test_scaffold_form_submit_button():
    result = scaffold_form([{"name": "q", "type": "text", "label": "Q"}])
    assert "c-button" in result
    assert "Submit" in result


def test_scaffold_form_multiple_fields():
    fields = [
        {"name": "name", "type": "text", "label": "Name", "required": True},
        {"name": "agency", "type": "select", "label": "Agency"},
        {"name": "resume", "type": "file", "label": "Resume"},
    ]
    result = scaffold_form(fields)
    assert "c-text-input" in result
    assert "c-select" in result
    assert "c-file-input" in result
    assert result.count("c-") >= 4  # 3 fields + submit button


def test_scaffold_form_wrapped_in_code_block():
    result = scaffold_form([{"name": "q", "type": "text", "label": "Q"}])
    assert result.startswith("```django")
    assert result.endswith("```")


# ---------------------------------------------------------------------------
# Fetcher — mocked (no network needed)
# ---------------------------------------------------------------------------


def test_fetch_returns_none_on_network_error():
    clear_cache()
    with _patch(
        "django_cotton_uswds.mcp.fetcher.urlopen",
        side_effect=URLError("simulated timeout"),
    ):
        result = fetch_uswds_guidance(
            "https://designsystem.digital.gov/components/alert/"
        )
    assert result is None


def test_fetch_caches_none_on_failure():
    """A failed fetch must be cached so urlopen is only called once per session."""
    clear_cache()
    url = "https://designsystem.digital.gov/components/alert/"
    call_count = 0

    def failing_urlopen(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        raise URLError("simulated failure")

    with _patch("django_cotton_uswds.mcp.fetcher.urlopen", side_effect=failing_urlopen):
        fetch_uswds_guidance(url)
        fetch_uswds_guidance(url)

    assert call_count == 1


def test_fetch_returns_none_on_missing_guidance_section():
    clear_cache()
    bad_html = b"<html><body><p>No guidance section here</p></body></html>"
    with _patch("django_cotton_uswds.mcp.fetcher.urlopen") as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = bad_html
        result = fetch_uswds_guidance(
            "https://designsystem.digital.gov/components/alert/"
        )
    assert result is None
