# 00_PRODUCTION_WORKFLOW_GUIDE.md
# ลำดับการใช้งาน Prompt ก่อนขึ้น Production + เงื่อนไขการใช้แต่ละไฟล์

เอกสารนี้คือ “คู่มือหลัก” สำหรับใช้ชุด Prompt ก่อนขึ้น Production  
ใช้เพื่อบอกว่าแต่ละไฟล์ต้องใช้ตอนไหน ใช้อย่างไร และต้องผ่านเงื่อนไขอะไรถึงจะไปไฟล์ถัดไปได้

ชุดไฟล์ทั้งหมด:

```txt
00_PRODUCTION_WORKFLOW_GUIDE.md
01_MASTER_PROJECT_AUDIT_PROMPT.md
01_1_MASTER_RE_AUDIT.md
02_FULL_MASTER_QA_TESTING_PROMPT.md
03_FINAL_GO_LIVE_REVIEW_PROMPT.md
04_PRODUCTION_RELEASE_CHECKLIST.md
05_POST_DEPLOY_MONITORING_PROMPT.md
```

---

## 1. ภาพรวม Workflow ทั้งหมด

ลำดับใช้งานมาตรฐาน:

```txt
00 Read Workflow Guide
↓
01 Master Project Audit
↓
Fix Critical / High Issues
↓
01_1 Master Re-Audit
↓
02 Full Master QA Testing
↓
Fix QA Bugs + Regression Test
↓
03 Final Go-Live Review
↓
04 Production Release Checklist
↓
Deploy Production
↓
05 Post-Deploy Monitoring
```

สรุปหน้าที่แต่ละไฟล์:

| File | ใช้ทำอะไร | ใช้เมื่อไหร่ |
|---|---|---|
| 00 | คู่มือลำดับและเงื่อนไข | อ่านก่อนเริ่มทุกครั้ง |
| 01 | Audit ใหญ่ทั้งระบบ | ก่อนแก้/ก่อนเตรียม Production |
| 01_1 | ตรวจว่าที่แก้ไปถูกไหม | หลังแก้ issue จาก audit หรือ QA |
| 02 | QA/Test ทั้งระบบ | หลัง audit/re-audit ผ่าน |
| 03 | ตัดสิน Go / No-Go | หลัง QA ผ่าน |
| 04 | Checklist ตอน deploy จริง | หลัง 03 เป็น Go หรือ Go with Conditions |
| 05 | Monitor หลัง deploy | หลังขึ้น Production แล้ว |

---

## 2. 00_PRODUCTION_WORKFLOW_GUIDE.md

### ใช้ทำอะไร

ใช้เป็นคู่มือหลักในการจัดลำดับงานทั้งหมดก่อนขึ้น Production

### ใช้เมื่อไหร่

- ก่อนเริ่ม Audit
- ก่อนส่งงานให้ AI agent
- ก่อนจะตัดสินใจว่าจะใช้ prompt ไฟล์ไหนต่อ
- เมื่อทีมเริ่มสับสนว่า “ตอนนี้ควรทำอะไรต่อ”

### Output ที่ต้องได้

- รู้ว่าต้องใช้ไฟล์ไหนต่อ
- รู้ว่าเงื่อนไขผ่าน/ไม่ผ่านคืออะไร
- รู้ว่าถ้าเจอ bug ต้องย้อนกลับไปไฟล์ไหน

---

## 3. 01_MASTER_PROJECT_AUDIT_PROMPT.md

### ใช้ทำอะไร

ใช้ทำ Audit ใหญ่ทั้งระบบแบบ Full System / Full Flow / Production Readiness

ตรวจเรื่อง:

- Architecture
- Database
- Backend logic
- Frontend / UI / UX
- Compatibility
- Feature flow
- Auth / permission
- Tenant / store / organization
- Payment / subscription
- AI / OCR / external API
- API
- Security
- Performance
- Logging / monitoring
- Testing readiness
- DevOps / deployment
- Business logic / product risk

