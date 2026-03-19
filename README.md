# django-cotton-uswds

[USWDS](https://designsystem.digital.gov/) components as [Django Cotton](https://django-cotton.com/) templates.

Use the U.S. Web Design System in your Django projects with a clean, declarative component syntax.

## Installation

```bash
git clone https://github.com/iversondiles/django-cotton-uswds.git
cd django-cotton-uswds
pip install -e .
```

Then add both `django_cotton` and `django_cotton_uswds` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    "django_cotton",
    "django_cotton_uswds",
]
```

## Usage

Components follow the `<c-component>` naming convention:

```html
<c-alert type="info" heading="Informative status">
    This is an informative alert.
</c-alert>
```

Attributes pass through to the underlying USWDS markup, so you can use the same options documented on the [USWDS component pages](https://designsystem.digital.gov/components/overview/).

## USWDS Assets

This package provides **markup only** — no CSS or JavaScript is bundled. You need to add USWDS assets to your project separately.

See the [USWDS getting started guide](https://designsystem.digital.gov/documentation/getting-started/developers/phase-two-compile/) for instructions on compiling and including the USWDS stylesheet and scripts.

## Available Components

This project is in early development. Components are being added incrementally. See the [USWDS components page](https://designsystem.digital.gov/components/overview/) for reference on what's planned.

## Form Rendering

The package includes a USWDS form renderer that automatically styles Django forms with USWDS markup — labels, hints, error messages, and all standard widget types.

### Per-form via mixin

```python
from django import forms
from django_cotton_uswds.mixins import USWDSFormMixin

class ContactForm(USWDSFormMixin, forms.Form):
    name = forms.CharField(label="Full name")
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

### Globally via settings

```python
# settings.py
FORM_RENDERER = "django_cotton_uswds.renderer.USWDSFormRenderer"
```

### Widget attribute passthrough

USWDS-specific attributes can be passed through widget `attrs`:

```python
class MyForm(USWDSFormMixin, forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"width": "md"}),
    )
    resume = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"accept": ".pdf,.doc"}),
    )
```

### Supported widget mappings

| Django widget | USWDS rendering |
|---|---|
| `TextInput`, `EmailInput`, `NumberInput`, etc. | `usa-input` text field |
| `Textarea` | `usa-textarea` |
| `Select` | `usa-select` dropdown |
| `RadioSelect` | Fieldset with `usa-radio` buttons |
| `CheckboxSelectMultiple` | Fieldset with `usa-checkbox` items |
| `CheckboxInput` (boolean) | Single `usa-checkbox` |
| `ClearableFileInput` | `usa-file-input` |

## Demo

A demo project is included to showcase components. Requires [just](https://github.com/casey/just) and [uv](https://github.com/astral-sh/uv).

```bash
# Install the package with demo dependencies
just install

# Run the development server at http://127.0.0.1:8000/
just demo

# Build a static site into demo_project/dist/
just build
```

## Requirements

- Python 3.10+
- Django 4.2+
- django-cotton 1.2.1+

## Domain Language

See [UBIQUITOUS_LANGUAGE.md](UBIQUITOUS_LANGUAGE.md) for a glossary of canonical domain terms used in this project.

## License

MIT
