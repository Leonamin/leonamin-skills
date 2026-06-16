#!/usr/bin/env python3
"""Initialize a repo-local design-product operating layer."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any


VERSION = "0.1.0"


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def detect_project(root: Path) -> dict[str, Any]:
    package = read_json(root / "package.json") if (root / "package.json").exists() else {}
    deps: dict[str, Any] = {}
    for key in ("dependencies", "devDependencies"):
        value = package.get(key)
        if isinstance(value, dict):
            deps.update(value)

    markers: list[str] = []
    if "next" in deps or (root / "next.config.js").exists() or (root / "next.config.mjs").exists():
        markers.append("nextjs")
    if "vite" in deps or (root / "vite.config.ts").exists() or (root / "vite.config.js").exists():
        markers.append("vite")
    if "react" in deps:
        markers.append("react")
    if "vue" in deps:
        markers.append("vue")
    if "svelte" in deps:
        markers.append("svelte")
    if "tailwindcss" in deps or any(root.glob("tailwind.config.*")):
        markers.append("tailwind")
    if (root / "components" / "ui").exists() or (root / "src" / "components" / "ui").exists():
        markers.append("shadcn-or-ui-primitives")
    if "@radix-ui/react-slot" in deps or any(name.startswith("@radix-ui/") for name in deps):
        markers.append("radix-ui")
    if "@mui/material" in deps:
        markers.append("mui")
    if "@chakra-ui/react" in deps:
        markers.append("chakra-ui")

    source_dirs: list[str] = []
    if (root / "src").exists():
        for child in (root / "src").iterdir():
            if child.is_dir():
                source_dirs.append(str(child.relative_to(root)))
    if (root / "app").exists():
        source_dirs.append("app")
    if (root / "pages").exists():
        source_dirs.append("pages")

    css_files = [
        str(path.relative_to(root))
        for pattern in ("**/globals.css", "**/global.css", "**/index.css", "**/app.css")
        for path in root.glob(pattern)
        if "node_modules" not in path.parts and ".git" not in path.parts
    ][:12]

    package_name = package.get("name") if isinstance(package.get("name"), str) else root.name

    return {
        "projectName": package_name,
        "markers": sorted(set(markers)),
        "packageManager": detect_package_manager(root),
        "sourceDirs": sorted(set(source_dirs))[:20],
        "cssFiles": css_files,
    }


def detect_package_manager(root: Path) -> str:
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    if (root / "package-lock.json").exists():
        return "npm"
    if (root / "bun.lockb").exists() or (root / "bun.lock").exists():
        return "bun"
    return "unknown"


def write_file(path: Path, content: str, force: bool, touched: list[str], skipped: list[str]) -> None:
    if path.exists() and not force:
        skipped.append(str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    touched.append(str(path))


def json_dumps(data: Any) -> str:
    return json.dumps(data, indent=2, ensure_ascii=True) + "\n"


def title_from_name(name: str) -> str:
    cleaned = re.sub(r"[-_]+", " ", name).strip()
    return cleaned.title() if cleaned else "Product"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=".", help="Project root to initialize.")
    parser.add_argument("--project-name", default="", help="Override detected project name.")
    parser.add_argument("--figma-url", default="", help="Figma file URL to store in manifest.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing design-product files.")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    if not root.exists():
        parser.error(f"Path does not exist: {root}")

    detected = detect_project(root)
    project_name = args.project_name or detected["projectName"] or root.name
    display_name = title_from_name(project_name)
    today = dt.date.today().isoformat()

    manifest = {
        "project": project_name,
        "designProductVersion": VERSION,
        "status": "draft",
        "createdAt": today,
        "identity": {
            "oneLine": "TBD",
            "keywords": [],
            "not": [
                "generic SaaS page",
                "template marketplace look",
                "AI-generated decorative layout",
            ],
        },
        "sourceOfTruth": {
            "productBrief": "design-product/product-brief.md",
            "visualLanguage": "design-product/identity/visual-language.md",
            "tokens": "design-product/system/design-tokens.json",
            "antiPatterns": "design-product/system/ai-anti-patterns.md",
            "componentRules": "design-product/system/component-rules.md",
            "layoutRules": "design-product/system/layout-rules.md",
            "changeWorkflow": "design-product/system/change-workflow.md",
            "productComponents": "design-product/components/product-components.md",
            "currentState": "design-product/memory/current-design-state.md",
            "proposals": "design-product/memory/design-system-proposals.md",
        },
        "figma": {
            "fileUrl": args.figma_url,
            "requiredPages": [
                "00 Brand Board",
                "01 Foundations",
                "02 Components",
                "03 Product Patterns",
                "04 Screens",
                "99 Rejected Patterns",
            ],
        },
        "hardRules": {
            "noRawHexOutsideTokens": True,
            "noCardInCard": True,
            "maxRadius": "24px",
            "requirePlanBeforeFigmaWrite": True,
            "requireAutoLayoutInFigma": True,
            "requireMemoryUpdateAfterDesignDecision": True,
        },
        "detectedStack": detected,
    }

    token_data = {
        "$schema": "https://design-tokens.org/schema.json",
        "meta": {
            "status": "draft",
            "note": "Edit these semantic tokens after product identity is clarified.",
        },
        "color": {
            "background": {"canvas": "#F8F7F3", "surface": "#FFFFFF", "muted": "#EFEEE8"},
            "text": {"primary": "#171717", "secondary": "#55524B", "muted": "#78746B"},
            "border": {"subtle": "#E2DFD6", "strong": "#BBB5A8"},
            "action": {"primary": "#1F4D46", "primaryText": "#FFFFFF", "accent": "#B66A3C"},
            "state": {"success": "#2F6B4F", "warning": "#A15C1B", "danger": "#A33A3A"},
        },
        "radius": {"xs": "4px", "sm": "8px", "md": "12px", "lg": "20px", "max": "24px"},
        "spacing": {
            "2xs": "4px",
            "xs": "8px",
            "sm": "12px",
            "md": "16px",
            "lg": "24px",
            "xl": "32px",
            "2xl": "48px",
            "3xl": "64px",
        },
        "shadow": {
            "none": "none",
            "soft": "0 8px 24px rgba(23, 23, 23, 0.08)",
            "raised": "0 14px 40px rgba(23, 23, 23, 0.12)",
        },
        "forbidden": {
            "radius": ["32px", "rounded-3xl by default", "rounded-full except badges and avatars"],
            "effects": ["random gradients", "glassmorphism", "shadow-xl by default"],
            "colors": ["raw hex outside token files", "dominant purple/blue SaaS gradients"],
        },
    }

    files: dict[str, str] = {
        "design-product/manifest.json": json_dumps(manifest),
        "design-product/product-brief.md": f"""# Product Brief

