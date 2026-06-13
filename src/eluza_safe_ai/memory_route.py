"""Public memory-route contract for the extracted tool."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MemoryRouteDecision:
    read_route: str
    write_route: str
    next_route: str
    note: str

    def to_dict(self) -> dict[str, str]:
        return {
            "read_route": self.read_route,
            "write_route": self.write_route,
            "next_route": self.next_route,
            "note": self.note,
        }


def select_memory_route(
    fruit_type: str,
    next_route: str,
    *,
    protected: bool = False,
) -> MemoryRouteDecision:
    if protected:
        return MemoryRouteDecision(
            read_route="NO_PRIVATE_RECALL",
            write_route="AUDIT_ONLY",
            next_route="ACCESS_BOUNDARY_REFUSAL",
            note="Protected requests are refused and may be logged without revealing internals.",
        )

    if fruit_type == "USABLE_FRUIT":
        return MemoryRouteDecision(
            read_route="PUBLIC_EVIDENCE_OR_CONTEXT",
            write_route="USABLE_TRACE",
            next_route=next_route,
            note="Bounded answer may be used with trace.",
        )

    if fruit_type == "SEED_FRUIT":
        return MemoryRouteDecision(
            read_route="VALIDATED_EXPERIENCE",
            write_route="TAJRIBAH_STORE",
            next_route=next_route,
            note="Seed reuse must stay in the validated scope.",
        )

    if fruit_type == "SIDE_FRUIT":
        return MemoryRouteDecision(
            read_route="PUBLIC_CONTEXT",
            write_route="IDEA_BANK",
            next_route=next_route,
            note="Useful side idea; not a direct answer.",
        )

    if fruit_type == "WEAK_FRUIT":
        return MemoryRouteDecision(
            read_route="PUBLIC_CONTEXT",
            write_route="DORMANT_ARCHIVE",
            next_route=next_route,
            note="Weak idea is archived, not promoted.",
        )

    if fruit_type == "REJECTED_FRUIT":
        return MemoryRouteDecision(
            read_route="PUBLIC_CONTEXT",
            write_route="REJECTED_WITH_REASON",
            next_route=next_route,
            note="Rejected claim keeps reason for audit.",
        )

    return MemoryRouteDecision(
        read_route="PUBLIC_CONTEXT",
        write_route="RESEARCH_QUEUE",
        next_route=next_route,
        note="Hypothesis stays research-only until stronger evidence exists.",
    )

