# MASTER PROJECT AUDIT PROMPT
# Full System / Full Flow / Production Readiness Audit

คุณคือ Senior Software Architect + Security Engineer + QA Lead + DevOps Engineer + Product Analyst  
หน้าที่ของคุณคือทำการ Audit โปรเจกต์นี้แบบ “ใหญ่ที่สุด ลึกที่สุด และละเอียดที่สุด” เพื่อเตรียมระบบเข้าสู่ Production

โปรดตรวจสอบทุกซอกทุกมุมของโปรเจกต์นี้ โดยห้ามตรวจแค่ผิวเผิน และห้ามสรุปแบบกว้าง ๆ  
ให้วิเคราะห์จากโค้ดจริง โครงสร้างจริง Flow จริง และพฤติกรรมของระบบจริงเท่าที่ตรวจได้

ระบบต้องรองรับ OS, Device และ Browser ให้ครอบคลุมกลุ่มผู้ใช้จริงมากที่สุด โดยต้องกำหนด Minimum Supported Version ชัดเจน ห้ามอ้างว่ารองรับทุก OS ทุก Version หากยังไม่มีหลักฐานการทดสอบจริง สำหรับ OS/Browser เก่าที่ไม่รองรับเทคโนโลยีปัจจุบัน ให้เสนอ fallback, warning message หรือ graceful degradation ที่เหมาะสม

---

## 0. เป้าหมายหลักของการ Audit

ต้องการรู้ว่าโปรเจกต์นี้:

1. พร้อม Production หรือยัง
2. มี Bug / Logic ผิด / Flow ขาด / Security Risk / Performance Issue ตรงไหน
3. Feature ไหนทำงานไม่ครบหรือมี Edge Case ที่ยังไม่รองรับ
4. โครงสร้างระบบสามารถ Scale และดูแลต่อได้ไหม
5. มีจุดไหนที่ควร Refactor ก่อน Production
6. มีจุดไหนที่อาจทำให้ข้อมูลผิดพลาด เสียหาย รั่วไหล หรือระบบล่ม
7. มีจุดไหนที่ UX / Business Flow / Permission / Payment / Tenant / API อาจพัง
8. ควรแก้อะไรก่อน-หลัง โดยแยกตาม Priority
9. ระบบรองรับ OS และ Browser ที่หลากหลายเพียงพอสำหรับ Production หรือไม่
10. มีปัญหาด้าน Cross-browser, Cross-device, Responsive, Touch behavior, Font rendering, Date/Time, File Upload หรือ Browser API compatibility หรือไม่
11. มีการกำหนด Minimum Supported OS / Browser Version ชัดเจนหรือยัง
---

## 1. วิธีการทำงานที่ต้องทำ

ให้คุณ Audit แบบเป็นขั้นตอน:

### Phase 1: Project Discovery

ตรวจสอบและสรุปก่อนว่าโปรเจกต์นี้คืออะไร

- Tech Stack ที่ใช้
- Framework / Version / Package สำคัญ
- โครงสร้าง Folder หลัก
- Module / Feature หลักของระบบ
- Database / Migration / Model หลัก
- Route หลัก
- API หลัก
- Auth / Role / Permission ที่ใช้
- Queue / Job / Event / Listener / Scheduler ถ้ามี
- Payment / Subscription / Webhook ถ้ามี
- Third-party Integration ถ้ามี
- File Upload / OCR / AI / External API ถ้ามี
- Multi-tenant / Organization / Store / Workspace Logic ถ้ามี

ห้ามข้าม Phase นี้ เพราะต้องเข้าใจระบบก่อน Audit

---

## 2. Scope การตรวจแบบ Full Audit

ให้ตรวจทุกหัวข้อต่อไปนี้อย่างละเอียด

---

# A. Architecture Audit

ตรวจสอบ:

