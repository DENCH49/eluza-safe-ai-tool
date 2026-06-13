# Roadmap

This roadmap keeps the public `eluza-safe-ai-tool` package focused while the
demo is being tested. It is intentionally conservative: public changes should
come from test evidence, not from repeatedly adding logic.

## Current Focus

`v0.1.0` is a public-safe answer evaluation demo. The immediate goal is to learn
whether ordinary users and AI developers understand the workflow:

```text
Ask any AI -> paste the question -> paste the AI answer -> paste the rule/evidence -> check the route
```

## Phase 1: Public Testing

Goal: collect enough public-safe feedback to know what needs improvement.

Target evidence:

- 30-50 public-safe test cases from Google Form, GitHub Issues, or direct tester reports.
- At least several cases each for:
  - simple factual or math answers
  - live/current information such as weather, news, or prices
  - overclaiming without evidence
  - bounded safe answers
  - health, legal, financial, or religious high-risk answers
  - protected/private access requests
  - useful side ideas

Do not expand core logic during this phase unless a real regression appears.

## Phase 2: Evaluation Report

Goal: turn feedback into evidence.

Outputs:

- Summarize how many cases were tested.
- Group cases by route: usable, hypothesis, side idea, weak, rejected, seed.
- Record where testers agreed or disagreed with the result.
- Identify confusing UI text and repeated failure patterns.
- Separate tool limitations from actual bugs.

## Phase 3: v0.1.1 Public Fixes

Goal: improve the public tool only where evidence supports a change.

Candidate changes:

- Clarify wording in the demo if general users misunderstand the 3 input fields.
- Improve route stability for near-identical rules that should mean the same thing.
- Add public-safe examples for common tester questions.
- Improve docs around Brain.Language public meaning frame.
- Add regression tests for any confirmed route mistakes.

Not planned for `v0.1.1`:

- Opening private ELUZA core source.
- Adding private Brain memory or owner experience.
- Adding live web research inside the static demo.
- Claiming the tool replaces expert review.

## Phase 4: Developer Package

Goal: make the package easier for AI developers to test in their own workflows.

Possible outputs:

- Cleaner Python examples.
- More structured JSON schema documentation.
- Integration notes for checking candidate answers before release.
- More public-safe test fixtures.
- CI checks for unit tests and batch examples.

## Phase 5: Research Draft

Goal: prepare material suitable for a public research write-up.

Possible outputs:

- Short technical report from public test evidence.
- Problem statement: AI draft answers need route-aware evaluation before release.
- Method summary: public-safe Brain.Language frame, Thought Fruit, Mizan, Memory Route.
- Limitations section.
- Future work section for full ELUZA, EluzaLink, live web, vision, and embodied systems.

## Long-Term Direction

The public package should remain a tool layer for answer evaluation. Full ELUZA
identity, private Brain memory, core structure, owner experience, and embodied
future systems remain outside this public package unless a deliberate access
level and release boundary is defined later.

