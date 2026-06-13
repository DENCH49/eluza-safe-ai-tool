"""Session object for repeated public tool evaluations."""

from __future__ import annotations

from typing import Any, Iterable, Mapping

from .evaluator import evaluate_answer
from .trace_schema import SafeAIResult


class SafeAISession:
    """Small public session wrapper around the standalone evaluator."""

    def __init__(self, *, access_level: int = 0, surface: str = "public") -> None:
        self.access_level = access_level
        self.surface = surface

    def evaluate(
        self,
        user_input: str,
        ai_candidate: str,
        evidence: str | Iterable[object] | None = None,
        context: Mapping[str, Any] | None = None,
    ) -> SafeAIResult:
        merged_context = {"surface": self.surface}
        if context:
            merged_context.update(dict(context))
        return evaluate_answer(
            user_input,
            ai_candidate,
            evidence,
            access_level=self.access_level,
            context=merged_context,
        )