## Product
{display_name}

## One-line identity
TBD

## Primary users
- TBD

## Primary value
- TBD

## Primary conversion
- TBD

## Trust moments
- TBD

## Not this
- Generic SaaS landing page
- Template marketplace UI
- AI-looking card stack

## Confidence
Low until the brand interview is answered.
""",
        "design-product/identity/brand-interview.md": """# Brand Interview

Answer only what is known. Leave unknowns as TBD.

1. What is the product in one sentence?
2. Why should users choose it over alternatives?
3. What is this product explicitly not?
4. What should users feel on the first screen?
5. What should the product never look like?
6. Which references are useful without copying them?
7. What is the primary conversion action?
8. Where must the interface create trust?
9. What content is most important for user decisions?
10. What should a non-developer stakeholder understand immediately?
""",
        "design-product/identity/positioning.md": """# Positioning

## Category
TBD

## Differentiation
TBD

## Audience
TBD

## Competitive contrast
TBD
""",
        "design-product/identity/visual-language.md": """# Visual Language

## Desired qualities
- Specific to the product
- Calm enough to support repeated use
- Clear hierarchy before decoration
- Trustworthy without fake proof

## Surface
Use restrained surfaces. Avoid wrapping every section in a card.

## Shape
Use the radius scale in `system/design-tokens.json`. Large radius must be intentional.

## Color
Use semantic tokens. Raw hex values belong only in token files.

## Motion
TBD. Avoid decorative motion until product needs are clear.
""",
        "design-product/identity/tone-of-voice.md": """# Tone Of Voice

## Voice
TBD

## Copy rules
- Be specific.
- Do not invent proof.
- Avoid generic AI marketing copy.
- Prefer concrete product nouns over vague adjectives.
""",
        "design-product/identity/anti-identity.md": """# Anti-Identity

