# Plan: Ralph Task Runner

> Source: Grill session 2026-03-19

## Architectural decisions

- **Task source**: `TASKS.md` in project root, formatted as plan phases
- **Execution engine**: Local `ralph.sh` (not the plugin)
- **Permissions model**: `allow: ["*"]` with denylist in `settings.local.json` (no `--dangerously-skip-permissions` — that would bypass the denylist)
- **Test strategy**: Each task is executed via the `/tdd` skill
- **Autonomy**: Cycle prompt instructs Claude to assume its judgment is correct and never ask for user input
- **Scoped destructive ops**: `rm` and `mv` allowed within the project directory, blocked everywhere else

---

## Phase 1: TASKS.md format and parsing

**User stories**: As a developer, I want Ralph to read structured tasks from a file so I can queue up work and walk away.

### What to build

Define the `TASKS.md` format. Each task mirrors a plan phase:

```markdown
## TASK-1: <Title>

**Status:** TODO | IN_PROGRESS | DONE | BLOCKED

**User stories**: ...

### What to build
...

### Acceptance criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

Update `ralph.sh` to:
1. Read `TASKS.md` and find the first task with `**Status:** TODO`
2. Extract the task content (title, description, acceptance criteria)
3. Pass it to Claude as the prompt for that cycle

### Acceptance criteria

- [ ] `TASKS.md` format is documented with an example task
- [ ] `ralph.sh` correctly parses the first `TODO` task from `TASKS.md`
- [ ] Skips tasks with status `DONE`, `IN_PROGRESS`, or `BLOCKED`

---

## Phase 2: Task lifecycle (completion and status updates)

**User stories**: As a developer, I want Ralph to mark tasks done when complete and move to the next one automatically.

### What to build

After each cycle, Ralph (via Claude) should:
1. Set the task's status to `IN_PROGRESS` when starting
2. Check off acceptance criteria as they pass
3. Set status to `DONE` when all acceptance criteria are met
4. Read `TASKS.md` again and pick up the next `TODO` task
5. Exit cleanly when all tasks are `DONE`

### Acceptance criteria

- [ ] Task status transitions from `TODO` → `IN_PROGRESS` → `DONE`
- [ ] Acceptance criteria checkboxes are checked off as they pass
- [ ] Ralph moves to the next task after completing one
- [ ] Ralph exits with code 0 when all tasks are done

---

## Phase 3: Failure handling (3 strikes and BLOCKED)

**User stories**: As a developer, I want Ralph to skip stuck tasks so it doesn't waste all its iterations on one broken thing.

### What to build

Track attempt count per task. After 3 failed attempts (tests don't pass, can't satisfy acceptance criteria):
1. Set status to `BLOCKED`
2. Write failure context inline under the task in `TASKS.md` (what was tried, what failed)
3. Move to the next `TODO` task
4. Carry forward awareness of the blocked task's failure so Ralph avoids repeating the same mistake on related tasks

### Acceptance criteria

- [ ] Ralph retries a failing task up to 3 times
- [ ] After 3 failures, task status is set to `BLOCKED`
- [ ] Failure context (what was tried, why it failed) is written inline in `TASKS.md`
- [ ] Ralph moves to the next task after blocking one

---

## Phase 4: Autonomous cycle prompt

**User stories**: As a developer, I want Ralph to run without asking me questions so I can go AFK.

### What to build

Replace the current `PROMPT.md` template with a cycle prompt that:
1. Instructs Claude to read `TASKS.md` and pick the first `TODO` task
2. Tells Claude to run `/tdd` on the task
3. Includes the directive: assume your judgment is correct, do not ask for user input, make autonomous decisions
4. Preserves existing constraints (run pytest, run ruff, commit working increments)
5. Uses `<promise>DONE</promise>` when the current task is complete (triggering the next cycle)

### Acceptance criteria

- [ ] Cycle prompt includes autonomous decision-making directive
- [ ] Cycle prompt instructs Claude to use `/tdd` for each task
- [ ] Cycle prompt preserves pytest/ruff/commit constraints
- [ ] Claude does not prompt for user input during execution

---

## Phase 5: Poll mode

**User stories**: As a developer, I want Ralph to optionally keep watching for new tasks instead of exiting.

### What to build

Add a `--poll` flag to `ralph.sh`. When set:
1. After all tasks are `DONE`, instead of exiting, wait and re-read `TASKS.md` on the next cycle
2. If new `TODO` tasks appear, pick them up
3. Without `--poll`, exit cleanly when all tasks are done (default behavior)

### Acceptance criteria

- [ ] `--poll` flag is accepted by `ralph.sh`
- [ ] Without `--poll`, Ralph exits when all tasks are done
- [ ] With `--poll`, Ralph continues looping and picks up newly added tasks

---

## Phase 6: Project-scoped permissions

**User stories**: As a developer, I want Ralph to be safe when running autonomously — allowed to modify project files but blocked from touching anything else.

### What to build

Update `settings.local.json` deny rules to:
1. Allow `rm` and `mv` within the project directory
2. Block `rm` and `mv` outside the project directory
3. Keep all existing denylist entries

Document the recommended denylist for AFK Ralph operation.

### Acceptance criteria

- [ ] `rm` within project directory is allowed
- [ ] `mv` within project directory is allowed
- [ ] `rm` and `mv` outside project directory are blocked
- [ ] All existing denylist entries are preserved
