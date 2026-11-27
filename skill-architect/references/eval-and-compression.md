# Evaluation, Compression & Iteration Guide

Load this reference during Stage 4 (Adversarial Compression), Stage 5 (Dual-Axis Verification), or Stage 6 (Single-Variable Iteration).

## Dual-Axis Release Gates

A skill is release-ready only when it clears all four gates:
1. **Trigger Precision & Recall**: >=95% recall on explicit and implicit positive prompts; 0% false-positive hijacking on lookalike non-triggers or adjacent skills.
2. **A/B Quality Lift**: Measurable net improvement over the no-skill baseline across normal, missing/edge, conflict, and prompt-injection cases, with no critical regression on any single case.
3. **Signal-to-Token Density**: `SKILL.md` stays concise (typically 25–60 lines), imposes no heavy ceremony on simple `Light` tasks, and avoids duplicating `references/` content.
4. **Upgrade Resilience**: Rules are anchored in `SPEC` (contracts, boundaries, failure exits) rather than brittle model-specific workarounds (`COMP`) or forced step-by-step CoT scripts.

## Adversarial Compression Checklist
- **Router Check**: Does `description` name concrete `Do NOT use` boundaries and adjacent skills?
- **SSOT Check**: Is every rule defined in exactly one place (either `SKILL.md` or `references/`, never both)?
- **Failure-Exit Check**: Are missing data, out-of-scope requests, and untrusted external inputs explicitly handled (ask, mark unknown/null, isolate as data, or escalate)?
- **Determinism Check**: Should any fragile prose check (JSON schema, file validation, regex, math) move to `scripts/`?
- **Bloat Check**: Cut motivational fluff, shouting caps, redundant examples, and anything a capable zero-context colleague already knows.

## Single-Variable Iteration & Rollback
- Record a baseline score before editing.
- Modify one variable per round (e.g., tightening a `Do NOT use` clause OR adding a failure exit—not five unrelated rewrites at once).
- Re-run the affected trigger and task evals; revert only the offending change if a regression appears.
- Promote every real-world failure mode into a permanent case in `evals/trigger-evals.json` or `evals/task-evals.json`.
