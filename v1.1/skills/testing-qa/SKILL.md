---
name: testing-qa
description: >
  Use this skill when adding tests, reviewing test coverage, debugging
  regressions, setting up test infrastructure, or preparing production
  release QA. Triggers on requests about unit tests, integration tests,
  E2E tests, test strategy, coverage gaps, flaky tests, CI pipeline tests,
  QA checklists, or any request mentioning testing or quality assurance.
---

# Testing QA Skill

Use this skill when adding tests, reviewing test coverage, debugging regressions, setting up test infrastructure, or preparing production release QA.

## Production-Grade Operating Contract

- Before starting, read `../../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, test behavior rather than implementation, avoid fabricating coverage/results, validate commands before claiming success, and report unrun checks explicitly.
- Use this skill for testing depth; do not let it override user instructions, repository guidance, or CI/runtime constraints.
- Keep responses proportional. Use the output format for test plans/release QA; use a concise summary for small test additions.
- Division of labor with `test-driven-development`: that skill owns the RED→GREEN→REFACTOR *order discipline* (when/how to write a test relative to code). This skill owns test *design, coverage strategy, pyramid, and QA*. When implementing a feature/bugfix, follow `test-driven-development` for the cycle and use this skill for what and how thoroughly to test. Do not restate the TDD cycle here.

## Core Principles

1. Tests exist to prevent regression — not to achieve a coverage number.
2. Test behavior, not implementation — tests should survive refactoring.
3. Fast tests run often — keep the suite under 5 minutes for dev experience.
4. Flaky tests are worse than no tests — they erode trust.
5. Every bug fix should include a test that would have caught it.

## Testing Pyramid

```
         ╱  E2E Tests  ╲         Few, slow, high confidence
        ╱  Integration   ╲       Some, moderate speed
       ╱   Feature Tests   ╲     Many for API routes
      ╱    Unit Tests        ╲   Many, fast, focused
     ╱_______________________ ╲  Foundation
