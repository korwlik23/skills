---
name: git-workflow
Mode: git-workflow
description: Principal-level Git workflow skill for branching strategy, commit conventions, PR workflow, conflict resolution, release management, monorepo patterns, and version control best practices.
---

# Git Workflow Skill

Use this skill for Git branching strategy, commit messages, PR workflow, merge conflict resolution, release management, changelog generation, and version control best practices.

## Production-Grade Operating Contract

- Before starting, read `../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, inspect repository state before Git changes, never discard work without explicit confirmation, and report exactly what changed.
- Use this skill for Git technical depth; do not let it override user instructions, repository guidance, or destructive-operation safety rules.
- Keep responses proportional. Use the output format for workflow reviews/plans; use a concise summary for small Git tasks.

## Core Principles

1. Commits tell a story — each commit should be a logical, self-contained change.
2. Branches are cheap — use them liberally, clean them up regularly.
3. Main branch is sacred — it should always be deployable.
4. History matters — write for the person reading `git log` in 6 months.
5. Automate what you can — hooks, CI checks, changelog generation.

## Branching Strategies

### Strategy Selection Guide

| Project Type | Team Size | Recommended Strategy |
|-------------|-----------|---------------------|
| Solo / small project | 1-2 | GitHub Flow |
| Product with releases | 3-10 | Git Flow (simplified) |
| Continuous deployment | Any | Trunk-Based Development |
| Open source | Any | Fork & PR |
| Monorepo | Large | Trunk-Based + Feature Flags |

### GitHub Flow (Recommended for Most Projects)

```
main ──────●──────●──────●──────●──────●──────
            \          /         \    /
  feature/x  ●──●──●──●          ●──●
                                feature/y
```

Rules:
- `main` is always deployable.
- Create feature branches from `main`.
- Open PR when ready for review.
- Merge to `main` after approval.
- Deploy from `main`.

### Git Flow (For Versioned Releases)

```
main     ──●────────────────●──────────────●──
            \              / \            /
develop  ────●──●──●──●──●────●──●──●──●──
               \     /          \  /
