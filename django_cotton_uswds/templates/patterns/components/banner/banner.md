# Banner

A government banner identifying official U.S. government websites and informing users about HTTPS security. Follows USWDS banner patterns.

## Props

| Prop                | Default | Description                                                                                      |
| ------------------- | ------- | ------------------------------------------------------------------------------------------------ |
| `header_text`       |         | Main header text (e.g., "An official website of the United States government")                   |
| `header_action`     |         | Action link text shown in the header (e.g., "Here's how you know")                              |
| `control_id`        |         | Unique ID for the accordion toggle linking the button to the expanded panel                      |
| `is_gov`            |         | Set to `"true"` to display the U.S. flag icon and the standard `.gov`/HTTPS guidance panels     |
| `content_primary`   |         | HTML content for the primary guidance panel (`.gov` domain info); shown when `is_gov="true"`    |
| `content_secondary` |         | HTML content for the secondary guidance panel (HTTPS info); shown when `is_gov="true"`          |
| `custom_content`    |         | HTML content for a custom banner body; shown when `is_gov="false"`                               |

## Example Usage

### Official .gov Banner (Default)

```django
<c-banner
    header_text="An official website of the United States government"
    header_action="Here's how you know"
    control_id="gov-banner"
    is_gov="true"
    content_primary="<p><strong>Official websites use .gov</strong><br />A <strong>.gov</strong> website belongs to an official government organization in the United States.</p>"
    content_secondary="<p><strong>Secure .gov websites use HTTPS</strong><br />A <strong>lock</strong> or <strong>https://</strong> means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.</p>"
/>
```

### Custom Banner

```django
<c-banner
    header_text="An official test banner"
    header_action="Click to learn more"
    control_id="custom-banner"
    is_gov="false"
    custom_content="<p>This is custom expandable content for a non-.gov banner.</p>"
/>
```

## Usage Notes

- Set `is_gov="true"` to display the U.S. flag icon alongside the standard `.gov` domain and HTTPS guidance panels
- Set `is_gov="false"` and provide `custom_content` for custom or non-government banner scenarios
- Each banner on a page requires a unique `control_id`
- The banner uses an internal accordion; USWDS JavaScript is required for the expand/collapse behavior
- Place the banner at the very top of the page, above the header