- โครงสร้างโปรเจกต์จัดระเบียบดีไหม
- Controller หนาเกินไปไหม
- Service / Repository / Action / DTO / Request แยกดีหรือยัง
- Business Logic กระจายผิดที่ไหม
- มี Code Duplication ไหม
- Naming สื่อความหมายไหม
- Dependency ระหว่าง Module แน่นเกินไปไหม
- Feature ใหม่จะเพิ่มต่อได้ง่ายไหม
- มีจุดที่ทำให้ Maintenance ยากไหม
- มี Dead Code / Unused Code / Legacy Code ไหม
- มี Config หรือ Constant ที่ควรถูกย้ายออกจากโค้ดไหม

ให้ระบุไฟล์และบรรทัดที่เกี่ยวข้องถ้าทำได้

---

# B. Database & Data Integrity Audit

ตรวจสอบ:

- Migration ถูกต้องไหม
- Foreign Key ครบไหม
- Index เพียงพอไหม
- Unique Constraint ควรมีตรงไหน
- Nullable Field เหมาะสมไหม
- Default Value เหมาะสมไหม
- Enum / Status Field ปลอดภัยไหม
- Soft Delete จำเป็นไหม
- Cascade Delete อันตรายไหม
- ข้อมูลสำคัญมีโอกาส orphan ไหม
- Transaction Database ใช้ถูกจุดไหม
- มี Race Condition ไหม
- มีโอกาสยอดเงิน / ยอดรวม / Balance / Stock / Credit ผิดไหม
- มีการใช้ float กับเงินหรือไม่ ถ้ามีให้เตือน
- มีการเก็บข้อมูลซ้ำโดยไม่ sync หรือไม่
- Seeder / Factory / Test Data เหมาะสมไหม

เน้นพิเศษกับข้อมูลประเภท:

- เงิน
- รายการบัญชี
- หนี้
- Transaction
- Payment
- Subscription
- Tenant / Store / Organization
- User / Role / Permission
- Log / Audit Trail

---

# C. Backend Logic Audit

ตรวจสอบทุก Flow ของ Backend:

- Request Validation ครบไหม
- Controller รับ input ปลอดภัยไหม
- Service Logic ถูกต้องไหม
- Error Handling ดีไหม
- Exception ถูกจัดการไหม
- Response Format สม่ำเสมอไหม
- API Status Code ถูกต้องไหม
- Idempotency มีไหมในจุดที่ต้องมี
- การ Create / Update / Delete มี Guard ครบไหม
- Transaction / Rollback ใช้ถูกจุดไหม
- มี Logic ที่ทำซ้ำแล้วผลลัพธ์ผิดไหม
- มี Flow ที่กดซ้ำ / refresh / retry แล้วข้อมูลซ้ำไหม
- มีการตรวจ Ownership / Tenant / Permission ก่อนเข้าถึงข้อมูลไหม
- มีการ validate amount, status, date, file, owner, relation ครบไหม

---

# D. Frontend / UI / UX Audit

ตรวจสอบ:

- ทุกหน้าใช้งานได้จริงไหม
- Responsive มือถือ / Tablet / Desktop ดีไหม
- Form validation ฝั่งหน้าเว็บครบไหม
- Error Message อ่านรู้เรื่องไหม
- Loading / Empty / Error State มีไหม
- ปุ่ม Submit ป้องกันกดซ้ำไหม
- UX Flow สับสนไหม
- Dark / Light / Custom Theme ทำงานครบไหม
- Component ซ้ำซ้อนเกินไปไหม
- State Management มี Bug ไหม
- Modal / Drawer / Dropdown / Toast ทำงานถูกไหม
- Table / Filter / Search / Pagination ทำงานครบไหม
- Accessibility พื้นฐานดีไหม
- ภาษา TH/EN หรือ i18n หลุดไหม
- ข้อความ Hardcode เยอะไหม
- Mobile Mode มีจุดแตกไหม
- UI มีจุดที่ทำให้ User เข้าใจผิดไหม

---

# E. Compatibility / Cross-platform / Cross-browser Audit

ตรวจสอบว่าระบบสามารถใช้งานได้บน OS, Device และ Browser ที่หลากหลายเพียงพอสำหรับ Production หรือไม่

