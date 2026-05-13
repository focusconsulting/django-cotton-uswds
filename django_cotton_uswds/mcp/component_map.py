USWDS_BASE_URL = "https://designsystem.digital.gov/components"

# Maps local component directory name → USWDS URL slug.
# None means the component is a custom extension with no dedicated USWDS page.
COMPONENT_USWDS_SLUGS: dict[str, str | None] = {
    "accordion": "accordion",
    "alert": "alert",
    "banner": "banner",
    "breadcrumb": "breadcrumb",
    "button": "button",
    "button_group": "button-group",
    "card": "card",
    "character_count": "character-count",
    "checkbox": "checkbox",
    "collection": "collection",
    "combo_box": "combo-box",
    "currency_input": None,  # custom component, no USWDS page
    "date_picker": "date-picker",
    "date_range_picker": "date-range-picker",
    "file_input": "file-input",
    "footer": "footer",
    "form": "form",
    "header": "header",
    "icon": "icon",
    "icon_list": "icon-list",
    "identifier": "identifier",
    "in_page_nav": "in-page-navigation",
    "input_group": None,  # custom component, no USWDS page
    "input_prefix": "input-prefix-suffix",
    "input_suffix": "input-prefix-suffix",  # shares a page with input_prefix
    "label": None,  # part of form, no standalone USWDS page
    "link": "link",
    "list": "list",
    "memorable_date": "memorable-date",
    "modal": "modal",
    "pagination": "pagination",
    "process_list": "process-list",
    "prose": "prose",
    "radio_button": "radio-buttons",  # USWDS uses plural
    "range_slider": "range-slider",
    "search": "search",
    "select": "select",
    "side_nav": "side-navigation",  # USWDS uses full word
    "site_alert": "site-alert",
    "step_indicator": "step-indicator",
    "summary_box": "summary-box",
    "table": "table",
    "tag": "tag",
    "text_input": "text-input",
    "textarea": "text-input",  # covered on the text-input USWDS page
    "time_picker": "time-picker",
    "tooltip": "tooltip",
}


def component_tag(name: str) -> str:
    """Convert a component directory name to its cotton tag name."""
    return f"<c-{name.replace('_', '-')}>"


def uswds_url(name: str) -> str | None:
    """Return the full USWDS documentation URL for a component, or None."""
    slug = COMPONENT_USWDS_SLUGS.get(name)
    if slug is None:
        return None
    return f"{USWDS_BASE_URL}/{slug}/"
