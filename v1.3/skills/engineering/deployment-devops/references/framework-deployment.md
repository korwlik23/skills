# Framework-Specific Deployment Reference

Loaded on demand by the `deployment-devops` skill. Framework-specific deploy commands
and production config. The skill's SKILL.md keeps the framework-agnostic rules; this
file holds the concrete per-framework material (per the conciseness clause).

## Laravel Deployment Checklist

```bash
# Install production dependencies
composer install --no-dev --optimize-autoloader

# Cache configuration
php artisan config:cache
php artisan route:cache
php artisan view:cache
php artisan event:cache

# Run migrations
php artisan migrate --force

# Restart queue workers
php artisan queue:restart

# Verify
php artisan about
```

### Laravel Production Config

- `APP_DEBUG=false`
- `APP_ENV=production`
- Correct `APP_URL`
- Correct filesystem disk configuration
- Session driver (database/redis, not file for multi-server)
- Cache driver (redis, not file for multi-server)
- Queue connection (redis/database, not sync)
- Log channel (stack with daily rotation)
- Mail driver configured and tested
- Storage link created

## Node.js / Next.js Deployment

```bash
# Install production dependencies
npm ci --production

# Build
npm run build

# Start with process manager
pm2 start ecosystem.config.js --env production
# or
node server.js
```

### Node.js Production Config

- `NODE_ENV=production`
- Process manager (PM2, systemd) for restart on crash
- Cluster mode for multi-core utilization
- Memory limits set
- Graceful shutdown handling
- Health check endpoint

> Version-specific commands/flags change — confirm against the framework's current
> official deployment docs per `../../../../RULES.md` §10.