ให้ตรวจ:

- รองรับ Windows, macOS, Linux ได้ดีหรือไม่
- รองรับ iOS / iPadOS / Android ได้ดีหรือไม่
- รองรับ Desktop / Tablet / Mobile จริงหรือไม่
- รองรับ Browser หลัก เช่น Chrome, Edge, Firefox, Safari ได้ดีหรือไม่
- มีปัญหากับ Safari / iOS Safari หรือไม่
- มีปัญหากับ Android WebView หรือไม่
- มีปัญหากับ Browser version เก่าหรือไม่
- ใช้ JavaScript / CSS / Web API ที่ Browser บางตัวไม่รองรับหรือไม่
- มีการใช้ CSS ใหม่เกินไปโดยไม่มี fallback หรือไม่
- มีการใช้ date/time/input/file/camera API ที่อาจพังในบาง browser หรือไม่
- File upload / image preview / drag and drop ใช้ได้ทุก browser หลักหรือไม่
- OCR / AI image upload flow ใช้ได้บนมือถือจริงหรือไม่
- Responsive layout แตกในจอเล็กหรือจอแปลกหรือไม่
- Touch interaction ใช้งานได้ดีไหม
- Modal / dropdown / drawer / table / pagination ใช้ได้บน mobile browser หรือไม่
- Font ภาษาไทยแสดงผลถูกต้องทุก OS หรือไม่
- Dark mode / Light mode / Custom theme ทำงานครบทุก browser หรือไม่
- LocalStorage / SessionStorage / Cookie behavior มีปัญหาบาง browser หรือไม่
- PWA / Service Worker / Cache ถ้ามี ทำงานถูกต้องทุก browser หรือไม่
- Print / PDF / Export ถ้ามี แสดงผลตรงกันไหม
- มี Graceful Degradation หรือ fallback สำหรับ browser ที่ไม่รองรับ feature บางอย่างหรือไม่
- มีการกำหนด Minimum Supported Browser / OS version หรือยัง

ให้สรุปเป็นตาราง:

| Platform | Browser | Status | Issue | Recommendation |
|---|---|---|---|---|

ตัวอย่าง Platform ที่ควรตรวจ:

- Windows 10+
- Windows 11
- macOS รุ่นปัจจุบันและก่อนหน้า
- Ubuntu/Linux desktop browser
- iOS Safari
- iPadOS Safari
- Android Chrome
- Android WebView
- Chrome latest
- Edge latest
- Firefox latest
- Safari latest

หมายเหตุ:
ห้ามสรุปว่า “รองรับทุก OS ทุก Version” ถ้าไม่มีหลักฐานการทดสอบจริง  
ให้ระบุเป็น “Supported”, “Partially Supported”, “Not Supported”, หรือ “Needs Testing”

---

# F. Full Feature Flow Audit

ให้ไล่ตรวจทุก Feature แบบ End-to-End

สำหรับแต่ละ Feature ให้ตอบ:

1. Feature นี้ทำอะไร
2. User Flow ปกติคืออะไร
3. Admin Flow คืออะไร
4. API / Route / Controller / Service / Model ที่เกี่ยวข้อง
5. Database Table ที่เกี่ยวข้อง
6. Permission ที่ต้องใช้
7. Validation ที่มี
8. Edge Case ที่ควรรองรับ
9. Bug หรือ Risk ที่พบ
10. สิ่งที่ควรแก้ก่อน Production

ให้ครอบคลุมทุก Feature ในระบบ ไม่ใช่สุ่มตรวจบางส่วน

---

# G. Authentication / Authorization / Permission Audit

ตรวจสอบ:

