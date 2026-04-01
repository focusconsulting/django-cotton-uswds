from django import forms

from django_cotton_uswds.renderer import USWDSFormRenderer


class TestTextArea:
    def test_textarea_renders_with_uswds_class(self):
        class TextareaForm(forms.Form):
            comments = forms.CharField(
                label="Additional comments", widget=forms.Textarea
            )

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-textarea" in html

    def test_textarea_renders_value_in_body(self):
        class TextareaForm(forms.Form):
            description = forms.CharField(
                label="Project description", widget=forms.Textarea
            )

        form = TextareaForm(
            data={"description": "This is my project description."},
            renderer=USWDSFormRenderer(),
        )
        form.is_valid()
        html = form.render()

        assert "This is my project description." in html

    def test_textarea_help_text_renders_as_hint(self):
        class TextareaForm(forms.Form):
            appeal = forms.CharField(
                label="Reason for appeal",
                help_text="Provide specific details about why you are appealing",
                widget=forms.Textarea,
            )

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-hint" in html
        assert "Provide specific details about why you are appealing" in html

    def test_textarea_with_maxlength_renders_character_count_wrapper(self):
        class TextareaForm(forms.Form):
            description = forms.CharField(
                label="Short description",
                widget=forms.Textarea(attrs={"maxlength": "10"}),
            )

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-character-count" in html
        assert 'data-maxlength="10"' in html

    def test_textarea_with_maxlength_renders_character_count_message(self):
        class TextareaForm(forms.Form):
            description = forms.CharField(
                label="Short description",
                widget=forms.Textarea(attrs={"maxlength": "25"}),
            )

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "25 characters allowed" in html

    def test_textarea_with_maxlength_renders_character_count_field_class(self):
        class TextareaForm(forms.Form):
            description = forms.CharField(
                label="Short description",
                widget=forms.Textarea(attrs={"maxlength": "10"}),
            )

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-character-count__field" in html

    def test_textarea_without_maxlength_has_no_character_count(self):
        class TextareaForm(forms.Form):
            comments = forms.CharField(label="Comments", widget=forms.Textarea)

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-character-count" not in html

    def test_textarea_with_rows_renders_rows_attribute(self):
        class TextareaForm(forms.Form):
            summary = forms.CharField(
                label="Brief summary",
                widget=forms.Textarea(attrs={"rows": "3"}),
            )

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert 'rows="3"' in html

    def test_textarea_required_renders_required_attribute(self):
        class TextareaForm(forms.Form):
            statement = forms.CharField(
                label="Statement of purpose", widget=forms.Textarea
            )

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "required" in html

    def test_textarea_required_shows_required_marker(self):
        class TextareaForm(forms.Form):
            statement = forms.CharField(
                label="Statement of purpose", widget=forms.Textarea
            )

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-hint--required" in html

    def test_textarea_optional_has_no_required_marker(self):
        class TextareaForm(forms.Form):
            notes = forms.CharField(
                label="Additional notes", widget=forms.Textarea, required=False
            )

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "usa-hint--required" not in html

    def test_textarea_disabled_renders_disabled_attribute(self):
        class TextareaForm(forms.Form):
            previous = forms.CharField(
                label="Previous submission", widget=forms.Textarea, disabled=True
            )

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert "disabled" in html

    def test_textarea_error_state_renders_error_classes(self):
        class TextareaForm(forms.Form):
            justification = forms.CharField(
                label="Justification", widget=forms.Textarea, min_length=50
            )

        form = TextareaForm(
            data={"justification": "too short"}, renderer=USWDSFormRenderer()
        )
        form.is_valid()
        html = form.render()

        assert "usa-error-message" in html
        assert "usa-form-group--error" in html

    def test_textarea_empty_required_field_shows_error(self):
        class TextareaForm(forms.Form):
            comments = forms.CharField(label="Comments", widget=forms.Textarea)

        form = TextareaForm(data={}, renderer=USWDSFormRenderer())
        form.is_valid()
        html = form.render()

        assert "usa-error-message" in html
        assert "usa-form-group--error" in html

    def test_textarea_passes_through_id_and_name(self):
        class TextareaForm(forms.Form):
            comments = forms.CharField(label="Comments", widget=forms.Textarea)

        form = TextareaForm(renderer=USWDSFormRenderer())
        html = form.render()

        assert 'name="comments"' in html
        assert 'id="id_comments"' in html
