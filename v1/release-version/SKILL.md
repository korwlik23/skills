---
name: release-version
description: Principal release versioning — SemVer management, changelog, tagging, release notes, version bumping.
---

# Release Version

## Goal

Manage project versioning with precision — ensure every release is properly versioned, documented, tagged, and communicated. Maintain a clear history of what changed, when, and why.

## Core Rules

1. **SemVer is law** — follow Semantic Versioning 2.0.0 strictly. No exceptions.
2. **Every release tells a story** — changelog must be human-readable and complete.
3. **Tags are immutable** — once tagged, never rewrite. Use new patch/revision if needed.
4. **Automate what you can** — version bumping, changelog generation, tag creation.
5. **Release notes ≠ changelog** — release notes are user-facing summaries; changelog is developer-facing detail.
6. **No version without validation** — build + test must pass before any version bump.

## Safe Operating Constraints

**Do**: Bump versions, update changelogs, create tags, generate release notes, update version references across files.

**Don't**: Delete or overwrite existing tags. Force-push version changes to shared branches. Skip validation before release. Publish to registries without explicit user confirmation. Modify past changelog entries (append corrections instead).

**Escalate when**: Breaking change detected (confirm MAJOR bump). Multiple packages need coordinated release. Pre-release versioning strategy unclear. Rollback of published version needed. Version conflicts between dependencies.

## When to Trigger

### Auto-Trigger

- User says "release", "bump version", "new version", "publish"
- After completing a milestone or sprint worth of changes
- Hotfix merged to main/production branch

### Manual Trigger

- Version planning and strategy discussion
- Release retrospective or audit
- Setting up release automation

## Semantic Versioning

### Version Format

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]

Examples:
  1.0.0          # Stable release
  1.2.3          # Patch release
  2.0.0-alpha.1  # Pre-release alpha
  2.0.0-beta.3   # Pre-release beta
  2.0.0-rc.1     # Release candidate
  1.2.3+build.456 # Build metadata (ignored in precedence)
```

### When to Bump

| Change Type | Bump | Examples |
|-------------|------|----------|
| Breaking API/behavior change | **MAJOR** | Remove endpoint, rename public API, change response format, drop support |
| New feature (backward-compatible) | **MINOR** | New endpoint, new UI page, new config option, new integration |
| Bug fix (backward-compatible) | **PATCH** | Fix crash, correct calculation, fix typo in output, security patch |
| No public-facing change | **None** | Refactor internals, update dev deps, improve tests, update docs |

### Pre-release Strategy

```
Development Flow:
  alpha → internal testing, API may change freely
  beta  → feature-complete, API stable, bugs expected
  rc    → release candidate, production-ready unless blocker found

Versioning:
  2.0.0-alpha.1 → 2.0.0-alpha.2 → ... → 2.0.0-beta.1 → ... → 2.0.0-rc.1 → 2.0.0
```

## Process

### Phase 1: Pre-Release Audit

Before any version bump:

1. **Validate build** — `npm run build` / equivalent must pass
2. **Run all tests** — unit, integration, e2e must pass
3. **Check lint** — no lint errors
4. **Review changes since last release** — `git log [last-tag]..HEAD --oneline`
5. **Classify changes** — determine MAJOR/MINOR/PATCH based on changes
6. **Check for breaking changes** — search for `BREAKING CHANGE`, removed APIs, changed signatures
7. **Check dependency updates** — any security advisories, breaking dep updates?
8. **Verify PROJECT_SITEMAP.md** — ensure sitemap is current (if using project-sitemap skill)

### Phase 2: Version Bump

Update version in all relevant files:

| File Type | Location | Example |
|-----------|----------|---------|
| **package.json** | `version` field | Node.js projects |
| **composer.json** | `version` field | PHP/Laravel projects |
| **pyproject.toml** | `[project] version` | Python projects |
| **Cargo.toml** | `[package] version` | Rust projects |
| **build.gradle** | `version` property | Java/Kotlin projects |
| **pubspec.yaml** | `version` field | Flutter/Dart projects |
| **mix.exs** | `@version` | Elixir projects |
| **App config** | Version constants | Any framework |
| **Docker** | Image tags | Dockerfile, compose |
| **README** | Version badges, install commands | All projects |
| **API docs** | Version header | OpenAPI/Swagger |

**Multi-file sync**: Search all files referencing the old version and update consistently.

```bash
# Find all version references
grep -rn "1\.2\.3" --include="*.json" --include="*.toml" --include="*.yaml" --include="*.md"
```

### Phase 3: Changelog

#### Format (Keep a Changelog)

```markdown
# Changelog

