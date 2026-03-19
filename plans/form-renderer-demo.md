# Plan: Form Renderer Demo Page

> Source PRD: Grill-me session output from issue #1 (Django Forms Integration: USWDS Form Renderer)

## Architectural decisions

Durable decisions that apply across all phases:

- **Route**: `components/form-renderer/` — follows existing component pattern
- **Component entry**: `("form-renderer", "Form Renderer", "Forms")` added to `COMPONENTS` list in views.py
- **Form class**: Lives in new `demo_app/forms.py`, uses `USWDSFormMixin` (not global `FORM_RENDERER` setting)
- **View**: New `FormRendererView` in `demo_app/views.py` — a `FormView`-style class handling GET and POST
- **Template**: `demo_app/components/form_renderer.html` extending `pattern_base.html`, renders with `{{ form }}`
- **Distill**: Pre-renders GET state only; POST/validation works only when running locally
- **Success flow**: POST/redirect/GET with `?success=1` query param — no session/messages framework needed
- **No database**: Validate-and-redisplay only, no persistence

---

## Phase 1: Minimal end-to-end form demo

**User stories**: Core pipeline proving renderer works in the demo context

### What to build

A new demo page at `components/form-renderer/` with a Django form using `USWDSFormMixin` and 2-3 fields (CharField with help_text, EmailField, ChoiceField). A view that renders the empty form on GET and validates + re-renders with errors on POST. The page appears in the side nav under "Forms" and is pre-renderable by distill.

### Acceptance criteria

- [x] `demo_app/forms.py` exists with a form class using `USWDSFormMixin` and 2-3 fields
- [x] `FormRendererView` in `views.py` handles GET (empty form) and POST (validate, re-render with errors)
- [x] Template at `demo_app/components/form_renderer.html` extends `pattern_base.html` and renders with `{{ form }}`
- [x] `("form-renderer", "Form Renderer", "Forms")` added to `COMPONENTS` list
- [x] URL registered with `distill_path` and the page builds successfully with `python manage.py distill-local`
- [x] Running locally (`just demo`), submitting the form with invalid data shows validation errors styled with USWDS components

---

## Phase 2: Complete form and success flow

**User stories**: All widget types covered, success UX

### What to build

Expand the form to ~8 fields covering every supported widget type, with renderer features (required markers, help_text hints, width attrs) distributed naturally across them. Add POST/redirect/GET success flow using `?success=1` query param that renders a `<c-alert>` at the top of the page.

### Acceptance criteria

- [x] Form includes all widget types: CharField, EmailField, Textarea, BooleanField, ChoiceField (select), ChoiceField (RadioSelect), MultipleChoiceField (CheckboxSelectMultiple), FileField
- [x] Required vs optional fields both present (shows required marker difference)
- [x] At least one field has `help_text` (shows hint rendering)
- [x] At least one field uses widget `attrs` like `width` (shows attrs pass-through)
- [x] Valid submission redirects to same page with `?success=1`
- [x] `?success=1` renders a success `<c-alert>` above the form
- [x] Submitting with invalid data preserves entered values and shows field-level errors
- [x] Static site build still works (distill renders the GET state)
