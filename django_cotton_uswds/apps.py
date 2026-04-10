import logging
from functools import partial
from django.apps import AppConfig


logger = logging.getLogger(__name__)


class DjangoCottonUswdsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_cotton_uswds"
    verbose_name = "Django Cotton USWDS Components"

    def ready(self):
        """Ready is defined in order to add extra extensions to the markdown
        call in the pattern_library app."""

        try:
            import markdown
            from pattern_library import utils

            utils.markdown.markdown = partial(
                markdown.markdown,
                extensions=[
                    "extra",
                ],
            )
        except ImportError:
            logger.warn("Import error when loading the USWDS component library.")
