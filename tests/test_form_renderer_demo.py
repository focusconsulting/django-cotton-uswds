from django import forms
from django.test import RequestFactory

from django_cotton_uswds.mixins import USWDSFormMixin


class TestDemoForm:
    def test_form_uses_uswds_mixin_and_has_expected_fields(self):
        from demo_app.forms import DemoForm

        assert issubclass(DemoForm, USWDSFormMixin)
        assert issubclass(DemoForm, forms.Form)

        form = DemoForm()
        assert "name" in form.fields
        assert "email" in form.fields
        assert "reason" in form.fields


class TestFormRendererView:
    def test_get_returns_200_with_form_in_context(self):
        from demo_app.forms import DemoForm
        from demo_app.views import FormRendererView

        factory = RequestFactory()
        request = factory.get("/components/form-renderer/")
        response = FormRendererView.as_view()(request)

        assert response.status_code == 200
        assert isinstance(response.context_data["form"], DemoForm)

    def test_component_registered_in_components_list(self):
        from demo_app.views import COMPONENTS

        entry = ("form-renderer", "Form Renderer", "Forms")
        assert entry in COMPONENTS

    def test_post_with_invalid_data_returns_form_with_errors(self):
        from demo_app.views import FormRendererView

        factory = RequestFactory()
        request = factory.post("/components/form-renderer/", data={})
        response = FormRendererView.as_view()(request)

        assert response.status_code == 200
        form = response.context_data["form"]
        assert form.errors
        assert "name" in form.errors
        assert "email" in form.errors
