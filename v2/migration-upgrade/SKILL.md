---
name: migration-upgrade
description: Principal migration & upgrade — framework upgrades, dependencies, breaking changes, data migration.
---

# Migration & Upgrade

## Core Rules

1. Never upgrade blindly — read changelogs + migration guides first.
2. Upgrade incrementally — one major version at a time, verify each step.
3. Test before and after — know what works now, verify it works after.
4. Always have rollback plan.
5. Don't mix upgrades with feature work.

## Process

### Phase 1: Assess

**Audit current state**: versions, dependency tree, test coverage, deprecation warnings, custom patches.

**Research target**: Official migration guide (ALWAYS first). Full changelog. Breaking changes. Deprecated features you use. Community issues. Dependency compatibility.

**Risk matrix**:

| Factor | Low | Medium | High |
|--------|-----|--------|------|
| Version gap | 1 minor | 1 major | 2+ major |
| Breaking changes | 0-2 | 3-10 | 10+ |
| Test coverage | >80% | 40-80% | <40% |
| Custom patches | None | Few | Many |

### Phase 2: Plan

Pre-upgrade: backup DB, tag current release, verify tests pass, snapshot lock files.

Upgrade order: Framework core → official plugins → third-party deps → dev deps → custom code → config → database migrations.

### Phase 3: Execute

One dependency at a time. Test after each change. Commit frequently. Keep notes of issues + resolutions. If stuck >30min, note it and move on.

### Phase 4: Verify

- [ ] All unit/integration/E2E tests pass
- [ ] Manual smoke test critical flows
- [ ] No new deprecation warnings
- [ ] Production build succeeds
- [ ] Performance acceptable
- [ ] Staging deployed and tested

## Framework Upgrades

### Laravel (e.g., 10→11)

1. Read laravel.com/docs/[ver]/upgrade
2. Update composer.json → `composer update`
3. Fix: removed/renamed classes, changed signatures, config diffs (vs fresh install), middleware, routing, Eloquent
4. Clear all caches → run tests → `php artisan about`

### Next.js (e.g., 14→15)

1. Read nextjs.org/docs/upgrading
2. Run `npx @next/codemod upgrade`
3. Update next + react versions
4. Fix: App Router changes, Server Component defaults, API routes, middleware, config
5. `npm run build` → test all pages

### Svelte/Kit

1. Read svelte.dev migration guide
2. Run `npx svelte-migrate` if available
3. Fix: component API, stores, routing, load functions
4. Build and test

### Node.js Version

Check changelog → check dep compatibility → update .nvmrc + engines + CI + Docker → `npm ci && npm run build && npm test`

## Dependency Management

| Frequency | What | How |
|-----------|------|-----|
| Weekly | Security patches | `npm audit fix` |
| Monthly | Minor versions | Update + test |
| Quarterly | Major versions | Plan + assess breaking |
| Yearly | Framework major | Dedicated sprint |

**Health signals**: Last publish >2yr (find alternative), security advisory (update now), deprecated (plan migration), few downloads (evaluate alternatives).

**Conflicts**: Identify conflicting packages → check newer versions → find alternatives → use resolution overrides as last resort → document with review date.

## Data Migration

| Type | Risk | Strategy |
|------|------|----------|
| Add column | Low | Nullable → backfill → constrain |
| Rename column | Medium | Add new → copy → deploy → remove old |
| Change format | Medium | Script + test on prod-size data |
| Merge/split tables | High | Multi-step with backward compat |
| New database | Very High | Dual-write → verify → cutover |

Rules: Always backup. Test on prod-size data. Measure time (downtime?). Make idempotent. Validate after (counts, checksums). Keep old data during transition. Have rollback.

## Tech Stack Migration

Strangler Fig pattern: New system handles new features → gradually migrate existing → old handles only legacy → complete migration → decommission.

## Output Format

```
# Migration Report
## Current State — versions, tests, known issues
## Target State — versions, improvements
## Breaking Changes — per change: description, impact, code changes, effort
## Plan — numbered steps with checkpoints
## Risks — risk, likelihood, impact, mitigation
## Rollback — revert steps if migration fails
## Verification — tests, build, critical flows, performance
## Post-Migration — cleanup, docs, monitoring
```
