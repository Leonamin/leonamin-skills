# leonamin-skills Agent Rules

## Lazy Loading

- For Git work, load the `git-workflow` skill before running Git commands.
- For complex multi-agent work, load the `swarm` skill before orchestrating.
- Keep each skill as `<skill-name>/SKILL.md` at this repository root.
- Keep each agent as `<agent-name>.md` at `../agents/`.
- After editing a skill, agent, or `install.sh`, run:

```bash
bash -n install.sh
./install.sh all
```

## Available Agents (OpenCode)

| Agent | Complexity | Flow |
|---|---|---|
| `executor` (default) | 단순 | 바로 구현 |
| `planner` | 중간 | Planner → Executor |
| `planner` | 복잡 | Planner → Architect → Executor → Reviewer |
