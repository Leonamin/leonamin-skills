---
name: design-product
description: Repo-scoped Design Product OS for AI-assisted product design. Use when the user asks to initialize, discuss, change, evolve, or enforce a project design system; define product identity; reduce AI-looking UI; create or update Figma screens through MCP; generate or revise design tokens/components/patterns; audit AI slop; or preserve design decisions across chat sessions.
---

# Design Product

Use this skill to turn an existing project into a designable product system:

1. Durable repo memory in `design-product/`
2. Identity, token, component, layout, and anti-slop rules
3. A plan-before-write workflow for screens and components
4. A proposal-before-change loop for evolving the design system
5. Deterministic audit scripts for common AI UI failures
6. Figma MCP guidance for editable native Figma output

Keep the project repository as the source of truth. Chat memory is temporary.

## First Move

Resolve script paths relative to this `SKILL.md`.

- New project setup: run `scripts/init_design_product.py --path <repo>`, then read `references/init.md`.
- Existing `design-product/`: run `scripts/render_context.py --path <repo>` before design work.
- Design system discussion or changes: read `references/design-system.md`; use `scripts/propose_design_change.py` for durable proposals.
- Screen or component work: read `references/screen.md`; also read `references/figma.md` if writing to Figma.
- Audit or review: run `scripts/audit_design_product.py --path <repo>` and read `references/audit.md`.
- Memory update: use `scripts/update_memory.py --path <repo>` and read `references/memory.md`.

## Required Operating Rules

- Read `design-product/manifest.json` before every design task.
- Read the listed source-of-truth files relevant to the task.
- Do not write UI or Figma nodes before producing an IA/component plan.
- Use product-specific components over primitive UI composition.
- Treat shadcn, Radix, MUI, Chakra, Tailwind, or similar libraries as primitives, not the product design language.
- Preserve existing project conventions unless they conflict with explicit design-product hard rules.
- Do not invent testimonials, metrics, brands, destinations, compliance claims, or trust markers.
- Do not use generic SaaS page structures unless the product is actually a SaaS product.
- Record durable decisions in `design-product/memory/`.
- When the user wants to discuss design-system changes, do not apply changes until a proposal and decision are clear.

## Commands

Initialize:

```bash
python3 <skill-dir>/scripts/init_design_product.py --path .
```

Render compact context:

```bash
python3 <skill-dir>/scripts/render_context.py --path .
```

Audit:

```bash
python3 <skill-dir>/scripts/audit_design_product.py --path .
```

Propose design-system change:

```bash
python3 <skill-dir>/scripts/propose_design_change.py --path . \
  --type component \
  --title "Replace generic product cards with RouteSummary" \
  --problem "Transport detail pages rely on primitive Card composition." \
  --option "Create RouteSummary as the product component boundary." \
  --recommendation "Adopt RouteSummary and keep Card as an internal primitive."
```

Append decisions:

```bash
python3 <skill-dir>/scripts/update_memory.py --path . \
  --decision "Adopt compact comparison rows for pricing-heavy product cards." \
  --approved "Use route-summary components for transport detail pages." \
  --rejected "Avoid nested marketing cards inside detail pages."
```

## Figma Work

When Figma MCP tools are available, use them only after the plan step. Native Figma output must use named frames, auto layout, variables/tokens where possible, reusable components, and a clear layer hierarchy. Before calling any Figma write tool, follow the active Figma tool skill prerequisites in the environment.

## Output Contract

For meaningful work, finish with:

- Files created or updated
- Audit result or skipped-audit reason
- Design memory entries added
- Next design-product command to run, if useful
