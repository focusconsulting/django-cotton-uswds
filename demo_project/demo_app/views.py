from django.http import Http404
from django.views.generic import TemplateView


COMPONENTS = [
    # Content
    ("alert", "Alert", "Content"),
    ("button", "Button", "Content"),
    ("button-group", "Button Group", "Content"),
    ("card", "Card", "Content"),
    ("collection", "Collection", "Content"),
    ("list", "List", "Content"),
    ("prose", "Prose", "Content"),
    ("summary-box", "Summary Box", "Content"),
    ("table", "Table", "Content"),
    ("tag", "Tag", "Content"),
    # Navigation
    ("banner", "Banner", "Navigation"),
    ("breadcrumb", "Breadcrumb", "Navigation"),
    ("footer", "Footer", "Navigation"),
    ("header", "Header", "Navigation"),
    ("identifier", "Identifier", "Navigation"),
    ("in-page-nav", "In-Page Navigation", "Navigation"),
    ("pagination", "Pagination", "Navigation"),
    ("side-nav", "Side Navigation", "Navigation"),
    # Forms
    ("character-count", "Character Count", "Forms"),
    ("checkbox", "Checkbox", "Forms"),
    ("combo-box", "Combo Box", "Forms"),
    ("currency-input", "Currency Input", "Forms"),
    ("date-picker", "Date Picker", "Forms"),
    ("date-range-picker", "Date Range Picker", "Forms"),
    ("error-message", "Error Message", "Forms"),
    ("fieldset", "Fieldset", "Forms"),
    ("file-input", "File Input", "Forms"),
    ("form", "Form", "Forms"),
    ("form-group", "Form Group", "Forms"),
    ("input-group", "Input Group", "Forms"),
    ("input-mask", "Input Mask", "Forms"),
    ("input-prefix", "Input Prefix", "Forms"),
    ("input-suffix", "Input Suffix", "Forms"),
    ("label", "Label", "Forms"),
    ("memorable-date", "Memorable Date", "Forms"),
    ("radio-button", "Radio Button", "Forms"),
    ("range-slider", "Range Slider", "Forms"),
    ("select", "Select", "Forms"),
    ("text-input", "Text Input", "Forms"),
    ("textarea", "Textarea", "Forms"),
    ("time-picker", "Time Picker", "Forms"),
    # Interactive
    ("accordion", "Accordion", "Interactive"),
    ("modal", "Modal", "Interactive"),
    ("step-indicator", "Step Indicator", "Interactive"),
    ("tooltip", "Tooltip", "Interactive"),
    # Other
    ("icon", "Icon", "Other"),
    ("icon-list", "Icon List", "Other"),
    ("link", "Link", "Other"),
    ("process-list", "Process List", "Other"),
    ("search", "Search", "Other"),
    ("site-alert", "Site Alert", "Other"),
]

CATEGORY_ORDER = ["Content", "Navigation", "Forms", "Interactive", "Other"]


def get_components_by_category():
    grouped = {}
    for slug, name, category in COMPONENTS:
        grouped.setdefault(category, []).append({"slug": slug, "name": name})
    return [(cat, grouped.get(cat, [])) for cat in CATEGORY_ORDER if cat in grouped]


class IndexView(TemplateView):
    template_name = "demo_app/index.html"


class ComponentIndexView(TemplateView):
    template_name = "demo_app/component_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["components_by_category"] = get_components_by_category()
        return context


class ComponentView(TemplateView):
    def get_template_names(self):
        slug = self.kwargs["slug"]
        valid_slugs = {s for s, _, _ in COMPONENTS}
        if slug not in valid_slugs:
            raise Http404(f"Component '{slug}' not found")
        template_name = slug.replace("-", "_")
        return [f"demo_app/components/{template_name}.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]
        for s, name, category in COMPONENTS:
            if s == slug:
                context["component_name"] = name
                context["component_slug"] = slug
                context["component_category"] = category
                break
        context["components_by_category"] = get_components_by_category()
        return context
