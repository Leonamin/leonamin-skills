---

name: explain
description: Explain unfamiliar or complex topics with minimal cognitive overhead. Use visual structure, concrete examples, and progressive disclosure instead of long prose. Assume an intelligent reader with zero prior knowledge of the topic.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Explain

Explain the requested topic so that an intelligent person with no prior knowledge of the topic can understand it with minimal cognitive overhead.

The goal is not to "explain like I'm five."

The goal is:

> Make the path to understanding as short and clear as possible without making the explanation inaccurate.

## Core principles

### 1. Assume zero domain knowledge, not low intelligence

Treat the reader as a smart non-expert.

Do not assume familiarity with domain-specific terminology, conventions, notation, architecture, or background knowledge.

Do not use childish language or simplistic analogies merely because the reader is unfamiliar with the topic.

Simplify the explanation, not the reader.

### 2. Big picture first

Before explaining details, establish what the thing is, why it exists, or what problem it solves.

The reader should quickly be able to answer:

* What am I looking at?
* Why does this exist?
* What is the central idea?

Prefer one or two sentences plus a visual structure over an introductory essay.

Do not begin with history, formal definitions, taxonomy, or prerequisite lectures unless they are essential to understanding the core idea.

### 3. Visual structure before prose

Do not default to long-form prose.

When information has meaningful structure, represent that structure visually before explaining it in paragraphs.

Useful representations include:

* flows for processes
* diagrams for structures and relationships
* side-by-side comparisons for differences
* timelines for sequences over time
* trees for hierarchies
* tables for structured comparisons
* annotated examples for concrete mechanisms
* charts for meaningful quantitative relationships
* cards or panels for distinct concepts

The reader should not have to reconstruct an obvious diagram mentally from several paragraphs of prose.

### 4. Choose the lightest effective representation

Visual-first does not mean HTML-first.

Choose the simplest representation that materially improves understanding.

Use, roughly in order of necessity:

1. Structured Markdown
2. Tables or simple text diagrams
3. Mermaid or another suitable diagram format
4. HTML/CSS visualization
5. Interactive HTML only when interaction itself improves understanding

Escalate to HTML when spatial layout, highlighting, multiple coordinated panels, animation, or interaction would substantially reduce cognitive load.

Do not create rich visuals merely for decoration.

### 5. Few words, high information density

Prefer short explanations surrounding a strong visual model.

Avoid large uninterrupted blocks of prose.

As a default:

* keep paragraphs short
* avoid repeating the same idea in different wording
* omit background knowledge that is not currently necessary
* omit edge cases from the first explanation
* avoid exhaustive enumeration

The core idea should ideally be understandable from roughly one screen of content.

If the subject requires substantially more explanation, disclose it progressively instead of presenting everything at once.

### 6. Concrete before abstract

When possible, show a concrete case before introducing the generalized abstraction.

Prefer:

concrete situation
→ observable behavior
→ mechanism
→ technical concept

over:

formal definition
→ terminology
→ abstract mechanism
→ example

A reader should have something concrete to attach the abstraction to.

### 7. Mechanism before terminology

Whenever practical, explain what happens before naming the formal concept.

For example, prefer:

"Two operations both read the old value, modify it independently, and one overwrites the other's result."

Then introduce:

"This class of problem is called a race condition."

Do not force the reader to memorize terminology before they understand what the terminology refers to.

When a technical term is important, introduce it once the reader has enough intuition to understand why the term exists.

### 8. Just-in-time prerequisites

Do not front-load prerequisite lectures.

If understanding the current concept requires another concept, explain only the minimum prerequisite necessary at the moment it becomes relevant.

Then return immediately to the original explanation.

Avoid chains such as:

"To understand A, first we need B. To understand B, first we need C..."

unless those prerequisites are genuinely unavoidable.

### 9. Progressive disclosure

Organize explanations by depth.

A useful default ladder is:

Level 1 — Big picture
What it is and why it matters.

Level 2 — Intuition
A concrete example or visual mental model.

Level 3 — Mechanism
What actually happens step by step.

Level 4 — Technical model
Precise terminology, implementation details, notation, or formal structure.

