"""
Tests for accessibility fixes bundled for CORE-57:

* CORE-288 — the required-marker asterisk is hidden from assistive tech so it
  is not read aloud as "star"; the required state is conveyed by the control's
  own ``required`` attribute instead.
* CORE-289 — ``c-alert`` and ``c-accordion-item`` accept a ``heading_level`` so
  the heading element matches the surrounding page hierarchy (no skipped
  levels). The default preserves the previous ``<h4>`` output.
"""

from django.template.loader import render_to_string


class TestRequiredMarker:
    def test_asterisk_hidden_from_assistive_tech(self):
        html = render_to_string("required_marker.html")
        assert 'aria-hidden="true"' in html
        assert ">*</abbr>" in html


class TestAlertHeadingLevel:
    def test_default_heading_level_is_h4(self):
        html = render_to_string("alert_heading_default.html")
        assert '<h4 class="usa-alert__heading">Heads up</h4>' in html

    def test_heading_level_prop_sets_heading_element(self):
        html = render_to_string("alert_heading_level.html")
        assert '<h2 class="usa-alert__heading">Heads up</h2>' in html
        assert "<h4" not in html


class TestAccordionItemHeadingLevel:
    def test_default_heading_level_is_h4(self):
        html = render_to_string("accordion_item_heading_default.html")
        assert '<h4 class="usa-accordion__heading">' in html

    def test_heading_level_prop_sets_heading_element(self):
        html = render_to_string("accordion_item_heading_level.html")
        assert '<h3 class="usa-accordion__heading">' in html
        assert "</h3>" in html
        assert "<h4" not in html
