"""
Tests for c-text_input aria-describedby wiring.

These tests render fixture templates that use the component directly
(with explicit props) to verify the aria-describedby output logic in
isolation from Django's form renderer.
"""

from django.template.loader import render_to_string


class TestTextInputAriaDescribedBy:
    def test_hint_prop_emits_aria_describedby_pointing_at_hint_element(self):
        html = render_to_string("text_input_hint.html")
        assert 'aria-describedby="id_test-hint"' in html

    def test_aria_describedby_prop_forwarded_to_input(self):
        html = render_to_string("text_input_aria.html")
        assert 'aria-describedby="custom-id"' in html

    def test_error_takes_precedence_and_includes_hint(self):
        html = render_to_string("text_input_error_hint.html")
        assert 'aria-describedby="id_test-error-message id_test-hint"' in html

    def test_no_hint_omits_aria_describedby(self):
        html = render_to_string("text_input_no_hint.html")
        assert "aria-describedby" not in html
