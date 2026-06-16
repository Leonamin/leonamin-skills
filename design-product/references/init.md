# Init Workflow

Use this reference after running `scripts/init_design_product.py`.

## Goal

Initialize a repo-local design operating layer without replacing the app's existing UI stack. The output should make future AI design work slower at the start and safer at the end: identity first, IA before visuals, product components over primitives, audit after changes, memory updated.

## Procedure

1. Inspect the project scan printed by the script.
2. Open `design-product/manifest.json`.
3. Fill or refine these files if the user provides product context:
   - `design-product/product-brief.md`
   - `design-product/identity/positioning.md`
   - `design-product/identity/visual-language.md`
   - `design-product/identity/anti-identity.md`
4. Keep unknowns explicit. Use `TBD` or low-confidence notes instead of pretending certainty.
5. If the project already has a UI system, map it as a primitive layer.
6. If the project lacks product components, propose 3-7 product-specific components before making screens.
7. Run the audit script once to establish a baseline.

## Brand Interview

Ask only the questions needed for the current task. Do not dump every question unless the user asks for a full interview.

Core questions:

1. What is the product in one sentence?
2. Why should users choose it over alternatives?
3. What is this product explicitly not?
4. What feeling should the first screen create?
5. Which design references are acceptable, and what must not be copied?
6. What is the primary conversion action?
7. Where must the interface create trust?
8. What generic AI-looking patterns should be avoided?

## Expected Repo Shape

`design-product/` is the durable memory layer. The most important files are:

- `manifest.json`
- `product-brief.md`
- `identity/visual-language.md`
- `system/design-tokens.json`
- `system/ai-anti-patterns.md`
- `system/component-rules.md`
- `system/layout-rules.md`
- `components/product-components.md`
- `memory/current-design-state.md`
- `memory/decision-log.md`

Do not create extra user-facing docs unless the user asks.
