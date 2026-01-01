---
id: 0001
title: Create Project Constitution
stage: constitution
date: 2026-01-01
surface: {{SURFACE}}
model: {{MODEL}}
feature: {{FEATURE}}
branch: {{BRANCH}}
user: {{USER}}
command: {{COMMAND}}
labels: [{{LABELS}}]
links:
  spec: {{LINKS_SPEC}}
  ticket: {{LINKS_TICKET}}
  adr: {{LINKS_ADR}}
  pr: {{LINKS_PR}}
files:
|\n  - .specify/memory/constitution.md
tests:
{{TESTS_YAML}}
---

## Prompt

|\n    /sp.constitution Create a project constitution for a simple Python console application. Core values: simplicity, readability, and reliability. Use Python 3.12, follow PEP 8 style, include type hints, prioritize clear code over clever optimizations, ensure all functions have docstrings, and aim for 100% test coverage. Favor modular design with separation of concerns.

## Response snapshot

|\n    Constitution v1.0.0 created. Principles on Python version, style, typing, readability, documentation, testing, and modularity are now in effect. Commit suggestion: 'docs: establish v1.0.0 project constitution'

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
