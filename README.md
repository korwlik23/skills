# AI Skills Pack

A principal-level full‑stack engineering **skill pack** for AI coding agents
(Claude Code and compatible harnesses). Skills are markdown instruction files that
shape agent behavior; a shared contract (`RULES.md` / `AGENTS.md`) governs *how* the
agent works, while each skill governs a domain.

> **Recommended version: [`v1.2/`](v1.2) — installable plugin, 24 skills, behaviorally benchmarked.**

## Version lineage

| Version | What it is | Status |
|---|---|---|
| `v1/` | Original 18 domain skills | legacy baseline |
| `v2/` | Earlier iteration (14 skills) | legacy |
| `v1.1/` | v1 + enforced **Workflow Discipline Layer** + 6 lifecycle skills; pushed | superseded by v1.2 |
| **`v1.2/`** | **v1.1 refined**: content fixes, `references/` extraction, RULES tidy, plugin manifest + installer, **self-testing `skill-benchmark`** | **current / recommended** |
| `v3/`, `v4/` | External standalone Thai specialized 5‑skill sets (`jirateep12z/skills`) — kept locally, **git‑ignored** | reference only |
| `superpowers/` | External methodology (`obra/superpowers`, MIT) — discipline concepts adapted into v1.1/v1.2 with attribution; **git‑ignored** | reference only |

`.gitignore` excludes `superpowers/`, `v3/`, `v4/` (each has its own nested `.git`)
and local Claude settings, so they are never pushed.

## What's in v1.2

```
v1.2/
├── .claude-plugin/plugin.json   # plugin manifest (name: fullstack-skills)
├── RULES.md                     # shared operating contract + Workflow Discipline Layer
├── AGENTS.md                    # bootstrap pointing agents to RULES.md
├── install.ps1                  # one-command installer
└── skills/                      # 24 skills, each skills/<name>/SKILL.md
    ├── <18 domain skills>       # backend, frontend, security, db, testing, ...
    ├── <5 lifecycle skills>     # brainstorming, writing-plans, TDD, verification, finishing-branch
    └── skill-benchmark/         # meta: behaviorally evaluates the pack itself
```

Each `SKILL.md` references the contract via `../../RULES.md`. The contract adds:
mandatory skill invocation, instruction priority, Rigid/Flexible skill types, two HARD
GATES (design‑before‑code, verification‑before‑completion), a Red Flags
anti‑rationalization table, evidence/version‑currency rules, and a Thai‑default
response rule.

## Install

Claude Code discovers skills only from `.claude/skills/`, `~/.claude/skills/`, or a
plugin directory. v1.2 is plugin‑shaped, so the simplest path is `--plugin-dir`:

**Option 1 — no copy (fastest):** from inside the target project
```bash
claude --plugin-dir "/abs/path/to/ai_skills/v1.2"
```

**Option 2 — clone then load:**
```bash
git clone https://github.com/korwlik23/skills.git
claude --plugin-dir "./skills/v1.2"
```

**Option 3 — vendored installer (copies into project + updates .gitignore):**
```powershell
pwsh ./v1.2/install.ps1 -Project "C:\path\to\your-project"
```

Skills are invoked as `/fullstack-skills:<name>` or auto‑trigger from their
description.

**Enforce the contract every session** — add to the project's `.claude/CLAUDE.md`:
```markdown
@/abs/path/to/ai_skills/v1.2/RULES.md
@/abs/path/to/ai_skills/v1.2/AGENTS.md
```

(CLI flags can change between Claude Code versions — verify with `claude --help`.)

## Test it (self-benchmark)

v1.2 ships a `skill-benchmark` skill that turns "it should work" into measured
scores.

- **Quick smoke:** `/fullstack-skills:skill-benchmark` → runs a few scenarios, 1 trial each (indicative).
- **Authoritative:** ask it to *"run skill-benchmark, all scenarios, N≥3, isolated blind trials"*. Each trial runs in a fresh context with a blind prompt (skill not named); results are scored against a rubric with pass‑rate + variance, unstable scenarios flagged.

Scenario battery + rubric: `v1.2/skills/skill-benchmark/references/benchmark-scenarios.md`.

## Benchmark results (latest run)

13 scenarios × **N=2** blind, isolated trials (26 trials). Trials operated under the
pack (RULES.md read as contract); skill *expected* was never named.

| Dimension | Scenarios | Pass | Stability |
|---|---|---|---|
| T — trigger accuracy | T1,T2,T3 | 6/6 | ✓ stable |
| G — design‑before‑code gate | G1,G2 | 4/4 | ✓ behavior stable* |
| V — verification gate | V1 | 2/2 | ✓ stable |
| R — Rigid discipline (TDD) | R1 | 2/2 | ✓ stable |
| S — safety gate (shadcn, git) | S1,S2 | 4/4 | ✓ stable |
| E — evidence discipline | E1 | 2/2 | ✓ stable |
| X — anti‑rationalization | X1 | 2/2 | ✓ stable |
| N — negative control | N1,N2 | 4/4 | ✓ behavior stable* |
| **Total** | **13** | **26/26 (100%)** | |

\* **Honest finding:** for "new feature, code now" (G1) and "make it faster" (N2) the
correct *behavior* held every trial (design gate enforced / scope questions asked,
zero blind changes), but the *skill attributed* varied between `brainstorming` and
`backend-architecture`. Behavior is solid; the trigger boundary between the
process‑first skill and the domain skill is not perfectly crisp — the one concrete
improvement area surfaced by this run.

**Honest limitations:** N=2 is a small sample (consistent 2/2 across all, but not
statistically strong — N≥3 recommended for full authority). Trials were a controlled
harness with the pack read as contract, **not** real Claude Code sessions
auto‑triggering skills — this measures *adherence + skill selection*, not the
harness's auto‑trigger. It measures behavioral conformance, not downstream product
quality.

## Status

v1.2 is the strongest, most consistent, install‑ready version, and now has **real
first behavioral evidence (26/26)** — moved from "structurally improved, unproven" to
"strong behavioral signal, small sample". Full authority needs an N≥3 run via the
plugin in fresh sessions (the harness and benchmark are in place to do this).

## License / attribution

Discipline concepts in the lifecycle skills are adapted from the Superpowers
methodology by Jesse Vincent (MIT — github.com/obra/superpowers), reworked for this
pack's contract; attribution is retained in each adapted skill.
