# leonamin-skills

Reusable skills for AI agentic coding tools.

## Skills

- `design-product`: Repo-scoped Design Product OS for AI-assisted product design.
- `git-workflow`: Git branch, commit, push, and pull request rules.
- `mentor`: 개발·운영 전반의 판단과 실행을 돕는 멘토.
- `multi-work-orchestrator`: Coordinate multiple related tasks across branches and worktrees.
- `swarm`: Role-separated orchestration for complex or high-risk work.

## Layout

Each skill lives in its own directory and uses `SKILL.md`.

```text
skills/
  design-product/
    SKILL.md
    agents/
      openai.yaml
    references/
      audit.md
      design-system.md
      figma.md
      init.md
      memory.md
      screen.md
    scripts/
      audit_design_product.py
      init_design_product.py
      propose_design_change.py
      render_context.py
      update_memory.py
  git-workflow/
    SKILL.md
  mentor/
    SKILL.md
    agents/
      openai.yaml
  multi-work-orchestrator/
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

This layout is compatible with Codex, Codex-compatible tools, Claude Code, and Reasonix.

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
- OpenCode: same as Codex, `~/.agents/skills/<skill-name>/`
- Claude Code: `~/.claude/skills/<skill-name>/`
- Reasonix: `~/.reasonix/skills/<skill-name>/`
