---
name: bug-debugging
description: Principal debugging — systematic error analysis, log reading, root cause, production incidents.
---

# Bug Debugging

## Core Rules

1. Reproduce before fixing — can't verify what you can't reproduce.
2. Understand before changing — read error, trace flow, find root cause.
3. Fix the cause, not the symptom.
4. One change at a time — multiple changes hide what fixed it.
5. Every fix needs a test.

## Debug Process

### 1. Gather Info
What error? When? Where? Who? What changed recently? New or regression?

### 2. Reproduce

| Method | Reliability |
|--------|------------|
| Automated failing test | ✅ Best |
| Local repro steps | ✅ Good |
| Staging repro | ⚠️ OK |
| "Happened once in prod" | ❌ Poor |

Check: same role/perms, same data state, same config, same browser, same payload, same action sequence.

Can't reproduce? → Check logs for exact request. Look for race conditions, env-specific config, data-specific triggers. Add logging for next occurrence.

### 3. Isolate

**Frontend**: Console errors? Network tab correct? Component render? State issue? CSS?
**Backend**: Request reaches server? Middleware passes? Controller input correct? Service logic? Query results? Response formation?
**Database**: Wrong data? Missing data? Constraint violation? Connection issue?

### 4. Find Root Cause

| Technique | When |
|-----------|------|
| Stack trace reading | Error with trace available |
| Git bisect | "It worked before" |
| Print/log debugging | Tracing data flow |
| Minimum reproduction | Strip until bug disappears |
| Diff analysis | Working vs broken state |
| 5 Whys | Symptom → cause → deeper cause |

### 5. Fix
Minimal change at root cause. Don't refactor while fixing. Check same pattern elsewhere. Add guards for the bad state.

### 6. Verify
- [ ] Test fails without fix, passes with fix
- [ ] Original repro steps no longer trigger bug
- [ ] Related functionality still works
- [ ] Edge cases checked
- [ ] No performance regression

### 7. Prevent
Add test. Check similar patterns. Update docs. Add monitoring if hard to detect.

## HTTP Error Guide

| Status | Common Cause | Where to Look |
|--------|-------------|---------------|
| 400 | Malformed request | Payload, validation |
| 401 | Missing/expired token | Auth middleware, token |
| 403 | Wrong role, CORS | Policies, gates, CORS |
| 404 | Wrong URL, deleted resource | Routes, model binding |
| 419 | CSRF expired (Laravel) | CSRF middleware, session |
| 422 | Validation failed | Validation rules |
| 429 | Rate limited | Rate limiter config |
| 500 | Unhandled exception | App logs, error tracker |
| 502/504 | Server down/timeout | Server status, slow queries |

## Stack Trace Reading

Read bottom-up. Ignore framework internals. Find first line in YOUR code. Check that exact line + variable values.

## Common Patterns

| Error | Likely Cause | Direction |
|-------|-------------|-----------|
| "undefined is not a function" | Null/undefined | Null check, verify data loaded |
| "Cannot read property of null" | Data not loaded yet | Optional chaining, loading state |
| "Integrity constraint" | Duplicate/FK violation | Check unique constraints |
| "CORS error" | Backend CORS config | Check CORS middleware |
| "Memory limit exhausted" | Too much data | Paginate, chunk, stream |
| "Hydration mismatch" | Server/client HTML differs | Check dynamic content, useEffect |

## Log Analysis

Search: timestamp, user/session ID, request URL, ERROR/CRITICAL level, stack trace.

| Pattern | Interpretation |
|---------|---------------|
| Same error × many | Systematic issue |
| Error after deploy | Deploy introduced it |
| Error at fixed time daily | Cron/scheduled job |
| Error from one user | Data-specific or permission |
| Intermittent | Race condition, timeout, external |
| Growing count | Resource leak, scaling issue |

## Production Rules

**Safe**: Read logs, error tracking, monitoring, read-only queries, health endpoints, review deploys.
**Never**: Modify prod data, untested queries, breakpoints, restart during peak, untested hotfix.

**Incident protocol**: Detect → Acknowledge → Communicate → Triage (data loss? security? down?) → Mitigate (rollback/flag/scale) → Fix → Verify → Post-mortem

**Severity**: 🔴 P0 Service down/data loss (immediate) → 🟠 P1 Major feature broken (<1h) → 🟡 P2 Degraded with workaround (<4h) → 🟢 P3 Minor/cosmetic (next day)

## Output Format

```
# Bug Analysis
## Problem — what, when, who affected
## Root Cause — file, line, specific logic error
## Evidence — errors, logs, repro steps
## Fix — code change and why it fixes root cause
## Verification — failing test added, regression checked, edge cases
## Prevention — tests, monitoring, similar patterns checked
```
