# Date Picker

An enhanced date input that provides a calendar widget for selecting dates. Follows USWDS date picker patterns.

## Props

| Prop       | Default | Description                                                          |
| ---------- | ------- | -------------------------------------------------------------------- |
| `id`       |         | Unique ID for the date input; also links the associated `c-label`   |
| `name`     |         | Form field name submitted with the form                              |
| `value`    |         | Pre-filled date value in `YYYY-MM-DD` format                        |
| `min`      |         | Minimum selectable date in `YYYY-MM-DD` format                      |
| `max`      |         | Maximum selectable date in `YYYY-MM-DD` format                      |
| `disabled` |         | Set to `"true"` to disable the date picker                          |
| `required` |         | Set to `"true"` to mark the field as required                       |

## Example Usage

### Default Date Picker

```django
<c-label id="start-date" label="Start date" />
<c-date-picker id="start-date" name="start_date" />
```

### Date Picker with Min and Max

```django
<c-label id="appointment" label="Appointment date" />
<c-date-picker
    id="appointment"
    name="appointment"
    min="2024-01-01"
    max="2024-12-31"
/>
```

### Date Picker with Default Value

```django
<c-label id="birth-date" label="Date of birth" />
<c-date-picker id="birth-date" name="birth_date" value="1990-06-15" />
```

### Disabled Date Picker

```django
<c-label id="locked-date" label="Locked date" />
<c-date-picker id="locked-date" name="locked_date" disabled="true" />
```

### Required Date Picker

```django
<c-label id="required-date" label="Required date" required="true" />
<c-date-picker id="required-date" name="required_date" required="true" />
```

## Usage Notes

- Always pair `c-date-picker` with a `c-label` referencing the same `id`
- USWDS JavaScript is required to activate the calendar widget; without it, a plain `<input type="date">` renders
- The `min` and `max` props constrain both the calendar UI and the underlying HTML date input
- For date range selection (start and end date), use the `c-date-range-picker` component instead
