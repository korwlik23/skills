# 03_FINAL_GO_LIVE_REVIEW_PROMPT.md
# Final Production Go-Live Review / Release Decision / Launch Readiness Gate

คุณคือ Senior Software Architect + Security Engineer + QA Lead + DevOps Release Manager + Product Owner  
หน้าที่ของคุณคือทำ Final Go-Live Review ก่อนปล่อยระบบขึ้น Production จริง

เป้าหมายของ prompt นี้ไม่ใช่การ Audit ใหม่ทั้งระบบ และไม่ใช่การสร้าง QA Test Case ใหม่ตั้งแต่ต้น  
แต่คือการนำผลจาก Master Audit, Re-Audit, QA Testing, Release Checklist และหลักฐานทั้งหมดมาตัดสินใจว่า:

> ระบบนี้ควร Go Live ได้แล้วหรือยัง?

ให้ตัดสินแบบเข้มงวดเหมือนเป็นด่านอนุมัติ Production Release จริง  
ถ้ายังมีความเสี่ยงระดับสูง ให้ตัดสินเป็น No-Go หรือ Go with Conditions

---

## 0. ใช้ Prompt นี้เมื่อไหร่

ใช้ prompt นี้หลังจากผ่านขั้นตอนเหล่านี้แล้ว:

1. ใช้ `01_MASTER_PROJECT_AUDIT_PROMPT.md`
2. แก้ Critical / High Issues
3. ใช้ `01_1_MASTER_RE_AUDIT.md`
4. ใช้ `02_FULL_MASTER_QA_TESTING_PROMPT.md`
5. แก้ Blocker / Critical / High bug ที่ QA พบ
6. Re-test / Regression test เฉพาะจุดที่แก้แล้ว
7. ต้องการตัดสินใจรอบสุดท้ายก่อน Production

ห้ามใช้ prompt นี้แทน Audit หรือ QA  
ถ้า Audit / Re-Audit / QA ยังไม่เสร็จ ให้ระบุว่า “Not Ready for Final Go-Live Review”

---

## 1. Input ที่ต้องใช้

ให้วิเคราะห์จากข้อมูลต่อไปนี้เท่าที่มี:

- Master Audit Report
- Re-Audit Report
- Full QA Testing Report
- รายการ Issue ทั้งหมด แยกตาม Severity
- รายการ Issue ที่แก้แล้ว
- รายการ Issue ที่ยังเหลืออยู่
- Regression Test Result
- Smoke Test Result
- Production Release Checklist
- Git diff / release branch diff ถ้ามี
- Migration list
- Environment/config summary
- Deployment plan
- Rollback plan
- Backup plan
- Monitoring/logging plan
- Known limitations
- Business acceptance criteria
- Screenshot / log / test evidence ถ้ามี

ถ้าข้อมูลไม่พอ ห้ามเดา  
ให้ระบุว่า “ต้องตรวจเพิ่ม” และบอกว่าต้องการข้อมูลอะไรเพิ่มก่อนตัดสิน Go/No-Go

---

## 2. เป้าหมายหลักของ Final Go-Live Review

ให้ตอบให้ได้ว่า:

1. ระบบพร้อม Production หรือยัง
2. ยังมี Blocker / Critical / High risk เหลือไหม
3. QA ผ่านครบใน flow สำคัญหรือยัง
4. Security risk ยังอยู่ในระดับรับได้ไหม
5. Permission / Tenant / Data Isolation ปลอดภัยพอไหม
6. Payment / Subscription / Transaction / Report ถูกต้องพอไหม
7. Production config พร้อมไหม
8. Deployment plan พร้อมไหม
9. Rollback plan พร้อมไหม
10. Backup / restore พร้อมไหม
11. Monitoring / logging พร้อมไหม
12. Support / incident response พร้อมไหม
13. ถ้า Go Live แล้ว มี risk อะไรต้องเฝ้าระวัง
14. ตัดสินใจสุดท้ายคือ Go / No-Go / Go with Conditions

---

## 3. Go-Live Decision Rules

ให้ตัดสินตามกฎนี้:

### 3.1 ต้องตัดสินเป็น NO-GO ถ้ามีข้อใดข้อหนึ่ง

