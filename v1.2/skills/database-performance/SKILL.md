---
name: database-performance
description: >
  Use this skill for database schema review, slow queries, index strategy,
  migrations, relationships, data integrity, scaling, and performance
  optimization. Triggers on requests about SQL, EXPLAIN, N+1 queries,
  indexes, schema design, pagination, connection pooling, query optimization,
  table design, or any database-related performance concern.
---

# Database Performance Skill

Use this skill for database schema review, slow queries, migrations, indexes, relationships, data integrity, scaling, and performance optimization.

## Production-Grade Operating Contract

- Before starting, read `../../RULES.md` when available and apply it as the behavior, safety, validation, and communication baseline.
- If shared rules are unavailable, treat schema/data changes as high risk, avoid destructive operations without explicit confirmation, validate with realistic data assumptions, and report only verified results.
- Use this skill for database technical depth; do not let it override user instructions, repository guidance, or data-integrity constraints.
- Keep responses proportional. Use the output format for database reviews/plans; use a concise summary for small query or migration changes.

## Core Principles

1. The database is the foundation — schema mistakes are the most expensive to fix.
2. Measure before optimizing — use EXPLAIN, query logs, and profiling.
3. Indexes are not free — they speed reads but slow writes.
4. Every query should be predictable — no surprises at scale.
5. Data integrity is non-negotiable — enforce at the database level, not just application.

## Index Strategy

### Must Index

- Foreign keys — always.
- Columns in WHERE clauses with large tables.
- Columns used in JOIN conditions.
- Columns used in ORDER BY with pagination.
- Columns used in UNIQUE constraints.
- Composite indexes matching actual query patterns (left-prefix rule).

### Don't Over-Index

- Tables that are small relative to the working set rarely benefit from non-primary indexes; confirm with `EXPLAIN` on production-like data rather than assuming a fixed row count.
- Boolean columns alone — low cardinality makes indexes ineffective.
- Columns that are written far more than read.
- Every possible column combination — maintain only what queries actually use.

### Composite Index Rules

- Column order matters — put equality conditions first, range conditions last.
- A composite index on `(a, b, c)` supports queries on `(a)`, `(a, b)`, `(a, b, c)` but NOT `(b, c)`.
- Include SELECT columns in the index for covering index optimization.

## Query Optimization

### Analysis Process

1. **Identify** — Find slow queries via query log, APM, or `EXPLAIN`.
2. **Measure** — Get current execution time and row scans.
3. **Analyze** — Run `EXPLAIN ANALYZE` to see actual execution plan.
4. **Optimize** — Apply fixes (index, rewrite, restructure).
5. **Verify** — Confirm improvement with same analysis.

### EXPLAIN Red Flags

| Flag | Meaning | Fix |
|------|---------|-----|
| `type: ALL` | Full table scan | Add index |
| `rows:` very high | Scanning too many rows | Add/improve index |
| `Extra: Using filesort` | Sorting not using index | Add sorted column to index |
| `Extra: Using temporary` | Temp table created | Optimize GROUP BY/ORDER BY |
| `Extra: Using where` with high rows | Filtering after scan | Improve index selectivity |
| No index used | Missing index | Create appropriate index |

### Query Anti-Patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| `SELECT *` on large tables | Wastes memory/bandwidth | Select only needed columns |
| N+1 queries | Multiplied latency | Eager load / JOIN |
| Query in loop | Unbounded query count | Batch or single query |
| `LIKE '%term%'` | Cannot use index | Full-text search or search engine |
| `ORDER BY RAND()` | Full table scan + sort | Application-level randomization |
| `COUNT(*)` on huge tables | Slow on InnoDB | Use cached counters |
| Unbounded `SELECT` | Memory/timeout | Always paginate |
| `OR` across columns | Often prevents index use | UNION or restructure |
| Functions on indexed columns | Index bypassed | Rewrite to keep column clean |
| Implicit type coercion | Index bypassed | Match types exactly |

## Schema Design Rules

### Naming

- Use `snake_case` for tables and columns.
- Use plural table names: `users`, `orders`, `order_items`.
- Foreign keys: `{singular_table}_id` — e.g., `user_id`, `order_id`.
- Boolean columns: `is_` or `has_` prefix — `is_active`, `has_verified`.
- Timestamp columns: `_at` suffix — `created_at`, `deleted_at`.

### Data Types

- Use the smallest appropriate type — `TINYINT` vs `INT`, `VARCHAR(100)` vs `TEXT`.
- Use `UNSIGNED` for IDs and counters.
- Use `DECIMAL` for money — never `FLOAT` or `DOUBLE`.
- Use `TIMESTAMP` or `DATETIME` consistently — be timezone-aware.
- Use `UUID` for public-facing IDs, auto-increment for internal.
- Use `JSON` columns sparingly — they can't be indexed traditionally.
- Use `ENUM` only for truly fixed values — prefer lookup tables for changing lists.

### Relationships

