# Sub-Agent Delegation Briefs

Use this guide when drafting a delegation brief for a sub-agent or multi-agent workflow.

## Context Modes: Fresh vs. Forked
- **Fresh (Isolated context)**: The child has no prior conversation history. Make the brief self-contained with exact goals, known facts, ruled-out dead ends, relevant paths/commands, and explicit assumptions or `{{variable}}` slots.
- **Forked (Inherited context)**: The child already sees prior conversation history. Focus on deltas, boundaries, and task-specific constraints rather than repeating existing history.

## Core Delegation Principles
- **Clear Scope & Write Isolation**: State what is in-scope, explicitly out-of-scope (including read-only vs. writable paths), and whether child sub-agent spawning is allowed. In parallel delegations, assign disjoint write scopes to prevent file collisions.
- **Verifiable Done State & Budgets**: Specify objective completion criteria, step/retry limits, and what to do when stuck (report current findings and blockers rather than guessing or looping).
- **Auditable Return Contract**: Require concise, conclusion-first results with concrete evidence (`path:line`, command results, or exact quotes), confidence/assumptions, open gaps, and strict data-vs-instruction isolation for any external content. Parent agents verify critical claims rather than trusting completion at face value.
