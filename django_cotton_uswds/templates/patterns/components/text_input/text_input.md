# Text Input

A single-line text input field. Supports validation states, width modifiers, and input masks. Follows USWDS text input patterns.

## Props

| Prop           | Default      | Description                                                                        |
| -------------- | ------------ | ---------------------------------------------------------------------------------- |
| `id`           |              | Unique ID for the input; also used to link the associated `c-label`               |
| `name`         |              | Form field name submitted with the form                                            |
| `type`         |              | HTML input type (e.g., `text`, `email`, `password`, `search`)                     |
| `value`        |              | Pre-filled value for the field                                                     |
| `placeholder`  |              | Placeholder text displayed inside the input when empty                             |
| `hint`         |              | Hint text displayed below the label via `c-label`                                  |
| `error`        |              | Error message text; also applies the error styling class to the input              |
| `success`      |              | Set to `"true"` to apply the success styling class to the input                   |
| `disabled`     |              | Set to `"true"` to disable the input                                               |
| `readonly`     |              | Set to `"true"` to make the input read-only                                        |
| `required`     |              | Set to `"true"` to mark the input as required                                      |
| `width`        |              | Width modifier: `2xs`, `xs`, `sm`, `md`, `lg`, `xl`, `2xl`                        |
| `maxlength`    |              | Maximum number of characters allowed                                               |
| `pattern`      |              | HTML `pattern` attribute for client-side validation                                |
| `inputmode`    |              | Hints at the type of virtual keyboard to show (e.g., `numeric`, `text`)           |
| `input_classes`|              | Additional CSS classes applied directly to the `<input>` element                  |
| `class`        | `usa-input`  | Override the base CSS class on the `<input>` element                              |

## Example Usage

### Basic Text Input

```django
<c-label id="input-basic" label="Text input label" />
<c-text-input id="input-basic" name="basic" type="text" />
```

### Text Input with Hint

```django
<c-label id="input-hint" label="Text input with hint" hint="This is a helpful hint message." />
<c-text-input id="input-hint" name="hint" type="text" />
```

### Text Input with Error

```django
<c-label id="input-error" label="Text input with error" error="This field is required." />
<c-text-input id="input-error" name="error" type="text" error="This field is required." />
```

### Text Input with Success

```django
<c-label id="input-success" label="Text input with success" />
<c-text-input id="input-success" name="success" type="text" value="Valid input" success="true" />
```

### Small Width Input

```django
<c-label id="input-small" label="Small text input" />
<c-text-input id="input-small" name="small" type="text" width="sm" />
```

### Medium Width Input

```django
<c-label id="input-medium" label="Medium text input" />
<c-text-input id="input-medium" name="medium" type="text" width="md" />
```

### Disabled Input

```django
<c-label id="input-disabled" label="Disabled text input" />
<c-text-input id="input-disabled" name="disabled" type="text" value="This is disabled" disabled="true" />
```

### Readonly Input

```django
<c-label id="input-readonly" label="Readonly text input" />
<c-text-input id="input-readonly" name="readonly" type="text" value="This is readonly" readonly="true" />
```

### Required Input

```django
<c-label id="input-required" label="Required text input" required="true" />
<c-text-input id="input-required" name="required" type="text" required="true" />
```

### Input with Max Length

```django
<c-label id="input-maxlength" label="Text input with max length" hint="Maximum 10 characters." />
<c-text-input id="input-maxlength" name="maxlength" type="text" maxlength="10" />
```

### Social Security Number Input Mask

```django
<c-label id="input-ssn" label="Social Security Number" hint="Format: XXX-XX-XXXX" />
<c-text-input
    id="input-ssn"
    name="ssn"
    type="text"
    placeholder="___-__-____"
    pattern="^(?!(000|666|9))\d{3} (?!00)\d{2} (?!0000)\d{4}$"
    input_classes="usa-masked"
    inputmode="numeric"
/>
```

### US Telephone Number Input Mask

```django
<c-label id="input-tel" label="US Telephone Number" hint="Format: (XXX) XXX-XXXX" />
<c-text-input
    id="input-tel"
    name="tel"
    type="text"
    placeholder="(___) ___-____"
    pattern="^\(\d{3}\) \d{3}-\d{4}$"
    input_classes="usa-masked"
    inputmode="numeric"
/>
```

### 9-Digit US ZIP Code Input Mask

```django
<c-label id="input-zip9" label="9-Digit US ZIP Code" hint="Format: XXXXX-XXXX" />
<c-text-input
    id="input-zip9"
    name="zip9"
    type="text"
    placeholder="_____-____"
    pattern="^\d{5}(-\d{4})?$"
    input_classes="usa-masked"
    inputmode="numeric"
/>
```

### Alphanumeric Input Mask

```django
<c-label id="input-alphanumeric" label="Alphanumeric Input" hint="Format: A1A 2B3" />
<c-text-input
    id="input-alphanumeric"
    name="alphanumeric"
    type="text"
    placeholder="___ ___"
    pattern="\w\d\w \d\w\d"
    input_classes="usa-masked"
    inputmode="text"
    data-charset="A# #A#"
/>
```

## Usage Notes

- Always pair `c-text-input` with a `c-label` that references the same `id`
- Pass `error` to both `c-label` (for the error message display) and `c-text-input` (for the error CSS class)
- Width modifiers (`width`) constrain the visual width of the input without affecting its submitted value
- Input masks require USWDS JavaScript and the `usa-masked` class on the input via `input_classes`
- Wrap `c-label` and `c-text-input` in `c-form-group` for correct USWDS form layout
