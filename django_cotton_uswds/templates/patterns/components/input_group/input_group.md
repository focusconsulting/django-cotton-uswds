# Input Group

A wrapper that combines a text input with one or both of a prefix and suffix element. Supports validation states and width modifiers. Follows USWDS input group patterns.

## Props

| Prop      | Default | Description                                                               |
| --------- | ------- | ------------------------------------------------------------------------- |
| `error`   |         | Error message text; applies the error styling to the group                |
| `success` |         | Set to `"true"` to apply the success styling to the group                |
| `width`   |         | Width modifier for the group: `2xs`, `xs`, `sm`, `md`, `lg`, `xl`, `2xl` |
| `class`   |         | Additional CSS classes for the input group wrapper                        |

## Slots

| Slot      | Description                                                                                 |
| --------- | ------------------------------------------------------------------------------------------- |
| (default) | A `c-input-prefix` and/or `c-input-suffix` wrapping a `c-text-input`                       |

## Example Usage

### Currency Input (Dollar)

```django
<c-label id="price-usd" label="Price" hint="Enter price in US dollars." />
<c-input-group>
    <c-input-prefix>$</c-input-prefix>
    <c-text-input id="price-usd" name="price_usd" type="text" inputmode="numeric" />
    <c-input-suffix>USD</c-input-suffix>
</c-input-group>
```

### Currency Input (Euro)

```django
<c-label id="price-eur" label="Price" hint="Enter price in euros." />
<c-input-group>
    <c-input-prefix>€</c-input-prefix>
    <c-text-input id="price-eur" name="price_eur" type="text" inputmode="numeric" />
    <c-input-suffix>EUR</c-input-suffix>
</c-input-group>
```

### Temperature

```django
<c-label id="temperature" label="Temperature" hint="Enter temperature." />
<c-input-group>
    <c-input-prefix>From</c-input-prefix>
    <c-text-input id="temperature" name="temperature" type="text" inputmode="numeric" />
    <c-input-suffix>°F</c-input-suffix>
</c-input-group>
```

### Discount Percentage

```django
<c-label id="discount" label="Discount" hint="Enter discount amount." />
<c-input-group>
    <c-input-prefix>-</c-input-prefix>
    <c-text-input id="discount" name="discount" type="text" inputmode="numeric" />
    <c-input-suffix>%</c-input-suffix>
</c-input-group>
```

### Website URL

```django
<c-label id="website" label="Website" hint="Enter your website URL." />
<c-input-group>
    <c-input-prefix>https://</c-input-prefix>
    <c-text-input id="website" name="website" type="url" />
    <c-input-suffix>.com</c-input-suffix>
</c-input-group>
```

### Social Media Handle

```django
<c-label id="twitter" label="Twitter handle" hint="Enter your Twitter username." />
<c-input-group>
    <c-input-prefix>@</c-input-prefix>
    <c-text-input id="twitter" name="twitter" type="text" />
    <c-input-suffix><c-icon icon="launch" /></c-input-suffix>
</c-input-group>
```

### Search with Icon Prefix

```django
<c-label id="search-products" label="Search products" hint="Enter product name or SKU." />
<c-input-group>
    <c-input-prefix><c-icon icon="search" /></c-input-prefix>
    <c-text-input id="search-products" name="search_query" type="search" />
    <c-input-suffix>in Stock</c-input-suffix>
</c-input-group>
```

### With Error State

```django
<c-label id="amount-error" label="Amount" hint="Enter the amount." error="Please enter a valid amount." />
<c-input-group error="Please enter a valid amount.">
    <c-input-prefix>$</c-input-prefix>
    <c-text-input id="amount-error" name="amount_error" type="text" inputmode="numeric" error="Please enter a valid amount." />
    <c-input-suffix>USD</c-input-suffix>
</c-input-group>
```

### With Success State

```django
<c-label id="amount-success" label="Amount" />
<c-input-group success="true">
    <c-input-prefix>$</c-input-prefix>
    <c-text-input id="amount-success" name="amount_success" type="text" value="1,250.00" success="true" inputmode="numeric" />
    <c-input-suffix>USD</c-input-suffix>
</c-input-group>
```

### Small Width Group

```django
<c-label id="zip-ext" label="ZIP+4" hint="Last 4 digits." />
<c-input-group width="sm">
    <c-input-prefix>-</c-input-prefix>
    <c-text-input id="zip-ext" name="zip_ext" type="text" inputmode="numeric" pattern="\d{4}" />
</c-input-group>
```

## Usage Notes

- `c-input-group` is the required wrapper for any `c-input-prefix` or `c-input-suffix` usage
- Apply validation states (`error`, `success`) to both `c-input-group` and the inner `c-text-input` so that both the border styling and the input styling update together
- For a pre-built currency input with `$` prefix, use the dedicated `c-currency-input` component
- Prefix and suffix elements are `aria-hidden="true"` and are decorative only