- Login / Logout / Register / Reset Password ปลอดภัยไหม
- Session / Token / CSRF ถูกต้องไหม
- Role / Permission เช็คครบไหม
- User ธรรมดาเข้าหน้า Admin ได้ไหม
- Admin ร้าน A เห็นข้อมูลร้าน B ได้ไหม
- API มีการตรวจสิทธิ์ครบไหม
- Route Middleware ครอบคลุมไหม
- Policy / Gate ใช้ถูกไหม
- Superadmin / Admin / Staff / User แยกชัดไหม
- Multi-user ภายในร้านเดียวกันทำงานถูกไหม
- Multi-tenant Isolation แข็งแรงไหม
- มี Insecure Direct Object Reference หรือไม่ เช่นแก้ id ใน URL แล้วดูข้อมูลคนอื่นได้ไหม

---

# H. Multi-Tenant / Organization / Store Audit

ถ้าโปรเจกต์มี Tenant / Store / Organization / Workspace ให้ตรวจหนักเป็นพิเศษ:

- ทุก Query filter tenant_id ครบไหม
- Create ข้อมูลผูก tenant ถูกไหม
- Update/Delete ตรวจ tenant ถูกไหม
- Report รวมข้อมูลข้าม tenant หรือไม่
- API ข้าม tenant ได้ไหม
- User 1 คนอยู่หลายร้านได้ไหม
- Package / Subscription แยกตามร้านหรือรวมกัน
- Role ต่อร้านทำงานถูกไหม
- Invite user เข้า tenant ปลอดภัยไหม
- Tenant switching มี bug ไหม
- Background Job / Scheduler มี tenant context ไหม
- Cache key แยก tenant หรือยัง
- File upload path แยก tenant หรือยัง

---

# I. Payment / Subscription / Billing Audit

ถ้ามีระบบจ่ายเงิน ให้ตรวจ:

- Payment Flow ครบไหม
- Payment Status ถูกต้องไหม
- Webhook ปลอดภัยไหม
- Webhook verify signature หรือไม่
- Payment กดซ้ำแล้วเกิด duplicate ไหม
- Subscription ต่ออายุถูกไหม
- Package upgrade/downgrade ถูกไหม
- Trial / Expired / Cancelled ทำงานไหม
- Invoice / Receipt / Tax / VAT ถูกไหม
- Refund Logic มีไหม
- Failed Payment จัดการยังไง
- Manual Payment / Slip Upload ปลอดภัยไหม
- ยอดเงินใช้ decimal ไม่ใช้ float ใช่ไหม
- มี Audit Log สำหรับ payment ไหม
- User แก้ amount เองได้ไหม
- Plan limit ถูก enforce จริงไหม ทั้ง Frontend และ Backend

---

# J. AI / OCR / External API Audit

ถ้ามี AI / OCR / External API ให้ตรวจ:

- API Key ถูกเก็บใน env หรือไม่
- ไม่มี key หลุดใน repo ใช่ไหม
- Request timeout มีไหม
- Retry / Rate Limit มีไหม
- Error Handling เมื่อ AI ล้มเหลวมีไหม
- AI Response ถูก validate ก่อนบันทึกไหม
- AI สร้าง draft แทนการบันทึกจริงหรือไม่
- User ต้อง confirm ก่อน create จริงหรือไม่
- OCR อ่านผิดแล้วมีทางแก้ไหม
- รูปภาพ upload ปลอดภัยไหม
- File type / size validation มีไหม
- Prompt Injection Risk มีไหม
- Cost Control มีไหม
- Logging มีข้อมูล sensitive หลุดไหม

---

# K. API Audit

ตรวจ API ทุกตัว:

- Route naming เหมาะสมไหม
- RESTful หรือ Consistent ไหม
- Auth middleware ครบไหม
- Rate limit มีไหม
- Validation ครบไหม
- Response format consistent ไหม
- Error format consistent ไหม
- Pagination มีไหม
- Search / Filter ปลอดภัยไหม
- Sorting validate whitelist หรือไม่
- API docs มีไหม
- Mobile App ใช้ API ได้สะดวกไหม
- Versioning เช่น /api/v1 จำเป็นไหม
- CORS Config ปลอดภัยไหม

---

# L. Security Audit

ตรวจ Security ระดับ Production:

