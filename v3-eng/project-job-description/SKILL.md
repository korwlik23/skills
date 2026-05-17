---
name: project-job-description
description: >
  Use this skill immediately when the user wants to analyze real project source
  code or a real codebase and turn the evidence into professional career
  content, such as a job description from a project, resume work experience,
  portfolio entry, career highlight, or technical accomplishment summary in
  recruiter-friendly Markdown. Always use this skill when the user asks to
  summarize a project from code, write resume material from a repository,
  explain what they built in a project, convert a codebase into a JD, create a
  portfolio entry from a real project, or asks to "look at the code and
  summarize what it does" even without saying resume or portfolio directly.
  The output must be grounded in code evidence and must not exaggerate beyond
  what the evidence supports.
---

# Project Job Description

## About

This skill is for reading real source code or a real codebase and converting what is found in the project into professional content that can be used immediately in a resume, portfolio, job description, career highlight, or technical accomplishment summary.

The main goal is to help the user communicate what they did in the project, what technologies they used, what features the system has, and how the work can be written in an interesting way. All claims must be grounded in evidence from real code and must not embellish beyond what is found.

The primary output must be recruiter-friendly Markdown with a clear structure, concise language, and an appropriate connection between technical details and professional impact.

## General Requirements

- Always respond in Thai, except for filenames, identifiers, keywords, code, libraries, frameworks, commands, or text that must remain unchanged as evidence.
- Use only information that can actually be inspected from source code, configuration, manifests, README files, schemas, routes, components, tests, commit context, or project files.
- If information is insufficient, state the limitation plainly and ask the user before summarizing anything that depends on context outside the code.
- When an issue depends on the version of a language, framework, library, runtime, or Markdown standard, look up the latest official source before concluding, and do not hard-code version numbers in this skill content.
- Keep all guidance in a single `SKILL.md` file. Do not split references, scripts, assets, or additional files.
- Write each point clearly, concisely, and with complete meaning on its own.
- Check and fix grammar in every response before sending so the text is readable, correct, and unambiguous.
- Do not claim that the user worked on a team, led a team, increased revenue, reduced costs, or achieved numeric results unless there is clear evidence from code or the user confirms it.

## Workflow

### 1. Define Project Scope

- Identify the repository, folder, module, or files in scope for analysis.
- Identify the output type the user wants, such as Job Description, resume work experience, portfolio entry, career highlight, or technical accomplishment summary.
- Identify the role that should be reflected from evidence, such as frontend developer, backend developer, full-stack developer, data engineer, DevOps engineer, or mobile developer.
- If the user does not specify a role, infer possible roles from the code and clearly state that the role is an inference from evidence.
- If scope is unclear, inspect the project structure first and state the assumptions used in the analysis.

### 2. Read and Understand the Codebase

- Inspect the file structure to identify framework, runtime, package manager, entry point, and important modules.
- Read manifests and configuration such as package files, lockfiles, build config, environment examples, routing config, or deployment config when present.
- Read the main source code to identify features, user flows, business logic, data flow, integrations, and architecture.
- Read schemas, migrations, models, API routes, service layers, components, and tests to find evidence supporting the career description.
- Separate what can be proven from code from what is only an inference.

### 3. Extract Evidence From Code

- Identify technologies actually used, such as languages, frameworks, libraries, databases, APIs, authentication, deployment, or testing tools.
- Identify features with clear evidence from route, component, service, model, or test files.
- Identify engineering responsibilities such as UI design, API creation, state management, database integration, validation, authentication, or performance improvement.
- Identify architecture patterns or design decisions only when there is evidence from code structure.
- Identify quality practices such as testing, linting, type safety, error handling, security controls, or observability when found in the project.
- Record important evidence locations as paths or filenames so the user can trace claims back to source.

### 4. Convert Evidence Into Career Content

- Write what the user did, not only what the project contains.
- Convert technical implementation into accomplishments that recruiters can understand.
- Use action verbs such as developed, designed, built, improved, integrated, managed, stabilized, or enhanced quality.
- Connect features to system value, such as helping users work faster, reducing steps, preventing mistakes, or making the system easier to maintain, only when evidence supports it.
- Avoid numeric impact claims unless there are metrics, benchmarks, analytics, test results, or user confirmation.
- Use honest, professional language without overselling.

### 5. Verify Accuracy Before Sending

- Check that every important claim has code evidence or is clearly labeled as an inference.
- Check that no technology, feature, or business outcome was added if it was not found in the project.
- Check that Markdown is readable, headings are clear, and bullets are not unnecessarily long.
- Check that Thai grammar is correct and sentences are not ambiguous or repetitive.
- Check that the content can be adapted to a resume, LinkedIn, or portfolio without major structural edits.

