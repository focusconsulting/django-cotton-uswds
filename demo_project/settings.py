import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = "demo-secret-key-not-for-production"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "django_cotton",
    "django_cotton_uswds",
    "pattern_library",
    "demo_app",
    "django_distill",
]

MIDDLEWARE = [
    "demo_app.middleware.URLPrefixMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "OPTIONS": {
            "loaders": [
                "django_cotton.cotton_loader.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.request",
                "django.template.context_processors.static",
            ],
            "builtins": [
                "pattern_library.loader_tags",
                "django_cotton.templatetags.cotton",
            ],
        },
    },
]

PATTERN_LIBRARY = {
    "SECTIONS": (
        ("Components", ["patterns/components"]),
        ("Pages", ["patterns/pages"]),
    ),
    "TEMPLATE_SUFFIX": ".html",
    "PATTERN_BASE_TEMPLATE_NAME": "patterns/base.html",
}

WSGI_APPLICATION = "wsgi.application"

DATABASES = {}

URL_PREFIX = os.environ.get("URL_PREFIX", "")

STATIC_URL = os.environ.get("STATIC_URL", "static/")
STATIC_ROOT = BASE_DIR / "staticfiles"

DISTILL_DIR = BASE_DIR / "dist"
