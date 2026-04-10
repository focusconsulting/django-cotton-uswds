# Combo Box

An enhanced select input that allows users to filter a list by typing. Follows USWDS combo box patterns.

## Props

| Prop             | Default | Description                                                         |
| ---------------- | ------- | ------------------------------------------------------------------- |
| `id`             |         | Unique ID for the combo box element                                 |
| `name`           |         | Form field name submitted with the form                             |
| `options`        |         | List of option dicts with `value` and `label` keys                 |
| `default_value`  |         | Value of the option that should be selected on initial render       |
| `disabled`       |         | Set to `"true"` to disable the combo box                           |
| `assistive_hint` |         | Screen reader hint text describing the filtering behavior           |
| `class`          |         | Additional CSS classes to apply to the combo box wrapper            |

## Example Usage

### Basic Combo Box

```django
<c-combo-box
    id="fruit-select"
    name="fruit"
    :options="[
        {'value': 'apple', 'label': 'Apple'},
        {'value': 'banana', 'label': 'Banana'},
        {'value': 'cherry', 'label': 'Cherry'},
    ]"
/>
```

### Combo Box with Default Value

```django
<c-combo-box
    id="fruit-default"
    name="fruit"
    default_value="banana"
    :options="[
        {'value': 'apple', 'label': 'Apple'},
        {'value': 'banana', 'label': 'Banana'},
        {'value': 'cherry', 'label': 'Cherry'},
    ]"
/>
```

### Disabled Combo Box

```django
<c-combo-box
    id="fruit-disabled"
    name="fruit"
    disabled="true"
    :options="[
        {'value': 'apple', 'label': 'Apple'},
        {'value': 'banana', 'label': 'Banana'},
        {'value': 'cherry', 'label': 'Cherry'},
    ]"
/>
```

## Usage Notes

- Options are passed as a list of dicts, each with `value` and `label` keys
- Use `default_value` to pre-select an option matching one of the option `value` fields
- USWDS JavaScript is required to activate the combo box filtering behavior
- For simple dropdowns without filtering, use the `c-select` component instead
