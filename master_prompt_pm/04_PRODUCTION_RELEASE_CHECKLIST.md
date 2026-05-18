# 04_PRODUCTION_RELEASE_CHECKLIST.md
# Production Release Checklist / Deploy Runbook / Post-Deploy Smoke Test

เอกสารนี้ใช้หลังจากผ่าน `03_FINAL_GO_LIVE_REVIEW_PROMPT.md` แล้ว และผลลัพธ์เป็น:

- `Go`
- หรือ `Go with Conditions` ที่เคลียร์เงื่อนไขสำคัญครบแล้ว

เป้าหมายของไฟล์นี้คือใช้เป็น Checklist ก่อนกด Deploy Production จริง  
ใช้ได้กับทุกโปรเจกต์ เช่น Laravel, Next.js, Nuxt, Svelte, Node.js, SaaS, API, Dashboard, Mobile API Backend, Accounting SaaS, E-commerce, Community Platform

---

## 0. Release Information

กรอกข้อมูลรอบ release นี้ก่อนเริ่ม deploy

```txt
Project Name:
Environment:
Release Version:
Release Branch:
Release Tag:
Commit Hash:
Release Date:
Release Owner:
Reviewer:
Deploy Window:
Expected Downtime:
Rollback Owner:
```

---

## 1. Pre-Release Gate

ก่อนทำ production release ต้องผ่านเงื่อนไขนี้

```md
- [ ] ผ่าน 01_MASTER_PROJECT_AUDIT_PROMPT.md แล้ว
- [ ] ผ่าน 01_1_MASTER_RE_AUDIT.md แล้ว
- [ ] ผ่าน 02_FULL_MASTER_QA_TESTING_PROMPT.md แล้ว
- [ ] ผ่าน 03_FINAL_GO_LIVE_REVIEW_PROMPT.md แล้ว
- [ ] Final Decision เป็น Go หรือ Go with Conditions
- [ ] ไม่มี Blocker เหลืออยู่
- [ ] ไม่มี Critical issue เหลืออยู่
- [ ] ไม่มี High issue ที่กระทบ Security / Permission / Tenant / Payment / Transaction / Data Integrity
- [ ] Known issues ที่เหลือถูกยอมรับแล้ว
- [ ] มี rollback plan
- [ ] มี backup plan
- [ ] มี post-deploy monitoring plan
```

ถ้าข้อใดข้อหนึ่งไม่ผ่าน ให้หยุด release และกลับไปแก้ก่อน

---

## 2. Risk Acceptance Before Deploy

ใช้ section นี้เพื่อบันทึก issue ที่ยังเหลือแต่ยอมรับได้

| Issue ID | Severity | Area | Risk | Reason Accepted | Mitigation | Owner |
|---|---|---|---|---|---|---|
| | | | | | | |

ห้ามปล่อย production ถ้า issue ที่เหลือเป็น:

- Blocker
- Critical
- High ด้าน Security
- High ด้าน Permission / Role
- High ด้าน Tenant Isolation
- High ด้าน Payment / Subscription
- High ด้าน Transaction / Accounting / Report
- High ด้าน Data Integrity
- High ด้านข้อมูลรั่ว / cross-tenant leak

---

## 3. Backup Checklist

ต้องทำก่อน deploy เสมอ โดยเฉพาะระบบที่มีข้อมูลผู้ใช้จริง

### 3.1 Database Backup

```md
- [ ] Backup database production แล้ว
- [ ] ตรวจว่า backup file ถูกสร้างจริง
- [ ] ตรวจขนาดไฟล์ backup สมเหตุสมผล
- [ ] เก็บ backup ไว้ในที่ปลอดภัย
- [ ] ระบุ path / location ของ backup
- [ ] ระบุเวลาที่ backup
- [ ] ระบุคนที่รับผิดชอบ backup
```

บันทึกข้อมูล:

```txt
Database Backup File:
Backup Location:
Backup Time:
Backup Owner:
Restore Command / Method:
```

### 3.2 Uploaded Files / Storage Backup

