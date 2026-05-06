---
name: senior-fullstack-audit
Mode: senior-fullstack-audit
description: Principal-level full project audit for architecture, backend, frontend, database, security, performance, testing, deployment, maintainability, scalability, and business logic correctness with actionable roadmap.
---

# Senior Fullstack Audit Skill

Use this skill when the user asks to audit, inspect, review, validate, or assess the whole project.

## Production-Grade Operating Contract

- Before starting, read `../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, use evidence-based findings, avoid changing code during read-only audits unless asked, and report uncertainty clearly.
- Use this skill for full-project audit depth; do not let it override user instructions, repository guidance, or security/data-integrity constraints.
- Keep responses proportional. Use the output format for full audits; use a shorter findings-first format for targeted reviews.

## Goal

Perform a deep principal-level audit of the entire codebase and produce a practical, prioritized improvement report with clear action items and effort estimates.

## Audit Scope

Review these 20 areas systematically:

1. Project structure and organization
2. Architecture patterns and decisions
3. Backend logic and service design
4. Frontend UX/UI quality
5. API design and consistency
6. Database schema and queries
7. Security posture
8. Authentication and authorization
9. Performance (backend and frontend)
10. Testing coverage and quality
11. Error handling strategy
12. Logging and observability
13. Deployment readiness
14. Maintainability and code health
15. Developer experience
16. Business logic correctness
17. Scalability readiness
18. Data integrity and consistency
19. Third-party integration health
20. Documentation completeness

## Audit Process

### Phase 1: Discovery (Map the System)

1. Identify the tech stack, framework versions, and key dependencies.
2. Map the project structure — directories, modules, packages.
3. Identify entry points — routes, pages, API endpoints.
4. Map the data flow — request → processing → response → storage.
5. Identify configuration management — env vars, config files, secrets.

### Phase 2: High-Risk Review (Critical Paths First)

Review high-risk files and flows in this priority order:

| Priority | Area | Risk |
|----------|------|------|
| 🔴 P0 | Authentication (login, register, password reset) | Account takeover |
| 🔴 P0 | Authorization (permissions, roles, guards) | Privilege escalation |
| 🔴 P0 | Payment/checkout (if applicable) | Financial loss |
| 🟠 P1 | Admin panel/dashboard | Data manipulation |
| 🟠 P1 | File upload/download | Server compromise |
| 🟠 P1 | Webhook handlers | Data injection |
| 🟠 P1 | User management (CRUD, profile) | Data breach |
| 🟡 P2 | API routes (all endpoints) | Data exposure |
| 🟡 P2 | Search/filter/export | Performance, injection |
| 🟢 P3 | Static pages and public content | SEO, UX |

### Phase 3: Systematic Review (Every Layer)

#### Architecture Review
- Is the architecture appropriate for the project size?
- Are responsibilities separated cleanly (controllers, services, models)?
- Are there circular dependencies?
- Is the dependency direction correct (domain doesn't depend on infrastructure)?
- Is the code organized by feature or by layer? Is it consistent?

#### Backend Review
- Are controllers thin?
- Is business logic in services/actions?
- Are database queries efficient?
- Are transactions used for multi-step writes?
- Are jobs idempotent and retryable?
- Are external API calls handled with timeouts and retries?

#### Frontend Review
- Are components reasonably sized?
- Is state management appropriate?
- Are all UI states handled (loading, error, empty, success)?
- Is the layout responsive across breakpoints?
- Are forms validated with good UX?
- Are images optimized?

#### Database Review
- Is the schema normalized appropriately?
- Are indexes covering actual query patterns?
- Are foreign keys and constraints defined?
- Are migrations reversible?
- Are there N+1 query patterns?

#### Security Review
- Is every endpoint authenticated and authorized?
- Is input validated on the server?
- Are OWASP Top 10 risks addressed?
- Are security headers configured?
- Are secrets properly managed?

#### Performance Review
- Are queries optimized (EXPLAIN check)?
- Is caching used where appropriate?
- Are assets optimized (images, fonts, bundles)?
- Are expensive operations async (queues)?
- What are the Core Web Vitals?

#### Testing Review
- What is the test coverage for critical paths?
- Are tests deterministic and independent?
- Are edge cases covered?
- Is there integration/E2E testing?
- Can the test suite run in CI?

#### Deployment Review
- Is deployment automated?
- Is rollback possible?
- Are environment configs correct?
- Is monitoring configured?
- Is backup automated?

### Phase 4: Classify and Prioritize

Every issue must be classified:

| Severity | Definition | SLA |
|----------|-----------|-----|
| 🔴 Critical | Active vulnerability, data loss risk, or production failure | Fix immediately |
| 🟠 High | Significant risk, major bug, or blocking issue | Fix within 1 week |
| 🟡 Medium | Code smell, performance concern, or UX problem | Fix within 1 month |
| 🟢 Low | Best practice, minor improvement | Fix when convenient |
| 💡 Improvement | Enhancement suggestion, future optimization | Backlog |

### Phase 5: Roadmap Creation

Create a phased improvement plan:

- **Phase 1**: Must fix before production — security, data integrity, critical bugs.
- **Phase 2**: Stability — error handling, logging, monitoring, testing.
- **Phase 3**: Scale — performance, caching, query optimization, infrastructure.
- **Phase 4**: Excellence — code quality, architecture, developer experience, documentation.

## Scoring Rubric

Rate each area on a 1-5 scale:

| Score | Meaning |
|-------|---------|
| 1 | Broken or missing — critical risk |
| 2 | Minimal — significant gaps |
| 3 | Adequate — meets basic requirements |
| 4 | Good — follows best practices |
| 5 | Excellent — production-grade, scalable |

### Areas to Score

- Architecture: /5
- Backend Logic: /5
- Frontend UX: /5
- API Design: /5
- Database: /5
- Security: /5
- Performance: /5
- Testing: /5
- Error Handling: /5
- Deployment: /5
- **Overall: /50**

## Metrics to Collect

Where possible, measure:

- Total files and lines of code
- Number of routes/endpoints
- Number of database tables
- Test coverage percentage
- Bundle size (frontend)
- Number of dependencies
- Number of TODO/FIXME/HACK comments
- Build time
- Largest files (potential god objects)

## L5 Acceptance Gates

- Findings are evidence-based, prioritized, and tied to production impact.
- Audit scope and blind spots are explicit, including commands or areas that could not be inspected.
- Security, data integrity, correctness, reliability, performance, testing, deployment, maintainability, and UX are all considered.
- Recommendations are phased into must-fix, should-fix, and longer-term improvements with effort estimates.
- The final verdict is actionable: ship/no-ship/readiness level and next verification steps.

## Output Format

```markdown
# Fullstack Audit Report

