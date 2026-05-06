---
name: senior-fullstack-audit
description: Principal full-project audit — 20-area review, scoring, phased roadmap, actionable report.
---

# Fullstack Audit

## Goal

Deep principal-level audit of entire codebase → practical, prioritized report with effort estimates.

## Audit Scope (20 Areas)

Project structure, Architecture, Backend logic, Frontend UX, API design, Database schema, Security, Auth/authz, Performance (backend+frontend), Testing, Error handling, Logging, Deployment readiness, Maintainability, DX, Business logic, Scalability, Data integrity, Third-party integrations, Documentation.

## Process

### Phase 1: Discovery
Identify stack + versions + deps. Map structure (dirs/modules). Map entry points (routes/pages/APIs). Map data flow (request → process → store). Map config (env/secrets).

### Phase 2: High-Risk Review First

| Priority | Area | Risk |
|----------|------|------|
| 🔴 P0 | Auth (login/register/reset) | Account takeover |
| 🔴 P0 | Authorization (perms/roles) | Privilege escalation |
| 🔴 P0 | Payment/checkout | Financial loss |
| 🟠 P1 | Admin panel | Data manipulation |
| 🟠 P1 | File upload/download | Server compromise |
| 🟠 P1 | Webhooks | Data injection |
| 🟡 P2 | All API routes | Data exposure |
| 🟡 P2 | Search/filter/export | Performance, injection |
| 🟢 P3 | Static/public content | SEO, UX |

### Phase 3: Layer Review

**Architecture**: Appropriate for project size? Clean separation? Circular deps? Consistent organization?
**Backend**: Thin controllers? Logic in services? Efficient queries? Transactions? Idempotent jobs? Timeouts on external calls?
**Frontend**: Components sized well? All UI states handled? Responsive? Forms validated? Images optimized?
**Database**: Normalized? Indexes match queries? FKs defined? Migrations reversible? N+1?
**Security**: Every endpoint auth'd? Input validated server-side? OWASP addressed? Headers configured? Secrets managed?
**Performance**: Queries optimized (EXPLAIN)? Caching used? Assets optimized? Expensive ops async? Core Web Vitals?
**Testing**: Critical paths covered? Deterministic? Edge cases? E2E? CI-ready?
**Deployment**: Automated? Rollback possible? Monitoring configured? Backup automated?

### Phase 4: Classify

| Severity | SLA |
|----------|-----|
| 🔴 Critical | Fix immediately |
| 🟠 High | Fix within 1 week |
| 🟡 Medium | Fix within 1 month |
| 🟢 Low | When convenient |
| 💡 Improvement | Backlog |

## Scoring Rubric

Rate each 1-5: (1=broken/missing, 2=minimal, 3=adequate, 4=good, 5=excellent)

Architecture, Backend, Frontend, API Design, Database, Security, Performance, Testing, Error Handling, Deployment → **Overall /50**

## Metrics to Collect

Files/LOC count. Routes/endpoints count. DB tables count. Test coverage %. Bundle size. Dependency count. TODO/FIXME/HACK count. Build time. Largest files.

## Output Format

```
# Fullstack Audit Report

## Executive Summary
Score /50. Critical count. One paragraph health assessment.

## Scorecard
| Area | /5 | Status |
|------|-----|--------|
(10 areas)

## Critical Issues 🔴
Per issue: problem, file+line, risk, fix, effort.

## High 🟠 / Medium 🟡 / Low 🟢

## Security / Performance / Database / Frontend / Backend / Testing findings

## Deployment Risks

## Roadmap
### Phase 1: Before Production (X days) — items + effort
### Phase 2: Stability (X days)
### Phase 3: Scale (X days)
### Phase 4: Excellence (X days)

## Verdict
🔴 Not ready | 🟠 Almost ready | 🟡 Ready with caution | 🟢 Production ready
+ conditions to upgrade level
```
