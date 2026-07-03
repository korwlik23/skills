You are working inside the v1.3 AI skills pack (**27 skills** across 5 buckets:
15 engineering + 5 lifecycle + 4 communication + 2 project + 1 meta `skill-benchmark`).
The rigid debugging gate lives inside `bug-debugging`.

v1.3 = v1.2 + three new skills (`post-mortem`, `management-talk`, `scrutinize`),
a recite-verbatim mantra inside the Rigid Debugging Gate, a mandatory
"Simpler-alternative pass" in `code-review-refactor`, the "one iteration is normal,
three is a smell" revision-loop guardrail, explicit cross-skill handoff lines wiring
the lifecycle end-to-end, a 5-bucket directory structure, and slimming of
`bug-debugging` and `code-review-refactor` by moving framework-specific and long
reference material into per-skill `references/` files. The new skills and the
mantra / simpler-alternative / bucketing patterns are adapted from the 9arm-skills
pack. v1.2's domain knowledge and Workflow Discipline Layer carry over unchanged.

Pack layout: `RULES.md` and `AGENTS.md` are at the pack root (`v1.3/`); skills live
at `skills/<bucket>/<name>/SKILL.md`. Each `SKILL.md` reaches the contract via
`../../../RULES.md` (three levels up). Long framework-specific material lives in
`skills/<bucket>/<name>/references/*.md`, loaded on demand and referencing
`../../../../RULES.md` (four levels up).

Buckets:
- **engineering/** — 15 domain skills for code work (backend, frontend, security,
  database, deployment, migration, testing, git, bug-debugging, code-review-refactor,
  scrutinize, release-version, remove-color-transition, remove-shadow-utilities,
  shadcn-reinstall)
- **lifecycle/** — 5 process gates (brainstorming, writing-plans,
  test-driven-development, verification-before-completion,
  finishing-a-development-branch)
- **communication/** — 4 written-artifact skills (post-mortem, management-talk,
  project-documentation, project-job-description)
- **project/** — 2 whole-project skills (senior-fullstack-audit, project-sitemap)
- **meta/** — 1 pack self-evaluation skill (skill-benchmark)

Before changing, reviewing, or acting on any task in this directory:

1. Read `RULES.md` as the shared operating contract — including the **Workflow Discipline
   Layer** (instruction priority, mandatory skill invocation, Rigid/Flexible skill types,
   the development lifecycle, the two HARD GATES, the Red Flags table, and the
   three-iteration revision rule) and the Evidence-Based Findings principle.
2. **Skill invocation is mandatory.** If there is even a ~1% chance a skill applies, read
   and apply its `SKILL.md` BEFORE any response or action — including clarifying questions
   and codebase exploration.
3. Read the relevant `skills/<bucket>/<skill>/SKILL.md` files for domain-specific guidance.
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
   → (optional) post-mortem → (optional) management-talk
```

Debugging path: `bug-debugging` (Rigid Debugging Gate with recite-verbatim Debug Mantra)
→ reproduce → root cause → failing test → fix → `verification-before-completion` →
`post-mortem` (if non-trivial) → `management-talk` (if leadership / PM needs the update).

Review path: pair `scrutinize` (outsider stance, simpler-alternative pass) with
`code-review-refactor` (checklist) — they don't overlap.

The two HARD GATES from `RULES.md` always apply:
- **Design before code** — no implementation until a design is approved.
- **Verification before completion** — no "done" without observed evidence.

Production-grade skill changes should keep `SKILL.md` concise, move large
examples/templates into `references/`, include explicit safety gates for destructive
operations, and preserve valid YAML frontmatter with `name` and `description`.
