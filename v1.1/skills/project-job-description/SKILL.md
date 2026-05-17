---
name: project-job-description
description: >
  Use this skill to analyze a codebase and generate professional career
  documentation — resumes, portfolios, job descriptions, or skill assessments
  based on actual code evidence. Triggers on requests about "create resume
  from this project", "what skills does this codebase demonstrate",
  "write a job description", "build a portfolio from my code", summarize a
  project from code, write work experience from a repository, explain what was
  built in this project, convert a codebase into a JD, create a career
  highlight, or "look at the code and summarize what it does".
---

# Project Job Description Skill

Use this skill when the user wants to extract professional career documentation from a codebase — including resumes, portfolios, job descriptions, skill assessments, or interview preparation materials based on actual code evidence.

## Production-Grade Operating Contract

- Before starting, read `../../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, base all claims on evidence from the actual codebase, never fabricate skills or experience, and clearly separate demonstrated skills from inferred ones.
- Use this skill for career documentation depth; do not let it override user instructions, repository guidance, or privacy constraints.
- Keep responses proportional. Use the output format for full portfolio generation; use a concise summary for quick skill assessments.

## Core Principles

1. Evidence over claims — every skill listed must be traceable to actual code.
2. Quality over quantity — highlight depth and mastery, not just tool exposure.
3. Honesty — distinguish between "uses extensively" and "has one file using it."
4. Context matters — explain the scale, complexity, and impact of the work.
5. Privacy first — never expose proprietary business logic, secrets, or internal details.

## Evidence and Anti-Fabrication Rules

- Do not claim teamwork, leadership, revenue impact, cost reduction, production deployment, real users, or numeric outcomes unless the code, documentation, metrics, or user confirmation supports it.
- Technology claims must come from dependencies, imports, configuration, file structure, or code usage.
- Feature claims must come from routes, components, functions, services, schemas, tests, UI text, or documentation.
- Performance claims must come from implementation evidence such as caching, indexing, lazy loading, benchmark output, or optimization code.
- Security claims must come from authentication, authorization, validation, sanitization, encryption, secret handling, or related tests/configuration.
- Business impact claims must come from metrics, analytics, documented user stories, production notes, or explicit user confirmation.
- If evidence is ambiguous, use cautious language such as "appears to", "from the code structure", or "should be confirmed".
- Record evidence paths for important claims so the user can verify or edit the wording confidently.

## Process

### Phase 1: Codebase Analysis

Scan and identify:

1. **Tech stack** — languages, frameworks, libraries, tools, and versions.
2. **Architecture patterns** — MVC, microservices, monorepo, event-driven, etc.
3. **Code complexity** — project size, module count, depth of features.
4. **Quality indicators** — test coverage, CI/CD, linting, type safety, documentation.
5. **Domain expertise** — industry-specific patterns (e-commerce, SaaS, fintech, etc.).

### Phase 2: Skill Extraction

For each identified skill, classify:

| Evidence Level | Definition | How to Describe |
|---------------|-----------|-----------------|
| **Expert** | Core architecture decisions, extensive usage, advanced patterns | "Designed and built..." |
| **Proficient** | Multiple features, consistent quality, best practices | "Developed and maintained..." |
| **Familiar** | Some usage, basic patterns, configuration | "Worked with..." |
| **Exposure** | Minimal usage, single file or config | Do not include unless requested |

### Phase 3: Impact Assessment

For each significant feature or system, document:

- **What** — what was built or achieved.
- **How** — key technical decisions and patterns used.
- **Scale** — data volume, user count, performance characteristics (when visible).
- **Quality** — testing, security, monitoring practices demonstrated.

### Phase 4: Generate Documentation

Default to recruiter-friendly Markdown. When useful, include:

- **Project overview** — what the project is, the system type, and what problem it appears to solve.
- **Technologies found** — languages, frameworks, libraries, databases, services, and tools with evidence.
- **Features and system capabilities** — feature summaries grounded in routes, components, services, models, schemas, tests, or UI text.
- **Resume work experience** — concise action-oriented bullets that say what the user built or improved.
- **Portfolio entry** — project title, problem/goal, built features, tech stack, and evidence-backed result.
- **Job description from project** — responsibilities and qualifications that match the codebase.
- **Technical accomplishment summary** — short paragraph for recruiters or hiring managers.
- **Evidence used** — files or project areas supporting key claims, plus inferred or unconfirmed items.

### Career Wording Rules

- Write what the user built, designed, improved, integrated, validated, stabilized, or maintained rather than only describing what the project contains.
- Use concrete feature or responsibility names from the codebase instead of vague phrases like "built a system" or "managed data".
- Connect technical work to user or system value only when the evidence supports that connection.
- Keep bullets short enough for a resume, with one central idea per bullet.
- Preserve technical substance while making the text readable for recruiters and hiring managers.
- Mark unverified context explicitly instead of filling gaps with assumptions.

## Output Formats

### Resume / CV Format

```markdown
## Technical Skills

### Languages & Frameworks
- [Language/Framework]: [evidence-based proficiency description]

### Architecture & Patterns
- [Pattern]: [how it's demonstrated in the codebase]

### Tools & Infrastructure
- [Tool]: [evidence of usage]

## Professional Experience

### [Project Name] — [Role Description]
- Built [feature] using [technology], handling [scale/complexity]
- Implemented [pattern] to solve [problem], resulting in [outcome]
- Designed [system] with [quality attributes] (tested, documented, monitored)
```

### Portfolio Format

```markdown
## Project: [Name]

### Overview
One-paragraph description of what the project does and its significance.

### Tech Stack
Categorized list of technologies with evidence of usage depth.

### Key Features
- Feature 1: technical description + complexity + quality indicators
- Feature 2: ...

### Architecture Highlights
Notable design decisions with rationale visible in code.

### Quality & Best Practices
Testing, security, performance, documentation evidence.
```

### Job Description Format

```markdown
## [Role Title]

### Required Skills
Skills demonstrated extensively in the codebase.

### Nice-to-Have Skills
Skills present but not deeply demonstrated.

### Responsibilities
Based on the types of work visible in the codebase.

### Technical Environment
Stack, tools, and infrastructure used in the project.
```

## L5 Acceptance Gates

- Every skill claim is backed by specific code evidence (file, pattern, or feature).
- Proficiency levels honestly reflect depth of usage, not mere presence.
- No proprietary business logic, secrets, or internal details are exposed.
- Output clearly separates demonstrated skills from inferred or assumed ones.
- Documentation is formatted for its intended audience (recruiter, hiring manager, developer).

## Example Trigger Phrases

- "Create a resume from this project"
- "What skills does this codebase demonstrate?"
- "Write a job description based on this code"
- "Build a portfolio entry from my project"
- "What technical experience can I claim from this?"
- "Assess my skill level based on this codebase"
- "Help me prepare for interviews based on this project"

## Usage Limitations

- Do not fabricate skills or experience not evidenced in the codebase.
- Do not expose proprietary business logic, internal APIs, or trade secrets.
- Do not include credentials, API keys, or personally identifiable information.
- Do not claim proficiency levels that the code evidence does not support.
- Do not use this skill for actual code review — use `code-review-refactor` instead.
