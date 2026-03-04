# django-cotton-uswds

[USWDS](https://designsystem.digital.gov/) components as [Django Cotton](https://django-cotton.com/) templates.

Use the U.S. Web Design System in your Django projects with a clean, declarative component syntax.

## Installation

```bash
pip install django-cotton-uswds
```

Add both `django_cotton` and `django_cotton_uswds` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    "django_cotton",
    "django_cotton_uswds",
]
```

## Usage

Components follow the `<c-uswds.component>` naming convention:

```html
<c-uswds.alert type="info" heading="Informative status">
    This is an informative alert.
</c-uswds.alert>
```

Attributes pass through to the underlying USWDS markup, so you can use the same options documented on the [USWDS component pages](https://designsystem.digital.gov/components/overview/).

## USWDS Assets

This package provides **markup only** — no CSS or JavaScript is bundled. You need to add USWDS assets to your project separately.

See the [USWDS getting started guide](https://designsystem.digital.gov/documentation/getting-started/developers/phase-two-compile/) for instructions on compiling and including the USWDS stylesheet and scripts.

## Available Components

This project is in early development. Components are being added incrementally. See the [USWDS components page](https://designsystem.digital.gov/components/overview/) for reference on what's planned.

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

## License

MIT
