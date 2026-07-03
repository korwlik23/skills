# Git Hooks Setup & .gitignore Essentials Reference

Loaded on demand by the `git-workflow` skill. Tool-specific setup snippets and a sample
`.gitignore`. The skill's SKILL.md keeps the conceptual hook policy and best-practice
rules; this file holds the concrete copy-paste blocks (per the conciseness clause).

## Setup with Husky (Node.js)

```bash
npx husky init
echo "npx lint-staged" > .husky/pre-commit
echo "npx commitlint --edit \$1" > .husky/commit-msg
```

## lint-staged Configuration

```json
{
  "*.{js,ts,jsx,tsx}": ["eslint --fix", "prettier --write"],
  "*.{css,scss}": ["prettier --write"],
  "*.md": ["prettier --write"]
}
```

## .gitignore Essentials

```gitignore
# Dependencies
node_modules/
vendor/

# Build output
.next/
dist/
build/

# Environment
.env
.env.local
.env.production

# IDE
.idea/
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*

# Testing
coverage/

# Generated
*.lock  # Only if not using lockfile pinning
```

> Tooling commands/flags change between versions — confirm against current official
> Husky/lint-staged docs per `../../../../RULES.md` §10.
