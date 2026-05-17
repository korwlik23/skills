---
name: code-review
description: >
  Use this skill immediately when the user wants code inspected in any form,
  even if they do not say "review" directly. Examples include code review,
  PR review, diff review, bug analysis, "look at this code", "are there bugs",
  security review, performance review, database review, API review,
  accessibility review, observability review, code-quality review, naming review,
  refactor assessment, or requests for code improvement advice. Always use this
  skill when there is code to inspect or analyze. Report only issues backed by
  evidence from the real context, with clear scope, severity, location, impact,
  and fix guidance.
---

# Code Review

## About

This skill is the standard for systematic code review. It focuses on logical correctness, security, performance, data integrity, maintainability, consistency with project standards, and readiness for real use.

Use this skill to help the user find risks that can be proven from the provided code, diff, configuration, log, schema, contract, test, or documentation only. Do not infer behavior without evidence, and do not turn taste-based suggestions into findings unless they affect the real system.

## General Requirements

- Always respond in Thai, except for filenames, identifiers, keywords, code, or text that must remain unchanged as evidence.
- Use only information from the real available context. If information is insufficient, state the limitation or ask the user before drawing conclusions.
- When an issue depends on the version of a language, framework, library, runtime, standard, security guidance, or accessibility guidance, look up the latest official source before concluding, and do not hard-code version numbers in this skill content.
- Keep all guidance in a single `SKILL.md` file. Do not split references, scripts, assets, or additional files.
- Write each point clearly, concisely, and with complete meaning on its own.
- Check and fix grammar in every response before sending so the text is readable, correct, and unambiguous.
- When more than one fix is possible, present all options with trade-offs and let the user decide when the outcome depends on system goals.

## Review Process

### 1. Define Scope

- Identify the kind of work being reviewed, such as PR, diff, snippet, module, architecture, security, performance, or refactor.
- Identify the system area in scope, such as frontend, backend, API, database, infrastructure, build pipeline, or shared library.
- Identify out-of-scope areas when the user has clearly limited the scope.
- Choose the appropriate depth for the context: quick scan, standard review, or deep review.
- If the scope is unclear but there is enough evidence, perform a standard review and state the assumptions used.
- If missing information prevents a decision, ask the user before finalizing a finding.

### 2. Understand Context

- Identify the language, framework, library, runtime, and related tooling from available evidence.
- Identify the role of the code and where it sits in the system.
- Read callers, callees, schema, contracts, configuration, tests, and logs that affect the code behavior when they are present in context.
- Separate provable behavior from assumptions that still need confirmation.
- State review limitations when important information is missing, such as expected behavior, schema, runtime logs, or production configuration.

### 3. Review by Category

- Use the categories below as a thinking framework so the review is broad enough.
- Report only issues that are actually present, have clear evidence, and affect the system or code quality.
- Skip categories that do not apply to the reviewed code without reporting that they were checked and no issue was found.
- Merge repeated issues with the same root cause into one finding and explain the combined impact.
- Separate optional recommendations from findings that are real problems.

### 4. Assign Severity

- **Critical** - Causes system failure, destroys data, opens a severe vulnerability, bypasses authorization, or severely affects production and needs immediate remediation.
- **Important** - Causes behavior to violate requirements, corrupts data, weakens a security control, clearly degrades performance, or creates high production risk.
- **Improve** - Makes code harder to maintain, increases coupling, violates naming standards, or makes structure unnecessarily complex, while not being an immediate user-impacting bug.
- **Suggestion** - Improves maintainability, ergonomics, consistency, or developer experience, but is not required before merge.

### 5. Analyze Impact and Fix Path

- Explain the impact on correctness, security, data integrity, user experience, operations, cost, or maintainability based on the evidence found.
- Propose the smallest fix that truly addresses the root cause.
- State migration risk, compatibility risk, or side effects when a fix may affect other areas.
- When multiple fixes are possible, summarize the pros, cons, and conditions for choosing each option.

## Category 1: Logical Correctness

Check that the code works correctly for its intended purpose.

- Verify that every condition covers all possible cases and no case falls through without handling.
- Verify that loop and index boundaries are precise and do not cause off-by-one errors.
- Verify that value comparisons use the right method for the data type, separating value equality from reference equality.
- Verify that defaults are applied only when a value is truly absent, not when the value is `0`, `false`, or `""`.
- Verify that intentionally empty values are distinguished from values that have not been set.
- Verify that financial or precision-sensitive calculations use fixed-point or integer math instead of floating point.

## Category 2: Naming

Check that names follow the required standards.

