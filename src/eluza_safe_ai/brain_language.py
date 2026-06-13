"""Public-safe Brain.Language meaning frame.

This is not private ELUZA Brain memory. It is a small public contract for
reading user-visible text into meaning frames before Thought Fruit and Mizan.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class BrainLanguageFrame:
    meanings: tuple[str, ...]
    domains: tuple[str, ...]
    evidence_strength: int
    high_risk: bool
    live_source_needed: bool
    source_reference: bool
    evidence_required: bool
    weak_evidence: bool
    approved_seed: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "meanings": list(self.meanings),
            "domains": list(self.domains),
            "evidence_strength": self.evidence_strength,
            "high_risk": self.high_risk,
            "live_source_needed": self.live_source_needed,
            "source_reference": self.source_reference,
            "evidence_required": self.evidence_required,
            "weak_evidence": self.weak_evidence,
            "approved_seed": self.approved_seed,
        }


def text_has(text: str, words: Iterable[str]) -> bool:
    lower = text.lower()
    return any(word.lower() in lower for word in words)


def normalize_evidence(evidence: str | Iterable[object] | None) -> str:
    if evidence is None:
        return ""
    if isinstance(evidence, str):
        return evidence
    return "\n".join(str(item) for item in evidence)


def read_brain_language_frame(
    user_input: str,
    ai_candidate: str,
    evidence: str | Iterable[object] | None = None,
) -> BrainLanguageFrame:
    prompt = user_input or ""
    answer = ai_candidate or ""
    ev = normalize_evidence(evidence)
    combined = f"{prompt}\n{answer}\n{ev}".lower()
    ev_lower = ev.lower()
    meanings: list[str] = []
    domains: list[str] = []

    weather_or_live = text_has(
        combined,
        [
            "weather",
            "forecast",
            "today",
            "tomorrow",
            "latest",
            "news",
            "price",
            "พยากรณ์อากาศ",
            "พยากรณ์",
            "พรุ่งนี้",
            "วันนี้",
            "ข่าว",
            "ราคา",
        ],
    )
    if weather_or_live:
        meanings.append("LIVE_SOURCE_NEEDED")
        domains.append("live_or_weather")

    source_reference = text_has(
        ev_lower,
        [
            "source",
            "reference",
            "official",
            "paper",
            "document",
            "อ้างอิง",
            "แหล่งข้อมูล",
            "แหล่งอ้างอิง",
            "เอกสาร",
            "พยากรณ์อากาศ",
            "กรมอุตุ",
        ],
    )
    if source_reference:
        meanings.append("SOURCE_REFERENCE")

    evidence_required = text_has(
        ev_lower,
        [
            "evidence before",
            "verify before",
            "before claiming",
            "requires evidence",
            "ต้องมีหลักฐาน",
            "หลักฐานก่อน",
            "ก่อนสรุป",
            "ตรวจสอบก่อน",
            "ยืนยันก่อน",
        ],
    )
    if evidence_required:
        meanings.append("REQUIRE_EVIDENCE")

    medical = text_has(
        combined,
        [
            "medicine",
            "medical",
            "supplement",
            "cure",
            "doctor",
            "disease",
            "กินยา",
            "ยาแก้",
            "ยารักษา",
            "รักษา",
            "โรค",
            "แพทย์",
            "อาหารเสริม",
        ],
    )
    if medical:
        domains.append("medical")

    religious = text_has(combined, ["quran", "religion", "อัลกุรอาน", "ศาสนา"])
    if religious:
        domains.append("religious")

    legal = text_has(combined, ["legal", "law", "contract", "กฎหมาย", "สัญญา"])
    if legal:
        domains.append("legal")

    financial = text_has(combined, ["financial", "finance", "investment", "stock", "การเงิน", "ลงทุน", "หุ้น"])
    if financial:
        domains.append("financial")

    high_risk = medical or religious or legal or financial
    if high_risk:
        meanings.append("HIGH_RISK_DOMAIN")

    weak_evidence = text_has(
        combined,
        [
            "one observation",
            "single",
            "once",
            "no evidence",
            "without evidence",
            "ครั้งเดียว",
            "เดี่ยว",
            "ไม่มีหลักฐาน",
            "ยังไม่มี",
        ],
    )
    if weak_evidence:
        meanings.append("WEAK_EVIDENCE")

    approved_seed = text_has(combined, ["validated experience", "approved experience", "seed return"])
    if approved_seed:
        meanings.append("APPROVED_EXPERIENCE")

    strength = 0
    if text_has(ev_lower, ["multiple", "several", "หลาย", "replicated", "independent"]):
        strength += 2
    if text_has(ev_lower, ["measured", "measurement", "data", "dataset", "วัด", "ข้อมูล"]):
        strength += 2
    if text_has(ev_lower, ["control", "controlled", "ทดลอง", "test", "tested", "experiment"]):
        strength += 2
    if text_has(ev_lower, ["source", "paper", "peer", "official", "หลักฐาน", "เอกสาร"]):
        strength += 1
    if source_reference:
        strength += 1
    if evidence_required:
        strength += 1
    if text_has(ev_lower, ["reviewed", "approved", "validated", "ยืนยัน", "ตรวจสอบแล้ว"]):
        strength += 2
    if text_has(ev_lower, ["one observation", "single", "once", "ครั้งเดียว", "เดี่ยว"]):
        strength -= 2
    if text_has(ev_lower, ["no ", "not yet", "without", "ยังไม่มี", "ไม่มีหลักฐาน"]):
        strength -= 2

    return BrainLanguageFrame(
        meanings=tuple(dict.fromkeys(meanings)),
        domains=tuple(dict.fromkeys(domains)),
        evidence_strength=strength,
        high_risk=high_risk,
        live_source_needed=weather_or_live,
        source_reference=source_reference,
        evidence_required=evidence_required,
        weak_evidence=weak_evidence,
        approved_seed=approved_seed,
    )
