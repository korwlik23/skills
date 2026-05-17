# Migration Safety — Canonical Reference

Single source of truth for schema/data migration safety across the pack. The
`database-performance`, `deployment-devops`, and `migration-upgrade` skills reference
this instead of restating it, so the guidance cannot drift between skills.

## Schema-change safety matrix

| Change | Zero-downtime safe? | Safe strategy |
|--------|--------------------|---------------|
| Add column (nullable) | ✅ | Direct migration |
| Add column (NOT NULL) | ⚠️ | Add nullable → backfill → then add NOT NULL/constraint |
| Remove column | ⚠️ | Stop reading it in code first → deploy → then drop |
| Rename column | ❌ (as a single step) | Add new → copy data → deploy code using new → remove old |
| Add index | ✅ | `CREATE INDEX CONCURRENTLY` (or pt-online-schema-change / gh-ost on large tables) |
| Change column type | ⚠️ | Depends on data size and conversion; often add-new-column pattern |
| Drop table | ⚠️ | Remove all code references first, deploy, then drop |

## Universal rules (apply to every migration)

1. Forward **and** rollback paths both work and are tested.
2. Back up before any destructive or irreversible change; verify the backup.
3. Test against production-size data, not just dev data.
4. Make migrations idempotent where possible (safe to run twice).
5. Measure migration time on realistic data — will it lock or cause downtime?
6. Large-table `ALTER` can lock — use online DDL tools for large tables.
7. Never rename/drop in production without a deprecation/transition period where old
   and new coexist.
8. Validate after migrating: row counts, checksums, spot checks.
9. Keep old data accessible during the transition; have a data rollback plan.

## Higher-risk data migrations (beyond simple schema changes)

| Type | Risk | Strategy |
|------|------|----------|
| Change data format | Medium | Migration script, tested on a copy of prod data |
| Merge / split tables | High | Multi-step migration with backward compatibility |
| Move to a new database | Very High | Dual-write period → verify parity → cutover |
