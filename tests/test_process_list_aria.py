"""
Tests for the process list accessibility props.

``c-process_list`` passes undeclared attributes through to its ``<ol>`` so the
list can carry an accessible name, and ``c-process_list.item`` accepts a
``screen_reader_text`` that composes into the heading's accessible name
(rather than replacing it, the way an ``aria-label`` would).
"""

from django.template.loader import render_to_string


class TestProcessListDefaults:
    def test_no_extra_attributes_rendered_by_default(self):
        html = render_to_string("process_list_default.html")
        assert 'class="usa-process-list ' in html
        assert "aria-label" not in html
        assert "usa-sr-only" not in html
        assert '<h4 class="usa-process-list__heading ">Start a process</h4>' in html


class TestProcessListAttrsPassthrough:
    def test_wrapper_accepts_aria_label(self):
        html = render_to_string("process_list_aria.html")
        assert 'aria-label="Process steps"' in html

    def test_item_accepts_arbitrary_attributes(self):
        html = render_to_string("process_list_aria.html")
        assert 'data-step="1"' in html


class TestProcessListScreenReaderText:
    def test_screen_reader_text_renders_inside_heading_before_the_text(self):
        html = render_to_string("process_list_aria.html")
        assert (
            '<h4 class="usa-process-list__heading ">'
            '<span class="usa-sr-only">Step 1 of 3: </span>'
            "Start a process</h4>"
        ) in html