ถ้าระบบมี upload, receipt, slip, image, document, report export ให้ทำ backup storage ด้วย

```md
- [ ] Backup uploaded files แล้ว
- [ ] Backup public/private storage แล้ว
- [ ] Backup tenant/store files ถ้ามี
- [ ] ตรวจว่า file permission ไม่เสียหลัง backup
- [ ] มีวิธี restore file กลับ
```

```txt
Storage Backup Location:
Storage Backup Time:
Storage Backup Owner:
```

### 3.3 Config / Env Backup

```md
- [ ] Backup `.env` production เดิมแล้ว
- [ ] Backup nginx/apache config แล้ว ถ้ามีการแก้
- [ ] Backup supervisor/pm2 config แล้ว ถ้ามีการแก้
- [ ] Backup cron config แล้ว ถ้ามีการแก้
- [ ] Backup deployment script แล้ว ถ้ามีการแก้
```

---

## 4. Production Environment Checklist

### 4.1 General Config

```md
- [ ] `APP_ENV=production`
- [ ] `APP_DEBUG=false`
- [ ] App key / secret ถูกต้อง
- [ ] Timezone ถูกต้อง
- [ ] Locale ถูกต้อง
- [ ] Production URL ถูกต้อง
- [ ] Domain / subdomain ถูกต้อง
- [ ] HTTPS ใช้งานได้
- [ ] CORS ถูกต้อง
- [ ] Cookie domain ถูกต้อง
- [ ] Session config ถูกต้อง
- [ ] Cache driver ถูกต้อง
- [ ] Queue driver ถูกต้อง
- [ ] Mail config ถูกต้อง ถ้ามี
- [ ] Storage disk ถูกต้อง
- [ ] Log channel ถูกต้อง
- [ ] Error reporting ไม่เปิดเผยข้อมูล sensitive
```

### 4.2 Secrets / API Keys

```md
- [ ] ไม่มี secret อยู่ใน git
- [ ] ไม่มี API key อยู่ใน frontend bundle
- [ ] ไม่มี token อยู่ใน log
- [ ] Payment key เป็น production key หรือ sandbox key ตามที่ตั้งใจ
- [ ] AI/OCR key ถูกต้อง
- [ ] LINE / webhook / external API key ถูกต้อง
- [ ] OAuth callback URL เป็น production URL
- [ ] Webhook URL เป็น production URL
- [ ] Secret rotation plan มีหรือไม่จำเป็น
```

### 4.3 Laravel-specific Checklist

ใช้ถ้าโปรเจกต์เป็น Laravel

```md
- [ ] `composer install --no-dev --optimize-autoloader` พร้อม
- [ ] `.env` production ถูกต้อง
- [ ] `php artisan key:generate` ไม่ถูกรันซ้ำทับ production key โดยไม่ตั้งใจ
- [ ] `php artisan migrate --force` พร้อม
- [ ] ตรวจ migration ก่อนรันจริง
- [ ] `php artisan config:cache` พร้อม
- [ ] `php artisan route:cache` พร้อม ถ้า route ไม่มี closure ที่ทำให้พัง
- [ ] `php artisan view:cache` พร้อม
- [ ] `php artisan storage:link` ตรวจแล้ว
- [ ] `storage/` writable
- [ ] `bootstrap/cache/` writable
- [ ] Queue worker / Supervisor พร้อม
- [ ] Scheduler / cron พร้อม
- [ ] Laravel log writable
- [ ] `APP_DEBUG=false`
```

### 4.4 Node / Next / Nuxt / Svelte Checklist

ใช้ถ้าโปรเจกต์มี frontend build หรือ Node app

```md
- [ ] Node version ถูกต้อง
- [ ] Package manager ถูกต้อง เช่น npm / pnpm / yarn
- [ ] Lock file commit แล้ว
- [ ] `npm ci` หรือ install แบบ production พร้อม
- [ ] Build ผ่าน
- [ ] Environment variable ฝั่ง build ถูกต้อง
- [ ] Public env ไม่มี secret
- [ ] Static asset path ถูกต้อง
- [ ] SSR/SPA routing ถูกต้อง
- [ ] PM2/systemd process พร้อม ถ้ามี
- [ ] Reverse proxy ไป port ถูกต้อง
```

