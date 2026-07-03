# Framework-Specific Review Reference

Loaded on demand by the `code-review-refactor` skill. Per-framework review prompts; the
skill's SKILL.md keeps the framework-agnostic review checklist, severity model, SOLID/
CUPID, anti-patterns, and naming rules. This file holds only the framework-specific
review questions (per the conciseness clause).

### Laravel
- Form Requests for validation?
- Policies for authorization?
- Eager loading for relationships?
- Mass assignment guarded?
- Transactions for multi-step writes?
- Config values instead of `env()` outside config?

### Next.js / React
- Components < 200 lines?
- Hooks extracted for reused logic?
- Effects cleaned up?
- State lifted only as high as necessary?
- Server/client components separated correctly?

### Svelte
- Stores for shared state?
- Reactive declarations used properly?
- Components split at logical boundaries?
- Lifecycle functions cleaned up?

### TypeScript
- Explicit types for function signatures?
- No unjustified `any`?
- Union types instead of optional fields where appropriate?
- Type guards for runtime narrowing?

> Framework idioms evolve — confirm version-specific expectations against current
> official docs per `../../../../RULES.md` §10.