The product should not feel like:

- A generic SaaS template
- A random AI-generated landing page
- A pile of cards and badges
- A visual style copied from a competitor
- A dashboard unless the workflow is actually operational
""",
        "design-product/system/design-principles.md": """# Design Principles

1. Identity before ornament.
2. IA before visual design.
3. Product components over primitive components.
4. Tokens before one-off styling.
5. Figma output must be editable, named, and structured.
6. Audit every meaningful design change.
7. Record durable decisions in repo memory.
""",
        "design-product/system/design-tokens.json": json_dumps(token_data),
        "design-product/system/token-taxonomy.md": """# Token Taxonomy

Use semantic tokens first:

- `color.background.*`
- `color.text.*`
- `color.border.*`
- `color.action.*`
- `color.state.*`
- `radius.*`
- `spacing.*`
- `shadow.*`

Component-specific tokens may be added when a repeated product component needs them.
""",
        "design-product/system/layout-rules.md": """# Layout Rules

- Choose the information architecture before the grid.
- Use cards only for repeated items, contained tools, or genuinely grouped content.
- Do not put cards inside cards.
- Keep page sections unframed unless a frame improves scanning or comparison.
- Use stable responsive dimensions for fixed-format UI.
- Keep primary actions visually stable across breakpoints.
- Avoid decorative full-page gradients unless identity explicitly requires them.
""",
        "design-product/system/component-rules.md": """# Component Rules

## Layers

- Primitive layer: library components such as Button, Card, Dialog, Select.
- Product layer: domain components such as BookingPanel, RouteSummary, PlanComparison.

AI agents should design and implement the product layer first. Primitive components are implementation details.

## Naming

Name product components by user-facing domain meaning, not by shape.

Good:
- BookingPanel
- RouteSummary
- ItineraryTimeline
- LocalNote

Weak:
- BigCard
- InfoBox
- FancySection
""",
        "design-product/system/change-workflow.md": """# Change Workflow

Use this loop for changes to identity, tokens, components, layouts, patterns, Figma structure, and code mappings.

## Loop

1. Classify the change.
2. State the problem in product terms.
3. Identify affected source-of-truth files, code components, and Figma pages.
4. Compare 2-3 options with tradeoffs.
5. Recommend one option.
6. Record the proposal in `memory/design-system-proposals.md`.
7. Apply only the accepted scope.
8. Audit the result.
9. Update design memory.

## Decision states

- Proposed
- Accepted
- Rejected
- Deferred

Discussion alone should not mutate tokens, components, code, or Figma.
""",
        "design-product/system/figma-rules.md": """# Figma Rules

- Use native frames, auto layout, variables, styles, components, and variants.
- Name pages using the manifest page list.
- Name layers by domain role.
- Do not flatten screens into screenshots except as temporary references.
- Do not write to Figma before the IA/component plan exists.
- Keep rejected explorations on `99 Rejected Patterns` when useful.
""",
        "design-product/system/ai-anti-patterns.md": """# AI Anti-Patterns

## Forbidden by default

- Card in card
- Every section wrapped in a floating card
- Hero plus three feature cards as a default answer
- Generic FAQ/testimonial/stat blocks with invented content
- Purple/blue SaaS gradients
- Large decorative blur blobs
- Glassmorphism without product reason
- `rounded-3xl` everywhere
- `shadow-xl` as a default surface style
- Raw hex outside token files
- Product pages that read like marketing templates

## Required instead

- Choose IA before surface style
- Use product-specific components
- Use tokens
- Explain why repeated containers exist
- Audit after creation
""",
        "design-product/components/primitives.md": f"""# Primitive Components

Detected stack markers:

```json
{json.dumps(detected["markers"], indent=2)}
```

Treat existing UI libraries as primitives. Do not let primitive names become the product language.
""",
        "design-product/components/product-components.md": """# Product Components

Add product-specific components here as they become clear.

## Component spec template

Each product component should define:

- Purpose
- When to use
- When not to use
- Anatomy
- Content model
- States and variants
- Token bindings
- Layout behavior
- Accessibility requirements
- Figma mapping
- Code mapping
- Anti-patterns

## Candidates

