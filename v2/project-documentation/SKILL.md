---
name: project-documentation
description: Principal documentation — README, installation, architecture, features, usage, API docs.
---

# Project Documentation

## Core Rules

1. Docs are the first impression — determines if someone uses or abandons the project.
2. Write for the reader — assume they know nothing about your project.
3. Show don't tell — code examples, screenshots, diagrams > paragraphs.
4. Keep current — outdated docs mislead. Update with every feature change.
5. Progressive disclosure — overview first, details deeper.

## Process

### Phase 1: Discover

Investigate before writing:

1. **Purpose** — what problem, who it's for
2. **Stack** — framework, DB, cache, queue, frontend, hosting (with versions)
3. **Structure** — directory layout, modules, feature areas
4. **Entry points** — routes, pages, API endpoints, CLI
5. **Config** — env vars, config files, feature flags
6. **Dependencies** — runtime, dev, system requirements, external services
7. **Data flow** — request lifecycle, state management
8. **Auth** — system, providers, roles, permissions
9. **Features** — core functionality, integrations, automations
10. **Build/Deploy** — commands, targets, CI/CD

### Phase 2: Choose Structure

**Web Apps**: Name + screenshot → Description → Features → Tech Stack → Prerequisites → Installation → Env Vars → Running → Project Structure → Architecture → API Docs → Testing → Deployment → Contributing → License

**Libraries**: Name + badges → Description → Features → Install → Quick Start → API Reference → Config → Examples → Contributing → License

**CLI Tools**: Name + badges → Description → Features → Install → Usage/Commands → Config → Examples → Troubleshooting → Contributing → License

### Phase 3: Write Content

## Section Rules

### Header
Project name. One-line description (<20 words answering "what is this?"). Badges (build, version, license — only if real). Screenshot or demo GIF for visual projects.

### Features
Most impressive first. Each: `✅ **Name** — one sentence of user value`. Use ✅/🚧/📋 for done/in-progress/planned. Group by category if >10. Benefits, not implementation.

### Tech Stack
Table format: Layer | Technology (with versions). Only meaningful technologies.

### Prerequisites
Explicit minimum versions. Download links. Note which are optional. Mention Docker alternative.

### Installation
Numbered steps, sequential. Every command copy-paste-ready. Env vars in table (Variable | Description | Example). Show expected result of each step. Separate required from optional. Provide one-command option if possible (docker-compose, make setup).

### Project Structure
2-3 levels deep max. One-line comment per directory. Only directories readers interact with. Omit obvious (node_modules, .git).

### Architecture
Mermaid diagram for system overview. Document 2-3 key flows. Include external services. High-level, not every detail.

### API Docs
Table: Method | Endpoint | Description | Auth. Auth requirements per endpoint. Real curl examples. Realistic response examples. Document error formats.

### Usage Guide
Step-by-step numbered lists. `<details>` for collapsible FAQ. Screenshots for complex UI. Cover common tasks first. User perspective ("You can..." not "The system...").

### Testing & Deployment
Copy-paste commands only. Docker + manual options.

## Writing Style

**Do**: Active voice ("Run this command"). Second person ("You can"). Specific versions ("Node.js 18+"). Include expected output. Consistent formatting. Update with changes.

**Don't**: Unexplained jargon. Assume project knowledge. Leave TODOs/placeholders. Walls of text. Implementation details that change. Real secrets in examples.

## Env Var Documentation

Group by category. Inline comments. Realistic examples. Mark optional. Include requirements (min length, format).

```env
# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/db  # PostgreSQL connection
# Auth
JWT_SECRET=change-this-in-production  # JWT signing key (min 32 chars)
# GOOGLE_CLIENT_ID=                   # Optional: Google OAuth
```

## Quality Checklist

- [ ] New developer can set up from scratch using only README?
- [ ] All commands copy-paste-ready and tested?
- [ ] Env vars documented with descriptions + examples?
- [ ] Screenshots/diagrams for visual projects?
- [ ] Feature list current and accurate?
- [ ] Prerequisites listed with versions?
- [ ] Structure explained clearly?
- [ ] Common tasks have step-by-step guides?
- [ ] No placeholder text (TODO, TBD)?
- [ ] No sensitive data in examples?
- [ ] Renders correctly on GitHub?

## Output Format

```
# Documentation Update
## Changes — added, updated, removed
## Files — README.md, .env.example, docs/
## Verification — install tested, commands work, links valid, renders OK, no secrets
## Remaining — areas needing documentation
```
