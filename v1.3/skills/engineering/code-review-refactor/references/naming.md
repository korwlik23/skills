# Naming Convention Reference

Loaded on demand by the `code-review-refactor` skill. Case conventions and naming
quality rules for evaluating identifier choices. Pulled out of `SKILL.md` per the
conciseness clause; load when a review surfaces naming concerns that need a structured
checklist to back them up.

## Case Conventions

| Convention | Use For |
|-----------|--------|
| `PascalCase` | Components, Classes, Interfaces, Types, Enums, Hooks |
| `snake_case` | Variables, Parameters, Properties, DB fields, API keys |
| `UPPER_CASE` | Constants, Env vars, Enum members, Error codes |
| `kebab-case` | Files, Folders, URLs, CSS classes, Data attributes |

> Project conventions override this default — check the project's existing patterns
> first; if they conflict, the project wins.

## Naming Quality Rules

| Rule | Check |
|------|-------|
| Intent First | Name reveals purpose before implementation detail |
| Domain Vocabulary | Uses terms consistent with project/team domain |
| Specific Meaning | No vague names (`value`, `data`, `item`, `temp`) when context demands precision |
| Boolean Clarity | Boolean names clearly express state/capability/condition |
| Unit Awareness | Names include units when ambiguous (time, distance, money, size) |
| Scope Precision | Name reflects scope (local, shared, request, session) when it matters |
| Role Differentiation | Similar items have names distinguishing source/target/current/computed |
| Action Accuracy | Functions use verbs matching actual behavior (create, read, validate, transform) |
| Collection Naming | Collections named as plural, individual items named differently |
| Abbreviation Control | Abbreviations only when universally understood in context |
| Lifecycle State | Names clarify lifecycle status (pending, completed, failed, cancelled, expired) |
| Searchable Names | Names are grep-friendly, not too short or common |
