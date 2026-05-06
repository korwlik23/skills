---
name: testing-qa
description: Principal testing & QA — test strategy, pyramid, coverage, CI, performance, security testing, release confidence.
---

# Testing & QA

## Core Rules

1. Tests prevent regression — not achieve a coverage number.
2. Test behavior, not implementation — survive refactoring.
3. Fast suite (< 5 min) — devs run it often.
4. Flaky tests are worse than no tests.
5. Every bug fix includes a test that catches it.

## Testing Pyramid

```
    /  E2E  \        Few, slow, high confidence
   / Integration \   Some, moderate
  / Feature Tests  \ Many for routes
 /  Unit Tests      \Many, fast, focused
```

| Level | Speed | Tools |
|-------|-------|-------|
| Unit | <10ms each | PHPUnit, Jest, Vitest |
| Feature | <100ms each | PHPUnit, Supertest |
| Integration | <500ms each | PHPUnit, Jest+DB |
| E2E | <30s each | Playwright, Cypress |

## 10 Scenarios Per Feature

1. ✅ Happy path
2. ❌ Validation errors
3. 🔒 Unauthorized (401)
4. 🚫 Forbidden (403)
5. 🔍 Not found (404)
6. 📭 Empty state
7. 📊 Large data / pagination
8. 🔄 Duplicate submit (409 or idempotent)
9. ⚡ Edge cases (null, zero, negative, boundary, special chars)
10. 🐛 Regression (previously broken)

## API Test Matrix

| Test | Assert |
|------|--------|
| GET list | 200, paginated |
| GET single | 200, correct |
| GET missing | 404 |
| GET unauth | 401 |
| GET forbidden | 403 |
| POST valid | 201, created |
| POST invalid | 422, errors |
| POST duplicate | 409/422 |
| PUT valid | 200, updated |
| PUT forbidden | 403 |
| DELETE valid | 204 |
| DELETE forbidden | 403 |

## Frontend QA

| State | Check |
|-------|-------|
| Loading | Spinner/skeleton |
| Empty | Helpful message |
| Error | Message + retry |
| Success | Confirmation |
| Disabled | Visual + non-clickable |
| Mobile/Tablet/Desktop | Layout correct |
| Dark mode | Colors + contrast |
| Long text | Truncate/wrap |
| Missing image | Fallback |
| Slow API | Loading state |
| Refresh/back | State preserved |

## E2E Critical Flows

Register → verify → login. Login → dashboard → core feature → logout. CRUD resource. Search → filter → paginate. Form → validation error → fix → success. Payment flow. Admin ops.

## Test Quality Rules

Deterministic. Independent (no order dependency). Fast (unit <10ms, feature <100ms, E2E <30s). Readable names (`"returns 404 when user not found"`). Factories/fixtures (no hard-coded data). Mock externals. Clean up state.

**Don't test**: Framework internals. Trivial getters. Third-party lib functionality. Private methods directly. Implementation details.

## Coverage Targets

| Area | Min | Ideal |
|------|-----|-------|
| Auth/Payment flows | 90% | 100% |
| Business logic/services | 80% | 95% |
| API endpoints | 80% | 95% |
| Components | 60% | 80% |
| Utilities | 90% | 100% |
| Overall | 60% | 80% |

Focus on **high-risk code** first. Measure branch coverage. Track trends (should go up).

## CI Integration

Pipeline: Install → Lint → Static analysis → Unit tests → Feature tests → E2E (staging) → Coverage report → Fail if below threshold.

Rules: All tests pass before merge. No skipped tests without reason. Coverage must not decrease. E2E on staging, not every commit. Flaky tests fixed within 1 week.

## Security Tests

Auth required on protected endpoints. Authorization checked (IDOR). Input validation rejects malicious. Rate limiting active. CSRF protection. SQLi/XSS patterns rejected. File upload restrictions enforced.

## Performance Tests

When: New queries on large tables. New list endpoints. Critical flow changes. Before releases.
Measure: Response time (p50/p95/p99). Throughput. Query count/request. Memory under load. Error rate under load.

## Regression Protocol

Bug found → Write failing test → Fix → Test passes → Check similar code → Commit test+fix together.

Before release: All automated tests pass. Critical flows manual tested. New features tested all devices. Recent bug fix edge cases re-tested. Performance benchmarks OK. No new console errors.

## Output Format

```
# Test Plan
## Current Coverage — existing quality assessment
## Critical Gaps 🔴 — untested paths risking prod
## Tests to Add — Unit / Feature / E2E (grouped by priority)
## Manual QA Checklist — step-by-step for non-automatable
## Regression Checklist — re-test from recent fixes
## Performance Plan — endpoints + targets
## CI Recommendations — pipeline improvements
## Commands — copy-paste ready
## Confidence — 🔴 Low (don't release) | 🟠 Medium (with monitoring) | 🟡 High (safe) | 🟢 Very High (comprehensive)
```