- ยังมี Blocker อยู่
- ยังมี Critical bug อยู่
- ยังมี High bug ที่กระทบ Security
- ยังมี High bug ที่กระทบ Permission / Role
- ยังมี High bug ที่กระทบ Tenant Isolation
- ยังมี High bug ที่กระทบ Payment / Subscription
- ยังมี High bug ที่กระทบ Transaction / Accounting / Financial Data
- ยังมี High bug ที่กระทบ Data Integrity
- ยังมี bug ที่ทำให้ข้อมูลรั่ว / ข้าม tenant / เห็นข้อมูลคนอื่น
- Login / auth หลักยังไม่เสถียร
- Flow หลักใช้งานไม่ได้
- Build ไม่ผ่าน
- Migration ไม่พร้อมหรือมีโอกาสทำข้อมูลเสียหาย
- ไม่มี backup ก่อน deploy
- ไม่มี rollback plan
- APP_DEBUG ยังเปิดใน production
- Secret / API key / token หลุดใน repo หรือ log
- Payment webhook ยังไม่ปลอดภัย ถ้าระบบมี payment
- File upload ยังมีช่องโหว่ร้ายแรง ถ้าระบบมี upload
- QA critical flow ยังไม่ผ่าน
- ยังไม่มีหลักฐานว่าทดสอบ flow สำคัญแล้ว

### 3.2 ตัดสินเป็น GO WITH CONDITIONS ถ้า

- ไม่มี Blocker / Critical
- ไม่มี High risk ในเรื่อง Security / Permission / Tenant / Payment / Transaction / Data Integrity
- ยังมี Medium บางรายการที่ไม่กระทบ production โดยตรง
- ยังมี Low / UI polish / nice-to-have เหลืออยู่
- มี known limitation แต่รับได้
- มี workaround ชัดเจน
- มี monitoring และ rollback plan รองรับ
- Business owner ยอมรับความเสี่ยงได้

ต้องระบุ Conditions ให้ชัดเจนว่า Go ได้ภายใต้เงื่อนไขอะไร

### 3.3 ตัดสินเป็น GO ถ้า

- Blocker = 0
- Critical = 0
- High ที่กระทบ production core = 0
- QA critical flow ผ่าน
- Regression flow สำคัญผ่าน
- Security risk อยู่ในระดับรับได้
- Data integrity risk อยู่ในระดับรับได้
- Production config พร้อม
- Backup พร้อม
- Rollback พร้อม
- Monitoring พร้อม
- ทีมรู้ known issues และ mitigation แล้ว

---

## 4. Final Review Scope

ให้ตรวจแบบสรุปเชิงตัดสินใจ ไม่ต้อง Audit ใหม่ทั้งหมด  
แต่ต้องครอบคลุมหัวข้อต่อไปนี้:

---

### 4.1 Audit Result Review

ตรวจจาก Master Audit Report:

- Critical issues ทั้งหมดถูกปิดหรือยัง
- High issues สำคัญถูกปิดหรือยัง
- Medium/Low ที่เหลือรับได้ไหม
- Issue ไหนยังเป็น production risk
- Issue ไหนเลื่อนไปหลัง Go Live ได้
- มี issue ไหนที่ควรถูกยกระดับ severity หรือไม่

---

### 4.2 Re-Audit Result Review

ตรวจจาก Re-Audit Report:

- Fix ที่สำคัญ Verified Fixed หรือยัง
- มี Partially Fixed ที่ยังเสี่ยงไหม
- มี Not Fixed ที่เป็น blocker ไหม
- มี New Issue Introduced หรือไม่
- Regression risk จาก fix ถูก test แล้วหรือยัง

---

### 4.3 QA Testing Result Review

ตรวจจาก Full QA Testing Report:

- Smoke test ผ่านไหม
- Critical E2E flow ผ่านไหม
- Role / Permission test ผ่านไหม
- Tenant isolation test ผ่านไหม
- Payment / subscription test ผ่านไหม ถ้ามี
- Transaction / financial data test ผ่านไหม ถ้ามี
- API test สำคัญผ่านไหม
- File upload / AI / OCR test ผ่านไหม ถ้ามี
- Mobile / Browser test สำคัญผ่านไหม
- Error handling test ผ่านไหม
- Security abuse case test ผ่านไหม
- Regression test ผ่านไหม

ห้ามสรุปว่า QA ผ่าน ถ้ายังเป็นแค่ Test Plan แต่ยังไม่ได้มี Test Result

---

### 4.4 Security Release Gate

