---
name: project-documentation
description: >
  Use this skill when creating, updating, or reviewing project documentation
  including README, installation guides, architecture docs, API docs, usage
  guides, changelogs, runbooks, or contribution guidelines. Triggers on
  requests about docs, README, how-to guides, or any documentation need.
---

# Project Documentation Skill

Use this skill when the user asks to create, update, or review project documentation including README files, installation guides, system descriptions, feature lists, usage guides, API docs, changelogs, runbooks, or contribution guidelines.

## Production-Grade Operating Contract

- Before starting, read `../../../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, inspect the project before writing, avoid inventing commands or features, never include real secrets, validate claims where practical, and report any unverified documentation.
- Use this skill for documentation depth; do not let it override user instructions, repository guidance, or security/data-integrity constraints.
- Keep responses proportional. Use the output format for substantial documentation updates; use a concise summary for small edits.

## L5 Documentation Standard

Production-grade documentation is:

1. **Accurate** - reflects the current code, commands, configuration, and behavior.
2. **Operational** - a new contributor can install, run, test, and troubleshoot from it.
3. **Secure** - uses dummy secrets, redacts sensitive values, and warns about production-only settings.
4. **Navigable** - starts with the common path, then links to deeper details.
5. **Verifiable** - commands, links, diagrams, and examples are checked or clearly marked unverified.
6. **Maintainable** - avoids stale implementation trivia and points to source files where details change often.

## Progressive Disclosure

Keep this `SKILL.md` as the workflow and quality contract. Load `references/documentation-templates.md` only when you need concrete templates for README sections, API docs, `.env.example`, architecture diagrams, changelog entries, or verification checklists.

## Documentation Process

### Phase 1: Discover

Inspect before writing:

1. Project purpose and target users.
2. Runtime stack, framework versions, package managers, and system prerequisites.
3. Project structure, entry points, routes, commands, and background workers.
4. Configuration files, environment variables, feature flags, and secret boundaries.
5. Auth model, roles, permissions, external services, and data stores.
6. Build, test, lint, deploy, migration, and rollback commands.
7. Existing docs, comments, examples, screenshots, diagrams, and CI workflows.

### Phase 2: Choose Artifact Shape

- **README**: overview, quick start, install, config, run/test/deploy, architecture links, troubleshooting.
- **Installation guide**: prerequisites, environment setup, exact commands, expected results, common failures.
- **Architecture doc**: system diagram, module boundaries, key flows, data ownership, deployment shape.
- **API docs**: auth model, endpoint table, request/response examples, errors, pagination, rate limits.
- **Usage guide**: task-based workflows from the user's perspective.
- **Runbook**: alert, symptom, diagnosis, mitigation, rollback, escalation, post-incident notes.
- **Changelog/release notes**: user-visible changes, breaking changes, migrations, rollback notes.

### Phase 3: Write From Source

- Prefer facts discovered from code, config, tests, CI, and existing docs.
- Use placeholders only when the user explicitly asks for a template. Otherwise, resolve or omit unknowns.
- Mark uncertain content with a clear verification note instead of guessing.
- Keep examples realistic but sanitized.
- Link to relevant local files when helpful so future maintainers can verify details.

### Phase 4: Verify

Run or inspect what is relevant:

- Markdown renders cleanly.
- Commands are syntactically correct and, when practical, executed.
- Links point to real local files or valid external docs.
- Env examples contain dummy values and no secrets.
- Diagrams match the actual architecture at the level of detail claimed.
- Installation and test instructions match available package manager scripts.

## Content Rules

### README

- Lead with the project name and a one-sentence description of what it does and who it is for.
- Include badges only when they correspond to real systems.
- Put the fastest successful path near the top.
- Document prerequisites with explicit minimum versions.
- Separate required setup from optional integrations.
- Include a project structure section only for directories users need to understand.
- Include screenshots or diagrams for visual or complex systems when assets exist or the user requests them.

### Environment Variables

- Group variables by purpose.
- Include description, example, required/optional status, and security notes.
- Use dummy values. Never paste real tokens, passwords, keys, cookies, or production URLs unless already public and intentionally documented.
- State generation requirements for secrets, such as minimum length or command to generate a safe value.

### API Documentation

- Include method, path, purpose, auth requirement, permissions, request body, query params, response shape, error format, pagination, and rate limits where applicable.
- Examples must be internally consistent and avoid exposing full database records or sensitive fields.

### Architecture Documentation

- Describe responsibilities and boundaries, not every implementation detail.
- Use diagrams for system-level flows when they reduce ambiguity.
- Call out data ownership, asynchronous work, external dependencies, and failure modes.

### Troubleshooting

- List symptoms, likely causes, diagnostic commands, and safe recovery steps.
- Avoid instructions that modify production data or infrastructure without confirmation.

## L5 Acceptance Gates

- A new contributor can follow the docs without hidden project knowledge.
- Public commands, env vars, routes, and examples match the current repo.
- Sensitive data is absent and secret-generation guidance is safe.
- Complex workflows include expected outcomes and failure recovery.
- Verification status is explicit: tested, inspected, or not verified.
- Large reusable examples live in `references/`, not in `SKILL.md`.

## Output Format

When creating or updating documentation:

```markdown
# Documentation Update

## Changes Made
What was added, updated, or removed.

## Files Modified
List changed files with a short purpose for each.

## Verification
Commands/checks run and their results. If not run, explain why.

## Risks
Unverified commands, stale upstream docs, missing screenshots, or production-specific gaps.

## Remaining Documentation Needs
Areas that still need documentation or user-provided facts.
```

## Example Trigger Phrases

- "Create a README for this project"
- "Document the API endpoints"
- "Write installation guide"
- "Update the architecture docs"
- "Generate changelog"
- "Create a runbook for this service"
- "Document environment variables"
- "Write contribution guidelines"

## Usage Limitations

- Do not invent commands, features, or configurations — document only what exists in the codebase.
- Do not include real secrets, tokens, or production URLs in documentation.
- Do not use placeholder content unless the user explicitly asks for a template.
- Do not skip verification of commands and links when practical.
- Do not assume project purpose or setup steps without inspecting the actual codebase.
