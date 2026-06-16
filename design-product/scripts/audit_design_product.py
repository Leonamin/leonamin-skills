#!/usr/bin/env python3
"""Audit a project for common Design Product OS violations."""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


DEFAULT_EXTENSIONS = {".tsx", ".ts", ".jsx", ".js", ".css", ".scss", ".html", ".vue", ".svelte"}
EXCLUDED_DIRS = {
    ".git",
    ".next",
    ".nuxt",
    ".svelte-kit",
    "node_modules",
    "dist",
    "build",
    "coverage",
    ".turbo",
    ".cache",
}


@dataclass
class Finding:
    severity: str
    rule: str
    path: str
    line: int
    message: str
    excerpt: str = ""


def load_config(root: Path) -> dict[str, Any]:
    path = root / "design-product" / "audits" / "design-lint.config.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def iter_files(root: Path, extensions: set[str]) -> Iterable[Path]:
    for current_root, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        base = Path(current_root)
        for filename in files:
            path = base / filename
            if path.suffix in extensions:
                yield path


def is_allowed_hex_path(rel: str, allowed_paths: list[str]) -> bool:
    normalized = rel.replace("\\", "/")
    return any(normalized.endswith(item) or normalized == item for item in allowed_paths)


def scan_file(root: Path, path: Path, config: dict[str, Any]) -> list[Finding]:
    rel = str(path.relative_to(root))
    allowed_hex_paths = config.get("allowedHexPaths") or ["design-product/system/design-tokens.json"]
    max_cards = int(config.get("maxCardsPerFile") or 10)
    forbidden_classes = config.get("forbiddenTailwindClasses") or [
        "rounded-3xl",
        "shadow-xl",
        "shadow-2xl",
        "bg-gradient-to-r",
        "bg-gradient-to-br",
        "backdrop-blur",
        "blur-3xl",
    ]

    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except Exception:
        return []

    findings: list[Finding] = []
    card_depth = 0
    card_count = 0
    hex_re = re.compile(r"(?<![A-Za-z0-9_])#[0-9A-Fa-f]{3,8}\b")
    card_token_re = re.compile(r"</Card>|<Card(?:\s|>)")
    generic_copy_re = re.compile(
        r"(powerful features|everything you need|trusted by|seamless experience|"
        r"unlock your potential|boost productivity|all[- ]in[- ]one platform)",
        re.IGNORECASE,
    )

    for index, line in enumerate(lines, start=1):
        stripped = line.strip()

        if hex_re.search(line) and not is_allowed_hex_path(rel, allowed_hex_paths):
            findings.append(
                Finding(
                    "error",
                    "raw-hex",
                    rel,
                    index,
                    "Raw hex value outside an allowed token file.",
                    stripped[:160],
                )
            )

        for forbidden in forbidden_classes:
            if forbidden in line:
                findings.append(
                    Finding(
                        "warning",
                        "forbidden-style-shortcut",
                        rel,
                        index,
                        f"Potential AI-slop style shortcut: `{forbidden}`.",
                        stripped[:160],
                    )
                )

        if "from-purple" in line or "to-blue" in line or "from-blue" in line or "to-purple" in line:
            findings.append(
                Finding(
                    "warning",
                    "purple-blue-gradient",
                    rel,
                    index,
                    "Dominant purple/blue gradient drift.",
                    stripped[:160],
                )
            )

        if generic_copy_re.search(line):
            findings.append(
                Finding(
                    "warning",
                    "generic-marketing-copy",
                    rel,
                    index,
                    "Generic marketing copy that often makes AI UI look unspecific.",
                    stripped[:160],
                )
            )

        for match in card_token_re.finditer(line):
            token = match.group(0)
            if token == "</Card>":
                if card_depth > 0:
                    card_depth -= 1
                continue

            card_count += 1
            if card_depth > 0:
                findings.append(
                    Finding(
                        "error",
                        "card-in-card",
                        rel,
                        index,
                        "Nested Card detected. Use product components or unframed sections.",
                        stripped[:160],
                    )
                )
            tail = line[match.end() :]
            if not tail.lstrip().startswith("/>"):
                card_depth += 1

    if card_count > max_cards:
        findings.append(
            Finding(
                "warning",
                "card-overuse",
                rel,
                1,
                f"{card_count} Card components found; max configured is {max_cards}.",
                "",
            )
        )

    return findings


def print_text(root: Path, findings: list[Finding], has_manifest: bool) -> None:
    print("Design Product Audit")
    print(f"Root: {root}")
    print(f"Manifest: {'found' if has_manifest else 'missing'}")
    print(f"Findings: {len(findings)}")
    if not findings:
        return
    for finding in findings:
        location = f"{finding.path}:{finding.line}" if finding.line else finding.path
        print(f"- [{finding.severity.upper()}] {location} {finding.rule}: {finding.message}")
        if finding.excerpt:
            print(f"  {finding.excerpt}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=".", help="Project root to audit.")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--strict", action="store_true", help="Exit 1 when error findings exist.")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    if not root.exists():
        parser.error(f"Path does not exist: {root}")

    config = load_config(root)
    extensions = set(config.get("scanExtensions") or DEFAULT_EXTENSIONS)
    has_manifest = (root / "design-product" / "manifest.json").exists()
    findings: list[Finding] = []

    if not has_manifest:
        findings.append(
            Finding(
                "error",
                "missing-design-product",
                "design-product/manifest.json",
                0,
                "Run init_design_product.py before design work.",
            )
        )

    for path in iter_files(root, extensions):
        findings.extend(scan_file(root, path, config))

    if args.format == "json":
        print(
            json.dumps(
                {
                    "root": str(root),
                    "manifest": has_manifest,
                    "findings": [finding.__dict__ for finding in findings],
                },
                indent=2,
            )
        )
    else:
        print_text(root, findings, has_manifest)

    has_error = any(finding.severity == "error" for finding in findings)
    return 1 if args.strict and has_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
