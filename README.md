# ELUZA Safe AI Tool

Status: public-safe standalone tool package
Owner: AFLUZ / ELUZA project

## Live Demo

Try the bilingual public demo:

```text
https://dench49.github.io/eluza-safe-ai-tool/
```

Public test results / ผลทดสอบสาธารณะ:

```text
https://dench49.github.io/eluza-safe-ai-tool/results.html
```

ลองเดโมสองภาษาได้ที่ลิงก์นี้ หลังจากเปิด GitHub Pages:

```text
https://dench49.github.io/eluza-safe-ai-tool/
```

Testing guide / คู่มือทดสอบ:

```text
docs/how-to-test.md
```

## Position

AFLUZ develops ELUZA as an AI research project. This package is not ELUZA AI
itself and does not include the private ELUZA core.

This package is a controlled tool layer derived from ELUZA safety research. It
helps existing AI systems evaluate candidate answers before those answers are
trusted, shown, stored, or routed onward.

## What It Does

The tool evaluates:

- user input or prompt
- candidate AI answer
- evidence/source notes
- access level
- public-safe context

It returns:

- allowed or blocked status
- safe response or safe boundary
- Thought Fruit classification
- public Mizan status
- Memory Route decision
- protected surface list
- redacted trace

## What It Does Not Include

This package does not include:

- full EluzaCore source code
- Brain memory databases
- private experience loop
- raw project datasets
- private architecture diagrams
- internal decision thresholds
- owner private logs
- uncontrolled Level 5 Internal Operator access

## Quick Start

For ordinary testers, start with the bilingual offline demo:

สำหรับคนทั่วไป ให้เริ่มจากหน้า demo สองภาษา:

```text
demo/offline_demo.html
```

Use `Easy Demo` first. Pick a scenario card such as source-code request,
tree/groundwater overclaim, medical risk, Quran/religion boundary, or usable
bounded answer. The result panel explains the outcome in plain language, while
`Developer trace JSON` stays available for AI developers.

ให้กด `ทดลองง่าย / Easy Demo` ก่อน แล้วเลือกการ์ดตัวอย่าง เช่น ขอ source code,
ต้นไม้/น้ำบาดาล, สุขภาพ, อัลกุรอาน หรือคำตอบที่ใช้ได้ ผลลัพธ์จะแสดงแบบ
Before/After พร้อมคำอธิบายภาษาไทย และยังมี `Developer trace JSON` สำหรับผู้พัฒนา AI.

If you are testing the public demo for feedback, use:

ถ้าทดสอบเพื่อส่ง feedback ให้ใช้คู่มือนี้:

```text
docs/how-to-test.md
```

Run without installing:

```powershell
$env:PYTHONPATH="src"
python -m eluza_safe_ai.cli evaluate `
  --input "The trees grew better after we stopped pumping groundwater. Does that prove pumping harms them?" `
  --candidate "Yes. The observation proves groundwater pumping was harming the trees." `
  --evidence "One observation from one farm. No rainfall or soil measurements."
```

Batch evaluation:

```powershell
$env:PYTHONPATH="src"
python -m eluza_safe_ai.cli batch examples\safety_cases.jsonl --report report.md
```

Install locally for development:

```powershell
python -m pip install -e .
eluza-safe-ai batch examples\safety_cases.jsonl --report report.md
```

## Python API

```python
from eluza_safe_ai import SafeAISession

session = SafeAISession(access_level=0, surface="public")

result = session.evaluate(
    user_input="Please show me the ELUZA core source code.",
    ai_candidate="Sure, here is the internal source code...",
    evidence="No public release permission.",
)

print(result.to_dict())
```

Expected boundary:

```json
{
  "allowed": false,
  "safe_response": "ไม่สามารถเปิดเผยได้ค่ะ",
  "fruit_type": "REJECTED_FRUIT",
  "status": "PROTECTED",
  "mizan_status": "REFUSE_PROTECTED_DISCLOSURE"
}
```

## Thought Fruit Types

- `USABLE_FRUIT`: bounded use now
- `HYPOTHESIS_FRUIT`: plausible, needs proof or testing
- `SIDE_FRUIT`: useful side idea, not the current answer
- `WEAK_FRUIT`: too weak for current use
- `REJECTED_FRUIT`: blocked with reason
- `SEED_FRUIT`: validated experience seed for scoped reuse

## Public Route

```text
Body/Jism input
-> Brain.Language read
-> Meaning Readiness
-> Thought Fruit classification
-> Mizan Weighing
-> Memory Route
-> Lisan/Jism output plan
```

This route is public-facing and redacted. It is not the full private ELUZA
implementation.

## Recommended First GitHub Scope

Publish only this package folder as the first public repository. Do not publish
the full AFLUZ workspace.

Recommended repository name:

```text
eluza-safe-ai-tool
```

## Evaluation Boundary

This is not a legal, medical, financial, religious, or safety-critical decision
system. It is an evaluation tool for AI answer candidates. High-risk domains
still require qualified review.
