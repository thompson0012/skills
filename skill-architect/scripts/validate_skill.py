#!/usr/bin/env python3
"""Deterministic structural validator for Agent Skills built with skill-architect."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
REL_REF_RE = re.compile(r"`((?:references|scripts|evals|assets)/[A-Za-z0-9._/-]+)`")
NEG_BOUNDARY_RE = re.compile(r"\b(do not use|don't use|not for|never use)\b", re.IGNORECASE)
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    data: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, val = line.split(":", 1)
        data[key.strip()] = val.strip().strip("\"'")
    return data


def validate_skill(skill_dir: Path, tier: str = "standard") -> dict:
    errors: list[str] = []
    warnings: list[str] = []

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return {"ok": False, "errors": ["Missing SKILL.md"], "warnings": []}

    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    line_count = len(lines)

    # 1. Frontmatter & L1 router checks
    fm = parse_frontmatter(text)
    if fm is None:
        errors.append("SKILL.md is missing YAML frontmatter (--- ... ---).")
    else:
        name = fm.get("name", "")
        desc = fm.get("description", "")
        user_only = fm.get("disable-model-invocation", "").lower() == "true"

        if not name:
            errors.append("Frontmatter missing required 'name'.")
        else:
            if not KEBAB_RE.match(name):
                errors.append(f"Frontmatter 'name' ({name}) must be kebab-case.")
            if name != skill_dir.name:
                warnings.append(f"Frontmatter 'name' ({name}) differs from directory name ({skill_dir.name}).")

        if not desc:
            errors.append("Frontmatter missing required 'description'.")
        elif not user_only and not NEG_BOUNDARY_RE.search(desc):
            errors.append("Model-invoked 'description' lacks an explicit negative boundary (e.g., 'Do NOT use when...').")

    # 2. L2 length budget checks
    if line_count > 150:
        errors.append(f"SKILL.md is {line_count} lines (hard cap 150). Move details to references/.")
    elif line_count > 60:
        warnings.append(f"SKILL.md is {line_count} lines (target 25-60). Check for bloat or duplication.")

    # 3. Broken L3 pointer checks
    for ref in sorted(set(REL_REF_RE.findall(text))):
        if not (skill_dir / ref).exists():
            errors.append(f"Broken pointer in SKILL.md: '{ref}' does not exist.")

    # 4. Eval suite checks (required for standard/full)
    trig_path = skill_dir / "evals" / "trigger-evals.json"
    task_path = skill_dir / "evals" / "task-evals.json"

    if tier in ("standard", "full"):
        if not trig_path.is_file():
            errors.append("Missing evals/trigger-evals.json (required for Standard/Full tier).")
        if not task_path.is_file():
            errors.append("Missing evals/task-evals.json (required for Standard/Full tier).")

    if trig_path.is_file():
        try:
            trig_data = json.loads(trig_path.read_text(encoding="utf-8"))
            cases = trig_data.get("cases", [])
            if not isinstance(cases, list) or not cases:
                errors.append("evals/trigger-evals.json must contain a non-empty 'cases' list.")
            else:
                pos = sum(1 for c in cases if c.get("expected_trigger") is True)
                neg = sum(1 for c in cases if c.get("expected_trigger") is False)
                if pos < 1:
                    errors.append("evals/trigger-evals.json needs at least 1 positive trigger case.")
                if neg < 3:
                    errors.append(f"evals/trigger-evals.json has {neg} non-trigger cases (minimum 3 lookalike non-triggers required).")
        except json.JSONDecodeError as exc:
            errors.append(f"evals/trigger-evals.json is invalid JSON: {exc}")

    if task_path.is_file():
        try:
            task_data = json.loads(task_path.read_text(encoding="utf-8"))
            cases = task_data.get("cases", [])
            if not isinstance(cases, list) or not cases:
                errors.append("evals/task-evals.json must contain a non-empty 'cases' list.")
            else:
                for i, c in enumerate(cases):
                    if not c.get("prompt") or not c.get("expectations"):
                        errors.append(f"evals/task-evals.json case[{i}] missing 'prompt' or 'expectations'.")
        except json.JSONDecodeError as exc:
            errors.append(f"evals/task-evals.json is invalid JSON: {exc}")

    return {
        "ok": len(errors) == 0,
        "skill": skill_dir.name,
        "tier": tier,
        "line_count": line_count,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a skill directory against skill-architect invariants.")
    parser.add_argument("skill_dir", type=Path, help="Path to the skill directory")
    parser.add_argument("--tier", choices=["light", "standard", "full"], default="standard", help="Risk tier")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    result = validate_skill(args.skill_dir.resolve(), tier=args.tier)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        status = "PASS" if result["ok"] else "FAIL"
        print(f"[{status}] {result.get('skill', args.skill_dir)} (tier={result.get('tier')}, lines={result.get('line_count', 0)})")
        for w in result["warnings"]:
            print(f"  WARN: {w}")
        for e in result["errors"]:
            print(f"  ERROR: {e}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
