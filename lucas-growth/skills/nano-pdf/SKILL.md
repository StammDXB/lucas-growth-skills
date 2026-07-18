---
name: nano-pdf
description: >-
  Edit specific pages of a PDF or add new AI-generated slides using natural-language
  instructions. Use when the user wants to modify content on a PDF page, fix a slide,
  add a new page to a deck, or make any targeted AI-powered edit to an existing PDF.
  Triggers on: "edit page X of PDF", "fix this slide", "add a slide to", "modify the PDF",
  "change page 3 of", "update this PDF page". Use this in addition to the pdf skill when
  the task requires changing existing content — not just reading or restructuring.
---

# Skill: nano-pdf

**One responsibility:** Edit or add specific pages in an existing PDF via AI-generated natural language instructions.

This skill does NOT: read, extract, merge, split, or create PDFs from scratch — use the `pdf` skill for those.

---

## Overview

`nano-pdf` applies AI-powered edits to specific pages of a PDF. It uses Nano Banana (Gemini image generation) to regenerate individual pages based on your instructions, then stitches them back into the original document.

Invoked via: `uvx nano-pdf`

---

## Commands

### Edit a page
```bash
uvx nano-pdf edit <file.pdf> <page-number> "<natural language instruction>"
```

**Example:**
```bash
uvx nano-pdf edit proposal.pdf 3 "Update the pricing table: change Enterprise plan to $599/month"
uvx nano-pdf edit deck.pdf 1 "Change the title to 'Q2 2026 Roadmap' and update the subtitle to 'Hospitality Division'"
```

Multiple pages in one command:
```bash
uvx nano-pdf edit deck.pdf 2 "Add bullet: 'Dubai expansion confirmed'" 4 "Update chart to show 30% growth"
```

### Add a new slide
```bash
uvx nano-pdf add <file.pdf> <insert-after-page> "<description of new slide>"
```

**Example:**
```bash
uvx nano-pdf add proposal.pdf 0 "Title slide: 'Guest Retention Strategy — Acme Hospitality'"
uvx nano-pdf add deck.pdf 5 "Closing slide with call to action: 'Schedule a Discovery Call'"
```

Note: Page numbering may be 0-based or 1-based depending on version — if the wrong page is edited, try adjusting by ±1.

---

## Workflow

1. Identify the PDF file path and which pages need editing
2. Describe the required change as a clear natural-language instruction (be specific about text, numbers, positioning)
3. Run `uvx nano-pdf edit` (or `add`) with the file, page, and instruction
4. Review the output — AI edits warrant human review before distribution
5. If the result is for a client or external use, route through INBOX as usual

---

## Tips

- **Be specific in instructions** — "change the title" is vague; "change the title text to 'Q2 Hospitality Review 2026'" is actionable
- **Layouts are rebuilt by AI** — complex page layouts may simplify; review visuals carefully
- **Images in original pages** may be approximated — check fidelity on image-heavy pages
- **Chain edits** — you can pass multiple page+instruction pairs in a single command for efficiency
