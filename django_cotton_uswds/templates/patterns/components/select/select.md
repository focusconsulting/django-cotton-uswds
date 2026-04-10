# Select

A styled dropdown menu that allows users to choose one option from a list. Follows USWDS select patterns.

## Props

| Prop             | Default | Description                                                                  |
| ---------------- | ------- | ---------------------------------------------------------------------------- |
| `id`             |         | Unique ID for the select element; also links the associated `c-label`       |
| `name`           |         | Form field name submitted with the form                                      |
| `options`        |         | List of option dicts with `display` and `value` keys                        |
| `default_option` |         | Display text for a pre-selected placeholder option (e.g., `"- Select one -"`) |
| `default_value`  |         | Value of the `default_option`; the option is selected when `value` matches  |
| `value`          |         | Currently selected value; pre-selects a matching option on render           |
| `disabled`       |         | Set to `"true"` to disable the select element                               |
| `required`       |         | Set to `"true"` to mark the select as required                              |
| `extra_classes`  |         | Additional CSS classes for the `<select>` element                           |

## Example Usage

### Basic Select

```django
<c-label id="select-1" label="Select an option" />
<c-select
    id="select-1"
    name="my_select"
    :options="[
        {'display': 'Option 1', 'value': 'option1'},
        {'display': 'Option 2', 'value': 'option2'},
        {'display': 'Option 3', 'value': 'option3'},
    ]"
/>
```

### Select with Default Placeholder Option

```django
<c-label id="select-2" label="Select an option" />
<c-select
    id="select-2"
    name="my_select"
    default_option="- Select one -"
    default_value=""
    :options="[
        {'display': 'Option 1', 'value': 'option1'},
        {'display': 'Option 2', 'value': 'option2'},
        {'display': 'Option 3', 'value': 'option3'},
    ]"
/>
```

### Disabled Select

```django
<c-label id="select-3" label="Select an option" />
<c-select
    id="select-3"
    name="my_select"
    disabled="true"
    :options="[
        {'display': 'Option 1', 'value': 'option1'},
        {'display': 'Option 2', 'value': 'option2'},
        {'display': 'Option 3', 'value': 'option3'},
    ]"
/>
```

### Required Select

```django
<c-label id="select-4" label="Select an option" required="true" />
<c-select
    id="select-4"
    name="my_select"
    required="true"
    :options="[
        {'display': 'Option 1', 'value': 'option1'},
        {'display': 'Option 2', 'value': 'option2'},
        {'display': 'Option 3', 'value': 'option3'},
    ]"
/>
```

### Select with Pre-selected Value

```django
<c-label id="select-5" label="Select an option" />
<c-select
    id="select-5"
    name="my_select"
    value="option2"
    :options="[
        {'display': 'Option 1', 'value': 'option1'},
        {'display': 'Option 2', 'value': 'option2'},
        {'display': 'Option 3', 'value': 'option3'},
    ]"
/>
```

## Usage Notes

- Always pair `c-select` with a `c-label` referencing the same `id`
- Options are passed as a list of dicts with `display` (shown text) and `value` (submitted value) keys
- Use `default_option` for a placeholder prompt (e.g., `"- Select one -"`) that is shown when no real option is selected
- For a searchable/filterable dropdown, use the `c-combo-box` component instead
- Wrap in `c-form-group` for correct USWDS form layout