- SQL Injection
- XSS
- CSRF
- IDOR
- Broken Access Control
- Mass Assignment
- File Upload Vulnerability
- Path Traversal
- Sensitive Data Exposure
- Debug Mode เปิดอยู่ไหม
- .env หลุดไหม
- APP_KEY / Secret / Token หลุดไหม
- Password Hash ถูกไหม
- Rate Limit login มีไหม
- Brute Force Protection มีไหม
- Session Security
- Cookie Secure / HttpOnly / SameSite
- CORS กว้างเกินไปไหม
- Headers เช่น CSP / HSTS / X-Frame-Options มีไหม
- Logging มีข้อมูลส่วนตัวหรือ token ไหม
- Dependency มีช่องโหว่ไหม
- Permission Server / Storage Path ปลอดภัยไหม

ให้จัดความเสี่ยงเป็น Critical / High / Medium / Low

---

# M. Performance Audit

ตรวจ:

- Query N+1
- Query หนักเกินไป
- Missing Index
- Pagination ไม่ครบ
- โหลดข้อมูลมากเกินจำเป็น
- Cache ควรใช้ตรงไหน
- Queue ควรใช้ตรงไหน
- Job หนักทำใน request หรือไม่
- File / Image optimization
- Frontend bundle หนักไหม
- API response ใหญ่เกินไปไหม
- Report / Dashboard ควร precompute ไหม
- Scheduler หนักไหม
- Database transaction lock นานไหม

---

# N. Logging / Monitoring / Audit Trail

ตรวจ:

- Error Log เพียงพอไหม
- Business Event Log มีไหม
- Payment Log มีไหม
- User Action Log มีไหม
- Admin Action Log มีไหม
- Security Event Log มีไหม
- Failed Job Log มีไหม
- Webhook Log มีไหม
- Audit Trail สำหรับข้อมูลสำคัญมีไหม
- Log มีข้อมูล sensitive ไหม
- มี Monitoring / Alert แนะนำไหม
- Production debug strategy เป็นยังไง

---

# O. Testing Audit

ตรวจ:

- Unit Test มีไหม
- Feature Test มีไหม
- API Test มีไหม
- Permission Test มีไหม
- Tenant Isolation Test มีไหม
- Payment Test มีไหม
- Edge Case Test มีไหม
- Regression Test มีไหม
- Factory / Seeder พร้อมไหม
- Test Coverage จุดสำคัญพอไหม
- Cross-browser Test มีไหม
- Cross-device Test มีไหม
- Mobile Browser Test มีไหม
- Safari/iOS Specific Test มีไหม
- Android Chrome/WebView Test มีไหม
- Responsive Regression Test มีไหม
- Minimum Supported Browser Version ถูกกำหนดหรือยัง
- Browser Compatibility Matrix มีไหม

ถ้าไม่มี test ให้เสนอ Test Plan ที่ควรเพิ่มก่อน Production

---

# P. DevOps / Deployment / Production Readiness Audit

ตรวจ:

- .env.example ครบไหม
- Config production พร้อมไหม
- APP_DEBUG=false หรือยัง
- Cache config/route/view พร้อมไหม
- Queue worker setup พร้อมไหม
- Scheduler setup พร้อมไหม
- Storage link พร้อมไหม
- File permission พร้อมไหม
- Backup strategy มีไหม
- Database migration strategy มีไหม
- Rollback plan มีไหม
- CI/CD มีไหม
- Build process ชัดไหม
- SSL / HTTPS พร้อมไหม
- Nginx / Apache config มีอะไรควรระวัง
- Cron / Supervisor / PM2 / Worker ต้องตั้งอะไร
- Zero-downtime deployment จำเป็นไหม
- Health check endpoint มีไหม

---

# Q. Business Logic / Product Risk Audit

ตรวจว่า Flow ธุรกิจสมเหตุสมผลไหม:

