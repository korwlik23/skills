# Documentation Templates

Load this file only when concrete documentation examples or section templates are needed.

## README Skeleton

````markdown
# Project Name

One sentence explaining what this project does and who it is for.

## Quick Start

1. Install dependencies:
   ```bash
   npm install
   ```
2. Configure environment:
   ```bash
   cp .env.example .env
   ```
3. Run the app:
   ```bash
   npm run dev
   ```

## Features

- **Feature name** - User-facing value in one sentence.

## Tech Stack

| Layer | Technology | Notes |
|-------|------------|-------|
| Runtime | Node.js 20+ | Required |

## Project Structure

```text
src/
  routes/      Request/page entry points
  services/    Business logic
  tests/       Automated tests
```

## Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start local development |
| `npm test` | Run tests |
````

## Environment Example

```env
# App
APP_ENV=local
APP_URL=http://localhost:3000

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/app

# Auth
JWT_SECRET=change-this-to-a-random-32-plus-character-secret

# Optional integrations
# GOOGLE_CLIENT_ID=
# GOOGLE_CLIENT_SECRET=
```

Use dummy values only. Add comments for format, minimum length, and whether a value is required.

## API Endpoint Pattern

````markdown
### `POST /api/resources`

Creates a resource.

**Auth:** Required  
**Permission:** `resources:create`

#### Request

```json
{
  "name": "Example"
}
```

#### Response `201`

```json
{
  "id": "res_123",
  "name": "Example",
  "created_at": "2026-05-06T00:00:00Z"
}
```

#### Errors

| Status | Meaning |
|--------|---------|
| 400 | Invalid request body |
| 401 | Missing or invalid authentication |
| 403 | Authenticated but not allowed |
````

## Architecture Diagram Pattern

```mermaid
flowchart LR
  User["User"] --> App["Web/App Server"]
  App --> DB["Database"]
  App --> Queue["Queue Worker"]
  App --> External["External Service"]
```

Pair diagrams with short notes on ownership, failure behavior, and operational concerns.

## Changelog Entry Pattern

```markdown
## 2026-05-06

### Added
- New user-visible capability.

### Changed
- Behavior that existing users should know about.

### Fixed
- Defect fixed and impact.

### Migration Notes
- Required commands, rollback notes, and compatibility concerns.
```

## Verification Checklist

- [ ] Commands match package scripts or documented tooling.
- [ ] Links resolve.
- [ ] Examples use sanitized data.
- [ ] Env vars are documented with required/optional status.
- [ ] API examples match actual response shape.
- [ ] Markdown renders cleanly.