feature/x       ●──●        hotfix/y
```

Branches:
- `main` — production releases only.
- `develop` — integration branch.
- `feature/*` — new features from develop.
- `release/*` — release preparation.
- `hotfix/*` — emergency production fixes from main.

### Trunk-Based Development

```
main ──●──●──●──●──●──●──●──●──●──●──
        \/ \/ 
   short-lived branches (< 1 day)
```

Rules:
- All developers commit to `main` (or very short-lived branches).
- Feature flags for incomplete features.
- Automated tests gate every merge.
- Deploy multiple times per day.

## Branch Naming Convention

```
Format: <type>/<ticket-id>-<short-description>

Examples:
  feature/ABC-123-user-profile
  bugfix/ABC-456-fix-login-error
  hotfix/ABC-789-payment-crash
  chore/update-dependencies
  refactor/extract-auth-service
  docs/update-readme
```

| Prefix | Use When |
|--------|----------|
| `feature/` | New feature or enhancement |
| `bugfix/` | Non-critical bug fix |
| `hotfix/` | Critical production fix |
| `chore/` | Maintenance, deps, tooling |
| `refactor/` | Code restructuring |
| `docs/` | Documentation only |
| `test/` | Adding/fixing tests |
| `experiment/` | Spike, prototype, exploration |

## Commit Message Convention

### Conventional Commits Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

| Type | When |
|------|------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code change, no feature/fix |
| `perf` | Performance improvement |
| `test` | Adding/fixing tests |
| `chore` | Build, CI, deps, tooling |
| `revert` | Reverting a previous commit |

### Rules

1. **Subject line**: Imperative mood, < 72 chars, no period.
   - ✅ `feat(auth): add Google OAuth login`
   - ❌ `Added Google OAuth login.`
   - ❌ `feat: stuff`

2. **Body** (optional): Explain *what* and *why*, not *how*. Wrap at 80 chars.

3. **Footer** (optional): Reference issues, breaking changes.
   - `Closes #123`
   - `BREAKING CHANGE: removed legacy auth endpoint`

### Examples

```
feat(auth): add Google OAuth login

Implement Google OAuth 2.0 as an additional login provider.
Users can now sign in with their Google account alongside
email/password authentication.

Closes #123

---

fix(orders): prevent duplicate order submission

Race condition allowed double-clicking submit to create
two orders. Added debounce + server-side idempotency key.

Fixes #456

---

chore(deps): update Next.js from 14.1 to 14.2

Minor version update with bug fixes and performance
improvements. No breaking changes.
```

## Pull Request Workflow

### PR Creation Checklist

- [ ] Branch is up to date with target branch.
- [ ] All tests pass locally.
- [ ] Linting passes.
- [ ] Build succeeds.
- [ ] Self-reviewed the diff — no debug code, no unrelated changes.
- [ ] PR title follows commit convention.
- [ ] PR description explains what and why.
- [ ] Screenshots/recordings for UI changes.
- [ ] Breaking changes documented.
- [ ] Related issues linked.

### PR Description Template

```markdown
## What
Brief description of the change.

## Why
Problem this solves or feature this adds.

## How
Key technical decisions and approach.

## Testing
How this was tested. Include test commands.

## Screenshots
Before/after for UI changes.

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Self-reviewed
```

### PR Review Rules

1. Review within 24 hours — don't block teammates.
2. Approve if it's good enough, not perfect — perfect is the enemy of shipped.
3. Use conventional review signals:
   - ✅ **Approve** — Ship it.
   - 💬 **Comment** — Non-blocking feedback.
   - 🔄 **Request Changes** — Must fix before merge.
4. Focus on:
   - Correctness — Does it do what it claims?
   - Security — Any new attack surface?
   - Performance — Any obvious bottlenecks?
   - Maintainability — Will someone understand this in 6 months?
5. Don't focus on:
   - Style preferences already covered by linters.
   - Unrelated code in the same file.
   - Theoretical problems that are unlikely.

### Merge Strategy

| Strategy | When | Result |
|----------|------|--------|
| **Squash merge** | Feature branches, messy commits | Clean single commit on main |
| **Merge commit** | Long-running branches, preserved history | Merge commit + all commits |
| **Rebase** | Clean linear history desired | Linear history, no merge commits |
| **Fast-forward** | Up-to-date branch, single commit | No merge commit |

Recommendation: **Squash merge** for feature branches → clean `main` history.

## Conflict Resolution

### Prevention

- Keep branches short-lived (< 3 days ideal).
- Rebase/merge main into feature branch daily.
- Communicate with team about overlapping work.
- Use `CODEOWNERS` to identify file ownership.

### Resolution Process

```
1. git fetch origin
2. git rebase origin/main (or merge)
3. For each conflict:
   a. Understand BOTH changes (yours and theirs)
   b. Decide which to keep (or combine both)
   c. Verify the resolution makes logical sense
   d. Run tests after resolving
4. git rebase --continue (or commit merge)
5. Force push only to your own feature branch after checking branch ownership: git push --force-with-lease
```

### Resolution Rules

- **Never blindly accept "ours" or "theirs"** — understand both changes.
- **If unsure, ask the other author** — don't guess at intent.
- **Run tests after resolving** — conflicts can introduce subtle bugs.
- **Use `--force-with-lease`** not `--force` — prevents overwriting others' work.

## Release Management

### Semantic Versioning (SemVer)

```
MAJOR.MINOR.PATCH

1.0.0 → 1.0.1  (patch: bug fix, no API change)
1.0.0 → 1.1.0  (minor: new feature, backward compatible)
1.0.0 → 2.0.0  (major: breaking change)
```

### Pre-release Versions

```
1.0.0-alpha.1  → Internal testing
1.0.0-beta.1   → External testing
1.0.0-rc.1     → Release candidate
1.0.0          → Stable release
```

### Release Checklist

- [ ] All features for this release are merged.
- [ ] All tests pass.
- [ ] Version number updated in package files.
- [ ] Changelog updated.
- [ ] Release notes written.
- [ ] Tag created: `git tag -a v1.0.0 -m "Release 1.0.0"`
- [ ] Tag pushed: `git push origin v1.0.0`
- [ ] Build artifact created.
- [ ] Deployed to staging and verified.
- [ ] Deployed to production.
- [ ] Monitored for issues post-deploy.

### Changelog Format

```markdown
# Changelog

## [1.1.0] - 2024-01-15

### Added
- User profile page with avatar upload
- Export data as CSV

### Changed
- Improved dashboard loading speed by 40%
- Updated dependencies

### Fixed
- Login redirect loop on expired session
- Order total calculation rounding error

### Security
- Fixed XSS vulnerability in comment field
```

## Git Hooks

### Recommended Hooks

| Hook | Purpose | Tool |
|------|---------|------|
| `pre-commit` | Lint staged files | lint-staged + husky |
| `commit-msg` | Validate commit message | commitlint |
| `pre-push` | Run tests before push | Custom script |

### Setup with Husky (Node.js)

```bash
npx husky init
echo "npx lint-staged" > .husky/pre-commit
echo "npx commitlint --edit \$1" > .husky/commit-msg
```

### lint-staged Configuration

```json
{
  "*.{js,ts,jsx,tsx}": ["eslint --fix", "prettier --write"],
  "*.{css,scss}": ["prettier --write"],
  "*.md": ["prettier --write"]
}
```

## Git Best Practices

### Do

- Commit early, commit often (on feature branches).
- Write meaningful commit messages.
- Pull/rebase before pushing.
- Delete merged branches.
- Use `.gitignore` properly.
- Tag releases.
- Back up important branches.

### Don't

- Force push to shared branches (main, develop).
- Commit secrets, credentials, or `.env` files.
- Commit large binary files (use Git LFS).
- Commit generated files (node_modules, build output, .next).
- Rewrite published history.
- Create branches that live longer than 1 week without merging.
- Mix unrelated changes in one commit.

### .gitignore Essentials

```gitignore
# Dependencies
node_modules/
vendor/

# Build output
.next/
dist/
build/

# Environment
.env
.env.local
.env.production

# IDE
.idea/
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*

# Testing
coverage/

# Generated
*.lock  # Only if not using lockfile pinning
```

## Monorepo Patterns

### When to Use Monorepo

- Multiple related packages/apps sharing code.
- Team wants unified tooling and CI/CD.
- Frequent cross-package changes.

### Tools

| Tool | Ecosystem | Features |
|------|-----------|----------|
| Turborepo | Node.js | Build caching, parallel tasks |
| Nx | Node.js | Dependency graph, affected tests |
| pnpm workspaces | Node.js | Fast installs, workspace linking |
| Lerna | Node.js | Publishing, versioning |

### Monorepo Branch Rules

- Same branching strategy for the whole repo.
- Use path-based CODEOWNERS for review assignment.
- CI should only build/test affected packages.
- Independent versioning per package.

## Emergency Procedures

### Undo Last Commit (Not Pushed)

Before any command that discards history or working tree changes:

- Inspect `git status --short` and the target branch.
- Explain what will be lost or rewritten.
- Get explicit user confirmation for destructive options such as `git reset --hard`.
- Prefer non-destructive alternatives (`git revert`, `git reset --soft`, new branch backup) when they solve the problem.

```bash
git reset --soft HEAD~1     # Keep changes staged
git reset --mixed HEAD~1    # Keep changes unstaged
git reset --hard HEAD~1     # Discard changes (DANGEROUS)
```

### Undo Pushed Commit

```bash
git revert <commit-hash>    # Create new commit that undoes changes (SAFE)
```

### Recover Deleted Branch

```bash
git reflog                  # Find the commit hash
git checkout -b recovered-branch <hash>
```

### Fix Wrong Branch

```bash
git stash                   # Save current changes
git checkout correct-branch
git stash pop               # Apply changes on correct branch
```

## L5 Acceptance Gates

- Repository state is inspected before changing branches, history, tags, remotes, or working tree contents.
- Commands that rewrite history or discard changes require explicit confirmation and a recovery path.
- Shared branches are protected from force pushes and direct risky changes.
- PR/release guidance includes validation status, review ownership, and rollback/revert strategy.
- Final summaries distinguish committed, staged, unstaged, untracked, and unpushed work.

## Output Format

```markdown
# Git Workflow Review

## Current Workflow Assessment
Branching strategy, commit quality, merge patterns.

## Issues Found
- Inconsistent commit messages
- Long-lived branches
- Missing hooks/automation
- etc.

## Recommended Workflow
Strategy, branch naming, commit convention, merge strategy.

## Setup Steps
Commands and configuration to implement.

## Automation
Hooks, CI checks, and tools to enforce.

## Team Guidelines
Concise rules for all developers to follow.
```
