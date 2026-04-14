# Step Indicator

A multi-step progress tracker that shows the user's position within a multi-page form or process. Follows USWDS step indicator patterns.

## Props

### `c-step-indicator`

| Prop             | Default | Description                                                                                          |
| ---------------- | ------- | ---------------------------------------------------------------------------------------------------- |
| `current_step`   |         | The number of the step currently being completed (displayed in the header counter)                   |
| `total_steps`    |         | Total number of steps in the process (displayed in the header counter)                               |
| `segment_name`   |         | Name of the current step displayed in the header heading                                             |
| `indicator_type` |         | Visual style: leave empty for default, `"no-labels"`, `"center"`, `"counters"`, or `"counters-sm"` |

### `c-step-indicator.step-item`

| Prop            | Default | Description                                                                               |
| --------------- | ------- | ----------------------------------------------------------------------------------------- |
| `name`          |         | Display label for this step segment                                                       |
| `segment_state` |         | State of this step: `"complete"`, `"current"`, or `"incomplete"`                         |

## Example Usage

### Default Step Indicator (Middle of Process)

```django
<c-step-indicator current_step="3" total_steps="5" segment_name="Supporting documents">
    <c-step-indicator.step-item name="Personal information" segment_state="complete" />
    <c-step-indicator.step-item name="Household status" segment_state="complete" />
    <c-step-indicator.step-item name="Supporting documents" segment_state="current" />
    <c-step-indicator.step-item name="Signature" segment_state="incomplete" />
    <c-step-indicator.step-item name="Review and submit" segment_state="incomplete" />
</c-step-indicator>
```

### Default Step Indicator (Beginning of Process)

```django
<c-step-indicator current_step="1" total_steps="5" segment_name="Personal information">
    <c-step-indicator.step-item name="Personal information" segment_state="current" />
    <c-step-indicator.step-item name="Household status" segment_state="incomplete" />
    <c-step-indicator.step-item name="Supporting documents" segment_state="incomplete" />
    <c-step-indicator.step-item name="Signature" segment_state="incomplete" />
    <c-step-indicator.step-item name="Review and submit" segment_state="incomplete" />
</c-step-indicator>
```

### Default Step Indicator (End of Process)

```django
<c-step-indicator current_step="5" total_steps="5" segment_name="Review and submit">
    <c-step-indicator.step-item name="Personal information" segment_state="complete" />
    <c-step-indicator.step-item name="Household status" segment_state="complete" />
    <c-step-indicator.step-item name="Supporting documents" segment_state="complete" />
    <c-step-indicator.step-item name="Signature" segment_state="complete" />
    <c-step-indicator.step-item name="Review and submit" segment_state="current" />
</c-step-indicator>
```

### No Labels

Hides the step name labels beneath the segments.

```django
<c-step-indicator indicator_type="no-labels" current_step="3" total_steps="5" segment_name="Supporting documents">
    <c-step-indicator.step-item name="Personal information" segment_state="complete" />
    <c-step-indicator.step-item name="Household status" segment_state="complete" />
    <c-step-indicator.step-item name="Supporting documents" segment_state="current" />
    <c-step-indicator.step-item name="Signature" segment_state="incomplete" />
    <c-step-indicator.step-item name="Review and submit" segment_state="incomplete" />
</c-step-indicator>
```

### Centered

Centers the step labels beneath each segment.

```django
<c-step-indicator indicator_type="center" current_step="3" total_steps="5" segment_name="Supporting documents">
    <c-step-indicator.step-item name="Personal information" segment_state="complete" />
    <c-step-indicator.step-item name="Household status" segment_state="complete" />
    <c-step-indicator.step-item name="Supporting documents" segment_state="current" />
    <c-step-indicator.step-item name="Signature" segment_state="incomplete" />
    <c-step-indicator.step-item name="Review and submit" segment_state="incomplete" />
</c-step-indicator>
```

### Counters

Displays step numbers inside each segment circle.

```django
<c-step-indicator indicator_type="counters" current_step="3" total_steps="5" segment_name="Supporting documents">
    <c-step-indicator.step-item name="Personal information" segment_state="complete" />
    <c-step-indicator.step-item name="Household status" segment_state="complete" />
    <c-step-indicator.step-item name="Supporting documents" segment_state="current" />
    <c-step-indicator.step-item name="Signature" segment_state="incomplete" />
    <c-step-indicator.step-item name="Review and submit" segment_state="incomplete" />
</c-step-indicator>
```

### Small Counters

Smaller version of the counters style.

```django
<c-step-indicator indicator_type="counters-sm" current_step="3" total_steps="5" segment_name="Supporting documents">
    <c-step-indicator.step-item name="Personal information" segment_state="complete" />
    <c-step-indicator.step-item name="Household status" segment_state="complete" />
    <c-step-indicator.step-item name="Supporting documents" segment_state="current" />
    <c-step-indicator.step-item name="Signature" segment_state="incomplete" />
    <c-step-indicator.step-item name="Review and submit" segment_state="incomplete" />
</c-step-indicator>
```

## Usage Notes

- Exactly one `c-step-indicator.step-item` should have `segment_state="current"` per indicator
- The `current_step`, `total_steps`, and `segment_name` props populate the header counter and heading; omit all three to hide the header entirely
- The `indicator_type` controls only visual presentation; step progression logic must be handled in your view/form
- Place the step indicator above the form content for the current step
