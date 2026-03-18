from pathlib import Path

import django.forms
from django.forms.renderers import DjangoTemplates
from django.utils.functional import cached_property


class USWDSFormRenderer(DjangoTemplates):
    form_template_name = "django/forms/uswds/form.html"

    @cached_property
    def engine(self):
        return self.backend(
            {
                "APP_DIRS": False,
                "DIRS": [
                    Path(__file__).parent / "templates",
                    Path(django.forms.__file__).parent / self.backend.app_dirname,
                ],
                "NAME": "uswds-forms",
                "OPTIONS": {
                    "loaders": [
                        "django_cotton.cotton_loader.Loader",
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ],
                    "builtins": [
                        "django_cotton.templatetags.cotton",
                    ],
                },
            }
        )