### ใช้เมื่อไหร่

ใช้ในช่วง:

```txt
ก่อน Production
หลังพัฒนา feature เยอะ
ก่อนเริ่ม QA ใหญ่
หลัง refactor ใหญ่
ก่อน release สำคัญ
```

### Input ที่ควรให้ AI

- Source code ทั้งโปรเจกต์
- Route list
- Migration / database schema
- Feature list ถ้ามี
- Business flow ถ้ามี
- Role / permission structure ถ้ามี
- Integration list ถ้ามี
- README / docs ถ้ามี

### Output ที่ต้องได้

- Full Project Audit Report
- Critical / High / Medium / Low issues
- Feature-by-feature audit
- Flow-by-flow audit
- Security audit
- Database audit
- Performance audit
- Production checklist
- Recommended refactor plan
- Test plan ที่ควรเพิ่ม
- Final verdict ว่าพร้อม production หรือยัง

### เงื่อนไขผ่านไปขั้นต่อไป

ยังไม่ต้อง perfect แต่ต้องได้รายการ issue ชัดเจน

หลังใช้ 01 แล้วให้ทำสิ่งนี้:

```txt
1. แยก Critical / High / Medium / Low
2. แก้ Critical ทั้งหมด
3. แก้ High ที่กระทบ production core
4. Medium/Low เก็บไว้ backlog ได้ ถ้าไม่กระทบ production
5. หลังแก้แล้วไปใช้ 01_1 Re-Audit
```

### ห้ามไป 02 QA ทันที ถ้า

```txt
- ยังมี Critical issue
- ยังมี High ด้าน Security
- ยังมี High ด้าน Permission / Role
- ยังมี High ด้าน Tenant Isolation
- ยังมี High ด้าน Payment / Subscription
- ยังมี High ด้าน Transaction / Accounting / Report
- ยังมี High ด้าน Data Integrity
- Build ยังไม่ผ่าน
- Flow หลักเปิดใช้ไม่ได้
```

---

## 4. Fix Critical / High Issues

### ใช้ทำอะไร

เป็นขั้นตอนแก้ปัญหาที่ Audit เจอ ก่อนเข้าสู่ Re-Audit

### ต้องแก้อะไรก่อน

ลำดับแก้ที่แนะนำ:

```txt
1. Security
2. Permission / Role
3. Tenant / Store isolation
4. Payment / Subscription
5. Transaction / Accounting / Financial data
6. Database integrity
7. Main feature flow
8. API / External integration
9. File upload / AI / OCR
10. Production config / deployment
11. Performance สำคัญ
12. UX ที่กระทบ flow หลัก
```

### ยังไม่จำเป็นต้องแก้อะไรก่อน QA

ถ้าไม่กระทบ production core สามารถเลื่อนได้:

```txt
- UI polish
- typo
- minor UX
- minor refactor
- naming
- nice-to-have
- minor performance
- docs improvement
```

แต่ถ้า Medium เกี่ยวกับเงิน/tenant/permission/payment/data ต้องพิจารณาแก้ก่อนเสมอ

---

## 5. 01_1_MASTER_RE_AUDIT.md

### ใช้ทำอะไร

ใช้ตรวจหลังแก้ issue แล้วว่า:

- แก้ถูกไหม
- แก้ครบไหม
- แก้ root cause หรือแค่ patch
- มี regression หรือ side effect ไหม
- มี risk ใหม่ไหม
- พร้อมเข้า QA หรือยัง

### ใช้เมื่อไหร่

ใช้หลังจาก:

```txt
- แก้ issue จาก 01 Master Audit
- แก้ bug จาก 02 QA
- แก้ blocker จาก 03 Go-Live Review
- แก้ hotfix สำคัญก่อนปล่อย
```

### Input ที่ควรให้ AI

- Audit report เดิม
- รายการ issue ที่แก้
- Git diff / changed files
- Code ปัจจุบันหลังแก้
- Test result ถ้ามี
- Error log ถ้ามี

