# Audit Edge Cases, SOPs & Verification

Load this reference when handling tricky classification boundaries, human-AI SOPs, or regression/rollback planning without an existing test suite.

## Classification Traps to Avoid
- **Style/Policy vs. Old Crutch**: Rules like avoiding emojis/slang, enforcing disclaimers, or following brand tone may be `SPEC` rather than obsolete model hacks. Without clear evidence it was a model patch, keep and mark `unverified`.
- **Intentional Tail Anchor vs. `DUP`**: Repeating a brief goal reminder at the end of a long dynamic context can aid attention; do not treat deliberate anchoring as accidental duplication.
- **Legacy `DEBT` vs. Upgrade Gain**: Fixing missing failure exits, injection isolation, or cache-hostile ordering is structural remediation (`DEBT`)—label it clearly rather than crediting it to a model upgrade.
- **Silent Conflict Resolution**: Do not silently drop or favor one side of a `CONFLICT`; present the contradiction clearly for decision.

## Human-AI SOP Audit Principles
- Replace manual workarounds (such as hand-checking syntax or formatting) with automated or schema checks where safe.
- Audit human review checkpoints for real decision authority and supporting evidence rather than rubber-stamping.
- Remove intermediate handoffs with no downstream consumer, align automation boundaries with risk, update stale roles/SLA/system references (`STALE`), and change one workflow step at a time.

## Comparison & Single-Point Rollback
- Without a pre-existing benchmark, compare old vs. new across representative normal cases, missing/edge inputs, prompt-injection inputs, and the exact failure scenario a removed `COMP` originally targeted.
- Record old vs. new behavior per case and roll back only the specific offending edit if a regression appears, rather than reverting everything blindly.
