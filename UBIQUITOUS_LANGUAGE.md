# Ubiquitous Language

## Component system

| Term | Definition | Aliases to avoid |
|------|-----------|-----------------|
| **Component** | A reusable Cotton template that renders USWDS-compliant HTML markup | Widget (when referring to the template), element, block |
| **Slot** | The default content area between a component's opening and closing tags, rendered via `{{ slot }}` | Children, body, inner content |
| **Variable** | A typed prop declared via `<c-vars>` at the top of a component template that controls its behavior | Prop, parameter, option |
| **Attribute passthrough** | The mechanism (`{{ attrs }}`) that forwards undeclared HTML attributes from a component tag to its root element | Props spread, rest attributes |

## Form rendering

| Term | Definition | Aliases to avoid |
|------|-----------|-----------------|
| **Form Renderer** | The `USWDSFormRenderer` class that bridges Django's form rendering to Cotton component templates | Template backend, form engine |
| **Form Mixin** | The `USWDSFormMixin` class applied to a Django Form to opt it into USWDS rendering | Form base class, form decorator |
| **Widget** | A Django form field renderer (e.g., `TextInput`, `Select`) that determines which HTML input type is produced | Component (when referring to Django's rendering unit), field type |
| **Widget template** | An HTML file in `templates/django/forms/widgets/` that overrides Django's default widget markup with USWDS classes | Widget override, input template |
| **Form Group** | A wrapper structure combining a label, optional hint, input field, and error message into a single USWDS form unit | Field wrapper, form row, form field |

## USWDS design system

| Term | Definition | Aliases to avoid |
|------|-----------|-----------------|
| **USWDS** | The U.S. Web Design System — the federal government's design system that defines the HTML patterns and CSS classes this library implements | Design system (too generic), theme |
| **USWDS class** | A CSS class name prefixed with `usa-` that applies USWDS styling to an HTML element | Style, CSS class (too generic) |
| **Variant** | A modifier that changes a component's visual style, mapped to a USWDS modifier class (e.g., `variant="secondary"` → `usa-button--secondary`) | Type (overloaded — see ambiguities), style, modifier |
| **Width modifier** | An input sizing option (`sm`, `md`, `lg`, `2xs`, `xs`, `xl`) that maps to `usa-input--{width}` | Size, input size |

## Component configuration

| Term | Definition | Aliases to avoid |
|------|-----------|-----------------|
| **Type** | A semantic category for a component that determines both its visual style and ARIA role (e.g., alert types: `info`, `warning`, `error`, `success`) | Kind, severity, level |
| **Hint** | Help text displayed below a form label to guide user input, rendered with the `usa-hint` class | Help text, description, subtitle |
| **Error message** | Validation feedback displayed within a form group when a field fails validation, rendered via `<c-error-message>` | Validation message, error text, feedback |
| **Extra classes** | Additional CSS classes passed to a component via the `extra_classes` variable to extend its default styling | Custom classes, class override |

## Relationships

- A **Component** renders zero or more **Slots** and declares zero or more **Variables**
- A **Form Renderer** resolves **Widget templates** and **Components** to produce USWDS markup
- A **Form Mixin** sets the **Form Renderer** as the default renderer for a Django Form class
- A **Form Group** contains exactly one **Widget**, one label, and optionally a **Hint** and **Error message**
- A **Variant** maps to exactly one **USWDS class** modifier (e.g., `--secondary`, `--outline`)
- A **Type** maps to both a **USWDS class** modifier and an ARIA role (e.g., `type="error"` → `usa-alert--error` + `role="alert"`)
- **Attribute passthrough** forwards any HTML attribute not declared as a **Variable** to the rendered element

## Example dialogue

> **Dev:** "I want to add a new USWDS **Component** for date pickers. Do I create a **Widget template** or a **Component**?"
> **Domain expert:** "Both, but they serve different purposes. The **Component** (`<c-date-picker>`) is the standalone Cotton template people use directly in their templates. The **Widget template** is what Django's form system uses when rendering a date field — it lives under `templates/django/forms/widgets/`."
> **Dev:** "So the **Form Renderer** picks up the **Widget template** automatically?"
> **Domain expert:** "Yes. When a form uses the **Form Mixin**, the **Form Renderer** resolves the correct **Widget template** based on the Django **Widget** class. The **Widget template** can itself use **Components** internally."
> **Dev:** "What about the **Variant** — does `type` on a date picker work the same as `type` on an alert?"
> **Domain expert:** "No — on an alert, **Type** determines the semantic category and ARIA role. On an input, `type` is just the HTML input type attribute passed through via **Attribute passthrough**. Don't confuse them."

## Flagged ambiguities

- **"type"** is used for two distinct concepts: (1) the semantic **Type** of a component like alerts (`info`, `warning`, `error`, `success`) which maps to USWDS modifier classes and ARIA roles, and (2) the HTML `type` attribute on inputs (`text`, `email`, `number`) which is a standard HTML attribute. Recommendation: use **Type** (capitalized) when referring to the component semantic category; use "HTML type attribute" or just `type` in code when referring to the input attribute.
- **"widget"** refers to both (1) a Django **Widget** class that determines form field rendering behavior, and (2) loosely to any UI **Component**. Recommendation: reserve **Widget** exclusively for Django's form field renderers; use **Component** for Cotton templates.
- **"variant"** and **"type"** overlap on some components — alerts use `type` for what buttons call `variant`. Both map to USWDS modifier classes. Recommendation: this mirrors USWDS's own API, so keep both but document that **Type** is for semantic categories (with ARIA implications) while **Variant** is for purely visual style differences.
