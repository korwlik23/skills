# Refactoring Patterns Reference

Loaded on demand by the `code-review-refactor` skill. Common anti-patterns and the
refactoring techniques that address them. Pulled out of `SKILL.md` per the conciseness
clause; load when you have identified a smell and need a named technique to recommend.

## Common Anti-Patterns

| Smell | Fix |
|-------|-----|
| Primitive Obsession (5+ params) | Use DTO/Value Object |
| Feature Envy | Move method to the class it uses |
| Shotgun Surgery (change → 10+ files) | Consolidate related logic |
| Long Parameter List | Use options object/DTO |
| Boolean Trap `fn(true, false)` | Use named options or enum |
| God Object | Split by responsibility |
| Copy-Paste Programming | Extract shared function |
| Arrow Code (deep nesting) | Use early returns, extract |
| Stringly-Typed states | Use enums or constants |

## Refactoring Techniques

| Technique | When |
|-----------|------|
| Extract Method | Function too long or does multiple things |
| Extract Class | Class has multiple responsibilities |
| Guard Clause | Deep nesting from validation checks |
| Replace Conditional with Polymorphism | Complex switch/if-else on type |
| Introduce Parameter Object | Related params passed together |
| Replace Magic Number with Constant | Unclear hard-coded values |
| Compose Method | Long method with sequential steps |
| Move Method/Field | Logic belongs elsewhere |