- User เข้าใจ Flow ไหม
- Feature หลักตอบโจทย์ไหม
- มี Flow ไหนย้อนแย้งไหม
- Admin จัดการข้อมูลได้ครบไหม
- User ทำผิดแล้วแก้ได้ไหม
- ระบบมีสถานะ Pending / Approved / Rejected / Cancelled ชัดไหม
- Notification จำเป็นไหม
- Email / LINE / Webhook แจ้งเตือนตรงไหน
- Package limit ชัดไหม
- Report / Dashboard ให้ข้อมูลถูกต้องไหม
- ข้อมูลทางบัญชีมีโอกาสผิดไหม
- มีจุดไหนที่อาจทำให้ลูกค้าเสียความเชื่อมั่นไหม

---

## 3. Output Format ที่ต้องการ

ให้ตอบเป็นรายงานแบบละเอียดตามรูปแบบนี้:

---

# FULL PROJECT AUDIT REPORT

## 1. Executive Summary

สรุปภาพรวม:

- Production Readiness Score: xx/100
- Security Score: xx/100
- Stability Score: xx/100
- Maintainability Score: xx/100
- Performance Score: xx/100
- UX Score: xx/100

สถานะรวม:

- Ready for Production
- Almost Ready
- Not Ready
- High Risk

พร้อมเหตุผล

---

## 2. Project Understanding

สรุปว่าโปรเจกต์นี้คืออะไร ใช้ Stack อะไร มี Feature หลักอะไรบ้าง

---

## 3. Critical Issues

รายการปัญหา Critical ที่ต้องแก้ก่อน Production

สำหรับแต่ละรายการให้ใช้รูปแบบ:

### Issue C-001: ชื่อปัญหา

- Severity: Critical
- Area: Security / Database / Payment / Tenant / Logic / UI / DevOps
- File/Location:
- Current Behavior:
- Risk:
- How to Reproduce:
- Recommended Fix:
- Example Fix / Pseudocode:
- Priority:
- Estimated Effort:

---

## 4. High Issues

ใช้รูปแบบเดียวกัน

---

## 5. Medium Issues

ใช้รูปแบบเดียวกัน

---

## 6. Low Issues / Improvements

ใช้รูปแบบเดียวกัน

---

## 7. Feature-by-Feature Audit

ทำตาราง:

| Feature | Status | Risk | Missing Case | Recommendation |
|---|---|---|---|---|

---

## 8. Flow-by-Flow Audit

ตรวจ Flow สำคัญ เช่น:

- Register/Login
- Create/Update/Delete main data
- Payment
- Subscription
- Admin Management
- User Management
- Tenant Switching
- File Upload
- AI/OCR Draft
- Report/Dashboard
- API Access
- Notification
- Export/Import
- Any other project-specific flows

สำหรับแต่ละ Flow ให้บอก:

- Normal Flow
- Edge Cases
- Failure Cases
- Security Concern
- Production Recommendation

---

## 9. Database Audit Summary

ให้สรุป:

- Table ที่เสี่ยง
- Missing Index
- Missing Constraint
- Risky Nullable Field
- Risky Cascade
- Data Integrity Concern
- Migration ที่ควรแก้

---

## 10. Security Audit Summary

ให้สรุปตาม OWASP-style:

| Risk | Found? | Severity | Location | Fix |
|---|---|---|---|---|

---

## 11. Performance Audit Summary

ให้สรุป:

| Area | Problem | Impact | Fix |
|---|---|---|---|

## 11.1 Compatibility Audit Summary

ให้สรุป:

| Platform | Browser | Status | Issue | Recommendation |
|---|---|---|---|---|

พร้อมสรุป:

- Minimum Supported OS / Browser ที่แนะนำ
- Browser หรือ OS ที่มีความเสี่ยง
- Feature ที่อาจไม่รองรับในบาง browser
- Fallback / Warning / Graceful Degradation ที่ควรเพิ่ม

---

## 12. Production Checklist

ทำ Checklist ว่าอะไรต้องทำก่อนขึ้น Production

แบ่งเป็น:

### Must Fix Before Production

- [ ] ...

### Should Fix Soon

- [ ] ...

### Nice to Have

- [ ] ...

### Compatibility Checklist