### Output ที่ต้องได้

- Re-Audit Report
- Issue Verification Result
- Verified Fixed / Partially Fixed / Not Fixed
- New Issues Introduced
- Regression Risk Summary
- Required Test Cases After Fix
- Final Decision: Ready for Full QA Testing หรือ Not Ready

### เงื่อนไขผ่านไป 02 QA

ไป 02 ได้เมื่อ:

```txt
- Critical issue = 0
- High issue ที่กระทบ Security / Permission / Tenant / Payment / Transaction / Data Integrity = 0
- Issue สำคัญมีสถานะ Verified Fixed
- ไม่มี New Issue Introduced ระดับ Critical / High
- Flow หลักยังรันได้
- Build ผ่าน
- ไม่มี migration/config/env ค้าง
- ไม่มี error ใหญ่ใน console/log
```

### ถ้าไม่ผ่าน

```txt
กลับไป Fix → ใช้ 01_1 Re-Audit ซ้ำ
```

### ใช้ 01 ใหม่แทน 01_1 เมื่อไหร่

ใช้ 01 Master Audit ใหม่เฉพาะกรณี:

```txt
- เปลี่ยน architecture ใหญ่
- เปลี่ยน database schema หลายจุด
- เปลี่ยน auth/permission/tenant core logic
- เปลี่ยน payment/transaction core logic
- เพิ่ม feature ใหญ่ก่อน production
- QA เจอบั๊กกระจายหลาย module
- ระบบเปลี่ยนไปมากจน audit เดิมล้าสมัย
```

---

## 6. 02_FULL_MASTER_QA_TESTING_PROMPT.md

### ใช้ทำอะไร

ใช้ทำ QA Testing ใหญ่ทั้งระบบ

ตรวจเรื่อง:

- Functional Testing
- End-to-End Testing
- Regression Testing
- Smoke Testing
- Role / Permission Testing
- Tenant Isolation Testing
- Payment / Subscription Testing
- Transaction / Financial Data Testing
- API Testing
- UI / UX Testing
- Mobile / Tablet / Desktop Testing
- Cross-browser Testing
- File Upload / AI / OCR Testing
- Notification / Email / LINE / Webhook Testing
- Error Handling / Failure Testing
- Security Abuse Case Testing
- Performance / Load Testing เบื้องต้น
- Backup / Restore / Deployment QA

### ใช้เมื่อไหร่

ใช้หลังจาก:

```txt
01 Audit ผ่านในระดับไม่มี Critical/High core
01_1 Re-Audit ยืนยันว่า fix สำคัญผ่าน
Build ผ่าน
Flow หลักเปิดได้
```

### Input ที่ควรให้ AI

- Source code ปัจจุบัน
- Audit report
- Re-Audit report
- Fixed issue list
- Feature list
- Role / permission matrix
- Route/API list
- Database schema
- Existing test result ถ้ามี

### Output ที่ต้องได้

- Full Master QA Testing Report
- Smoke Test Checklist
- Critical E2E Test Cases
- Feature Test Matrix
- Role / Permission Test Matrix
- Tenant Isolation Test Matrix
- Payment / Subscription Test Matrix
- API Test Matrix
- File Upload / AI / OCR Test Matrix
- UI / Responsive Test Matrix
- Browser / Device Compatibility Matrix
- Error Handling Test Matrix
- Security Abuse Case Matrix
- Regression Test Checklist
- Automation Recommendation
- Final QA Verdict

### เงื่อนไขผ่านไป 03

ไป 03 ได้เมื่อ:

```txt
- QA ไม่มี Blocker
- QA ไม่มี Critical bug
- QA ไม่มี High bug ที่กระทบ Security / Permission / Tenant / Payment / Transaction / Data Integrity
- Smoke test ผ่าน
- Critical E2E flow ผ่าน
- Role/Permission test สำคัญผ่าน
- Tenant isolation test ผ่าน ถ้ามี tenant
- Payment/subscription test ผ่าน ถ้ามี payment
- Transaction/report test ผ่าน ถ้าเกี่ยวกับเงิน/บัญชี
- Regression test ของส่วนที่แก้ผ่าน
- เหลือได้เฉพาะ Medium/Low ที่รับความเสี่ยงได้
```

