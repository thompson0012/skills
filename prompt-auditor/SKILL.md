---
name: prompt-auditor
description: Audits, diagnoses, compresses, refactors, and model-upgrades existing prompts, system prompts, skills, and human-AI SOPs while protecting business contracts. Use when the user pastes an existing prompt, skill, or SOP to review, remove anti-patterns, fix prompt-injection or cache bugs, or decide what to keep, update, or drop after changing models, tools, data sources, or policies. Do NOT use when the user has no existing draft and wants a new prompt or sub-agent brief written from scratch (use prompt-translator), or when asking to directly execute a project task.
---

# prompt-auditor

## Core Principles

1. **Quality Axis vs. Survival Axis**: A well-written rule may be redundant on a newer model (removable on the survival axis), while a poorly phrased rule may encode an irreplaceable business contract (must be preserved on the survival axis, refining wording only).
2. **Default Conservative (Keep Unless Proven Removable)**: Unlike greenfield drafting, auditing existing artifacts defaults to **retaining** unclear rules as `unverified` rather than deleting them on assumptions about newer models or neatness.
3. **Classify Before Cutting**: Tag segments before editing (`SPEC`, `COMP`, `STALE`, `DEBT`, `DUP`, `CONFLICT`) so every removal, edit, or keep decision is auditable and reversible.

## Audit Workflow

1. **Identify Mode & Risk Stance**:
   - **Quality Refactor (Assumptions unchanged)**: Fix structural debt (`DEBT`), duplication (`DUP`), and counterproductive patches (`COMP`) while preserving `SPEC` semantics.
   - **Upgrade / Assumption-Shift Audit (Model, tool, data source, or policy changed)**: Re-evaluate `COMP` necessity, update `STALE` facts/versions/limits, and isolate pre-existing `DEBT` rather than disguising it as upgrade gains.
   - Inspect workspace context/tests/history when available. If risk or change vector is unspecified, default to conservative (keep uncertain items) and state the assumption on the first turn; only ask first if no target draft was provided.
2. **Tag & Apply Two-Proof Rule for `COMP` Removal**:
   - `SPEC`: Business/domain rules, policies, permissions, output contracts, and priority order—keep and preserve meaning.
   - `COMP`: Workarounds for old model limits or emotional/repetitive pressure. Delete a `COMP` only when you can state both (a) the **specific failure it originally addressed** and (b) **why the new setup no longer needs it**; otherwise keep and mark `unverified`.
   - `STALE`: Outdated model names, limits, APIs, dates, or rates—update in place rather than deleting surrounding contracts.
   - `DEBT`: Missing failure exits, unisolated external inputs, cache-breaking dynamic prefixes, or deterministic tasks left to prose—remediate structurally.
   - `DUP`: Redundant repetitions—consolidate into a single authoritative place.
   - `CONFLICT`: Contradictory rules without precedence—surface explicitly rather than silently picking a side.
3. **Safe Rewrite & Verification**: Preserve all `SPEC` contracts and safety/compliance rules, apply structural fixes, and provide a concise audit summary, per-item classification, refactored draft, key diffs, and targeted regression checks (including failure/edge/injection cases and any removed `COMP` scenario). Load `references/audit-rubric.md` for edge-case classification traps, human-AI SOP auditing, and baseline-free comparison/rollback rules.