- **PascalCase** - Use for functions, components, classes, interfaces, types, enums, namespaces, event handlers, methods, constructors, decorators, custom hooks, and callback patterns.
- **snake_case** - Use for variables, parameters, properties, state management, JSON properties, object keys, database fields, API response keys, and log field keys.
- **UPPER_CASE** - Use for constants, environment variables, magic values, enum members, symbolic keys, global configuration, event names, HTTP methods, status codes, and error codes.
- **kebab-case** - Use for files, folders, URLs, namespace identifiers, module names, CSS classes, attribute values, custom attributes, and data attributes.
- **Intent First** - Check that a name communicates the primary intent before implementation detail.
- **Domain Vocabulary** - Check that names use terms from the system domain and match language used by users or the team.
- **Specific Meaning** - Check that vague names like `value`, `data`, `item`, or `temp` are avoided when the context needs a more specific meaning.
- **Boolean Clarity** - Check that boolean names clearly express a state, capability, or condition so `true` has an obvious meaning.
- **Unit Awareness** - Check that names include units when ambiguity is possible, such as time, distance, money, or data size.
- **Scope Precision** - Check that names reflect scope, such as local, shared, request, or session, when that matters.
- **Role Differentiation** - Check that similar values have distinct names for different roles, such as source, destination, current, or computed values.
- **Action Accuracy** - Check that functions and methods use verbs that match actual behavior, such as create, read, validate, transform, or calculate.
- **Collection Naming** - Check that collections are named as collections and single members have distinct names.
- **Abbreviation Control** - Use abbreviations only when they are understood in that context; use full words when an abbreviation can be ambiguous.
- **Lifecycle State** - Check that names clearly express lifecycle states such as pending, completed, failed, cancelled, or expired.
- **Searchable Names** - Check that names are easy to search in the code and avoid overly short or overly common words.

## Category 3: Design Principles and Code Quality

Check that the code follows good design principles.

### SOLID

- **Single Responsibility** - Each unit should have one reason to change and should not combine unrelated responsibilities.
- **Open/Closed** - Stable code should be extensible for new behavior without modification when that is appropriate.
- **Liskov Substitution** - Subclasses should be usable in place of base types without changing system behavior.
- **Interface Segregation** - Interfaces should be small and specific, without forcing consumers to depend on things they do not need.
- **Dependency Inversion** - Depend on abstractions rather than concrete implementations when that reduces meaningful coupling.

### CUPID

- **Composable** - Parts should combine with other parts without requiring too much internal knowledge.
- **Unix** - Each unit should do one thing well and avoid unrelated responsibilities.
- **Predictable** - Behavior should be consistent from the given input, state, and contract.
- **Idiomatic** - Code should follow the idioms and patterns of the language, framework, and project.
- **Domain-based** - Code should reflect the language and concepts of the problem domain.

### Additional Principles

- **KISS** - Prefer the simplest approach and avoid unnecessary complexity.
- **YAGNI** - Support current requirements only; do not build speculative structure without evidence.
- **DRY** - Each piece of logic should have one source of truth, and duplication should not make change harder.
- **Separation of Concerns** - Keep responsibilities separated so each layer or module has a clear role.
- **Composition over Inheritance** - Prefer composing small units over inheritance when that keeps behavior clearer.
- **Law of Demeter** - Avoid reaching through long chains of collaborators.
- **Defensive Programming** - Validate inputs before critical operations.
- **Immutability** - Avoid unnecessary mutation and create new values where that reduces risk.
- **Cognitive Complexity** - Keep functions easy to follow, reduce deep nesting, and use guard clauses when helpful.

## Category 4: Error Handling

Check that failure paths are explicit, actionable, and safe.

- Verify that errors are caught at the right boundary and are not swallowed silently.
- Verify that user-facing error messages are clear without exposing internal implementation details.
- Verify that logs contain enough context to debug without exposing secrets or sensitive data.
- Verify that retries are bounded and safe, especially for non-idempotent operations.
- Verify that fallback behavior does not hide real failures or corrupt state.
- Verify that async errors, promise rejections, and background-job failures are handled.

## Category 5: Performance

Check that the code avoids unnecessary cost and scales for the likely workload.

