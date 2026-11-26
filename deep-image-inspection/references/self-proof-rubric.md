# Self-Proof Rubric for Formal Image Audits

Load this reference for Tier 3 escalations, formal audit outputs, or structured verification tables. Every major finding must be verifiable against the image itself without unstated assumptions.

## Four Self-Proof Pillars

### 1. Spatial and Structural Anchor
- Locate the evidence using clear spatial terms (quadrant, grid cell, relative offset, parent container, or layer).
- If an item spans multiple regions or overlaps another element, note the overlapping boundaries.

### 2. Observable Visual Cue
- Cite concrete, non-circular visual cues: contours, stroke weight, tonal/color contrast, texture, alignment, typography, or repetition.
- State the observable cues before the interpretation.

### 3. Counter-Hypothesis and Falsification Check
- Ask: *"What else could produce this visual pattern?"*
- Check primary confounders:
  - Foreground/background occlusion or layer overlap
  - Compression artifacts, blur, motion smear, or glare
  - Visual lookalikes or cropped/partial framing
  - Specialized color or intensity encoding (false color, heatmaps, inverted contrast)
- If a plausible alternative cannot be ruled out from the image alone, downgrade certainty.

### 4. Certainty Tier and Defeasibility
Assign one explicit status:
- `confirmed`: Clear, unoccluded visual evidence directly supports the claim.
- `inferred`: Supported by visual cues plus structural/domain reasoning where pixels alone are partial or indirect.
- `ambiguous`: Multiple interpretations remain plausible due to low resolution, overlap, or visual similarity.
- `occluded`: Blocked, cut off, or hidden behind another layer or boundary.

For non-trivial claims, state one concrete **defeasibility condition** (what crop, higher-resolution view, alternate angle, or external input would overturn or refine the claim).

## Formal Audit Output Template

```markdown
### Findings
- **[Status | Region]** Claim statement.
  - **Evidence:** Observable visual cues.
  - **Counter-check:** Alternative considered and why it was kept or ruled out.
  - **Falsified if:** Condition that would overturn or refine this claim.

### Unverified / Blind Spots
- Region or question that could not be verified from the current image, plus the exact additional input needed.
```
