# Textarea

A multi-line text input for longer free-form text. Supports validation states, row count, and max length. Follows USWDS textarea patterns.

## Props

| Prop            | Default | Description                                                                |
| --------------- | ------- | -------------------------------------------------------------------------- |
| `id`            |         | Unique ID for the textarea; also links the associated `c-label`           |
| `name`          |         | Form field name submitted with the form                                    |
| `value`         |         | Pre-filled text content                                                    |
| `hint`          |         | Hint text displayed below the label via `c-label`                         |
| `error`         |         | Error message text; also applies the error CSS class to the textarea       |
| `success`       |         | Set to `"true"` to apply the success CSS class                            |
| `disabled`      |         | Set to `"true"` to disable the textarea                                   |
| `readonly`      |         | Set to `"true"` to make the textarea read-only                            |
| `required`      |         | Set to `"true"` to mark the textarea as required                          |
| `rows`          |         | Number of visible text rows (HTML `rows` attribute)                       |
| `maxlength`     |         | Maximum number of characters allowed; wraps in a character count widget when set |
| `extra_classes` |         | Additional CSS classes for the textarea element                            |
| `input_classes` |         | Additional CSS classes applied directly to the `<textarea>` element       |

## Example Usage

### Basic Textarea

```django
<c-label id="textarea-basic" label="Textarea label" />
<c-textarea id="textarea-basic" name="basic" />
```

### Textarea with Hint

```django
<c-label id="textarea-hint" label="Description" hint="Enter a brief description (optional)." />
<c-textarea id="textarea-hint" name="description" />
```

### Textarea with Error

```django
<c-label id="textarea-error" label="Comments" error="This field is required." />
<c-textarea id="textarea-error" name="comments" error="This field is required." />
```

### Textarea with Success

```django
<c-label id="textarea-success" label="Feedback" />
<c-textarea id="textarea-success" name="feedback" value="This is valid input." success="true" />
```

### Textarea with Custom Row Count

```django
<c-label id="textarea-rows" label="Notes" />
<c-textarea id="textarea-rows" name="notes" rows="4" />
```

### Disabled Textarea

```django
<c-label id="textarea-disabled" label="Archived notes" />
<c-textarea id="textarea-disabled" name="archived_notes" value="This content is read-only." disabled="true" />
```

### Readonly Textarea

```django
<c-label id="textarea-readonly" label="Terms of service" />
<c-textarea id="textarea-readonly" name="terms" value="These are the terms of service..." readonly="true" />
```

### Required Textarea

```django
<c-label id="textarea-required" label="Message" required="true" />
<c-textarea id="textarea-required" name="message" required="true" />
```

### Textarea with Max Length

When `maxlength` is set, the textarea is automatically wrapped in a character count widget.

```django
<c-label id="textarea-maxlength" label="Summary" hint="Maximum 200 characters." />
<c-textarea id="textarea-maxlength" name="summary" rows="5" maxlength="200" />
```

## Usage Notes

- Always pair `c-textarea` with a `c-label` referencing the same `id`
- Pass `error` to both `c-label` (for the error message) and `c-textarea` (for the error border styling)
- When `maxlength` is provided, a live character counter is automatically rendered via USWDS JavaScript
- Wrap in `c-form-group` for correct USWDS form layout with label, hint, and error message
