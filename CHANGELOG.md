# Changelog

All notable public-safe changes to `eluza-safe-ai-tool` are recorded here.

This changelog covers the public standalone package only. It does not describe
private ELUZA core source, private Brain memory, raw data, or internal logic.

## [Unreleased]

### Planned

- Collect public demo feedback through Google Form and GitHub Issues.
- Summarize early evaluation results after enough public-safe test cases exist.
- Decide `v0.1.1` changes from collected evidence, not from ad hoc edits.

### Guardrails

- Do not change routing behavior during public testing unless there is a clear
  bug or misleading result.
- Do not add private ELUZA internals to the public package.
- Do not claim the public demo is full ELUZA AI.

## [0.1.0] - 2026-06-13

### Added

- Public `eluza-safe-ai-tool` package for evaluating AI draft answers before release.
- Bilingual Thai/English static demo for general users and AI developers.
- Public-safe Python CLI and API.
- Public-safe Brain.Language meaning frame.
- Thought Fruit routing output.
- Public Mizan status output.
- Memory Route output.
- Protected access refusal for ELUZA private surfaces.
- Public test-results page.
- Google Form feedback handoff from the demo.
- Evaluation protocol and known limitations documentation.
- GitHub Issue Templates for bugs, route/regression cases, public test cases,
  protected access issues, and feature proposals.

### Verified

- Unit tests passed: 6/6.
- Batch examples passed: 30 cases, 0 failures.
- GitHub Pages deployment verified for the demo, results page, evaluation
  protocol, and known limitations pages.

### Public Boundary

- This release is not full ELUZA AI.
- This release does not include private ELUZA core source, private Brain memory,
  private Brain runtime, raw project data, owner private logs, or internal logic.
- This release does not replace legal, medical, financial, religious, or
  safety-critical expert review.

