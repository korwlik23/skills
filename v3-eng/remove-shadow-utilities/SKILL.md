---
name: remove-shadow-utilities
description: >
  Use this skill immediately when the user wants to remove, disable, or
  eliminate shadows from frontend code across every source that may create them.
  This covers CSS properties, Tailwind classes, inline styles, React JSX/TSX,
  Vue SFC, styled-components, Emotion, and CSS-in-JS. Always use this skill
  when the user mentions removing shadows, removing box-shadow, text-shadow,
  drop-shadow, inset shadow, Tailwind shadow utilities, or making UI have no
  shadow, even with wording like "shadow", "do not make it raised", or "remove
  the shadow", while preserving rings and focus indicators.
---

# Remove Shadow Utilities

## About

This skill is for removing or disabling "shadows" from frontend code across every source that may create shadows, whether from CSS properties, Tailwind classes, inline styles, Vue, React, styled-components, or CSS-in-JS.

The scope covers only `box-shadow`, `text-shadow`, `filter: drop-shadow(...)`, `drop-shadow(...)`, inset shadow, Tailwind shadow utilities, and Tailwind drop-shadow utilities.

The goal is to ensure elements in scope have no remaining shadows while preserving other unrelated styles as much as possible.

## General Requirements

- Always respond in Thai, except for filenames, identifiers, class names, CSS properties, code, or text that must remain unchanged as evidence.
- Use only information from real code, and do not guess that a shadow exists in files that have not been inspected.
- When an issue depends on the version of CSS, Tailwind, React, Vue, or a related library, look up the latest official documentation before concluding, and do not hard-code version numbers in this skill content.
- Keep all guidance in a single `SKILL.md` file. Do not split references, scripts, assets, or additional files.
- Write each point clearly, concisely, and with complete meaning on its own.
- Check and fix grammar in every response before sending so the text is readable, correct, and unambiguous.
- Remove only shadows and shadow-producing utilities. Do not change color, spacing, border radius, layout, or animation unless necessary.
- Do not remove `ring`, `ring-*`, `inset-ring-*`, `outline`, or focus indicators, because they are outside the scope of shadow removal.

## Workflow

### 1. Define Scope

- Identify files, components, selectors, classes, style blocks, or shared styles in scope.
- Identify whether the goal is to remove shadows from certain elements or from the whole component.
- If the user specifies states such as hover, focus, active, dark mode, or responsive breakpoints, modify those states too.
- If the request is ambiguous, ask the user before changing styles that are not shadows.

### 2. Find Shadow Sources

- Search for CSS properties such as `box-shadow`, `text-shadow`, and `filter`.
- Search for `drop-shadow(...)` inside `filter`, `backdrop-filter`, or helpers that compose filter values.
- Search for Tailwind classes such as `shadow-*`, `shadow`, `shadow-none`, `inset-shadow-*`, `drop-shadow-*`, and `filter`.
- Search arbitrary utilities such as `shadow-[...]`, `drop-shadow-[...]`, and `inset-shadow-[...]`.
- Search shadow color utilities such as `shadow-*/*`, `drop-shadow-*/*`, and custom properties related to shadow.
- Search inline styles such as `style={{ boxShadow: ... }}`, `style={{ textShadow: ... }}`, or `:style="{ boxShadow: ... }"`.
- Search CSS-in-JS for `boxShadow`, `textShadow`, `filter`, `box-shadow`, `text-shadow`, or template literals with shadow definitions.
- Inspect base components, variants, theme tokens, and shared styles that may inject shadows.

### 3. Separate Shadows From Other Styles

- Treat `box-shadow` as a direct shadow and remove it or change it to a no-shadow value.
- Treat `text-shadow` as a direct shadow and remove it or change it to a no-shadow value.
- Treat `filter: drop-shadow(...)` as a direct shadow and remove only the `drop-shadow(...)` function if other filters must remain.
- Treat Tailwind `shadow-*` and `inset-shadow-*` as shadow utilities that must be removed or replaced.
- Treat Tailwind `drop-shadow-*` as shadow utilities that must be removed or replaced.
- Do not treat Tailwind `ring-*`, `ring`, `inset-ring-*`, `outline`, or focus indicators as shadows in this skill.
- Do not remove `ring`, `outline`, `border`, or focus indicators even if they are near shadow utilities in the same class list.

### 4. Modify Code by Style Type

- For CSS, SCSS, or LESS, change `box-shadow` to `none` or remove the declaration when cascade will not bring the shadow back.
- For CSS, SCSS, or LESS, change `text-shadow` to `none` or remove the declaration when no shadow is inherited from elsewhere.
- For `filter`, remove only `drop-shadow(...)` and keep other filters such as `blur(...)`, `brightness(...)`, or `grayscale(...)`.
- For Tailwind, use `shadow-none` when you need to override box shadow from another class or variant.
- For Tailwind, remove `shadow-*` and `inset-shadow-*` when there is no need to override the cascade.
- For Tailwind, use `drop-shadow-none` or remove `drop-shadow-*` according to the safest pattern in context.
- For inline styles, change `boxShadow` or `textShadow` to `'none'` when external styles must be overridden.
- For React, Vue, styled-components, Emotion, and CSS-in-JS, preserve the existing writing style and change only shadow-related values.

