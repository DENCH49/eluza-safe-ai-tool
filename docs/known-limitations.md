# Known Limitations

เอกสารนี้ระบุข้อจำกัดของ `eluza-safe-ai-tool` รุ่น public demo เพื่อไม่ให้ผู้ทดสอบ
หรือผู้พัฒนา AI เข้าใจว่า package นี้คือ ELUZA AI เต็มระบบ

## Not Full ELUZA AI / ไม่ใช่ ELUZA เต็มตัว

Package นี้เป็นเครื่องมือตรวจคำตอบร่างของ AI ก่อนปล่อยออกไป ไม่ใช่ตัวตน ELUZA
เต็มระบบ และไม่รวม private ELUZA core, private Brain runtime, memory,
experience loop, raw data, หรือ internal architecture

## Public-Safe Brain.Language Only

Brain.Language ที่อยู่ใน package นี้เป็น meaning frame แบบ public-safe สำหรับอ่าน
ข้อความที่ผู้ใช้เห็นเท่านั้น

มันไม่ใช่สมองเต็มของ ELUZA และไม่สามารถแทน private Brain memory,
Brain registry, owner experience, หรือระบบเรียนรู้ภายในได้

## No Live Web / ไม่มีข้อมูลสด

Demo นี้ทำงานแบบ offline/static จึงไม่ดึงข่าว ราคา พยากรณ์อากาศ หรือข้อมูลล่าสุด
จากอินเทอร์เน็ตเอง

ถ้าคำตอบขึ้นกับข้อมูลปัจจุบัน เครื่องมือควร route ไปที่ research/live source
แต่ผู้ใช้หรือระบบภายนอกต้องไปตรวจแหล่งข้อมูลจริงอีกที

## Not Expert Review / ไม่แทนผู้เชี่ยวชาญ

เครื่องมือนี้ไม่ใช่แพทย์ นักกฎหมาย นักการเงิน ผู้เชี่ยวชาญศาสนา
หรือระบบตัดสินความปลอดภัยจริง

คำตอบด้านสุขภาพ กฎหมาย การเงิน ศาสนา หรือความปลอดภัยสูง ต้องมีผู้เชี่ยวชาญ
ตรวจสอบก่อนนำไปใช้จริง

## Rule Field Sensitivity / ช่องหลักเกณฑ์ยังไวต่อถ้อยคำ

ช่องที่ 3 ใช้เพื่อบอกหลักเกณฑ์ หลักฐาน กฎ หรือแหล่งอ้างอิงที่อยากให้ AI ยึด
ถ้อยคำที่ต่างกันอาจทำให้ route ต่างกันได้ โดยเฉพาะใน demo ที่ยังไม่มี private
Brain memory และยังไม่มี live source

เป้าหมายของการเก็บ feedback คือหาจุดที่ถ้อยคำใกล้เคียงกันแต่ผลต่างเกินควร
แล้วนำไปปรับในรุ่นถัดไป

## No Private Access / ไม่เปิดข้อมูล protected

คำขอที่ต้องการ source code, core, private memory, raw data, internal logic,
private architecture หรือ owner private logs ต้องถูกปฏิเสธใน public demo

ข้อความปฏิเสธที่คาดหวังคือ:

```text
ไม่สามารถเปิดเผยได้ค่ะ
```

## Demo Is Evidence, Not Final Proof

ผลทดสอบจาก demo เป็นหลักฐานเพื่อพัฒนาและประเมิน tool layer
ยังไม่ใช่หลักฐานว่า ELUZA full system แก้ปัญหา AI ทั้งหมดได้สมบูรณ์แล้ว

การอ้างผลควรใช้ถ้อยคำแบบมีขอบเขต เช่น:

- public-safe answer evaluation demo
- preliminary public testing
- routed AI draft answer evaluation
- derived from ELUZA safety research

ไม่ควรอ้างว่า:

- full ELUZA AI is publicly released
- the system guarantees truth
- the system replaces expert review
- the public package contains private ELUZA core

## Current Best Use

การใช้ที่เหมาะสมที่สุดตอนนี้:

1. ช่วยคนทั่วไปตรวจคำตอบ AI ก่อนเชื่อหรือแชร์ต่อ
2. ช่วยผู้พัฒนา AI เห็น route ว่าคำตอบควรถูกปล่อย ปฏิเสธ หรือวิจัยเพิ่ม
3. เก็บ feedback เพื่อวัดว่า UI และผลลัพธ์เข้าใจง่ายหรือไม่
4. ใช้เป็น public demo สำหรับ GitHub, report, และงานวิจัยระยะต้น

