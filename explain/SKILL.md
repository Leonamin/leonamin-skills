---
name: explain
description: Explain unfamiliar or complex topics to a smart non-expert with concise visual structure, concrete examples, and interaction when it improves understanding. Use for explanations, mental models, comparisons, walkthroughs, diagrams, or interactive explainers.
---

# Explain

Give the reader a correct mental model with as little cognitive overhead as possible.

## Approach

- Start with what the topic is and why it matters.
- Assume no domain knowledge, but do not use childish language.
- Prefer a small concrete example before abstractions.
- Explain the mechanism before introducing jargon; define important terms briefly.
- Add prerequisites only when they become necessary.
- Stop when the question is answered. Offer deeper detail instead of front-loading edge cases.

## Visualization

Treat visualization and interaction as core explanation tools.

- Show meaningful structure before describing it at length. Use a flow for a process, a diagram for relationships, a table for comparisons, and a timeline for sequences.
- Choose the lightest representation that preserves the idea: structured Markdown, a table or text diagram, a native visualization, then self-contained HTML.
- Use interaction when changing inputs, stepping through states, or toggling alternatives reveals the mechanism.
- Do not replace a useful visualization with prose merely because the host lacks a native visualization tool.

## Portable interactive output

1. Use a native visualization or browser-preview tool when available.
2. Otherwise create one self-contained HTML file with inline CSS and JavaScript.
3. Avoid frameworks, package installation, build steps, and network-loaded assets.
4. Keep controls labeled, keyboard-usable, responsive, and focused on teaching the mechanism.
5. Open and verify the result when browser tooling is available. Otherwise provide the absolute file path and state that visual verification was unavailable.

Do not create an artifact when concise Markdown explains the topic equally well.

## Accuracy

- Do not trade correctness for simplicity.
- Mark where a simplified model stops being accurate.
- Use analogies only when they clarify the mechanism, and state their limits.

Do not force every explanation into the same layout or add decorative visuals that do not improve understanding.