---

## 5. Database / Migration Checklist

ก่อนรัน migration ต้องตรวจละเอียด

```md
- [ ] ตรวจ migration ที่จะรันแล้ว
- [ ] ไม่มี migration ที่ drop column/table โดยไม่ backup
- [ ] ไม่มี migration ที่แก้ข้อมูลจำนวนมากโดยไม่มีแผน rollback
- [ ] Foreign key ถูกต้อง
- [ ] Index สำคัญพร้อม
- [ ] Default value ถูกต้อง
- [ ] Nullable ถูกต้อง
- [ ] Decimal สำหรับเงินถูกต้อง
- [ ] Enum/status ไม่ทำให้ข้อมูลเก่าพัง
- [ ] Seed ที่จะรัน production-safe
- [ ] มี rollback plan สำหรับ migration
- [ ] มี database backup ก่อน migrate
```

บันทึก migration ที่จะรัน:

| Migration | Risk | Rollback Plan | Notes |
|---|---|---|---|
| | | | |

---

## 6. Build Checklist

```md
- [ ] Pull code จาก branch/tag ที่ถูกต้อง
- [ ] Dependency install ผ่าน
- [ ] Frontend build ผ่าน
- [ ] Backend build/optimize ผ่าน ถ้ามี
- [ ] Static assets ถูกสร้าง
- [ ] Manifest ถูกสร้าง ถ้าใช้ Vite/Mix
- [ ] ไม่มี build warning ร้ายแรง
- [ ] ไม่มี secret หลุดใน generated assets
- [ ] Version/release tag ถูกต้อง
```

บันทึก:

```txt
Build Command:
Build Result:
Build Artifact Path:
```

---

## 7. Server / Infrastructure Checklist

```md
- [ ] Server CPU/RAM เพียงพอ
- [ ] Disk space เพียงพอ
- [ ] Swap พร้อม ถ้าจำเป็น
- [ ] Web server running
- [ ] PHP-FPM / Node / App runtime running
- [ ] Database running
- [ ] Redis/cache running ถ้ามี
- [ ] Queue worker running ถ้ามี
- [ ] Scheduler/cron running ถ้ามี
- [ ] SSL certificate valid
- [ ] SSL auto-renew พร้อม
- [ ] Firewall เปิดเฉพาะ port ที่จำเป็น
- [ ] File permission ถูกต้อง
- [ ] Log rotation มีหรือมีแผน
```

คำสั่งตัวอย่างที่ควรตรวจบน Linux:

```bash
df -h
free -h
uptime
systemctl status nginx
systemctl status php*-fpm
systemctl status mysql
systemctl status redis
systemctl status supervisor
crontab -l
```

---

## 8. Security Checklist Before Deploy

```md
- [ ] Protected routes ต้อง login
- [ ] Admin routes มี middleware/policy
- [ ] API routes มี auth/rate limit ตามความเหมาะสม
- [ ] CSRF เปิดใช้กับ web form
- [ ] CORS ไม่เปิดกว้างเกินไป
- [ ] Cookie secure/httpOnly/SameSite เหมาะสม
- [ ] Debug mode ปิด
- [ ] Error page ไม่โชว์ stack trace
- [ ] SQL injection risk สำคัญถูกตรวจแล้ว
- [ ] XSS risk สำคัญถูกตรวจแล้ว
- [ ] IDOR risk สำคัญถูกตรวจแล้ว
- [ ] Mass assignment ป้องกันแล้ว
- [ ] File upload validate type/size/path แล้ว
- [ ] Webhook verify signature แล้ว ถ้ามี
- [ ] Payment amount ไม่เชื่อจาก client
- [ ] Tenant isolation ผ่านแล้ว
- [ ] Secrets ไม่หลุด
```

---

## 9. Feature-specific Release Checklist

