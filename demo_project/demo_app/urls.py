from demo_app.views import (
    COMPONENTS,
    ComponentIndexView,
    ComponentView,
    FormRendererView,
)
from django_distill import distill_path


def no_params():
    return None


def all_component_slugs():
    for slug, _, _ in COMPONENTS:
        if slug == "form-renderer":
            continue
        yield {"slug": slug}


urlpatterns = [
    distill_path(
        "", ComponentIndexView.as_view(), name="index", distill_func=no_params
    ),
    distill_path(
        "components/form-renderer/",
        FormRendererView.as_view(),
        name="form-renderer",
        distill_func=no_params,
    ),
    distill_path(
        "components/<slug:slug>/",
        ComponentView.as_view(),
        name="component-detail",
        distill_func=all_component_slugs,
    ),
]