## Executive Summary
Project health score (/50), critical risk count, overall assessment.
One paragraph summary of the project's current state.

## Scorecard

| Area | Score | Status |
|------|-------|--------|
| Architecture | /5 | |
| Backend Logic | /5 | |
| Frontend UX | /5 | |
| API Design | /5 | |
| Database | /5 | |
| Security | /5 | |
| Performance | /5 | |
| Testing | /5 | |
| Error Handling | /5 | |
| Deployment | /5 | |
| **Overall** | **/50** | |

## Critical Issues 🔴
For each:
- Problem description
- File location with line reference
- Risk assessment
- Recommended fix
- Effort estimate

## High Priority Issues 🟠
## Medium Priority Issues 🟡
## Low Priority Issues 🟢

## Security Findings
## Performance Findings
## Database Findings
## Frontend / UX Findings
## Backend Findings
## Testing Gaps

## Deployment Risks

## Recommended Roadmap

### Phase 1: Must Fix Before Production
Estimated effort: X days
- Item 1 (effort)
- Item 2 (effort)

### Phase 2: Stability and Reliability
Estimated effort: X days

### Phase 3: Scale and Performance
Estimated effort: X days

### Phase 4: Excellence and Developer Experience
Estimated effort: X days

## Final Verdict

State the project status:
- 🔴 Not production ready — critical issues must be resolved
- 🟠 Almost production ready — high priority issues remain
- 🟡 Production ready with caution — known risks accepted
- 🟢 Production ready — meets professional standards

Include specific conditions for upgrading to the next level.
```
