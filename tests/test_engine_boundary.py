"""Boundary tests for the renderer engine's wiring invariants.

These tests verify the engine's public contract — they should survive
internal refactors as long as external behavior is preserved.
"""

from django_cotton_uswds import USWDSFormRenderer


class TestEngineProducedWithNoArguments:
    def test_renderer_creates_engine_without_arguments(self):
        renderer = USWDSFormRenderer()
        engine = renderer.engine

        assert engine is not None


class TestCottonLoaderIsFirst:
    def test_cotton_loader_is_first_in_loader_chain(self):
        renderer = USWDSFormRenderer()
        engine = renderer.engine
        loaders = engine.engine.template_loaders

        first_loader = loaders[0]
        assert type(first_loader).__module__ == "django_cotton.cotton_loader"


class TestEngineResolvesPackageTemplates:
    def test_resolves_uswds_form_template(self):
        renderer = USWDSFormRenderer()
        engine = renderer.engine
        template = engine.get_template("django/forms/uswds/form.html")

        assert template is not None

    def test_resolves_uswds_widget_template(self):
        renderer = USWDSFormRenderer()
        engine = renderer.engine
        template = engine.get_template(
            "django/forms/widgets/input.html"
        )

        assert template is not None


class TestEngineResolvesDjangoBuiltinTemplates:
    def test_resolves_django_div_form_template(self):
        renderer = USWDSFormRenderer()
        engine = renderer.engine
        template = engine.get_template("django/forms/div.html")

        assert template is not None

    def test_resolves_django_field_template(self):
        renderer = USWDSFormRenderer()
        engine = renderer.engine
        template = engine.get_template("django/forms/field.html")

        assert template is not None


class TestCottonBuiltinsRegistered:
    def test_engine_has_cotton_tags_in_builtins(self):
        renderer = USWDSFormRenderer()
        engine = renderer.engine
        all_builtin_tags = set()
        for lib in engine.engine.template_builtins:
            all_builtin_tags.update(lib.tags.keys())

        assert "cotton" in all_builtin_tags

    def test_engine_renders_cotton_syntax_without_load(self):
        """The engine can process <c-*> tags without {% load cotton %}."""
        from django import forms

        class TestForm(forms.Form):
            name = forms.CharField(label="Name")

        renderer = USWDSFormRenderer()
        form = TestForm(renderer=renderer)
        html = form.render()

        # If Cotton builtins weren't registered, rendering would fail
        # or produce raw <c-*> tags in output instead of USWDS markup
        assert "usa-form-group" in html
