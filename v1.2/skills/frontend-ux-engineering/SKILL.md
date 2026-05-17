---
name: frontend-ux-engineering
description: >
  Use this skill for UI/UX work including responsive design, layout fixes,
  component architecture, state management, accessibility, performance
  optimization, design system cleanup, dark mode, animations, form UX, and
  Core Web Vitals. Triggers on frontend bugs, visual issues, CSS problems,
  data integration, or any request about how the UI looks or behaves.
---

# Frontend UX Engineering Skill

Use this skill for UI redesign, frontend bugs, layout issues, design system cleanup, responsiveness, data integration, performance optimization, and accessibility.

## Production-Grade Operating Contract

- Before starting, read `../../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, preserve existing behavior, keep visual changes scoped, validate responsive states where practical, and report only verified results.
- Use this skill for frontend/UX depth; do not let it override user instructions, repository guidance, accessibility requirements, or security constraints.
- Keep responses proportional. Use the output format for frontend reviews/plans; use a concise summary for small UI fixes.

## Specialized Companion Skills

- Use `remove-color-transition` instead of this general skill when the task is specifically to remove color fade, `transition-colors`, or color-only transition behavior while preserving other motion.
- Use `remove-shadow-utilities` instead of this general skill when the task is specifically to remove shadows, Tailwind shadow utilities, `box-shadow`, `text-shadow`, or `drop-shadow` while preserving rings and focus indicators.
- Use `shadcn-reinstall` instead of this general skill when the task involves resetting, wiping, reinstalling, or regenerating shadcn/ui files.
- Combine this skill with those specialized skills when the change affects shared UI, accessibility, responsive behavior, design-system consistency, or needs browser verification.

## Core Principles

1. Judge UI by observed output — rendered result on real data, real viewport, and real devices — not by code that "should" render correctly. A visual or interaction defect is a real defect.
2. Design for real data — never assume ideal content length or perfect images.
3. Accessibility is not optional — it's a requirement for professional software.
4. Performance is a feature — slow UI is bad UI.
5. Consistency builds trust — every inconsistency erodes user confidence.

## UI Goals

Make every interface:

- **Clean** — visual hierarchy guides the eye naturally
- **Responsive** — works from 320px mobile to 4K desktop
- **Accessible** — keyboard navigable, screen reader friendly
- **Consistent** — follows design system tokens and patterns
- **Real-data ready** — handles all content variations gracefully
- **Production-grade** — no broken states, no missing error handling
- **Performant** — fast initial load, smooth interactions
- **Delightful** — thoughtful micro-interactions that feel alive

## Layout Rules

1. Never leave broken layouts — every viewport must be visually correct.
2. Never overlap elements — use proper stacking context and z-index.
3. Never rely on fixed heights unless necessary — use min-height or auto.
4. Handle long text — truncate, wrap, or scroll deliberately.
5. Handle missing images — use fallback placeholders with correct aspect ratio.
6. Handle empty data — show helpful empty states, not blank screens.
7. Handle loading state — skeleton screens or spinners, never blank content flash.
8. Handle error state — clear error messages with retry option.
9. Handle unauthorized state — redirect or show access denied.
10. Handle all breakpoints — mobile (< 640px), tablet (640-1024px), desktop (> 1024px).

## Component Architecture

### Component Size Rules

- Prefer components under 200 lines; exceed that only when splitting would reduce clarity or break an established local pattern.
- One component = one responsibility.
- Prefer composition over configuration (slots/children over 20+ props).
- Props should be typed and documented for complex components.

### Component Hierarchy

```
Page (layout + data fetching)
  └── Section (layout grouping)
       └── Feature Component (business logic)
            └── UI Component (pure presentation)
                 └── Design System Primitive (button, input, badge)
