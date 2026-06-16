# Design System Change Loop

Use this reference when the user wants to discuss, revise, add, remove, rename, or govern design tokens, components, patterns, visual language, Figma structure, or code mappings.

## Rule

Discussion is not implementation. If the user is exploring or deciding, do not edit product UI, Figma, or token files until the decision is explicit or strongly implied.

## Required Reads

Run compact context:

```bash
python3 <skill-dir>/scripts/render_context.py --path <repo>
```

Then read the relevant files:

- Identity change: `product-brief.md`, `identity/*`
- Token change: `system/design-tokens.json`, `system/token-taxonomy.md`
- Component change: `components/product-components.md`, `components/component-contracts.json`, `system/component-rules.md`
- Layout or pattern change: `system/layout-rules.md`, `patterns/*`
- Figma system change: `system/figma-rules.md`, `references/figma.md`
- Governance change: `system/change-workflow.md`, `memory/design-system-proposals.md`

## Loop

1. Classify the change:
   - identity
   - token
   - component
   - pattern
   - layout
   - figma
   - code-mapping
   - governance
2. State the problem in product terms.
3. Identify the affected files, Figma pages, and code components.
4. Offer 2-3 options with tradeoffs.
5. Recommend one option.
6. Record the proposal with `scripts/propose_design_change.py`.
7. Wait for a decision when the user is still discussing.
8. Apply only the accepted scope.
9. Run audit or explain why it is not applicable.
10. Update memory and proposal status.

## Component Change Spec

For each product component proposal, define:

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

## Token Change Spec

For token proposals, define:

- Semantic role
- Existing token to replace or extend
- Affected components
- Allowed values
- Forbidden one-off values
- Figma variable mapping
- Code mapping
- Migration notes

## Decision States

- Proposed: captured but not adopted.
- Accepted: apply to source-of-truth files and memory.
- Rejected: add rationale to rejected patterns or proposal notes.
- Deferred: keep as a known question.

## Response Shape

Use this shape for design-system discussion:

```txt
Change Type
component

Problem
The current product card is a primitive Card composition, so the product language is not reusable.

Options
1. Rename only.
2. Create a product component boundary.
3. Redesign the entire pattern.

Recommendation
Option 2.

Affected Files
- design-product/components/product-components.md
- design-product/components/component-contracts.json
- relevant UI component files

Decision Needed
Confirm whether to adopt Option 2 before implementation.
```

If the user directly asks to implement the change, treat the decision as accepted and continue through audit and memory.
