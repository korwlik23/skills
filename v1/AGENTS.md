You are working inside the v1 AI skills pack.

Before changing or reviewing any skill in this directory:

1. Read `RULES.md` as the shared operating contract.
2. Read the relevant `<skill>/SKILL.md` files for domain-specific guidance.
3. If `RULES.md` and a `SKILL.md` conflict, use `RULES.md` for behavior, safety, communication, escalation, and validation. Use `SKILL.md` for domain-specific technical detail.
4. User instructions override both, except for destructive, unsafe, or unverifiable actions, which still require explicit confirmation or a clear limitation note.

Production-grade skill changes should keep `SKILL.md` concise, move large examples/templates into `references/`, include explicit safety gates for destructive operations, and preserve valid YAML frontmatter with `name` and `description`.
