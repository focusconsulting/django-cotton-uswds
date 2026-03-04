from django_distill import distill_path

from demo_app.views import COMPONENTS, ComponentIndexView, ComponentView, IndexView


def no_params():
    return None


def all_component_slugs():
    for slug, _, _ in COMPONENTS:
        yield {"slug": slug}


urlpatterns = [
    distill_path("", IndexView.as_view(), name="index", distill_func=no_params),
    distill_path(
        "components/",
        ComponentIndexView.as_view(),
        name="component-index",
        distill_func=no_params,
    ),
    distill_path(
        "components/<slug:slug>/",
        ComponentView.as_view(),
        name="component-detail",
        distill_func=all_component_slugs,
    ),
]