### ถ้า QA เจอ Blocker / Critical / High bug

ให้ทำแบบนี้:

```txt
02 QA พบ bug ใหญ่
↓
Fix bug
↓
ใช้ 01_1 Re-Audit ตรวจ fix
↓
ใช้ 02 เฉพาะ Regression / Failed Test / Affected Flow
↓
ถ้าผ่านแล้วค่อยไป 03
```

### ไม่ต้องกลับไป 01 ยกเว้น

```txt
- แก้ bug แล้วกระทบ core system ใหญ่
- ต้อง refactor ใหม่กว้าง
- database/auth/tenant/payment/transaction เปลี่ยนหลักการทำงาน
- bug กระจายหลายระบบจนเหมือนต้อง audit ใหม่
```

---

## 7. 03_FINAL_GO_LIVE_REVIEW_PROMPT.md

### ใช้ทำอะไร

ใช้ตัดสินรอบสุดท้ายว่า:

```txt
Go
No-Go
Go with Conditions
```

ไม่ใช่ QA และไม่ใช่ Audit ใหม่  
เป็นด่านอนุมัติ Production Release

### ใช้เมื่อไหร่

ใช้หลังจาก:

```txt
01 Master Audit เสร็จ
01_1 Re-Audit ผ่าน
02 Full QA Testing ผ่าน
Bug/blocker จาก QA ถูกแก้และ retest แล้ว
กำลังจะตัดสินใจปล่อย Production จริง
```

### Input ที่ควรให้ AI

- Master Audit Report
- Re-Audit Report
- Full QA Testing Report
- Regression Test Result
- Smoke Test Result
- Remaining issue list
- Production checklist draft
- Deployment plan
- Backup plan
- Rollback plan
- Monitoring plan

### Output ที่ต้องได้

- Final Go-Live Review Report
- Final Decision: Go / No-Go / Go with Conditions
- Production Readiness Score
- Release Gate Summary
- Remaining Issues
- Blockers
- Go with Conditions
- Deployment Readiness
- Backup / Rollback Readiness
- Post-Deploy Monitoring Plan
- Final Pre-Launch Checklist

### ถ้า 03 ได้ผลเป็น Go

```txt
ไป 04 Production Release Checklist
```

### ถ้า 03 ได้ผลเป็น Go with Conditions

```txt
ทำ conditions ให้ครบ
เอา conditions ไปใส่ใน 04 checklist
แล้วค่อย deploy
```

### ถ้า 03 ได้ผลเป็น No-Go

```txt
หยุด deploy
แก้ blocker
ใช้ 01_1 Re-Audit
ใช้ 02 Regression เฉพาะส่วนที่กระทบ
ใช้ 03 ซ้ำ
```

### ห้ามไป 04 ถ้า

```txt
- 03 เป็น No-Go
- ยังมี Blocker
- ยังมี Critical
- ยังมี High core risk
- ไม่มี backup/rollback plan
- QA critical flow ยังไม่ผ่าน
```

---

## 8. 04_PRODUCTION_RELEASE_CHECKLIST.md

### ใช้ทำอะไร

ใช้เป็น Checklist / Runbook ตอน deploy จริง

ครอบคลุม:

- Release information
- Pre-release gate
- Risk acceptance
- Backup
- Production env
- Secrets/API keys
- Laravel/Node checklist
- Database/migration
- Build
- Server/infrastructure
- Security before deploy
- Feature-specific release checklist
- Deploy execution
- Post-deploy smoke test
- Rollback
- Monitoring
- Incident report
- Final sign-off

### ใช้เมื่อไหร่

ใช้หลังจาก:

```txt
03 Final Go-Live Review = Go
หรือ
03 = Go with Conditions และทำเงื่อนไขครบแล้ว
```

