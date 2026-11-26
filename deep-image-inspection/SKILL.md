---
name: deep-image-inspection
description: Principle-first guide for thorough multimodal image inspection on dense UI screenshots, charts/dashboards, small or degraded text, tables, technical diagrams, multi-object counting, visual diffs, occluded scenes, and high-stakes visual verification. Do NOT escalate to multi-pass protocols for clear, single-target, low-stakes visual questions.
---

# deep-image-inspection

## Core Objective

Maximize visual accuracy without wasting tokens: stay fast and direct on clear images, and escalate proportionally on dense, degraded, occluded, or high-stakes visuals.

## Tiered Routing

Match inspection effort to visual clarity, density, and task stakes:

- **Tier 1 — Quick Grounded Pass (Default for clear, single-target, low-stakes queries)**: Answer directly with brief location + observable cue grounding. Note any cutoff or low-contrast blind spot in one line. Skip multi-pass templates.
- **Tier 2 — Focused Multi-Pass Inspection (Dense, multi-element, text/data extraction, counting, UI/diagram analysis, or visual diffs)**: Inspect through the lens(es) the task demands, sweep margins/corners/overlaps before concluding, and ground key claims in visual evidence first.
- **Tier 3 — Escalated Verification (Small/blurred/rotated pixels, heavy occlusion, anomaly/tamper checks, or high-consequence decisions)**: Escalate to available crop/zoom/rotation/enhancement tools before concluding, test plausible counter-hypotheses, and load `references/self-proof-rubric.md` for formal certainty tagging and audit structure.

## Timeless Inspection Principles

1. **Pixels Over Priors**: Ground observations in concrete, non-circular visual cues (contours, strokes, contrast, alignment, relative position, encoding) before naming or interpreting them. Never let familiar templates overwrite anomalous, cropped, or altered pixels.
2. **Task-Matched Lenses & Targeted Re-Inspection**: Direct attention intentionally—**Spatial** (layout, scale, containment, layer order, connections), **Detail** (fine geometry, small characters/symbols, boundaries, artifacts), or **Aesthetic/Encoding** (lighting, contrast, color/intensity scales, hierarchy). Re-inspect specific regions whenever overlaps obscure boundaries, questions shift, or a hypothesis needs testing.
3. **Verify Over Guess**: When critical details are too small, blurred, low-contrast, or rotated to read reliably from the full frame, use any crop, zoom, rotation, or image-enhancement capability available in your environment to re-inspect the region. If no such tool is available, mark the region resolution-limited rather than fabricating precision.
4. **Calibrated Uncertainty**:
   - **Absence != Missing**: Sweep borders, corners, legends, headers/footers, and occluded layers before claiming something is absent.
   - **Downgrade, Don't Rationalize**: Fluent reasoning does not increase pixel fidelity. When competing interpretations remain plausible, downgrade certainty (`inferred`, `ambiguous`, or `occluded`) and state what additional view or input would resolve it.
5. **Evidence-First Claims**: On analytical, contested, or multi-part findings, state **Region + Observable Cue** before the conclusion so every claim stays auditable against the image.

## Deferred Reference

- Read `references/self-proof-rubric.md` only when producing formal audit reports, structured verification tables, or Tier 3 certainty/falsification breakdowns.
