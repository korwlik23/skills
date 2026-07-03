# lifecycle/

Process gates that wrap any non-trivial build, bugfix, or behavior change. Move through
them in order; skipping requires explicit user permission.

```
brainstorming → writing-plans → test-driven-development + (domain skills)
   → verification-before-completion → finishing-a-development-branch
```

| Skill | Use When |
|-------|----------|
| [`brainstorming`](./brainstorming/SKILL.md) | Before any new feature/build/behavior change — turn idea into approved design |
| [`writing-plans`](./writing-plans/SKILL.md) | After design approval — break work into small, verifiable tasks |
| [`test-driven-development`](./test-driven-development/SKILL.md) | Implementing — RED→GREEN→REFACTOR, test before code (Rigid) |
| [`verification-before-completion`](./verification-before-completion/SKILL.md) | Before claiming done — evidence over claims (Rigid) |
| [`finishing-a-development-branch`](./finishing-a-development-branch/SKILL.md) | Work complete — verify, then decide merge / PR / keep / discard |

After finishing, hand off to `communication/post-mortem` (if non-trivial bug) and
`communication/management-talk` (if leadership / PM needs the update).
