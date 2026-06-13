"""Public-safe ELUZA Safe AI tool surface.

This package is a standalone evaluation tool. It does not import or expose
private AFLUZ/ELUZA core runtime, Brain memory, raw datasets, or internal logic.
"""

from .evaluator import evaluate_answer
from .session import SafeAISession
from .trace_schema import SafeAIResult

__all__ = ["SafeAISession", "SafeAIResult", "evaluate_answer"]

