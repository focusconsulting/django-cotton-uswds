# ADR-001: URL prefix middleware for GitHub Pages

## Status
Accepted

## Context
GitHub Pages serves this site at `/django-cotton-uswds/`, but Django's `{% url %}` tags produce unprefixed paths like `/components/`. Django's built-in `FORCE_SCRIPT_NAME` doesn't work here because `django-distill` renders pages in a `ThreadPoolExecutor` worker thread, and `set_script_prefix` uses thread-local storage that doesn't propagate across threads. Additionally, the prefix must only apply to rendered HTML content — not to the file paths distill uses to write output files.

## Decision
Use a custom `URLPrefixMiddleware` that sets the script prefix on entry and resets it on exit of each request. This scopes the prefix to template rendering (where `{% url %}` runs) without affecting distill's `generate_uri` calls that determine output file paths. The prefix is controlled by a `URL_PREFIX` environment variable.

## Consequences
- Navigation links work correctly on GitHub Pages
- Local dev is unaffected (no `URL_PREFIX` set by default)
- The middleware is tightly coupled to `django-distill`'s internal threading behavior
