---
name: post-mortem
description: >
  Use this skill to write the canonical engineering record of a fixed bug —
  root cause, mechanism, fix, validation, and how it slipped through. Audience
  is other engineers (and future-you); code identifiers are first-class. Trigger
  on "/post-mortem", "write the post-mortem / postmortem / RCA / root cause
  analysis", "document this fix", "write up the root cause", "close out this bug
  with a writeup", or after a debug session has landed and validated a real fix.
---

# Post-mortem

The canonical engineering record of a bug fix. Written **after** debugging has landed a
real, validated fix — **for** other engineers (and future-you, who will have forgotten
everything in 6 months). Code identifiers are welcome here: this is the artifact that
lets the next person recover the mental model fast.

For the leadership / non-eng version of the same content, hand the finished post-mortem
to [`management-talk`](../management-talk/SKILL.md). They compose: post-mortem owns the
engineering truth; management-talk reframes it for the channel and the audience.

## Production-Grade Operating Contract

- Before starting, read `../../../RULES.md` and apply it as the behavior, safety, validation,
  and communication baseline — including the two HARD GATES and the three-iteration rule.
- This skill **produces a written artifact**. The "Required inputs" gate below is the
  skill-level enforcement of the Verification HARD GATE: refuse to draft until evidence
  is in hand.
- Code identifiers (function names, file paths, struct fields, commit SHAs, line numbers)
  are first-class here. Do **not** strip them — that is `management-talk`'s job.
- Keep responses proportional. A trivial typo fix does not need a post-mortem; the PR
  description is the record.

## When to invoke

- "/post-mortem"
- "write the post-mortem / postmortem / RCA / root-cause analysis"
- "document this fix" / "write up the root cause" / "close out this bug with a writeup"
- After a `bug-debugging` session has clearly landed a fix, proactively offer to draft one.

## When NOT to use

- **Bug not fixed yet, or fix not validated.** A post-mortem of a hypothesis is
  misleading. Refuse and tell the user what's missing.
- **Customer-visible outage / incident.** Those need a separate incident report (timeline,
  blast radius, paging history, comms). This skill is bug-fix scope. Flag and confirm
  before producing one.
- **Trivial fix** (typo, obvious one-liner). The PR description is the record. Don't
  manufacture ceremony.

## Required inputs — refuse to draft without these

Before writing a single line, confirm all four. If any are missing, list what's missing
and stop. Do **not** draft a placeholder.

- [ ] **Reliable repro** exists (not "happens sometimes" — a deterministic or high-rate
      reproducer the next person can run).
- [ ] **Root cause is known** (the mechanism is identified, not a hypothesis).
- [ ] **Fix is identified** (PR / commit / branch pointer).
- [ ] **Fix is validated** (the original repro now passes; the failing workload now
      succeeds).

These map 1-to-1 to the four phases of the Rigid Debugging Gate in `bug-debugging`. If
you came in via `bug-debugging`, pull from its Phase-4 ledger — that is the raw material.

## Structure

Use these blocks in this order. **Summary, Root cause, Fix, and Validation are
mandatory.** The rest are conditional but usually present.

### 1. Summary _(mandatory)_

One paragraph. What broke, in user / workload terms. What fixed it, in one sentence.
Ticket key, PR number, owner. A reader who stops here should have the right answer.

### 2. Symptom

What was actually observed. Test output, error message, log line, perf number, customer
report. Concrete identifiers — don't paraphrase the failure mode.

### 3. Root cause _(mandatory)_

The actual bug mechanism. **Code identifiers welcome and expected** — function names,
file paths, struct fields, branch conditions, commit SHAs of the offending change. Walk
the cause chain end-to-end. This is the most expensive section and the reason the
post-mortem exists at all. Future-you will live or die by how clearly you write this.

### 4. Why it produced the symptom

Link the root cause to the symptom. Often non-obvious — the bug is in function `A` but
the visible failure is in function `Z` minutes / hours later. Walk the chain so a reader
who only knows the symptom can connect it back to the cause without re-deriving it.

### 5. Fix _(mandatory)_

What changed and **why this change addresses the root cause** rather than hiding the
symptom. Link to PR / commit. If a previous fix attempt papered over the symptom, name
it and explain what was wrong with it — that history is part of the cause.

