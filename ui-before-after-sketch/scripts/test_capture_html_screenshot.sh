#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
capture_script="$script_dir/capture_html_screenshot.sh"
test_dir="$(mktemp -d)"

cleanup() {
  rm -rf "$test_dir"
}

trap cleanup EXIT

html_path="$test_dir/index.html"
fake_browser="$test_dir/agent-browser"
browser_log="$test_dir/browser.log"
touch "$html_path"

cat > "$fake_browser" <<'FAKE_BROWSER'
#!/usr/bin/env bash
set -euo pipefail

printf 'ARGS:%s\n' "$*" >> "$FAKE_BROWSER_LOG"
printf 'ENV:%s\n' "${AGENT_BROWSER_ARGS:-}" >> "$FAKE_BROWSER_LOG"

last_argument=""
for argument in "$@"; do
  last_argument="$argument"
done

if [[ " $* " == *" screenshot "* ]]; then
  touch "$last_argument"
fi
FAKE_BROWSER
chmod +x "$fake_browser"

fail() {
  echo "FAIL: $1" >&2
  exit 1
}

assert_log_contains() {
  grep -F -- "$1" "$browser_log" >/dev/null || fail "missing log entry: $1"
}

assert_log_exact() {
  grep -Fx -- "$1" "$browser_log" >/dev/null || fail "missing exact log entry: $1"
}

full_output="$test_dir/full.png"
FAKE_BROWSER_LOG="$browser_log" AGENT_BROWSER_BIN="$fake_browser" \
  "$capture_script" "$html_path" "$full_output" 390 844

[[ -f "$full_output" ]] || fail "full screenshot output was not created"
assert_log_contains "set viewport 390 844"
assert_log_contains "screenshot --full $full_output"
assert_log_contains " close"
assert_log_exact "ENV:"

: > "$browser_log"
viewport_output="$test_dir/viewport.png"
FAKE_BROWSER_LOG="$browser_log" AGENT_BROWSER_BIN="$fake_browser" \
  "$capture_script" "$html_path" "$viewport_output" 1440 1024 viewport

[[ -f "$viewport_output" ]] || fail "viewport screenshot output was not created"
assert_log_contains "set viewport 1440 1024"
assert_log_contains "screenshot $viewport_output"
if grep -F -- "screenshot --full" "$browser_log" >/dev/null; then
  fail "viewport mode passed --full"
fi

if AGENT_BROWSER_BIN="$test_dir/missing-browser" \
  "$capture_script" "$html_path" "$test_dir/missing.png" >/dev/null 2>&1; then
  fail "missing browser was accepted"
fi

if FAKE_BROWSER_LOG="$browser_log" AGENT_BROWSER_BIN="$fake_browser" \
  "$capture_script" "$html_path" "$test_dir/invalid.png" 390 844 invalid >/dev/null 2>&1; then
  fail "invalid capture mode was accepted"
fi

echo "All capture_html_screenshot tests passed."
