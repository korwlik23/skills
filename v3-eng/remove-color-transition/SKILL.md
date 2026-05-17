---
name: remove-color-transition
description: >
  Use this skill immediately when the user wants to remove, disable, or stop
  CSS transitions related to color in frontend work so colors change instantly
  without fade or transition effects. This covers CSS, SCSS, LESS, Tailwind CSS,
  React JSX/TSX, Vue SFC, inline styles, styled-components, Emotion, and
  CSS-in-JS. Always use this skill for requests involving removal of
  `transition-colors`, disabling color transitions, making hover/focus/active
  colors change immediately, or removing gradual color-change effects, even
  when the user does not say "transition" directly but asks for "instant color
  changes" or "no fade".
---

# Remove Color Transition

## About

This skill is for removing or disabling CSS transitions related to color in frontend work so colors change instantly without fade or transition effects between states.

The skill scope covers transitions affecting `color`, `background-color`, `border-color`, `outline-color`, `fill`, `stroke`, `text-decoration-color`, `caret-color`, `accent-color`, and gradient-token colors when found in project context.

This skill applies to regular CSS, SCSS, LESS, Tailwind CSS, React, Vue, inline styles, styled-components, Emotion, and other CSS-in-JS patterns that can define color transitions.

## General Requirements

- Always respond in Thai, except for filenames, identifiers, class names, CSS properties, code, or text that must remain unchanged as evidence.
- Use only information from real code, and do not guess that a transition exists in files that have not been inspected.
- When an issue depends on the version of CSS, Tailwind, React, Vue, or a related library, look up the latest official documentation before concluding, and do not hard-code version numbers in this skill content.
- Keep all guidance in a single `SKILL.md` file. Do not split references, scripts, assets, or additional files.
- Write each point clearly, concisely, and with complete meaning on its own.
- Check and fix grammar in every response before sending so the text is readable, correct, and unambiguous.
- Preserve transitions that are not related to color unless the user asked to remove all transitions.

## Workflow

### 1. Define Scope

- Identify the files, components, selectors, classes, or style blocks in scope.
- Identify whether the goal is to remove only color transitions or disable all transitions for the element.
- If the user specifies only certain interactions such as hover, focus, active, or dark mode, modify only the relevant states.
- If the request is ambiguous, ask the user before removing transitions that may affect other motion such as opacity, transform, or layout.

### 2. Find Color-Related Transitions

- Search for `transition`, `transition-property`, `transition-duration`, `transition-delay`, and `transition-timing-function` in relevant files.
- Search for Tailwind classes such as `transition`, `transition-all`, `transition-colors`, `duration-*`, `delay-*`, `ease-*`, and `motion-*`.
- Search for inline styles such as `style={{ transition: ... }}` or `:style="{ transition: ... }"`.
- Search CSS-in-JS for `transition: ...`, `transitionProperty: ...`, or object styles that define transitions.
- Inspect pseudo-classes and state classes such as `:hover`, `:focus`, `:active`, `group-hover`, `peer-*`, `data-*`, `aria-*`, and dark mode.

### 3. Separate Color Transitions From Other Transitions

- Treat a transition as color-related when `transition-property` directly lists color properties.
- Treat a transition as color-related when `transition: all` or Tailwind `transition-all` is used and the element changes color in the same state.
- Treat Tailwind `transition` as color-related when the element state changes color, because that utility covers many color properties.
- Treat Tailwind `transition-colors` as the primary target to remove or replace.
- Do not remove transitions for `opacity`, `transform`, `translate`, `scale`, `rotate`, `filter`, `height`, `width`, or layout properties unless that transition is tied to color or the user asks to remove all transitions.

### 4. Modify Code by Style Type

