---
name: bug-debugging
description: >
  Use this skill when fixing bugs, debugging errors, reading logs, troubleshooting
  production issues, diagnosing performance problems, or responding to incidents.
  Triggers on requests involving error messages, stack traces, broken features,
  unexpected behavior, log analysis, "it doesn't work", "there's a bug",
  or any request about finding and fixing problems in code.
---

# Bug Debugging Skill

Use this skill when fixing bugs, debugging errors, reading logs, troubleshooting production issues, diagnosing performance problems, or responding to incidents.

## Production-Grade Operating Contract

- Before starting, read `../../../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, preserve existing behavior, avoid destructive or production-changing actions without explicit confirmation, validate before completion, and report only verified evidence.
- Use this skill for debugging depth; do not let it override user instructions, repository guidance, or security/data-integrity constraints.
- Keep responses proportional. Use the output format for full bug analyses and incidents; use a concise summary for narrow fixes.

## Core Principles

1. Reproduce before you fix — if you can't reproduce it, you can't verify the fix.
2. Understand before you change — read the error, trace the flow, find the root cause.
3. Fix the cause, not the symptom — patching symptoms creates more bugs.
4. One change at a time — multiple changes make it impossible to know what fixed it.
5. Every bug fix needs a test — prevent the same bug from returning.

## Rigid Debugging Gate (mandatory)

This is a **Rigid** discipline (per `../../../RULES.md` Skill Types): the order is not
optional. Every bug, error, failing test, or unexpected behavior goes through these
four phases in order. The "Debugging Process" Steps below are not a second model —
they are these four phases expanded. The mapping is exact:

- **Phase 1 Reproduce** = Step 1 (Gather Information) + Step 2 (Reproduce the Issue)
- **Phase 2 Isolate root cause** = Step 3 (Isolate the Problem) + Step 4 (Find Root Cause)
- **Phase 3 Fix at root** = Step 5 (Implement the Fix)
- **Phase 4 Verify & prevent** = Step 6 (Verify the Fix) + Step 7 (Prevent Recurrence)

Do not skip ahead; do not treat the Steps as an alternative to the phases.

### Recite verbatim — first thing in your first response of any debug session

Before doing anything else, output this block exactly as written. No paraphrasing,
no shortening, no skipped lines. Recite **once** per debug session — do not re-recite
mid-session. If the user explicitly says "skip the mantra," skip the recital but still
apply the four phases silently.

> **Debug Mantra:**
> 1. **Reproduce first.** No fix proposal until the failure is deterministic.
> 2. **Know the fail path.** Debugger → source trace + knob enumeration →
>    in-code instrumentation, in that order.
> 3. **Falsify the hypothesis.** Run the cleanest *disproof* before the *proof*.
> 4. **Every run is a breadcrumb.** Cross-reference all of them; the ledger is your
>    memory across the session.

The mantra is a constraint **you** carry through the session — not advice to deliver
back to the user. After reciting, begin Phase 1.

### The four phases

1. **Reproduce** — make the failure deterministic. If it is intermittent, find the
   conditions that make it reliable. **No reliable reproduction → do not attempt a fix;**
   say so and gather more evidence.
2. **Isolate the root cause** — trace symptom → origin in the actual code path (not
   memory). One hypothesis at a time, confirmed with evidence. Ask "why" until the
   answer is a specific line/condition, not "it returns the wrong value". When a
   candidate root cause surfaces, design the cleanest disproof and run it **before** the
   proof — if it survives the disproof, it's real. Maintain a running **ledger** of every
   experiment: what changed, what happened, what it ruled in or out. When a new
   hypothesis surfaces, walk the ledger — does it hold for *every* prior observation,
   not just the most recent?
3. **Fix at the root** — fix the cause, not the symptom. No swallowing errors or
   masking band-aids. Write a failing test that reproduces the bug **before** the fix,
   then make it pass.
4. **Verify & prevent regression** — original reproduction now passes; run the
   surrounding suite for side effects; keep the regression test; flag whether the same
   root cause exists elsewhere. Then apply `verification-before-completion`. For any
   non-trivial bug, after this phase hand off to [`post-mortem`](../../communication/post-mortem/SKILL.md)
   to write the engineering record — your Phase-2 ledger is its raw material.

### Red Flags — STOP, you are rationalizing

| Thought | Reality |
|---------|---------|
| "Let me just try changing this and see" | Guess-and-check ≠ debugging. Find the cause. |
| "It's probably the same as last time" | Verify on evidence, not memory. |
| "Wrap it in try/catch and move on" | That hides the bug, it doesn't fix it. |
| "Can't reproduce, but I'll fix it anyway" | An unconfirmed fix is a new guess. |
| "The fix works, no need for a test" | Without a regression test it will come back. |
| "One symptom fixed, done" | Same root cause may surface elsewhere. Check. |

## Debugging Process

### Step 1: Gather Information  ·  Phase 1 (Reproduce)

Before touching any code:

- **What is the error?** — Exact error message, status code, stack trace.
- **When does it happen?** — Always, sometimes, after a specific action?
- **Where does it happen?** — Which page, endpoint, function, environment?
- **Who reported it?** — User type, permissions, browser, device?
- **What changed recently?** — Recent deploys, config changes, dependency updates?
- **Is it new or regression?** — Was this working before? When did it break?

### Step 2: Reproduce the Issue  ·  Phase 1 (Reproduce)

Reproduction priority:

| Method | Reliability | Speed |
|--------|------------|-------|
| Automated test that fails | ✅ Best | Fast |
| Local reproduction steps | ✅ Good | Medium |
| Staging environment reproduction | ⚠️ OK | Slow |
| "It happened once in production" | ❌ Poor | N/A |

Reproduction checklist:
- [ ] Same user role/permissions?
- [ ] Same data state (empty, full, edge case)?
- [ ] Same environment config?
- [ ] Same browser/device (for frontend)?
- [ ] Same request payload?
- [ ] Same timing/sequence of actions?

If you can't reproduce:
- Check logs for the exact request.
- Check for race conditions or timing-dependent behavior.
- Check for environment-specific configuration.
- Check for data-specific triggers (specific IDs, values, character sets).
- Add logging/monitoring to capture the next occurrence.

### Step 3: Isolate the Problem  ·  Phase 2 (Isolate root cause)

Narrow down where the bug lives:

```
Frontend Bug?
├── Browser console errors?
├── Network tab — request/response correct?
├── Component rendering issue?
├── State management issue?
└── CSS/layout issue?

