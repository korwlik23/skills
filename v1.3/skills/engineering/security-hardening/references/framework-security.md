# Framework-Specific Security Reference

Loaded on demand by the `security-hardening` skill. Per-framework hardening checklists;
the skill's SKILL.md keeps OWASP coverage and framework-agnostic rules, this file holds
the concrete Laravel / Next.js-Node / SvelteKit specifics (per the conciseness clause).

## Laravel-Specific Security

- [ ] `APP_DEBUG=false` in production
- [ ] `APP_KEY` exists and is unique per environment
- [ ] CSRF middleware on all web routes
- [ ] Auth middleware on protected routes
- [ ] Policies/Gates for resource authorization
- [ ] Form Requests for input validation
- [ ] Mass assignment: explicit `$fillable` (never `$guarded = []`)
- [ ] Storage symlink doesn't expose private files
- [ ] File upload validation in Form Request
- [ ] Signed URLs for temporary file access
- [ ] RateLimiter configured for login/register/API
- [ ] Sanctum/Passport token scopes if used
- [ ] Session config: secure, httponly, samesite
- [ ] Cookie: secure, samesite, httponly
- [ ] No `env()` calls outside config files
- [ ] Telescope/Debugbar disabled in production

## Next.js / Node.js Security

- [ ] API routes validate authentication
- [ ] API routes validate authorization
- [ ] Input validated with Zod/Joi before processing
- [ ] `next.config.js` security headers configured
- [ ] Environment variables not exposed to client (no `NEXT_PUBLIC_` for secrets)
- [ ] Server actions validate input
- [ ] Middleware checks authentication for protected routes
- [ ] Rate limiting on API routes
- [ ] CORS configured restrictively
- [ ] File uploads validated and stored securely
- [ ] No `eval()` or `Function()` with user input
- [ ] Dependencies audited regularly

## Svelte / SvelteKit Security

- [ ] Server-side load functions validate authentication
- [ ] Form actions validate CSRF
- [ ] API routes validate input
- [ ] Hooks handle auth checking
- [ ] Client-side stores don't contain secrets
- [ ] SSR doesn't leak server data to client

> Framework security defaults change between versions — confirm against current
> official security docs/advisories per `../../../../RULES.md` §10.