### 6. How it was found

Short. The debugging path:
- What repro made it deterministic.
- What tools cracked it (debugger first, then source trace + knob enumeration, then
  in-code instrumentation — the `bug-debugging` cascade).
- Hypotheses tried and rejected, with the one-line reason each was rejected.
- The single experiment that confirmed the cause.

This section is for the next debugger — make it learnable.

### 7. Why it slipped through

What allowed this bug to reach the branch / release / customer. Pick the real reason:
- **CI gap** — no test exercises this path or configuration.
- **Latent code** — correct when written, broken by a later change in a different file.
- **Workload gap** — no real workload reached this code path until now.
- **Incomplete prior fix** — a defensive check hid the symptom; root cause untouched.
- **Review miss** — the change was reviewable; the implication wasn't.

If the honest answer is "no good reason — we should have caught this," say so.
**Blameless** — describe the gap, not the person.

### 8. Validation _(mandatory)_

How we know the fix works. Concrete:
- Original failing test now passes (test name, link).
- Customer workload now completes (workload identifier, run link).
- Perf regression resolved (number before, number after).
- Stress / soak / fuzz run completed clean (duration, scale).
- Other affected configurations / workloads also tested.

If you only validated one configuration, **say so explicitly** — *"validated on
\<config\>; not retested on \<other configs\>."* Don't imply broader coverage than you
actually have.

### 9. Action items / follow-ups

Concrete next steps that are not in the fix PR itself. Each item: *what + owner +
tracking artifact*.

- Regression test added at \<seam\>. (Owner, test name.)
- Refactor to prevent class of bug. (Owner, ticket.)
- CI gap closed: \<new check\>. (Owner, PR.)
- Doc / runbook updated. (Owner, link.)
- Related ticket filed for \<adjacent issue you noticed\>. (Owner, key.)

If there are no action items, write *"None — the fix is sufficient and no class-of-bug
follow-up is warranted."* Don't manufacture action items to look thorough.

## Tone

This is engineer-to-engineer. Different from `management-talk`:

- **Code identifiers are first-class.** Function names, file paths, struct fields,
  commit SHAs, line numbers — keep them. The whole point is that future engineers can
  grep their way back to the change.
- **Mechanism over narrative.** Walk the actual cause chain. Don't soften it into
  "a synchronization issue" — say which function skipped which event under which gate.
- **Active voice, concrete subjects, short paragraphs.**
- **No hedging.** "We believe" / "appears to" / "may have" — drop. State it or don't
  write it.
- **Blameless.** Describe the bug, the gap, and the fix. Never "X should have caught
  this." The CI gap is the failure mode, not the person.
- **No advocacy.** A post-mortem records what happened and what's next. If you want to
  argue for a refactor, that's a separate proposal — link to it from the action items.

## Output flow

1. **Confirm all four required inputs are satisfied.** If any are missing, list them
   and stop. Do not draft.
2. **Confirm the destination** (PR description, ticket comment, `docs/postmortems/`
   file, internal wiki). The shape is the same; only the wrapping changes.
3. **Produce the draft** as a single chat block.
4. **Sign-off before posting anywhere external.** Print-only output (the user copies
   it themselves) needs no approval. For posting to a ticket / wiki via tooling, show
   the exact payload and wait for explicit *"post it"* / *"go ahead"* / *"yes"* before
   firing the request.
5. **Offer the management-talk handoff:** *"Want a leadership-flavored version? I can
   hand this to `management-talk`."* Don't do it automatically.

## Compact worked example