- PrimaryActionPanel: the main conversion surface for the current flow.
- TrustNote: specific reassurance tied to a user decision.
- ComparisonRow: compact comparison of decision attributes.
- DetailSummary: high-signal summary for a product, route, plan, or record.

Replace these candidates with domain-specific names after product discovery.
""",
        "design-product/components/component-contracts.json": json_dumps({"components": [], "status": "draft"}),
        "design-product/patterns/screen-planning.md": """# Screen Planning Pattern

Before UI or Figma work, define:

- Screen type
- User goal
- Primary action
- Secondary actions
- Content hierarchy
- Product components
- Explicit non-goals
- Anti-pattern risks
""",
        "design-product/patterns/product-detail-page.md": """# Product Detail Page Pattern

Use when a user must evaluate one product, service, plan, route, venue, or offer.

## IA

1. Decision summary
2. Primary action
3. Key attributes
4. Trust or constraints
5. Detail sections in order of decision value
6. Alternatives or next step only if helpful

## Avoid

- Marketing feature grid
- Repeating the same CTA in every section
- Hiding price, timing, constraints, or eligibility
""",
        "design-product/patterns/empty-state.md": """# Empty State Pattern

An empty state should state:

- What is missing
- Why it matters
- The next useful action

Do not use decorative filler copy.
""",
        "design-product/memory/current-design-state.md": f"""# Current Design State

Updated: {today}

## Status
Design Product OS initialized. Product identity is still draft.

## Known stack
```json
{json.dumps(detected, indent=2)}
```

## Active constraints
- Plan before UI or Figma writes.
- Use proposal-before-change for design-system changes.
- Use tokens and product components.
- Audit meaningful design changes.
""",
        "design-product/memory/decision-log.md": f"""# Decision Log

## {today}

- Initialized Design Product OS for `{project_name}`.
""",
        "design-product/memory/approved-patterns.md": """# Approved Patterns

Add reusable patterns here after they survive review or implementation.
""",
        "design-product/memory/rejected-patterns.md": """# Rejected Patterns

Add rejected patterns here with reasons so future sessions avoid them.
""",
        "design-product/memory/design-system-proposals.md": """# Design System Proposals

Use this file for proposed, accepted, rejected, and deferred changes to identity, tokens, components, layout rules, patterns, Figma structure, or code mappings.
""",
        "design-product/audits/design-lint.config.json": json_dumps(
            {
                "maxCardsPerFile": 10,
                "scanExtensions": [".tsx", ".ts", ".jsx", ".js", ".css", ".scss", ".html", ".vue", ".svelte"],
                "allowedHexPaths": ["design-product/system/design-tokens.json"],
                "forbiddenTailwindClasses": [
                    "rounded-3xl",
                    "shadow-xl",
                    "shadow-2xl",
                    "bg-gradient-to-r",
                    "bg-gradient-to-br",
                    "backdrop-blur",
                    "blur-3xl",
                ],
            }
        ),
        "design-product/audits/last-audit.md": """# Last Audit

No audit has been run yet.
""",
        "design-product/agent-instructions.md": """# Agent Instructions

For design, UI, component, or Figma work in this repo:

1. Read `design-product/manifest.json`.
2. Read the relevant source-of-truth files listed in the manifest.
3. Produce an IA/component plan before writing UI or Figma nodes.
4. For design-system changes, record a proposal before mutating source-of-truth files.
5. Use product components over primitive UI composition.
6. Run `audit_design_product.py` after meaningful code edits.
7. Update `design-product/memory/` after durable decisions.
""",
    }

    touched: list[str] = []
    skipped: list[str] = []
    for rel, content in files.items():
        write_file(root / rel, content, args.force, touched, skipped)

    print(f"Design Product OS initialized at: {root / 'design-product'}")
    print(f"Project: {project_name}")
    print(f"Detected markers: {', '.join(detected['markers']) or 'none'}")
    print(f"Created/updated: {len(touched)}")
    for path in touched:
        print(f"  + {Path(path).relative_to(root)}")
    if skipped:
        print(f"Skipped existing files: {len(skipped)}")
        for path in skipped[:20]:
            print(f"  = {Path(path).relative_to(root)}")
        if len(skipped) > 20:
            print(f"  ... {len(skipped) - 20} more")
    print("Next: answer brand interview gaps, then run audit_design_product.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
