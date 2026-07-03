# Error Patterns Reference

Loaded on demand by the `bug-debugging` skill. HTTP status taxonomy, stack-trace reading
rules, and the common-error-pattern lookup table. Pulled out of `SKILL.md` per the
conciseness clause; load this file when an error message or stack trace lands and the
high-level process steps don't tell you what to look at first.

## HTTP Error Analysis

| Status | Common Causes | Where to Look |
|--------|--------------|---------------|
| 400 | Malformed request, missing fields | Request payload, validation rules |
| 401 | Missing/expired token, wrong credentials | Auth middleware, token generation |
| 403 | Wrong role, missing permission, CORS | Policies, gates, CORS config |
| 404 | Wrong URL, deleted resource, route not registered | Routes, route model binding |
| 405 | Wrong HTTP method | Route definitions |
| 409 | Duplicate entry, conflict | Unique constraints, business logic |
| 419 | CSRF token expired (Laravel) | CSRF middleware, session config |
| 422 | Validation failed | Validation rules, request format |
| 429 | Rate limited | Rate limiter config |
| 500 | Unhandled exception | Application logs, error tracking |
| 502 | App server down/timeout | Server status, process manager |
| 503 | Maintenance/overloaded | Server config, deployment status |
| 504 | Upstream timeout | Proxy config, slow queries/APIs |

## Stack Trace Reading

```
1. Read BOTTOM-UP — the root cause is usually at the bottom.
2. Ignore framework internals — focus on YOUR code files.
3. Look for the FIRST line in YOUR codebase.
4. Note the file, line number, function name.
5. Check the exact line — what operation failed?
6. Check the variable values at that point.
```

## Common Error Patterns

| Error Pattern | Likely Cause | Quick Fix Direction |
|---------------|-------------|---------------------|
| "undefined is not a function" | Calling method on null/undefined | Add null check, verify data loaded |
| "Cannot read property of null" | Accessing property before data exists | Optional chaining, loading state |
| "SQLSTATE[23000] Integrity constraint" | Duplicate key or FK violation | Check unique constraints, data exists |
| "Class not found" | Missing import, autoload, namespace | Check imports, run autoload dump |
| "CORS error" | Backend CORS not configured | Check CORS middleware/config |
| "419 CSRF token mismatch" | Session expired, missing token | Verify CSRF token, check session |
| "Memory limit exhausted" | Loading too much data | Paginate, chunk, stream |
| "Maximum execution time exceeded" | Slow query or infinite loop | Profile query, check loop condition |
| "Connection refused" | Service not running | Check DB/Redis/queue service status |
| "Hydration mismatch" (React/Next) | Server/client HTML differs | Check dynamic content, useEffect |

> Framework-specific error codes evolve — confirm version-specific behavior against
> current official docs per `../../../../RULES.md` §10.
