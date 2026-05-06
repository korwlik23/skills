---
name: security-hardening
description: Principal security review — OWASP Top 10, penetration testing, secrets, hardening across Laravel/Next.js/Svelte.
---

# Security Hardening

## Core Rules

1. Never trust user input — validate everything, everywhere.
2. Defense in depth — multiple layers, never rely on one.
3. Least privilege — minimum permissions required.
4. Fail securely — errors deny access, not grant it.
5. Secure by default.

## OWASP Top 10

### A01 Broken Access Control
Every endpoint checks auth. Every resource checks authorization + ownership. IDOR protected. Vertical/horizontal escalation prevented. Rate limiting. CORS restrictive.

### A02 Cryptographic Failures
Passwords: bcrypt/argon2 (cost ≥12). TLS 1.2+ enforced. No sensitive data in URLs or logs. Keys rotated, not hard-coded. No MD5/SHA1 for security.

### A03 Injection
SQL: parameterized queries only. XSS: output encoded + CSP. Command: no user input in shell. SSRF: validate outbound URLs. Path traversal: sanitize paths, use allowlists.

### A04 Insecure Design
Business logic reviewed (discount bypass, order tampering). Rate limit critical ops. Multi-step processes validated at each step. Fail-safe authorization defaults.

### A05 Misconfiguration
Debug off in prod. Default credentials changed. Unnecessary endpoints disabled. Errors don't leak internals. Security headers set.

### A06 Vulnerable Components
`npm audit` / `composer audit`. Pin versions. Regular update schedule. Remove unused deps.

### A07 Auth Failures
Brute force protection. Session fixation prevented (regenerate on login). Session timeout. Password reset: time-limited, one-use tokens.

### A08 Data Integrity
Webhook signatures verified. Payment amounts validated server-side. CI/CD pipeline secured. Supply chain verified.

### A09 Logging Failures
Security events logged (login, failed login, permission denied). No sensitive data in logs. Alerting on suspicious patterns. Audit trail for critical ops.

### A10 SSRF
Outbound URLs validated against allowlist. Internal network restricted. Cloud metadata endpoints blocked.

## Security Rules

1. Always validate backend — never rely on frontend.
2. Authorize every request — never assume previous checks.
3. Check ownership — never trust IDs without verification.
4. No internals to users — no stack traces, SQL, file paths.
5. No secrets in logs — passwords, tokens, PII, payment data.
6. Rate limit: login, OTP, reset, register, forms, webhooks, expensive endpoints.
7. Verify webhook signatures.
8. File uploads: allowlist extension + MIME, limit size, random filenames, store outside webroot, strip EXIF, never execute.
9. Secure cookies: HttpOnly, Secure, SameSite=Lax minimum.
10. CSRF on all state-changing endpoints.
11. Regenerate session after login and privilege changes.

## Security Headers

```
CSP: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:
HSTS: max-age=31536000; includeSubDomains
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

## Secrets Management

Never commit secrets. Use env vars or secret manager. Rotate regularly. Different per environment. Audit access. `.env.example` with dummy values only.

## Framework Specifics

**Laravel**: `APP_DEBUG=false`. CSRF middleware. Auth middleware. Policies/Gates. FormRequest. Explicit `$fillable`. Signed URLs. RateLimiter. Sanctum scopes. Secure session/cookie. No `env()` outside config. Telescope/Debugbar off in prod.

**Next.js/Node**: API routes validate auth+authz. Zod/Joi validation. Security headers in config. No `NEXT_PUBLIC_` for secrets. Rate limiting. Restricted CORS. No `eval()` with user input.

**Svelte/Kit**: Server load functions validate auth. Form actions validate CSRF. Hooks handle auth. Stores don't contain secrets. SSR doesn't leak server data.

## Penetration Testing Checklist

**Auth**: Brute force login. Account enumeration. Session fixation/timeout.
**Authz**: IDOR all endpoints. Privilege escalation. Expired/revoked tokens.
**Input**: SQLi all fields. XSS (reflected/stored/DOM). CSRF state-changing. File upload bypass. Path traversal.
**Logic**: Price tampering. Quantity manipulation. Coupon abuse. Race conditions. Step-skipping.

## Output Format

```
# Security Review
## Executive Summary — posture, critical risks
## Critical 🔴 — exploitable now (vulnerability, location, PoC, impact, fix)
## High 🟠 — fix before next release
## Medium 🟡 — upcoming sprints
## Low 🟢 — best practice
## Config Status — headers, cookies, CORS, rate limiting
## Fixes — prioritized by risk × effort
## Verification — how to confirm each fix
## Tests to Add — prevent regression
```
