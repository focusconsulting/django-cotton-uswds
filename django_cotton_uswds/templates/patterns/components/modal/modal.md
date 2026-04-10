# Modal

A dialog overlay that focuses user attention on a task or critical information, blocking interaction with the rest of the page. Follows USWDS modal patterns.

## Props

### `c-modal`

| Prop               | Default    | Description                                                                  |
| ------------------ | ---------- | ---------------------------------------------------------------------------- |
| `id`               |            | Unique ID for the modal element; also used in the trigger button's `aria-controls` |
| `href`             |            | Hash link matching the modal `id` (e.g., `"#example-modal"`)               |
| `button_text`      |            | Text for the trigger button that opens the modal                             |
| `heading_id`       |            | ID of the heading element inside the modal for `aria-labelledby`            |
| `body_id`          |            | ID of the body element inside the modal for `aria-describedby`              |
| `type`             |            | Set to `"large"` for a wider modal                                          |
| `is_forced_action` | `"false"`  | Set to `"true"` to hide the close button, requiring the user to take an explicit action |

### `c-modal.modal-header`

| Prop         | Default | Description                                       |
| ------------ | ------- | ------------------------------------------------- |
| `heading_id` |         | ID applied to the heading element inside the header |

### Sub-components

| Sub-component            | Description                                          |
| ------------------------ | ---------------------------------------------------- |
| `c-modal.modal-header`   | Container for the modal title                        |
| `c-modal.modal-body`     | Container for the modal body content                 |
| `c-modal.modal-footer`   | Container for modal action buttons                   |
| `c-modal.modal-close-button` | Close/action button within the modal footer     |

## Example Usage

### Default Modal

```django
<c-modal
    id="example-modal-1"
    href="#example-modal-1"
    button_text="Open Modal"
    heading_id="modal-1-heading"
    body_id="modal-1-description"
>
    <c-modal.modal-header heading_id="modal-1-heading">
        <h2>Are you sure you want to continue?</h2>
    </c-modal.modal-header>
    <c-modal.modal-body>
        <p id="modal-1-description">You have unsaved changes that will be lost.</p>
    </c-modal.modal-body>
    <c-modal.modal-footer>
        <c-button-group>
            <c-button-group.button-group-item>
                <c-modal.modal-close-button text="Continue without saving" />
            </c-button-group.button-group-item>
            <c-button-group.button-group-item>
                <c-modal.modal-close-button
                    text="Go back"
                    type="unstyled"
                    extra_classes="padding-105 text-center"
                />
            </c-button-group.button-group-item>
        </c-button-group>
    </c-modal.modal-footer>
</c-modal>
```

### Large Modal

```django
<c-modal
    id="example-modal-2"
    type="large"
    href="#example-modal-2"
    button_text="Open Large Modal"
    heading_id="modal-2-heading"
    body_id="modal-2-description"
>
    <c-modal.modal-header heading_id="modal-2-heading">
        <h2>Are you sure you want to continue?</h2>
    </c-modal.modal-header>
    <c-modal.modal-body>
        <p id="modal-2-description">You have unsaved changes that will be lost.</p>
    </c-modal.modal-body>
    <c-modal.modal-footer>
        <c-button-group>
            <c-button-group.button-group-item>
                <c-modal.modal-close-button text="Continue without saving" />
            </c-button-group.button-group-item>
            <c-button-group.button-group-item>
                <c-modal.modal-close-button
                    text="Go back"
                    type="unstyled"
                    extra_classes="padding-105 text-center"
                />
            </c-button-group.button-group-item>
        </c-button-group>
    </c-modal.modal-footer>
</c-modal>
```

### Forced Action Modal

The close button is hidden; users must choose an explicit action.

```django
<c-modal
    id="example-modal-3"
    href="#example-modal-3"
    button_text="Open modal with forced action"
    heading_id="modal-3-heading"
    body_id="modal-3-description"
    is_forced_action="true"
>
    <c-modal.modal-header heading_id="modal-3-heading">
        <h2>Your session will end soon.</h2>
    </c-modal.modal-header>
    <c-modal.modal-body>
        <p id="modal-3-description">
            You've been inactive for too long. Please choose to stay signed in
            or sign out. Otherwise, you'll be signed out automatically in 5 minutes.
        </p>
    </c-modal.modal-body>
    <c-modal.modal-footer>
        <c-button-group>
            <c-button-group.button-group-item>
                <c-modal.modal-close-button text="Yes, stay signed in" />
            </c-button-group.button-group-item>
            <c-button-group.button-group-item>
                <c-modal.modal-close-button
                    text="Sign out"
                    type="unstyled"
                    extra_classes="padding-105 text-center"
                />
            </c-button-group.button-group-item>
        </c-button-group>
    </c-modal.modal-footer>
</c-modal>
```

## Usage Notes

- Each modal on a page must have a unique `id`; the `href` must match that `id` with a leading `#`
- Pass matching `heading_id` to both `c-modal` (for `aria-labelledby`) and `c-modal.modal-header` (for the `id` on the heading element)
- Pass matching `body_id` to both `c-modal` (for `aria-describedby`) and the `<p>` inside `c-modal.modal-body`
- USWDS JavaScript is required to activate the modal show/hide behavior
- Use `is_forced_action="true"` only for critical decisions; always provide at least one actionable button to dismiss the modal
