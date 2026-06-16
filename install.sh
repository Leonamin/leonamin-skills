#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

usage() {
  echo "Usage: $0 [reasonix|codex|claude|opencode|all]"
  echo ""
  echo "  reasonix   Install for Reasonix  (~/.reasonix/skills)"
  echo "  codex      Install for Codex     (~/.agents/skills)"
  echo "  claude     Install for Claude    (~/.claude/skills)"
  echo "  opencode   Install for OpenCode  (~/.agents/skills)"
  echo "  all        Install for all supported tools"
  exit 1
}

TARGET="${1:-reasonix}"

skill_names() {
  local skill_dir

  for skill_dir in "$SCRIPT_DIR"/*; do
    if [ -f "$skill_dir/SKILL.md" ]; then
      basename "$skill_dir"
    fi
  done | sort
}

install_all_skills_to() {
  local target_root="$1"
  local label="$2"
  local skill_name
  local source_dir
  local target_dir

  mkdir -p "$target_root"

  while IFS= read -r skill_name; do
    source_dir="$SCRIPT_DIR/$skill_name"
    target_dir="$target_root/$skill_name"

    rm -rf "$target_dir"
    cp -R "$source_dir" "$target_dir"
    find "$target_dir" \( -name "__pycache__" -o -name "*.pyc" \) -exec rm -rf {} +
    echo "Installed $skill_name for $label: $target_dir"
  done < <(skill_names)
}

install_reasonix() {
  install_all_skills_to "$HOME/.reasonix/skills" "Reasonix"
}

install_codex_compatible() {
  local label="${1:-Codex}"
  install_all_skills_to "$HOME/.agents/skills" "$label"
}

install_codex() {
  install_codex_compatible "Codex"
}

install_claude() {
  install_all_skills_to "$HOME/.claude/skills" "Claude"
}

install_opencode() {
  install_codex_compatible "OpenCode"
}

if [ -z "$(skill_names)" ]; then
  echo "No skills found under $SCRIPT_DIR" >&2
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
    install_codex_compatible "Codex/OpenCode"
    install_claude
    ;;

  *)
    usage
    ;;
esac
