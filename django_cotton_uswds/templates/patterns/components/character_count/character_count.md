# Character Count

An input or textarea that displays a live character count, informing users how many characters remain before reaching the maximum. Follows USWDS character count patterns.

## Props

| Prop            | Default  | Description                                                              |
| --------------- | -------- | ------------------------------------------------------------------------ |
| `id`            |          | Unique ID for the input; also used as the base for the counter element IDs |
| `name`          |          | Form field name submitted with the form (use `name_attr` in some contexts) |
| `label`         |          | Label text displayed above the input                                     |
| `hint`          |          | Optional hint text displayed below the label                             |
| `maxlength`     |          | Maximum number of characters allowed; drives the counter display         |
| `is_textarea`   | `"false"`| Set to `"true"` to render a `<textarea>` instead of a text `<input>`    |
| `default_value` |          | Pre-filled value for the field                                           |
| `disabled`      |          | Set to `"disabled"` to disable the field                                 |
| `required`      |          | Set to `"true"` to mark the field as required                            |
| `rows`          |          | Number of visible rows; only applies when `is_textarea="true"`           |
| `placeholder`   |          | Placeholder text displayed inside the input                              |
| `type`          | `"text"` | Input type (e.g., `text`, `password`); only applies when `is_textarea="false"` |
| `class`         |          | Additional CSS classes for the character count wrapper                   |

## Example Usage

### Text Input with Character Count

```django
<c-label id="char-count-input" label="Text input" hint="This input has a character limit." />
<c-character-count
    id="char-count-input"
    name="char_count_input"
    maxlength="25"
    type="text"
    placeholder="Enter text here"
/>
```

### Textarea with Character Count

```django
<c-label id="char-count-textarea" label="Textarea" hint="This textarea has a character limit." />
<c-character-count
    id="char-count-textarea"
    name="char_count_textarea"
    maxlength="50"
    is_textarea="true"
    rows="3"
/>
```

### Input with Default Value

```django
<c-label id="char-count-default" label="Text input with default value" />
<c-character-count
    id="char-count-default"
    name="char_count_default"
    maxlength="30"
    default_value="Hello World"
    type="text"
/>
```

### Disabled Character Count Input

```django
<c-label id="char-count-disabled" label="Disabled input" />
<c-character-count
    id="char-count-disabled"
    name="char_count_disabled"
    maxlength="20"
    disabled="disabled"
    type="text"
/>
```

### Required Character Count Input

```django
<c-label id="char-count-required" label="Required input" hint="This field is required." required="true" />
<c-character-count
    id="char-count-required"
    name="char_count_required"
    maxlength="40"
    required="true"
    type="text"
/>
```

## Usage Notes

- Always pair `c-character-count` with a `c-label` referencing the same `id`
- The `maxlength` prop is required; it controls both the HTML `maxlength` attribute and the counter message
- Use `is_textarea="true"` together with the `rows` prop for multi-line inputs
- For a combined label + input + character count within a form group, wrap all three in `c-form-group`
