from django_distill import distill_path

from demo_app.views import DemoView, IndexView


def no_params():
    return None


urlpatterns = [
    distill_path("", IndexView.as_view(), name="index", distill_func=no_params),
    distill_path(
        "demo/", DemoView.as_view(), name="demo", distill_func=no_params
    ),
]