> **Summary.** The webhook retry worker double-processed events for ~6 hours because
> the idempotency key was computed from a mutable field that the producer rewrote
> between the first attempt and the retry. Affected 412 customer events on
> 2026-05-22, no data loss but ~80 duplicate notifications sent. Fixed by switching
> the key to an immutable `event.id`. Ticket WEBHOOK-1042, PR app/services#2871,
> owner Sarah.
>
> **Symptom.** Customers reported receiving two confirmation emails for single
> purchases. Log search showed paired
> `webhook.delivered event_id=<X>` entries with different `request_id`s but the same
> `event_id`, within 30–90 s of each other.
>
> **Root cause.** `WebhookRetryWorker::idempotencyKey()` in
> [`app/Jobs/WebhookRetryWorker.php:84`](app/Jobs/WebhookRetryWorker.php:84) hashed
> `payload['updated_at']`. The producer (`OrderConfirmedListener::handle`)
> normalises and overwrites `updated_at` on republish, so the retry computed a
> different key than the first attempt — the dedupe set
> (`redis://retry-dedupe`) missed the match, and the worker treated the retry as a
> brand-new event.
>
> **Why it produced the symptom.** Dedupe miss → second handler invocation →
> second email sent. No exception, no log warning — the failure was silently
> "two emails" instead of "one."
>
> **Fix.** PR #2871 changes `idempotencyKey()` to hash `event.id` (immutable,
> assigned at event creation in `OrderEvent::boot`). Adds an assertion in the
> worker that `event.id` is present; missing-id events go to a dead-letter queue
> instead of being silently retried with a degraded key.
>
> A prior fix (PR #2790, March 2026) added a *"prefer event.id when present"*
> fallback but kept the old hash path as default — that change papered over the
> symptom in one code path while leaving the bug live everywhere else. The old
> path is now removed entirely.
>
> **How it was found.** Customer report → repro built from production log replay
> (deterministic in <5 s). Initial hypothesis: queue redelivery before the dedupe
> set was written. Disproved with Redis MONITOR showing the key *was* written —
> just with a different value. Second hypothesis: payload mutation between
> attempts. Confirmed by logging the computed key on both attempts and diffing.
> Single experiment that nailed it: pinning `updated_at` to a constant in the
> producer made the bug disappear.
>
> **Why it slipped through.** Latent code. The mutable hash had been in place for
> ~14 months. No real workload triggered a retry that overlapped with a republish
> until May, when retry attempts increased after a Redis latency spike on
> 2026-05-22. CI had no test for the "republish during retry" interleaving.
>
> **Validation.** Original 412 affected events re-ran against the fixed worker in
> a staging replay; zero duplicates. New regression test
> `tests/Feature/WebhookRetryDedupeTest.php` covers the interleaving case.
> Production canary deployed 2026-05-23 06:00 UTC, watched for 12 h: 4,318
> webhooks delivered, zero duplicates. Not retested under the original Redis
> latency spike conditions — those have not recurred.
>
> **Action items.**
> - Regression test merged: `WebhookRetryDedupeTest`. (Sarah, in PR #2871.)
> - CI gap closed: nightly job replays a 1 % sample of yesterday's webhook events
>   through the worker, asserts no dedupe collisions. (Sarah, WEBHOOK-1043.)
> - Runbook entry added: `docs/runbooks/webhook-dedupe.md`. (Sarah, PR #2872.)
> - Audit ticket: other queues using mutable-payload-derived keys. Filed as
>   WEBHOOK-1044.

What this example does that a management-talk version would not:

- Names every code identifier (`WebhookRetryWorker::idempotencyKey()`,
  `OrderConfirmedListener::handle`, `redis://retry-dedupe`,
  `OrderEvent::boot`).
- Walks the cause chain end-to-end so the reader can grep back to the offending lines.
- Names the *prior fix attempt* (PR #2790) and what was wrong with it.
- Documents the *exact experiment* that nailed the cause (pinning `updated_at`).
- States validation coverage honestly — "not retested under the original Redis spike
  conditions" is information, not a hole.
- Action items have owners and tracking artifacts.

## Rules

- **Refuse to draft without all four required inputs.** A post-mortem of a hypothesis
  is worse than no post-mortem.
- **Never invent** root cause, owner, validation runs, or action items. If a section's
  facts are not there, ask. Don't fill the gap with plausible prose.
- **Never strip code identifiers** in the engineering record. They are the index. The
  leadership reframe is `management-talk`'s job, not yours.
- **Blameless.** Describe gaps and bugs, never people.
- **State validation coverage honestly.** If you only tested one config, say so.
  Implying broader coverage is the failure mode that breeds repeat regressions.
- **Get sign-off before posting** to any external system (ticket, wiki, doc repo).
  Print-only output needs no approval.
- **One iteration is normal, three is a smell.** If the user is still revising on the
  third pass, stop and ask what specific section is wrong — don't keep tweaking blindly.
