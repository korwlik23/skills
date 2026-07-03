---
name: finishing-a-development-branch
description: >
  Use this skill when implementation work on a branch is complete and you need to decide
  what happens to it. Triggers on "I'm done", "wrap this up", "finish the branch",
  "ready to merge", "create the PR", or the end of a plan's tasks. Verifies the branch is
  green, then walks the user through merge / PR / keep / discard with a destructive-action
  gate.
---

# Finishing a Development Branch

Close out a branch deliberately. Verify first; never decide its fate for the user.

## Production-Grade Operating Contract

- Read `../../../RULES.md` first and apply it as the baseline — especially the destructive-
  operation confirmation rule.
- Pair with `git-workflow` for branching/PR/conflict mechanics and `release-version`
  when the merge implies a release.
- Run `verification-before-completion` before this skill — finishing assumes the work is
  actually verified.
- **After the branch is finished**, if the work resolved a non-trivial bug, hand off to
  [`post-mortem`](../../communication/post-mortem/SKILL.md) to write the engineering record. If leadership /
  PM / cross-team needs a status update, hand the post-mortem (or the change summary) to
  [`management-talk`](../../communication/management-talk/SKILL.md) to reshape for the channel.

## Step 1 — Verify the Branch Is Green

- Working tree state is known (`git status`); no unintended files.
- Build, tests, lint/type-check run and pass (show output). If anything fails, **stop** —
  the branch is not finishable; return to debugging/TDD.
- The branch does only what the design/plan said. Flag scope creep.

## Step 2 — Summarize What Changed

Briefly: what was built, files touched, behavior changes, risks, and anything left for a
follow-up. The user needs this to choose well.

## Step 3 — Present Options (do not pick for the user)

| Option | When it fits |
|--------|--------------|
| **Merge** | Trunk-based flow, change is small/approved, tests green |
| **Open a PR** | Needs review, team workflow, or CI gates |
| **Keep the branch** | More work coming; not ready to integrate |
| **Discard the branch** | Experiment/dead end — work intentionally thrown away |

State your recommendation and why, then let the user decide.

## Step 4 — Execute the Chosen Option

- **Merge / PR:** confirm target branch first. Never force-push to a shared branch. Never
  push or open a PR unless the user asked for that specific action. Follow `git-workflow`.
- **Keep:** leave it; summarize how to resume.
- **Discard — DESTRUCTIVE GATE:** deleting a branch or resetting/`clean`-ing the worktree
  is irreversible and can lose work. Require **explicit, specific user confirmation** for
  this exact action ("yes, delete branch X and discard its changes"). Before deleting:
  confirm nothing is uncommitted that the user wants, and prefer a recoverable path
  (leave the branch, or tag/stash) when there is any doubt. A prior approval of a
  different action is not approval to discard.

## Red Flags — STOP

| Thought | Reality |
|---------|---------|
| "Tests mostly pass, good enough to merge" | "Mostly" is not green. Finish or fix first. |
| "I'll just merge/push to save a step" | Pushing/merging is the user's call. Confirm. |
| "Branch is junk, I'll delete it" | Discard is destructive. Explicit confirmation only. |
| "Force-push will clean this up" | Never force-push shared branches without explicit ask. |
| "It's done" (no run shown) | Verify first via verification-before-completion. |

## L5 Acceptance Gates

- Branch verified green (build + tests shown) before any finish action.
- A change summary with risks/leftovers was presented.
- Merge / PR / keep / discard options were presented; the user chose.
- No push, merge, or branch deletion happened without explicit user instruction.
- Discard required specific confirmation and a check for unsaved work.

## Output Format

```markdown
### Branch Finish: <branch>
- **Verification:** build/tests → <result>
- **Summary:** what changed · risks · leftovers
- **Recommendation:** <option> because …
- **Awaiting decision:** merge / PR / keep / discard
```

---

*Adapted from the Superpowers `finishing-a-development-branch` skill by Jesse Vincent
(MIT — github.com/obra/superpowers), reworked for the v1.1 contract.*
