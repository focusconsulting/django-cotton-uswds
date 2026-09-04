# Process List

A process list displays a series of steps or stages in a process, helping users understand what to expect.

## Props

### `c-process_list`

The wrapper `<ol>`. Any undeclared attribute is passed straight through to the
`<ol>` element, so an accessible name can be set with `aria-label` (or
`aria-labelledby` pointing at a visible heading).

| Prop            | Default | Description                                                  |
| --------------- | ------- | ------------------------------------------------------------ |
| `extra_classes` |         | Additional CSS classes for the list (e.g., `margin-top-0`)   |

### `c-process_list.item`

| Prop              | Default | Description                                                      |
| ----------------- | ------- | ---------------------------------------------------------------- |
| `heading`         |         | The heading text for the step                                    |
| `heading_tag`     | `h4`    | HTML tag for heading (`h4`, `p`, etc.)                           |
| `heading_classes` |         | Additional CSS classes for the heading (e.g., `font-sans-xl`)    |
| `sr_prefix`       |         | Screen-reader-only text rendered inside the heading, before `heading` (e.g., `Step 1 of 3: `) |
| `extra_classes`   |         | Additional CSS classes for the list item (e.g., `padding-bottom-4`) |

Undeclared attributes are passed through to the `<li>` element.

`sr_prefix` renders as a `usa-sr-only` span inside the heading element, so it
composes into the heading's accessible name rather than replacing it: sighted
users see `Start a process`, screen reader users hear
`Step 1 of 3: Start a process`.

## Example Usage

### Default Process List

```django
<c-process_list>
    <c-process_list.item heading="Start a process">
        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</p>
        <ul>
            <li>First sub-item</li>
            <li>Second sub-item</li>
        </ul>
    </c-process_list.item>
    <c-process_list.item heading="Proceed to the second step">
        <p>More description text here.</p>
    </c-process_list.item>
    <c-process_list.item heading="Complete the step-by-step process">
        <p>Final step description.</p>
    </c-process_list.item>
</c-process_list>
```

### Custom Sizing (No Body Text)

```django
<c-process_list>
    <c-process_list.item 
        heading="Start a process." 
        heading_tag="p" 
        extra_classes="padding-bottom-4"
    />
    <c-process_list.item 
        heading="Proceed to the second step." 
        heading_tag="p" 
        extra_classes="padding-bottom-4"
    />
    <c-process_list.item 
        heading="Complete the step-by-step process." 
        heading_tag="p"
    />
</c-process_list>
```

### Custom Sizing (With Body Text)

```django
<c-process_list>
    <c-process_list.item 
        heading="Start a process."
        heading_classes="font-sans-xl line-height-sans-1"
        extra_classes="padding-bottom-4"
    >
        <p class="font-sans-lg margin-top-1 text-light">
            Nullam sit amet enim. Suspendisse id velit vitae ligula volutpat condimentum.
        </p>
    </c-process_list.item>
    <c-process_list.item 
        heading="Proceed to the second step."
        heading_classes="font-sans-xl line-height-sans-1"
        extra_classes="padding-bottom-4"
    >
        <p class="font-sans-lg margin-top-1 text-light">
            Suspendisse id velit vitae ligula volutpat condimentum. Aliquam erat volutpat.
        </p>
    </c-process_list.item>
    <c-process_list.item 
        heading="Complete the step-by-step process."
        heading_classes="font-sans-xl line-height-sans-1"
    >
        <p class="font-sans-lg margin-top-1 text-light">
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
        </p>
    </c-process_list.item>
</c-process_list>
```

### Labelled List With Screen Reader Step Prefixes

```django
<c-process_list aria-label="Process steps">
    <c-process_list.item heading="Start a process" sr_prefix="Step 1 of 3: ">
        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</p>
    </c-process_list.item>
    <c-process_list.item heading="Proceed to the second step" sr_prefix="Step 2 of 3: ">
        <p>Nullam sit amet enim. Suspendisse id velit vitae ligula volutpat condimentum.</p>
    </c-process_list.item>
    <c-process_list.item heading="Complete the step-by-step process" sr_prefix="Step 3 of 3: ">
        <p>Aliquam erat volutpat. Sed quis velit.</p>
    </c-process_list.item>
</c-process_list>
```