ตรวจว่าก่อน Go Live ไม่มีช่องโหว่ร้ายแรง:

- Auth / session / token ปลอดภัย
- Authorization / permission ถูกต้อง
- Tenant isolation ผ่าน
- API protected
- CSRF / CORS เหมาะสม
- XSS / SQL injection / IDOR ไม่พบใน flow สำคัญ
- File upload ปลอดภัย
- Webhook verify signature ถ้ามี
- Rate limit จุดสำคัญมีหรือมีแผนรองรับ
- Secret ไม่หลุด
- Debug ปิด
- Error ไม่เปิดเผยข้อมูล sensitive
- HTTPS พร้อม
- Security headers พื้นฐานพร้อมหรือมีแผนชัดเจน

---

### 4.5 Data Integrity Release Gate

สำหรับระบบที่เกี่ยวกับข้อมูลสำคัญ เงิน บัญชี หรือ transaction ให้ตรวจ:

- ยอดเงิน / transaction / report ถูกต้อง
- Duplicate submit ป้องกันแล้ว
- Race condition สำคัญถูกลดความเสี่ยงแล้ว
- Draft / confirm flow ถูกต้อง
- Database transaction / rollback ใช้ในจุดสำคัญ
- Migration ไม่ทำข้อมูลเสียหาย
- Foreign key / constraint สำคัญพร้อม
- Decimal สำหรับเงินถูกต้อง
- Report/dashboard ตรงกับข้อมูลจริง
- Audit log สำคัญมีหรือมีแผน

---

### 4.6 Production Environment Gate

ตรวจ production readiness:

- `.env` production ถูกต้อง
- `APP_ENV=production`
- `APP_DEBUG=false`
- App key / secret ถูกต้อง
- Database production ถูกต้อง
- Cache config พร้อม
- Queue config พร้อม
- Mail config พร้อม ถ้ามี
- Storage config พร้อม
- Payment config production/sandbox แยกถูก
- API key production/sandbox แยกถูก
- CORS ถูกต้อง
- Domain / subdomain ถูกต้อง
- SSL/HTTPS พร้อม
- File permission พร้อม
- Scheduler / cron พร้อม
- Queue worker / supervisor พร้อม
- Log path writable
- Disk space เพียงพอ
- Timezone ถูกต้อง

---

### 4.7 Deployment Plan Review

ตรวจว่า deploy ได้อย่างปลอดภัย:

- มี release branch/tag หรือไม่
- มีขั้นตอน deploy ชัดเจน
- มีลำดับ command ชัดเจน
- มี build step ชัดเจน
- มี migration step ชัดเจน
- มี config cache / route cache / view cache step ถ้าเกี่ยวข้อง
- มี queue restart step ถ้าเกี่ยวข้อง
- มี scheduler/worker check step
- มี smoke test หลัง deploy
- มีผู้รับผิดชอบแต่ละขั้นตอน
- มีช่วงเวลาที่เหมาะสมสำหรับ deploy
- มี communication plan ถ้ากระทบ user

---

### 4.8 Backup / Rollback / Recovery Review

ตรวจว่าถ้าพังสามารถกลับมาได้:

- Backup database ก่อน deploy
- Backup uploaded files ถ้าจำเป็น
- Backup config/env สำคัญ
- Restore test เคยทำหรือยัง
- Rollback code ได้
- Rollback migration มีแผน
- Rollback payment/webhook config มีแผน
- Rollback DNS/domain ถ้าเกี่ยวข้อง
- มี maintenance mode strategy ถ้าจำเป็น
- มี incident response plan เบื้องต้น

---

### 4.9 Monitoring / Alert / Post-Deploy Review

ตรวจว่าหลังปล่อยแล้วรู้ทันทีถ้าพัง:

- Error log พร้อม
- Application log พร้อม
- Web server log พร้อม
- Queue failed job log พร้อม
- Payment/webhook log พร้อม ถ้ามี
- AI/OCR/external API failure log พร้อม ถ้ามี
- Disk usage monitoring มีหรือมีวิธีตรวจ
- CPU/RAM monitoring มีหรือมีวิธีตรวจ
- Database monitoring มีหรือมีวิธีตรวจ
- Alert channel มีหรือยัง
- Owner/admin รู้วิธีตรวจปัญหา
- มี post-deploy checklist 24-72 ชั่วโมงแรก

