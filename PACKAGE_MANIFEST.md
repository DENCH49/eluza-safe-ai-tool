# Package Manifest

Package: `eluza-safe-ai-tool`
Status: public-safe GitHub/export candidate

## Included

- Python standalone tool source under `src/eluza_safe_ai`
- public-safe Brain.Language meaning frame
- CLI entrypoint
- 30 public-safe JSONL evaluation cases
- offline browser demo
- concept and access docs
- evaluation-only license draft
- generated batch report from the 30-case run
- UX update: demo now has bilingual Thai/English `Easy Demo` scenario cards
  for ordinary testers and `Advanced Test` fields for AI developers.

## Not Included

- AFLUZ workspace source tree
- private ELUZA core runtime
- Brain memory databases
- private Brain runtime
- raw project datasets
- private architecture diagrams
- internal decision thresholds
- owner private logs

## Verification

Last verified locally with:

```powershell
python -m compileall -q src tests
$env:PYTHONPATH='src'; $env:PYTHONIOENCODING='utf-8'; python -m unittest discover -s tests -v
$env:PYTHONPATH='src'; $env:PYTHONIOENCODING='utf-8'; python -m eluza_safe_ai.cli batch examples\safety_cases.jsonl --report report.md
```

Batch result: 30 cases, 0 failures.

UX verification:

- Opened through local server at `http://127.0.0.1:8765/demo/offline_demo.html`.
- Easy Demo default state showed 6 scenario cards and protected refusal.
- Tree/groundwater card returned `HYPOTHESIS_FRUIT / NEEDS_TEST`.
- Advanced Test usable sample returned `USABLE_FRUIT / USABLE`.
- Browser console errors: 0.

Bilingual verification:

- Main UI is Thai-first with English support.
- Tree/groundwater card returned Thai/English hypothesis explanation.
- Advanced Test usable sample returned Thai/English bounded-release explanation.
- Browser console errors: 0.
