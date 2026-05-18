# Alert

A contextual notification that informs users of a status change or action they need to take. Follows USWDS alert patterns.

## Props

| Prop           | Default | Description                                                                                       |
| -------------- | ------- | ------------------------------------------------------------------------------------------------- |
| `type`         | `info`  | Alert type: `info`, `warning`, `success`, `error`, or `emergency`                                |
| `heading`      |         | Optional heading text displayed above the body content                                            |
| `role`         |         | ARIA role override; automatically set to `alert` for `error` and `emergency` types               |
| `extra_classes`|         | Additional CSS classes (e.g., `usa-alert--no-icon`)                                              |
| `:slim`        | `False` | Renders the compact slim variant (adds `usa-alert--slim`)                                        |
| `:rich`        | `False` | Wraps the body in a `usa-prose` `<div>` instead of a single `<p>` so the slot can contain multiple block elements (paragraphs, lists, headings) |

## Slots

| Slot      | Description                                                        |
| --------- | ------------------------------------------------------------------ |
| (default) | Alert body content; supports safe HTML including links             |

## Example Usage

### Informational Alert

```django
<c-alert type="info" heading="Informative status">
    Lorem ipsum dolor sit amet, <a class="usa-link" href="#">consectetur adipiscing</a> elit.
</c-alert>
```

### Warning Alert

```django
<c-alert type="warning" heading="Warning status">
    Lorem ipsum dolor sit amet, <a class="usa-link" href="#">consectetur adipiscing</a> elit.
</c-alert>
```

### Success Alert

```django
<c-alert type="success" heading="Success status">
    Lorem ipsum dolor sit amet, <a class="usa-link" href="#">consectetur adipiscing</a> elit.
</c-alert>
```

### Error Alert

```django
<c-alert type="error" heading="Error status">
    Lorem ipsum dolor sit amet, <a class="usa-link" href="#">consectetur adipiscing</a> elit.
</c-alert>
```

### Emergency Alert

```django
<c-alert type="emergency" heading="Emergency status">
    Lorem ipsum dolor sit amet, <a class="usa-link" href="#">consectetur adipiscing</a> elit.
</c-alert>
```

### Slim Alert

```django
<c-alert type="info" extra_classes="usa-alert--slim">
    Lorem ipsum dolor sit amet, <a class="usa-link" href="#">consectetur adipiscing</a> elit.
</c-alert>
```

### Alert with No Icon

```django
<c-alert type="info" extra_classes="usa-alert--no-icon">
    No icon alert example.
</c-alert>
```

### Rich Content Alert

Use `:rich="True"` when the body needs to contain multiple block elements such as paragraphs or lists. The slot is rendered inside a `usa-prose` `<div>` rather than a single `<p>`.

```django
<c-alert type="info" heading="Rich content status" :rich="True">
    <p>Lorem ipsum dolor sit amet, <a class="usa-link" href="#">consectetur adipiscing</a> elit.</p>
    <ul>
        <li>First supporting detail</li>
        <li>Second supporting detail</li>
    </ul>
    <p>Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
</c-alert>
```

## Usage Notes

- The `error` and `emergency` types automatically set `role="alert"` for screen readers
- Use `:slim="True"` for compact notifications that don't need a heading
- Set `:rich="True"` when the body needs multiple block-level elements; otherwise the default `<p>` wrapper is preferred
- Body content is passed as the slot and supports safe HTML rendering
- For sitewide alerts that wrap the full page width, use the `c-site_alert` component instead
