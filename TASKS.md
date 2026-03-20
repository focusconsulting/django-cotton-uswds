# Tasks

<!-- Ralph reads this file to find work. Each task follows the format below. -->

<!--
## TASK-N: Title

**Status:** TODO | IN_PROGRESS | DONE | BLOCKED

**User stories**: As a <role>, I want <goal> so that <benefit>.

### What to build

Description of the work.

### Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
-->

## TASK-1: Add breadcrumb component

**Status:** DONE

**User stories**: As a developer, I want a `<c-breadcrumb>` component so that I can add USWDS-styled breadcrumb navigation to my pages without writing raw HTML.

### What to build

Create a Cotton component that wraps the USWDS breadcrumb markup. It should support a list of links and render the final item as the current page (non-linked).

### Acceptance criteria

- [x] `<c-breadcrumb>` component renders valid USWDS breadcrumb HTML
- [x] Supports an arbitrary number of breadcrumb items
- [x] The last item displays as plain text (current page), not a link
- [x] Component is documented in the demo app

## EPIC-1: Deepen renderer engine configuration module (GH #10)

Issue #10 is the parent PRD. The three tasks below implement it.

---

## TASK-2: Promote USWDSFormMixin and USWDSFormRenderer to package root (GH #11)

**Status:** DONE

**User stories**: As a developer, I want to import `USWDSFormMixin` and `USWDSFormRenderer` from the package root so that I have a single, obvious import location.

### What to build

Export `USWDSFormMixin` and `USWDSFormRenderer` from `django_cotton_uswds/__init__.py`. The deep import paths (`from django_cotton_uswds.renderer import ...`, `from django_cotton_uswds.mixins import ...`) must remain functional for backward compatibility. The `FORM_RENDERER` settings string should work from the package root path (`"django_cotton_uswds.USWDSFormRenderer"`).

### Acceptance criteria

- [x] `from django_cotton_uswds import USWDSFormMixin` works
- [x] `from django_cotton_uswds import USWDSFormRenderer` works
- [x] `__all__` is defined in `__init__.py` with both names
- [x] `FORM_RENDERER = "django_cotton_uswds.USWDSFormRenderer"` activates USWDS rendering
- [x] Deep import paths still work
- [x] Tests cover both import paths

## TASK-3: Add renderer engine boundary tests (GH #12)

**Status:** DONE

**User stories**: As a maintainer, I want boundary tests for the renderer engine so that internal refactors don't silently break the engine's wiring.

### What to build

Add tests that verify the renderer engine's internal invariants at its public boundary. These tests ensure the engine is correctly wired without testing implementation details — they should survive internal refactors. See GH #10 for the full list of behaviors to verify.

### Acceptance criteria

- [x] Test that `USWDSFormRenderer()` produces a functional engine with no arguments
- [x] Test that Cotton loader is the first loader in the engine's loader chain
- [x] Test that the engine resolves templates from the package's `templates/` directory
- [x] Test that the engine resolves templates from Django's built-in form templates directory
- [x] Test that Cotton builtins are registered (engine can process `<c-*>` syntax without `{% load %}`)
- [x] All new tests pass with `uv run pytest`

## TASK-4: Deprecate cotton_aliases templatetag module (GH #13)

**Status:** DONE

**Blocked by:** TASK-2 (DONE)

**User stories**: As a developer, I want clear guidance that `cotton_aliases` is deprecated so that I don't configure unnecessary templatetag builtins when the renderer already handles Cotton registration internally.

### What to build

Deprecate `django_cotton_uswds/templatetags/cotton_aliases.py`. The renderer already handles Cotton builtin registration internally. Add a `DeprecationWarning` when the module is imported, pointing users to `django-cotton`'s own docs for making Cotton tags available in project templates. Existing code that references the module in `TEMPLATES` builtins must still function.

### Acceptance criteria

- [x] `cotton_aliases.py` emits a `DeprecationWarning` when imported, with a clear message about what to do instead
- [x] Existing code that references `django_cotton_uswds.templatetags.cotton_aliases` in `TEMPLATES` builtins still functions
- [x] The warning message points users to `django-cotton`'s own documentation
