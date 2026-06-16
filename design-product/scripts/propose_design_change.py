#!/usr/bin/env python3
"""Record a design-system change proposal in repo-local memory."""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path


VALID_TYPES = {
    "identity",
    "token",
    "component",
    "pattern",
    "layout",
    "figma",
    "code-mapping",
    "governance",
}

VALID_STATUS = {"proposed", "accepted", "rejected", "deferred"}


def bullet_block(title: str, items: list[str]) -> list[str]:
    if not items:
        return []
    lines = [f"### {title}"]
    for item in items:
        cleaned = item.strip()
        if cleaned:
            lines.append(f"- {cleaned}")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=".", help="Project root.")
    parser.add_argument("--type", required=True, choices=sorted(VALID_TYPES), help="Change type.")
    parser.add_argument("--title", required=True, help="Proposal title.")
    parser.add_argument("--problem", action="append", default=[], help="Problem statement.")
    parser.add_argument("--option", action="append", default=[], help="Option to consider.")
    parser.add_argument("--recommendation", default="", help="Recommended option.")
    parser.add_argument("--affected", action="append", default=[], help="Affected file, component, or Figma page.")
    parser.add_argument("--status", default="proposed", choices=sorted(VALID_STATUS), help="Proposal status.")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    memory = root / "design-product" / "memory"
    memory.mkdir(parents=True, exist_ok=True)

    proposal_path = memory / "design-system-proposals.md"
    existing = proposal_path.read_text(encoding="utf-8") if proposal_path.exists() else "# Design System Proposals\n"

    today = dt.date.today().isoformat()
    stdin_note = sys.stdin.read().strip() if not sys.stdin.isatty() else ""

    lines = [
        f"## {today} - {args.title}",
        "",
        f"- Type: {args.type}",
        f"- Status: {args.status}",
    ]
    lines.extend([""] + bullet_block("Problem", args.problem))
    lines.extend([""] + bullet_block("Options", args.option))
    if args.recommendation.strip():
        lines.extend(["", "### Recommendation", args.recommendation.strip()])
    lines.extend([""] + bullet_block("Affected", args.affected))
    if stdin_note:
        lines.extend(["", "### Notes", stdin_note])

    proposal_path.write_text(existing.rstrip() + "\n\n" + "\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Recorded design-system proposal: {proposal_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
