# Audit Workflow

Use deterministic audit for code and qualitative audit for Figma or conceptual design.

## Deterministic Audit

Run:

```bash
python3 <skill-dir>/scripts/audit_design_product.py --path <repo>
```

Use `--strict` when the user wants a CI-style failure on errors.

The script checks common failure modes:

- Raw hex outside token files
- Tailwind gradient shortcuts
- Purple/blue SaaS gradient drift
- Radius abuse such as `rounded-3xl`
- Heavy shadows
- Glassmorphism and decorative blur
- Nested cards
- Card overuse per file
- Generic marketing copy
- Missing design-product setup

Treat findings as signals. Fix clear violations; explain any intentional exception and record it in memory.

## Qualitative Audit

For screens, components, or Figma output, check:

- Identity fit: does it match the product brief and anti-identity?
- IA: is the primary user decision obvious?
- Product specificity: could this screen belong to any random app?
- Token discipline: are colors, radius, spacing, and type from the system?
- Component grammar: are product components doing the semantic work?
- Layout restraint: are cards, shadows, badges, and gradients justified?
- Figma editability: named layers, auto layout, variables, components, clean hierarchy.
- Non-developer shareability: can a stakeholder understand the system without reading code?

## Audit Report Shape

Lead with findings:

```txt
Findings
- [High] file:line - Raw hex outside token file.
- [Medium] Figma frame "Product Detail" - Primary action competes with tertiary content.

Decisions
- Keep compact route rows for transport detail pages.

Memory Updated
- decision-log.md
```
