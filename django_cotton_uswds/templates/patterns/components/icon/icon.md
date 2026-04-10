# Icon

An inline SVG icon from the USWDS sprite sheet. Renders a `<svg>` element referencing the named icon from the bundled sprite. Follows USWDS icon patterns.

## Props

| Prop    | Default      | Description                                                              |
| ------- | ------------ | ------------------------------------------------------------------------ |
| `icon`  |              | Name of the icon from the USWDS sprite (e.g., `search`, `close`, `info`) |
| `class` | `usa-icon`   | CSS class applied to the `<svg>` element                                 |

## Example Usage

### Basic Icon

```django
<c-icon icon="search" />
```

### Icon with Custom Class

```django
<c-icon icon="close" class="usa-icon usa-icon--size-3" />
```

### Icon Inside a Button

```django
<button class="usa-button" type="button">
    <c-icon icon="add" />
    Add item
</button>
```

### Icon Used as a Decorative Element in Text

```django
<p>
    <c-icon icon="info" />
    This information is important.
</p>
```

## Available Icon Names

The USWDS sprite includes icons such as: `accessibility_new`, `account_balance`, `add`, `alarm`, `arrow_back`, `arrow_forward`, `calendar_today`, `cancel`, `check`, `check_circle`, `close`, `credit_card`, `delete`, `directions`, `download`, `edit`, `error`, `event`, `facebook`, `file_download`, `flag`, `folder`, `github`, `help`, `home`, `info`, `instagram`, `launch`, `link`, `linkedin`, `lock`, `login`, `logout`, `mail`, `map`, `menu`, `navigate_before`, `navigate_next`, `notifications`, `people`, `person`, `phone`, `print`, `public`, `remove`, `rss_feed`, `save_alt`, `search`, `security`, `send`, `settings`, `share`, `star`, `support`, `twitter`, `upload_file`, `verified`, `visibility`, `warning`, `work`, `youtube`, `zoom_in`, `zoom_out`, and many more.

See the pattern library Icon component page for a full visual listing of all available icons.

## Usage Notes

- Icons are `aria-hidden="true"` and `focusable="false"` by default, making them decorative
- When an icon conveys meaning without accompanying text, add a visually hidden `<span class="usa-sr-only">` label nearby for screen reader users
- Use USWDS size utility classes (e.g., `usa-icon--size-3`, `usa-icon--size-4`) via the `class` prop to scale the icon
