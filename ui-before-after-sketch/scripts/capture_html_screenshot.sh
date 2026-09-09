#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 || $# -gt 5 ]]; then
  echo "Usage: $0 <html-path> <output-png> [width] [height] [full|viewport]" >&2
  exit 2
fi

html_path="$1"
output_path="$2"
viewport_width="${3:-1440}"
viewport_height="${4:-1024}"
capture_mode="${5:-full}"

if [[ ! -f "$html_path" ]]; then
  echo "HTML file not found: $html_path" >&2
  exit 1
fi

if ! [[ "$viewport_width" =~ ^[1-9][0-9]*$ && "$viewport_height" =~ ^[1-9][0-9]*$ ]]; then
  echo "Viewport width and height must be positive integers." >&2
  exit 2
fi

if [[ "$capture_mode" != "full" && "$capture_mode" != "viewport" ]]; then
  echo "Capture mode must be either full or viewport." >&2
  exit 2
fi

html_path="$(cd "$(dirname "$html_path")" && pwd)/$(basename "$html_path")"
output_path="$(mkdir -p "$(dirname "$output_path")" && cd "$(dirname "$output_path")" && pwd)/$(basename "$output_path")"

browser_bin="${AGENT_BROWSER_BIN:-agent-browser}"
if ! command -v "$browser_bin" >/dev/null 2>&1; then
  echo "Browser CLI not found: $browser_bin" >&2
  echo "Install agent-browser or set AGENT_BROWSER_BIN to its executable path." >&2
  exit 1
fi

file_url="$(python3 -c 'from pathlib import Path; import sys; print(Path(sys.argv[1]).as_uri())' "$html_path")"
session_name="ui-before-after-$$-$(date +%s)"
browser_args="${AGENT_BROWSER_ARGS:-}"

run_browser() {
  AGENT_BROWSER_ARGS="$browser_args" "$browser_bin" --session "$session_name" "$@"
}

cleanup() {
  run_browser close >/dev/null 2>&1 || true
}

trap cleanup EXIT

run_browser set viewport "$viewport_width" "$viewport_height"
run_browser open "$file_url"
run_browser wait --load networkidle
if [[ "$capture_mode" == "full" ]]; then
  run_browser screenshot --full "$output_path"
else
  run_browser screenshot "$output_path"
fi

echo "Screenshot saved to $output_path ($capture_mode, ${viewport_width}x${viewport_height})"
