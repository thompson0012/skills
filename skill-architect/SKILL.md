---
name: skill-architect
description: Designs, compiles, compresses, and evaluates new or existing Agent Skills (SKILL.md, references/, scripts/, evals/) using progressive disclosure, delta-only contracts, and eval-driven iteration. Use when the user asks to create a new skill, turn a workflow/SOP into a reusable skill, architect a skill suite, or optimize a skill's trigger accuracy and token efficiency. Do NOT use when the user only wants a one-off prompt or sub-agent brief (use prompt-translator), wants to audit a standalone non-skill prompt (use prompt-auditor), or asks the current agent to directly execute the underlying task rather than build a skill.
---

# skill-architect

## Core Axioms

1. **Three-Tier Progressive Disclosure**:
   - **L1 Router (Frontmatter `name` + `description`)**: Always in context. Treat as a precision classifier—specify explicit/implicit triggers AND explicit `Do NOT use` boundaries (lookalike non-triggers and adjacent skills).
   - **L2 Execution (`SKILL.md`, target 25–60 lines)**: Loaded on trigger. Encode only high-leverage principles, routing/scaling decisions, invariants, failure exits, and pointers to L3 files. Never dump long templates, basic model knowledge, or full examples here.
   - **L3 On-Demand (`references/`, `scripts/`, `assets/`)**: Lazy-loaded Single Source of Truth (SSOT) for rubrics, edge cases, schemas, and deterministic scripts. Zero duplication with L2.
2. **Delta-Only (`SPEC` over `COMP`)**: Encode only what a capable zero-context colleague would still get wrong—domain contracts, risk gates, tool ordering, and edge traps. Every line must pass the *upgrade survival test*: would a stronger future model still need this rule?
3. **Code Over Prose**: Offload deterministic checks (validation, parsing, formatting, math, schema enforcement) to `scripts/` or structured schemas rather than prose instructions.
4. **Eval-Driven Delivery**: A skill is a draft until verified on both **Trigger Routing** (positive recall + zero lookalike false positives) and **A/B Execution** (baseline vs. skill-enabled quality lift).

## 6-Stage Build & Iteration Pipeline

1. **Scope & Boundary Definition**: Inspect existing workspace skills first to avoid overlap. Define the target capability, risk tier (`Light / Standard / Full`), and **at least 3 lookalike non-triggers** before drafting.
2. **Gap Audit**: Separate what the base model already does well from where it reliably fails. Keep only gap-closing `SPEC` invariants; drop model crutches (`COMP`).
3. **3-Tier Assembly**: Draft `SKILL.md` (L2), split deep rubrics/edge cases into `references/` (L3), and isolate deterministic operations into `scripts/` (L3) when warranted.
4. **Adversarial Compression**: Cut filler, hype, and duplicated rules; surface any `CONFLICT`; verify external-input isolation and explicit failure exits (what to do when context is missing, ambiguous, or out-of-scope).
5. **Dual-Axis Verification**: Create `evals/trigger-evals.json` (explicit, implicit, and lookalike non-triggers) and `evals/task-evals.json` (normal, missing/edge, conflict, and injection cases), then run A/B checks against baseline. Load `references/eval-and-compression.md` for grading thresholds and anti-pattern checks.
6. **Single-Variable Iteration**: Change one principle, boundary, or routing rule per iteration against the previous version; roll back isolated regressions and lock real failures into `evals/`.
