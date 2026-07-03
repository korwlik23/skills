---
name: migration-upgrade
description: >
  Use this skill when upgrading framework versions, updating dependencies,
  migrating tech stacks, handling breaking changes, performing data migrations,
  or planning version transitions. Triggers on requests about upgrading,
  updating packages, handling deprecations, breaking changes, migration
  planning, or switching technologies.
---

# Migration & Upgrade Skill

Use this skill when upgrading framework versions, updating dependencies, migrating tech stacks, handling breaking changes, performing data migrations, or planning version transitions.

## Production-Grade Operating Contract

- Before starting, read `../../../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, preserve compatibility where possible, require rollback plans for migrations/upgrades, avoid destructive actions without explicit confirmation, and report only verified results.
- Use this skill for migration technical depth; do not let it override user instructions, repository guidance, or data-integrity constraints.
- Keep responses proportional. Use the output format for migration plans/reviews; use a concise summary for small dependency updates.

## Core Principles

1. Never upgrade blindly — read changelogs, breaking changes, and migration guides first.
2. Upgrade incrementally — one major version at a time, verify at each step.
3. Test before and after — know what works now to verify it still works after.
4. Have a rollback plan — every upgrade must be reversible.
5. Don't mix upgrades with feature work — one concern per PR/commit.

## Upgrade Process

### Phase 1: Assessment

Before touching anything:

1. **Current state audit**
   - Current framework/library versions.
   - Current dependency tree (`npm ls`, `composer show`).
   - Current test coverage and pass rate.
   - Known deprecation warnings.
   - Custom patches or workarounds in place.

2. **Target state research**
   - Read the official migration guide (ALWAYS the first step).
   - Read the full changelog between current and target version.
   - Identify all breaking changes.
   - Identify deprecated features you're using.
   - Check community reports of upgrade issues (GitHub issues, forums).
   - Check compatibility of all major dependencies with target version.

3. **Risk assessment**

| Risk Factor | Low | Medium | High |
|-------------|-----|--------|------|
| Version gap | 1 minor | 1 major | 2+ major |
| Breaking changes | 0-2 | 3-10 | 10+ |
| Test coverage | > 80% | 40-80% | < 40% |
| Custom patches | None | Few | Many |
| Dependency conflicts | None | Some | Many |
| Data migration | None | Simple | Complex |

### Phase 2: Planning

Create a migration plan:

```markdown
## Upgrade Plan: [Library] v[current] → v[target]

### Prerequisites
- [ ] Backup database
- [ ] Tag current release
- [ ] All tests passing on current version
- [ ] CI/CD pipeline verified

### Steps
1. [ ] Update config/settings for new version
2. [ ] Update dependency version
3. [ ] Fix breaking changes (list each one)
4. [ ] Replace deprecated features
5. [ ] Update related dependencies
6. [ ] Run tests — fix failures
7. [ ] Run static analysis — fix issues
8. [ ] Test in staging
9. [ ] Deploy to production
10. [ ] Monitor for issues

### Rollback Plan
Steps to revert if upgrade fails.

