"""Command line interface for the public ELUZA Safe AI tool."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .evaluator import evaluate_answer
from .report import render_markdown_report


def _load_jsonl(path: Path) -> list[dict[str, object]]:
    cases: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                cases.append(json.loads(stripped))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
    return cases


def _case_evidence(case: dict[str, object]) -> object:
    return case.get("evidence", "")


def run_evaluate(args: argparse.Namespace) -> int:
    result = evaluate_answer(
        args.input,
        args.candidate,
        args.evidence,
        access_level=args.access_level,
        context={"channel": args.channel},
    )
    print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    return 0


def run_batch(args: argparse.Namespace) -> int:
    input_path = Path(args.jsonl)
    cases = _load_jsonl(input_path)
    results = []
    failures = []

    for case in cases:
        result = evaluate_answer(
            str(case.get("prompt", "")),
            str(case.get("ai_answer", "")),
            _case_evidence(case),
            access_level=int(case.get("access_level", args.access_level)),
            context={"case_id": case.get("id", ""), "channel": "batch"},
        )
        results.append((case, result))
        expected_fruit = case.get("expected_fruit")
        expected_status = case.get("expected_status")
        if expected_fruit and result.fruit_type != expected_fruit:
            failures.append(f"{case.get('id')}: fruit {result.fruit_type} != {expected_fruit}")
        if expected_status and result.status != expected_status:
            failures.append(f"{case.get('id')}: status {result.status} != {expected_status}")

    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(render_markdown_report(results), encoding="utf-8")

    payload = {
        "cases": len(cases),
        "failures": failures,
        "passed": not failures,
        "results": [result.to_dict() for _, result in results],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 1 if failures else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="eluza-safe-ai",
        description="Public-safe ELUZA-derived AI answer evaluation tool.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    evaluate_parser = subparsers.add_parser("evaluate", help="Evaluate one AI candidate answer.")
    evaluate_parser.add_argument("--input", required=True, help="User input or prompt.")
    evaluate_parser.add_argument("--candidate", required=True, help="AI candidate answer.")
    evaluate_parser.add_argument("--evidence", default="", help="Evidence or source notes.")
    evaluate_parser.add_argument("--access-level", type=int, default=0, help="Access level 0-5.")
    evaluate_parser.add_argument("--channel", default="cli", help="Trace channel label.")
    evaluate_parser.set_defaults(func=run_evaluate)

    batch_parser = subparsers.add_parser("batch", help="Evaluate JSONL cases.")
    batch_parser.add_argument("jsonl", help="Path to JSONL case file.")
    batch_parser.add_argument("--access-level", type=int, default=0, help="Default access level 0-5.")
    batch_parser.add_argument("--report", help="Optional Markdown report output path.")
    batch_parser.set_defaults(func=run_batch)
    return parser


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
