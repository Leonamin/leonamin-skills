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

# Retired skills are moved out of discovery, preserving locally edited copies.
retire_old_skills_from() {
  local target_root="$1"
  local skill_name
  local expected_heading
  local target_dir
  local backup_dir=""

  while IFS='|' read -r skill_name expected_heading; do
    target_dir="$target_root/$skill_name"
    [ -f "$target_dir/SKILL.md" ] || continue
    if ! grep -Fqx -- "$expected_heading" "$target_dir/SKILL.md"; then
      echo "Preserved unrecognized skill: $target_dir"
      continue
    fi
    if [ -z "$backup_dir" ]; then
      backup_dir="$(mktemp -d "${target_root%/}/../leonamin-retired-skills.XXXXXX")"
    fi
    mv "$target_dir" "$backup_dir/$skill_name"
    echo "Retired $skill_name to $backup_dir/$skill_name"
  done <<'RETIRED_SKILLS'
squad|# Squad 오케스트레이터
multi-squad|# 다중 작업 조율자
mentor|# 개발·운영 멘토
architecture-review|# 아키텍처 리뷰
language-review|# 언어 품질 리뷰
engineering-practices-review|# 소프트웨어 공학 리뷰
naming-rules|# 네이밍 리뷰
RETIRED_SKILLS
}

install_all_skills_to() {
  local target_root="$1"
  local label="$2"
  local skill_name
  local source_dir
  local target_dir

  mkdir -p "$target_root"
  retire_old_skills_from "$target_root"

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