- **Algorithmic Complexity** - Check for avoidable `O(n^2)` or worse operations when a simpler structure can reduce cost.
- **N+1 Queries** - Check for database or API calls inside loops that should be batched or eager-loaded.
- **Unbounded Work** - Check that queries, loops, file reads, and responses are bounded by pagination, limits, or streaming.
- **Caching Fit** - Check whether repeated expensive work should use caching when correctness allows it.
- **Memory Usage** - Check that large datasets are streamed or paginated rather than loaded all at once.
- **Resource Cleanup** - Check that timers, listeners, subscriptions, handles, and connections are cleaned up.
- **Frontend Rendering** - Check for unnecessary rerenders, heavy components on critical paths, and missing memoization when evidence shows a real cost.
- **Bundle and Asset Weight** - Check for heavy dependencies, unoptimized images, and assets loaded before they are needed.
- **Blocking Work** - Check that the code avoids blocking calls in a single-threaded event loop and moves heavy computation off the main thread when needed.
- **Concurrency Utilization** - Check that independent work can run concurrently when there is no dependency between tasks.

## Category 6: Security

Check that the code does not create vulnerabilities or weaken required protections.

- **Input Validation** - Validate and normalize input from users, requests, files, environment, or external services before use.
- **Injection Prevention** - Avoid SQL, NoSQL, command, template, LDAP, or path traversal injection from direct string composition.
- **Cross-Site Scripting** - Escape or sanitize output shown in UI or HTML according to context, and avoid unsafe rendering without reason.
- **Authentication** - Ensure endpoints, routes, jobs, or actions that require identity verify it correctly.
- **Authorization** - Check access by resource and action; do not rely only on client-side checks or broad roles.
- **Secrets Management** - Do not hardcode, commit, log, or expose API keys, passwords, tokens, private keys, or credentials.
- **Sensitive Data Exposure** - Keep responses, events, analytics, telemetry, and logs from sending more personal or sensitive data than necessary.
- **Session and Token Safety** - Store, transmit, expire, refresh, and revoke tokens or sessions appropriately for the context.
- **CSRF and CORS** - Protect state-changing requests from CSRF when relevant and do not use overly broad CORS without justification.
- **Rate Limiting and Abuse Prevention** - Limit endpoints vulnerable to brute force, scraping, spam, or resource exhaustion.
- **Dependency Risk** - Review known vulnerabilities only when there is evidence such as a manifest, lockfile, audit output, advisory, or verifiable version.
- **Secure Defaults** - Production defaults should not enable debug mode, permissive permissions, public buckets, insecure transport, or unsafe features.

## Category 7: Database and Data Integrity

Check that database-related code preserves correctness, performance, and data-layer safety.

- **Schema Fit** - Schema, types, constraints, and nullable fields should match the domain rules used by the code.
- **Migration Safety** - Migrations should have a rollback or backward-compatible path when they affect existing data or rolling deployments.
- **Transaction Boundary** - Atomic work should be wrapped in an appropriate transaction, and external side effects should not happen inside the transaction unless justified.
- **Data Consistency** - Use unique constraints, foreign keys, optimistic locking, or idempotency when needed to prevent duplicates or conflicts.
- **Query Correctness** - Filters, joins, ordering, pagination, and aggregation should match intended behavior.
- **Query Performance** - Frequent or large-data queries should have appropriate indexes and avoid full scans, N+1 queries, or unbounded queries.
- **Pagination Semantics** - Pagination should use cursors or stable ordering when data can change between pages.
- **Connection and Resource Usage** - Use connection pools, timeouts, and cleanup appropriately; avoid opening duplicate connections unnecessarily.
- **Data Retention and Privacy** - Do not store more data than needed, and support retention, deletion, or anonymization when context requires it.
- **Seed Data Safety** - Seeds and fixtures must not mix with production data or create real credentials.

## Category 8: API Design

Check that APIs have clear contracts, consistent behavior, and safe client support.

- **Contract Clarity** - Request, response, error shape, and status codes should match the declared contract or project pattern.
- **HTTP Semantics** - Methods, status codes, headers, caching, and idempotency should match the operation.
- **Validation and Error Response** - APIs should validate input at the boundary and return actionable errors without internal details.
- **Backward Compatibility** - Changes should not break existing clients without migration, versioning, or deprecation guidance.
- **Response Minimality** - Responses should include only required fields that the caller is allowed to see.
- **Pagination, Filtering, Sorting** - Collection APIs should bound results and validate every query parameter.
- **Idempotency and Retry Safety** - Operations clients may retry should use idempotency keys or deduplication when needed.
- **Rate Limit and Quota Feedback** - APIs with quotas or limits should return feedback clients can use for retry or backoff decisions.
- **API Observability** - Request IDs, correlation IDs, or trace context should be propagated when relevant.

## Category 9: Accessibility

Check that UI and interactions are accessible to users with varied needs.