Level 5 — Nuance
Tradeoffs, limitations, exceptions, edge cases, and deeper implications.

Do not automatically expand every level.

Give enough depth to answer the question, and make deeper layers easy to continue into when useful.

### 10. Preserve correctness

Clarity is never an excuse for being wrong.

Simplify the packaging, not load-bearing facts.

If an intuitive explanation is useful but technically incomplete, explicitly mark the boundary.

For example:

"At this level, you can think of it as X. Strictly speaking, Y also happens, but that distinction is not necessary yet."

Never silently replace a real mechanism with a misleading analogy.

### 11. Use analogies selectively

Use an analogy only when it reduces cognitive load.

Prefer mechanism-based explanations over metaphor-based explanations.

When using an analogy:

* state what corresponds to what
* avoid extending the analogy beyond where it works
* return to the real mechanism afterward

Do not use childish analogies by default.

### 12. Control jargon

Do not introduce unexplained jargon.

When a technical term is useful:

1. establish the intuition
2. introduce the term
3. give a short plain-language meaning
4. continue using the correct term

Do not permanently replace useful technical vocabulary with vague everyday wording.

The reader should leave understanding both the concept and the name professionals use for it.

## Explanation workflow

Before responding, determine:

1. What is the single most important idea the reader needs to understand?
2. What does the reader need to see before the explanation will make sense?
3. What representation best matches the information?
4. What is the smallest concrete example that demonstrates the mechanism?
5. Which prerequisites are actually necessary?
6. At what depth should the initial explanation stop?

Then construct the explanation approximately as:

Big picture
→ visual model
→ concrete example
→ mechanism
→ terminology
→ deeper detail only when necessary

This is a reasoning guideline, not a rigid output template.

Do not force every explanation into identical headings or layouts.

## Representation selection

Match the representation to the information.

Process or transformation:
→ flow diagram

System architecture:
→ component or relationship diagram

Hierarchy:
→ tree

Two or more alternatives:
→ side-by-side comparison or table

Sequence over time:
→ timeline

Cause and effect:
→ causal flow

Algorithm:
→ state transitions or step-by-step visualization

Spatial structure:
→ annotated diagram

Quantitative relationship:
→ chart

Abstract concept:
→ concrete example followed by a conceptual diagram

Simple concept:
→ concise structured Markdown may be enough

Complex concept where layout itself matters:
→ HTML/CSS visualization

Concept where changing inputs reveals the mechanism:
→ interactive HTML may be appropriate

## HTML guidance

When HTML materially improves understanding, create a self-contained explainer rather than a decorative webpage.

Prioritize:

* clear visual hierarchy
* large readable labels
* whitespace
* spatial relationships
* arrows and grouping
* highlighted state changes
* side-by-side comparisons
* minimal explanatory text

Avoid:

* decorative dashboards
* unnecessary navigation
* excessive animation
* dense paragraphs inside cards
* UI elements that do not teach anything

Interaction is optional.

Use interaction only when manipulating a value, stepping through a process, toggling states, or revealing relationships helps the reader understand the mechanism.

## Failure modes

Avoid these common failures.

### Textbook preamble

Do not start with several paragraphs of definitions and history before reaching the point.

### Prerequisite rabbit hole

Do not turn one unfamiliar prerequisite into another full lesson unless necessary.

### Wall of text

Do not make the reader parse long prose when the same structure could be shown visually.

### Pretty but useless visualization

Do not convert difficult prose into attractive cards without improving the conceptual structure.

### Analogy substitution

Do not let an analogy replace the actual mechanism.

### Premature jargon

Do not introduce several technical terms before the reader knows what problem they describe.

### Fake simplicity

Do not omit a detail when omitting it would cause the reader to form a fundamentally incorrect model.

### Exhaustive first response

Do not explain every implementation detail, exception, historical reason, and edge case merely because they exist.

## Success criterion

A successful explanation lets a smart newcomer quickly form a correct mental model of the topic.

They should understand:

* what it is
* why it exists
* roughly how it works
* the important technical name or vocabulary
* where their simplified mental model stops being accurate

They should not need to read a miniature textbook chapter before reaching that point.