Backend Bug?
├── Request reaches server? (check access logs)
├── Middleware passes? (auth, validation)
├── Controller receives correct input?
├── Service/business logic correct?
├── Database query returns expected data?
├── Response formation correct?
└── External service call fails?

Database Bug?
├── Query returns wrong data?
├── Missing/incorrect data?
├── Constraint violation?
├── Migration issue?
└── Connection/timeout issue?
```

### Step 4: Find Root Cause  ·  Phase 2 (Isolate root cause)

Root cause analysis techniques:

| Technique | When to Use |
|-----------|-------------|
| **Stack trace reading** | Error with stack trace available |
| **Binary search** | "It worked before" — bisect commits |
| **Print/log debugging** | Tracing data flow through layers |
| **Rubber duck** | Explain the problem to find the gap |
| **Minimum reproduction** | Strip code until bug disappears, add back |
| **Diff analysis** | Compare working vs broken state/config |
| **5 Whys** | Symptom → cause → deeper cause → root |

### Step 5: Implement the Fix  ·  Phase 3 (Fix at root)

Fix rules:

1. Fix at the root cause level, not the symptom level.
2. Make the minimal change that fixes the issue.
3. Don't refactor while fixing bugs — separate concerns.
4. Check for the same bug pattern elsewhere in the codebase.
5. Add input validation or guards to prevent the bad state.
6. Consider edge cases the original code missed.

### Step 6: Verify the Fix  ·  Phase 4 (Verify & prevent)

Verification checklist:

- [ ] Write a test that fails without the fix and passes with it.
- [ ] Verify the original reproduction steps no longer trigger the bug.
- [ ] Check that related functionality still works (regression test).
- [ ] Test edge cases around the fix.
- [ ] Verify in the same environment where the bug was reported.
- [ ] Check performance — did the fix introduce any slowness?

### Step 7: Prevent Recurrence  ·  Phase 4 (Verify & prevent)

After fixing:

- [ ] Add automated test(s) covering the bug scenario.
- [ ] Check for similar patterns in other parts of the codebase.
- [ ] Update documentation if the bug revealed an unclear API or behavior.
- [ ] Add monitoring/alerting if the bug was hard to detect.
- [ ] Consider adding input validation to prevent the bad state.
- [ ] Update error messages to be more helpful if the error was confusing.

## Reading Error Messages

HTTP status taxonomy, stack-trace reading, and a common-error-pattern lookup table are
in `references/error-patterns.md` — load it when an error message or stack trace lands
and you need a quick triage hint before diving in.

## Log Analysis

Log-search heuristics, log-reading patterns, and framework-specific commands (Laravel,
Node.js / PM2) are in `references/log-tips.md` — load it when you have logs in hand and
need to extract signal.

## Production Debugging

### Safe Production Investigation

| ✅ Safe to Do | ❌ Never Do |
|-------------|------------|
| Read logs | Modify production data |
| Read error tracking (Sentry) | Run untested queries |
| Check monitoring dashboards | Debug with breakpoints |
| Run read-only queries | Restart services during peak |
| Check health endpoints | Deploy untested hotfix |
| Review recent deploys | Give yourself admin access |

### Production Incident Protocol

```
1. DETECT — Alert fired or user reported
2. ACKNOWLEDGE — Confirm the issue, assess severity
3. COMMUNICATE — Notify stakeholders, set expectations
4. TRIAGE — Is it data loss? Security breach? Service down? UX issue?
5. MITIGATE — Immediate action to reduce impact:
   - Rollback if deploy-related
   - Feature flag if feature-related
   - Scale up if load-related
   - Block traffic if attack-related