### Output ที่ต้องได้

- Checklist ที่ติ๊กครบ
- Backup location
- Deploy command/result
- Post-deploy smoke test result
- Rollback readiness
- Release sign-off

### เงื่อนไขถึงจะ Deploy ได้

```txt
- Backup DB แล้ว
- Backup storage/config แล้วถ้าจำเป็น
- .env production ถูกต้อง
- APP_DEBUG=false
- Secret ไม่หลุด
- Build ผ่าน
- Migration พร้อม
- Rollback plan พร้อม
- Queue/scheduler/storage พร้อม
- SSL/domain พร้อม
- Smoke test plan พร้อม
```

### ถ้า Deploy แล้ว Smoke Test ไม่ผ่าน

```txt
หยุด monitor ทั่วไป
ประเมิน severity
ถ้า Critical → rollback หรือ hotfix ทันที
ถ้า High → hotfix ด่วน หรือ rollback ตามผลกระทบ
ถ้า Medium/Low → monitor และสร้าง backlog
```

---

## 9. 05_POST_DEPLOY_MONITORING_PROMPT.md

### ใช้ทำอะไร

ใช้ monitor หลัง deploy production จริง

ตรวจช่วง:

```txt
First 30 minutes
First 24 hours
First 72 hours
After hotfix
After rollback
```

ครอบคลุม:

- Application availability
- Server health
- Logs
- Smoke test
- Error trend
- User flow monitoring
- Data integrity
- Performance
- Auth/session
- Permission/tenant
- Payment/subscription
- Transaction/report
- Upload/AI/OCR
- Notification/webhook
- API
- Frontend/UX
- Infrastructure
- Rollback/hotfix decision

### ใช้เมื่อไหร่

ใช้หลังจาก:

```txt
Deploy production แล้ว
Post-deploy smoke test เบื้องต้นแล้ว
มี log/metric/user feedback ให้ตรวจ
```

### Input ที่ควรให้ AI

- Release version
- Deploy time
- Deploy log
- Smoke test result
- Application logs
- Web server logs
- Queue logs
- Scheduler logs
- Payment/webhook logs ถ้ามี
- Server metrics
- User feedback
- Error monitoring report ถ้ามี

### Output ที่ต้องได้

- Post-Deploy Monitoring Report
- Overall Status: Healthy / Warning / Critical / Rollback Recommended
- Health Check Summary
- Errors / Incidents Found
- Log Findings
- Performance / Resource Findings
- Data Integrity Findings
- User Feedback Findings
- Hotfix / Rollback Recommendation
- Next Monitoring Plan
- Backlog / Follow-up Tasks
- Final Status

### ถ้า 05 บอก Healthy

```txt
Monitor ต่อจนครบ 24-72 ชั่วโมง
สรุป release
เก็บ backlog รอบถัดไป
```

### ถ้า 05 บอก Warning

```txt
สร้าง hotfix/backlog ตาม severity
monitor ต่อใกล้ชิด
ยังไม่ต้อง rollback ถ้าไม่กระทบ core
```

### ถ้า 05 บอก Critical หรือ Rollback Recommended

```txt
ประเมิน rollback ทันที
หยุด queue ถ้าข้อมูลเสี่ยงเสีย
เข้า maintenance mode ถ้าจำเป็น
rollback หรือ hotfix
ใช้ 05 monitor หลังแก้/rollback อีกครั้ง
```

---

## 10. Decision Tree แบบเร็ว

### หลัง 01 Audit

```txt
เจอ Critical/High core?
├─ Yes → Fix → 01_1
└─ No → 01_1 หรือ 02 ตามความมั่นใจ
```

### หลัง 01_1 Re-Audit

```txt
Ready for QA?
├─ Yes → 02
└─ No → Fix → 01_1 ซ้ำ
```

### หลัง 02 QA

```txt
เจอ Blocker/Critical/High core?
├─ Yes → Fix → 01_1 → 02 Regression
└─ No → 03
```