## Case-Based Fix Patterns

### CSS or SCSS

- Change `box-shadow: 0 10px 20px rgb(0 0 0 / 0.15);` to `box-shadow: none;`.
- Change `text-shadow: 0 1px 2px rgb(0 0 0 / 0.4);` to `text-shadow: none;`.
- Change `filter: blur(4px) drop-shadow(0 4px 8px rgb(0 0 0 / 0.2));` to `filter: blur(4px);`.
- Remove only the shadow declaration when the existing selector has no cascade or override that must be preserved.

### Tailwind CSS

- Remove `shadow-sm`, `shadow`, `shadow-md`, `shadow-lg`, `shadow-xl`, `shadow-2xl`, and `shadow-[...]` when those classes directly create shadows.
- Remove `inset-shadow-*` when it creates inner shadow on the element.
- Remove `drop-shadow-*` or replace it with `drop-shadow-none` when overriding a state or breakpoint.
- Use `shadow-none` when shadow comes from a component base, variant, or a class that is hard to control.
- Check variants such as `hover:shadow-lg`, `focus:shadow-md`, `dark:shadow-xl`, `md:shadow-lg`, `group-hover:shadow-*`, and `data-[state=open]:shadow-*`.
- Remove shadow color utilities such as `shadow-black/20` or `drop-shadow-blue-500/50` when the main shadow has already been removed.
- Do not remove `ring-*`, `ring`, `inset-ring-*`, `outline-*`, or focus-visible utilities during shadow removal.

### React and Vue

- Modify `className`, `class`, computed classes, or array/object classes that contain shadow utilities.
- Modify inline style objects with `boxShadow`, `textShadow`, or `filter` using `drop-shadow(...)`.
- Inspect component props that create shadow variants, such as `elevation`, `raised`, `variant`, `isActive`, or `hasShadow`.
- Preserve existing state logic and change only styles that create shadows.

### styled-components and CSS-in-JS

- Modify template literals or style objects that define `box-shadow`, `text-shadow`, `boxShadow`, `textShadow`, or `filter`.
- Inspect theme tokens such as `shadow`, `elevation`, `surfaceShadow`, or `cardShadow` before concluding no shadow remains.
- If shadow comes from a shared component, assess the impact on other components before changing it.
- If only one instance should lose its shadow, override in the narrowest scope rather than changing a central token.

## Impact Verification

- Verify that elements in scope have no box shadow, text shadow, drop shadow, or inset shadow remaining.
- Verify that hover, focus, active, selected, disabled, loading, dark mode, and responsive breakpoints do not add shadows back.
- Verify that non-drop-shadow filters still work when the user did not ask to remove all filters.
- Verify that rings, outlines, and focus indicators remain after shadow removal.
- Verify that shared components or the design system are not unintentionally damaged in other pages or states.
- Verify that remaining classes do not include unused shadow color utilities or shadow tokens.

## Output Format

When reporting completed work, use this format:

### Changes Made

- Identify files and locations where shadows were removed.
- Identify the shadow source changed, such as CSS property, Tailwind class, inline style, or CSS-in-JS.
- Identify the removed shadow type, such as box shadow, text shadow, drop shadow, or inset shadow.

### Verification

- State how you verified that no shadow remains in scope.
- State states or breakpoints checked, such as hover, focus, dark mode, or responsive state.
- State limitations if the app was not run or not checked in a browser.

### Cautions

- State possible impact on shared components when relevant.
- State clearly that rings, outlines, or focus indicators were not removed.

## Example Requests That Should Use This Skill

- "ลบ shadow ออกจาก component นี้"
- "เอาเงาออกให้หมด"
- "remove all shadow utilities"
- "ไม่อยากให้ card มีเงา"
- "ลบ drop-shadow ใน SVG นี้"
- "เอา box-shadow และ text-shadow ออกจากหน้า UI"
- "ลบ Tailwind shadow class ทั้งหมด แต่ไม่ต้องเปลี่ยน layout"
- "ทำให้ปุ่มไม่มี shadow ตอน focus แต่ยังคง ring ไว้"

## Usage Limitations

- Do not use this skill to change color, border, spacing, radius, or layout when the user did not ask.
- Do not automatically remove outlines or focus indicators that are not shadows, because this may affect accessibility.
- Do not remove an entire filter when only `drop-shadow(...)` can be removed.
- Do not modify a central theme token without assessing impact on other components.
- Do not conclude all shadows are gone until class names, inline styles, inherited styles, variants, and relevant shared styles have all been checked.
