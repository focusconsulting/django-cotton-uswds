# Search

A search form component with a text input and submit button. Supports default, big, and small size variants. Follows USWDS search patterns.

## Props

| Prop          | Default | Description                                                                         |
| ------------- | ------- | ----------------------------------------------------------------------------------- |
| `id`          |         | ID applied to the search input; also used as the `name` attribute on the input     |
| `search_type` |         | Size variant: leave empty for the default size, `"big"` for large, `"small"` for compact |

## Example Usage

### Default Search

```django
<c-search id="search-field" />
```

### Big Search

```django
<c-search search_type="big" id="search-field-big" />
```

### Small Search

```django
<c-search search_type="small" id="search-field-small" />
```

## Usage Notes

- The small variant (`search_type="small"`) hides the "Search" button label, showing only the search icon
- The `id` prop is used for both the input `id` and `name` attributes, and for the `<label>` `for` attribute (the label is visually hidden via `usa-sr-only`)
- Wrap `c-search` in a `<header>` or landmark region so screen reader users can find it easily
