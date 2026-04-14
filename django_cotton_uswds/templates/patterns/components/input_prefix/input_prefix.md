# Input Prefix

A decorative element placed before a text input to provide context about the expected value (e.g., a currency symbol or icon). Must be used inside a `c-input-group` wrapper alongside `c-text-input`. Follows USWDS input prefix patterns.

## Props

| Prop    | Default | Description                                   |
| ------- | ------- | --------------------------------------------- |
| `class` |         | Additional CSS classes for the prefix element |

## Slots

| Slot      | Description                                             |
| --------- | ------------------------------------------------------- |
| (default) | Prefix content: a text string or a `c-icon` component  |

## Example Usage

### Dollar Sign Prefix

```django
<c-label id="price" label="Item price" hint="Enter the dollar amount." />
<c-input-group>
    <c-input-prefix>$</c-input-prefix>
    <c-text-input
        id="price"
        name="price"
        type="text"
        inputmode="numeric"
    />
</c-input-group>
```

### Credit Card Icon Prefix

```django
<c-label id="cc-number" label="Credit card number" hint="Enter your 16-digit card number." />
<c-input-group>
    <c-input-prefix>
        <c-icon icon="credit_card" />
    </c-input-prefix>
    <c-text-input
        id="cc-number"
        name="cc_number"
        type="text"
        inputmode="numeric"
    />
</c-input-group>
```

## Usage Notes

- `c-input-prefix` must be placed inside a `c-input-group` wrapper
- The prefix is marked `aria-hidden="true"` automatically; it is decorative and not read by screen readers
- Use text strings for units or symbols (e.g., `$`, `€`, `@`) and `c-icon` for icon prefixes
- To add both a prefix and a suffix, use `c-input-group` with `c-input-prefix` combined with `c-input-suffix`; see the `c-input-group` component for that pattern
