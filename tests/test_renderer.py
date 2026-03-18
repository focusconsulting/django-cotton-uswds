from django import forms

from django_cotton_uswds.renderer import USWDSFormRenderer


class SimpleForm(forms.Form):
    name = forms.CharField(label="Full name")


class TestCharFieldRendersUSWDSStructure:
    def test_charfield_renders_with_form_group_label_and_input(self):
        form = SimpleForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-form-group" in html
        assert "usa-label" in html
        assert "usa-input" in html

    def test_help_text_renders_as_hint(self):
        class HelpTextForm(forms.Form):
            name = forms.CharField(
                label="Full name",
                help_text="Enter your first and last name",
            )

        form = HelpTextForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-hint" in html
        assert "Enter your first and last name" in html

    def test_required_field_shows_marker_and_attribute(self):
        form = SimpleForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-hint--required" in html
        assert "required" in html

    def test_optional_field_has_no_required_marker(self):
        class OptionalForm(forms.Form):
            name = forms.CharField(label="Nickname", required=False)

        form = OptionalForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-hint--required" not in html

    def test_field_errors_render_as_error_message_with_error_state(self):
        form = SimpleForm(data={}, renderer=USWDSFormRenderer())
        form.is_valid()
        html = form.render()

        assert "usa-error-message" in html
        assert "usa-form-group--error" in html

    def test_non_field_errors_render_as_alert(self):
        class ValidatedForm(forms.Form):
            name = forms.CharField()

            def clean(self):
                raise forms.ValidationError("Something went wrong overall")

        form = ValidatedForm(data={"name": "test"}, renderer=USWDSFormRenderer())
        form.is_valid()
        html = form.render()

        assert "usa-alert--error" in html
        assert "Something went wrong overall" in html

    def test_email_field_renders_with_type_email(self):
        class EmailForm(forms.Form):
            email = forms.EmailField(label="Email address")

        form = EmailForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert 'type="email"' in html
        assert "usa-input" in html

    def test_boolean_field_renders_as_checkbox(self):
        class CheckboxForm(forms.Form):
            agree = forms.BooleanField(label="I agree")

        form = CheckboxForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-checkbox" in html

    def test_textarea_widget_renders_as_textarea(self):
        class TextareaForm(forms.Form):
            bio = forms.CharField(label="Biography", widget=forms.Textarea)

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-textarea" in html


class TestFormRoundTrip:
    def test_submitted_form_preserves_values_and_shows_errors(self):
        class ProfileForm(forms.Form):
            name = forms.CharField(label="Full name", min_length=3)
            email = forms.EmailField(label="Email")

        form = ProfileForm(
            data={"name": "Al", "email": "bad"},
            renderer=USWDSFormRenderer(),
        )
        form.is_valid()
        html = form.render()

        # Values preserved
        assert 'value="Al"' in html
        assert 'value="bad"' in html
        # Errors shown
        assert "usa-error-message" in html
        assert "usa-form-group--error" in html


class TestUSWDSFormMixin:
    def test_mixin_renders_uswds_structure(self):
        from django_cotton_uswds.mixins import USWDSFormMixin

        class MixinForm(USWDSFormMixin, forms.Form):
            name = forms.CharField(label="Full name")

        form = MixinForm()
        html = form.render()

        assert "usa-form-group" in html
        assert "usa-label" in html
        assert "usa-input" in html
