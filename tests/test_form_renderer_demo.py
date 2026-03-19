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

    def test_form_covers_all_widget_types(self):
        from demo_app.forms import DemoForm

        form = DemoForm()
        field_widgets = {
            name: type(field.widget).__name__ for name, field in form.fields.items()
        }

        widget_types = set(field_widgets.values())
        assert "TextInput" in widget_types
        assert "EmailInput" in widget_types
        assert "Textarea" in widget_types
        assert "CheckboxInput" in widget_types
        assert "Select" in widget_types
        assert "RadioSelect" in widget_types
        assert "CheckboxSelectMultiple" in widget_types
        assert "ClearableFileInput" in widget_types

    def test_form_has_required_and_optional_fields(self):
        from demo_app.forms import DemoForm

        form = DemoForm()
        required = [n for n, f in form.fields.items() if f.required]
        optional = [n for n, f in form.fields.items() if not f.required]
        assert len(required) >= 1
        assert len(optional) >= 1

    def test_form_has_help_text(self):
        from demo_app.forms import DemoForm

        form = DemoForm()
        fields_with_help = [n for n, f in form.fields.items() if f.help_text]
        assert len(fields_with_help) >= 1

    def test_form_has_width_attr(self):
        from demo_app.forms import DemoForm

        form = DemoForm()
        has_width = any(f.widget.attrs.get("width") for f in form.fields.values())
        assert has_width


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

    def test_valid_post_redirects_with_success_param(self):
        from demo_app.views import FormRendererView

        factory = RequestFactory()
        request = factory.post(
            "/components/form-renderer/",
            data={
                "name": "Jane Doe",
                "email": "jane@example.com",
                "message": "Hello",
                "reason": "question",
                "contact_method": "email",
            },
        )
        response = FormRendererView.as_view()(request)

        assert response.status_code == 302
        assert response.url == "/components/form-renderer/?success=1"

    def test_get_with_success_param_includes_success_in_context(self):
        from demo_app.views import FormRendererView

        factory = RequestFactory()
        request = factory.get("/components/form-renderer/?success=1")
        response = FormRendererView.as_view()(request)

        assert response.status_code == 200
        assert response.context_data["success"] is True

    def test_get_without_success_param_has_no_success_in_context(self):
        from demo_app.views import FormRendererView

        factory = RequestFactory()
        request = factory.get("/components/form-renderer/")
        response = FormRendererView.as_view()(request)

        assert response.status_code == 200
        assert response.context_data.get("success") is not True

    def test_success_alert_rendered_on_success(self):
        from demo_app.views import FormRendererView

        factory = RequestFactory()
        request = factory.get("/components/form-renderer/?success=1")
        response = FormRendererView.as_view()(request)
        response.render()
        content = response.content.decode()

        assert "usa-alert--success" in content
        assert "submitted successfully" in content

    def test_form_has_multipart_enctype(self):
        from demo_app.views import FormRendererView

        factory = RequestFactory()
        request = factory.get("/components/form-renderer/")
        response = FormRendererView.as_view()(request)
        response.render()
        content = response.content.decode()

        assert 'enctype="multipart/form-data"' in content

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

    def test_post_with_partial_data_preserves_values(self):
        from demo_app.views import FormRendererView

        factory = RequestFactory()
        request = factory.post(
            "/components/form-renderer/",
            data={
                "name": "Jane Doe",
                "email": "",  # missing required field
                "message": "Some message",
                "reason": "feedback",
                "contact_method": "phone",
            },
        )
        response = FormRendererView.as_view()(request)

        assert response.status_code == 200
        form = response.context_data["form"]
        assert form.errors
        assert "email" in form.errors
        # Submitted values are preserved
        assert form["name"].value() == "Jane Doe"
        assert form["message"].value() == "Some message"
        assert form["reason"].value() == "feedback"
        assert form["contact_method"].value() == "phone"

    def test_no_success_alert_on_normal_get(self):
        from demo_app.views import FormRendererView

        factory = RequestFactory()
        request = factory.get("/components/form-renderer/")
        response = FormRendererView.as_view()(request)
        response.render()
        content = response.content.decode()

        assert "usa-alert--success" not in content