เลือกเฉพาะส่วนที่โปรเจกต์มี

### 9.1 Auth / User / Role

```md
- [ ] Login ได้
- [ ] Logout ได้
- [ ] Register ได้ ถ้ามี
- [ ] Reset password ได้ ถ้ามี
- [ ] User role ถูกต้อง
- [ ] Permission ถูกต้อง
- [ ] Admin เข้าได้เฉพาะส่วนที่ควรเข้า
- [ ] User เข้า admin ไม่ได้
- [ ] API auth ถูกต้อง
```

### 9.2 Multi-tenant / Store / Organization

```md
- [ ] Tenant A ไม่เห็นข้อมูล Tenant B
- [ ] User ผูก tenant ถูกต้อง
- [ ] Admin ร้าน A ไม่เห็นร้าน B
- [ ] Tenant switching ถูกต้อง
- [ ] Report แยก tenant ถูกต้อง
- [ ] File upload แยก tenant ถูกต้อง
- [ ] Cache key แยก tenant แล้ว
- [ ] Package/subscription ผูก tenant ถูกต้อง
```

### 9.3 Payment / Subscription

```md
- [ ] Payment provider production config ถูกต้อง
- [ ] Webhook production URL ถูกต้อง
- [ ] Webhook signature verify
- [ ] Payment success flow ผ่าน
- [ ] Payment failed flow ผ่าน
- [ ] Duplicate webhook ไม่ทำให้ข้อมูลซ้ำ
- [ ] Subscription activate ถูกต้อง
- [ ] Expired/cancelled status ถูกต้อง
- [ ] Package limit enforce ทั้ง frontend/backend
- [ ] Invoice/receipt/VAT ถูกต้อง ถ้ามี
```

### 9.4 Transaction / Accounting / Report

```md
- [ ] Create transaction ถูกต้อง
- [ ] Update transaction ถูกต้อง
- [ ] Delete/void/cancel ถูกต้อง
- [ ] Draft ไม่ถูกนับเป็นยอดจริง
- [ ] Confirm draft แล้วนับยอดจริง
- [ ] Duplicate submit ไม่ทำให้ยอดซ้ำ
- [ ] Amount decimal ถูกต้อง
- [ ] Report/dashboard ตรงกับข้อมูลจริง
- [ ] Export ตรงกับข้อมูลจริง
- [ ] Audit log สำคัญครบ
```

### 9.5 File Upload / AI / OCR

```md
- [ ] File type validation
- [ ] File size validation
- [ ] Upload บน mobile ผ่าน
- [ ] Upload path ปลอดภัย
- [ ] Private file ไม่เปิดสาธารณะผิด
- [ ] OCR/AI timeout handling
- [ ] OCR/AI fail handling
- [ ] AI response validate ก่อนบันทึก
- [ ] AI สร้าง draft ไม่บันทึกจริงทันที
- [ ] User confirm ก่อน create จริง
- [ ] API key ไม่หลุด
- [ ] Cost/rate limit มีแผน
```

### 9.6 Notification / Email / LINE / Webhook

```md
- [ ] Notification ส่งถูกคน
- [ ] Notification ไม่ซ้ำ
- [ ] Email template ถูกต้อง
- [ ] LINE message ถูก context
- [ ] Webhook log พร้อม
- [ ] Failed notification มี retry/log
- [ ] Link ใน notification เป็น production URL
```

---

## 10. Deploy Execution Checklist

ใช้ขณะ deploy จริง

### 10.1 Before Maintenance / Deploy

```md
- [ ] แจ้งทีม/ผู้เกี่ยวข้องก่อน deploy
- [ ] เลือก deploy window แล้ว
- [ ] Backup database แล้ว
- [ ] Backup storage/config แล้ว
- [ ] Confirm release branch/tag
- [ ] Confirm rollback commit/tag
- [ ] Confirm migration plan
- [ ] Confirm smoke test plan
```

### 10.2 Deployment Steps

ปรับ command ให้เข้ากับโปรเจกต์จริง

#### Laravel Example

