# Button

A clickable element used to trigger actions or navigate within a form. Supports multiple color variants, sizes, and states. Follows USWDS button patterns.

## Props

| Prop           | Default    | Description                                                                                      |
| -------------- | ---------- | ------------------------------------------------------------------------------------------------ |
| `text`         |            | Button label text                                                                                |
| `variant`      |            | Color/style variant: leave empty for default, or use `secondary`, `accent-cool`, `accent-warm`, `base`, `outline`, `outline-inverse`, `big`, or `unstyled` |
| `state`        |            | Force a visual state for demonstration: `hover`, `active`, `focus`, `unstyled`                  |
| `type`         | `"button"` | HTML button type: `button`, `submit`, or `reset`                                                |
| `disabled`     |            | Set to `"true"` to disable the button                                                           |
| `aria_disabled`|            | Set to `"true"` to mark the button as disabled via ARIA without removing interactivity          |
| `onClick`      |            | JavaScript expression for the `onclick` handler                                                  |
| `name`         |            | Form field name for submit buttons                                                               |
| `value`        |            | Value submitted with the form for submit buttons                                                 |

## Example Usage

### Default Button

```django
<c-button text="Default" />
```

### Secondary Button

```django
<c-button text="Secondary" variant="secondary" />
```

### Accent Cool Button

```django
<c-button text="Accent Cool" variant="accent-cool" />
```

### Accent Warm Button

```django
<c-button text="Accent Warm" variant="accent-warm" />
```

### Base Button

```django
<c-button text="Base" variant="base" />
```

### Outline Button

```django
<c-button text="Outline" variant="outline" />
```

### Outline Inverse Button

Use on dark backgrounds.

```django
<c-button text="Outline Inverse" variant="outline-inverse" />
```

### Big Button

```django
<c-button text="Big" variant="big" />
```

### Unstyled Button

```django
<c-button text="Unstyled" variant="unstyled" />
```

### Disabled Button

```django
<c-button text="Disabled" disabled="true" />
```

### ARIA-Disabled Button

Visually disabled but still focusable and interactive.

```django
<c-button text="ARIA Disabled" aria_disabled="true" />
```

### Submit Button

```django
<c-button text="Submit" type="submit" />
```

## Usage Notes

- The `state` prop is intended for visual demonstration in the pattern library; in production the browser handles hover/active/focus states automatically
- Use `disabled="true"` to fully prevent interaction; use `aria_disabled="true"` when you need the button to remain focusable (e.g., to show a tooltip explaining why it is unavailable)
- `variant="outline-inverse"` renders as `usa-button--outline usa-button--inverse` and should be used on dark-colored backgrounds