### หลัง 03 Go-Live Review

```txt
Decision?
├─ Go → 04
├─ Go with Conditions → ทำเงื่อนไข → 04
└─ No-Go → Fix → 01_1 → 02 Regression → 03
```

### หลัง 04 Deploy

```txt
Smoke test ผ่าน?
├─ Yes → 05
└─ No → Hotfix หรือ Rollback → 05
```

### หลัง 05 Monitoring

```txt
Status?
├─ Healthy → monitor ต่อ / สรุป release
├─ Warning → hotfix/backlog/monitor
└─ Critical → rollback หรือ hotfix ด่วน
```

---

## 11. เกณฑ์ Severity กลางที่ใช้ทุกไฟล์

### Blocker

ระบบไปต่อไม่ได้หรือ deploy ไม่ได้

ตัวอย่าง:

- Build ไม่ผ่าน
- Login ใช้ไม่ได้
- Database migration พัง
- ระบบเปิดไม่ได้
- ไม่มี backup/rollback ก่อน deploy

### Critical

ห้ามขึ้น Production

ตัวอย่าง:

- ข้อมูลรั่ว
- Tenant isolation พัง
- Payment ผิด
- Transaction/ยอดเงินผิด
- Permission bypass
- Secret หลุด
- File private เปิด public
- ข้อมูลหาย/เสียหาย
- ระบบล่มใน flow หลัก

### High

ต้องแก้ก่อน production ถ้ากระทบ core

ตัวอย่าง:

- Flow หลักใช้ไม่ได้
- Report สำคัญผิด
- API หลักพัง
- Upload สำคัญพัง
- Subscription/package limit ผิด
- Role บางส่วนผิด
- Webhook สำคัญพัง

### Medium

อาจเลื่อนได้ถ้าไม่กระทบ core

ตัวอย่าง:

- Feature รองมี bug
- UX สับสนบางจุด
- Browser บางตัวมีปัญหาแต่มี workaround
- Performance ช้าแต่ไม่ล่ม

### Low

เก็บไว้ปรับปรุงหลัง launch ได้

ตัวอย่าง:

- UI polish
- typo
- minor layout
- minor copy
- nice-to-have

---

## 12. กฎสำคัญสำหรับทุกโปรเจกต์

### ห้ามขึ้น Production ถ้า

```txt
- ยังมี Blocker
- ยังมี Critical
- ยังมี High core risk
- QA critical flow ยังไม่ผ่าน
- ไม่มี backup
- ไม่มี rollback plan
- APP_DEBUG ยังเปิด
- Secret หลุด
- Tenant/permission/payment/transaction ยังไม่มั่นใจ
```

### ไป Production แบบ Go with Conditions ได้ถ้า

```txt
- ไม่มี Blocker/Critical
- ไม่มี High core risk
- เหลือ Medium/Low ที่รับได้
- มี workaround
- มี monitoring
- มี rollback
- business owner ยอมรับ risk
```

### หลัง Production ต้องทำเสมอ

```txt
- Smoke test ทันที
- Monitor log
- Monitor server
- Monitor flow หลัก
- Monitor payment/transaction ถ้ามี
- Monitor user feedback
- สรุป incident และ backlog
```

---

## 13. Workflow แนะนำสำหรับ Project ใหญ่ เช่น SaaS / Accounting / Multi-tenant

สำหรับระบบที่เกี่ยวกับบัญชี เงิน หลายร้าน หลาย user ให้เข้มกว่าปกติ:

```txt
01 Master Audit
↓
Fix Critical/High
↓
01_1 Re-Audit เฉพาะ:
- Security
- Permission
- Tenant Isolation
- Transaction
- Payment
- Subscription
- Report
- AI/OCR Draft
↓
02 Full QA Testing
↓
Fix QA bug
↓
01_1 Re-Audit เฉพาะ fix
↓
02 Regression
↓
03 Final Go-Live Review
↓
04 Production Release Checklist
↓
Deploy
↓
05 Post-Deploy Monitoring 72 ชั่วโมง
```