```bash
cd /path/to/project
git fetch --all
git checkout main
git pull origin main

composer install --no-dev --optimize-autoloader

npm ci
npm run build

php artisan down

php artisan migrate --force
php artisan config:cache
php artisan route:cache
php artisan view:cache

php artisan queue:restart

php artisan up
```

Checklist:

```md
- [ ] Pull code สำเร็จ
- [ ] Composer install สำเร็จ
- [ ] NPM install/build สำเร็จ
- [ ] Maintenance mode เปิดถ้าจำเป็น
- [ ] Migration สำเร็จ
- [ ] Cache config/route/view สำเร็จ
- [ ] Queue restart สำเร็จ
- [ ] Maintenance mode ปิด
- [ ] Web server reload/restart ถ้าจำเป็น
```

#### Node / Frontend Example

```bash
cd /path/to/project
git fetch --all
git checkout main
git pull origin main

npm ci
npm run build

pm2 restart app-name
# or systemctl restart app-name
```

Checklist:

```md
- [ ] Pull code สำเร็จ
- [ ] Install dependency สำเร็จ
- [ ] Build สำเร็จ
- [ ] Process restart สำเร็จ
- [ ] Reverse proxy ยังทำงาน
```

---

## 11. Post-Deploy Smoke Test

ต้องทำทันทีหลัง deploy

### 11.1 Application Smoke Test

```md
- [ ] หน้าแรกเปิดได้
- [ ] Login ได้
- [ ] Logout ได้
- [ ] Dashboard โหลดได้
- [ ] Navigation หลักใช้งานได้
- [ ] ไม่มี 500 error
- [ ] ไม่มี console error ร้ายแรง
- [ ] Static assets โหลดครบ
- [ ] CSS/JS ไม่ 404
- [ ] Mobile view หลักไม่แตก
```

### 11.2 Core Feature Smoke Test

```md
- [ ] Create ข้อมูลหลักได้
- [ ] Update ข้อมูลหลักได้
- [ ] Delete/archive ข้อมูลหลักได้
- [ ] Search/filter หลักได้
- [ ] Report/dashboard หลักถูกต้อง
- [ ] API หลักตอบกลับถูกต้อง
```

### 11.3 Security Smoke Test

```md
- [ ] Protected page เข้าโดยไม่ login ไม่ได้
- [ ] User ไม่มีสิทธิ์เข้า admin ไม่ได้
- [ ] Admin access ยังถูกต้อง
- [ ] Tenant A ไม่เห็น Tenant B ในเคสหลัก
- [ ] API protected ยังต้อง auth
```

### 11.4 Payment / Subscription Smoke Test

ใช้ถ้าระบบมี payment/subscription

```md
- [ ] Payment page เปิดได้
- [ ] Webhook endpoint reachable
- [ ] Webhook log ทำงาน
- [ ] Subscription status แสดงถูกต้อง
- [ ] Package limit ทำงาน
```

### 11.5 Upload / AI / OCR Smoke Test

ใช้ถ้าระบบมี upload/AI/OCR

```md
- [ ] Upload file ได้
- [ ] Preview file ได้
- [ ] AI/OCR draft ทำงาน
- [ ] User confirm draft ได้
- [ ] Error handling ใช้งานได้ถ้า AI/OCR fail
```

---

## 12. Rollback Checklist

ใช้ถ้า deploy แล้วพบปัญหาร้ายแรง

### 12.1 Rollback Trigger

Rollback ทันทีถ้าเจอ:

- Login ใช้ไม่ได้
- ระบบ 500 ใน flow หลัก
- Payment ผิด
- Transaction/ยอดเงินผิด
- Tenant isolation พัง
- ข้อมูลรั่ว
- Migration ทำข้อมูลเสียหาย
- Queue/webhook ทำงานผิดจนกระทบข้อมูล
- Bug ระดับ Critical ที่กระทบ user จริง

### 12.2 Rollback Steps

