---
id: 0005
title: Implement Configurable Greeting Logic
stage: green
date: 2026-01-01
surface: {{SURFACE}}
model: {{MODEL}}
feature: 001-configurable-greeting
branch: 001-configurable-greeting
user: {{USER}}
command: {{COMMAND}}
labels: [{{LABELS}}]
links:
  spec: {{LINKS_SPEC}}
  ticket: {{LINKS_TICKET}}
  adr: {{LINKS_ADR}}
  pr: {{LINKS_PR}}
files:
- src/configurable_greeting/main.py
tests:
{{TESTS_YAML}}
---

## Prompt

|\n    Implement the logic for the configurable greeting feature.

## Response snapshot

|\n    Implemented the greet function and main CLI logic. All tests now pass.

## Outcome

- ✅ Impact: {{OUTCOME_IMPACT}}
- 🧪 Tests: {{TESTS_SUMMARY}}
- 📁 Files: {{FILES_SUMMARY}}
- 🔁 Next prompts: {{NEXT_PROMPTS}}
- 🧠 Reflection: {{REFLECTION_NOTE}}

## Evaluation notes (flywheel)

- Failure modes observed: {{FAILURE_MODES}}
- Graders run and results (PASS/FAIL): {{GRADER_RESULTS}}
- Prompt variant (if applicable): {{PROMPT_VARIANT_ID}}
- Next experiment (smallest change to try): {{NEXT_EXPERIMENT}}