```

### Extraction Rules

| Signal | Action |
|--------|--------|
| Same UI in 2+ places | Extract to shared component |
| Component > 200 lines | Split into sub-components |
| Complex conditional rendering | Extract to separate components |
| Reusable logic with UI | Extract to custom hook + component |
| Pure logic without UI | Extract to utility/hook only |

## State Management

### State Location Guide

| State Type | Where | Example |
|-----------|-------|---------|
| UI state (toggle, modal) | Local component state | `useState`, `let` |
| Form state | Form library or local | React Hook Form, local |
| Server data | Data fetching library | SWR, React Query, Svelte load |
| Global UI state | Global store | Zustand, Svelte stores |
| URL state | Router/URL params | Search filters, pagination |
| Persistent state | localStorage + store | User preferences |

### Rules

- Keep state as close to where it's used as possible.
- Lift state only when siblings need the same data.
- Don't put server data in global state — use a data fetching library.
- Derive computed values — don't store what you can calculate.
- Clear state on unmount when appropriate.

## Form UX Rules

Every form must include:

- [ ] **Labels** — visible, associated with input (`htmlFor`/`for`)
- [ ] **Placeholders** — helpful examples, not replacements for labels
- [ ] **Validation errors** — inline, near the field, visible without scrolling
- [ ] **Required indicators** — clear which fields are required
- [ ] **Disabled state** — visually distinct, with reason if non-obvious
- [ ] **Loading state** — button shows spinner/loading during submission
- [ ] **Success feedback** — confirmation message or redirect
- [ ] **Error feedback** — specific error with retry option
- [ ] **Double-submit protection** — disable button during submission
- [ ] **Keyboard navigation** — Tab order logical, Enter submits
- [ ] **Autofocus** — first field focused on page load
- [ ] **Field masking** — format phone, currency, date as user types
- [ ] **Undo capability** — for destructive actions, confirm or provide undo

## Accessibility (a11y)

### Must Have

- [ ] Semantic HTML — `nav`, `main`, `section`, `article`, `aside`, `header`, `footer`
- [ ] Keyboard navigation — all interactive elements reachable via Tab
- [ ] Focus management — focus visible, trapped in modals, restored on close
- [ ] ARIA labels — only when semantic HTML isn't sufficient
- [ ] Input labels — every input has an associated label
- [ ] Button names — every button has accessible text
- [ ] Alt text — every meaningful image has descriptive alt text
- [ ] Color contrast — minimum 4.5:1 for normal text, 3:1 for large text
- [ ] No color-only indicators — use icons/text alongside color
- [ ] Skip navigation link — for keyboard users on content-heavy pages
- [ ] Error announcements — validation errors announced to screen readers
- [ ] Reduced motion — respect `prefers-reduced-motion`

### ARIA Rules

- First rule of ARIA: don't use ARIA if native HTML works.
- `aria-label` for elements without visible text.
- `aria-describedby` for additional context.
- `aria-live="polite"` for dynamic content updates.
- `aria-expanded` for collapsible sections.
- `role="dialog"` with `aria-modal="true"` for modals.

## Performance Optimization

### Core Web Vitals Targets

| Metric | Good | Needs Work | Poor |
|--------|------|------------|------|
| LCP (Largest Contentful Paint) | < 2.5s | < 4.0s | > 4.0s |
| FID (First Input Delay) | < 100ms | < 300ms | > 300ms |
| CLS (Cumulative Layout Shift) | < 0.1 | < 0.25 | > 0.25 |
| INP (Interaction to Next Paint) | < 200ms | < 500ms | > 500ms |

### Performance Checklist

- [ ] Images optimized (WebP/AVIF, proper sizing, lazy loading)
- [ ] Fonts optimized (subset, preload, `font-display: swap`)
- [ ] Bundle size analyzed and minimized
- [ ] Code splitting implemented (route-based minimum)
- [ ] Unused CSS/JS removed
- [ ] Third-party scripts deferred or async
- [ ] API calls minimized and cached where appropriate
- [ ] Lists virtualized for large datasets (> 100 items)
- [ ] Animations use CSS transforms/opacity (GPU-accelerated)
- [ ] No layout thrashing (read-then-write DOM pattern)

### Image Rules

- Use `next/image` or equivalent for automatic optimization.
- Always set `width` and `height` or `aspect-ratio` to prevent CLS.
- Use `loading="lazy"` for below-the-fold images.
- Use `loading="eager"` or `priority` for above-the-fold hero images.
- Provide `alt` text for all meaningful images.
- Use `srcset` for responsive images when framework doesn't handle it.

## Animation & Transition Guidelines

### When to Animate

- Page transitions — smooth content replacement.
- State changes — expand/collapse, show/hide.
- Feedback — button press, form submission, success/error.
- Attention — notification entry, badge update.
- Loading — skeleton pulse, progress indication.

### Animation Rules

- Duration: 150-300ms for micro-interactions, 300-500ms for larger transitions.
- Easing: `ease-out` for entrances, `ease-in` for exits, `ease-in-out` for movement.
- Use CSS transitions for simple state changes.
- Use CSS animations for complex sequences.
- Use `transform` and `opacity` only for 60fps performance.
- Respect `prefers-reduced-motion` — disable non-essential animations.
- Don't animate layout properties (`width`, `height`, `margin`, `padding`).

## Responsive Design

### Breakpoint Strategy

```css
/* Mobile first — design for mobile, enhance for larger */
/* Small phone */    @media (min-width: 375px)  { }
/* Large phone */    @media (min-width: 640px)  { }
/* Tablet */         @media (min-width: 768px)  { }
/* Desktop */        @media (min-width: 1024px) { }
/* Large desktop */  @media (min-width: 1280px) { }
```

### Responsive Rules

- Mobile first — base styles for mobile, add complexity for larger screens.
- Use relative units (`rem`, `%`, `vw`) over fixed pixels.
- Test at real device widths (375, 390, 414, 768, 1024, 1440).
- Touch targets minimum 44x44px on mobile.
- Consider thumb reach zones on mobile.
- Hide/show content intentionally — don't just shrink desktop layout.

## Dark Mode

- Use CSS custom properties for theme colors.
- Test all states in both themes.
- Ensure sufficient contrast in both modes.
- Don't just invert colors — design for dark intentionally.
- Respect `prefers-color-scheme` for automatic detection.
- Images may need different treatment (opacity, background).

## L5 Acceptance Gates

- Core states are handled: loading, error, empty, partial data, success, disabled, and permission-denied where relevant.
- Responsive behavior is verified across mobile, tablet, and desktop or the validation gap is stated.
- Accessibility uses semantic HTML first, visible focus, keyboard paths, labels, and contrast checks.
- Visual changes respect existing design system patterns and real content lengths.
- Performance risks such as large bundles, layout shift, unnecessary rerenders, and unoptimized media are considered.

## Output Format

```markdown
# Frontend Review

