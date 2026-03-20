"""Tests for the cotton_aliases deprecation."""

import importlib
import warnings


class TestCottonAliasesDeprecation:
    def test_importing_cotton_aliases_emits_deprecation_warning(self):
        import django_cotton_uswds.templatetags.cotton_aliases as mod

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            importlib.reload(mod)

        deprecation_warnings = [
            w for w in caught if issubclass(w.category, DeprecationWarning)
        ]
        assert len(deprecation_warnings) == 1

    def test_deprecation_message_mentions_django_cotton_docs(self):
        import django_cotton_uswds.templatetags.cotton_aliases as mod

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            importlib.reload(mod)

        deprecation_warnings = [
            w for w in caught if issubclass(w.category, DeprecationWarning)
        ]
        msg = str(deprecation_warnings[0].message)
        assert "django-cotton" in msg.lower()

    def test_cotton_aliases_still_exposes_register(self):
        import django_cotton_uswds.templatetags.cotton_aliases as mod

        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            importlib.reload(mod)

        assert hasattr(mod, "register")
