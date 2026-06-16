#!/usr/bin/env python3
"""Render compact design-product context for a fresh agent session."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def read_head(path: Path, max_lines: int = 80) -> str:
    if not path.exists():
        return "Missing."
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    selected = lines[:max_lines]
    suffix = "\n..." if len(lines) > max_lines else ""
    return "\n".join(selected).strip() + suffix


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=".", help="Project root.")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    manifest_path = root / "design-product" / "manifest.json"
    manifest = read_json(manifest_path)

    if not manifest:
        print("# Design Product Context")
        print()
        print("No design-product manifest found. Run init_design_product.py first.")
        return 0

    source = manifest.get("sourceOfTruth") or {}
    print("# Design Product Context")
    print()
    print(f"Project: {manifest.get('project', 'unknown')}")
    print(f"Version: {manifest.get('designProductVersion', 'unknown')}")
    print(f"Status: {manifest.get('status', 'unknown')}")
    print()
    print("## Identity")
    print(json.dumps(manifest.get("identity", {}), indent=2, ensure_ascii=True))
    print()
    print("## Hard Rules")
    print(json.dumps(manifest.get("hardRules", {}), indent=2, ensure_ascii=True))
    print()
    print("## Current State")
    print(read_head(root / source.get("currentState", "design-product/memory/current-design-state.md"), 80))
    print()
    print("## Product Brief")
    print(read_head(root / source.get("productBrief", "design-product/product-brief.md"), 60))
    print()
    print("## Visual Language")
    print(read_head(root / source.get("visualLanguage", "design-product/identity/visual-language.md"), 60))
    print()
    print("## Anti-Patterns")
    print(read_head(root / source.get("antiPatterns", "design-product/system/ai-anti-patterns.md"), 80))
    print()
    print("## Design System Proposals")
    print(read_head(root / source.get("proposals", "design-product/memory/design-system-proposals.md"), 80))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
