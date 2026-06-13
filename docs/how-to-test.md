# How to Test ELUZA Safe AI Tool

คู่มือทดสอบ ELUZA Safe AI Tool สำหรับคนทั่วไปและผู้พัฒนา AI

## Goal

ELUZA Safe AI Tool checks an AI draft answer before release.

เครื่องมือนี้ช่วยตรวจคำตอบร่างของ AI ก่อนปล่อยออก ว่าคำตอบนั้นควรถูกปล่อย
ปฏิเสธ เก็บเป็นสมมติฐาน ส่งไปวิจัยต่อ หรือเก็บเป็นประสบการณ์ที่ใช้ซ้ำได้แบบมีขอบเขต

This public demo is not ELUZA AI itself. It does not include private ELUZA core
source, private memory, raw data, private architecture, or internal logic.

เดโมนี้ไม่ใช่ ELUZA AI ตัวเต็ม และไม่รวม core source, private memory, raw data,
private architecture หรือ internal logic

## Quick Test

Open the public demo:

เปิดเดโม:

```text
https://dench49.github.io/eluza-safe-ai-tool/
```

Click:

กด:

```text
Open Demo / เปิดเดโม
```

Then use:

จากนั้นใช้:

```text
ทดลองง่าย / Easy Demo
```

Choose one scenario card and read the result panel.

เลือกการ์ดตัวอย่างหนึ่งอัน แล้วดูผลลัพธ์ด้านขวา

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
- evidence, permission, source notes, or context
- หลักฐาน สิทธิ์ แหล่งอ้างอิง หรือบริบท

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
