---
name: scrutinize
description: >
  Use this skill for an outsider-perspective end-to-end review of a plan, PR,
  diff, design doc, or proposed code change. First questions intent and whether
  a simpler or more elegant approach would achieve the same goal, then traces
  the actual code path (not just the diff) to verify the change does what it
  claims. Output is concise, actionable, and every call carries its rationale.
  Trigger on "/scrutinize", "second opinion", "sanity check", "outsider review",
  "is this the right approach", "is this worth doing", or whenever the user
  wants a fresh pair of eyes on a design decision or implementation choice —
  complements `code-review-refactor`, which is checklist-based.
---

# Scrutinize Skill

Stand outside the change and ask whether it should exist at all, then verify it actually
does what it claims end-to-end. This is the **outsider-stance** review — pair it with
[`code-review-refactor`](../code-review-refactor/SKILL.md) when you also need full
checklist coverage. Two different lenses on the same artifact; both can run on the same
PR.

## Production-Grade Operating Contract

- Before starting, read `../../../RULES.md` and apply it as the behavior, safety, validation,
  and communication baseline — including Evidence-Based Findings and the
  three-iteration rule.
- This skill is **read-only by default**. Do not change code during a scrutinize pass
  unless the user explicitly asks for a fix.
- Keep responses proportional. Lead with the most valuable finding (usually the
  simpler-alternative pass) — not a checklist dump.

## When to use this skill vs `code-review-refactor`

| Need | Use |
|------|-----|
| "Is this the right approach? Could it be simpler?" | **scrutinize** |
| "Does this PR have correctness / security / style issues?" | `code-review-refactor` |
| "Second opinion on a design doc / plan" | **scrutinize** |
| "Standard PR review across the full checklist" | `code-review-refactor` |
| "Both" | run both — they don't overlap |

`code-review-refactor` already includes the **Simpler-alternative pass** as Step 0, so
small PRs are usually fine with just that. Reach for `scrutinize` when:
- The change is large enough that scope itself is a question.
- The user explicitly asked for an outsider perspective / second opinion.
- The artifact is a plan or design doc (not code yet).

## Operating stance

- **Outsider.** Forget who wrote it and why they think it's right. Read the artifact
  cold.
- **End-to-end, not diff-local.** The diff is the entry point, not the scope. Follow
  the call graph through real code paths.
- **Actionable, concise, with rationale.** Every finding states *what to change*, *why*,
  and *what evidence* led you there. No filler, no restating the diff back.

## Workflow

Run these in order. Do not skip ahead.

### 1. Intent — what is this actually trying to do?

- State the goal in one sentence, in your own words. If you cannot, the artifact is
  underspecified — say so and stop.
- Ask: **is there a simpler, smaller, or more elegant way to achieve the same goal?**
  Consider:
  - **Doing nothing** — is the problem real and load-bearing, or speculative?
  - **Using something that already exists** — is there a helper / utility / library /
    pattern in the codebase that already solves this, avoiding new surface?
  - **A smaller change** — solving 90% of the goal with 10% of the risk.
  - **A different layer** — config vs code, framework vs app, build vs runtime,
    database vs application.
- If a better alternative exists, name it explicitly with rationale. **This is the most
  valuable thing you can output — surface it before the line-by-line review.**

### 2. Trace — walk the actual code path

- For each behavior the change claims, trace the path end-to-end through the real code,
  not just the lines in the diff:
  - Entry point → call sites → branches taken → state mutated → exit / return / side effect.
  - Include the unchanged code on either side of the diff. Bugs hide at the seams.
- For a plan or design doc: trace the proposed flow against the existing system. Where
  does it touch reality? What does it assume that isn't true?
- Note every place the trace surprises you (unexpected branch, dead code reached, state
  you didn't know existed). **Surprises are signal.**

### 3. Verify — does it actually do what it claims?

For each claim the change / plan makes, answer:

- **Does the code path you just traced actually produce that behavior?** Walk it
  explicitly. *"It claims X. Path: A → B → C. At C, [observation]. Therefore [holds /
  doesn't hold]."*
- **What inputs / states would break it?** Edge cases, concurrent callers, error paths,
  partial failures, retries, empty / null / unicode / huge inputs, ordering assumptions.
- **What does it silently change?** Performance, error semantics, observability,
  contract for other callers, on-disk / on-wire format.
- **How is it tested?** Do the tests actually exercise the traced path, or do they
  pass while skipping it (mocks that hide the bug, asserts on intermediate state,
  happy path only)?

### 4. Report

Output one tight section per finding. Order by severity (blocker → major → nit).
For each:

- **Finding** — one sentence, specific. Cite `file:line` when applicable.
- **Why it matters** — the consequence, not the principle.
- **Evidence** — the trace step or input that exposes it.
- **Suggested change** — concrete, minimal.

Close with a one-line verdict: ship / fix-then-ship / rework / reject — with the single
biggest reason.

## Output format

```markdown
### Scrutinize: <artifact>

**Goal (as I understand it):** <one sentence>

**Simpler alternative:** <named alternative with rationale, or "none — change is
appropriately scoped">

### Findings

#### [Blocker] <one-sentence finding> — `file:line`
- Why it matters: …
- Evidence: …
- Suggested change: …

#### [Major] <…>
…

#### [Nit] <…>
…

### Verdict
<ship / fix-then-ship / rework / reject> — <single biggest reason>
```

## Operating rules

- **No rubber-stamps.** "LGTM" is not an output. If you genuinely find nothing, say
  what you traced and what you checked, so the user can judge whether your review
  covered the surface they cared about.
- **Cite or it didn't happen.** Every claim about the code references a specific path,
  file, or line. No vague *"this might break under load."*
- **Distinguish claim from verification.** *"The PR says X"* and *"I traced X and
  confirmed / refuted it"* are different — keep them separate in the output.
- **One simpler-alternative pass is mandatory.** Even on small changes, spend one
  breath asking if the whole thing is necessary. Skip only if the user explicitly says
  *"don't question scope."*
- **Don't pad with style nits when there's a structural problem.** If step 1 or
  step 2 surfaces a real issue, lead with it; defer nits or drop them.
- **No flattery, no hedging.** "This is a great PR but..." adds nothing. State the
  finding.
- **One iteration is normal, three is a smell.** If the user pushes back twice and
  asks for a third pass, stop and ask what specific finding or framing is wrong —
  don't keep tweaking blindly.

## Handoff

- If scrutinize surfaces a concrete bug that needs fixing, hand off to
  [`bug-debugging`](../bug-debugging/SKILL.md). Scrutinize identifies; bug-debugging
  reproduces and fixes.
- If scrutinize concludes "fix-then-ship" and the user wants the checklist pass too,
  follow up with [`code-review-refactor`](../code-review-refactor/SKILL.md) on the
  same diff — the two reviews don't overlap.

---

*Adapted from the `scrutinize` skill in the 9arm-skills pack.*
