from django.template.loader import render_to_string


class TestBreadcrumbRendersUSWDSStructure:
    def test_renders_nav_with_breadcrumb_class(self):
        html = render_to_string("test_breadcrumb_current_page.html")

        assert "<nav" in html
        assert "usa-breadcrumb" in html
        assert "usa-breadcrumb__list" in html
        assert "<ol" in html


class TestBreadcrumbItemCurrentPage:
    def test_current_page_renders_as_plain_text_not_link(self):
        html = render_to_string("test_breadcrumb_current_page.html")

        # The current page item should have aria-current and usa-current class
        assert 'aria-current="page"' in html
        assert "usa-current" in html
        # The current page text should appear
        assert "Current Page" in html
        # The current page item should NOT be a link
        # Count anchor tags - only the "Home" link should exist
        assert html.count("usa-breadcrumb__link") == 1


class TestBreadcrumbSupportsMultipleItems:
    def test_renders_arbitrary_number_of_items(self):
        html = render_to_string("test_breadcrumb_multiple_items.html")

        # All 5 items should be rendered as list items
        assert html.count("usa-breadcrumb__list-item") == 5
        # First 4 items should be links, last one should be current page
        assert html.count("usa-breadcrumb__link") == 4
        # Each linked item text should appear
        assert "Home" in html
        assert "Services" in html
        assert "Benefits" in html
        assert "Apply" in html
        # Current page should be plain text
        assert "Confirmation" in html
        assert html.count("usa-current") == 1


class TestBreadcrumbWrappedVariant:
    def test_default_breadcrumb_does_not_have_wrap_class(self):
        html = render_to_string("test_breadcrumb_current_page.html")

        assert "usa-breadcrumb--wrap" not in html

    def test_wrapped_breadcrumb_has_wrap_class(self):
        html = render_to_string("test_breadcrumb_wrapped.html")

        assert "usa-breadcrumb--wrap" in html
