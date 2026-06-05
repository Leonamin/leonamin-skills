# leonamin-skills

Reusable skills for AI agentic coding tools.

## Skills

- `git-workflow`: Git branch, commit, push, and pull request rules.

## Layout

Each skill lives in its own directory and uses `SKILL.md`.

```text
skills/
  git-workflow/
    SKILL.md
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

- Codex: `~/.agents/skills/git-workflow/SKILL.md`
- Codex compatibility: `~/.codex/skills/git-workflow/SKILL.md`
- Claude Code: `~/.claude/skills/git-workflow/SKILL.md`
- Reasonix: `~/.reasonix/skills/git-workflow/SKILL.md`
- OpenCode: `~/.config/opencode/skills/git-workflow/SKILL.md`

