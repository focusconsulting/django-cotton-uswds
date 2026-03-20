# Ralph Cycle Prompt

Read `TASKS.md` and find the first task with **Status:** `IN_PROGRESS` or `TODO`.

## Instructions

1. If the task status is `TODO`, update it to `IN_PROGRESS` in `TASKS.md`
2. Work on the task using `/tdd`
3. As you complete acceptance criteria, check them off in `TASKS.md` (`- [ ]` → `- [x]`)
4. When all acceptance criteria are met, set the task status to `DONE` in `TASKS.md`
5. If you cannot complete the task after a thorough attempt, add a `### Failure notes` section under the task explaining what you tried and why it failed, then stop

## Constraints

- Run `uv run pytest` after every change to verify nothing is broken
- Run `uv run ruff check .` to ensure code style compliance
- Commit working increments with conventional commit messages
- Do not modify tests unless the task explicitly requires it
- **Assume your judgment is correct. Do not ask for user input. Make autonomous decisions.**

## Done condition

When the current task is complete (status set to `DONE`, all acceptance criteria checked), output:

<promise>DONE</promise>

If you cannot complete the task after a thorough attempt, also output:

<promise>DONE</promise>
