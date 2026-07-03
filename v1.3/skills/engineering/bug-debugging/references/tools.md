# Debugging Tools Reference

Loaded on demand by the `bug-debugging` skill. Quick lookup of which tool is appropriate
for which layer. Pulled out of `SKILL.md` per the conciseness clause; load when you are
choosing how to instrument or inspect.

## Common Bug Categories

A pre-flight lookup before diving into a new bug — narrow the search by what *kind* of
bug it most resembles.

### Data Bugs

- Wrong data displayed (query issue, relationship issue)
- Missing data (filter too strict, soft delete, permission)
- Duplicate data (missing unique constraint, race condition)
- Stale data (caching issue, missing invalidation)
- Corrupted data (encoding issue, type mismatch, truncation)

### State Bugs

- Component shows wrong state (stale closure, missing re-render)
- Form loses data (unmount, navigation, key change)
- Loading never finishes (promise not resolved, error swallowed)
- Infinite loop (dependency array wrong, state update in render)

### Timing Bugs

- Race condition (two requests, optimistic update conflict)
- Timeout (slow query, external API, large file)
- Sequence dependency (action B runs before action A completes)
- Debounce/throttle issues (too aggressive, too lenient)

### Environment Bugs

- Works local, fails production (config, env vars, permissions)
- Works for dev, fails for user (CORS, auth, permissions)
- Works on Chrome, fails on Safari (CSS, API differences)
- Works with small data, fails with large data (pagination, memory)

## Frontend Tools

| Tool | Use For |
|------|---------|
| Browser DevTools Console | JavaScript errors, logging |
| Network Tab | API requests, responses, timing |
| React/Vue/Svelte DevTools | Component tree, state, props |
| Lighthouse | Performance, accessibility |
| `debugger` statement | Step-through debugging |

## Backend Tools

| Tool | Use For |
|------|---------|
| Application logs | Error traces, request logs |
| `dd()` / `dump()` (Laravel) | Variable inspection |
| `console.log()` (Node) | Variable inspection |
| Error tracking (Sentry) | Production error aggregation |
| Database query log | SQL queries, N+1 detection |
| `EXPLAIN ANALYZE` | Query performance |

## Database Tools

| Tool | Use For |
|------|---------|
| `EXPLAIN ANALYZE` | Query execution plan |
| Slow query log | Finding slow queries |
| `SHOW PROCESSLIST` | Active connections |
| `pg_stat_statements` | Query statistics (PostgreSQL) |

> Tool availability and command syntax vary by stack and version — confirm against the
> project's actual dependencies and current official docs per `../../../../RULES.md` §10.
