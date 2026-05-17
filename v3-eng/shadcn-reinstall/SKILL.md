---
name: shadcn-reinstall
description: >
  Use this skill immediately when the user wants to remove shadcn/ui and
  reinstall it safely from scratch in a frontend or React-based project. Always
  use this skill when the user mentions reinstall shadcn, reset shadcn/ui, wipe
  shadcn, remove and reinstall shadcn, install shadcn again, clean shadcn and
  reinstall, split cva variants after reinstall, or change the utility from
  `cn` to `Cn` after reinstall, even if the user does not say "reinstall" but
  asks to "wipe and reinstall" or "reset shadcn completely". Always inspect
  git status, important paths, package manager, framework, `components.json`,
  UI path, utils path, and CSS path before deleting or overwriting files.
---

# Shadcn Reinstall

## About

This skill is for safely removing `shadcn/ui` and reinstalling it from scratch while preventing deletion of the user's custom components and preventing overwrites of files with uncommitted changes.

This skill emphasizes a check-before-delete workflow, confirmation before overwrite, and reinstalling through the `shadcn` CLI only. Do not manually create shadcn files or copy components by hand.

This skill also supports follow-up work after reinstall, such as reinstalling the previous components with `shadcn add`, cleaning dependencies, build verification, auditing `"use client"`, and splitting `cva()` variants only when the user asks for it.

## General Requirements

- Always respond in Thai, except for filenames, identifiers, packages, commands, code, or text that must remain unchanged as evidence.
- Use only information from the real project. Do not guess framework, package manager, alias, or paths that have not been inspected.
- When an issue depends on the version of shadcn/ui, the CLI, framework, Tailwind, React, or package manager, look up the latest official documentation before concluding, and do not hard-code version numbers in this skill content.
- Keep all guidance in a single `SKILL.md` file. Do not split references, scripts, assets, or additional files.
- Write each point clearly, concisely, and with complete meaning on its own.
- Check and fix grammar in every response before sending so the text is readable, correct, and unambiguous.
- Do not delete or overwrite risky files without user confirmation.
- Do not use destructive commands such as reset, clean, or recursive delete without explaining the paths and getting user approval first.

## Workflow

### 1. Check Status Before Starting

- Check `git status` before deleting or editing files every time.
- Identify all uncommitted changes related to `components`, `lib`, CSS, config, and dependency files.
- Separate files the user may have edited manually from files that are likely shadcn-generated components.
- If there are uncommitted changes in paths that will be deleted or overwritten, stop and ask the user to confirm before proceeding.
- If the project has no git repository or git status cannot be checked, state the limitation and ask the user to confirm before deleting files.

### 2. Inspect Project Structure

- Detect the package manager from lockfiles and package scripts, such as `pnpm-lock.yaml`, `package-lock.json`, `yarn.lock`, or `bun.lock`.
- Detect the framework from dependencies, config, and file structure, such as Next.js, Vite, Astro, Laravel, React Router, or TanStack Start.
- Inspect `components.json` to read aliases, style, `rsc`, `tsx`, icon library, and paths used by the CLI.
- Identify the UI path from aliases, such as `components/ui` or `src/components/ui`.
- Identify the utils path from aliases, such as `lib/utils` or `src/lib/utils`.
- Identify the CSS path from `components.json`, framework config, app entry, or global stylesheet.
- Inspect import aliases from `tsconfig.json`, `jsconfig.json`, or `package.json#imports`.

### 3. Identify Related shadcn Files

- Identify existing shadcn components from the UI path only.
- Identify utilities used by shadcn, such as `cn` in the utils path, according to what is found in the project.
- Identify CSS variables or base styles that `shadcn init` previously added to global CSS.
- Identify dependencies related to installed components, such as Radix, class-variance-authority, clsx, tailwind-merge, or lucide-react when found in the manifest.
- Do not include the user's custom components in the delete list when they live outside the UI path or contain project-specific logic.

### 4. Ask for Confirmation Before Deleting or Overwriting

- Show the user the paths that will be deleted or overwritten before taking action.
- Group paths by category, such as shadcn components, shadcn utilities, global CSS, `components.json`, and dependency files.
- Briefly and clearly explain the impact of each group.
- Ask the user to confirm before deleting files or running commands that may overwrite files.
- If the user does not confirm, stop before the delete or overwrite step.

### 5. Delete Only Confirmed shadcn Files

- Delete only shadcn files the user has confirmed may be deleted.
- Do not delete the user's custom components, wrapper components, pages, feature modules, or business logic.
- Do not delete the entire `components` folder if it contains files that are not shadcn-generated components.
- Do not delete the entire `lib` folder just because it contains `lib/utils`.
- If global CSS added by shadcn must be removed, edit only the related block or tokens and preserve other styles.
- If you are not sure whether a file belongs to shadcn or is custom user code, ask before deleting.

### 6. Reinstall Only Through the shadcn CLI

