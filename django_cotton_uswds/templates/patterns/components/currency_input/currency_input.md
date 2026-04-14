# Currency Input

A pre-built text input with a `$` prefix for entering US dollar amounts. Built on top of `c-input-group`, `c-input-prefix`, and `c-text-input`. Follows USWDS input group patterns.

## Props

| Prop        | Default     | Description                                                        |
| ----------- | ----------- | ------------------------------------------------------------------ |
| `id`        |             | Unique ID for the input; also used to link the associated `c-label` |
| `name`      |             | Form field name submitted with the form                            |
| `value`     |             | Pre-filled dollar amount                                           |
| `hint`      |             | Optional hint text displayed below the label via `c-label`        |
| `error`     |             | Error message text; applies error styling to the input group       |
| `success`   |             | Set to `"true"` to apply success styling                          |
| `disabled`  |             | Set to `"true"` to disable the input                              |
| `readonly`  |             | Set to `"true"` to make the input read-only                       |
| `required`  |             | Set to `"true"` to mark the input as required                     |
| `width`     |             | Width modifier: `2xs`, `xs`, `sm`, `md`, `lg`, `xl`, `2xl`        |
| `inputmode` | `"numeric"` | Virtual keyboard hint; defaults to `numeric` for dollar amounts   |

## Example Usage

### Basic Currency Input

```django
<c-label id="price" label="Item price" />
<c-currency-input id="price" name="price" />
```

### Currency Input with Hint

```django
<c-label id="budget" label="Monthly budget" hint="Enter an amount in US dollars." />
<c-currency-input id="budget" name="budget" hint="Enter an amount in US dollars." />
```

### Currency Input with Default Value

```django
<c-label id="salary" label="Annual salary" />
<c-currency-input id="salary" name="salary" value="50000.00" />
```

### Required Currency Input

```django
<c-label id="amount" label="Payment amount" required="true" />
<c-currency-input id="amount" name="amount" required="true" />
```

### Currency Input with Error

```django
<c-label id="total" label="Total" error="Please enter a valid dollar amount." />
<c-currency-input id="total" name="total" error="Please enter a valid dollar amount." />
```

### Disabled Currency Input

```django
<c-label id="fixed-fee" label="Fixed fee" />
<c-currency-input id="fixed-fee" name="fixed_fee" value="25.00" disabled="true" />
```

## Usage Notes

- Always pair `c-currency-input` with a `c-label` referencing the same `id`
- The `$` prefix is hardcoded; for other currencies, use `c-input-group` with `c-input-prefix` directly
- The `step="0.01"` attribute is set automatically to support cent-level precision
- Wrap in `c-form-group` for proper USWDS form layout with error messaging
