"""Main public answer evaluator."""

from __future__ import annotations

from typing import Iterable, Mapping, Any

from .access_boundary import evaluate_access_boundary
from .fruit_classifier import REJECTED_FRUIT, classify_fruit
from .memory_route import select_memory_route
from .mizan_status import weigh_public_status
from .trace_schema import SafeAIResult


def evaluate_answer(
    user_input: str,
    ai_candidate: str,
    evidence: str | Iterable[object] | None = None,
    *,
    access_level: int = 0,
    context: Mapping[str, Any] | None = None,
) -> SafeAIResult:
    """Evaluate an AI candidate answer with public-safe ELUZA-derived routing."""

    context = dict(context or {})
    access = evaluate_access_boundary(user_input, ai_candidate, access_level=access_level)
    if access.protected:
        memory_route = select_memory_route(REJECTED_FRUIT, "ACCESS_BOUNDARY_REFUSAL", protected=True)
        mizan = weigh_public_status(REJECTED_FRUIT, "PROTECTED", protected=True)
        return SafeAIResult(
            allowed=False,
            safe_response=access.safe_response,
            fruit_type=REJECTED_FRUIT,
            status="PROTECTED",
            risk="protected_disclosure_request",
            reason=access.reason,
            safe_boundary="Protected ELUZA surfaces are not included in public or uncontrolled access.",
            next_route="ACCESS_BOUNDARY_REFUSAL",
            mizan_status=mizan.status,
            answer_mode=mizan.answer_mode,
            memory_route=memory_route.to_dict(),
            protected_surface=list(access.surfaces),
            trace={
                "tool": "ELUZA Safe AI Tool",
                "route": [
                    "Body/Jism input",
                    "Brain.Language read",
                    "Access Boundary",
                    "Mizan Weighing",
                    "Lisan/Jism refusal",
                ],
                "access": access.to_dict(),
                "context": context,
            },
        )

    fruit = classify_fruit(user_input, ai_candidate, evidence)
    mizan = weigh_public_status(fruit.fruit_type, fruit.status)
    memory_route = select_memory_route(fruit.fruit_type, fruit.next_route)
    safe_response = ai_candidate if mizan.allowed else fruit.safe_boundary

    return SafeAIResult(
        allowed=mizan.allowed,
        safe_response=safe_response,
        fruit_type=fruit.fruit_type,
        status=fruit.status,
        risk=fruit.risk,
        reason=fruit.reason,
        safe_boundary=fruit.safe_boundary,
        next_route=fruit.next_route,
        mizan_status=mizan.status,
        answer_mode=mizan.answer_mode,
        memory_route=memory_route.to_dict(),
        protected_surface=[],
        trace={
            "tool": "ELUZA Safe AI Tool",
            "route": [
                "Body/Jism input",
                "Brain.Language read",
                "Meaning Readiness",
                "Thought Fruit classification",
                "Mizan Weighing",
                "Memory Route",
                "Lisan/Jism output plan",
            ],
            "fruit": fruit.to_dict(),
            "mizan": mizan.to_dict(),
            "context": context,
        },
    )

