# Breadcrumb

A secondary navigation trail showing the user's location within a site hierarchy. Follows USWDS breadcrumb patterns.

## Props

### `c-breadcrumb`

| Prop      | Default  | Description                                                                         |
| --------- | -------- | ----------------------------------------------------------------------------------- |
| `wrapped` | `"false"`| Set to `"true"` to allow breadcrumb items to wrap to multiple lines on small screens |

### `c-breadcrumb.breadcrumb-item`

| Prop           | Default | Description                                                                    |
| -------------- | ------- | ------------------------------------------------------------------------------ |
| `href`         |         | URL the breadcrumb item links to; leave empty for unlinked items               |
| `list_item`    |         | Display text for the breadcrumb item                                           |
| `aria_current` |         | Set to `"page"` on the current page item to mark it for screen readers        |

## Example Usage

### Default Breadcrumb

```django
<c-breadcrumb>
    <c-breadcrumb.breadcrumb-item href="/" list_item="Home" />
    <c-breadcrumb.breadcrumb-item href="/section/" list_item="Section" />
    <c-breadcrumb.breadcrumb-item href="" list_item="Current Page" aria_current="page" />
</c-breadcrumb>
```

### Breadcrumb with Wrapping

Use `wrapped="true"` to allow the trail to wrap onto multiple lines on narrow viewports.

```django
<c-breadcrumb wrapped="true">
    <c-breadcrumb.breadcrumb-item href="/" list_item="Home" />
    <c-breadcrumb.breadcrumb-item href="/section/" list_item="Section" />
    <c-breadcrumb.breadcrumb-item href="" list_item="Current Page" aria_current="page" />
</c-breadcrumb>
```

## Usage Notes

- Mark the final (current page) item with `aria_current="page"` for accessibility
- The current page item does not need a meaningful `href` since it represents the user's current location
- By default, long breadcrumb trails are truncated with CSS on smaller screens; use `wrapped="true"` to show all items
