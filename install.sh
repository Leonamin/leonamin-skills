#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_NAME="git-workflow"
SKILL_SOURCE="$SCRIPT_DIR/$SKILL_NAME/SKILL.md"

usage() {
  echo "Usage: $0 [reasonix|codex|claude|opencode|all]"
  echo ""
  echo "  reasonix   Install for Reasonix  (~/.reasonix/skills/git-workflow/SKILL.md)"
  echo "  codex      Install for Codex     (~/.agents/skills/git-workflow/SKILL.md, ~/.codex/skills/git-workflow/SKILL.md)"
  echo "  claude     Install for Claude    (~/.claude/skills/git-workflow/SKILL.md)"
  echo "  opencode   Install for OpenCode  (~/.config/opencode/skills/git-workflow/SKILL.md)"
  echo "  all        Install for all supported tools"
  exit 1
}

TARGET="${1:-reasonix}"

install_skill_dir() {
  local target_dir="$1"

  mkdir -p "$target_dir"
  cp "$SKILL_SOURCE" "$target_dir/SKILL.md"
}

install_reasonix() {
  install_skill_dir "$HOME/.reasonix/skills/$SKILL_NAME"
  echo "Installed for Reasonix: ~/.reasonix/skills/$SKILL_NAME/SKILL.md"
}

install_codex() {
  install_skill_dir "$HOME/.agents/skills/$SKILL_NAME"
  install_skill_dir "$HOME/.codex/skills/$SKILL_NAME"
  echo "Installed for Codex: ~/.agents/skills/$SKILL_NAME/SKILL.md"
  echo "Installed for Codex compatibility: ~/.codex/skills/$SKILL_NAME/SKILL.md"
}

install_claude() {
  install_skill_dir "$HOME/.claude/skills/$SKILL_NAME"
  echo "Installed for Claude: ~/.claude/skills/$SKILL_NAME/SKILL.md"
}

install_opencode() {
  install_skill_dir "$HOME/.config/opencode/skills/$SKILL_NAME"
  echo "Installed for OpenCode: ~/.config/opencode/skills/$SKILL_NAME/SKILL.md"
}

if [ ! -f "$SKILL_SOURCE" ]; then
  echo "Missing skill source: $SKILL_SOURCE" >&2
  exit 1
fi

case "$TARGET" in
  reasonix)
    install_reasonix
    ;;

  codex)
    install_codex
    ;;

  claude)
    install_claude
    ;;

  opencode)
    install_opencode
    ;;

  all)
    install_reasonix
    install_codex
    install_claude
    install_opencode
    ;;

  *)
    usage
    ;;
esac
