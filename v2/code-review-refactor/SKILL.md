---
name: code-review-refactor
description: Principal code review and refactoring — quality, patterns, anti-patterns, maintainability.
---

# Code Review & Refactor

## Philosophy

Code is read 10x more than written. Every refactor preserves behavior unless explicitly changing it. The best refactor makes the next change easier. Complexity is the enemy.

## Rules

1. Don't change behavior unless asked.
2. Small steps — each must compile and pass tests.
3. Clean diffs — reviewable in 60 seconds.
4. Good names eliminate need for comments.
5. Reduce duplication only when code changes for the same reason.
6. Extract only when it improves clarity.
7. YAGNI until proven otherwise.
8. Tests for risky refactors.
9. Preserve public APIs unless necessary.
10. Delete dead code — use version control.
11. Simplify conditionals — name or extract complex booleans.

## Severity

| Level | Meaning | Action |
|-------|---------|--------|
| 🔴 Critical | Bugs, security, data loss | Must fix before merge |
| 🟠 High | Performance, reliability risk | Should fix before merge |
| 🟡 Medium | Code smell, tech debt | Fix or ticket |
| 🟢 Low | Style, naming | Optional |
| 💡 Suggestion | Alternative approach | Informational |

## Review Checklist

**Quality**: Naming reveals intent? Functions < 30 lines? Classes < 300 lines? Nesting < 3 levels? No magic values? Dead code removed?

**Logic**: Edge cases (null/empty/zero/boundary)? Errors caught/logged/surfaced? Race conditions? Type safety? Input validated?

**Architecture**: Single responsibility? Low coupling? Consistent abstraction levels? No hidden side effects? Framework conventions?

**Performance**: N+1? Unbounded ops? Memory leaks? Caching opportunities?

**Security**: Authorization checked? Input sanitized? No sensitive data in logs/responses?

## Anti-Patterns → Fixes

| Smell | Fix |
|-------|-----|
| Primitive Obsession (5+ params) | DTO/Value Object |
| Feature Envy | Move method to used class |
| Shotgun Surgery (1 change → 10 files) | Consolidate |
| Boolean Trap `fn(true, false)` | Named options/enum |
| God Object | Split by responsibility |
| Copy-Paste × 3+ | Extract shared function |
| Arrow Code (deep nesting) | Early returns, extract |
| Stringly-Typed | Enums/constants |

## Refactoring Techniques

Extract Method/Class, Guard Clause, Replace Conditional with Polymorphism, Introduce Parameter Object, Replace Magic Number with Constant, Compose Method, Move Method/Field.

## Framework Review Points

**Laravel**: FormRequest? Policies? Eager loading? Guarded? Transactions? Config vs env()?
**Next.js/React**: Components < 200 lines? Hooks extracted? Effects cleaned? State minimal? Server/client split?
**Svelte**: Stores appropriate? Reactive declarations? Lifecycle cleanup?
**TypeScript**: Explicit signatures? No unjustified `any`? Type guards?

## Output Format

```
# Code Review
## Summary — overview, quality, confidence
## Critical Issues 🔴 — file, line, problem, risk, fix
## High Priority 🟠 — significant risks
## Medium Issues 🟡 — smells, maintainability
## Improvements 💡 — optional enhancements
## Done Well ✅ — positive observations
## Refactor Opportunities — quick wins (<30min), medium (1-4h), major (separate PR)
## Verdict — ✅ Approve | ⚠️ Approve+comments | 🔄 Request changes | ❌ Reject
```
