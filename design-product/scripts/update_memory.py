#!/usr/bin/env python3
"""Append design decisions to repo-local design-product memory."""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path


def append_lines(path: Path, heading: str, entries: list[str]) -> None:
    if not entries:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()
    existing = path.read_text(encoding="utf-8") if path.exists() else f"# {heading}\n"
    block = [f"\n## {today}"]
    for entry in entries:
        cleaned = entry.strip()
        if cleaned:
            block.append(f"- {cleaned}")
    path.write_text(existing.rstrip() + "\n" + "\n".join(block) + "\n", encoding="utf-8")


def update_current_state(path: Path, entries: list[str]) -> None:
    if not entries:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()
    existing = path.read_text(encoding="utf-8") if path.exists() else "# Current Design State\n"
    block = [f"\n## Latest Update ({today})"]
    for entry in entries[-8:]:
        cleaned = entry.strip()
        if cleaned:
            block.append(f"- {cleaned}")
    path.write_text(existing.rstrip() + "\n" + "\n".join(block) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=".", help="Project root.")
    parser.add_argument("--decision", action="append", default=[], help="Decision to append.")
    parser.add_argument("--approved", action="append", default=[], help="Approved pattern to append.")
    parser.add_argument("--rejected", action="append", default=[], help="Rejected pattern to append.")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    memory = root / "design-product" / "memory"
    stdin_text = sys.stdin.read().strip() if not sys.stdin.isatty() else ""
    decisions = list(args.decision)
    if stdin_text:
        decisions.append(stdin_text)

    append_lines(memory / "decision-log.md", "Decision Log", decisions)
    append_lines(memory / "approved-patterns.md", "Approved Patterns", args.approved)
    append_lines(memory / "rejected-patterns.md", "Rejected Patterns", args.rejected)
    update_current_state(memory / "current-design-state.md", decisions + args.approved + args.rejected)

    total = len(decisions) + len(args.approved) + len(args.rejected)
    print(f"Updated design memory entries: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