```

| Level | What | Speed | Count | Tools |
|-------|------|-------|-------|-------|
| Unit | Pure functions, services, utilities | < 10ms each | Many | PHPUnit, Jest, Vitest |
| Feature | HTTP routes, API endpoints | < 100ms each | Many | PHPUnit, Supertest |
| Integration | Multi-service flows, database | < 500ms each | Some | PHPUnit, Jest + DB |
| E2E | Full user flows in browser | < 30s each | Few | Playwright, Cypress |

## Testing Strategy

For every feature, cover these 10 scenarios:

1. **Happy path** — expected input produces expected output.
2. **Validation errors** — invalid input returns proper errors.
3. **Unauthorized user** — unauthenticated request is rejected (401).
4. **Forbidden user** — authenticated but unpermitted request is rejected (403).
5. **Not found** — non-existent resource returns 404.
6. **Empty state** — no data returns empty result, not error.
7. **Large data** — pagination works, no timeout or memory issue.
8. **Duplicate submission** — idempotent or properly rejected (409).
9. **Edge cases** — null, zero, negative, boundary values, special characters.
10. **Regression** — previously broken scenarios have explicit tests.

## Backend Testing

### Unit Tests

Test pure logic without external dependencies:

```
✅ Service methods with mocked dependencies
✅ Validation rules and custom validators
✅ Data transformations and formatters
✅ Business rule calculations
✅ Helper/utility functions
✅ Value objects and DTOs
```

### Feature/Integration Tests

Test full request → response cycle:

```
✅ Route returns correct status code
✅ Route returns correct response structure
✅ Authentication required (401 without token)
✅ Authorization checked (403 for wrong user)
✅ Validation errors returned with correct format
✅ Database writes committed correctly
✅ Database writes rolled back on failure
✅ Events dispatched
✅ Jobs dispatched/queued
✅ Notifications sent
✅ Side effects executed (or not for dry run)
```

### API Test Checklist

For every API endpoint:

| Test | Assertion |
|------|-----------|
| GET list | 200, paginated, correct structure |
| GET single | 200, correct resource |
| GET not found | 404 |
| GET unauthorized | 401 |
| GET forbidden | 403 (other user's resource) |
| POST valid | 201, resource created |
| POST invalid | 422, validation errors |
| POST duplicate | 409 or 422 |
| PUT/PATCH valid | 200, resource updated |
| PUT/PATCH forbidden | 403 |
| DELETE valid | 204 or 200 |
| DELETE forbidden | 403 |
| DELETE not found | 404 |

### Database Testing Rules

- Use transactions to rollback after each test (RefreshDatabase).
- Use factories/fixtures for test data — never hard-coded IDs.
- Test database constraints (unique, foreign key, not null).
- Test soft delete behavior if used.
- Verify eager loading in critical queries.

## Frontend Testing

### Component Testing

```
✅ Renders correctly with required props
✅ Renders correctly with optional props
✅ Handles missing/null props gracefully
✅ Triggers correct events/callbacks
✅ Displays loading state
✅ Displays error state
✅ Displays empty state
✅ Responds to user interaction (click, type, submit)
```

### Frontend QA Checklist

| State | What to Check |
|-------|---------------|
| Loading | Spinner/skeleton shown, content hidden |
| Empty | Helpful message, not blank screen |
| Error | Error message shown, retry available |
| Success | Confirmation, data updated |
| Disabled | Visually distinct, not clickable |
| Mobile | Layout correct, touch targets 44px+ |
| Tablet | Layout adjusts appropriately |
| Desktop | Full layout, no wasted space |
| Dark mode | Colors correct, contrast sufficient |
| Long text | Truncated or wrapped, not overflowing |
| Missing image | Fallback shown, layout intact |
| Slow API | Loading state shown, no timeout crash |
| Refresh | State preserved or gracefully reset |
| Back button | Navigation works, no broken state |

### E2E Test Scenarios

Write E2E tests for critical user flows:

```
✅ User registration → email verification → first login
✅ Login → dashboard → core feature → logout
✅ Create resource → edit → delete
✅ Search → filter → paginate
✅ Form submission → validation error → fix → success
✅ Payment flow (if applicable)
✅ Admin operations (if applicable)
```

## Test Quality Rules

### Must Follow

1. Tests must be **deterministic** — same result every run.
2. Tests must be **independent** — no dependency on execution order.
3. Tests must be **fast enough for their role** — set project-specific budgets; keep smoke tests quick and track suite runtime trends.
4. Tests must be **readable** — test name describes the scenario.
5. Tests must use **factories/fixtures** — no hard-coded test data.
6. Tests must **mock external services** — no real API calls in tests.
7. Tests must **clean up** — no leftover state between tests.

### Test Naming Convention

Use descriptive names that explain the scenario:

```
✅ "it returns 404 when user does not exist"
✅ "it prevents unauthorized users from accessing admin"
✅ "it validates email format on registration"

❌ "test1"
❌ "it works"
❌ "test user endpoint"
```

### What NOT to Test

- Framework internals (Laravel's validation engine, React's rendering).
- Trivial getters/setters with no logic.
- Third-party library functionality.
- Implementation details that may change during refactoring.
- Private methods directly (test through public API).

## Test Coverage Strategy

### Coverage Targets

| Area | Minimum | Ideal |
|------|---------|-------|
| Auth flows | 90% | 100% |
| Payment/checkout | 90% | 100% |
| Business logic/services | 80% | 95% |
| API endpoints | 80% | 95% |
| Controllers | 70% | 85% |
| Frontend components | 60% | 80% |
| Utility functions | 90% | 100% |
| Overall project | 60% | 80% |

### Coverage Rules

- Coverage percentage alone is meaningless — quality matters.
- 100% coverage doesn't mean no bugs — it means every line was executed.
- Focus coverage on **high-risk code** first (auth, payment, business logic).
- Measure branch coverage, not just line coverage.
- Track coverage trends — it should go up, not down.

## CI/CD Integration

### CI Pipeline Test Stage

```yaml
# Example pipeline structure
test:
  steps:
    - Install dependencies
    - Run linting (code style)
    - Run static analysis (type checking)
    - Run unit tests
    - Run feature/integration tests
    - Run E2E tests (on staging build)
    - Generate coverage report
    - Fail if coverage drops below threshold
