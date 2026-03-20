#!/usr/bin/env bash
set -euo pipefail

TASKS_FILE="TASKS.md"
STATE_DIR=".ralph"
MAX_ATTEMPTS=3
POLL=false

# ── Parse flags ──────────────────────────────────────────────────────────────

while [[ $# -gt 0 ]]; do
  case "$1" in
    --poll) POLL=true; shift ;;
    *) echo "[ralph] Unknown option: $1"; exit 1 ;;
  esac
done

if [ ! -f "$TASKS_FILE" ]; then
  echo "[ralph] Error: $TASKS_FILE not found"
  exit 1
fi

mkdir -p "$STATE_DIR"

# ── Task parsing helpers ─────────────────────────────────────────────────────

# Print the TASK-N id of the first task matching the given status.
find_task_by_status() {
  local status="$1"
  awk -v st="$status" '
    /^## TASK-[0-9]+:/ {
      match($0, /TASK-[0-9]+/)
      id = substr($0, RSTART, RLENGTH)
    }
    id && $0 ~ "^\\*\\*Status:\\*\\* " st {
      print id
      exit
    }
  ' "$TASKS_FILE"
}

# Update a task's status in TASKS.md (used only for BLOCKED transitions).
set_task_status() {
  local task_id="$1"
  local new_status="$2"
  awk -v task="$task_id" -v status="$new_status" '
    /^## TASK-[0-9]+:/ { found = index($0, task) }
    found && /^\*\*Status:\*\*/ {
      $0 = "**Status:** " status
      found = 0
    }
    { print }
  ' "$TASKS_FILE" > "${TASKS_FILE}.tmp" && mv "${TASKS_FILE}.tmp" "$TASKS_FILE"
}

# Append a failure-context section to a blocked task.
add_failure_context() {
  local task_id="$1"
  local attempts="$2"
  awk -v task="$task_id" -v n="$attempts" '
    /^## TASK-[0-9]+:/ { in_task = index($0, task) }
    in_task && /^---$/ {
      print ""
      print "### Failure context"
      print ""
      print "Blocked after " n " failed attempts. Review conversation history or logs for details on what was tried."
      print ""
      in_task = 0
    }
    { print }
  ' "$TASKS_FILE" > "${TASKS_FILE}.tmp" && mv "${TASKS_FILE}.tmp" "$TASKS_FILE"
}

# ── Attempt tracking ─────────────────────────────────────────────────────────

get_attempts() {
  cat "$STATE_DIR/$1" 2>/dev/null || echo "0"
}

increment_attempts() {
  local task_id="$1"
  local count
  count=$(get_attempts "$task_id")
  echo $((count + 1)) > "$STATE_DIR/$task_id"
}

# ── Main loop ────────────────────────────────────────────────────────────────

while true; do
  # Prefer an in-progress task (resuming after a crash / failed cycle).
  task_id=$(find_task_by_status "IN_PROGRESS")

  # Otherwise pick the next TODO.
  if [ -z "$task_id" ]; then
    task_id=$(find_task_by_status "TODO")
  fi

  # Nothing left to do.
  if [ -z "$task_id" ]; then
    if $POLL; then
      echo "[ralph] All tasks complete. Polling for new tasks…"
      sleep 30
      continue
    else
      echo "[ralph] All tasks complete. Exiting."
      exit 0
    fi
  fi

  # ── Three-strikes rule ──────────────────────────────────────────────────

  attempts=$(get_attempts "$task_id")

  if [ "$attempts" -ge "$MAX_ATTEMPTS" ]; then
    echo "[ralph] $task_id failed $MAX_ATTEMPTS times. Marking BLOCKED."
    set_task_status "$task_id" "BLOCKED"
    add_failure_context "$task_id" "$MAX_ATTEMPTS"
    continue
  fi

  increment_attempts "$task_id"
  attempts=$((attempts + 1))
  echo "[ralph] ── $task_id (attempt $attempts/$MAX_ATTEMPTS) ──"

  # ── Run Claude cycle ────────────────────────────────────────────────────

  cat PROMPT.md | claude --dangerously-skip-permissions

done
