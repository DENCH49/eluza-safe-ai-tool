# Public Testing Kit / ชุดโพสต์ชวนทดสอบ

เอกสารนี้ช่วยประกาศชวนคนมาทดสอบ ELUZA Safe AI Tool แบบอ่านง่าย

## Short Thai Post / โพสต์สั้นภาษาไทย

```text
ผมทำ demo เครื่องมือตรวจคำตอบ AI ก่อนเชื่อหรือแชร์ต่อครับ

วิธีลอง:
1. เปิด AI ตัวไหนก็ได้ แล้วถาม 1 คำถาม
2. เอาคำถามกับคำตอบ AI มาใส่ใน demo
3. ใส่หลักเกณฑ์ที่อยากให้ AI ยึด เช่น ต้องมีหลักฐาน / ห้ามเปิดข้อมูลลับ / ต้องอ้างอิงแหล่งข้อมูล
4. ดูว่าเครื่องมือบอกให้ปล่อย ใช้แบบมีขอบเขต หาหลักฐานเพิ่ม หรือปฏิเสธ

นี่ไม่ใช่ ELUZA AI เต็มตัว แต่เป็น public-safe tool สำหรับช่วยตรวจคำตอบ AI
ลองแล้วช่วยส่ง feedback ให้หน่อยครับ

Demo:
https://dench49.github.io/eluza-safe-ai-tool/

ถ้าไม่รู้จะถามอะไร ใช้โจทย์ตัวอย่างนี้ได้:
https://dench49.github.io/eluza-safe-ai-tool/docs/test-case-bank.html
```

## Friendly Thai Post / โพสต์ไทยแบบเป็นกันเอง

```text
ขอแรงช่วยทดสอบเครื่องมือตรวจคำตอบ AI หน่อยครับ

ปัญหาที่ผมอยากแก้คือ หลายครั้ง AI ตอบดูมั่นใจ แต่เราไม่รู้ว่าควรเชื่อไหม
ตัว demo นี้ไม่ได้ตอบแทน AI แต่ช่วยตรวจ "คำตอบที่ AI ตอบมาแล้ว" ว่าควรปล่อยไหม
ควรหาหลักฐานเพิ่มไหม หรือควรปฏิเสธ

ใช้ง่าย ๆ:
- ช่อง 1 ใส่คำถามที่ถาม AI
- ช่อง 2 ใส่คำตอบที่ AI ตอบ
- ช่อง 3 ใส่หลักที่อยากให้ AI ยึด เช่น ต้องมีหลักฐาน / ต้องอ้างอิง / ห้ามเปิดข้อมูลลับ

ถ้าไม่รู้จะถามอะไร กดดูธนาคารโจทย์ได้เลย

Demo:
https://dench49.github.io/eluza-safe-ai-tool/

ธนาคารโจทย์:
https://dench49.github.io/eluza-safe-ai-tool/docs/test-case-bank.html

ขอบคุณทุก feedback ครับ ผมจะใช้ผลทดสอบแบบไม่ระบุตัวตนเพื่อพัฒนางานวิจัยต่อ
```

## Short English Post

```text
I am testing a public-safe tool for checking AI draft answers before release.

It does not generate a new answer. It checks an answer that an AI already gave,
then routes it as usable, bounded, needs evidence, research, or rejected.

Demo:
https://dench49.github.io/eluza-safe-ai-tool/

Test case bank:
https://dench49.github.io/eluza-safe-ai-tool/docs/test-case-bank.html

This is not full ELUZA AI and does not include private core source, memory, raw data, or internal logic.
Feedback is welcome.
```

## Where To Post / ควรโพสต์ที่ไหนดี

เริ่มจากช่องทางที่มีโอกาสได้ feedback จริง ไม่ใช่แค่ยอดวิว:

1. Facebook ส่วนตัว  
   เหมาะกับคนทั่วไป เพราะจะได้รู้ว่าคนธรรมดาเข้าใจ demo ไหม

2. กลุ่มหรือเพจสาย AI/ChatGPT ภาษาไทย  
   เหมาะกับคนที่สนใจ AI อยู่แล้ว ให้โพสต์แบบขอ feedback ไม่ใช่ขายของ

3. กลุ่ม Data Science / Python / Developer ไทย  
   เหมาะกับผู้พัฒนา AI ที่อ่าน JSON trace, README, CLI/API ได้

4. LinkedIn  
   เหมาะกับผู้พัฒนา นักวิจัย คนทำ product หรือคนในองค์กรที่สนใจ AI safety

5. GitHub Issues  
   เหมาะกับ feedback ที่ต้องการเก็บเป็นเคส มีขั้นตอน มี input/output ชัดเจน

6. กลุ่มมหาวิทยาลัยหรือชมรมเทคโนโลยี  
   เหมาะกับนักเรียน นักศึกษา และคนที่ช่วยลองหลายเคสได้

## Suggested Communities / ช่องทางที่น่าลอง

ควรอ่านกฎของแต่ละกลุ่มก่อนโพสต์ และถ้าเป็นกลุ่มที่ห้ามโปรโมต ให้ขออนุญาต admin ก่อน

- AI Thailand / AI Thailand Community: https://www.ai.in.th/
- Data Science Thailand: https://www.facebook.com/DataScienceTh/
- Global AI Bangkok: https://www.meetup.com/global-ai-thailand/
- PyCon Thailand / Python community: https://th.pycon.org/
- ThaiPy, Bangkok AI, Data Science meetup communities
- LinkedIn post with tags such as `AI safety`, `LLM evaluation`, `Thai AI`
- GitHub repository Issues for structured cases

## Posting Order / ลำดับที่แนะนำ

1. โพสต์ Facebook ส่วนตัวก่อน
2. ส่งให้เพื่อน 5-10 คนที่ไม่ใช่นักพัฒนา เพื่อดูว่างงไหม
3. โพสต์ในกลุ่ม AI/ChatGPT ไทยแบบขอ feedback
4. โพสต์ LinkedIn แบบเน้นผู้พัฒนาและ AI safety
5. หลังมีผล 30-50 เคส ค่อยสรุปเป็น report

## What Not To Do / สิ่งที่ไม่ควรทำ

- อย่าโพสต์ว่าเป็น ELUZA AI เต็มตัว
- อย่าอ้างว่าระบบรับประกันความจริง 100%
- อย่าโพสต์ถี่จนดูเป็น spam
- อย่าให้คนใส่ข้อมูลส่วนตัว รหัสผ่าน API key เอกสารลับ หรือข้อมูลสุขภาพจริง
- อย่าขอให้คนเปิดเผยข้อมูล private ของตัวเองเพื่อทดสอบ

## Reply Template / ข้อความตอบคนถามว่า “มันทำอะไร”

```text
มันคือเครื่องมือตรวจคำตอบ AI ครับ

ปกติเราไปถาม AI แล้ว AI ตอบมา แต่เราไม่รู้ว่าควรเชื่อไหม
เครื่องมือนี้ให้เราเอาคำถาม คำตอบ และหลักเกณฑ์ที่อยากให้ยึด มาใส่
แล้วระบบจะช่วยบอกว่าคำตอบนั้นควรใช้ได้ไหม ต้องหาหลักฐานเพิ่มไหม หรือควรปฏิเสธ

มันไม่ได้แทนผู้เชี่ยวชาญ และไม่ใช่ ELUZA AI เต็มตัว
ตอนนี้เปิดให้ช่วยทดสอบว่าแนวคิดนี้ใช้งานจริงเข้าใจง่ายไหมครับ
```
