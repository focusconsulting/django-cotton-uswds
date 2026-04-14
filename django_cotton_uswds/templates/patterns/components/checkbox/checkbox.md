# Checkbox

A form input that allows users to select one or more options. Supports tile style, label descriptions, and indeterminate state. Follows USWDS checkbox patterns.

## Props

| Prop                | Default | Description                                                             |
| ------------------- | ------- | ----------------------------------------------------------------------- |
| `id`                |         | Unique ID for the checkbox input; also links the `<label>` via `for`   |
| `name`              |         | Form field name submitted with the form                                 |
| `label`             |         | Label text displayed next to the checkbox                               |
| `value`             |         | Value submitted when the checkbox is checked                            |
| `tile`              | `False` | Set to `"true"` to use the tile checkbox style                         |
| `label_description` |         | Optional secondary description text below the label                    |
| `indeterminate`     | `False` | Set to `"true"` to show an indeterminate (mixed) state                 |
| `checked`           |         | Set to `"true"` to pre-check the checkbox                              |
| `disabled`          |         | Set to `"true"` to disable the checkbox                                |
| `required`          |         | Set to `"true"` to mark the checkbox as required                       |
| `extra_classes`     |         | Additional CSS classes to apply to the checkbox wrapper                 |

## Example Usage

### Checkbox Group

Use multiple `c-checkbox` elements sharing the same `name` to create a checkbox group. Wrap them in `c-fieldset` for accessible grouping.

```django
<c-fieldset legend="Select all that apply">
    <c-checkbox id="opt-1" name="options" label="Option 1" value="option1" checked="true" />
    <c-checkbox id="opt-2" name="options" label="Option 2" value="option2" />
    <c-checkbox id="opt-3" name="options" label="Option 3" value="option3" />
</c-fieldset>
```

### Checkbox with Label Description

```django
<c-checkbox
    id="desc-checkbox"
    name="desc"
    label="Checkbox with Description"
    label_description="This is additional description text."
/>
```

### Tile Checkbox

```django
<c-checkbox
    id="tile-checkbox"
    name="tile"
    label="Tile Checkbox"
    tile="true"
/>
```

### Tile Checkbox with Label Description

```django
<c-checkbox
    id="tile-desc-checkbox"
    name="tile_desc"
    label="Tile Checkbox with Description"
    tile="true"
    label_description="This is additional description text."
/>
```

### Indeterminate Checkbox

```django
<c-checkbox
    id="indeterminate-checkbox"
    name="indeterminate"
    label="Indeterminate Checkbox"
    indeterminate="true"
/>
```

### Disabled Checkbox

```django
<c-checkbox
    id="disabled-checkbox"
    name="disabled"
    label="Disabled Checkbox"
    disabled="true"
/>
```

### Required Checkbox

```django
<c-checkbox
    id="required-checkbox"
    name="required"
    label="Required Checkbox"
    required="true"
/>
```

### Checked Tile Checkbox

```django
<c-checkbox
    id="checked-tile-checkbox"
    name="checked_tile"
    label="Checked Tile Checkbox"
    tile="true"
    checked="true"
/>
```

### Disabled Indeterminate Checkbox

```django
<c-checkbox
    id="disabled-indeterminate-checkbox"
    name="disabled_indeterminate"
    label="Disabled Indeterminate Checkbox"
    indeterminate="true"
    disabled="true"
/>
```

## Usage Notes

- For checkbox groups, wrap multiple `c-checkbox` elements in `c-fieldset` with a `legend` for accessibility
- The tile style (`tile="true"`) provides a larger click target with a bordered card appearance
- The indeterminate state is a visual-only indicator; it must be managed in JavaScript after render
- A required marker is automatically added to the label when `required="true"` is set