```

### CI Rules

1. All tests must pass before merge — no exceptions.
2. No skipped tests without documented reason.
3. Coverage must not decrease on PR.
4. E2E tests run on staging deploy, not every commit.
5. Test results visible in PR — use reporters.
6. Flaky tests are tracked and fixed within 1 week.

## Performance Testing

### When to Performance Test

- New database queries on large tables.
- New API endpoints serving lists.
- Changes to critical user flows.
- Before major releases.

### What to Measure

- Response time (p50, p95, p99).
- Throughput (requests/second).
- Database query count per request.
- Memory usage under load.
- Error rate under load.

## Security Testing

### Automated Security Tests

```
✅ Authentication required on protected endpoints
✅ Authorization checked (IDOR prevention)
✅ Input validation rejects malicious input
✅ Rate limiting active on auth endpoints
✅ CSRF protection on state-changing endpoints
✅ SQL injection patterns rejected
✅ XSS patterns rejected
✅ File upload restrictions enforced
```

## Regression Testing

### When Fixing a Bug

1. **Reproduce** — Write a test that fails with the bug.
2. **Fix** — Implement the fix.
3. **Verify** — Confirm the test passes.
4. **Review** — Check for similar bugs in related code.

### Regression Checklist

Before every release:

- [ ] All automated tests pass.
- [ ] Critical user flows tested manually.
- [ ] New features tested on all target devices/browsers.
- [ ] Edge cases from recent bug fixes re-tested.
- [ ] Performance benchmarks within acceptable range.
- [ ] No new console errors or warnings.

## L5 Acceptance Gates

- Test strategy maps to business-critical paths, security/data risks, and recent changes.
- New tests are deterministic, isolated, readable, and fail for the intended regression.
- Coverage targets are risk-based and project-specific, not vanity percentages.
- External services are mocked or isolated unless the test is explicitly an integration/E2E check.
- Validation clearly distinguishes tests run, tests not run, failures, flakes, and residual release risk.

## Output Format

```markdown
# Test Plan

## Current Coverage Assessment
Overview of existing test coverage and quality.

## Critical Test Gaps 🔴
Untested critical paths that risk production failures.

## Automated Tests to Add
Grouped by priority and test level:

### Unit Tests
- Test description (file, function, scenarios)

### Feature/Integration Tests
- Test description (endpoint, scenarios)

### E2E Tests
- Test description (user flow, scenarios)

## Manual QA Checklist
Step-by-step manual verification for features that can't be automated.

## Regression Checklist
Re-test items from recent bug fixes and changes.

## Performance Test Plan
Endpoints and flows to load test, with targets.

## CI/CD Recommendations
Pipeline configuration and test automation improvements.

## Commands to Run
Copy-paste-ready test commands.

## Release Confidence
- 🔴 Low — Critical gaps, do not release
- 🟠 Medium — Known risks, release with monitoring
- 🟡 High — Minor gaps, safe to release
- 🟢 Very High — Comprehensive coverage, confident release
```

## Example Trigger Phrases

- "Add tests for this feature"
- "What's the test coverage like?"
- "Write unit tests for this service"
- "Set up E2E testing"
- "Review test quality"
- "This test is flaky"
- "Create a QA checklist for release"
- "Is this safe to release?"
- "Add regression tests for this bug fix"

## Usage Limitations

- Do not fabricate test results or coverage numbers — run commands or state they were not run.
- Do not use this skill for feature implementation — use domain-specific skills instead.
- Do not write tests that depend on execution order or shared mutable state.
- Do not mock so heavily that the test no longer validates real behavior.
- Do not skip stating what tests were not written and why.
