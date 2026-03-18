SECRET_KEY = "test-secret-key"

INSTALLED_APPS = [
    "django_cotton",
    "django_cotton_uswds",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "OPTIONS": {
            "loaders": [
                "django_cotton.cotton_loader.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "builtins": [
                "django_cotton.templatetags.cotton",
            ],
        },
    },
]

DATABASES = {}
