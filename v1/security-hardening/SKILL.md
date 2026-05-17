---
name: security-hardening
description: >
  Use this skill for security review, vulnerability assessment, hardening,
  penetration testing, and production safety. Triggers on requests about
  authentication, authorization, OWASP Top 10, secrets management, CORS,
  CSRF, XSS, SQL injection, file upload security, rate limiting, security
  headers, or any request mentioning security, vulnerability, or exploit.
  Covers Laravel, Next.js, Node.js, and Svelte.
---

# Security Hardening Skill

Use this skill for security review, vulnerability fixing, hardening, penetration testing assessment, and production safety.

## Production-Grade Operating Contract

- Before starting, read `../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, default to least privilege, do not expose secrets, avoid production changes without explicit confirmation, and report only evidence-backed security findings.
- Use this skill for security depth; do not let it override user instructions, repository guidance, or legal/authorization boundaries.
- Keep responses proportional. Use the output format for security reviews; use a concise summary for small hardening patches.

## Core Principles

1. Never trust user input — validate everything, everywhere.
2. Defense in depth — multiple layers of security, never rely on one.
3. Least privilege — grant minimum permissions required.
4. Fail securely — errors should deny access, not grant it.
5. Security by default — secure configuration out of the box.

## OWASP Top 10 Coverage

### A01: Broken Access Control
- [ ] Every endpoint checks authentication.
- [ ] Every resource checks authorization (ownership/role).
- [ ] IDOR protected — users can't access other users' data by changing IDs.
- [ ] Vertical privilege escalation prevented — users can't access admin functions.
- [ ] Horizontal privilege escalation prevented — users can't access peer data.
- [ ] Rate limiting on sensitive endpoints.
- [ ] CORS configured restrictively.
- [ ] Directory listing disabled.

### A02: Cryptographic Failures
- [ ] Passwords hashed with bcrypt/argon2 (cost factor ≥ 12).
- [ ] Sensitive data encrypted at rest.
- [ ] TLS 1.2+ enforced for data in transit.
- [ ] No sensitive data in URLs (tokens, passwords).
- [ ] No sensitive data in logs.
- [ ] Proper key management — keys rotated, not hard-coded.
- [ ] No deprecated algorithms (MD5, SHA1 for security).

### A03: Injection
- [ ] SQL injection — parameterized queries, no raw string concatenation.
- [ ] Command injection — no user input in shell commands.
- [ ] XSS — output encoded, CSP headers set.
- [ ] LDAP injection — parameterized LDAP queries.
- [ ] Template injection — no user input in template rendering.
- [ ] Path traversal — sanitize file paths, use allowlists.
- [ ] SSRF — validate and restrict outbound URLs.

### A04: Insecure Design
- [ ] Threat modeling done for critical features.
- [ ] Business logic flaws reviewed (discount bypass, order tampering).
- [ ] Rate limiting on business-critical operations.
- [ ] Multi-step processes validated at each step.
- [ ] Fail-safe defaults for authorization.

### A05: Security Misconfiguration
- [ ] Debug mode disabled in production.
- [ ] Default credentials changed.
- [ ] Unnecessary features/endpoints disabled.
- [ ] Error messages don't leak internal details.
- [ ] Security headers configured.
- [ ] Directory listing disabled.
- [ ] Stack traces not exposed to users.

### A06: Vulnerable Components
- [ ] Dependencies audited (`npm audit`, `composer audit`).
- [ ] No known vulnerabilities in production dependencies.
- [ ] Dependencies pinned to specific versions.
- [ ] Regular update schedule for security patches.
- [ ] Unused dependencies removed.

### A07: Authentication Failures
- [ ] Brute force protection (rate limiting, account lockout).
- [ ] Password complexity requirements enforced.
- [ ] Session fixation prevented (regenerate on login).
- [ ] Session timeout configured.
- [ ] Multi-factor authentication available for sensitive operations.
- [ ] Password reset flow secure (time-limited tokens, one-use).

### A08: Data Integrity Failures
- [ ] Webhook signatures verified.
- [ ] Payment amounts validated server-side.
- [ ] Serialized data from untrusted sources validated.
- [ ] CI/CD pipeline secured.
- [ ] Software supply chain verified.

### A09: Logging & Monitoring Failures
- [ ] Security events logged (login, failed login, permission denied).
- [ ] Logs don't contain sensitive data (passwords, tokens, PII).
- [ ] Logs are tamper-resistant.
- [ ] Alerting on suspicious patterns (brute force, unusual access).
- [ ] Audit trail for critical operations.

### A10: Server-Side Request Forgery (SSRF)
- [ ] Outbound URLs validated against allowlist.
- [ ] Internal network access restricted.
- [ ] URL redirects validated.
- [ ] Metadata endpoints blocked (cloud provider).

## Security Rules

1. Never rely on frontend validation for security — always validate backend.
2. Always authorize on every request — never assume previous checks hold.
3. Never trust IDs from request without checking ownership.
4. Never expose internal stack traces, SQL, or file paths to users.
5. Never log passwords, tokens, API keys, PII, or payment secrets.
6. Rate limit: login, OTP, password reset, registration, public forms, webhooks, expensive endpoints.
7. Verify webhook signatures before processing.
8. Restrict file uploads: type, size, extension, MIME, storage location, public access.
9. Use secure headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options).
10. Use CSRF protection on all state-changing endpoints.
11. Use secure cookies: `HttpOnly`, `Secure`, `SameSite=Lax` minimum.
12. Regenerate session ID after login and privilege changes.

## Security Headers

Treat the following as a starting baseline, not a copy-paste policy. Tune CSP, HSTS, frame, referrer, and permissions directives to the app's asset sources, authentication model, embedding requirements, and deployment environment.

```
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' https:;
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
X-XSS-Protection: 0
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

