---
name: database-performance
description: Principal database design — schema, queries, indexes, migrations, scaling, monitoring.
---

# Database Performance

## Core Rules

1. Schema mistakes are the most expensive to fix — get it right early.
2. Measure before optimizing — use EXPLAIN, query logs, profiling.
3. Indexes speed reads but slow writes — index deliberately.
4. Every query must be predictable at scale.
5. Enforce integrity at database level, not just application.

## Index Strategy

**Must index**: Foreign keys. WHERE columns on large tables. JOIN columns. ORDER BY with pagination. UNIQUE constraints.

**Composite rules**: Equality columns first, range columns last. Index `(a,b,c)` supports `(a)`, `(a,b)`, `(a,b,c)` — NOT `(b,c)`.

**Don't over-index**: Small tables (<1K rows). Boolean columns alone. Write-heavy columns. Every possible combination.

## EXPLAIN Red Flags

| Flag | Problem | Fix |
|------|---------|-----|
| `type: ALL` | Full table scan | Add index |
| High `rows` count | Scanning too many | Improve index |
| `Using filesort` | Sort not indexed | Add sort column to index |
| `Using temporary` | Temp table created | Optimize GROUP BY |
| Function on indexed column | Index bypassed | Keep column clean |

## Query Anti-Patterns

| Pattern | Fix |
|---------|-----|
| `SELECT *` large tables | Select needed columns |
| N+1 queries | Eager load / JOIN |
| Query in loop | Batch or single query |
| `LIKE '%term%'` | Full-text search |
| `ORDER BY RAND()` | App-level randomization |
| Unbounded SELECT | Always paginate |
| `OR` across columns | UNION or restructure |
| Implicit type coercion | Match types exactly |

## Schema Rules

**Naming**: `snake_case`. Plural tables. FK: `{singular}_id`. Booleans: `is_`/`has_`. Timestamps: `_at`.

**Types**: Smallest appropriate type. `UNSIGNED` for IDs. `DECIMAL` for money (never FLOAT). `UUID` for public IDs. `JSON` sparingly. `ENUM` only for truly fixed values.

**Relationships**: Explicit foreign keys with ON DELETE/UPDATE. CASCADE only when child meaningless without parent. `RESTRICT` when deletion should block. Define both ORM sides.

**Soft deletes**: Index `deleted_at`. Consider UNIQUE constraint impact. Archive old records periodically.

## Migration Rules

- [ ] Forward + rollback both work
- [ ] Nullable/defaults for new columns
- [ ] Existing data handled (data migration if needed)
- [ ] Table size considered (large table ALTER locks)
- [ ] Index names explicit
- [ ] FK ON DELETE/UPDATE defined
- [ ] No destructive changes without backup

**Safe practices**: Add nullable first → backfill → add NOT NULL. Create indexes concurrently. Test on production-size data. Never rename columns without deprecation period.

## Pagination

| Method | Use When |
|--------|----------|
| OFFSET/LIMIT | Small datasets, UI needs page numbers |
| Cursor-based | Large datasets, infinite scroll, APIs |
| Keyset | Large datasets with unique sort key |

## Connection Management

Connection pooling (5-20 per instance). Set connection + query timeouts. Handle failures with retry + backoff. Close on shutdown.

## Monitoring

Track: slow queries (>200ms), query count per request, connection pool utilization, table sizes, index usage, lock wait time, replication lag.

## Scaling

| Strategy | When | Complexity |
|----------|------|------------|
| Read replicas | Read-heavy | Medium |
| Redis cache | Repeated expensive queries | Medium |
| Partitioning | 100M+ rows | High |
| Archival | Old rarely-accessed data | Medium |
| Sharding | Extreme scale | Very High |

## Output Format

```
# Database Review
## Schema Issues — types, naming, constraints
## Query Issues — slow, N+1, unbounded
## Index Recommendations — missing, unused, composite (with EXPLAIN)
## Migration Risks — locking, data loss, rollback
## Data Integrity — FKs, orphans, constraint gaps
## Performance Metrics — current times, estimated improvement
## Scaling Concerns — growth, bottlenecks, strategies
## Action Plan — 1.Critical 2.Performance 3.Schema 4.Long-term
```