```md
- [ ] ประกาศหยุด/maintenance ถ้าจำเป็น
- [ ] หยุด queue worker ถ้าอาจทำข้อมูลเสียหาย
- [ ] Checkout commit/tag ก่อนหน้า
- [ ] Restore dependency/build artifact ถ้ามี
- [ ] Rollback migration หรือ restore DB ตามแผน
- [ ] Restore config/env ถ้ามีการเปลี่ยน
- [ ] Restart app/web server/worker
- [ ] Smoke test หลัง rollback
- [ ] ตรวจ log ว่าระบบกลับมาปกติ
- [ ] บันทึก incident report
```

บันทึก:

```txt
Rollback Commit/Tag:
Rollback Started At:
Rollback Completed At:
Rollback Owner:
Incident Summary:
```

---

## 13. Monitoring Checklist

### 13.1 First 30 Minutes

```md
- [ ] ตรวจ error log
- [ ] ตรวจ web server log
- [ ] ตรวจ application log
- [ ] ตรวจ queue failed jobs
- [ ] ตรวจ CPU/RAM/Disk
- [ ] ตรวจ login flow
- [ ] ตรวจ dashboard
- [ ] ตรวจ feature หลัก
- [ ] ตรวจ payment/webhook ถ้ามี
- [ ] ตรวจ transaction/report ถ้ามี
- [ ] ตรวจ upload/AI/OCR ถ้ามี
```

### 13.2 First 24 Hours

```md
- [ ] ตรวจ error trend
- [ ] ตรวจ slow request
- [ ] ตรวจ failed job
- [ ] ตรวจ user feedback
- [ ] ตรวจ database growth
- [ ] ตรวจ disk usage
- [ ] ตรวจ payment mismatch ถ้ามี
- [ ] ตรวจ report/dashboard accuracy ถ้ามี
- [ ] ตรวจ notification/email/LINE delivery ถ้ามี
```

### 13.3 First 72 Hours

```md
- [ ] สรุป incident/bug ที่พบ
- [ ] จัด priority hotfix
- [ ] ตรวจ performance
- [ ] ตรวจ cost external API/AI ถ้ามี
- [ ] ตรวจ backup หลัง deploy
- [ ] ตรวจ cron/scheduler หลายรอบ
- [ ] อัปเดต release note / known issues
```

---

## 14. Incident Report Template

ใช้ถ้าเกิดปัญหาหลัง deploy

```md
# Incident Report

## Summary

## Severity
Critical / High / Medium / Low

## Timeline
- Detected At:
- Mitigated At:
- Resolved At:

## Impact
- Users affected:
- Features affected:
- Data affected:
- Financial impact:

## Root Cause

## Temporary Fix

## Permanent Fix

## Rollback Required?
Yes / No

## Prevention

## Follow-up Tasks
- [ ] ...
```

---

## 15. Final Release Sign-off

กรอกหลัง deploy และ smoke test ผ่าน

```md
- [ ] Deploy completed
- [ ] Smoke test passed
- [ ] No critical error after deploy
- [ ] Monitoring started
- [ ] Rollback no longer immediately required
- [ ] Release note updated
- [ ] Known issues recorded
- [ ] Team/user communication completed if needed
```

```txt
Release Status: Success / Rolled Back / Partial / Monitoring
Signed off by:
Signed off at:
Notes:
```

---

## 16. Quick Command Notes

บันทึกคำสั่งที่ใช้บ่อยของโปรเจกต์นี้

```bash
# project path
cd /path/to/project

# pull latest
git pull origin main

# install backend dependencies
composer install --no-dev --optimize-autoloader

# install frontend dependencies
npm ci

# build frontend
npm run build

# migrate
php artisan migrate --force

# clear/cache
php artisan optimize:clear
php artisan config:cache
php artisan route:cache
php artisan view:cache

# queue
php artisan queue:restart

# logs
tail -f storage/logs/laravel.log

# system
df -h
free -h
systemctl status nginx
systemctl status php*-fpm
```

---

## 17. Notes

ใช้พื้นที่นี้จดสิ่งที่ต้องจำเฉพาะโปรเจกต์

```md
- 
- 
- 
```