- Define foreign keys explicitly with ON DELETE/UPDATE behavior.
- Use cascading deletes only when child data has no meaning without parent.
- Use `SET NULL` when child should survive parent deletion.
- Use `RESTRICT` when deletion should be blocked if children exist.
- Always define both sides of a relationship in ORM.

### Soft Deletes

- Add `deleted_at` index for frequently queried tables.
- Consider the impact on UNIQUE constraints — partial indexes or composite uniqueness.
- Periodically archive/purge old soft-deleted records.

## Migration Rules

For every migration, verify:

- [ ] Forward migration works correctly.
- [ ] Rollback migration works correctly.
- [ ] Nullable/default values are set for new columns.
- [ ] Existing data is handled (data migration if needed).
- [ ] Production table size considered — large table ALTER can lock.
- [ ] Locking risk assessed — use online DDL tools for large tables.
- [ ] Index names are explicit and descriptive.
- [ ] Foreign key behavior (ON DELETE/UPDATE) is defined.
- [ ] No destructive changes without backup verification.
- [ ] Migration is idempotent where possible.

### Safe Migration Practices

- Add columns as nullable first, backfill, then add NOT NULL if needed.
- Create indexes concurrently when supported (`CREATE INDEX CONCURRENTLY`).
- For large tables, consider pt-online-schema-change or gh-ost.
- Never rename columns in production without a deprecation period.
- Test migrations against production-size data before deploying.

> Full schema-change safety matrix and universal rules: `references/migration-safety.md`
> (the pack-wide canonical source — `deployment-devops` and `migration-upgrade` defer to it).

## Pagination Strategy

| Method | Pros | Cons | Use When |
|--------|------|------|----------|
| `OFFSET/LIMIT` | Simple, supports page numbers | Slow on large offsets | Small datasets, UI needs page numbers |
| `Cursor-based` | Consistent performance | No page numbers, forward-only | Large datasets, infinite scroll, APIs |
| `Keyset` | Fast, consistent | Complex for multi-column sort | Large datasets with unique sort key |

## Connection Management

- Use connection pooling — never open a new connection per request.
- Size the pool to the workload and the database's max-connections budget across all instances; measure under realistic load instead of assuming a fixed number.
- Set connection timeout — don't wait forever.
- Set query timeout — kill runaway queries.
- Handle connection failures gracefully — retry with backoff.
- Close connections on application shutdown.

## Monitoring & Alerting

Track these metrics in production:

- **Slow query log** — queries exceeding threshold (e.g., > 200ms).
- **Query count per request** — detect N+1 patterns.
- **Connection pool utilization** — detect exhaustion before it happens.
- **Table sizes** — track growth for capacity planning.
- **Index usage** — identify unused indexes (wasted write overhead).
- **Lock wait time** — detect contention.
- **Replication lag** — if using read replicas.

## Scaling Strategies

| Strategy | When | Complexity |
|----------|------|------------|
| Read replicas | Read-heavy workload | Medium |
| Caching layer (Redis) | Repeated expensive queries | Medium |
| Table partitioning | Very large tables (100M+ rows) | High |
| Vertical scaling | Quick fix, hitting limits | Low |
| Sharding | Extreme scale, multi-tenant | Very High |
| Archival | Historical data rarely accessed | Medium |

## L5 Acceptance Gates

- Query recommendations are tied to observed access patterns, expected cardinality, and realistic data volume.
- Migration plans include lock/downtime risk, rollback or forward-fix path, and data validation.
- Index recommendations consider read speed, write cost, storage cost, and query planner behavior.
- Data integrity is enforced with constraints where practical, not only application logic.
- Performance claims are backed by EXPLAIN, timings, metrics, or clearly marked assumptions.

## Output Format

```markdown
# Database Review

## Schema Issues
Data type problems, naming inconsistencies, missing constraints.

## Query Issues
Slow queries, N+1 patterns, unbounded operations.

## Index Recommendations
Missing indexes, unused indexes, composite index suggestions.
Include EXPLAIN analysis where relevant.

## Migration Risks
Locking risk, data loss risk, rollback concerns.

## Data Integrity Risks
Missing foreign keys, orphaned records, constraint gaps.

## Performance Metrics
Current query times, estimated improvement, before/after EXPLAIN.

## Scaling Concerns
Growth projections, bottleneck predictions, recommended strategies.

## Prioritized Action Plan
1. Critical fixes (data integrity, production failures)
2. Performance wins (index additions, query rewrites)
3. Schema improvements (naming, types, constraints)
4. Long-term optimizations (partitioning, caching, archival)
```

## Example Trigger Phrases

- "This query is slow"
- "Review database schema"
- "Add indexes for this table"
- "Optimize this query"
- "Review migration safety"
- "Check for N+1 queries"
- "Design schema for this feature"
- "How should I paginate this?"
- "Review data integrity"

## Usage Limitations

- Do not use this skill for application logic — use `backend-architecture` instead.
- Do not run destructive queries (DROP, TRUNCATE, DELETE) without explicit confirmation.
- Do not assume table sizes or data distribution without EXPLAIN or metrics evidence.
- Do not recommend indexes without considering write cost and actual query patterns.
- Do not modify production data or schema without backup verification.