### Timeline
Estimated time for each phase.
```

### Phase 3: Execution

#### Pre-Upgrade Checklist

- [ ] Create a dedicated branch for the upgrade.
- [ ] Backup database (production and staging).
- [ ] Tag the current release for easy rollback.
- [ ] Verify all tests pass on current version.
- [ ] Document current behavior of critical flows.
- [ ] Snapshot current dependency versions (`package-lock.json`, `composer.lock`).

#### Upgrade Order

```
1. Framework core FIRST (Laravel, Next.js, Svelte)
2. Framework official plugins/packages
3. Third-party dependencies (check compatibility)
4. Dev dependencies (testing, linting, building)
5. Custom code changes for breaking APIs
6. Configuration file updates
7. Database migrations (if required)
```

#### During Upgrade

- Update one dependency at a time when possible.
- Run tests after each significant change.
- Commit frequently with descriptive messages.
- Keep notes of every issue encountered and how it was resolved.
- If stuck for > 30 minutes on one issue, note it and move on — come back later.

### Phase 4: Verification

Post-upgrade checklist:

- [ ] All unit tests pass.
- [ ] All integration/feature tests pass.
- [ ] All E2E tests pass.
- [ ] Manual smoke test of critical flows.
- [ ] No new deprecation warnings (unless planned).
- [ ] Build succeeds in production mode.
- [ ] Performance benchmarks within acceptable range.
- [ ] No new console errors or warnings.
- [ ] Staging environment deployed and tested.

## Framework-Specific Upgrade Guides

Per-framework upgrade checklists and common breaking-change areas (Laravel, Next.js,
SvelteKit, Node.js) are in `references/framework-upgrade-guides.md` — load it when
upgrading one of those stacks. They are version-agnostic: per `../../../RULES.md` §10,
always read the framework's official upgrade guide for the *actual* source and target
versions before acting. The framework-agnostic upgrade process above is the source of
truth.

## Dependency Management

### Routine Update Strategy

| Frequency | What | How |
|-----------|------|-----|
| Weekly | Security patches | `npm audit fix` / `composer audit` |
| Monthly | Minor versions | Update, test, deploy |
| Quarterly | Major versions | Plan, assess breaking changes, upgrade |
| Yearly | Framework major | Dedicated upgrade sprint |

### Handling Dependency Conflicts

```
1. Identify the conflict (which packages need incompatible versions)
2. Check if newer versions of conflicting packages resolve it
3. Check for alternative packages if one is unmaintained
4. As last resort, use resolution overrides (package.json resolutions)
5. Document any forced resolutions with reason and review date
```

### Dependency Health Check

| Signal | Risk | Action |
|--------|------|--------|
| Last publish > 2 years | High | Find alternative |
| Open security advisory | Critical | Update immediately |
| Deprecated package | High | Plan migration |
| < 100 weekly downloads | Medium | Evaluate alternatives |
| No TypeScript types | Low | Add @types or consider alternative |
| Many open issues | Medium | Check if actively triaged |

## Data Migration

When an upgrade forces schema or data changes (ORM/framework changes, column type
changes, data reshaping), the migration-safety matrix, the higher-risk data-migration
table (change format / merge-split / move database), and the universal rules are the
pack-wide canonical source: **`../database-performance/references/migration-safety.md`** —
use it, do not restate it here.

Upgrade-context additions on top of that:

- Run forced data migrations **after** the dependency/framework upgrade is verified in
  a non-prod environment, never blindly as part of the same step.
- If the upgrade's own changelog prescribes a migration path, that path overrides the
  generic strategy — follow the official guide (per `../../../RULES.md` §10).

## Tech Stack Migration

### Migration Pattern: Strangler Fig

```
Phase 1: New system handles new features
Phase 2: Gradually migrate existing features
Phase 3: Old system handles only legacy features
Phase 4: Complete migration, decommission old system
```

### Migration Checklist

- [ ] New stack handles all current features?
- [ ] Data migration plan tested?
- [ ] Both systems can coexist during transition?
- [ ] Team trained on new stack?
- [ ] Monitoring for both systems?
- [ ] Rollback plan if new stack has critical issues?
- [ ] Timeline and milestones defined?
- [ ] User communication plan?

## Breaking Change Management

### How to Handle Breaking Changes

| Type | Strategy |
|------|----------|
| Removed method/class | Find replacement in migration guide |
| Changed method signature | Update all call sites |
| Changed default behavior | Explicitly set the old default or adapt |
| Removed config option | Find replacement config |
| Changed data format | Write transformer/adapter |
| New required dependency | Install and configure |

### Communication Template

```markdown
## Breaking Change: [Description]

**What changed**: Brief description of the change.
**Why it changed**: Reason for the breaking change.
**What to do**: Step-by-step migration instructions.
**Timeline**: When this change takes effect.
**Impact**: Who/what is affected.
**Rollback**: How to revert if needed.
```

## L5 Acceptance Gates

- Current and target versions are identified with official migration/changelog references where available.
- Breaking changes are mapped to affected files, public contracts, data, deployment, and tests.
- Upgrade path is incremental unless a single-step upgrade is demonstrably safer.
- Rollback or forward-fix plan exists for code, schema, data, dependencies, and deployment.
- Validation includes build/typecheck/tests plus targeted runtime checks for changed behavior.

## Output Format

```markdown
# Migration Report

## Current State
Current versions, test status, known issues.

## Target State
Target versions, expected improvements.

## Breaking Changes Identified
For each:
- Change description
- Impact on our codebase
- Required code changes
- Effort estimate

## Migration Plan
Numbered steps with checkpoints.

## Risk Assessment
| Risk | Likelihood | Impact | Mitigation |

## Rollback Plan
Steps to revert if migration fails.

## Verification
- [ ] All tests pass
- [ ] Build succeeds
- [ ] Critical flows verified
- [ ] Performance acceptable
- [ ] No new deprecation warnings

## Post-Migration Tasks
Cleanup, documentation updates, monitoring.
```

## Example Trigger Phrases

- "Upgrade Laravel to the latest version"
- "Update Next.js from 14 to 15"
- "How do I handle this breaking change?"
- "Migrate from JavaScript to TypeScript"
- "Update all dependencies"
- "Plan the database migration"
- "What changed between these versions?"
- "Is it safe to upgrade this package?"

## Usage Limitations

- Do not upgrade without reading the official changelog and migration guide first.
- Do not mix upgrades with feature work in the same change.
- Do not skip rollback planning for any migration.
- Do not test migrations against dev-size data only — consider production data volume.
- Do not force-resolve dependency conflicts without documenting the reason and review date.
