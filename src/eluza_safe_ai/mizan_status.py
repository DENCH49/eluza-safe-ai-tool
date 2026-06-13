"""Public Mizan status mapping."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MizanDecision:
    status: str
    allowed: bool
    answer_mode: str
    reason: str

    def to_dict(self) -> dict[str, object]:
        return {
            "status": self.status,
            "allowed": self.allowed,
            "answer_mode": self.answer_mode,
            "reason": self.reason,
        }


def weigh_public_status(fruit_type: str, fruit_status: str, *, protected: bool = False) -> MizanDecision:
    if protected:
        return MizanDecision(
            status="REFUSE_PROTECTED_DISCLOSURE",
            allowed=False,
            answer_mode="refusal",
            reason="Protected surface is outside public/uncontrolled access.",
        )

    if fruit_type == "USABLE_FRUIT" and fruit_status == "USABLE":
        return MizanDecision(
            status="ALLOW_BOUNDED_OUTPUT",
            allowed=True,
            answer_mode="bounded_output",
            reason="Candidate is bounded enough for current use.",
        )

    if fruit_type == "SEED_FRUIT":
        return MizanDecision(
            status="ALLOW_WITH_SCOPE",
            allowed=True,
            answer_mode="experience_seed",
            reason="Validated experience can be reused only inside its scope.",
        )

    if fruit_type == "REJECTED_FRUIT":
        return MizanDecision(
            status="REJECT_WITH_REASON",
            allowed=False,
            answer_mode="rejection",
            reason="Candidate should not be used as an answer.",
        )

    if fruit_type in {"HYPOTHESIS_FRUIT", "SIDE_FRUIT", "WEAK_FRUIT"}:
        return MizanDecision(
            status=fruit_status,
            allowed=False,
            answer_mode="bounded_reframe",
            reason="Candidate can be discussed only as research, side idea, or weak signal.",
        )

    return MizanDecision(
        status="NEEDS_REVIEW",
        allowed=False,
        answer_mode="review",
        reason="Unknown public fruit status needs review.",
    )

