---
name: shadcn-reinstall
description: >
  Use this skill when the user wants to remove and reinstall shadcn/ui safely in
  a frontend or React-based project. Triggers include reinstall shadcn, reset
  shadcn/ui, wipe shadcn, remove and reinstall shadcn, clean shadcn and install
  again, reinstall previous shadcn components, audit `"use client"` after
  reinstall, split `cva()` variants after reinstall, or rename the shadcn utility
  from `cn` to `Cn` in a confirmed scope.
---

# Shadcn Reinstall Skill

Use this skill for high-risk shadcn/ui reset or reinstall work where files may be deleted, regenerated, or overwritten.

## Production-Grade Operating Contract

- Before starting, read `../../../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, inspect git status, package manager, framework, `components.json`, UI path, utils path, CSS path, and imports before proposing changes.
- Treat deletion, recursive deletion, overwrite, dependency cleanup, and generated component replacement as confirmation-gated operations.
- Do not delete or overwrite files with uncommitted changes unless the user explicitly confirms the exact affected paths.
- Use the official `shadcn` CLI as the generation source. Do not hand-write generated shadcn components.
- When shadcn CLI behavior or install flow matters, check the latest official documentation before running commands or giving version-specific advice.

## Safety Gates

Stop and ask for confirmation before:

- Deleting any file or directory.
- Running a command that may overwrite existing files.
- Reinitializing `components.json`.
- Replacing a component that may contain user customization.
- Editing global CSS blocks that may contain project-specific styles.
- Removing dependencies from `package.json` or a lockfile.
- Renaming `cn` to `Cn` outside a narrow user-approved scope.

## Process

### 1. Inspect Current State

- Run or inspect `git status` before deleting or editing files.
- List uncommitted changes related to components, `lib`, CSS, config, and dependency files.
- Detect package manager from lockfiles and scripts: `pnpm-lock.yaml`, `package-lock.json`, `yarn.lock`, `bun.lock`.
- Detect framework from dependencies, config, and file structure.
- Inspect `components.json` for aliases, style, `rsc`, `tsx`, icon library, UI path, utils path, and CSS path.
- Inspect import aliases from `tsconfig.json`, `jsconfig.json`, or `package.json#imports`.

### 2. Identify shadcn-Owned Surface

- Identify generated shadcn components from the configured UI path only.
- Identify the shadcn utility path, usually `lib/utils` or `src/lib/utils`, based on project config.
- Identify global CSS variables or base styles likely added by shadcn.
- Identify related dependencies such as Radix packages, `class-variance-authority`, `clsx`, `tailwind-merge`, and `lucide-react` when present.
- Do not treat custom components, wrappers, pages, feature modules, or business logic as safe to delete just because names resemble shadcn components.

### 3. Present a Pre-Delete Plan

Before deletion or overwrite, show:

- Detected package manager and framework.
- Detected `components.json`, UI path, utils path, and CSS path.
- Existing shadcn components found.
- Components proposed for reinstall.
- Paths proposed for deletion, edit, or overwrite.
- Files with uncommitted changes.
- Expected impact and what customization may be lost.

Proceed only after the user confirms the exact destructive or overwrite actions.

### 4. Delete Only Confirmed Files

- Delete only confirmed shadcn-generated files.
- Do not delete the whole `components` directory if it contains non-shadcn files.
- Do not delete the whole `lib` directory just because it contains a shadcn utility.
- If editing global CSS, remove or replace only the confirmed shadcn block or tokens.
- Ask before deleting any uncertain file.

### 5. Reinstall Through shadcn CLI

- Use the detected package manager, such as `pnpm dlx`, `npx`, `yarn dlx`, or `bunx`.
- Run `shadcn init` only with options appropriate to the inspected framework and latest official docs.
- Avoid overwrite flags unless the user has confirmed the paths.
- Read CLI output to verify generated paths match `components.json`.
- If CLI prompts are interactive, answer from inspected project evidence or ask the user when evidence is missing.

### 6. Add Previous Components Back

- Reconstruct the component list from the pre-delete UI path inventory.
- Use `shadcn add` only; do not hand-create generated component files.
- Add only components the user requested or components with evidence of active imports/usages.
- Warn before overwriting customized components.

### 7. Clean Dependencies and Verify

- Remove dependencies only after searching imports and usage across the project.
- Keep dependencies that custom components or non-shadcn code still use.
- Run package-manager install when lockfile consistency requires it.
- Run available lint, typecheck, tests, or build scripts.
- Treat the reinstall as incomplete until verification passes or the remaining verification gap is explicitly reported.

## Optional: Audit `"use client"`

Only do this when the user asks for it or when reinstall changed client/server boundaries.

- Audit `"use client"` only in files related to reinstalled shadcn components or affected wrappers.
- Do not remove `"use client"` just because a file looks non-interactive on a shallow read.
- Before proposing removal, check for hooks, event handlers, browser APIs, state, effects, context, animation, and third-party client-only components.
- Remove `"use client"` only where code evidence confirms it is unnecessary and the user agrees.
- When uncertain, report it as a question or recommendation instead of removing it.

## Optional: Split `cva()` Variants

Only do this when the user asks to split variants after reinstall.

- Confirm the component list before splitting.
- Verify each component actually contains `cva()` or variant definitions worth extracting.
- Name variant files in kebab-case, such as `button-variants.ts`.
- Name variant variables in snake_case, such as `button_variants`.
- Name exported prop types in PascalCase, such as `ButtonVariantsProps`.
- Preserve the original shadcn component public API unless the user asks otherwise.
- Move only variant styling and related types; do not move unrelated component logic.

## Optional: Rename `cn` to `Cn`

- Treat shadcn's default utility name as `cn`.
- Rename `cn` to `Cn` only in the user-approved scope.
- Update declarations, imports, and all call sites in that same scope.
- Do not leave confusing mixed usage of `cn` and `Cn` in the affected files.
- Run typecheck or build after the rename.

## Output Format

```markdown
# Shadcn Reinstall Report

## Pre-Delete Plan
- Package manager/framework detected.
- shadcn paths and components found.
- Paths proposed for deletion or overwrite.
- Uncommitted changes and confirmation status.

## Changes Made
- CLI commands run.
- Files deleted, generated, edited, or preserved.
- Components reinstalled.
- Dependencies cleaned or kept.

## Verification
- Commands run and results.
- Build/typecheck/test status.
- Remaining verification gaps.

## Risks
- Lost customizations, shared CSS impact, dependency uncertainty, or follow-up decisions.
```

## Usage Limitations

- Do not use this skill for normal `shadcn add` work that does not require reinstall or reset.
- Do not use this skill for general component refactors unrelated to shadcn reinstall.
- Do not delete custom components even if they resemble shadcn components.
- Do not hand-write generated shadcn files.
- Do not overwrite uncommitted user changes without confirmation.
- Do not split `cva()` variants or rename `cn` unless the user asks.
