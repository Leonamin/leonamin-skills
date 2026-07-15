# leonamin-skills

Reusable skills for AI agentic coding tools.

## Skills

- `design-audit`: 기존 GUI의 문제를 감사하고 세부 개선.
- `design-product`: 프로젝트별 제품 정체성과 디자인 시스템을 운영.
- `figma-design`: 제품 디자인 시스템과 감사 결과를 Figma에서 구현.
- `git-workflow`: Git branch, commit, push, and pull request rules.
- `mentor`: 개발·운영 전반의 판단과 실행을 돕는 멘토.
- `multi-squad`: 여러 관련 작업을 브랜치와 워크트리로 나누어 조율.
- `squad`: 복잡하거나 위험한 작업을 역할별로 나누어 검증.
- `wiki-read`: 작업과 의사결정에 필요한 위키 지식을 읽고 요약.
- `wiki-setup`: 프로젝트 위키 위치와 계층 구조를 초기 설정.
- `wiki-update`: 대화와 결정을 위키에 기록하고 갱신.

## Layout

Each skill lives in its own directory and uses `SKILL.md`.

```text
skills/
  design-product/
    SKILL.md
    agents/
      openai.yaml
    references/
      design-system.md
      init.md
      memory.md
      screen.md
    scripts/
      init_design_product.py
      propose_design_change.py
      render_context.py
      update_memory.py
  design-audit/
    SKILL.md
    agents/
      openai.yaml
    references/
      audit.md
    scripts/
      audit_design.py
  figma-design/
    SKILL.md
    agents/
      openai.yaml
    references/
      figma.md
  git-workflow/
    SKILL.md
  mentor/
    SKILL.md
    agents/
      openai.yaml
  multi-squad/
    SKILL.md
    agents/
      openai.yaml
  squad/
    SKILL.md
    references/
      artifacts.md
      decision-rules.md
      role-prompts.md
  wiki-read/
    SKILL.md
    agents/
      openai.yaml
  wiki-setup/
    SKILL.md
    agents/
      openai.yaml
  wiki-update/
    SKILL.md
    agents/
      openai.yaml
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
