# Label

A form label element with optional hint text and error state. Used to associate a visible text label with a form input. Follows USWDS label patterns.

## Props

| Prop       | Default | Description                                                                  |
| ---------- | ------- | ---------------------------------------------------------------------------- |
| `id`       |         | The ID of the associated input element (renders as `for` on the `<label>`)  |
| `label`    |         | Label text displayed above the input                                         |
| `hint`     |         | Optional hint text displayed below the label                                 |
| `required` |         | Set to `"true"` to append a required marker to the label                    |
| `error`    |         | Error message text; applies error styling to the label when set              |

## Example Usage

### Basic Label

```django
<c-label id="my-input" label="Full name" />
<c-text-input id="my-input" name="full_name" type="text" />
```

### Label with Hint

```django
<c-label id="email" label="Email address" hint="We'll only use this to contact you about your application." />
<c-text-input id="email" name="email" type="email" />
```

### Required Label

```django
<c-label id="username" label="Username" required="true" />
<c-text-input id="username" name="username" type="text" required="true" />
```

### Label with Error

```django
<c-label id="phone" label="Phone number" error="Please enter a valid phone number." />
<c-text-input id="phone" name="phone" type="tel" error="Please enter a valid phone number." />
```

## Usage Notes

- `c-label` renders both the `<label>` element and, when provided, the `<div class="usa-hint">` hint text
- The `id` prop maps to the `for` attribute on the label, linking it to the associated input for accessibility
- Pass the same `error` value to both `c-label` and the input component so that both the label styling and the input border update together
- For grouped inputs (checkboxes, radios), use `c-fieldset` with a `legend` instead of `c-label`
