---
name: code-review-refactor
Mode: code-review-refactor
description: Principal-level code review and refactoring skill for improving maintainability, readability, architecture, naming, error handling, testability, performance, and long-term code health across any framework.
---

# Code Review Refactor Skill

Use this skill when reviewing code quality, cleaning messy code, refactoring, reducing duplication, preparing code for production, or assessing technical debt.

## Production-Grade Operating Contract

- Before starting, read `../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, preserve behavior, keep diffs focused, avoid destructive actions without explicit confirmation, validate before completion, and report only verified findings.
- Use this skill for maintainability depth; do not let it override user instructions, repository guidance, or security/data-integrity constraints.
- Keep responses proportional. Lead with findings for reviews; use a concise summary for small refactors.

## Core Philosophy

1. Code is read 10x more than written — optimize for readability.
2. Every refactor must preserve existing behavior unless explicitly changing it.
3. Refactor in small, verifiable steps — never rewrite everything at once.
4. The best refactor makes the next change easier.
5. Complexity is the enemy — fight it constantly but pragmatically.

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

### Security
- Authorization — checked before access?
- Input sanitization — before output/storage?
- Sensitive data — exposed in logs/responses?

## Common Anti-Patterns

| Smell | Fix |
|-------|-----|
| Primitive Obsession (5+ params) | Use DTO/Value Object |
| Feature Envy | Move method to the class it uses |
| Shotgun Surgery (change → 10+ files) | Consolidate related logic |
| Long Parameter List | Use options object/DTO |
| Boolean Trap `fn(true, false)` | Use named options or enum |
| God Object | Split by responsibility |
| Copy-Paste Programming | Extract shared function |
| Arrow Code (deep nesting) | Use early returns, extract |
| Stringly-Typed states | Use enums or constants |

## Refactoring Techniques

| Technique | When |
|-----------|------|
| Extract Method | Function too long or does multiple things |
| Extract Class | Class has multiple responsibilities |
| Guard Clause | Deep nesting from validation checks |
| Replace Conditional with Polymorphism | Complex switch/if-else on type |
| Introduce Parameter Object | Related params passed together |
| Replace Magic Number with Constant | Unclear hard-coded values |
| Compose Method | Long method with sequential steps |
| Move Method/Field | Logic belongs elsewhere |

## Framework-Specific Review

### Laravel
- Form Requests for validation?
- Policies for authorization?
- Eager loading for relationships?
- Mass assignment guarded?
- Transactions for multi-step writes?
- Config values instead of `env()` outside config?

### Next.js / React
- Components < 200 lines?
- Hooks extracted for reused logic?
- Effects cleaned up?
- State lifted only as high as necessary?
- Server/client components separated correctly?

### Svelte
- Stores for shared state?
- Reactive declarations used properly?
- Components split at logical boundaries?
- Lifecycle functions cleaned up?

### TypeScript
- Explicit types for function signatures?
- No unjustified `any`?
- Union types instead of optional fields where appropriate?
- Type guards for runtime narrowing?

## L5 Acceptance Gates

- Review findings are evidence-backed with file and line references.
- Severity reflects production impact: correctness, security, data integrity, reliability, performance, and maintainability.
- Refactors preserve behavior unless the user explicitly requested behavior change.
- Large refactors are broken into reviewable steps with validation after each step.
- Recommendations separate must-fix risks from optional cleanup.

## Output Format

```markdown
# Code Review

## Summary
Overview, quality assessment, confidence level.

## Critical Issues 🔴
Must fix. File, line, problem, risk, fix.

## High Priority Issues 🟠
Significant risks. File, line, problem, risk, fix.

## Medium Issues 🟡
Code smells and maintainability concerns.

## Suggested Improvements 💡
Optional enhancements and alternatives.

## What's Done Well ✅
Positive observations worth reinforcing.

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