ห้ามปล่อยถ้ายังไม่มั่นใจเรื่อง:

```txt
- ยอดเงิน
- transaction
- report
- tenant isolation
- permission
- payment/subscription
- file upload security
- AI/OCR draft confirm flow
```

---

## 14. Workflow แนะนำสำหรับ Project เล็ก / Portfolio / Landing Page

ถ้าเป็นเว็บเล็ก ไม่มี payment ไม่มี tenant ไม่มีข้อมูลสำคัญ:

```txt
01 Master Audit
↓
Fix Critical/High
↓
01_1 Re-Audit
↓
02 QA แบบย่อ: responsive/browser/form/link
↓
03 Go-Live Review แบบย่อ
↓
04 Release Checklist
↓
05 Monitor log/uptime
```

สิ่งที่ต้องเน้น:

```txt
- build ผ่าน
- env ถูก
- SSL/domain ถูก
- responsive
- form/contact ใช้งานได้
- SEO/meta
- no console error
- no exposed secret
```

---

## 15. Template ข้อความสำหรับสั่ง AI ใช้แต่ละไฟล์

### ใช้ 01

```md
ใช้ไฟล์ 01_MASTER_PROJECT_AUDIT_PROMPT.md ตรวจโปรเจกต์นี้แบบเต็มระบบก่อน Production
ห้ามแก้โค้ดก่อน ให้ทำ Audit Report ก่อนเท่านั้น
```

### ใช้ 01_1

```md
ใช้ไฟล์ 01_1_MASTER_RE_AUDIT.md ตรวจหลังแก้ issue จาก Audit
ให้ตรวจจาก Audit Report เดิม + Git diff + Code ปัจจุบัน
เป้าหมายคือ verify ว่าแก้ครบไหม มี regression ไหม และพร้อมไป QA หรือยัง
```

### ใช้ 02

```md
ใช้ไฟล์ 02_FULL_MASTER_QA_TESTING_PROMPT.md ทำ Full QA Testing
ให้สร้าง QA Matrix, Test Case, Regression Checklist และ Final QA Verdict
ห้ามสรุปว่า test ผ่านถ้ายังไม่มีหลักฐานการ execute จริง
```

### ใช้ 03

```md
ใช้ไฟล์ 03_FINAL_GO_LIVE_REVIEW_PROMPT.md
ให้ดู Audit Report + Re-Audit Report + QA Report + Release Checklist
ตัดสินว่า Go / No-Go / Go with Conditions ก่อนขึ้น Production
```

### ใช้ 04

```md
ใช้ไฟล์ 04_PRODUCTION_RELEASE_CHECKLIST.md เป็น checklist ตอน deploy production จริง
ให้ช่วยตรวจว่าข้อไหนยังไม่พร้อม และต้องทำอะไรก่อนกด deploy
```

### ใช้ 05

```md
ใช้ไฟล์ 05_POST_DEPLOY_MONITORING_PROMPT.md ตรวจ production หลัง deploy
ให้วิเคราะห์ log, smoke test result, server metric, user feedback และตัดสินว่า Healthy / Warning / Critical / Rollback Recommended
```

---

## 16. สรุปสั้นที่สุด

```txt
01 = หาแผลทั้งระบบ
01_1 = เช็กว่าแก้แผลถูกไหม
02 = เทสใช้งานจริงทุก flow
03 = ตัดสินใจ Go / No-Go
04 = เช็คลิสต์ตอนปล่อยจริง
05 = เฝ้าระวังหลังปล่อยจริง
```

จุดสำคัญที่สุด:

```txt
ห้ามข้าม 01_1 หลังแก้ bug ใหญ่
ห้ามใช้ 03 แทน QA
ห้ามใช้ 04 ถ้า 03 ยัง No-Go
ห้ามจบงานหลัง deploy โดยไม่ใช้ 05 monitor
```
