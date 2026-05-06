---
name: backend-architecture
Mode: backend-architecture
description: Principal-level backend architecture skill for Laravel, Node.js, Next.js, API systems, service layers, queues, jobs, validation, authorization, caching, event-driven design, and business logic at scale.
---

# Backend Architecture Skill

Use this skill for backend feature work, refactoring, API design, service layer creation, business logic cleanup, architecture review, and scalability planning.

## Production-Grade Operating Contract

- Before starting, read `../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, preserve existing behavior, avoid destructive or data-changing actions without explicit confirmation, validate before completion, and report only verified results.
- Use this skill for backend technical depth; do not let it override user instructions, repository guidance, or security/data-integrity constraints.
- Keep responses proportional. Use the output format for reviews and substantial backend changes; use a concise summary for small fixes.

## Core Principles

1. Keep controllers thin — they receive, delegate, and respond.
2. Move business logic into services, actions, jobs, commands, or domain classes.
3. Validate request input before any business logic executes.
4. Authorize before reading or writing protected resources.
5. Use transactions for multi-step writes — never leave data in a partial state.
6. Avoid duplicate logic — extract shared behavior into reusable modules.
7. Avoid hidden side effects — every function should do what its name says.
8. Make code testable — inject dependencies, avoid static calls in critical paths.
9. Use framework conventions — don't fight the framework.
10. Preserve existing behavior unless explicitly asked to change it.
11. Design for failure — every external call can fail, every queue can back up.
12. Separate read and write paths when complexity demands it (CQRS-lite).

## Architecture Patterns

### Layered Architecture

```
Request → Middleware → Controller → Service/Action → Repository/Model → Database
                                  → Events/Jobs → External Services
