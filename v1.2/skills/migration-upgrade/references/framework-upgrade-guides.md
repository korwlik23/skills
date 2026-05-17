# Framework-Specific Upgrade Guides Reference

Loaded on demand by the `migration-upgrade` skill. Version-agnostic per-framework
upgrade checklists and common breaking-change areas. The skill's SKILL.md keeps the
framework-agnostic upgrade process; this file holds the per-framework specifics.

> Per `../../../RULES.md` §10, always read the framework's official upgrade guide for
> the *actual* source and target versions before acting; do not assume version-specific
> steps from this file.

### Laravel Upgrade

```
1. Read https://laravel.com/docs/[version]/upgrade
2. Update composer.json version constraints
3. composer update
4. Fix breaking changes:
   - Check removed/renamed classes
   - Check changed method signatures
   - Check config file changes (diff with fresh install)
   - Check middleware changes
   - Check routing changes
5. Run: php artisan config:clear && route:clear && view:clear && cache:clear
6. Run tests
7. Check for deprecations: php artisan about
```

#### Laravel Common Breaking Changes

| Area | What to Check |
|------|---------------|
| PHP version | Minimum PHP version requirement |
| Config files | Diff against fresh install configs |
| Middleware | New default middleware, changed signatures |
| Routes | Route method changes, parameter handling |
| Eloquent | Relationship method changes, cast changes |
| Auth | Guard changes, session handling |
| Validation | New/changed rules, error format |
| Queue | Job serialization, retry behavior |
| Testing | TestCase changes, assertion methods |

### Next.js Upgrade

```
1. Read https://nextjs.org/docs/upgrading
2. npx @next/codemod upgrade (automated migration)
3. Update next, react, react-dom versions
4. Fix breaking changes:
   - Check App Router changes
   - Check Server Component defaults
   - Check API route changes
   - Check middleware changes
   - Check config (next.config.js) changes
5. npm run build — fix any build errors
6. Test all pages and API routes
```

#### Next.js Common Breaking Changes

| Area | What to Check |
|------|---------------|
| React version | Minimum React version, new features/deprecations |
| Routing | App Router changes, dynamic routes |
| Data fetching | fetch caching defaults, revalidation |
| Server Components | Default component type, 'use client' requirements |
| API Routes | Route handler signature changes |
| Middleware | Matcher changes, response handling |
| Config | next.config.js structure, experimental flags |
| Build | Output format, static/dynamic rendering |

### Svelte/SvelteKit Upgrade

```
1. Read migration guide on svelte.dev
2. npx svelte-migrate (if available)
3. Update svelte, @sveltejs/kit versions
4. Fix breaking changes:
   - Check component API changes
   - Check store API changes
   - Check routing changes
   - Check load function changes
5. Build and test
```

### Node.js Version Upgrade

```
1. Check Node.js changelog for breaking changes
2. Check all dependencies support new Node version
3. Update .nvmrc / .node-version / engines in package.json
4. Update CI/CD pipeline Node version
5. Update Docker base image
6. Test: npm ci && npm run build && npm test
7. Check for deprecated API usage (--pending-deprecation flag)
```
