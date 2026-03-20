# Tasks

<!-- Ralph reads this file to find work. Each task follows the format below. -->

<!--
## TASK-N: Title

**Status:** TODO | IN_PROGRESS | DONE | BLOCKED

**User stories**: As a <role>, I want <goal> so that <benefit>.

### What to build

Description of the work.

### Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
-->

## TASK-1: Add breadcrumb component

**Status:** TODO

**User stories**: As a developer, I want a `<c-breadcrumb>` component so that I can add USWDS-styled breadcrumb navigation to my pages without writing raw HTML.

### What to build

Create a Cotton component that wraps the USWDS breadcrumb markup. It should support a list of links and render the final item as the current page (non-linked).

### Acceptance criteria

- [ ] `<c-breadcrumb>` component renders valid USWDS breadcrumb HTML
- [ ] Supports an arbitrary number of breadcrumb items
- [ ] The last item displays as plain text (current page), not a link
- [ ] Component is documented in the demo app
