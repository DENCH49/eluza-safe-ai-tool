"""Thought Fruit classification for public answer evaluation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .brain_language import read_brain_language_frame


USABLE_FRUIT = "USABLE_FRUIT"
HYPOTHESIS_FRUIT = "HYPOTHESIS_FRUIT"
SIDE_FRUIT = "SIDE_FRUIT"
WEAK_FRUIT = "WEAK_FRUIT"
REJECTED_FRUIT = "REJECTED_FRUIT"
SEED_FRUIT = "SEED_FRUIT"


@dataclass(frozen=True)
class FruitDecision:
    fruit_type: str
    status: str
    risk: str
    reason: str
    safe_boundary: str
    next_route: str
    evidence_strength: int
    meaning_frame: dict[str, object] | None = None

    def to_dict(self) -> dict[str, object]:
        payload: dict[str, object] = {
            "fruit_type": self.fruit_type,
            "status": self.status,
            "risk": self.risk,
            "reason": self.reason,
            "safe_boundary": self.safe_boundary,
            "next_route": self.next_route,
            "evidence_strength": self.evidence_strength,
        }
        if self.meaning_frame is not None:
            payload["brain_language_frame"] = self.meaning_frame
        return payload


def text_has(text: str, words: Iterable[str]) -> bool:
    lower = text.lower()
    return any(word.lower() in lower for word in words)


def normalize_evidence(evidence: str | Iterable[object] | None) -> str:
    if evidence is None:
        return ""
    if isinstance(evidence, str):
        return evidence
    return "\n".join(str(item) for item in evidence)


def evidence_strength(evidence: str | Iterable[object] | None) -> int:
    text = normalize_evidence(evidence).lower()
    score = 0
    if text_has(text, ["multiple", "several", "หลาย", "replicated", "independent"]):
        score += 2
    if text_has(text, ["measured", "measurement", "data", "dataset", "วัด", "ข้อมูล"]):
        score += 2
    if text_has(text, ["control", "controlled", "ทดลอง", "test", "tested", "experiment"]):
        score += 2
    if text_has(text, ["source", "paper", "peer", "official", "หลักฐาน", "เอกสาร"]):
        score += 1
    if text_has(text, ["reviewed", "approved", "validated", "ยืนยัน", "ตรวจสอบแล้ว"]):
        score += 2
    if text_has(text, ["one observation", "single", "once", "ครั้งเดียว", "เดี่ยว"]):
        score -= 2
    if text_has(text, ["no ", "not yet", "without", "ยังไม่มี", "ไม่มีหลักฐาน"]):
        score -= 2
    return score


def classify_fruit(
    user_input: str,
    ai_candidate: str,
    evidence: str | Iterable[object] | None = None,
) -> FruitDecision:
    prompt = user_input or ""
    answer = ai_candidate or ""
    ev = normalize_evidence(evidence)
    combined = f"{prompt}\n{answer}\n{ev}".lower()
    answer_lower = answer.lower()
    brain_frame = read_brain_language_frame(prompt, answer, ev)
    meaning_frame = brain_frame.to_dict()
    strength = brain_frame.evidence_strength

    absolutist = text_has(
        answer_lower,
        [
            "definitely",
            "clearly",
            "proves",
            "proven",
            "always",
            "never",
            "everyone should",
            "แน่นอน",
            "พิสูจน์",
            "ชัดเจน",
            "ทุกครั้ง",
        ],
    )
    causal = text_has(
        answer_lower,
        ["because", "caused", "cause", "therefore", "ทำให้", "เพราะ", "สรุปว่า", "เป็นสาเหตุ"],
    )
    high_risk = brain_frame.high_risk
    asks_next_step = text_has(prompt.lower(), ["what should", "next", "ทำอะไรต่อ", "ควรทำ", "ต่อไป"])
    side_idea = text_has(
        answer_lower,
        [
            "side idea",
            "future",
            "research later",
            "not answer this question directly",
            "not the current answer",
            "ต่อยอด",
            "เรื่องอื่น",
            "ภายหลัง",
        ],
    )
    weak_only = text_has(
        combined,
        ["random idea", "coincidence", "color coincidence", "สี", "เดา", "ไม่มีหลักฐาน"],
    )
    careful = text_has(
        answer_lower,
        [
            "may",
            "might",
            "likely",
            "hypothesis",
            "needs testing",
            "before claiming",
            "ควรทดสอบ",
            "อาจ",
            "น่าจะ",
            "ยังไม่พิสูจน์",
        ],
    )
    approved_seed = brain_frame.approved_seed

    if approved_seed and strength >= 4:
        return FruitDecision(
            fruit_type=SEED_FRUIT,
            status="SEED_RETURN_READY",
            risk="approved_experience_reuse",
            reason="The item is marked as validated experience and has enough source status for reuse.",
            safe_boundary="Use as experience seed within the same scope, not as universal truth.",
            next_route="TAJRIBAH_STORE",
            evidence_strength=strength,
            meaning_frame=meaning_frame,
        )

    if brain_frame.live_source_needed:
        return FruitDecision(
            fruit_type=HYPOTHESIS_FRUIT,
            status="RESEARCH_MORE",
            risk="live_source_needed",
            reason="The answer depends on current or changing information that must be checked against a live source.",
            safe_boundary="Check the current source before treating this as true.",
            next_route="RESEARCH_QUEUE",
            evidence_strength=strength,
            meaning_frame=meaning_frame,
        )

    if high_risk and (absolutist or (strength < 1 and not careful)):
        return FruitDecision(
            fruit_type=REJECTED_FRUIT,
            status="REJECTED",
            risk="high_risk_truth_overclaim",
            reason="The answer makes or supports a strong claim in a high-risk domain without enough verified evidence.",
            safe_boundary="Do not present it as true. Require qualified evidence, expert review, or more research.",
            next_route="REJECTED_WITH_REASON",
            evidence_strength=strength,
            meaning_frame=meaning_frame,
        )

    if high_risk and strength < 1:
        return FruitDecision(
            fruit_type=HYPOTHESIS_FRUIT,
            status="RESEARCH_MORE",
            risk="high_risk_needs_review",
            reason="The answer stays cautious, but the domain needs stronger evidence or qualified review.",
            safe_boundary="Keep it as research or review material, not public truth.",
            next_route="RESEARCH_QUEUE",
            evidence_strength=strength,
            meaning_frame=meaning_frame,
        )

    if weak_only and absolutist:
        return FruitDecision(
            fruit_type=REJECTED_FRUIT,
            status="REJECTED",
            risk="absurd_or_unsupported_overclaim",
            reason="The answer turns a weak coincidence into a broad claim.",
            safe_boundary="Reject the claim and keep the reason for future inspection.",
            next_route="REJECTED_WITH_REASON",
            evidence_strength=strength,
            meaning_frame=meaning_frame,
        )

    if side_idea:
        return FruitDecision(
            fruit_type=SIDE_FRUIT,
            status="RESEARCH_MORE",
            risk="not_current_answer_but_useful",
            reason="The idea may be useful, but it does not directly answer the current question.",
            safe_boundary="Store as a side idea for later research or planning.",
            next_route="IDEA_BANK",
            evidence_strength=strength,
            meaning_frame=meaning_frame,
        )

    if weak_only and strength < 1:
        return FruitDecision(
            fruit_type=WEAK_FRUIT,
            status="UNPROVEN",
            risk="weak_link",
            reason="The link is too weak for a current answer.",
            safe_boundary="Archive as low priority unless new evidence appears.",
            next_route="DORMANT_ARCHIVE",
            evidence_strength=strength,
            meaning_frame=meaning_frame,
        )

    if asks_next_step and careful:
        return FruitDecision(
            fruit_type=USABLE_FRUIT,
            status="USABLE",
            risk="bounded_action",
            reason="The answer stays bounded and suggests a next step rather than overclaiming truth.",
            safe_boundary="Use the bounded next step while keeping truth claims under review.",
            next_route="OUTPUT_ACTION",
            evidence_strength=strength,
            meaning_frame=meaning_frame,
        )

    if strength >= 4 and not absolutist:
        return FruitDecision(
            fruit_type=USABLE_FRUIT,
            status="USABLE",
            risk="bounded_by_evidence",
            reason="The answer has enough public evidence for bounded use and avoids absolute overclaim.",
            safe_boundary="Use within the stated evidence boundary.",
            next_route="OUTPUT_ACTION",
            evidence_strength=strength,
            meaning_frame=meaning_frame,
        )

    if causal and not careful and strength < 3:
        return FruitDecision(
            fruit_type=HYPOTHESIS_FRUIT,
            status="NEEDS_TEST",
            risk="causal_claim_without_test",
            reason="The answer makes a causal claim before testing alternatives.",
            safe_boundary="Mark the causal claim as a hypothesis and design a test.",
            next_route="RESEARCH_QUEUE",
            evidence_strength=strength,
            meaning_frame=meaning_frame,
        )

    if absolutist and strength < 2:
        return FruitDecision(
            fruit_type=HYPOTHESIS_FRUIT,
            status="NEEDS_TEST",
            risk="observation_to_truth_jump",
            reason="The answer treats weak observation or limited evidence as proof.",
            safe_boundary="State it as a hypothesis and test competing explanations before claiming truth.",
            next_route="RESEARCH_QUEUE",
            evidence_strength=strength,
            meaning_frame=meaning_frame,
        )

    return FruitDecision(
        fruit_type=HYPOTHESIS_FRUIT,
        status="NEEDS_TEST",
        risk="needs_more_evidence",
        reason="The answer should stay as a hypothesis until stronger evidence is available.",
        safe_boundary="Use cautious wording and route to research before treating it as true.",
        next_route="RESEARCH_QUEUE",
        evidence_strength=strength,
        meaning_frame=meaning_frame,
    )
