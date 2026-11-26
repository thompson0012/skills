# Contract & Evaluation Guide (`Standard` / `Full`)

Load this guide for `Standard` or `Full` prompt/agent specifications when verifying structural completeness or designing evaluation loops.

## Structural Contract Check
- **Clarity & Single Responsibility**: One prompt owns one clear stage/role with observable completion criteria, explicit assumptions, and clear conflict precedence.
- **Safe Boundaries & Fallbacks**: External/untrusted inputs are isolated as data; missing/out-of-scope cases have explicit failure exits; high-consequence or irreversible actions (writes, deletions, external sends, payments, policy/PII exposure) require HITL gates or hard code/schema enforcement.
- **Efficiency & Maintainability**: Static prefix precedes dynamic context; deterministic checks (math, schema validation, formatting, permissions) are offloaded to code/structured outputs; model-specific patches (`COMP`) are isolated and dated so future model upgrades do not leave mystery rules behind.

## Evaluation & Iteration Loop
- **Representative Test Coverage**: Include normal cases, missing/edge inputs, policy/rule conflicts, and prompt-injection attempts—plus targeted regression cases whenever removing or changing a rule.
- **Layered Grading**: Combine deterministic checks (schema, required fields, bounds, forbidden patterns) with anchored rubrics/judges and operational metrics (latency, cost, cache hit rate, retry/escalation rate).
- **Controlled Change & Rollback**: Change one variable at a time against a baseline, keep diff/rationale notes per change, roll back isolated changes if regressions appear, and feed real production failures back into tests.
