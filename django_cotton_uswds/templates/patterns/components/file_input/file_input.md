# File Input

A form input that allows users to attach one or more files. Must be wrapped in a `c-form-group`. Follows USWDS file input patterns.

## Props

| Prop             | Default | Description                                                                                                |
| ---------------- | ------- | ---------------------------------------------------------------------------------------------------------- |
| `id`             |         | Unique ID for the input; defaults to `file-input-{selection_type}` if not provided                        |
| `name`           |         | Form field name submitted with the form                                                                    |
| `selection_type` |         | Visual/semantic hint for the type of selection: `single`, `multiple`, `specific`, `wildcard`, or `error` |
| `accept`         |         | Comma-separated list of accepted MIME types or file extensions (e.g., `".pdf,.txt"`, `"image/*"`)        |
| `multiple`       |         | Set to `"true"` to allow selecting multiple files at once                                                 |
| `disabled`       |         | Set to `"true"` to disable the input                                                                      |
| `required`       |         | Set to `"true"` to mark the input as required                                                             |

## Example Usage

### Single File Input

```django
<c-form-group>
    <c-file-input selection_type="single" />
</c-form-group>
```

### Disabled File Input

```django
<c-form-group>
    <c-file-input selection_type="single" disabled="true" />
</c-form-group>
```

### Specific File Types

Accept only PDF and TXT files.

```django
<c-form-group>
    <c-file-input
        selection_type="specific"
        accept=".pdf,.txt"
        multiple="true"
    />
</c-form-group>
```

### Images Only

Accept any image format using a MIME type wildcard.

```django
<c-form-group>
    <c-file-input
        selection_type="wildcard"
        accept="image/*"
        multiple="true"
    />
</c-form-group>
```

### Multiple Files of Any Kind

```django
<c-form-group>
    <c-file-input
        selection_type="multiple"
        multiple="true"
    />
</c-form-group>
```

### File Input with Error State

```django
<c-form-group>
    <c-file-input
        selection_type="error"
        error="true"
    />
</c-form-group>
```

## Usage Notes

- Always wrap `c-file-input` in a `c-form-group` for proper USWDS form layout and hint/error message display
- The `selection_type` prop is used for semantic labeling and pattern library display; the actual enforcement of file types is handled by the `accept` attribute
- Set `multiple="true"` to allow multi-file selection; browsers display a multi-select file dialog
- USWDS JavaScript enhances the file input with a drag-and-drop zone and preview of selected file names
