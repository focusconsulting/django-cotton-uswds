from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = "demo-secret-key-not-for-production"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "django_cotton",
    "django_cotton_uswds",
    "django_distill",
    "demo_app",
]

MIDDLEWARE = [
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
                "django_cotton.templatetags.cotton",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"

DATABASES = {}

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DISTILL_DIR = BASE_DIR / "dist"
