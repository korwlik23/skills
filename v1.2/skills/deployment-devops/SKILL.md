---
name: deployment-devops
description: >
  Use this skill for deployment, production readiness, server setup, CI/CD,
  Docker, rollback, zero-downtime deployment, queue workers, cron, environment
  config, monitoring, alerting, observability, backup, and infrastructure.
  Triggers on requests about deploying, going live, server issues, pipeline
  setup, or any production operations concern.
---

# Deployment DevOps Skill

Use this skill for deployment, production readiness, server setup, CI/CD, rollback, zero-downtime, queue workers, cron, environment issues, monitoring, and infrastructure.

## Production-Grade Operating Contract

- Before starting, read `../../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, treat production, infrastructure, secret, rollback, and migration changes as high risk and require explicit confirmation before irreversible action.
- Use this skill for deployment technical depth; do not let it override user instructions, repository guidance, or security/data-integrity constraints.
- Keep responses proportional. Use the output format for deploy reviews/plans; use a concise summary for small config fixes.

## Core Principles

1. If it's not automated, it will break.
2. Every deployment must be reversible.
3. Monitor everything that matters — alert only on what's actionable.
4. Infrastructure should be reproducible — never rely on manual server setup.
5. Security is not optional in production.

## Production Readiness Checklist

### Environment & Config
- [ ] Environment variables set correctly (no dev values in prod)
- [ ] `APP_ENV=production` / `NODE_ENV=production`
- [ ] Debug mode disabled (`APP_DEBUG=false`)
- [ ] Correct `APP_URL` / `NEXT_PUBLIC_URL`
- [ ] Secrets rotated from development values
- [ ] No `.env` file committed to version control

### Build & Deploy
- [ ] Build command runs without errors
- [ ] All tests pass
- [ ] Migrations run safely (`--force` flag)
- [ ] Cache cleared and rebuilt
- [ ] Assets compiled and optimized
- [ ] Source maps disabled or restricted in production

### Infrastructure
- [ ] SSL/TLS configured and auto-renewing
- [ ] Web server properly configured (Nginx/Apache/Caddy)
- [ ] Storage permissions correct
- [ ] File upload limits configured
- [ ] Gzip/Brotli compression enabled
- [ ] Static asset caching headers set

### Background Processing
- [ ] Queue worker running via supervisor/systemd
- [ ] Queue worker restart on deploy
- [ ] Scheduler/cron configured
- [ ] Failed job handling configured
- [ ] Job timeout set

### Data & Backup
- [ ] Database backup automated (daily minimum)
- [ ] Backup restoration tested
- [ ] File storage backup configured
- [ ] Log rotation configured

### Monitoring & Alerting
- [ ] Error tracking configured (Sentry, Bugsnag, etc.)
- [ ] Uptime monitoring active
- [ ] Health check endpoint exists and is monitored
- [ ] Performance monitoring (APM) configured
- [ ] Disk space monitoring
- [ ] Log aggregation configured

### Security
- [ ] Rate limiting on auth endpoints
- [ ] Rate limiting on public forms
- [ ] CORS configured correctly
- [ ] Security headers set (CSP, HSTS, X-Frame-Options)
- [ ] No exposed debug routes (telescope, debugbar, phpinfo)
- [ ] Admin panel access restricted

## Zero-Downtime Deployment

### Deployment Flow

```
1. Pull code to new release directory
2. Install dependencies (composer/npm)
3. Build assets
4. Run tests (if CI didn't)
5. Run safe migrations
6. Warm cache
7. Switch symlink atomically
8. Reload app server gracefully (PHP-FPM, PM2, etc.)
9. Restart queue workers safely
10. Verify health check
11. Keep previous release for rollback
12. Clean old releases (keep last 5)
```

### Migration Safety for Zero-Downtime

The schema-change safety matrix and universal migration rules are the pack-wide
canonical source: **`../database-performance/references/migration-safety.md`** — use it,
do not restate it here.

Zero-downtime-specific deploy ordering on top of that matrix:

- Expand → migrate → contract: ship the additive/backward-compatible change first,
  backfill, deploy code that uses the new shape, only then remove the old shape.
- For "remove column" / "drop table": deploy the code that stops referencing it
  **before** the destructive migration, never in the same release.
- Run long backfills/`CREATE INDEX CONCURRENTLY` outside the deploy critical path.

## CI/CD Pipeline

### Recommended Pipeline Stages

```
1. Lint → Static analysis, code style
2. Test → Unit, integration, feature tests
3. Build → Compile assets, container image
4. Security → Dependency audit, secret scanning
5. Deploy Staging → Auto-deploy, smoke test
6. Deploy Production → Manual trigger or auto with approval
7. Post-Deploy → Health check, smoke test, notify
```

### CI/CD Rules

- Never deploy without passing tests.
- Pin dependency versions — no `latest` in production.
- Use build artifacts — don't rebuild between stages.
- Keep pipeline under 10 minutes for dev experience.
- Separate build and runtime dependencies.
- Scan for known vulnerabilities in dependencies.

## Docker Guidelines

### Dockerfile Best Practices

- Use specific base image versions — never `latest`.
- Use multi-stage builds — separate build from runtime.
- Put rarely changing layers first (dependencies before code).
- Run as non-root user.
- Set appropriate `HEALTHCHECK`.
- Use `.dockerignore` to exclude unnecessary files.
- Don't store secrets in image layers.
- Keep images small — use Alpine or distroless where possible.

### Docker Compose for Development

- Match production services (database, cache, queue).
- Use volumes for code in development.
- Use named volumes for data persistence.
- Set resource limits.

## Framework-Specific Deployment

Concrete Laravel and Node.js/Next.js deployment commands and production-config
checklists are in `references/framework-deployment.md` — load it when deploying one of
those stacks. The framework-agnostic readiness/zero-downtime/rollback rules above and
below remain the source of truth; the reference only holds per-framework specifics.

## Rollback Procedures

### Instant Rollback (Symlink Deploy)

```bash
# Switch symlink to previous release
ln -sfn /releases/previous /current

# Reload app server
sudo systemctl reload php-fpm  # or pm2 reload

# Restart queue workers
php artisan queue:restart  # or pm2 restart workers
```

### Database Rollback

```bash
# Only after backup, verification, and explicit confirmation that the migration is safely reversible
php artisan migrate:rollback --step=1

# If not reversible — deploy forward fix instead
```

### Rollback Rules

1. Always prefer forward-fix over rollback when possible.
2. Test rollback procedures before you need them.
3. Keep previous release artifacts available.
4. Document which migrations are safely reversible.
5. Have a communication plan for rollback scenarios.
6. Confirm before any rollback that can discard data, change production state, or affect active users.

## Monitoring & Alerting

### What to Monitor

| Metric | Warning | Critical |
|--------|---------|----------|
| Error rate | > 1% | > 5% |
| Response time (p95) | > 1s | > 3s |
| CPU usage | > 70% sustained | > 90% |
| Memory usage | > 80% | > 95% |
| Disk usage | > 75% | > 90% |
| Queue depth | > 1000 | > 10000 |
| Failed jobs | > 10/hour | > 100/hour |
| SSL expiry | < 30 days | < 7 days |
| Uptime | Any downtime | > 5 min |

### Alerting Rules

1. Alert on symptoms, not causes — "response time high" not "CPU high."
2. Every alert must be actionable — if you can't do anything, don't alert.
3. Set appropriate severity — not everything is page-worthy.
4. Include runbook links in alert messages.
5. Review and tune alerts monthly — remove noisy alerts.

## Incident Response

### When Things Go Wrong

```
1. Acknowledge — confirm the issue exists
2. Assess — determine scope and severity
3. Communicate — notify stakeholders
4. Mitigate — stop the bleeding (rollback, feature flag, scale)
5. Fix — implement proper fix
6. Verify — confirm fix works
7. Post-mortem — document what happened, why, and how to prevent
```

## Application Observability

Beyond infrastructure monitoring, ensure the application itself is observable:

### Logging Standards
- [ ] Structured logging (JSON format) with searchable fields
- [ ] Consistent log levels: DEBUG (dev only), INFO (normal ops), WARN (degraded), ERROR (failure)
- [ ] No debug logs in production hot paths
- [ ] Request ID / correlation ID in every log entry
- [ ] No secrets, tokens, PII, or passwords in logs

### Distributed Tracing
- [ ] Trace context propagated across service boundaries
- [ ] Async flows (queues, jobs, webhooks) carry correlation IDs
- [ ] External API calls include timing and status in traces

### Application Metrics
- [ ] Critical flows track throughput, latency (p50/p95/p99), and error rate
- [ ] Business metrics tracked (signups, orders, payments) where applicable
- [ ] Queue depth and processing time monitored
- [ ] Cache hit/miss ratio tracked

### Error Reporting
- [ ] Unhandled exceptions sent to error tracking (Sentry, Bugsnag, etc.)
- [ ] Error reports include request context (no secrets)
- [ ] Error grouping configured to avoid noise
- [ ] Alert on new error types or error rate spikes

### Operational Readiness
- [ ] Error messages help ops team understand impact and next steps
- [ ] High-risk changes have feature flags or rollback mechanism
- [ ] Runbook references included in alert configurations

## L5 Acceptance Gates

- Build, test, migration, deploy, rollback, and smoke-test paths are defined before release.
- Secrets and environment configuration are handled outside artifacts and logs.
- Rollback or forward-fix criteria are explicit, including database and queue-worker behavior.
- Monitoring, alerts, health checks, and ownership are documented.
- Production actions that affect users, data, or infrastructure require confirmation and a communication plan.

## Output Format

```markdown
# Deployment Review

## Current Risk Assessment
Overall production readiness score and critical gaps.

## Required Fixes (Before Deploy)
Must-fix items blocking safe deployment.

## Recommended Improvements
Important but non-blocking improvements.

## Deployment Steps
Numbered, copy-paste-ready deployment procedure.

## Rollback Steps
Numbered, copy-paste-ready rollback procedure.

## Verification Commands
Commands to verify successful deployment.

## Post-Deploy Checklist
Monitoring and verification tasks after deployment.

## Monitoring Gaps
Missing monitoring or alerting recommendations.
```

## Example Trigger Phrases

- "Deploy this to production"
- "Is this production-ready?"
- "Set up CI/CD pipeline"
- "Configure Docker for this project"
- "How do I rollback?"
- "Set up monitoring and alerting"
- "Review deployment process"
- "Server is down, what do I do?"
- "Set up zero-downtime deployment"

## Usage Limitations

- Do not execute destructive production commands without explicit confirmation.
- Do not modify production data, config, or infrastructure without backup verification.
- Do not assume cloud provider or hosting details not visible in the codebase.
- Do not skip stating rollback procedures for any deployment change.
- Do not restart production services during peak traffic without confirming with the user.
