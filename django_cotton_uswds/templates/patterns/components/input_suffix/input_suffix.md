# Input Suffix

A decorative element placed after a text input to provide context about the expected value (e.g., a unit of measurement or icon). Must be used inside a `c-input-group` wrapper alongside `c-text-input`. Follows USWDS input suffix patterns.

## Props

| Prop    | Default | Description                                   |
| ------- | ------- | --------------------------------------------- |
| `class` |         | Additional CSS classes for the suffix element |

## Slots

| Slot      | Description                                             |
| --------- | ------------------------------------------------------- |
| (default) | Suffix content: a text string or a `c-icon` component  |

## Example Usage

### Unit of Measurement Suffix

```django
<c-label id="weight" label="Weight" hint="Enter weight in pounds." />
<c-input-group>
    <c-text-input
        id="weight"
        name="weight"
        type="text"
        inputmode="numeric"
    />
    <c-input-suffix>lbs</c-input-suffix>
</c-input-group>
```

### Search Icon Suffix

```django
<c-label id="search-field" label="Search" hint="Enter search terms." />
<c-input-group>
    <c-text-input
        id="search-field"
        name="search"
        type="search"
    />
    <c-input-suffix>
        <c-icon icon="search" />
    </c-input-suffix>
</c-input-group>
```

## Usage Notes

- `c-input-suffix` must be placed inside a `c-input-group` wrapper
- The suffix is marked `aria-hidden="true"` automatically; it is decorative and not read by screen readers
- Use text strings for units or abbreviations (e.g., `lbs`, `USD`, `%`) and `c-icon` for icon suffixes
- To add both a prefix and a suffix, use `c-input-group` with both `c-input-prefix` and `c-input-suffix`; see the `c-input-group` component for that pattern
