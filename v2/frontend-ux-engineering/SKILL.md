---
name: frontend-ux-engineering
description: Principal frontend & UX — responsive UI, accessibility, performance, Core Web Vitals, component architecture.
---

# Frontend & UX Engineering

## Core Rules

1. UI is the product — if it looks broken, it is broken.
2. Design for real data — never assume ideal content.
3. Accessibility is a requirement, not a feature.
4. Performance is UX — slow UI is bad UI.
5. Consistency builds trust.

## Layout Rules

No broken layouts at any viewport. No overlapping elements. No fixed heights (use min-height). Handle: long text, missing images (fallback), empty data (helpful message), loading (skeleton/spinner), error (message + retry), unauthorized (redirect or deny). All breakpoints: mobile (<640), tablet (640-1024), desktop (>1024).

## Component Architecture

Components < 200 lines. One component = one responsibility. Composition over configuration (slots > 20+ props).

```
Page → Section → Feature Component → UI Component → Design Primitive
```

| Signal | Action |
|--------|--------|
| Same UI × 2+ | → Shared component |
| Component > 200 lines | → Split |
| Complex conditional render | → Separate components |
| Reusable logic + UI | → Hook + component |
| Pure logic | → Utility/hook only |

## State Management

| Type | Where |
|------|-------|
| UI (toggle, modal) | Local state |
| Form | Form library or local |
| Server data | Data fetching library (SWR, React Query) |
| Global UI | Global store (Zustand, Svelte stores) |
| URL state | Router/params |
| Persistent | localStorage + store |

Rules: Keep state close to usage. Lift only when siblings share. Don't put server data in global state. Derive, don't store computed values.

## Form UX

Every form: labels (associated), validation errors (inline, near field), required indicators, disabled state (visually distinct), loading button during submit, success/error feedback, double-submit protection, keyboard nav (Tab order, Enter submits), autofocus first field.

## Accessibility

**Must have**: Semantic HTML. Keyboard navigation. Visible focus. ARIA only when native HTML insufficient. Input labels. Button names. Alt text. Contrast ≥ 4.5:1 (3:1 large text). No color-only indicators. Skip nav link. Error announcements. Respect `prefers-reduced-motion`.

**ARIA rules**: Don't use ARIA if native HTML works. `aria-label` for no visible text. `aria-live="polite"` for dynamic updates. `role="dialog"` + `aria-modal` for modals.

## Performance

### Core Web Vitals Targets

| Metric | Good | Poor |
|--------|------|------|
| LCP | < 2.5s | > 4.0s |
| INP | < 200ms | > 500ms |
| CLS | < 0.1 | > 0.25 |

**Checklist**: Images optimized (WebP/AVIF, sized, lazy). Fonts subset + preload + `font-display: swap`. Bundle minimized + code-split. Unused CSS/JS removed. Third-party scripts deferred. Lists virtualized (>100 items). Animations use transform/opacity only. No layout thrashing.

**Images**: Use framework image component. Set width/height or aspect-ratio (prevent CLS). `loading="lazy"` below fold. `loading="eager"` hero images. Alt text. srcset for responsive.

## Animation Rules

Duration: 150-300ms micro, 300-500ms transitions. Easing: `ease-out` enter, `ease-in` exit. Only `transform` + `opacity` for 60fps. Respect `prefers-reduced-motion`. Never animate layout properties (width, height, margin, padding).

## Responsive

Mobile-first. Relative units (rem, %, vw). Test real widths (375, 390, 414, 768, 1024, 1440). Touch targets ≥ 44px. Hide/show content intentionally.

## Dark Mode

CSS custom properties for theme. Test all states both themes. Sufficient contrast both modes. Respect `prefers-color-scheme`. Images may need different treatment.

## Output Format

```
# Frontend Review
## Layout Issues — broken, overflow, responsive (viewport + browser)
## Accessibility — missing semantics, keyboard, contrast (Critical/High/Medium)
## Performance — Web Vitals, bundle, render blocking (with metrics)
## Component Issues — architecture, props, state
## UX Issues — missing states, confusing interactions
## Fixes — prioritized with effort
## Viewport Checklist — 375/414/768/1024/1440, dark mode, empty, long, error, loading, keyboard
```
