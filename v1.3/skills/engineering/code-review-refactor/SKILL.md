---
name: code-review-refactor
description: >
  Use this skill when the user requests any form of code review, even without
  saying "review" directly — e.g. review PR, check diff, analyze bugs, check
  code quality, assess naming, evaluate refactoring, review security, review
  performance, review database, review API, review accessibility, review
  observability, or request code improvement advice. Report only evidence-backed
  findings with scope, severity, location, impact, evidence, and actionable fix.
---

# Code Review Refactor Skill

Use this skill when reviewing code quality, cleaning messy code, refactoring, reducing duplication, preparing code for production, or assessing technical debt.

## Production-Grade Operating Contract

- Before starting, read `../../../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, preserve behavior, keep diffs focused, avoid destructive actions without explicit confirmation, validate before completion, and report only verified findings.
- Use this skill for maintainability depth; do not let it override user instructions, repository guidance, or security/data-integrity constraints.
- Keep responses proportional. Lead with findings for reviews; use a concise summary for small refactors.

## Core Philosophy

1. Code is read 10x more than written — optimize for readability.
2. Every refactor must preserve existing behavior unless explicitly changing it.
3. Refactor in small, verifiable steps — never rewrite everything at once.
4. The best refactor makes the next change easier.
5. Complexity is the enemy — fight it constantly but pragmatically.

## Review Discipline

### Step 0 — Simpler-alternative pass (mandatory)

**Before** running the checklist, spend one breath asking whether the change should exist
at all in its current shape. Stand outside the diff and consider:

- **Doing nothing.** Is the problem real and load-bearing, or speculative?
- **Using what already exists.** Is there a helper / utility / library / pattern in
  this codebase that already solves this, avoiding new surface?
- **Doing 90% with 10% of the risk.** Is there a smaller change that covers the
  important cases?
- **Different layer.** Could this be solved at config vs code, framework vs app,
  build vs runtime, database vs application?

If a meaningfully simpler alternative exists, name it explicitly with rationale at the
top of the review — **this is often the most valuable thing you can say.** Surface it
*before* the line-by-line review. Skip this step only if the user explicitly says
*"don't question scope"* or *"checklist only."*

### Review depth and scope

- Start by identifying scope: PR, diff, snippet, module, architecture, security, performance, database, API, accessibility, observability, or refactor.
- Choose a review depth appropriate to context and state which tier you used:
  - **Quick scan** — fast pass for obvious correctness, security, and risk issues; small diffs or time-boxed checks.
  - **Standard review** — the default; full checklist coverage at normal depth.
  - **Deep review** — exhaustive trace of logic, edge cases, data flow, and cross-module impact; high-risk or critical code.
  - If scope is unclear but evidence is sufficient, default to **Standard** and state the assumptions used. If missing information blocks judgement, ask before concluding.
- State reviewed areas and out-of-scope areas when the user limits the request.
- Use the available context only: code, diff, configuration, logs, schemas, contracts, tests, and documentation.
- **Trace end-to-end, not diff-local.** The diff is the entry point, not the scope.
  For each behavior the change claims, follow the call graph through the real code path
  (including unchanged code on either side of the diff — bugs hide at the seams). Note
  every place the trace surprises you; surprises are signal.
- **Distinguish claim from verification.** Keep "the PR says X" and "I traced X and
  confirmed / refuted it" as separate statements in the output. Don't conflate them.
- Separate provable behavior from assumptions that still need user confirmation.
- Report only issues that are real, evidence-backed, and have practical impact.
- Merge repeated symptoms with the same root cause into one finding and describe the combined impact.
- Keep optional recommendations separate from findings that block correctness, security, reliability, or maintainability.
- When more than one fix is valid, present the trade-offs and make the decision point explicit.
- Lead with findings before positive notes or broad summaries so production risks are visible first.
- Do not report that a category was checked with no issues unless that negative result is important to the user's decision.
- Do not promote style preferences into findings unless they create measurable readability, correctness, maintainability, accessibility, or operational impact.
- **No rubber-stamps.** "LGTM" is not an output. If you genuinely find nothing, say what
  you traced and what you checked, so the user can judge whether your review covered
  the surface they cared about.
- **Cite or it didn't happen.** Every claim about the code references a specific path,
  file, or line. No vague *"this might break under load."*

## Refactor Rules

1. Do not change behavior unless asked.
2. Refactor in small steps — each step should compile and pass tests.
3. Keep diffs readable.
4. Improve names — a good name eliminates the need for a comment.
5. Reduce duplication — only when the duplicated code changes for the same reason.
6. Extract functions/classes only when it improves clarity.
7. Avoid over-engineering — YAGNI applies until proven otherwise.
8. Add tests for risky refactors.
9. Preserve public APIs unless necessary.
10. Explain behavior changes clearly.
11. Delete dead code — commented-out code is dead code.
12. Simplify conditionals — complex boolean logic should be named or extracted.

## Severity Classification

| Severity | Definition | Action |
|----------|-----------|--------|
| 🔴 Critical | Bugs, security holes, or data loss | Must fix before merge |
| 🟠 High | Performance, maintainability, reliability risk | Should fix before merge |
| 🟡 Medium | Code smell, unclear logic, tech debt | Fix or create ticket |
| 🟢 Low | Style, naming, minor improvements | Optional |
| 💡 Suggestion | Alternative approach or future idea | Informational |

## Review Checklist

### Code Quality
- Naming — reveal intent?
- Function size — any > 30 lines?
- Class size — any > 300 lines?
- Nesting depth — any > 3 levels?
- Magic values — hard-coded numbers/strings?
- Dead code — commented-out or unused?

### Logic & Correctness
- Edge cases — null, empty, zero, boundary?
- Error handling — caught, logged, surfaced?
- Race conditions — concurrent data corruption?
- Type safety — explicit types, no implicit coercion?
- Validation — all input validated?
- Default values — don't treat `0`, `false`, or `""` as missing.
- Financial precision — use fixed-point/integer, never float.
- Empty vs unset — distinguish intentionally empty values from values not yet provided.
- Equality semantics — use the correct comparison strategy for value equality vs reference equality.
- Loop/index bounds — verify off-by-one and boundary behavior.

### Architecture & Design
- Single Responsibility — one job per module?
- Coupling — changeable without unrelated modifications?
- Abstraction level — high and low concerns mixed?
- Hidden side effects — does more than the name says?
- Framework conventions — follows idioms?

### Performance
- N+1 queries — queries inside loops?
- Unbounded operations — unlimited data sets?
- Memory leaks — listeners/subscriptions cleaned up?
- Caching opportunities — repeated expensive operations?
- Algorithm complexity — O(n²) when O(n) is available?
- Lazy loading — heavy resources loaded only when needed?
- Blocking work — synchronous blocking on single-threaded hot paths?
- Concurrency utilization — independent work executed sequentially without need?
- Bundle and asset weight — heavy frontend resources loaded before needed?

### Security
- Authorization — checked before access?
- Input sanitization — before output/storage?
- Sensitive data — exposed in logs/responses?
- CSRF/CORS — state-changing endpoints protected?
- Rate limiting — auth and abuse-prone endpoints guarded?

### Database & Data Integrity
- Schema fit — types, constraints, nullable match domain rules?
- Migration safety — rollback path, backward compatibility?
- Transaction boundary — atomic operations wrapped correctly?
- Data consistency — unique constraints, foreign keys, idempotency?
- Pagination — cursor/stable ordering for changing data?
- Seed data — not mixed with production data or real credentials?

### API Design
- Contract clarity — request/response/error shape consistent?
- HTTP semantics — methods, status codes, idempotency correct?
- Validation & error response — actionable errors without internal leaks?
- Backward compatibility — no client breakage without migration path?
- Response minimality — only necessary fields, no raw model exposure?
- Pagination & filtering — collections bounded, params validated?
- Idempotency — retry-safe operations have dedup keys?
- Rate limit feedback — quota info returned for client backoff?
- Observability — request/correlation IDs propagated?

### Accessibility
- Semantic HTML — correct elements for purpose (button, link, heading)?
- Keyboard navigation — all controls reachable, no traps?
- Accessible names — icon buttons, inputs, landmarks have labels?
- ARIA correctness — used only when necessary, roles/states correct?
- Color & contrast — sufficient contrast, not color-only indicators?
- Error & form feedback — validation linked to fields, screen-reader aware?
- Motion & timing — respects reduced motion, no forced auto-updates?
- Responsive & zoom — usable when zoomed or viewport changes?

### Observability & Operations
- Structured logging — searchable fields (request_id, user_id, operation, status)?
- Log level discipline — no debug logs in production hot paths?
- Metrics — critical flows have throughput/latency/error rate tracking?
- Tracing — async/distributed requests propagate trace context?
- Error reporting — exceptions sent to tracking system with context (no secrets)?
- Health & readiness — service/job has health signals reflecting dependencies?
- Timeouts & retries — external calls have timeout, backoff, circuit breaker?
- Operational runbook fit — errors help ops team know impact and next steps?
- Feature flag & rollout — high-risk changes have rollback mechanism?
- Retry safety — non-idempotent operations are not retried without deduplication?

## Knowledge Base — load on demand

The skill's reference content lives in `references/`. Load the relevant file when its
specific lens applies; otherwise stay with the inline checklist:

- `references/refactoring-patterns.md` — anti-patterns and the refactoring techniques
  that address them. Load when a code smell needs a named fix.
- `references/design-principles.md` — SOLID, CUPID, and additional principles. Load
  when calling out a structural concern by name.
- `references/naming.md` — case conventions and naming quality rules. Load when
  identifier choices are a finding.
- `references/framework-review.md` — per-framework review prompts (Laravel, Next.js /
  React, Svelte, TypeScript). Load when the code under review is one of those stacks.

The framework-agnostic checklist, severity model, and review discipline above remain
the source of truth.

## L5 Acceptance Gates

- Review findings are evidence-backed with file and line references.
- Severity reflects production impact: correctness, security, data integrity, reliability, performance, and maintainability.
- Refactors preserve behavior unless the user explicitly requested behavior change.
- Large refactors are broken into reviewable steps with validation after each step.
- Recommendations separate must-fix risks from optional cleanup.

## Output Format

```markdown
# Code Review

