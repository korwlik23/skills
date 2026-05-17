---
name: writing-plans
description: >
  Use this skill after a design is approved and before implementation begins. Triggers on
  "write the plan", "break this down", "create an implementation plan", or any transition
  from an approved design to coding. Produces a plan of small, ordered, independently
  verifiable tasks — each with exact file paths, the concrete change, and a verification
  step — clear enough for a junior engineer with no project context to follow.
---

# Writing Plans

Convert an approved design into an executable plan of bite-sized tasks.

## Production-Grade Operating Contract

- Read `../../RULES.md` first and apply it as the baseline. This skill follows
  `brainstorming` and precedes implementation.
- Do not write a plan for work that has no approved design — return to `brainstorming`.
- Keep the plan itself concise; the value is precision, not volume.

## What a Good Plan Task Looks Like

Each task must be:

- **Small** — roughly 2–5 minutes of focused work. If bigger, split it.
- **Ordered** — dependencies come first; each task leaves the tree buildable.
- **Self-contained** — exact file path(s), the concrete change or complete code, and
  what "done" looks like. No "figure out X" steps.
- **Verifiable** — a specific command, test, or observable result that confirms it.

A task an enthusiastic junior with no context and an aversion to testing could still
execute correctly.

## Process

1. Restate the approved design in one paragraph so the plan is anchored to it.
2. List the tasks in dependency order. Number them.
3. For each task, specify: **file(s)**, **change**, **verification**.
4. Mark which tasks are independent (parallelizable) vs strictly sequential.
5. Apply **YAGNI** and **DRY** — no task builds something the design didn't ask for; no
   task duplicates logic another task introduces.
6. **Plan self-review** — re-read with fresh eyes: any vague step, missing file path,
   unverifiable task, or hidden multi-step task? Fix inline.
7. Save the plan to `docs/specs/YYYY-MM-DD-<topic>-plan.md` (or the project's location)
   and, if the repo uses git, commit it.
8. Hand off to implementation: `test-driven-development` plus the relevant domain
   skill(s) per the `RULES.md` lifecycle.

## Red Flags — STOP

| Thought | Reality |
|---------|---------|
| "Task: implement the feature" | Not a task — that's the whole project. Decompose. |
| "They'll figure out the details" | A plan with gaps is not a plan. Specify the change. |
| "No need for a verification step" | An unverifiable task can't be confirmed done. Add one. |
| "Order doesn't matter" | It does — each task must leave the build green. |
| "Add tests at the end" | Tests are per-task with TDD, not a final task. |

## L5 Acceptance Gates

- Every task has explicit file path(s), a concrete change, and a verification step.
- No task exceeds the small (2–5 min) size; larger work was split.
- Task order respects dependencies; the build stays green between tasks.
- The plan traces back to the approved design with no scope additions.
- The plan was self-reviewed and saved.

## Output Format

```markdown
## Implementation Plan: <topic>

Design ref: <spec path>

### Task 1 — <short title>
- **Files:** path/to/file
- **Change:** <concrete change or complete code>
- **Verify:** <command / test / observable result>

### Task 2 — <short title>  (depends on Task 1)
...

### Parallelizable
Tasks {n, m} are independent and may run concurrently.
```

---

*Adapted from the Superpowers `writing-plans` skill by Jesse Vincent (MIT —
github.com/obra/superpowers), reworked for the v1.1 contract.*