- For CSS, SCSS, or LESS, remove color properties from `transition` or `transition-property`.
- For `transition: all ...`, replace it with non-color property transitions when other motion must be preserved.
- When all transitions for the element must be disabled, use `transition: none` or `transition-property: none` according to the existing code style.
- For Tailwind, remove `transition-colors` when only color transitions should stop.
- For Tailwind, replace `transition` or `transition-all` with a property-specific utility that still needs to transition, such as `transition-opacity`, `transition-transform`, or `transition-shadow`.
- For Tailwind, remove `duration-*`, `delay-*`, and `ease-*` only when no other transition remains.
- For inline styles, remove color properties from `transition` or change to `transition: 'none'` when the user wants all transitions disabled.
- For React, Vue, styled-components, Emotion, and CSS-in-JS, preserve the project's existing style pattern and change only the transition values related to color.

## Case-Based Fix Patterns

### CSS or SCSS

- Change `transition: color 150ms ease, transform 150ms ease;` to `transition: transform 150ms ease;`.
- Change `transition-property: color, background-color, transform;` to `transition-property: transform;`.
- Change `transition: all 150ms ease;` to a transition that targets only non-color properties when other motion should remain.
- Use `transition: none;` only when the user wants all transitions for that selector disabled.

### Tailwind CSS

- Remove `transition-colors` when that class causes colors to change gradually.
- Replace `transition` with `transition-opacity`, `transition-transform`, or a utility matching the motion that should remain.
- Replace `transition-all` with a more specific transition so color is not transitioned unintentionally.
- Use `transition-none` when the user wants all transitions for the element disabled.
- Remove `duration-*`, `delay-*`, and `ease-*` when no transition property remains.
- Watch variants such as `hover:transition-colors`, `focus:transition-colors`, `motion-safe:transition-colors`, and `md:transition-colors`.

### React and Vue

- Modify `className`, `class`, computed classes, or array/object classes containing color transitions.
- Modify inline style objects with `transition` or `transitionProperty` related to color.
- Preserve existing state logic and change only styles that make color transition.
- Inspect component variants or props that dynamically generate color classes before concluding the fix is complete.

### styled-components and CSS-in-JS

- Modify template literals or style objects that define color transitions.
- Preserve tokens, theme variables, and helper functions when they are still needed for other styles.
- Inspect styles composed or extended from base components, because color transitions may come from shared components.
- If a color transition is defined in shared styles, assess the impact on every component using those styles before changing it.

## Impact Verification

- Verify that hover, focus, active, selected, disabled, loading, and dark mode still change colors correctly.
- Verify that colors change immediately with no fade between states.
- Verify that non-color motion remains when the user did not ask to remove it.
- Verify that no unnecessary utility remains, such as `duration-*` without any transition in use.
- Verify that class order or specificity does not override the change and bring color transitions back.
- Verify that shared components do not unintentionally affect other pages or states.

## Output Format

When reporting completed work, use this format:

### Changes Made

- Identify files and locations where color transitions were removed or changed.
- Identify what kind of color transition was changed, such as `transition-colors`, `transition: all`, `transition-property: color`, or inline style.
- Identify which transitions were kept and why.

### Verification

- State how you verified that color changes happen instantly.
- State the states or interactions checked, such as hover, focus, active, or dark mode.
- State limitations if the app was not run or not checked in a browser.

### Cautions

- State possible impact on shared components or a design system when relevant.
- State what should be asked from the user when it is unclear whether to disable only color transitions or all transitions.

## Example Requests That Should Use This Skill

- "ลบ transition-colors ออกให้หน่อย"
- "ไม่อยากให้สีปุ่ม fade ตอน hover"
- "ทำให้ background เปลี่ยนสีทันที"
- "ปิด color transition ใน component นี้"
- "เอา transition เฉพาะสีออก แต่ให้ transform ยัง animate อยู่"
- "remove color transition from these Tailwind classes"
- "สีใน styled-components ค่อย ๆ เปลี่ยน ช่วยปิดให้หน่อย"

## Usage Limitations

- Do not use this skill to change theme or palette colors when the user did not ask to remove transitions.
- Do not use this skill to remove all animations unless the user explicitly asks to disable all transitions.
- Do not remove motion that supports accessibility or affordance without checking whether the user wants only color transitions removed.
- Do not conclude all transitions are gone until class names, inline styles, inherited styles, and relevant shared styles have all been checked.
