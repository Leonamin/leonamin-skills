# leonamin-skills Maintenance Rules

This file is for maintaining the `leonamin-skills` repository itself.

If installable `AGENTS.md` or `CLAUDE.md` files are needed later, keep their source files
in a dedicated project-root subdirectory and have `install.sh` copy them to each target.

## Layout

- Keep each skill as `<skill-name>/SKILL.md` at this repository root.
- Keep each agent as `<agent-name>.md` at `../agents/`.
- Do not put skill lazy-loading rules here. Put trigger conditions in each skill's `description`.

## Verification

After editing a skill, agent, or `install.sh`, run:

```sh
bash -n install.sh
./install.sh all
```

## Available Agents

| Agent | Complexity | Flow |
|---|---|---|
| `executor` (default) | 단순 | 바로 구현 |
| `planner` | 중간 | Planner → Executor |
| `planner` | 복잡 | Planner → Architect → Executor → Reviewer |