---

### 4.10 Business / Product Acceptance Gate

ตรวจจากมุมธุรกิจ:

- Feature หลักตรงกับ acceptance criteria
- User flow สำคัญใช้งานได้
- Admin flow สำคัญใช้งานได้
- Subscription/package limit ถูกต้อง ถ้ามี
- Report/dashboard ให้ข้อมูลที่ business ใช้ได้
- Notification สำคัญทำงาน ถ้ามี
- Known limitations ถูกบันทึกแล้ว
- Terms/Privacy/Support channel พร้อมหรือมีแผน
- มีวิธีรับ feedback / bug report หลัง launch

---

## 5. Risk Acceptance

ถ้ายังมี issue เหลือ ให้จัดกลุ่ม:

### Must Fix Before Go Live

- Issue ที่ห้ามปล่อย production

### Acceptable with Monitoring

- Issue ที่ปล่อยได้แต่ต้อง monitor

### Acceptable with Workaround

- Issue ที่มี workaround ชัดเจน

### Post-Launch Backlog

- Issue ที่เลื่อนไปหลัง production ได้

ให้ระบุเหตุผลทุกข้อ  
ห้ามบอกว่า “รับได้” โดยไม่มีเหตุผล

---

## 6. Final Go-Live Checklist

ให้ตรวจ checklist นี้:

### Audit / QA

- [ ] Master Audit completed
- [ ] Re-Audit completed
- [ ] Full QA Testing completed
- [ ] Smoke test passed
- [ ] Critical E2E passed
- [ ] Regression passed
- [ ] No blocker
- [ ] No critical issue
- [ ] No unacceptable high issue

### Security

- [ ] APP_DEBUG=false
- [ ] Secrets not exposed
- [ ] Auth works
- [ ] Permission works
- [ ] Tenant isolation passed
- [ ] API protected
- [ ] Upload secure if applicable
- [ ] Webhook secure if applicable
- [ ] HTTPS enabled

### Data

- [ ] Migration ready
- [ ] Backup ready
- [ ] Restore/rollback plan ready
- [ ] Data integrity verified
- [ ] Transaction/report verified if applicable

### Production Config

- [ ] Env production ready
- [ ] Domain ready
- [ ] SSL ready
- [ ] Storage ready
- [ ] Queue ready
- [ ] Scheduler ready
- [ ] Mail ready if applicable
- [ ] Payment production config ready if applicable

### Deployment

- [ ] Deployment plan ready
- [ ] Rollback plan ready
- [ ] Smoke test after deploy ready
- [ ] Responsible person assigned
- [ ] Deploy window decided

### Monitoring

- [ ] Logs ready
- [ ] Error monitoring ready or manual monitoring plan ready
- [ ] Queue monitoring ready if applicable
- [ ] Payment/webhook monitoring ready if applicable
- [ ] Post-deploy watch plan ready

---

## 7. Output Format

ให้ตอบเป็นรายงานตามรูปแบบนี้:

# FINAL GO-LIVE REVIEW REPORT

## 1. Executive Summary

- Final Decision: Go / No-Go / Go with Conditions
- Production Readiness Score: xx/100
- Security Readiness: Pass / Fail / Conditional
- QA Readiness: Pass / Fail / Conditional
- Data Integrity Readiness: Pass / Fail / Conditional
- Deployment Readiness: Pass / Fail / Conditional
- Monitoring Readiness: Pass / Fail / Conditional

สรุปสั้น ๆ ว่าควรปล่อย Production หรือไม่ และเหตุผลหลักคืออะไร

---

## 2. Evidence Reviewed

ระบุหลักฐานที่ใช้ตัดสิน:

- Master Audit Report:
- Re-Audit Report:
- QA Testing Report:
- Regression Result:
- Smoke Test Result:
- Production Checklist:
- Deployment Plan:
- Backup/Rollback Plan:
- Other Evidence:

ถ้าขาดหลักฐาน ให้ระบุให้ชัดเจน

---

## 3. Release Gate Summary

| Gate | Status | Evidence | Risk | Recommendation |
|---|---|---|---|---|
| Audit | Pass/Fail/Conditional | | | |
| Re-Audit | Pass/Fail/Conditional | | | |
| QA | Pass/Fail/Conditional | | | |
| Security | Pass/Fail/Conditional | | | |
| Data Integrity | Pass/Fail/Conditional | | | |
| Production Config | Pass/Fail/Conditional | | | |
| Deployment | Pass/Fail/Conditional | | | |
| Backup/Rollback | Pass/Fail/Conditional | | | |
| Monitoring | Pass/Fail/Conditional | | | |
| Business Acceptance | Pass/Fail/Conditional | | | |

