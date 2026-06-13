# How to Test ELUZA Safe AI Tool

คู่มือทดสอบ ELUZA Safe AI Tool สำหรับคนทั่วไปและผู้พัฒนา AI

## Goal

ELUZA Safe AI Tool checks an answer from another AI before release.

เครื่องมือนี้ช่วยตรวจคำตอบจาก AI ตัวอื่นก่อนปล่อยออก ว่าคำตอบนั้นควรถูกปล่อย
ปฏิเสธ เก็บเป็นสมมติฐาน ส่งไปวิจัยต่อ หรือเก็บเป็นประสบการณ์ที่ใช้ซ้ำได้แบบมีขอบเขต

It is not a chatbot and not a calculator. Ask another AI first, then paste the
question, the AI answer, and a rule/evidence/reference into this tool.

มันไม่ใช่แชทบอทและไม่ใช่เครื่องคิดเลข ให้ถาม AI ตัวอื่นก่อน แล้วเอาคำถาม
คำตอบของ AI และกฎ/หลักฐาน/อ้างอิง มาใส่เครื่องมือนี้เพื่อตรวจ

This public demo is not ELUZA AI itself. It does not include private ELUZA core
source, private memory, raw data, private architecture, or internal logic.

เดโมนี้ไม่ใช่ ELUZA AI ตัวเต็ม และไม่รวม core source, private memory, raw data,
private architecture หรือ internal logic

## Quick Test

Use this flow:

ใช้ตามขั้นนี้:

```text
1. Open any AI and ask a real question.
   เปิด AI ตัวไหนก็ได้ แล้วถามคำถามจริง

2. Copy the original question into field 1.
   คัดลอกคำถามเดิมใส่ช่องที่ 1

3. Copy the AI answer into field 2.
   คัดลอกคำตอบของ AI ใส่ช่องที่ 2

4. Add rules, policy, evidence, references, or context into field 3.
   ใส่กฎ ข้อบังคับ หลักฐาน อ้างอิง หรือบริบทในช่องที่ 3

5. Click Evaluate.
   กดตรวจ
```

Open the public demo:

เปิดเดโม:

```text
https://dench49.github.io/eluza-safe-ai-tool/
```

If you are a general tester, start with:

ถ้าเป็นคนทั่วไป ให้เริ่มจาก:

```text
ทดลองง่าย / Easy Demo
```

Choose one scenario card and read the result panel.

เลือกการ์ดตัวอย่างหนึ่งอัน แล้วดูผลลัพธ์ด้านขวา

General testers should start with scenario cards, not `Advanced Test`.

คนทั่วไปควรเริ่มจากการ์ดตัวอย่าง ไม่ควรเริ่มจาก `Advanced Test`

## General Tester Script

บททดสอบสำหรับคนทั่วไป

```text
1. Open the demo.
   เปิดเดโม

2. Click one scenario card, such as Tree overclaim or Source code request.
   กดการ์ดตัวอย่างหนึ่งอัน เช่น ต้นไม้/น้ำบาดาล หรือ ขอ source code

3. Read "Before: AI draft".
   อ่านช่อง "ก่อนตรวจ" ว่า AI ร่างคำตอบไว้อย่างไร

4. Read "After: safer output".
   อ่านช่อง "หลังตรวจ" ว่าเครื่องมือเปลี่ยนหรือหยุดคำตอบอย่างไร

5. Read "Plain meaning".
   อ่านช่อง "ความหมายแบบคนทั่วไป" ว่าเข้าใจเหตุผลไหม

6. Answer the feedback form.
   ตอบแบบประเมินท้ายบททดสอบ
```

## Feedback Form

แบบประเมินหลังทดสอบ

```text
1. เข้าใจไหมว่าเครื่องมือนี้ทำอะไร?
ตอบ:

2. ตอนกดตัวอย่าง จุดไหนงงที่สุด?
ตอบ:

3. ผลลัพธ์ช่วยให้คำตอบ AI น่าเชื่อถือหรือปลอดภัยขึ้นไหม?
ตอบ:

4. อยากให้เพิ่มหรือแก้อะไร?
ตอบ:
```

## What to Look For

