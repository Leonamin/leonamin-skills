# Screen And Component Workflow

Use this reference for UI, page, flow, component, or Figma screen requests.

## Required Reads

Read the compact context first:

```bash
python3 <skill-dir>/scripts/render_context.py --path <repo>
```

Then read these files as needed:

- `design-product/manifest.json`
- `design-product/product-brief.md`
- `design-product/identity/visual-language.md`
- `design-product/system/design-principles.md`
- `design-product/system/design-tokens.json`
- `design-product/system/ai-anti-patterns.md`
- `design-product/system/layout-rules.md`
- `design-product/system/component-rules.md`
- `design-product/components/product-components.md`
- Relevant file in `design-product/patterns/`

## Plan Before Write

Before editing code or Figma, produce a short plan containing:

- Screen type
- User goal
- Primary action
- Secondary actions
- Content hierarchy
- Layout pattern
- Product components to use
- Primitive components hidden inside product components
- Components or patterns explicitly not to use
- Anti-pattern risks and mitigations

If the task is tiny, the plan can be brief, but it must exist.

## Design Constraints

- Use design-product tokens or existing project tokens.
- Avoid raw hex outside token files.
- Avoid card-in-card.
- Avoid making every section a floating card.
- Avoid decorative gradients, glassmorphism, large soft shadows, and oversized radius unless the identity explicitly allows them.
- Avoid generic blocks such as "Powerful Features", "Everything You Need", fake testimonials, and fake metrics.
- Use stable responsive dimensions for fixed-format UI.
- Keep UI copy specific to the product.
- Keep product components named by domain concepts, not by visual containers.

## Product Component Rule

Do not let primitive UI names define the product language.

Weak:

```tsx
<Card>
  <CardHeader>Private Van</CardHeader>
  <CardContent>...</CardContent>
</Card>
```

Stronger:

```tsx
<TransportRouteSummary
  origin="Incheon Airport"
  destination="Seoul Hotel"
  vehicle="Private Van"
/>
```

The primitive `Card` may still exist inside `TransportRouteSummary`.

## Finish

Run the audit script after code edits. If Figma was modified, do a qualitative audit using `references/audit.md`. Append important decisions to memory.
