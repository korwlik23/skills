---
name: remove-color-transition
description: >
  Use this skill when the user wants to remove, disable, or stop frontend color
  transitions so colors change instantly without fade effects. Triggers include
  removing `transition-colors`, disabling color transition, making hover/focus/
  active colors change immediately, removing color fade, or preserving transform/
  opacity motion while removing only color-related transitions in CSS, SCSS,
  Tailwind, React, Vue, inline styles, styled-components, Emotion, or CSS-in-JS.
---

# Remove Color Transition Skill

Use this skill for focused frontend changes that remove color-related transitions while preserving unrelated motion and behavior.

## Production-Grade Operating Contract

- Before starting, read `../../../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, inspect real code before editing, preserve non-color behavior, keep the change scoped, and report verification limits.
- Use this skill for color-transition removal only; do not let it override accessibility requirements, user instructions, or design-system constraints.
- Ask before removing all transitions when the request could mean only color transitions.

## Scope

Color transitions include transitions affecting:

- `color`
- `background-color`
- `border-color`
- `outline-color`
- `fill`
- `stroke`
- `text-decoration-color`
- `caret-color`
- `accent-color`
- color-related gradient tokens when found in project context

This skill covers CSS, SCSS, LESS, Tailwind CSS, React JSX/TSX, Vue SFC, inline styles, styled-components, Emotion, and other CSS-in-JS patterns.

## Process

### 1. Identify Scope

- Identify the files, components, selectors, class lists, or style blocks in scope.
- Determine whether the user wants only color transitions removed or all transitions disabled for the element.
- If the user specifies a state such as hover, focus, active, selected, disabled, loading, dark mode, or responsive breakpoint, edit that state specifically.
- If the request is ambiguous, ask before removing transitions that affect `opacity`, `transform`, `filter`, dimensions, or layout.

### 2. Find Color Transitions

Search for:

- CSS properties: `transition`, `transition-property`, `transition-duration`, `transition-delay`, `transition-timing-function`
- Tailwind classes: `transition`, `transition-all`, `transition-colors`, `transition-none`, `duration-*`, `delay-*`, `ease-*`, `motion-*`
- Inline styles: `style={{ transition: ... }}`, `style={{ transitionProperty: ... }}`, `:style="{ transition: ... }"`
- CSS-in-JS values: `transition`, `transitionProperty`, template literals, and style objects
- State variants: `:hover`, `:focus`, `:active`, `group-hover`, `peer-*`, `data-*`, `aria-*`, `dark:*`, breakpoint variants

### 3. Separate Color Motion From Other Motion

- Treat `transition-property` values that list color properties as color transitions.
- Treat `transition: all` or Tailwind `transition-all` as color-related when the same element or state changes color.
- Treat Tailwind `transition` as color-related when the relevant state changes color, because it covers common color properties.
- Treat Tailwind `transition-colors` as the primary removal target.
- Preserve transitions for `opacity`, `transform`, `translate`, `scale`, `rotate`, `filter`, `height`, `width`, or layout properties unless the user asked to remove all transitions.

### 4. Apply the Smallest Safe Change

- For CSS/SCSS/LESS, remove only color properties from `transition` or `transition-property`.
- Replace `transition: all ...` with explicit non-color properties when other motion should remain.
- Use `transition: none` or `transition-property: none` only when the user wants all transitions disabled for that selector.
- For Tailwind, remove `transition-colors` when only color transitions should stop.
- Replace `transition` or `transition-all` with `transition-opacity`, `transition-transform`, `transition-shadow`, or another property-specific utility when needed.
- Remove `duration-*`, `delay-*`, and `ease-*` only when no transition remains that uses them.
- Preserve existing component state logic, variants, tokens, helper functions, and class ordering unless they directly create the color transition.

## Common Fix Patterns

| Context | Prefer |
|---------|--------|
| `transition: color 150ms ease, transform 150ms ease;` | `transition: transform 150ms ease;` |
| `transition-property: color, background-color, transform;` | `transition-property: transform;` |
| Tailwind `transition-colors` | Remove it when no color fade is desired |
| Tailwind `transition-all` plus color state | Replace with a specific non-color transition utility |
| Inline style color transition | Remove the color property or use `transition: 'none'` only when disabling all transitions |

## Validation

- Verify hover, focus, active, selected, disabled, loading, dark mode, and relevant responsive states still change color correctly.
- Verify colors change instantly without fade.
- Verify unrelated motion still works when the user did not ask to remove it.
- Verify no unused `duration-*`, `delay-*`, or `ease-*` utilities remain after removing all transition properties.
- For visual UI changes, run the app or inspect in a browser when practical; otherwise state the verification gap.

## Output Format

```markdown
# Color Transition Update

## Changes Made
- Files and locations changed.
- Color-transition source removed or replaced.
- Non-color transitions preserved and why.

## Verification
- States/interactions checked.
- Commands, build, or browser checks run.
- Verification limits if not run.

## Risks
- Shared component or design-system impact.
- Any ambiguity around removing only color transitions vs all transitions.
```

## Usage Limitations

- Do not use this skill to change theme colors or palettes when the user only asked to remove transitions.
- Do not remove all animation or motion unless the user explicitly asks for it.
- Do not remove motion that supports accessibility or affordance without checking the user's intent.
- Do not claim all color transitions are gone until class names, inline styles, inherited styles, variants, and shared styles in scope have been checked.