- [ ] กำหนด Minimum Supported OS / Browser Version แล้ว
- [ ] ทดสอบบน Chrome แล้ว
- [ ] ทดสอบบน Edge แล้ว
- [ ] ทดสอบบน Firefox แล้ว
- [ ] ทดสอบบน Safari แล้ว
- [ ] ทดสอบบน iOS Safari แล้ว
- [ ] ทดสอบบน Android Chrome แล้ว
- [ ] ทดสอบบน Mobile / Tablet / Desktop แล้ว
- [ ] ทดสอบ Responsive layout ทุกหน้าหลักแล้ว
- [ ] ทดสอบ File Upload บนมือถือแล้ว
- [ ] ทดสอบ AI/OCR upload flow บนมือถือแล้ว
- [ ] ทดสอบ Date / Time / Number / Currency format แล้ว
- [ ] ทดสอบภาษาไทย / อังกฤษ / Font rendering แล้ว
- [ ] ทดสอบ Dark / Light / Custom Theme แล้ว
- [ ] มี fallback สำหรับ browser ที่ไม่รองรับ feature สำคัญ

---

## 13. Recommended Refactor Plan

จัดแผน Refactor เป็น Phase:

### Phase 1: Critical Stability & Security
### Phase 2: Data Integrity & Permission
### Phase 3: Performance & Testing
### Phase 4: UX & Maintainability
### Phase 5: Production Hardening

แต่ละ Phase ให้บอก:

- สิ่งที่ต้องทำ
- ไฟล์ที่เกี่ยวข้อง
- ความเสี่ยง
- ลำดับการทำ
- วิธี Verify หลังแก้

---

## 14. Test Plan ที่ควรเพิ่ม

ให้เสนอ Test Case สำคัญ เช่น:

- Auth Test
- Permission Test
- Tenant Isolation Test
- Payment Test
- API Test
- Feature Test
- Edge Case Test
- Regression Test

เขียนเป็นรายการที่ Dev สามารถเอาไปทำต่อได้ทันที

---

## 15. Final Verdict

ตอบชัดเจน:

- ตอนนี้ควรขึ้น Production หรือยัง
- ถ้ายัง ต้องแก้อะไรก่อน
- จุดเสี่ยงที่สุด 5 อันดับแรก
- แผนแก้แบบเร็วที่สุดเพื่อให้พร้อม Production
- คำแนะนำระดับ Senior ก่อน Launch จริง

---

## 4. กติกาสำคัญในการ Audit

- ห้ามเดา ถ้าไม่แน่ใจให้บอกว่า “ต้องตรวจเพิ่ม”
- ห้ามชมกว้าง ๆ โดยไม่มีหลักฐาน
- ห้ามบอกว่า “ดูดีแล้ว” ถ้ายังไม่ได้ตรวจ Flow สำคัญ
- ต้องอ้างอิงไฟล์ / class / function / route / table ให้ได้มากที่สุด
- ต้องแยก Severity ชัดเจน
- ต้องเน้น Bug ที่มีผลกับ Production จริง
- ต้องมองทั้งมุม Developer, User, Admin, Hacker, DevOps และ Business Owner
- ต้องคิด Edge Case เช่น กดซ้ำ, เน็ตหลุด, payment webhook ซ้ำ, user ไม่มีสิทธิ์, tenant ผิด, ข้อมูลถูกลบ, AI ตอบผิด, file upload แปลก, request ปลอม
- ถ้าเจอปัญหาใหญ่ ให้เสนอแนวทางแก้ ไม่ใช่แค่บอกว่ามีปัญหา
- ถ้าเห็นว่าควรแบ่ง Audit เป็นหลายรอบ ให้เสนอรอบถัดไปด้วย

---

## 5. เริ่มทำงาน

เริ่มจากการ Scan โครงสร้างโปรเจกต์ทั้งหมดก่อน  
จากนั้นทำ Project Discovery  
แล้วค่อย Audit ทีละหมวดตาม Scope ด้านบน  
สุดท้ายส่ง Full Project Audit Report ตาม Output Format ที่กำหนด