## Layout Issues
Broken layouts, overflow, responsive problems.
Include viewport and browser where relevant.

## Accessibility Issues
Missing semantics, keyboard traps, contrast violations.
Severity: Critical (blocks usage), High (degrades experience), Medium (best practice).

## Performance Issues
Core Web Vitals violations, bundle size, render blocking resources.
Include metrics where measurable.

## Component Issues
Architecture problems, prop design, state management.

## UX Issues
Missing states, confusing interactions, inconsistent patterns.

## Recommended Fixes
Prioritized list with effort estimates.

## Test Viewport Checklist
- [ ] Mobile 375px
- [ ] Mobile 414px
- [ ] Tablet 768px
- [ ] Desktop 1024px
- [ ] Desktop 1440px
- [ ] Dark mode
- [ ] Empty data
- [ ] Long content
- [ ] Error state
- [ ] Loading state
- [ ] Keyboard navigation
```

## Example Trigger Phrases

- "Fix this layout issue"
- "Make this responsive"
- "The UI is broken on mobile"
- "Review frontend performance"
- "Check accessibility"
- "Add dark mode support"
- "Redesign this component"
- "Fix the form validation UX"
- "Optimize Core Web Vitals"

## Usage Limitations

- Do not use this skill for backend-only logic — use `backend-architecture` instead.
- Do not assume design tokens or system patterns that are not visible in the codebase.
- Do not make visual claims without specifying viewport and browser context.
- Do not skip responsive verification across breakpoints when reviewing layout changes.
- Do not introduce new UI libraries without justification and user confirmation.
