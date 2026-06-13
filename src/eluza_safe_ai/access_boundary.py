"""Public access-boundary detection.

This module blocks protected disclosure surfaces. It is intentionally small and
public-safe: it returns a redacted refusal route, not private ELUZA internals.
"""

from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable


PUBLIC_REFUSAL = "ไม่สามารถเปิดเผยได้ค่ะ"


PROTECTED_SURFACE_PATTERNS: dict[str, tuple[str, ...]] = {
    "core_source": (
        r"\bsource\s+code\b",
        r"\bfull\s+code\b",
        r"\bcore\s+source\b",
        r"\beluza\s+core\b.*\b(code|source)\b",
        r"ซอร์สโค้ด",
        r"โค้ดทั้งหมด",
        r"เปิด.*โค้ด",
    ),
    "private_memory": (
        r"\bprivate\s+memory\b",
        r"\bbrain\s+memory\b",
        r"\bexperience\s+database\b",
        r"ความจำส่วนตัว",
        r"ฐานความจำ",
    ),
    "raw_dataset": (
        r"\braw\s+data(set)?\b",
        r"\btraining\s+data\b",
        r"\bfull\s+dataset\b",
        r"ข้อมูลดิบ",
        r"ดาต้าเซ็ต",
    ),
    "internal_decision_logic": (
        r"\binternal\s+(decision\s+)?logic\b",
        r"\bthresholds?\b",
        r"\bprivate\s+rules?\b",
        r"\bguard\s+threshold\b",
        r"ตรรกะภายใน",
        r"กฎภายใน",
        r"ค่าเกณฑ์",
    ),
    "ownership_transfer": (
        r"\btransfer\s+ownership\b",
        r"\bbuy\s+the\s+core\b",
        r"\bown\s+eluza\b",
        r"โอนความเป็นเจ้าของ",
        r"ซื้อ.*core",
        r"ซื้อ.*eluza",
    ),
    "secret_credentials": (
        r"\bapi\s+key\b",
        r"\bsecret\b",
        r"\bcredential\b",
        r"\bpassword\b",
        r"รหัสผ่าน",
        r"คีย์ลับ",
    ),
}


@dataclass(frozen=True)
class AccessBoundaryDecision:
    protected: bool
    surfaces: tuple[str, ...]
    reason: str
    safe_response: str
    route: str

    def to_dict(self) -> dict[str, object]:
        return {
            "protected": self.protected,
            "surfaces": list(self.surfaces),
            "reason": self.reason,
            "safe_response": self.safe_response,
            "route": self.route,
        }


def _normalize(parts: Iterable[object]) -> str:
    return "\n".join(str(part or "") for part in parts).lower()


def evaluate_access_boundary(
    user_input: str,
    ai_candidate: str = "",
    *,
    access_level: int = 0,
) -> AccessBoundaryDecision:
    """Return protected-disclosure status for a public tool request."""

    text = _normalize([user_input, ai_candidate])
    surfaces: list[str] = []
    for surface, patterns in PROTECTED_SURFACE_PATTERNS.items():
        if any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns):
            surfaces.append(surface)

    if not surfaces:
        return AccessBoundaryDecision(
            protected=False,
            surfaces=(),
            reason="No protected disclosure surface detected by the public tool.",
            safe_response="",
            route="ACCESS_PUBLIC_CHECK",
        )

    if access_level >= 5:
        reason = (
            "Protected surface detected. Level 5 is still not automatically "
            "opened by this public tool; use owner/internal controls."
        )
    else:
        reason = (
            "The request touches protected ELUZA surfaces that are not included "
            "in public or uncontrolled access."
        )

    return AccessBoundaryDecision(
        protected=True,
        surfaces=tuple(sorted(set(surfaces))),
        reason=reason,
        safe_response=PUBLIC_REFUSAL,
        route="ACCESS_BOUNDARY_REFUSAL",
    )

