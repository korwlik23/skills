# Framework-Specific Backend Reference

Loaded on demand by the `backend-architecture` skill. Per-framework backend rules; the
skill's SKILL.md keeps the framework-agnostic architecture rules and this file holds the
concrete Laravel / Node.js specifics (per the conciseness clause).

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

> Framework APIs evolve — confirm version-specific details against current official
> docs per `../../../../RULES.md` §10.
