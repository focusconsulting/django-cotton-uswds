from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "demo_app/index.html"


class DemoView(TemplateView):
    template_name = "demo_app/demo.html"
