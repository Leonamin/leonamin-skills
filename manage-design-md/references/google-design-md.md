# Google Labs DESIGN.md Reference

Use this reference when authoring or validating `DESIGN.md`. The normative upstream specification is https://github.com/google-labs-code/design.md and may change because the format is alpha.

## File contract

- Keep optional YAML front matter at the top, delimited by `---`.
- Keep machine-readable design tokens in front matter and human-readable rationale in Markdown.
- Treat token values as normative. Use prose to explain intent and application.

## Supported top-level tokens

```yaml
version: alpha
name: Product name
description: Optional summary
colors: {}
typography: {}
rounded: {}
spacing: {}
components: {}
```

Use token references as `{path.to.token}`. Component properties supported by the linter include `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, and `width`. Define state variants as separate components, such as `button-primary-active`.

## Canonical body order

1. `## Overview`
2. `## Colors`
3. `## Typography`
4. `## Layout`
5. `## Elevation & Depth`
6. `## Shapes`
7. `## Components`
8. `## Do's and Don'ts`

Additional sections belong after these sections. Omit irrelevant canonical sections rather than filling them with generic advice.

## Commands

```sh
npx @google/design.md lint DESIGN.md
npx @google/design.md diff DESIGN-before.md DESIGN.md
npx @google/design.md export --format dtcg DESIGN.md
```

Treat unresolved references as errors. Review contrast, orphaned-token, missing-typography, and section-order findings before handoff.
