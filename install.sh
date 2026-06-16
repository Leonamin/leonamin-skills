#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

usage() {
  echo "Usage: $0 [reasonix|codex|claude|opencode|all]"
  echo ""
  echo "  reasonix   Install for Reasonix  (~/.reasonix/skills)"
  echo "  codex      Install for Codex     (~/.agents/skills, ~/.codex/skills)"
  echo "  claude     Install for Claude    (~/.claude/skills)"
  echo "  opencode   Install for OpenCode  (~/.config/opencode/skills, ~/.config/opencode/agents)"
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
    echo "Installed $skill_name for $label: $target_dir"
  done < <(skill_names)
}

install_reasonix() {
  install_all_skills_to "$HOME/.reasonix/skills" "Reasonix"
}

install_codex() {
  install_all_skills_to "$HOME/.agents/skills" "Codex"
  install_all_skills_to "$HOME/.codex/skills" "Codex compatibility"
}

install_claude() {
  install_all_skills_to "$HOME/.claude/skills" "Claude"
}

install_opencode() {
  install_all_skills_to "$HOME/.config/opencode/skills" "OpenCode"
  install_opencode_agents
}

AGENTS_DIR="$SCRIPT_DIR/../agents"

agent_names() {
  local agent_dir
  for agent_dir in "$AGENTS_DIR"/*; do
    if [ -f "$agent_dir" ]; then
      basename "$agent_dir"
    fi
  done | sort
}

install_opencode_agents() {
  local target_root="$HOME/.config/opencode/agents"
  local agent_name
  local source_file
  local target_file

  if [ ! -d "$AGENTS_DIR" ]; then
    echo "No agents directory found at $AGENTS_DIR, skipping"
    return
  fi

  mkdir -p "$target_root"

  while IFS= read -r agent_name; do
    source_file="$AGENTS_DIR/$agent_name"
    target_file="$target_root/$agent_name"
    cp "$source_file" "$target_file"
    echo "Installed agent $agent_name for OpenCode: $target_file"
  done < <(agent_names)
}

if [ -z "$(skill_names)" ] && [ ! -d "$AGENTS_DIR" ]; then
  echo "No skills or agents found under $SCRIPT_DIR" >&2
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
