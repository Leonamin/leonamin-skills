#!/usr/bin/env python3
"""Audit an existing GUI implementation using repository and screen evidence."""

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
HEX_RE = re.compile(r"(?<![A-Za-z0-9_])#(?:[0-9A-Fa-f]{8}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{4}|[0-9A-Fa-f]{3})\b")
FRAGMENT_ATTRIBUTE_RE = re.compile(
    r"(?:href|to)\s*=\s*(?:\{\s*)?([\"'])#[^\"']*\1(?:\s*\})?",
    re.IGNORECASE,
)
CARD_TAG_RE = re.compile(
    r"</Card\s*>|<Card\b(?:[^\"'>]|\"[^\"]*\"|'[^']*')*>",
    re.DOTALL,
)


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
        config = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Invalid design audit config: {path}: {error}") from error

    if not isinstance(config, dict):
        raise ValueError(f"Invalid design audit config: {path} must contain a JSON object.")

    for key in ("allowedHexPaths", "forbiddenTailwindClasses", "scanExtensions"):
        value = config.get(key)
        if value is not None and (
            not isinstance(value, list) or not all(isinstance(item, str) for item in value)
        ):
            raise ValueError(f"Invalid design audit config: {key} must be a list of strings.")

    max_cards = config.get("maxCardsPerFile")
    if max_cards is not None and (
        isinstance(max_cards, bool) or not isinstance(max_cards, int) or max_cards < 1
    ):
        raise ValueError("Invalid design audit config: maxCardsPerFile must be a positive integer.")

    return config


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


def find_raw_hex(line: str) -> re.Match[str] | None:
    fragment_spans = [match.span() for match in FRAGMENT_ATTRIBUTE_RE.finditer(line)]
    for match in HEX_RE.finditer(line):
        if not any(start <= match.start() < end for start, end in fragment_spans):
            return match
    return None


def scan_cards(rel: str, content: str, max_cards: int) -> list[Finding]:
    findings: list[Finding] = []
    card_depth = 0
    card_count = 0

    for match in CARD_TAG_RE.finditer(content):
        token = match.group(0)
        if token.startswith("</Card"):
            if card_depth > 0:
                card_depth -= 1
            continue

        card_count += 1
        line = content.count("\n", 0, match.start()) + 1
        excerpt = token.replace("\n", " ").strip()[:160]
        is_self_closing = bool(re.search(r"/\s*>$", token))
        if card_depth > 0:
            findings.append(
                Finding(
                    "error",
                    "card-in-card",
                    rel,
                    line,
                    "Nested Card detected. Use product components or unframed sections.",
                    excerpt,
                )
            )
        if not is_self_closing:
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


def scan_file(root: Path, path: Path, config: dict[str, Any]) -> list[Finding]:
    rel = str(path.relative_to(root))
    allowed_hex_paths = config.get("allowedHexPaths") or ["design-product/system/design-tokens.json"]
    max_cards = config.get("maxCardsPerFile") or 10
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
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []

    findings: list[Finding] = []
    generic_copy_re = re.compile(
        r"(powerful features|everything you need|trusted by|seamless experience|"
        r"unlock your potential|boost productivity|all[- ]in[- ]one platform)",
        re.IGNORECASE,
    )

    for index, line in enumerate(content.splitlines(), start=1):
        stripped = line.strip()

        if find_raw_hex(line) and not is_allowed_hex_path(rel, allowed_hex_paths):
            findings.append(
                Finding(
                    "warning",
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

    findings.extend(scan_cards(rel, content, max_cards))
    return findings


def print_text(root: Path, findings: list[Finding], has_manifest: bool) -> None:
    print("GUI Design Audit")
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
    if not root.is_dir():
        parser.error(f"Project directory does not exist: {root}")

    try:
        config = load_config(root)
    except ValueError as error:
        parser.error(str(error))
    extensions = set(config.get("scanExtensions") or DEFAULT_EXTENSIONS)
    has_manifest = (root / "design-product" / "manifest.json").exists()
    findings: list[Finding] = []

    if not has_manifest:
        findings.append(
            Finding(
                "info",
                "missing-design-product",
                "design-product/manifest.json",
                0,
                "Optional design-product context is unavailable; use repository and rendered UI evidence.",
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
