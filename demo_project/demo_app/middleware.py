from django.conf import settings
from django.urls import set_script_prefix


class URLPrefixMiddleware:
    """Set the URL script prefix only during request handling.

    This ensures {% url %} tags in templates produce prefixed URLs
    (e.g., /django-cotton-uswds/components/) when URL_PREFIX is set,
    without affecting django-distill's file path generation. The prefix
    is reset after each request to avoid leaking into non-request code.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        prefix = getattr(settings, "URL_PREFIX", "")
        if prefix:
            set_script_prefix(prefix)
        response = self.get_response(request)
        if prefix:
            set_script_prefix("/")
        return response
