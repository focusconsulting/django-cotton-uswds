# Radio Button

A form input that allows users to select exactly one option from a group. Supports tile style and label descriptions. Follows USWDS radio button patterns.

## Props

| Prop                | Default  | Description                                                               |
| ------------------- | -------- | ------------------------------------------------------------------------- |
| `id`                |          | Unique ID for the radio input; also links the `<label>` via `for`        |
| `name`              |          | Form field name; all radio buttons in a group share the same `name`      |
| `label`             |          | Label text displayed next to the radio button                             |
| `value`             |          | Value submitted when this radio button is selected                        |
| `radio_type`        |          | Style variant: leave empty for default, or `"tile"` for the tile style   |
| `label_description` |          | Optional secondary description text below the label                      |
| `checked`           | `False`  | Set to `"true"` to pre-select this radio button                          |

## Example Usage

### Default Radio Group

Wrap multiple `c-radio-button` elements sharing the same `name` in a `c-fieldset`.

```django
<c-fieldset legend="Please select an option">
    <c-radio-button id="radio-1" name="choice" label="Option A" value="a" />
    <c-radio-button id="radio-2" name="choice" label="Option B" value="b" />
    <c-radio-button id="radio-3" name="choice" label="Option C" value="c" />
</c-fieldset>
```

### Required Radio Group

```django
<c-fieldset legend="Please select an option" required="true">
    <c-radio-button id="radio-1" name="choice" label="Option A" value="a" />
    <c-radio-button id="radio-2" name="choice" label="Option B" value="b" />
    <c-radio-button id="radio-3" name="choice" label="Option C" value="c" />
</c-fieldset>
```

### Tile Radio Group with Label Descriptions

```django
<c-fieldset legend="Please select an option">
    <c-radio-button
        id="tile-1"
        name="tile_choice"
        label="Option A"
        value="a"
        radio_type="tile"
        label_description="Description for option A"
    />
    <c-radio-button
        id="tile-2"
        name="tile_choice"
        label="Option B"
        value="b"
        radio_type="tile"
        label_description="Description for option B"
    />
    <c-radio-button
        id="tile-3"
        name="tile_choice"
        label="Option C"
        value="c"
        radio_type="tile"
        label_description="Description for option C"
    />
</c-fieldset>
```

### Tile Radio Group (Required)

```django
<c-fieldset legend="Please select an option" required="true">
    <c-radio-button id="tile-req-1" name="tile_req" label="Option A" value="a" radio_type="tile" />
    <c-radio-button id="tile-req-2" name="tile_req" label="Option B" value="b" radio_type="tile" />
    <c-radio-button id="tile-req-3" name="tile_req" label="Option C" value="c" radio_type="tile" />
</c-fieldset>
```

### Radio Group with Default Selection

```django
<c-fieldset legend="Please select an option">
    <c-radio-button id="default-1" name="default_choice" label="Option A" value="a" checked="true" />
    <c-radio-button id="default-2" name="default_choice" label="Option B" value="b" />
    <c-radio-button id="default-3" name="default_choice" label="Option C" value="c" />
</c-fieldset>
```

### Tile Radio Group with Default Selection

```django
<c-fieldset legend="Please select an option">
    <c-radio-button id="tile-def-1" name="tile_default" label="Option A" value="a" radio_type="tile" checked="true" />
    <c-radio-button id="tile-def-2" name="tile_default" label="Option B" value="b" radio_type="tile" />
    <c-radio-button id="tile-def-3" name="tile_default" label="Option C" value="c" radio_type="tile" />
</c-fieldset>
```

## Usage Notes

- All radio buttons in a group must share the same `name` attribute so only one can be selected at a time
- Always wrap a radio button group in `c-fieldset` with a descriptive `legend` for accessibility
- Each radio button must have a unique `id` on the page
- The tile style (`radio_type="tile"`) displays each option as a bordered card with a larger click target
- Set `checked="true"` on at most one radio button per group to establish a default selection