## Primary Output Format

Use the following Markdown structure by default and adapt it to the user's request.

### 1. Project Overview

- Briefly explain what the project is and what problem it solves.
- Identify the system type, such as web application, API service, dashboard, automation tool, mobile app, or data pipeline.
- Identify the user's role based on the evidence found or an assumption that still needs confirmation.

### 2. Technologies Found in the Code

- List languages, frameworks, libraries, databases, services, and tools that were actually found.
- Separate core technologies from supporting tools when that improves readability.
- Cite the evidence source as a file or brief context when that technology affects the career text.

### 3. Features and System Capabilities

- Summarize important features found from routes, components, services, models, schemas, or tests.
- Write features in recruiter-friendly language while keeping technical substance.
- State limitations when behavior cannot be confirmed from the available code.

### 4. Resume Work Experience

Write resume bullets using this structure:

- Start with a clear action verb.
- State what was developed, designed, or improved.
- State the technology or approach used when it adds useful weight.
- State the outcome or value only when evidence supports it.

Example patterns:

- Developed `[feature]` with `[technology]` so `[user/system]` can `[outcome]` clearly.
- Designed `[module/API/data flow]` for `[use case]` using `[architecture/library]` to improve structure and reduce code complexity.

### 5. Portfolio Entry

- Write a project name or descriptive title that reflects the work domain.
- Summarize the project problem or goal from the evidence found.
- Explain what the user built and the important system features.
- State the tech stack and technical rationale only as far as evidence supports.
- Close with a qualitative result that does not exceed what the code shows.

### 6. Job Description From the Project

- Convert what the user did into responsibilities that read like a real role.
- Include responsibilities that match the codebase, such as developing frontend, building backend APIs, designing data models, integrating services, or maintaining deployment.
- Include qualifications or skills that can be proven from technologies and project structure.
- Avoid inventing requirements that are not related to the real project.

### 7. Technical Accomplishment Summary

- Summarize technical work in a short paragraph readable by recruiters or hiring managers.
- Emphasize complexity only as much as the code demonstrates.
- State trade-offs or engineering decisions when there is evidence from architecture or implementation.
- State summary limitations when production data, user metrics, or business outcomes are unavailable.

### 8. Evidence Used

- List files or project areas used as evidence for important claims.
- State which claims are inferences from code structure, not confirmed facts.
- State what still needs to be asked from the user to make the content more credible.

## Writing Guidelines

- Use clear, professional language without fluff or overselling.
- Help recruiters understand the value of the work within the first few seconds.
- Balance technical depth with readability for non-engineer readers.
- Use short bullets with one central meaning per bullet.
- Use domain terms found in the real project instead of replacing them with overly broad words.
- Avoid generic wording such as "built a system", "managed data", or "developed software" when a feature or responsibility can be stated more specifically.
- Write "no evidence found" when information required for a claim is missing instead of filling in content.

## Evidence Rules

- Technology claims must come from dependencies, imports, configuration, file structure, or code usage actually found.
- Feature claims must come from routes, components, functions, services, schemas, tests, or UI text actually found.
- Performance claims must come from implementation, benchmarks, caching, indexing, lazy loading, or optimization actually found.
- Security claims must come from authentication, authorization, validation, sanitization, encryption, or secret handling actually found.
- Business impact claims must come only from metrics, documentation, analytics, user stories, or user confirmation.
- If evidence is ambiguous, use cautious phrasing such as "appears to", "from the code structure, it seems", or "should be confirmed further".

## Example Requests That Should Use This Skill

- "ช่วยสรุปโปรเจกต์นี้ใส่ resume ให้หน่อย"
- "อ่าน codebase แล้วเขียน work experience ให้หน่อย"
- "แปลงโปรเจกต์นี้เป็น portfolio entry"
- "ช่วยเขียน JD จากสิ่งที่ทำใน repo นี้"
- "ดูโค้ดแล้วบอกว่าฉันควรเขียน career highlight ยังไง"
- "สรุป technical accomplishment จากโปรเจกต์นี้เป็น Markdown"
- "ช่วยทำให้ recruiter เข้าใจว่าโปรเจกต์นี้น่าสนใจตรงไหน"

## Usage Limitations

- Do not use this skill for general job-description writing that is not grounded in source code or a real project.
- Do not use this skill for general resume rewriting unless codebase analysis is the main evidence.
- Do not invent work experience, job titles, companies, numeric outcomes, or business impact without evidence.
- Do not conclude that a project is deployed or has real users without configuration, documentation, or user confirmation.
- Do not rename technologies or features to sound larger than they are in a way that could mislead recruiters.
