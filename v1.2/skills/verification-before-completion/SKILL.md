---
name: verification-before-completion
description: >
  Use this skill before reporting any task as done, fixed, working, complete, or ready.
  Triggers whenever you are about to claim success, close out work, or say "this should
  work". Enforces the Verification-Before-Completion HARD GATE: no completion claim
  without observed evidence.
---

# Verification Before Completion

"Done" is a claim about reality. Back it with observed evidence, never reasoning alone.

## Production-Grade Operating Contract

- Read `../../RULES.md` first and apply it as the baseline. This skill owns the
  **Verification Before Completion** HARD GATE.
- This is a **Rigid skill** — the gate is not optional.
- Complements the `RULES.md` "Quality Gates / Definition of Done" checklist.

## The Gate

Before stating a task is done/fixed/working, you must have **observed evidence**:

- A test you watched pass (with its output), not "the test should pass".
- Real command output (build, lint, type-check, run), not "it should build".
- A behavior reproduced and then re-checked, not "this fixes it".
- For UI/feature work: the feature exercised in the actual running app, or an explicit
  statement that it was not verified and why.

If you could not verify, **say so explicitly** and state exactly what is unverified and
what would be needed to verify it. That is acceptable. A false "done" is not.

## Forbidden Without Evidence

These phrases require backing output or an explicit "unverified" caveat:

- "This should work" / "this should fix it"
- "The tests will pass"
- "It builds fine" (without showing the build)
- "I've tested it" (without the run)
- "Everything is working"

Never fabricate results, benchmark numbers, logs, or validation claims.

## Verification Checklist

- [ ] Build / compile run and clean (output shown).
- [ ] Relevant tests run and pass; no pre-existing tests broken.
- [ ] Lint / type-check run where available.
- [ ] The specific reported problem was re-exercised and confirmed resolved.
- [ ] Edge cases and failure paths checked, not just the golden path.
- [ ] UI/behavior changes exercised in the running app, or explicitly marked unverified.
- [ ] No fabricated or assumed results in the report.

Can't check a box? It is not done — report the limitation honestly.

## Red Flags — STOP

| Thought | Reality |
|---------|---------|
| "It should work" | "Should" is a hypothesis, not evidence. Run it. |
| "Logic is obviously correct" | Obvious code still fails. Observe it. |
| "Too small to verify" | Small changes break builds too. Run it. |
| "I'll say done, they'll test it" | That makes the user your test runner on a false claim. |
| "Tests probably still pass" | "Probably" is not verified. Run the suite. |

## L5 Acceptance Gates

- Every completion claim is backed by shown, observed evidence.
- Unverifiable aspects are explicitly called out, not silently claimed.
- The originally reported problem was specifically re-checked.
- No fabricated output anywhere in the report.

## Output Format

```markdown
### Verification
- Build: <command> → <result/output>
- Tests: <command> → <pass/fail summary>
- Problem re-check: <how confirmed resolved>
- Unverified: <anything not verifiable, and why>
```

---

*Adapted from the Superpowers `verification-before-completion` skill by Jesse Vincent
(MIT — github.com/obra/superpowers), reworked for the v1.1 contract.*
