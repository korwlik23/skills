# Design Principles Reference

Loaded on demand by the `code-review-refactor` skill. SOLID, CUPID, and additional
principles used as evaluation lenses. Pulled out of `SKILL.md` per the conciseness
clause; load when the review needs to call out a structural concern by name.

## SOLID

| Principle | Check |
|-----------|-------|
| Single Responsibility | Each unit has one reason to change |
| Open/Closed | Extensible without modifying stable code |
| Liskov Substitution | Subtypes can replace base types safely |
| Interface Segregation | Interfaces are small and specific |
| Dependency Inversion | Depend on abstractions, not concretions |

## CUPID

| Principle | Check |
|-----------|-------|
| Composable | Parts combine without deep internal knowledge |
| Unix | Each unit does one thing well |
| Predictable | Behavior is consistent from input/state/contract |
| Idiomatic | Follows language/framework/project conventions |
| Domain-based | Code reflects domain language and concepts |

## Additional Principles

| Principle | Check |
|-----------|-------|
| KISS | Simplest approach chosen, no unnecessary complexity |
| YAGNI | Only current requirements built, no speculative structure |
| DRY | Each logic piece has single source of truth |
| SoC | Concerns clearly separated, minimal cross-knowledge |
| Composition over Inheritance | Behavior built by composing small parts |
| Law of Demeter | Only talks to direct collaborators |
| Defensive Programming | Validates input before critical operations |
| Immutability | Data not mutated unnecessarily, new values created |
| Cognitive Complexity | Functions not too long, nesting not too deep, early returns used |
