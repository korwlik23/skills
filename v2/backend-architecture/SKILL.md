---
name: backend-architecture
description: Principal backend architecture — APIs, services, queues, caching, event-driven design.
---

# Backend Architecture

## Core Rules

1. Controllers are thin — receive, delegate, respond. No business logic.
2. Business logic in services/actions. Services return data or throw domain exceptions, never HTTP responses.
3. Validate input before logic. Authorize before resource access.
4. Transactions for multi-step writes. No partial state.
5. Design for failure — every external call can fail, every queue can back up.
6. One Action class = one public method (single responsibility).
7. Max 2 levels of service chaining.

## Architecture Flow

```
Request → Middleware → Controller → Service/Action → Model/Repository → DB
                                  → Events/Jobs → External Services
```

## Extraction Signals

| Signal | Action |
|--------|--------|
| Controller > 30 lines/method | → Service/Action |
| Same logic in 2+ controllers | → Shared Service |
| Complex conditionals | → Policy/Strategy class |
| External API call | → Client class |
| Data transformation | → Transformer/Resource |
| Slow/async work | → Job/Command |

## Checklist

- [ ] Routes: method, URI, naming, grouping
- [ ] Middleware: auth, rate limit, CORS, scope
- [ ] Controller: thin, delegates, proper response
- [ ] Validation: all fields, FormRequest or schema
- [ ] Authorization: policies, guards, ownership
- [ ] Service layer: isolated, testable
- [ ] Models: relationships, eager loading
- [ ] Queries: no N+1, no SELECT *, indexed
- [ ] Transactions: multi-table writes wrapped
- [ ] Events: decoupled side effects
- [ ] Jobs: idempotent, retryable, timeout set
- [ ] Caching: reads cached, writes invalidate
- [ ] Logging: structured, no sensitive data
- [ ] Errors: domain exceptions, user-friendly messages
- [ ] Tests: unit for logic, feature for routes

## API Design

**Requests**: Proper HTTP methods. Plural nouns. Nested routes for relations. Query params for filter/sort/page. Version when breaking.

**Responses**: Consistent JSON. Proper status codes. Field-level validation errors. Paginated lists. No leaked internals. ISO 8601 dates.

| Status | Usage |
|--------|-------|
| 200/201/204 | Success / Created / Deleted |
| 400/401/403 | Bad request / Unauthenticated / Forbidden |
| 404/409/422 | Not found / Conflict / Validation failed |
| 429/500 | Rate limited / Server error |

**Resources**: Always use transformer layer. Control exposed fields. Hide internal IDs. Use `?include=` for relations.

## Caching Rules

Cache: expensive queries, external API responses, computed aggregations, rarely-changing config.
Always: set TTL, invalidate on write, use cache tags for groups, use locks for stampede prevention.
Never: cache user-specific data in shared cache without proper keying.

## Event-Driven Rules

Events are past-tense facts (`OrderPlaced`). Carry minimum payload. Listeners must be idempotent. Use queued listeners for async. Max ~5 listeners per event.

## Job Rules

Jobs must be: idempotent, retryable (max tries + backoff), failure-handled (`failed()` method), small (one thing), timeout-limited. Use separate queues for priority levels.

## Laravel Specifics

FormRequest for validation. Policies/Gates for auth. Eager loading (`with()`). `DB::transaction()`. `$fillable` explicit (never `$guarded = []`). `auth()->id()` over request user_id. Route model binding. `whenLoaded()` in Resources. `dispatchAfterResponse()` for fire-and-forget. Database constraints alongside validation.

## Node.js / Next.js Specifics

Zod/Joi for validation. Middleware for auth/rate limit. Try/catch for async. Connection pooling. Env vars for config. Structured JSON logging. Separate handlers from logic. TypeScript for critical paths. Graceful shutdown.

## Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| Fat controller | → Service |
| God service | → Split by domain |
| Implicit auth | → Explicit policy |
| Silent failures | → Log + alert |
| N+1 queries | → Eager load |
| Unbounded queries | → Paginate |
| Hard-coded config | → Env/config |
| String status | → Enum/constants |
| Sync external calls | → Queue |
| Missing transactions | → Wrap writes |

## Output Format

```
# Backend Review
## Architecture Assessment — health and patterns
## Critical Issues — security, data integrity, correctness
## Performance Issues — N+1, missing indexes, bottlenecks
## Design Issues — coupling, missing abstractions
## Recommended Changes — prioritized actions
## Implementation Notes — migration, backward compat
```
