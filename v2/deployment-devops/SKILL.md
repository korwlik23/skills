---
name: deployment-devops
description: Principal deployment & DevOps — CI/CD, Docker, monitoring, zero-downtime, incident response.
---

# Deployment & DevOps

## Core Rules

1. If it's not automated, it will break.
2. Every deployment must be reversible.
3. Monitor everything that matters — alert only on what's actionable.
4. Infrastructure must be reproducible.

## Production Readiness

**Environment**: Env vars correct (no dev values). Production mode. Debug off. Secrets rotated. No `.env` committed.

**Build**: Build passes. Tests pass. Migrations safe. Cache cleared/rebuilt. Assets compiled. Source maps restricted.

**Infrastructure**: SSL auto-renewing. Storage permissions. Upload limits. Compression enabled. Static asset caching.

**Background**: Queue worker via supervisor. Worker restart on deploy. Scheduler configured. Failed job handling. Timeouts set.

**Data**: DB backup automated (daily min). Backup restoration tested. Log rotation configured.

**Monitoring**: Error tracking (Sentry etc). Uptime monitoring. Health endpoint. APM configured. Disk space alerts. Log aggregation.

**Security**: Rate limiting on auth/forms. CORS restricted. Security headers. No debug routes exposed. Admin access restricted.

## Zero-Downtime Deploy

```
1. Pull to release dir → 2. Install deps → 3. Build assets → 4. Run tests
→ 5. Safe migrations → 6. Warm cache → 7. Switch symlink atomically
→ 8. Reload app server → 9. Restart queue workers → 10. Health check
→ 11. Keep previous release → 12. Clean old (keep 5)
```

### Migration Safety

| Type | Safe? | Strategy |
|------|-------|----------|
| Add nullable column | ✅ | Direct |
| Add NOT NULL column | ⚠️ | Add nullable → backfill → alter |
| Remove column | ⚠️ | Stop reading first → deploy → migrate |
| Rename column | ❌ | Add new → copy → deploy → remove old |
| Add index | ✅ | CONCURRENTLY if available |

## CI/CD Pipeline

```
Lint → Test → Build → Security audit → Deploy staging → Deploy prod → Health check
```

Rules: Never deploy without passing tests. Pin versions (no `latest`). Use build artifacts. Pipeline < 10 min. Scan dependencies.

## Docker

Use specific base versions. Multi-stage builds. Rarely-changing layers first. Non-root user. HEALTHCHECK. `.dockerignore`. No secrets in layers. Small images.

## Laravel Deploy

```bash
composer install --no-dev --optimize-autoloader
php artisan config:cache && route:cache && view:cache && event:cache
php artisan migrate --force
php artisan queue:restart
```
Config: `APP_DEBUG=false`, correct `APP_URL`, Redis session/cache/queue (not file for multi-server), daily log rotation.

## Node.js Deploy

```bash
npm ci --production && npm run build
pm2 start ecosystem.config.js --env production
```
Config: `NODE_ENV=production`, process manager for restart, cluster mode, memory limits, graceful shutdown, health endpoint.

## Rollback

**Symlink**: `ln -sfn /releases/previous /current` → reload app server → restart workers.
**Database**: Only if safely reversible. Prefer forward-fix over rollback.
**Rules**: Test rollback before needed. Keep artifacts. Document reversible migrations. Have communication plan.

## Monitoring Thresholds

| Metric | ⚠️ Warning | 🔴 Critical |
|--------|-----------|------------|
| Error rate | > 1% | > 5% |
| Response p95 | > 1s | > 3s |
| CPU | > 70% | > 90% |
| Memory | > 80% | > 95% |
| Disk | > 75% | > 90% |
| Queue depth | > 1K | > 10K |
| Failed jobs | > 10/hr | > 100/hr |

Alert rules: Alert on symptoms not causes. Every alert must be actionable. Include runbook links. Review monthly.

## Incident Response

Acknowledge → Assess scope → Communicate → Mitigate (rollback/flag/scale) → Fix → Verify → Post-mortem

## Output Format

```
# Deployment Review
## Risk Assessment — readiness score, critical gaps
## Required Fixes — blocking safe deploy
## Improvements — important but non-blocking
## Deploy Steps — numbered, copy-paste-ready
## Rollback Steps — numbered, copy-paste-ready
## Verification Commands — post-deploy checks
## Monitoring Gaps — missing alerting
```