- **Semantic HTML** - Use meaningful elements such as `button` for actions, links for navigation, and headings in a logical order.
- **Keyboard Navigation** - Every interactive control should be reachable by keyboard with a reasonable focus order and no keyboard trap.
- **Accessible Name** - Icon buttons, inputs, form controls, and landmarks should have clear accessible names or labels.
- **ARIA Correctness** - Use ARIA only when needed, with correct roles, states, and properties; do not replace semantic HTML unnecessarily.
- **Color and Contrast** - Text, icons, and important states should have enough contrast and should not communicate by color alone.
- **Error and Form Feedback** - Validation errors should be connected to the relevant field and readable by screen readers.
- **Motion and Timing** - Animations or auto-updates should not disturb users and should respect reduced motion when frontend context is present.
- **Responsive and Zoom Support** - UI should work when zoom, font size, or viewport changes, without text overlap or overflow.

## Category 10: Observability and Operations

Check that code can be monitored, debugged, and operated when problems happen.

- **Structured Logging** - Logs should include searchable fields such as request_id, user_id without sensitive exposure, operation, status, and duration where appropriate.
- **Log Level Discipline** - Log levels should be correct, with no debug logs on production paths and no noisy repeated logs.
- **Metrics** - Important flows should expose metrics for throughput, latency, error rate, saturation, or relevant business events.
- **Tracing** - Async flows, external calls, or distributed requests should propagate trace or correlation context when needed.
- **Error Reporting** - Important exceptions should be reported with enough context to debug, without secrets or PII.
- **Health and Readiness** - Services or jobs should have health and readiness signals that reflect important dependencies.
- **Timeouts and Retries** - External calls should have timeouts, retries, backoff, and circuit breakers where appropriate, and should not retry unsafe operations without deduplication.
- **Operational Runbook Fit** - Error messages, alerts, and logs should help operations understand impact and remediation steps, not just show a stack trace.
- **Feature Flag and Rollout Safety** - High-risk changes should have rollout, rollback, or feature-flag support when context indicates the need.

## Output Format

Always present findings before the overview so the user sees risks that need decisions before reading supporting context.

### 1. Reviewed Scope

- **Scope** - List files, diff, modules, or system areas reviewed.
- **Evidence Used** - List code, configuration, logs, schema, contract, tests, or documents used.
- **Limitations** - State missing information that affects confidence, such as missing schema, missing caller context, or missing runtime logs.

### 2. Findings

Group findings by severity from Critical to Important, Improve, and Suggestion.

Use this format for each finding:

- **[Issue Name]**
  - **Severity** - State the severity.
  - **Category** - State the relevant category, such as correctness, security, database, API, accessibility, observability, performance, naming, or code quality.
  - **Location** - State path and line number when known.
  - **Problem** - Explain what is wrong or inappropriate.
  - **Impact** - Explain why it matters and how it affects the system.
  - **Evidence** - Cite the code path, diff, configuration, log, or other data supporting the finding.
  - **Fix** - Provide a concrete fix, with code examples when appropriate.
  - **Alternatives** - If there is more than one approach, summarize pros, cons, and what the user must decide.

If there are no findings, write: "ไม่พบประเด็นที่มีหลักฐานชัดเจนจากบริบทที่ให้มา" and state any remaining limitations that affect confidence.

### 3. Questions or Assumptions to Confirm

- List questions that need user confirmation when there is not enough information to decide.
- List assumptions used during review, without turning assumptions into findings unless evidence supports them.

### 4. Overview

- Briefly summarize what the reviewed code does and the overall risk level.
- Mention strengths only when they are supported by code evidence.
- Do not let the overview bury findings that need to be fixed.

### 5. Additional Recommendations

- Suggest additional features or improvements when useful and consistent with context.
- Keep additional recommendations separate from findings that are actual problems.
- Avoid out-of-scope suggestions unless the user explicitly asks for design or roadmap advice.

## Example Requests That Should Use This Skill

- "review PR นี้ให้หน่อย"
- "ตรวจโค้ดว่ามี bug หรือ security issue ไหม"
- "ช่วยดู diff นี้ก่อน merge"
- "โค้ดนี้ performance มีปัญหาอะไรหรือเปล่า"
- "ตรวจ API design และ error handling ให้หน่อย"
- "ช่วยเช็ค accessibility ของ component นี้"
- "ดู naming และ code quality ให้หน่อย"

## Usage Limitations

- Do not use this skill for writing new code from scratch unless the user also wants existing code evaluated or improved.
- Do not conclude dependency vulnerabilities without a manifest, lockfile, audit output, advisory, or verifiable version.
- Do not cite specific external standards without checking the latest official source when that standard may change.
- Do not guess business requirements, API contracts, or data models that are not visible in context.
