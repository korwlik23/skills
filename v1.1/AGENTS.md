You are working inside the v1.1 AI skills pack (23 skills: 18 domain skills + 5 lifecycle skills). The rigid debugging gate lives inside `bug-debugging`.

v1.1 = v1's domain knowledge + an enforced Workflow Discipline Layer. The discipline
concepts are adapted from the Superpowers methodology by Jesse Vincent
(MIT — github.com/obra/superpowers), reworked to fit this pack's contract and tone.

Pack layout: `RULES.md` and `AGENTS.md` are at the pack root (`v1.1/`); the 23 skills
live in `skills/<name>/SKILL.md`. Each `SKILL.md` references the contract as `../../RULES.md`.

Before changing, reviewing, or acting on any task in this directory:

1. Read `RULES.md` as the shared operating contract — including the **Workflow Discipline
   Layer** (instruction priority, mandatory skill invocation, Rigid/Flexible skill types,
   the development lifecycle, the two HARD GATES, and the Red Flags table) and the
   Evidence-Based Findings principle.
2. **Skill invocation is mandatory.** If there is even a ~1% chance a skill applies, read
   and apply its `SKILL.md` BEFORE any response or action — including clarifying questions
   and codebase exploration.
3. Read the relevant `skills/<skill>/SKILL.md` files for domain-specific guidance.
4. If `RULES.md` and a `SKILL.md` conflict, use `RULES.md` for behavior, safety,
   communication, escalation, and validation. Use `SKILL.md` for domain-specific detail.
5. User instructions override both, except for destructive, unsafe, or unverifiable
   actions, which still require explicit confirmation or a clear limitation note.
6. Report only issues backed by clear evidence. Separate provable behavior from
   assumptions. Do not turn stylistic preferences into findings unless they have
   measurable system impact.

## Development Lifecycle

For any non-trivial build, bugfix, or behavior change, move through these gates in order.
Skipping a gate requires explicit user permission.

```
brainstorming → writing-plans → test-driven-development + (domain skills)
   → verification-before-completion → finishing-a-development-branch
```

Debugging path: `bug-debugging` (Rigid Debugging Gate) → reproduce → root cause →
failing test → fix → `verification-before-completion`.

The two HARD GATES from `RULES.md` always apply:
- **Design before code** — no implementation until a design is approved.
- **Verification before completion** — no "done" without observed evidence.

Production-grade skill changes should keep `SKILL.md` concise, move large
examples/templates into `references/`, include explicit safety gates for destructive
operations, and preserve valid YAML frontmatter with `name` and `description`.
