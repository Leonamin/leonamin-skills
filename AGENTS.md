# leonamin-skills Maintenance Rules

This file is for maintaining the `leonamin-skills` repository itself.

If installable `AGENTS.md` or `CLAUDE.md` files are needed later, keep their source files
in a dedicated project-root subdirectory and define their installation separately from skills.

## Layout

- Keep each skill as `<skill-name>/SKILL.md` at this repository root.
- Keep each agent as `<agent-name>.md` at `../agents/`.
- Do not put skill lazy-loading rules here. Put trigger conditions in each skill's `description`.

## Verification

After adding or editing a skill, verify discovery from this repository:

```sh
pnpm dlx skills add . --list
```

Keep the README skill list in sync with root `<skill-name>/SKILL.md` files.
When changing installation instructions, verify the commands in a temporary project
with project-scoped installation so checks do not overwrite user-level skills.