All notable changes to this project will be documented in this file.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [1.2.0] - 2024-03-15

### Added
- User profile page with avatar upload (#45)
- Email notification preferences (#52)

### Changed
- Dashboard layout to responsive grid (#48)
- API rate limit increased from 100 to 500 req/min (#50)

### Fixed
- Login redirect loop on expired session (#47)
- CSV export encoding issue for non-ASCII characters (#51)

### Security
- Upgraded bcrypt to v5.1 to address CVE-2024-xxxx (#53)

### Deprecated
- Legacy `/api/v1/users` endpoint (use `/api/v2/users`) (#49)

### Removed
- Support for Node.js 16 (EOL) (#46)

## [1.1.0] - 2024-02-01
...

[Unreleased]: https://github.com/user/repo/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/user/repo/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/user/repo/compare/v1.0.0...v1.1.0
```

#### Changelog Categories

| Category | When to Use |
|----------|-------------|
| **Added** | New features, new files, new endpoints |
| **Changed** | Modifications to existing functionality |
| **Deprecated** | Features marked for future removal |
| **Removed** | Features removed in this release |
| **Fixed** | Bug fixes |
| **Security** | Vulnerability fixes, security improvements |

#### Writing Rules

- Write from user's perspective ("Add user search" not "Implement ElasticSearch indexer")
- Include issue/PR numbers when available (#123)
- One line per change, be specific
- Most impactful changes first within each category
- Keep `[Unreleased]` section always present for ongoing work

### Phase 4: Git Tag & Release

```bash
# Commit version bump + changelog
git add -A
git commit -m "chore(release): v1.2.0"

# Create annotated tag
git tag -a v1.2.0 -m "Release v1.2.0 — [brief summary]"

# Push commit + tag
git push origin main
git push origin v1.2.0
```

### Phase 5: Release Notes

Generate user-facing release notes (different from changelog):

```markdown
# v1.2.0 — [Release Title]

## 🎯 Highlights
Brief summary of what this release brings (2-3 sentences max).

## ✨ New Features
- **User Profiles** — Users can now customize their profile with avatars and bios
- **Email Preferences** — Fine-grained control over notification emails

## 🐛 Bug Fixes
- Fixed login redirect loop affecting users with expired sessions
- Fixed CSV export for non-Latin characters

## ⚠️ Breaking Changes
(Only for MAJOR releases)
- Removed support for Node.js 16. Minimum required: Node.js 18

## 🔄 Migration Guide
(Only for MAJOR releases or when user action needed)
1. Update Node.js to v18+
2. Run `npm install` to update dependencies
3. Run `npx migrate-config` to update config format

## 📦 Upgrade
npm install package-name@1.2.0
# or
docker pull image-name:1.2.0

## Full Changelog
[v1.1.0...v1.2.0](https://github.com/user/repo/compare/v1.1.0...v1.2.0)
```

## Version Strategy by Project Type

| Project Type | Strategy | Notes |
|-------------|----------|-------|
| **SaaS/Web App** | Date-based or SemVer | Deploy continuously, version for communication |
| **Library/Package** | Strict SemVer | Public API contract matters |
| **API** | URL versioning + SemVer | `/api/v1/`, `/api/v2/` |
| **Mobile App** | SemVer + Build number | `1.2.0 (build 45)`, store requirements |
| **Monorepo** | Independent or locked | Per-package or unified versions |
| **CLI Tool** | Strict SemVer | Users depend on flags/output format |

## Monorepo Versioning

### Independent Versioning
Each package has its own version. Use when packages have different release cycles.

```
packages/
├── core/        # v2.1.0
├── cli/         # v1.5.0
└── ui/          # v3.0.0-beta.1
```

### Locked Versioning
All packages share the same version. Use when packages are tightly coupled.

```
packages/
├── core/        # v2.1.0
├── cli/         # v2.1.0
└── ui/          # v2.1.0
```

## Automation Setup

### Recommended Tools

| Tool | Purpose | Ecosystem |
|------|---------|-----------|
| `standard-version` | Bump + changelog + tag | Node.js |
| `semantic-release` | Fully automated releases | Node.js (CI) |
| `changesets` | Monorepo versioning | Node.js |
| `bump2version` | Version bumping | Python |
| `cargo-release` | Release workflow | Rust |
| `fastlane` | Mobile releases | iOS/Android |

### CI/CD Integration

```yaml
# GitHub Actions example
release:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - run: npm ci
    - run: npm test
    - run: npm run build
    - run: npx standard-version
    - run: git push --follow-tags origin main
```

## Rollback Protocol

| Situation | Action |
|-----------|--------|
| **Bug found post-release** | Patch release (1.2.1) with fix. Never delete tag. |
| **Critical vulnerability** | Immediate patch release + security advisory |
| **Wrong version published** | Publish new correct version. Deprecate wrong version if registry supports. |
| **Need to undo release** | `git revert` the release commit → new patch version |

**Never**: Delete published tags. Force-push over release commits. Reuse version numbers. Unpublish from registries (if avoidable).

## Cross-Skill Integration

### With project-sitemap
After version bump → update `PROJECT_SITEMAP.md` version field + Change Log entry.

### With git-workflow
Follow commit convention: `chore(release): v1.2.0`. Create release branch for MAJOR versions. Tag from main/release branch only.

### With project-documentation
Update README version badges, install commands, and API version references.

### With testing-qa
All tests must pass before version bump. Add version-specific regression tests for MAJOR releases.

## Error Recovery

| Failure | Protocol |
|---------|----------|
| Version bump missed files | Search all files for old version string, update, amend commit |
| Tag created on wrong commit | Delete local tag, create on correct commit, force-push tag (only if not yet pulled by others) |
| Changelog has errors | Add correction entry in next release, don't modify published changelog |
| Build fails after bump | Fix issue → new patch release. Don't revert version number. |
| Duplicate version number | If unpublished: delete tag + re-tag. If published: bump to next version. |

## Quality Checklist

- [ ] Build passes without errors?
- [ ] All tests pass (unit, integration, e2e)?
- [ ] Lint passes?
- [ ] Version bump is correct (MAJOR/MINOR/PATCH)?
- [ ] Version updated in ALL relevant files?
- [ ] Changelog is complete and accurate?
- [ ] Changelog follows Keep a Changelog format?
- [ ] No `[Unreleased]` changes left behind?
- [ ] Git tag matches version in files?
- [ ] Tag is annotated (not lightweight)?
- [ ] Release notes generated for user-facing changes?
- [ ] Breaking changes documented with migration guide?
- [ ] Previous version's deprecation warnings addressed?
- [ ] PROJECT_SITEMAP.md updated with new version?
- [ ] No secrets or sensitive data in changelog/notes?
- [ ] Compare link at bottom of changelog updated?

## Output Format

```
# Release Summary
## Version — [old] → [new] ([MAJOR/MINOR/PATCH])
## Reason — why this release
## Changes — categorized list (Added/Changed/Fixed/etc.)
## Files Updated — version bumped in [list]
## Tag — v[version] on commit [hash]
## Changelog — updated CHANGELOG.md
## Release Notes — generated/updated
## Validation — build ✅ tests ✅ lint ✅
## Breaking Changes — [list or "None"]
## Migration Required — [Yes/No + steps]
## Next Steps — deploy, notify, monitor
```
