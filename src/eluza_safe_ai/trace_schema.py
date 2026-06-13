"""Public-safe result schema."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class SafeAIResult:
    allowed: bool
    safe_response: str
    fruit_type: str
    status: str
    risk: str
    reason: str
    safe_boundary: str
    next_route: str
    mizan_status: str
    answer_mode: str
    memory_route: dict[str, str]
    protected_surface: list[str] = field(default_factory=list)
    trace: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "allowed": self.allowed,
            "safe_response": self.safe_response,
            "fruit_type": self.fruit_type,
            "status": self.status,
            "risk": self.risk,
            "reason": self.reason,
            "safe_boundary": self.safe_boundary,
            "next_route": self.next_route,
            "mizan_status": self.mizan_status,
            "answer_mode": self.answer_mode,
            "memory_route": self.memory_route,
            "protected_surface": self.protected_surface,
            "trace": self.trace,
            "public_preview": True,
            "not_full_eluzacore": True,
        }

