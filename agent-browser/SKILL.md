---
name: agent-browser
description: Use the installed agent-browser CLI to open, inspect, interact with, test, and capture web pages. Trigger when verifying a local dev server, debugging a frontend visually, taking screenshots or PDFs, filling forms, checking responsive behavior, or extracting rendered page content.
---

# Agent Browser

Use `agent-browser` as the default browser automation tool. It runs Chrome for Testing through a CLI and is available to both Codex and OpenCode in this environment.

## Environment

- Confirm availability with `agent-browser --version` before the first browser task.
- This Linux environment requires `AGENT_BROWSER_ARGS=--no-sandbox`; the user shell is configured for it already.
- If Chrome is missing, run `agent-browser install`. If shared-library errors occur, use `agent-browser install --with-deps`.
- Never expose or persist passwords, cookies, auth state, API keys, or other secrets in screenshots, logs, or committed files.

## Standard workflow

For a page or local dev server:

```bash
agent-browser open <url>
agent-browser wait --load networkidle
agent-browser snapshot -i
```

Use the interactive refs from the snapshot (`@e1`, `@e2`, etc.) for actions:

```bash
agent-browser click @e1
agent-browser fill @e2 "text"
agent-browser press Enter
```

Take a fresh snapshot after navigation, form submission, modal changes, or other DOM updates because old refs become invalid.

## Capture and verification

- Screenshot: `agent-browser screenshot <path>.png`
- Full page: `agent-browser screenshot --full <path>.png`
- Annotated controls: `agent-browser screenshot --annotate <path>.png`
- PDF: `agent-browser pdf <path>.pdf`
- Page text: `agent-browser get text body`
- URL/title: `agent-browser get url` and `agent-browser get title`
- Close sessions when finished: `agent-browser close`

When a dev server is started, verify the actual rendered result with `open`, `wait --load networkidle`, `snapshot -i`, and a screenshot. Report the URL, key interaction result, and capture path.

## Locators and sessions

Prefer snapshot refs for a short interaction sequence. Use semantic locators when refs are inconvenient:

```bash
agent-browser find text "Sign In" click
agent-browser find label "Email" fill "user@example.com"
agent-browser find role button click --name "Submit"
```

Use named sessions when multiple sites or ports must stay open:

```bash
agent-browser --session app open http://localhost:3000
agent-browser --session admin open http://localhost:3001
agent-browser session list
```

For authenticated testing, prefer a temporary saved state outside the repository and delete it after use. Do not save state unless the user explicitly needs reusable authentication.

## Failure handling

- If launch fails with `No usable sandbox`, verify `AGENT_BROWSER_ARGS` and retry with `agent-browser --args "--no-sandbox" ...`.
- If a page is still loading, use `agent-browser wait --load networkidle` or wait for a specific selector.
- If an interaction fails after a page change, snapshot again and use new refs.
- If the browser cannot launch after dependency installation, report the exact error and environment limitation; do not silently substitute an unverified screenshot method.