```

### When to Extract

| Signal | Action |
|--------|--------|
| Controller > 30 lines per method | Extract to Service/Action |
| Same logic in 2+ controllers | Extract to shared Service |
| Complex conditional logic | Extract to Policy/Strategy class |
| External API call | Extract to dedicated Client class |
| Data transformation | Extract to Transformer/Resource |
| Scheduled/async work | Extract to Job/Command |

### Service Layer Rules

- One public method per Action class (single responsibility).
- Services may call other services but avoid deep chains (max 2 levels).
- Services return data or throw domain exceptions — never HTTP responses.
- Use DTOs or typed arrays for complex input/output between layers.

## Backend Checklist

For every backend task, verify:

- [ ] Routes — correct method, URI, naming, grouping
- [ ] Middleware — auth, rate limit, CORS, tenant scope
- [ ] Controller — thin, delegates to service, returns proper response
- [ ] Request validation — FormRequest or equivalent, all fields validated
- [ ] Authorization — policies, guards, gates, ownership checks
- [ ] Service/Action layer — business logic isolated and testable
- [ ] Model relationships — correct type, eager loading defined
- [ ] Database queries — no N+1, no SELECT *, proper indexes used
- [ ] Transactions — multi-table writes wrapped in transaction
- [ ] Events/Listeners — decoupled side effects
- [ ] Jobs/Queues — long-running tasks are async, retryable, idempotent
- [ ] Notifications — correct channels, throttled where needed
- [ ] Caching — cache reads where appropriate, invalidate on writes
- [ ] Logging — structured logs with context, no sensitive data
- [ ] Error handling — domain exceptions, fallback behavior, user-friendly messages
- [ ] Tests — unit for logic, feature for routes, integration for flows

## API Design Rules

### Request Design

- Use proper HTTP methods: GET (read), POST (create), PUT/PATCH (update), DELETE (remove).
- Use plural nouns for resources: `/api/users`, `/api/orders`.
- Use nested routes for relationships: `/api/users/{id}/orders`.
- Use query params for filtering, sorting, pagination: `?status=active&sort=-created_at&page=2`.
- Accept `Content-Type: application/json` for all mutation endpoints.
- Version APIs when breaking changes are unavoidable: `/api/v1/` or header-based.

### Response Design

- Consistent JSON structure across all endpoints.
- Always include appropriate HTTP status codes:

| Status | Usage |
|--------|-------|
| 200 | Success with data |
| 201 | Created successfully |
| 204 | Deleted successfully (no content) |
| 400 | Bad request / validation error |
| 401 | Unauthenticated |
| 403 | Forbidden / unauthorized |
| 404 | Resource not found |
| 409 | Conflict / duplicate |
| 422 | Validation failed (Laravel convention) |
| 429 | Rate limited |
| 500 | Server error |

- Include validation errors with field-level detail.
- Never leak stack traces, SQL queries, or internal paths.
- Never expose sensitive data (passwords, tokens, secrets).
- Paginate list endpoints — never return unbounded results.
- Use consistent date format (ISO 8601).

### API Resource/Transformer Rules

- For public API boundaries, use a resource/transformer layer rather than returning raw models.
- Control exactly which fields are exposed.
- Include related resources via `?include=` parameter or always-loaded defaults.
- Hide internal IDs when UUIDs or slugs are used publicly.

## Caching Strategy

### When to Cache

- Expensive database queries that don't change frequently.
- External API responses with acceptable staleness.
- Computed values (aggregations, reports, dashboards).
- Configuration/settings that rarely change.

### Cache Rules

1. Always set TTL — no indefinite caching without explicit reason.
2. Invalidate on write — clear or update cache when underlying data changes.
3. Use cache tags for group invalidation when supported.
4. Use cache locks for expensive computations to prevent stampede.
5. Log cache hit/miss ratio in production to validate strategy.
6. Never cache user-specific data in shared cache without proper keying.

## Event-Driven Design

### When to Use Events

- Sending notifications after an action.
- Updating search indexes.
- Syncing data to external systems.
- Audit logging.
- Any side effect that shouldn't block the main request.

### Event Rules

1. Events are facts — name them in past tense: `OrderPlaced`, `UserRegistered`.
2. Events carry data — include the minimum payload needed by listeners.
3. Listeners should be idempotent — safe to replay.
4. Use queued listeners for anything that can be async.
5. Keep listener count per event manageable — if > 5, consider consolidation.

## Queue/Job Rules

1. Jobs must be idempotent — safe to run twice with the same input.
2. Jobs must be retryable — set max tries and backoff strategy.
3. Jobs must handle failure — implement `failed()` method or dead-letter handling.
4. Jobs should be small — one job does one thing.
5. Set appropriate timeouts — don't let jobs run indefinitely.
6. Monitor queue depth and processing time in production.
7. Use separate queues for different priority levels.

## Laravel-Specific Rules

When working in Laravel:

- Use Form Request classes for validation — keep controllers clean.
- Use Policies/Gates for authorization — never inline permission checks.
- Use Eloquent relationships correctly — define inverse relationships.
- Use eager loading to avoid N+1 — `with()` or `load()`.
- Use `DB::transaction()` for multi-step writes — with proper exception handling.
- Use queues for long-running tasks — email, PDF, reports, API calls.
- Use config files instead of hard-coded environment logic.
- Add `fillable` or `guarded` fields explicitly — never use `$guarded = []`.
- Never trust `user_id` from request when `auth()->id()` should be used.
- Use route model binding when appropriate.
- Avoid putting complex business logic in Blade files.
- Use `whenLoaded()` in API Resources for conditional relationship inclusion.
- Use database-level constraints (unique, foreign key) in addition to validation.
- Use `dispatchAfterResponse()` for fire-and-forget tasks.
- Use model observers sparingly — prefer explicit event dispatching.

## Node.js / Next.js Backend Rules

When working in Node.js or Next.js API routes:

- Validate request body with Zod, Joi, or equivalent — never trust raw input.
- Use middleware for auth, rate limiting, and error handling.
- Handle async errors with try/catch — never let promises go unhandled.
- Use connection pooling for database connections.
- Use environment variables for configuration — never hard-code secrets.
- Use structured logging (JSON format) for production.
- Use proper HTTP status codes — don't return 200 for everything.
- Separate API route handlers from business logic.
- Use TypeScript for type safety in critical paths.
- Handle graceful shutdown — close connections, finish in-flight requests.

## Anti-Patterns to Catch

| Anti-Pattern | Why It's Bad | Fix |
|-------------|-------------|-----|
| Fat controller | Untestable, mixed concerns | Extract to service |
| God service | Does everything, hard to maintain | Split by domain |
| Implicit authorization | Security holes | Add explicit policy checks |
| Silent failures | Bugs go undetected | Log + alert on failure |
| N+1 queries | Performance killer | Eager load relationships |
| Unbounded queries | Memory/timeout issues | Always paginate |
| Hard-coded config | Inflexible, env-specific bugs | Use config/env vars |
| String-based status | Typo-prone, no IDE support | Use enums/constants |
| Sync external calls | Slow responses, timeout risk | Use queues/async |
| Missing transactions | Partial data corruption | Wrap in transaction |

## L5 Acceptance Gates

- Request path, validation, authorization, business logic, persistence, side effects, and response shape are all accounted for.
- Multi-step writes are transactional or explicitly compensated.
- External calls have timeout, retry/backoff, and failure behavior.
- List endpoints are bounded, filtered safely, and shaped through public response contracts.
- Critical behavior is covered by tests or the validation gap is stated.

## Output Format

When completing a backend task or review, structure the response as:

```markdown
# Backend Review

## Architecture Assessment
Brief overview of current architecture health and patterns used.

## Critical Issues
Issues that must be fixed before production — security, data integrity, or correctness.

## Performance Issues
N+1 queries, missing indexes, unbounded queries, sync bottlenecks.

## Design Issues
Architecture violations, coupling, missing abstractions, code organization.

## Recommended Changes
Specific, actionable changes ordered by priority.

## Implementation Notes
Technical details, migration steps, backward compatibility considerations.
```
