from django.conf import settings


def pytest_configure():
    # Add tests/templates to DIRS so fixture templates can use cotton components.
    for backend in settings.TEMPLATES:
        if backend["BACKEND"] == "django.template.backends.django.DjangoTemplates":
            import os

            tests_dir = os.path.dirname(__file__)
            backend["DIRS"].append(os.path.join(tests_dir, "templates"))
            break