## File Upload Security

1. Validate file extension against allowlist (not blocklist).
2. Validate MIME type server-side.
3. Limit file size (both per-file and total).
4. Generate random filenames — never use user-provided names.
5. Store outside web root or use private storage.
6. Scan for malware if accepting public uploads.
7. Serve files through application with proper headers.
8. Strip EXIF data from images if privacy-sensitive.
9. Never execute uploaded files.

## API Security

1. Use token-based auth (Bearer tokens, not cookies for APIs).
2. Tokens should expire — short-lived access + refresh token pattern.
3. Validate Content-Type header.
4. Rate limit all endpoints — stricter for auth endpoints.
5. Paginate all list endpoints — no unbounded responses.
6. Filter response fields — never return full database records.
7. Log all authentication events.
8. Version APIs to avoid breaking security improvements.

## Secrets Management

- Never commit secrets to version control.
- Use environment variables or secret management service.
- Rotate secrets regularly (API keys, tokens, passwords).
- Use different secrets per environment (dev, staging, prod).
- Audit who has access to production secrets.
- Use `.env.example` with dummy values, never real secrets.

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

## Penetration Testing Checklist

### Authentication
- [ ] Test brute force on login
- [ ] Test account enumeration via login/register/reset
- [ ] Test session fixation
- [ ] Test session timeout
- [ ] Test remember-me token security

### Authorization
- [ ] Test IDOR on all resource endpoints
- [ ] Test privilege escalation (user → admin)
- [ ] Test horizontal access (user A → user B data)
- [ ] Test API endpoints without auth token
- [ ] Test expired/revoked tokens

### Input
- [ ] Test SQL injection on all input fields
- [ ] Test XSS (reflected, stored, DOM-based)
- [ ] Test CSRF on state-changing endpoints
- [ ] Test file upload bypass
- [ ] Test path traversal

### Business Logic
- [ ] Test price tampering
- [ ] Test quantity manipulation
- [ ] Test coupon/discount abuse
- [ ] Test race conditions
- [ ] Test step-skipping in multi-step flows

## L5 Acceptance Gates

- Findings are tied to exploitability, affected assets/users, likelihood, and concrete remediation.
- Authentication, authorization, input validation, secrets, logging, headers, dependencies, and business logic are all considered.
- No real secrets, tokens, PII, or exploit payloads beyond what is necessary are exposed in output.
- Security fixes include tests or verification steps that prove the risk is reduced.
- Residual risk and monitoring recommendations are stated for anything not fully remediated.

## Output Format

```markdown
# Security Review

## Executive Summary
Overall security posture and critical risk areas.

## Critical Vulnerabilities 🔴
Exploitable now, immediate fix required.
For each: vulnerability, location, proof of concept, impact, fix.

## High Risk Issues 🟠
Significant risk, fix before next release.

## Medium Risk Issues 🟡
Should be addressed in upcoming sprints.

## Low Risk Issues 🟢
Best practice improvements.

## Security Configuration
Headers, cookies, CORS, rate limiting status.

## Recommended Fixes (Prioritized)
Ordered by risk × effort.

## Verification Steps
How to verify each fix is effective.

## Security Tests to Add
Automated tests to prevent regression.

## Ongoing Security Practices
Recommendations for continuous security.
```

## Example Trigger Phrases

- "Review security of this app"
- "Check for vulnerabilities"
- "Is this endpoint secure?"
- "Review authentication flow"
- "Check OWASP Top 10 coverage"
- "Audit secrets management"
- "Review file upload security"
- "Harden this for production"

## Usage Limitations

- Do not use this skill for general code quality — use `code-review-refactor` instead.
- Do not claim vulnerabilities without evidence from code, config, or dependencies.
- Do not run actual penetration tests or exploit code — assess and recommend only.
- Do not expose real secrets, tokens, or PII in findings or examples.
- Do not assume infrastructure security details not visible in the codebase.
