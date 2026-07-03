---
name: brainstorming
description: >
  Use this skill BEFORE any creative or build work — creating a feature, building a
  component, adding functionality, scaffolding a project, or modifying behavior. Also
  triggers on "let's build X", "I want to add Y", "can you implement Z", or any request
  that would otherwise lead straight to writing code. Turns a rough idea into an approved
  design through one-question-at-a-time dialogue before any implementation.
---

# Brainstorming

Turn ideas into a clear, approved design before any code is written. This skill owns the
**Design Before Code** HARD GATE from `RULES.md`.

## Production-Grade Operating Contract

- Read `../../../RULES.md` first and apply it as the behavior, safety, validation, and
  communication baseline — especially the Workflow Discipline Layer.
- This is a **Rigid process skill**: do not adapt away the design gate.
- User instructions override this skill. If the user explicitly says "skip design, just
  do it", comply — but state the assumption you are proceeding on.

## The HARD GATE

Do NOT invoke any implementation skill, write code, scaffold, or take an irreversible
action until you have presented a design and the user has approved it. This applies to
every project regardless of perceived simplicity.

**Exempt:** explicitly requested trivial edits (a typo, a single config value).

### Anti-Pattern: "This is too simple to need a design"

Every project goes through this — a todo list, a one-function utility, a config change.
"Simple" projects are exactly where unexamined assumptions cause the most wasted work.
The design can be two sentences for a truly simple change, but you MUST present it and
get approval.

## Process

Create a TodoWrite item per step and complete them in order:

1. **Explore project context** — read files, docs, recent commits, existing patterns.
2. **Assess scope** — if the request is actually several independent subsystems, say so
   immediately and help decompose into sub-projects before refining details. Each
   sub-project gets its own design → plan → implementation cycle.
3. **Ask clarifying questions — one at a time.** Prefer multiple-choice. Focus on
   purpose, constraints, and success criteria. One question per message.
4. **Propose 2–3 approaches** with trade-offs; lead with your recommendation and why.
5. **Present the design in sections** scaled to complexity (a few sentences if simple,
   up to ~250 words if nuanced). Cover architecture, components, data flow, error
   handling, and testing. Ask after each section whether it looks right.
   For any build that creates code, the design MUST include a **file/module layout**
   per the `RULES.md` Structure Before Code HARD GATE: enumerate the files to be
   created (controllers, services, models, views), each with one responsibility.
   Unenumerated structure collapses into a god module at generation time.
6. **Get explicit approval** of the design before moving on.
7. **Write the design doc** to `docs/specs/YYYY-MM-DD-<topic>-design.md` (or the
   project's existing spec location) and, if the repo uses git, commit it.
8. **Spec self-review** — scan for placeholders/TODOs, internal contradictions, scope
   creep, and any requirement that could be read two ways. Fix inline.
9. **Ask the user to review the written spec** before proceeding.
10. **Hand off to `writing-plans`** — that is the only next skill. Do not jump to a
    domain/implementation skill from here.

## Design for Isolation and Clarity

- Break the system into small units with one clear purpose and well-defined interfaces.
- For each unit you should be able to answer: what it does, how it is used, what it
  depends on.
- In an existing codebase: follow existing patterns; include only targeted improvements
  that serve the current goal; do not propose unrelated refactoring.
- **YAGNI ruthlessly** — remove speculative features from every design.

## Red Flags — STOP

| Thought | Reality |
|---------|---------|
| "Too simple to design" | Simple is where assumptions cost most. Present a short design. |
| "I'll just start coding and adjust" | Unapproved direction = wasted work. Gate first. |
| "The user obviously wants X" | Obvious to you ≠ confirmed. Ask one question. |
| "Many questions at once is faster" | Overwhelms. One question per message. |
| "I'll design and implement in one go" | The gate exists between them for a reason. |

## L5 Acceptance Gates

- A design was presented in digestible sections and explicitly approved.
- 2–3 approaches with trade-offs were offered before settling.
- Scope was assessed; oversized requests were decomposed, not silently accepted.
- The design includes a file/module layout (Structure Before Code) — no whole-product
  namespace, no unenumerated controllers/views.
- A spec document was written, self-reviewed, and offered to the user for review.
- No implementation skill was invoked before approval.

## Output Format

```markdown
## Design: <topic>

### Problem & Goal
What we're solving and the success criteria.

### Approaches Considered
- A — trade-offs
- B — trade-offs (recommended, because …)

### Proposed Design
Architecture · components · data flow · error handling · testing — in sections.

### Open Questions
Anything still needing user confirmation.

### Next Step
Spec written to <path>. Awaiting review, then `writing-plans`.
```

---

*Adapted from the Superpowers `brainstorming` skill by Jesse Vincent (MIT —
github.com/obra/superpowers), reworked for the v1.1 contract.*
