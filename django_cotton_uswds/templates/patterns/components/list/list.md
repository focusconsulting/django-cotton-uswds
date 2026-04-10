# List

A styled list component that renders ordered, unordered, or unstyled lists using USWDS typography classes.

## Props

| Prop        | Default | Description                                                              |
| ----------- | ------- | ------------------------------------------------------------------------ |
| `list_type` |         | List style: `ordered`, `unstyled`, or leave empty for unordered (default)|

## Slots

| Slot      | Description                                |
| --------- | ------------------------------------------ |
| (default) | List items (`<li>` elements)               |

## Example Usage

### Unordered List (Default)

```django
<c-list>
    <li>Unordered list item one</li>
    <li>Unordered list item two</li>
    <li>Unordered list item three</li>
</c-list>
```

### Ordered List

```django
<c-list list_type="ordered">
    <li>First step</li>
    <li>Second step</li>
    <li>Third step</li>
</c-list>
```

### Unstyled List

Removes bullets and default list margins.

```django
<c-list list_type="unstyled">
    <li>Item without bullet</li>
    <li>Another item</li>
    <li>One more item</li>
</c-list>
```

## Usage Notes

- Omitting `list_type` (or leaving it empty) renders a standard `<ul class="usa-list">`
- The unstyled variant (`list_type="unstyled"`) is useful for navigation menus or custom list layouts where the default bullet styling is not wanted
- For icon-annotated lists, use the `c-icon-list` component instead
