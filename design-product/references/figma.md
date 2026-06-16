# Figma MCP Workflow

Use this reference only when the task writes to or reads from Figma.

## Preconditions

- Follow the active Figma MCP skill prerequisites in the environment before calling write tools.
- Search or inspect existing Figma libraries/components before creating new primitives.
- Treat the repo `design-product/` files as the design brief and guardrail source.
- Do not use Figma as an image canvas. Create native editable structure.

## Required Flow

1. Load design-product context.
2. Classify the screen or component.
3. Produce the IA/component plan.
4. Identify Figma pages to use:
   - `00 Brand Board`
   - `01 Foundations`
   - `02 Components`
   - `03 Product Patterns`
   - `04 Screens`
   - `99 Rejected Patterns`
5. Map tokens to Figma variables where possible.
6. Create or update named frames with auto layout.
7. Use product-specific component names.
8. Audit the output.
9. Update design memory.

## Native Figma Requirements

- Use frames, auto layout, constraints, variables, styles, components, and variants.
- Name layers by domain role, not visual accident.
- Avoid flattened screenshots except as temporary references.
- Avoid one-off colors and radius values.
- Keep rejected explorations on `99 Rejected Patterns` if useful.

## If Figma Tools Are Missing

Do not pretend the file was updated. Produce:

- The IA/component plan
- Figma page/frame/component structure
- Token and variable mapping
- Audit checklist
- Exact next command or tool action needed when Figma MCP is available
