from demo_app.views import (
    COMPONENTS,
)
from django.urls import include, path
from django_distill import distill_re_path
from pattern_library import get_pattern_template_suffix
from pattern_library import views as pl_views
from pattern_library.utils import TemplateRenderer


def no_params():
    return None


def all_component_slugs():
    for slug, _, _ in COMPONENTS:
        if slug == "form-renderer":
            continue
        yield {"slug": slug}


def all_pattern_templates():
    def extract(node):
        for t in node.get("templates_stored", []):
            yield {"pattern_template_name": t.origin.template_name}
        for group in node.get("template_groups", {}).values():
            yield from extract(group)

    yield from extract(TemplateRenderer.get_pattern_templates())


_suffix = get_pattern_template_suffix()


urlpatterns = [
    distill_re_path(
        r"^static-site/",
        pl_views.IndexView.as_view(),
        name="pattern_library:index",
        distill_func=no_params,
    ),
    distill_re_path(
        rf"^static-site/pattern/(?P<pattern_template_name>[\w./\-\\]+{_suffix})$",
        pl_views.IndexView.as_view(),
        name="pattern_library:display_pattern",
        distill_func=all_pattern_templates,
    ),
    distill_re_path(
        rf"^static-site/render-pattern/"
        rf"(?P<pattern_template_name>[\w./\-\\]+{_suffix})$",
        pl_views.RenderPatternView.as_view(),
        name="pattern_library:render_pattern",
        distill_func=all_pattern_templates,
    ),
    path("", include("pattern_library.urls")),
]