For each case, check whether the tool makes the answer safer:

สำหรับแต่ละเคส ให้ดูว่าเครื่องมือทำให้คำตอบปลอดภัยขึ้นหรือไม่

- Protected request: should refuse briefly.
- คำขอข้อมูลปกป้อง: ควรปฏิเสธสั้น ๆ
- Weak observation: should not become truth too early.
- ข้อมูลสังเกตอ่อน: ไม่ควรถูกสรุปเป็นความจริงเร็วเกินไป
- High-risk domain: should require evidence or expert review.
- เรื่องเสี่ยงสูง: ควรต้องมีหลักฐานหรือผู้เชี่ยวชาญตรวจ
- Bounded answer: can be released with a clear boundary.
- คำตอบมีขอบเขต: ปล่อยได้ถ้าไม่ฟันธงเกินหลักฐาน
- Validated experience: can return as scoped experience only.
- ประสบการณ์ที่ยืนยันแล้ว: ใช้ซ้ำได้เฉพาะในขอบเขตเดิม

## For General Testers

You do not need to understand the JSON.

คนทั่วไปไม่จำเป็นต้องเข้าใจ JSON

Please answer these three questions:

ช่วยตอบ 3 ข้อนี้:

```text
1. Did you understand what the tool does?
   เข้าใจไหมว่าเครื่องมือนี้ทำอะไร?

2. Which part was confusing?
   จุดไหนงงที่สุด?

3. Does this feel useful for AI safety or AI answer checking?
   รู้สึกว่ามีประโยชน์กับความปลอดภัยของ AI หรือการตรวจคำตอบ AI ไหม?
```

## For AI Developers

Use `Advanced Test` to enter:

ใช้ `ทดสอบขั้นสูง / Advanced Test` แล้วใส่:

- user input or prompt
- คำถามของผู้ใช้
- AI candidate answer
- คำตอบร่างของ AI
- rule, policy, evidence, reference, permission, source notes, or context
- กฎ ข้อบังคับ หลักฐาน อ้างอิง สิทธิ์ แหล่งอ้างอิง หรือบริบท

Do not use `Advanced Test` as a normal question box. It checks an answer from
another AI and routes it; it does not generate the answer.

อย่าใช้ `Advanced Test` เป็นช่องถามคำถามทั่วไป ช่องนี้ตรวจคำตอบจาก AI ตัวอื่นและ
route คำตอบ ไม่ได้สร้างคำตอบแทน AI

Then check:

จากนั้นดู:

- `fruit_type`
- `status`
- `risk`
- `next_route`
- `mizan_status`
- `Developer trace JSON`

The trace is public-safe and redacted. It is meant for debugging the tool's
public routing behavior, not exposing ELUZA internals.

trace เป็นแบบ public-safe และถูกตัดข้อมูลลับออก ใช้เพื่อ debug เส้นทางสาธารณะของ
เครื่องมือ ไม่ใช่เพื่อเปิดเผยภายในของ ELUZA

## Feedback Format

If you report feedback, please include:

ถ้าจะส่ง feedback กรุณาใส่ข้อมูลนี้:

```text
Tester type:
คนทดสอบเป็น: general user / AI developer / other

Case tested:
เคสที่ลอง:

Expected result:
คิดว่าผลควรเป็น:

Actual result:
ผลที่ได้จริง:

Confusing part:
จุดที่งง:

Suggestion:
ข้อเสนอ:
```

## Boundaries

Do not paste private passwords, API keys, private documents, medical records, or
other sensitive personal data into the demo.

ห้ามใส่รหัสผ่าน API keys เอกสารส่วนตัว ข้อมูลแพทย์ หรือข้อมูลส่วนตัวที่อ่อนไหวลงในเดโม

The demo is an evaluation tool for AI draft answers. It is not a legal, medical,
financial, religious, or safety-critical decision system.

เดโมนี้เป็นเครื่องมือตรวจคำตอบร่างของ AI ไม่ใช่ระบบตัดสินใจแทนผู้เชี่ยวชาญด้านกฎหมาย
แพทย์ การเงิน ศาสนา หรือระบบความปลอดภัยจริง