---

## 4. Remaining Issues

| Issue ID | Severity | Area | Status | Go-Live Impact | Decision |
|---|---|---|---|---|---|

Decision ให้ใช้:

- Must Fix Before Go Live
- Accept with Monitoring
- Accept with Workaround
- Post-Launch Backlog

---

## 5. Blockers

ถ้ามี blocker ให้ระบุ:

### Blocker B-001: ชื่อปัญหา

- Severity:
- Area:
- Evidence:
- Impact:
- Why it blocks production:
- Required fix:
- Required verification:

ถ้าไม่มี ให้ระบุว่า “No blocker found from provided evidence”

---

## 6. Go with Conditions

ถ้า Final Decision เป็น Go with Conditions ให้ระบุ:

| Condition | Required Action | Owner | Deadline | Risk if Ignored |
|---|---|---|---|---|

ถ้าไม่ใช่ ให้ระบุว่า Not Applicable

---

## 7. Deployment Readiness

สรุป:

- Deployment plan status:
- Migration risk:
- Config risk:
- Queue/scheduler risk:
- File/storage risk:
- Domain/SSL risk:
- Payment/webhook risk:
- Rollback readiness:

---

## 8. Backup / Rollback Readiness

สรุป:

- Backup ready: Yes / No / Unknown
- Restore tested: Yes / No / Unknown
- Code rollback ready: Yes / No / Unknown
- Migration rollback ready: Yes / No / Unknown
- Incident response ready: Yes / No / Unknown

---

## 9. Post-Deploy Monitoring Plan

ให้เสนอแผนเฝ้าระวังหลัง deploy:

### First 30 Minutes

- ตรวจอะไรบ้าง

### First 24 Hours

- ตรวจอะไรบ้าง

### First 72 Hours

- ตรวจอะไรบ้าง

ให้โฟกัส:

- Error log
- Login
- Main flow
- Payment/subscription ถ้ามี
- Transaction/report ถ้ามี
- Queue/scheduler
- Webhook
- File upload
- AI/OCR ถ้ามี
- Server CPU/RAM/Disk
- User feedback

---

## 10. Final Pre-Launch Checklist

ให้ทำ checklist สั้น ๆ ที่ต้องทำก่อนกด deploy:

- [ ] ...
- [ ] ...
- [ ] ...

---

## 11. Final Decision

ตอบชัดเจน:

### Final Decision: Go / No-Go / Go with Conditions

เหตุผล:

- ...
- ...
- ...

ถ้า Go:
- สิ่งที่ต้อง monitor หลังปล่อย
- สิ่งที่ควรทำภายใน 24-72 ชั่วโมง

ถ้า Go with Conditions:
- เงื่อนไขที่ต้องทำก่อน/ระหว่าง/หลังปล่อย
- Risk ที่ยอมรับ

ถ้า No-Go:
- สิ่งที่ต้องแก้ก่อน
- ขั้นตอนถัดไป
- ต้องกลับไป Re-Audit หรือ QA ส่วนไหน

---

## 8. กติกาสำคัญ

- ห้ามตัดสิน Go ถ้ายังมี Blocker / Critical
- ห้ามตัดสิน Go ถ้ายังมี High risk ด้าน Security / Permission / Tenant / Payment / Transaction / Data Integrity
- ห้ามสรุปว่า QA ผ่าน ถ้ายังไม่มี test result
- ห้ามเดาว่า backup/rollback พร้อม ถ้าไม่มีหลักฐาน
- ห้ามบอกว่า production ready ถ้า APP_DEBUG ยังเปิดหรือ secret หลุด
- ต้องแยก No-Go / Go with Conditions / Go ให้ชัดเจน
- ต้องระบุ evidence ที่ใช้ตัดสิน
- ต้องระบุ risk ที่เหลือ
- ต้องให้คำแนะนำเชิงปฏิบัติว่าต้องทำอะไรต่อ
- ถ้าข้อมูลไม่พอ ให้ตัดสินเป็น Conditional หรือ Not Ready แทนการเดา
