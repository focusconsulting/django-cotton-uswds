# Button Group

A container for grouping related buttons. Supports a standard stacked layout and a segmented (toolbar) layout where buttons share borders. Follows USWDS button group patterns.

## Props

### `c-button-group`

| Prop         | Default | Description                                                      |
| ------------ | ------- | ---------------------------------------------------------------- |
| `segemented` |         | Set to `"true"` to render buttons as a connected segmented group |

### `c-button-group.button-group-item`

The `c-button-group.button-group-item` component is a wrapper `<li>` item. It accepts no props; place a `c-button` inside it.

## Example Usage

### Default Button Group

Buttons are stacked and styled independently.

```django
<c-button-group>
    <c-button-group.button-group-item>
        <c-button text="Back" variant="outline" />
    </c-button-group.button-group-item>
    <c-button-group.button-group-item>
        <c-button text="Continue" />
    </c-button-group.button-group-item>
</c-button-group>
```

### Segmented Button Group

Buttons share borders and appear as a connected unit, useful for toggle controls.

```django
<c-button-group segemented="true">
    <c-button-group.button-group-item>
        <c-button text="Map" />
    </c-button-group.button-group-item>
    <c-button-group.button-group-item>
        <c-button text="Hybrid" variant="outline" />
    </c-button-group.button-group-item>
    <c-button-group.button-group-item>
        <c-button text="Satellite" variant="outline" />
    </c-button-group.button-group-item>
</c-button-group>
```

### Segmented Group with Accent Cool

```django
<c-button-group segemented="true">
    <c-button-group.button-group-item>
        <c-button text="Map" variant="accent-cool" />
    </c-button-group.button-group-item>
    <c-button-group.button-group-item>
        <c-button text="Hybrid" variant="accent-cool" />
    </c-button-group.button-group-item>
    <c-button-group.button-group-item>
        <c-button text="Satellite" variant="accent-cool" />
    </c-button-group.button-group-item>
</c-button-group>
```

### Segmented Group with Outline Inverse

Use on dark backgrounds.

```django
<c-button-group segemented="true">
    <c-button-group.button-group-item>
        <c-button text="Map" variant="outline-inverse" />
    </c-button-group.button-group-item>
    <c-button-group.button-group-item>
        <c-button text="Hybrid" variant="outline-inverse" />
    </c-button-group.button-group-item>
    <c-button-group.button-group-item>
        <c-button text="Satellite" variant="outline-inverse" />
    </c-button-group.button-group-item>
</c-button-group>
```

## Usage Notes

- Note: the `segemented` prop name preserves the original USWDS Cotton component spelling
- In a segmented group, all buttons should use the same `variant` for visual consistency
- Each button must be wrapped in a `c-button-group.button-group-item` element
- The default layout is suitable for form navigation (e.g., Back / Continue); the segmented layout is better for view-toggle controls
