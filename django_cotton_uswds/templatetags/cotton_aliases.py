"""Deprecated alias module — kept for backward compatibility only.

The USWDS form renderer now registers Cotton builtins internally.
For project-level templates, add ``django_cotton.templatetags.cotton``
directly to your ``TEMPLATES`` builtins instead.

See the django-cotton docs: https://django-cotton.com/
"""

import contextlib
import warnings

warnings.warn(
    "django_cotton_uswds.templatetags.cotton_aliases is deprecated. "
    "The USWDS form renderer registers Cotton builtins automatically. "
    "For project templates, use 'django_cotton.templatetags.cotton' "
    "directly in your TEMPLATES builtins. "
    "See the django-cotton docs: https://django-cotton.com/",
    DeprecationWarning,
    stacklevel=2,
)

from django_cotton.templatetags import cotton  # noqa: F401, E402

with contextlib.suppress(Exception):
    register = cotton.register