- Use the `shadcn` CLI for `init` only, and do not create shadcn files manually.
- Use the package manager detected from the project, such as `pnpm dlx`, `npx`, `yarn dlx`, or `bunx`.
- Use the init command appropriate for the framework and project state according to the latest official documentation.
- Avoid flags that automatically overwrite files unless the user has already confirmed.
- Inspect CLI output to confirm init succeeded and paths match `components.json`.
- If the CLI asks interactive questions, answer from inspected evidence or ask the user when evidence is missing.

### 7. Reinstall Previous Components

- Summarize previous component names from files in the UI path before deletion.
- Reinstall previous components only with `shadcn add`.
- Use the `shadcn add` command through the detected package manager.
- Reinstall only components the user wants back or components with evidence of real use in the project.
- If previous components had user customization, warn that reinstall may remove customization and ask for confirmation before overwriting.

### 8. Clean Dependencies After Reinstall

- Inspect remaining dependencies after reinstall from `package.json` and the lockfile.
- Remove dependencies only after confirming there are no remaining imports or usage in the project.
- Do not remove dependencies that may be used by custom components or other project areas without checking usage.
- Run install through the original package manager when needed to keep the lockfile consistent.
- Run lint, typecheck, tests, or build according to the scripts available in the project.
- Treat the reinstall as incomplete until build or appropriate verification passes, or until clear limitations are documented.

### 9. Audit `"use client"`

- Audit `"use client"` after reinstall only in files related to affected shadcn components or wrappers.
- Do not remove `"use client"` just because a file appears to have no interaction after a superficial read.
- Check hooks, event handlers, browser APIs, state, effects, context, animation, and third-party client components before recommending removal.
- Remove `"use client"` only from files the user confirms do not need it and only when code evidence supports removal.
- If unsure, state a question or recommendation instead of deleting immediately.

## Splitting `cva()` Variants

Do this only when the user specifically wants to split `cva()` variants out of a component after reinstall.

### 1. Preconditions Before Splitting Variants

- Verify that the component to split has already been reinstalled and the build passes.
- Verify that the component actually has `cva()` or a variant definition worth splitting.
- Ask the user to confirm the component names whose variants should be split.
- Do not automatically split variants across the whole project unless the user specifies it.

### 2. Naming Convention

- Name variant files in kebab-case, such as `button-variants.ts`.
- Name variant variables in snake_case, such as `button_variants`.
- Name types in PascalCase, such as `ButtonVariantsProps`.
- Keep the component name as the original shadcn name, such as `Button`.
- State clearly that the default shadcn utility is `cn`.
- Change the utility from `cn` to `Cn` when performing the variant-splitting step or when the user asks for the rename.

### 3. Variant Split Structure

- Move only the `cva()` definition and related types to the variants file.
- Make the component import variants from the new file with a path consistent with the project's alias or relative-import pattern.
- Preserve the component public API unless the user asks to change it.
- Ensure exports from the variants file are sufficient for the component and downstream usage.
- Avoid moving logic that is not variant styling out of the component.

### 4. Changing `cn` to `Cn`

- State that shadcn uses `cn` as the default utility before customization.
- Rename the utility from `cn` to `Cn` only in files in the variant-splitting scope or the scope specified by the user.
- Update declarations, imports, and call sites that are related in the same scope.
- Verify that `cn` and `Cn` are not mixed in a way that makes imports or call sites confusing.
- Run typecheck or build after the rename to confirm there are no missed references.

## Output Format

### Pre-Delete Plan

- Show the detected package manager, framework, UI path, utils path, and CSS path.
- Show the previous shadcn components found and the components proposed for reinstall.
- Show paths proposed for deletion or overwrite.
- Identify files with uncommitted changes that require user confirmation.

### Post-Reinstall Report

- Summarize the shadcn CLI commands that were run.
- Summarize components reinstalled with `shadcn add`.
- Summarize files deleted, edited, or overwritten.
- Summarize dependencies cleaned up or kept, with reasons.
- Summarize lint, typecheck, test, or build results.
- State limitations or items that still require user decisions.

### Post-Variant-Split Report

- Summarize variant files created or edited.
- Summarize components that still use the original shadcn component name.
- Summarize types and variables adjusted to the naming convention.
- State that the default utility was `cn` and where it was changed to `Cn`.

## Example Requests That Should Use This Skill

- "ลบ shadcn แล้วติดตั้งใหม่ทั้งหมด"
- "reinstall shadcn/ui ให้ปลอดภัย"
- "reset shadcn แล้ว add component เดิมกลับ"
- "wipe shadcn แต่ห้ามลบ custom component"
- "ติดตั้ง shadcn ใหม่ผ่าน CLI"
- "หลัง reinstall ช่วยแยก cva variants ของ button ให้หน่อย"
- "เปลี่ยน cn เป็น Cn หลังแยก variants"

## Usage Limitations

- Do not use this skill for normally adding a shadcn component when no deletion or full reinstall is required.
- Do not use this skill for general component refactors unrelated to shadcn reinstall.
- Do not delete the user's custom components even if their names resemble shadcn components.
- Do not manually create shadcn files, because shadcn components must come from the shadcn CLI.
- Do not overwrite files with uncommitted changes unless the user confirms.
- Do not split `cva()` variants unless the user asks for it.
