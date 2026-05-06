---
name: git-workflow
description: Principal Git workflow — branching, commits, PRs, conflicts, releases, hooks.
---

# Git Workflow

## Core Rules

1. Commits tell a story — logical, self-contained changes.
2. Branches are cheap — use liberally, clean regularly.
3. Main is sacred — always deployable.
4. History matters — write for the person reading `git log` in 6 months.
5. Automate enforcement — hooks, CI checks, linters.

## Branching Strategy

| Project Type | Team | Strategy |
|-------------|------|----------|
| Solo/small | 1-2 | GitHub Flow |
| Versioned releases | 3-10 | Git Flow |
| Continuous deploy | Any | Trunk-Based |
| Open source | Any | Fork & PR |

**GitHub Flow (recommended)**: `main` always deployable. Feature branches from main. PR → review → merge. Deploy from main.

**Git Flow**: `main` (prod releases) + `develop` (integration). `feature/*` from develop. `release/*` for prep. `hotfix/*` from main.

**Trunk-Based**: All commit to main (or <1 day branches). Feature flags for incomplete features. Automated test gates.

## Branch Naming

```
<type>/<ticket>-<description>
feature/ABC-123-user-profile
bugfix/ABC-456-fix-login
hotfix/ABC-789-payment-crash
chore/update-deps
refactor/extract-auth-service
docs/update-readme
```

## Commit Convention (Conventional Commits)

```
<type>(<scope>): <subject>    ← imperative, <72 chars, no period
```

| Type | When |
|------|------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Docs only |
| `refactor` | No feature/fix change |
| `perf` | Performance |
| `test` | Tests |
| `chore` | Build, CI, deps |

Good: `feat(auth): add Google OAuth login`
Bad: `Added stuff` / `fix` / `updates`

Body: explain what+why (not how). Footer: `Closes #123`, `BREAKING CHANGE: ...`

## PR Workflow

### PR Checklist
- [ ] Branch up to date with target
- [ ] Tests pass locally
- [ ] Lint passes
- [ ] Build succeeds
- [ ] Self-reviewed diff (no debug code, no unrelated changes)
- [ ] Title follows commit convention
- [ ] Description explains what + why
- [ ] Screenshots for UI changes
- [ ] Breaking changes documented

### PR Template

```
## What — change description
## Why — problem solved or feature added
## How — key technical decisions
## Testing — how tested
## Screenshots — before/after for UI
```

### Review Rules
Review <24h. Approve if good enough (not perfect). Focus: correctness, security, performance, maintainability. Don't nitpick style covered by linters.

### Merge Strategy

| Strategy | When |
|----------|------|
| Squash merge | Feature branches (clean history) ← recommended |
| Merge commit | Long-running, preserve history |
| Rebase | Linear history desired |

## Conflict Resolution

**Prevent**: Short-lived branches (<3 days). Rebase main daily. Communicate overlapping work.

**Resolve**: `git fetch && git rebase origin/main` → understand BOTH changes → resolve → run tests → `git push --force-with-lease` (not `--force`).

Never blindly accept ours/theirs. Ask other author if unsure.

## Release Management

### SemVer

```
MAJOR.MINOR.PATCH
1.0.0 → 1.0.1 (patch: bug fix)
1.0.0 → 1.1.0 (minor: new feature, backward compat)
1.0.0 → 2.0.0 (major: breaking change)
Pre: -alpha.1 → -beta.1 → -rc.1 → stable
```

### Release Checklist
- [ ] All features merged
- [ ] Tests pass
- [ ] Version updated
- [ ] Changelog updated
- [ ] Tag: `git tag -a v1.0.0 -m "Release 1.0.0"` → push tag
- [ ] Staging verified
- [ ] Production deployed + monitored

### Changelog Format

```
## [1.1.0] - 2024-01-15
### Added — new features
### Changed — modifications
### Fixed — bug fixes
### Security — vulnerability fixes
```

## Git Hooks

| Hook | Purpose | Tool |
|------|---------|------|
| pre-commit | Lint staged files | lint-staged + husky |
| commit-msg | Validate message | commitlint |
| pre-push | Run tests | Custom script |

Setup: `npx husky init` → add hook scripts.

## Best Practices

**Do**: Commit often (on branches). Meaningful messages. Pull before push. Delete merged branches. Tag releases. Use .gitignore properly.

**Don't**: Force push shared branches. Commit secrets/.env. Commit node_modules/build. Rewrite published history. Branches >1 week. Mix unrelated changes.

## Emergency

```bash
# Undo last commit (not pushed)
git reset --soft HEAD~1     # keep staged
git reset --mixed HEAD~1    # keep unstaged
git reset --hard HEAD~1     # discard (DANGEROUS)

# Undo pushed commit (SAFE)
git revert <hash>

# Recover deleted branch
git reflog → git checkout -b recovered <hash>

# Fix wrong branch
git stash → git checkout correct-branch → git stash pop
```

## Output Format

```
# Git Workflow Review
## Current Assessment — strategy, commit quality, merge patterns
## Issues — inconsistencies, long branches, missing automation
## Recommended Workflow — strategy, naming, convention, merge
## Setup Steps — commands and configuration
## Automation — hooks, CI checks, tools
## Team Guidelines — concise rules for all devs
```
