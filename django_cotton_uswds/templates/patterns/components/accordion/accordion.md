# Accordion

A vertically stacked list of headings that reveal or hide associated sections of content. Follows USWDS accordion patterns.

## Props

### `c-accordion`

| Prop           | Default | Description                                                                             |
| -------------- | ------- | --------------------------------------------------------------------------------------- |
| `type`         |         | Accordion style: leave empty for borderless (default), `bordered`, or `multiselectable` |
| `extra_classes`|         | Additional CSS classes to apply to the accordion wrapper                                |

### `c-accordion-item`

| Prop            | Default                                | Description                                       |
| --------------- | -------------------------------------- | ------------------------------------------------- |
| `heading`       |                                        | The heading text displayed in the accordion button |
| `control_id`    |                                        | Unique ID linking the button to its content panel  |
| `is_expanded`   | `False`                                | Whether the panel is open on initial render        |
| `heading_class` | `usa-accordion__heading`               | CSS class for the heading element                  |
| `button_class`  | `usa-accordion__button`                | CSS class for the button element                   |
| `content_class` | `usa-accordion__content usa-prose`     | CSS class for the content panel                    |

## Example Usage

### Borderless (Default)

```
<c-accordion>
    <c-accordion-item heading="Accordion item 1" control_id="a1" :is_expanded="True">
        <p>Content for accordion item 1.</p>
    </c-accordion-item>
    <c-accordion-item heading="Accordion item 2" control_id="a2">
        <p>Content for accordion item 2.</p>
    </c-accordion-item>
    <c-accordion-item heading="Accordion item 3" control_id="a3">
        <p>Content for accordion item 3.</p>
    </c-accordion-item>
</c-accordion>
```

### Bordered

```django
<c-accordion type="bordered">
    <c-accordion-item heading="Accordion item 1" control_id="b1">
        <p>Content for accordion item 1.</p>
    </c-accordion-item>
    <c-accordion-item heading="Accordion item 2" control_id="b2">
        <p>Content for accordion item 2.</p>
    </c-accordion-item>
    <c-accordion-item heading="Accordion item 3" control_id="b3">
        <p>Content for accordion item 3.</p>
    </c-accordion-item>
</c-accordion>
```

### Multiselectable

```django
<c-accordion type="multiselectable">
    <c-accordion-item heading="Accordion item 1" control_id="c1">
        <p>Content for accordion item 1.</p>
    </c-accordion-item>
    <c-accordion-item heading="Accordion item 2" control_id="c2">
        <p>Content for accordion item 2.</p>
    </c-accordion-item>
    <c-accordion-item heading="Accordion item 3" control_id="c3">
        <p>Content for accordion item 3.</p>
    </c-accordion-item>
</c-accordion>
```

## Usage Notes

- Each `c-accordion-item` must have a unique `control_id` on the page
- By default only one panel can be open at a time; use `type="multiselectable"` to allow multiple open panels simultaneously
- Set `:is_expanded="True"` on an item to have it open on page load
- Accordion content is passed as slot content between the opening and closing `c-accordion-item` tags