## Scope
- **Reviewed**: files, diff, modules, or system areas inspected.
- **Evidence used**: code, config, log, schema, contract, test, or documentation.
- **Limitations**: missing info that affects confidence (no schema, no runtime log, etc.).

## Findings

Group by severity: 🔴 Critical → 🟠 High → 🟡 Medium → 💡 Suggestion.

For each finding:
- **[Issue Name]**
  - **Severity** — 🔴/🟠/🟡/💡
  - **Category** — correctness, security, database, API, accessibility, observability, performance, naming, or code quality
  - **Location** — file path and line number when known
  - **Problem** — what is wrong or inappropriate
  - **Impact** — why it matters and what it affects
  - **Evidence** — code path, diff, config, or data that supports this finding
  - **Fix** — smallest change that addresses root cause, with code example when appropriate
  - **Alternatives** — if multiple fixes exist, summarize trade-offs and what the user needs to decide

If no findings: "No evidence-backed issues found in the provided context" + state remaining limitations.

## Questions & Assumptions
- Questions that need user confirmation before a decision can be made.
- Assumptions used during review — do NOT turn assumptions into findings without evidence.

## What's Done Well ✅
Positive observations worth reinforcing (evidence-backed only).

## Refactoring Opportunities
- Quick wins (< 30 min)
- Medium effort (1-4 hours)
- Major refactors (separate PR)

## Final Verdict
- ✅ Approve — Ready to merge
- ⚠️ Approve with comments — Minor fixes, trust author
- 🔄 Request changes — Must fix critical/high issues
- ❌ Reject — Fundamental design problems
```

## Example Trigger Phrases

- "Review this PR"
- "Check this code for bugs or security issues"
- "Look at this diff before merge"
- "Is the performance OK here?"
- "Review API design and error handling"
- "Check accessibility of this component"
- "Review naming and code quality"
- "Help me refactor this"
- "Is this code production-ready?"

## Usage Limitations

- Do not use this skill for writing new code from scratch — use domain-specific skills instead.
- Do not conclude dependency vulnerabilities without manifest, lockfile, audit output, or verifiable version evidence.
- Do not cite external standards without verifying the latest authoritative source.
- Do not guess business requirements, API contracts, or data models not visible in context.
- Do not turn stylistic preferences into findings unless they have measurable system impact.
