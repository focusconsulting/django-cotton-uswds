import os

SECRET_KEY = "test-secret-key"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = [
    "django_cotton",
    "django_cotton_uswds",
    "demo_app",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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
    },
]

DATABASES = {}
