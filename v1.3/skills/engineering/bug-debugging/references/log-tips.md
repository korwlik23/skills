# Log Analysis Tips Reference

Loaded on demand by the `bug-debugging` skill. What to search for in logs, log-reading
patterns, and framework-specific log-access commands. Pulled out of `SKILL.md` per the
conciseness clause; load this file when you have logs in hand and need to extract
signal.

## What to Search in Logs

```
1. Timestamp matching the reported incident time
2. User ID or session ID of the affected user
3. Request URL and method
4. Error level (ERROR, CRITICAL, FATAL)
5. Stack trace
6. Related request/response data
7. Previous requests from same user (context)
```

## Log Reading Patterns

| Log Entry | Interpretation |
|-----------|---------------|
| Same error × many times | Systematic issue, not one-off |
| Error after deploy | Deployment introduced the bug |
| Error at specific time daily | Scheduled job/cron issue |
| Error from specific user only | Data-specific or permission issue |
| Error intermittent | Race condition, timeout, or external service |
| Error spike then stops | Temporary issue (deploy, service restart) |
| Growing error count | Resource leak, scaling issue |

## Laravel Log Tips

```bash
# View latest errors
tail -f storage/logs/laravel.log

# Search for specific error
grep -n "SQLSTATE" storage/logs/laravel.log

# Filter by date
grep "2024-01-15" storage/logs/laravel.log | grep "ERROR"

# Count errors by type
grep "ERROR" storage/logs/laravel.log | awk -F: '{print $4}' | sort | uniq -c | sort -rn
```

## Node.js Log Tips

```bash
# View PM2 logs
pm2 logs --lines 100

# Search for errors
pm2 logs --err

# Filter by timestamp
grep "2024-01-15" ~/.pm2/logs/app-error.log
```

> File paths and tooling vary by project. Confirm against the actual log paths the
> project uses (check the framework config and the process manager).
