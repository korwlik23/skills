---
name: test-driven-development
description: >
  Use this skill when implementing any feature or bugfix, before writing implementation
  code. Triggers on "implement", "add this feature", "fix this bug", "write the code for",
  or any transition into writing production code. Enforces RED→GREEN→REFACTOR: a failing
  test must exist and be observed failing before production code is written.
---

# Test-Driven Development

Write the test first. Watch it fail. Write the minimal code to pass.

**Core principle:** if you didn't watch the test fail, you don't know it tests the right
thing. Violating the letter of these rules violates their spirit.

## Production-Grade Operating Contract

- Read `../../../RULES.md` first and apply it as the baseline.
- This is a **Rigid skill** — follow it exactly; do not adapt away the discipline.
- Pair with `testing-qa` for framework setup, coverage strategy, and test design depth.
- User instructions override this skill. Throwaway prototypes, generated code, and pure
  config may skip TDD **only with the user's explicit agreement** — state it when you do.

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Wrote code before the test? Delete it and start over from the test. Not "keep as
reference", not "adapt while writing tests". Delete means delete. Implement fresh.

**Recoverable, not destructive:** make the discarded code recoverable before removing
it — `git stash` it or commit it on a throwaway branch — so nothing is irreversibly
lost. The discipline is that you do **not** look at or adapt it while writing tests;
it is not that the bytes must be unrecoverable. If the code is substantial or the user
may want it, say so and confirm before discarding rather than deleting silently.

## RED → GREEN → REFACTOR

1. **RED — write one failing test.** One behavior, a clear name, real code (mocks only if
   unavoidable). It describes what *should* happen.
2. **Verify RED — run it and watch it fail.** MANDATORY. Confirm it fails (not errors)
   and fails for the expected reason (feature missing, not a typo). Passes already? It
   tests existing behavior — fix the test.
3. **GREEN — minimal code to pass.** Simplest thing that works. No extra options,
   abstractions, or "while I'm here" changes.
4. **Verify GREEN — run it and watch it pass.** All other tests still pass; output is
   clean (no errors/warnings). Test fails? Fix the code, not the test.
5. **REFACTOR — clean up while green.** Remove duplication, improve names, extract
   helpers. Add no behavior. Stay green.
6. **Repeat** for the next behavior.

## Common Rationalizations — all mean STOP and start over

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. The test takes 30 seconds. |
| "I'll test after" | Tests written after pass immediately and prove nothing. |
| "Already manually tested" | Ad-hoc ≠ systematic. No record, can't re-run. |
| "Deleting X hours is wasteful" | Sunk cost. Unverified code is debt, not an asset. |
| "Keep as reference" | You'll adapt it — that's testing after. Delete. |
| "Test is hard to write" | Hard to test = hard to use. Listen to the test; simplify design. |
| "TDD is dogmatic, I'm pragmatic" | TDD finds bugs before commit — it *is* the pragmatic path. |
| "This case is different because…" | It isn't. Start from the test. |

## L5 Acceptance Gates

- Every new function/behavior has a test that was watched failing first.
- Each test failed for the expected reason before implementation.
- Minimal code was written to pass; no speculative scope.
- All tests pass and output is clean.
- Bugfixes include a regression test that reproduces the bug.

## Bugfix Integration

Found a bug? Write a failing test that reproduces it, then follow the cycle. The test
proves the fix and prevents regression. Never fix a bug without a test.

## When Stuck

| Problem | Solution |
|---------|----------|
| Don't know how to test it | Write the wished-for API and the assertion first. |
| Test too complicated | The design is too complicated. Simplify the interface. |
| Must mock everything | Code too coupled. Use dependency injection. |

## Output / Reporting

Report the cycle honestly: the test, the observed RED output, the minimal change, the
observed GREEN output. "It should pass" is not acceptable — show the run. Defer the final
"done" claim to `verification-before-completion`.

---

*Adapted from the Superpowers `test-driven-development` skill by Jesse Vincent (MIT —
github.com/obra/superpowers), reworked for the v1.1 contract.*
