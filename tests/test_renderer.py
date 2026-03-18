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

    def test_required_boolean_field_shows_required_marker(self):
        class RequiredCheckboxForm(forms.Form):
            agree = forms.BooleanField(label="I agree")

        form = RequiredCheckboxForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-hint--required" in html

    def test_boolean_field_help_text_renders_as_description(self):
        class CheckboxHelpForm(forms.Form):
            agree = forms.BooleanField(
                label="I agree",
                help_text="You must agree to continue",
            )

        form = CheckboxHelpForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "You must agree to continue" in html

    def test_textarea_widget_renders_as_textarea(self):
        class TextareaForm(forms.Form):
            bio = forms.CharField(label="Biography", widget=forms.Textarea)

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-textarea" in html

    def test_choice_field_renders_as_uswds_select(self):
        class SelectForm(forms.Form):
            color = forms.ChoiceField(
                label="Favorite color",
                choices=[("r", "Red"), ("g", "Green"), ("b", "Blue")],
            )

        form = SelectForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-select" in html
        assert "<option" in html
        assert 'value="r"' in html
        assert "Red" in html
        assert 'value="g"' in html
        assert 'value="b"' in html

    def test_choice_field_passes_through_attributes(self):
        class SelectForm(forms.Form):
            color = forms.ChoiceField(
                label="Color",
                choices=[("r", "Red")],
            )

        form = SelectForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert 'name="color"' in html
        assert 'id="id_color"' in html
        assert "required" in html

    def test_disabled_choice_field_renders_disabled(self):
        class DisabledSelectForm(forms.Form):
            color = forms.ChoiceField(
                label="Color",
                choices=[("r", "Red")],
                disabled=True,
            )

        form = DisabledSelectForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "disabled" in html

    def test_file_field_renders_as_uswds_file_input(self):
        class FileForm(forms.Form):
            document = forms.FileField(label="Upload document")

        form = FileForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-file-input" in html
        assert 'name="document"' in html
        assert 'id="id_document"' in html

    def test_disabled_file_field_renders_disabled(self):
        class DisabledFileForm(forms.Form):
            document = forms.FileField(label="Upload", disabled=True)

        form = DisabledFileForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-file-input" in html
        assert "disabled" in html

    def test_grouped_choices_render_optgroups(self):
        class GroupedSelectForm(forms.Form):
            color = forms.ChoiceField(
                label="Color",
                choices=[
                    ("Warm", [("r", "Red"), ("o", "Orange")]),
                    ("Cool", [("b", "Blue"), ("g", "Green")]),
                ],
            )

        form = GroupedSelectForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert '<optgroup label="Warm">' in html
        assert '<optgroup label="Cool">' in html
        assert "</optgroup>" in html

    def test_file_field_passes_through_accept_attribute(self):
        class AcceptFileForm(forms.Form):
            document = forms.FileField(
                label="Upload",
                widget=forms.ClearableFileInput(attrs={"accept": ".pdf,.doc"}),
            )

        form = AcceptFileForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert 'accept=".pdf,.doc"' in html

    def test_choice_field_preserves_selected_value(self):
        class SelectForm(forms.Form):
            color = forms.ChoiceField(
                label="Color",
                choices=[("r", "Red"), ("g", "Green"), ("b", "Blue")],
            )

        form = SelectForm(
            data={"color": "g"},
            renderer=USWDSFormRenderer(),
        )
        form.is_valid()
        html = form.render()

        assert 'value="g" selected' in html
        assert 'value="r" selected' not in html


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


class TestGlobalFormRendererSetting:
    def test_form_renderer_setting_activates_uswds_rendering(self, settings):
        settings.FORM_RENDERER = "django_cotton_uswds.renderer.USWDSFormRenderer"

        form = SimpleForm()
        html = form.render()

        assert "usa-form-group" in html
        assert "usa-label" in html
        assert "usa-input" in html


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
