# leonamin-skills

Reusable skills for AI agentic coding tools.

## Skills

- `git-workflow`: Git branch, commit, push, and pull request rules.
- `mentor-debugging`: Explain development errors and fixes like a senior mentor.
- `swarm`: Role-separated orchestration for complex or high-risk work.

## Layout

Each skill lives in its own directory and uses `SKILL.md`.

```text
skills/
  git-workflow/
    SKILL.md
  mentor-debugging/
    SKILL.md
    agents/
      openai.yaml
  swarm/
    SKILL.md
    references/
      artifacts.md
      decision-rules.md
      role-prompts.md
  install.sh
```

This layout is compatible with Codex, Claude Code, Reasonix, and OpenCode.

## Install

Install one target:

```bash
./install.sh codex
./install.sh claude
./install.sh reasonix
./install.sh opencode
```

Install all supported targets:

```bash
./install.sh all
```

## Target Paths

- Codex: `~/.agents/skills/<skill-name>/`
- Codex compatibility: `~/.codex/skills/<skill-name>/`
- Claude Code: `~/.claude/skills/<skill-name>/`
- Reasonix: `~/.reasonix/skills/<skill-name>/`
- OpenCode: `~/.config/opencode/skills/<skill-name>/`
