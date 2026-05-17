---
name: remove-shadow-utilities
description: >
  Use this skill when the user wants to remove, disable, or eliminate shadows
  from frontend code. Triggers include removing shadow utilities, `box-shadow`,
  `text-shadow`, `drop-shadow`, inset shadow, Tailwind `shadow-*` or
  `drop-shadow-*`, making UI flat/no-shadow, or removing raised card/button
  effects while preserving rings, outlines, focus indicators, layout, color,
  spacing, border radius, and unrelated animation.
---

# Remove Shadow Utilities Skill

Use this skill for focused frontend changes that remove shadows from a scoped UI surface without damaging accessibility or unrelated design styles.

## Production-Grade Operating Contract

- Before starting, read `../../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, inspect real code before editing, preserve non-shadow styles, keep the change scoped, and report verification limits.
- Use this skill for shadow removal only; do not let it override accessibility requirements, user instructions, or design-system constraints.
- Never remove focus indicators just because they are visually near a shadow utility.

## Scope

Shadow sources include:

- `box-shadow`
- `text-shadow`
- `filter: drop-shadow(...)`
- `drop-shadow(...)`
- inset shadow
- Tailwind `shadow`, `shadow-*`, `shadow-[...]`, `inset-shadow-*`
- Tailwind `drop-shadow-*`, `drop-shadow-[...]`
- shadow theme tokens, variant props, or CSS-in-JS values that generate the above

Out of scope unless the user explicitly asks:

- `ring`, `ring-*`, `inset-ring-*`
- `outline`, `outline-*`
- focus-visible utilities
- border, radius, spacing, layout, colors, and unrelated filters

## Process

### 1. Identify Scope

- Identify the files, components, selectors, class lists, style blocks, or shared styles in scope.
- Determine whether the user wants shadows removed from one element, one component, or an entire surface.
- Include user-specified states such as hover, focus, active, selected, disabled, loading, dark mode, and responsive breakpoints.
- If the request is ambiguous, ask before editing non-shadow styles.

### 2. Find Shadow Sources

Search for:

- CSS properties: `box-shadow`, `text-shadow`, `filter`, `backdrop-filter`
- CSS functions: `drop-shadow(...)`
- Tailwind classes: `shadow`, `shadow-*`, `shadow-none`, `inset-shadow-*`, `drop-shadow-*`, `drop-shadow-none`, `filter`
- Arbitrary utilities: `shadow-[...]`, `drop-shadow-[...]`, `inset-shadow-[...]`
- Shadow color utilities: `shadow-*/*`, `drop-shadow-*/*`
- Inline styles: `boxShadow`, `textShadow`, `filter`
- CSS-in-JS: `box-shadow`, `text-shadow`, `boxShadow`, `textShadow`, `filter`, template literals, style objects
- Shared sources: base components, variants, theme tokens, helper functions, component props such as `elevation`, `raised`, `hasShadow`, or `surfaceShadow`

### 3. Remove Only Shadow

- Change `box-shadow` and `text-shadow` to `none` or remove declarations when the cascade will not bring them back.
- Remove only `drop-shadow(...)` from `filter` when other filters such as `blur(...)`, `brightness(...)`, or `grayscale(...)` must remain.
- Remove Tailwind shadow utilities when they directly create shadow.
- Use `shadow-none` or `drop-shadow-none` only when an override is needed for a base class, variant, state, or breakpoint.
- Remove unused shadow color utilities after the main shadow class is gone.
- Preserve rings, outlines, borders, layout, spacing, color, radius, state logic, and unrelated animation.

## Common Fix Patterns

| Context | Prefer |
|---------|--------|
| `box-shadow: 0 10px 20px rgb(...);` | `box-shadow: none;` or remove the declaration when safe |
| `text-shadow: 0 1px 2px rgb(...);` | `text-shadow: none;` |
| `filter: blur(4px) drop-shadow(...);` | `filter: blur(4px);` |
| Tailwind `shadow-lg` | Remove it, or use `shadow-none` when overriding inherited/base shadow |
| Tailwind `drop-shadow-xl` | Remove it, or use `drop-shadow-none` for state/breakpoint override |

## Validation

- Verify elements in scope have no box shadow, text shadow, drop shadow, or inset shadow remaining.
- Verify hover, focus, active, selected, disabled, loading, dark mode, and responsive breakpoints do not add shadows back.
- Verify rings, outlines, and focus indicators remain intact.
- Verify non-shadow filters remain when the user did not ask to remove all filters.
- For visual UI changes, run the app or inspect in a browser when practical; otherwise state the verification gap.

## Output Format

```markdown
# Shadow Removal Update

## Changes Made
- Files and locations changed.
- Shadow sources removed or overridden.
- Accessibility indicators preserved.

## Verification
- States/breakpoints checked.
- Commands, build, or browser checks run.
- Verification limits if not run.

## Risks
- Shared component or design-system impact.
- Any remaining ambiguity around scope.
```

## Usage Limitations

- Do not change color, border, spacing, radius, layout, or animation unless required to remove a shadow.
- Do not remove outline or focus indicators automatically.
- Do not remove an entire `filter` when only `drop-shadow(...)` can be removed.
- Do not change central theme tokens without checking every affected component.
- Do not claim all shadows are gone until class names, inline styles, inherited styles, variants, and shared styles in scope have been checked.
