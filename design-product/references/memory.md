# Memory Workflow

Design memory lives in the repo, not in chat.

## Files

- `design-product/memory/current-design-state.md`: compact current state for session reloads.
- `design-product/memory/decision-log.md`: dated decisions and rationale.
- `design-product/memory/approved-patterns.md`: patterns to reuse.
- `design-product/memory/rejected-patterns.md`: patterns to avoid and why.

## What To Record

Record durable decisions:

- Identity refinements
- Token changes
- Component naming decisions
- Reusable page or flow patterns
- Explicit anti-patterns
- Intentional exceptions to audit findings
- Figma structure decisions

Do not record routine implementation details unless they affect future design work.

## Script Usage

Append entries:

```bash
python3 <skill-dir>/scripts/update_memory.py --path <repo> \
  --decision "Use editorial comparison rows for package selection." \
  --approved "Use LocalNote for contextual trust copy." \
  --rejected "Avoid generic three-column feature grids on product pages."
```

Use stdin for a longer note:

```bash
printf '%s\n' "Decision text" | python3 <skill-dir>/scripts/update_memory.py --path <repo>
```

After memory updates, render context again if continuing the same task.