6. FIX — Implement proper fix
7. VERIFY — Confirm fix in production
8. POST-MORTEM — Document what, why, how, and prevention
```

### Severity Classification

| Severity | Definition | Response Time |
|----------|-----------|---------------|
| 🔴 P0 — Critical | Service down, data loss, security breach | Immediate |
| 🟠 P1 — High | Major feature broken, significant user impact | < 1 hour |
| 🟡 P2 — Medium | Feature degraded, workaround exists | < 4 hours |
| 🟢 P3 — Low | Minor issue, cosmetic, edge case | Next business day |

## Common Bug Categories and Tools

A pre-flight category lookup (data / state / timing / environment bugs) and a
per-layer tool table (frontend / backend / database) live in `references/tools.md` —
load when you are choosing how to narrow the search or how to instrument.

## Error Recovery During Execution

When something goes wrong while you are working (not a user-reported bug). This is the
pack-wide canonical Error Recovery Protocol; `../../../RULES.md` points here.

### Build Failure

```
1. Read the full error message carefully.
2. Identify root cause (syntax, type, dependency, config).
3. Fix the specific error — don't make unrelated changes.
4. Rebuild and verify the fix.
5. Check if the fix introduced new issues.
```

### Test Failure

```
1. Determine if the failure is from your change or pre-existing.
2. If your change: fix the code to match expected behavior, or update the test if behavior intentionally changed.
3. If pre-existing: note it and continue, but don't hide it.
4. Re-run all tests after fixing.
```

### Unexpected Behavior

```
1. Reproduce the issue to confirm it exists.
2. Check if the behavior is documented or intentional.
3. Trace the code path to find the root cause.
4. Fix at the root cause, not the symptom.
5. Add a test to prevent regression.
```

### Cascading Failures

```
1. Stop making more changes.
2. Revert to last known working state if possible.
3. Analyze what caused the cascade.
4. Fix issues one at a time, validating after each fix.
5. Document the root cause for future reference.
```

## L5 Acceptance Gates

- The issue is reproduced or the inability to reproduce is stated with evidence.
- Root cause is traced to the smallest responsible layer, not only the visible symptom.
- The fix is scoped to the defect and avoids unrelated refactors.
- A regression test, monitor, or prevention step is added when practical.
- Verification distinguishes local, CI, staging, and production evidence.

## Output Format

When debugging, structure the response as:

```markdown
# Bug Analysis

## Problem Description
What the bug is, when it happens, who it affects.

## Root Cause
The technical reason the bug exists.
Include file, line, and the specific logic error.

## Evidence
- Error messages, log entries, or stack traces
- Steps that reproduce the issue
- Screenshots if visual

## Fix
The exact code change and why it fixes the root cause.

## Verification
- [ ] Test that reproduces the bug (fails before fix, passes after)
- [ ] Related functionality regression tested
- [ ] Edge cases checked

## Prevention
- Tests added to catch regression
- Similar patterns checked elsewhere
- Monitoring/alerting improvements (if applicable)

## Related Issues
Other areas that may have the same bug pattern.
```

## Example Trigger Phrases

- "There's a bug in this feature"
- "This endpoint returns 500"
- "It doesn't work"
- "Why is this failing?"
- "Debug this error"
- "Read these logs and find the problem"
- "Production is down"
- "This used to work but now it's broken"
- "Help me troubleshoot this"

## Usage Limitations

- Do not modify production data or run destructive commands during debugging without confirmation.
- Do not claim root cause without evidence from code, logs, or stack traces.
- Do not skip writing a regression test after confirming the fix.
- Do not deploy untested hotfixes — always verify before pushing to production.
- Do not assume environment-specific details (config, secrets, infrastructure) without evidence.
