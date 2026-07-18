---
name: ai-output-hygiene
description: >-
  Pre-output hygiene check that fires before ANY substantial deliverable. Blocks AI-fingerprint patterns: "John Doe", "Acme", 99.99%, Lorem Ipsum, Elevate/Seamless/Unleash, "// rest of code", "for brevity", skeleton outputs when full implementation was requested. Enforces completeness count-check before emission. Provides clean breakpoint pause protocol for long outputs that approach the token limit. Mandatory for: copy, code, mock data, placeholder content, design outputs with fake names/numbers, any multi-file delivery.
---

# /ai-output-hygiene: Pre-Emission Discipline

LLMs have three recognizable failure patterns:
1. **Placeholder fingerprint**: John Doe, Acme, Lorem Ipsum, 99.99%, cliche verbs.
2. **Laziness filler**: `// rest of code`, `for brevity`, skeletons when full code was asked.
3. **Token-limit panic**: truncating mid-function, compressing to fit.

This skill is a mandatory hygiene gate before emission.

Source: Leonxlnx taste-skill / output-skill / redesign-skill.

---

## When This Skill Fires

Auto-invoke before emitting:

- Any frontend, design, or landing-page deliverable that contains mock data, testimonials, names, numbers, or copy.
- Any multi-file or multi-function code delivery of 300+ lines.
- Any response requested as "full implementation", "complete", "production-ready".
- Any marketing copy, headline, landing page, or proposal output.
- Any long-form structured output (brief, SOP, research report).

This is a gate, not a slash command. The user shouldn't need to ask for it.

---

## Part 1: The Jane Doe Effect (Placeholder Fingerprint)

Never use the banned tokens below. Replace with organic, specific content.

### Banned token list (hard block)

**Names**: John Doe, Jane Doe, Jane Smith, John Smith, Bob Smith, Emily Johnson, Michael Johnson, placeholder avatar names, any pair of first + last where both are the five most common English names.

**Companies**: Acme, Acme Corp, Nexus, SmartFlow, CloudVision, DataFlow, TechPro, BrightLabs, Globex, Initech, any generic "X Corp" or "X Labs" or "X Systems".

**Numbers**: 99.99%, 100%, 99%, 50%, $100.00, 1234567, +1 (555) 123-4567, 1,000,000 as round stat.

**Copy clichés**: "Elevate", "Seamless", "Unleash", "Next-Gen", "Game-changer", "Delve", "Tapestry", "In the world of...", "In today's fast-paced world", "Revolutionary", "Cutting-edge" (unused as genuine term), "State-of-the-art", "Boost your productivity", "Supercharge your".

**Filler text**: Lorem Ipsum, "The quick brown fox", any dummy sentence from a content generator, duplicate paragraphs across sections.

**Dates**: all blog posts sharing the same publish date, "2 days ago" repeated, any `new Date()` that rounds to the current moment across multiple items.

**Errors**: "Oops!", "Something went wrong", exclamation marks in error copy.

### Replace with

- **Names**: Diverse, realistic, locale-appropriate. Use name generators specific to the target geography. For avatars, each person needs a unique image (don't reuse stock). Example pairings: "Priya Rao", "Dmitri Volkov", "Aisha Okonkwo", "Matteo Ferraro", "Yuki Tanaka", "Lucia Reyes".
- **Companies**: Invent premium, contextual brand names that fit the industry. Restaurant CMS → "Tavola", "Sal & Copper", "Mira Hospitality". SaaS dashboard → "Halcyon", "Leaflet", "Beacon". Fintech → "Threadline Capital", "Ember Banking". Avoid anything ending in "AI" unless the product is explicitly an AI tool.
- **Numbers**: Organic, specific, fractional. `47.2%`, `23k`, `+1 (312) 847-1928`, `$2,847.14`, `142 days`. If a number must be round in context (like a pricing tier), use realistic pricing patterns: `$29`, `$79`, `$249`.
- **Copy verbs**: Concrete action verbs. Replace "Elevate your workflow" with "Cut your weekly reporting from 4 hours to 20 minutes". Replace "Seamless integration" with "Push from Linear into Notion in one click". Replace "Unleash the power of AI" with "Ask it in plain English and get a cited answer".
- **Dates**: Randomize blog post publish dates across a 6-18 month range. Spread realistic cadence (not every post on a Tuesday).
- **Errors**: Plain language. "Connection failed. Please try again." "Payment declined. Check your card details." "File too large. Maximum is 25 MB." No exclamation marks, no personifying the app.

---

## Part 2: Banned LLM Output Patterns (Laziness Filler)

Every one of these is a partial output. A partial output is a broken output.

### Banned patterns (hard block, scan before emit)

Code:
- `// ...`
- `// rest of code`
- `// remaining code here`
- `// implement here`
- `// TODO`
- `// similar to above`
- `// continue pattern`
- `// omitted for brevity`
- `// (same as X)`
- `/* ... */` (without real content)

Prose:
- "for brevity"
- "the rest follows the same pattern"
- "similarly for the remaining"
- "and so on"
- "you can follow the same approach for..."
- "I'll leave that as an exercise"
- "shortened for clarity"
- "I'll skip the obvious ones"
- "you get the idea"
- "[etc.]" when the list was supposed to be complete

If any of these appear in the draft output, STOP. Return to the original request, count the actual deliverables, and produce every one.

### The Deliverable Count-Check

Before emitting any multi-part response:

1. **Parse the request**. Extract the exact number of deliverables the user asked for. Examples:
   - "Build 5 card components" → Y = 5
   - "Write emails for each of these 8 prospects" → Y = 8
   - "Refactor the checkout into service + repository + controller" → Y = 3
   - "Create the landing page" → Y = however many sections the landing page has (hero, features, pricing, FAQ, footer = 5, each must be full)

2. **Track X as you build**. Do NOT move to the next deliverable until the current one is complete.

3. **Before emit, re-read the request and confirm X == Y**. If X < Y, go back and finish the missing ones. Never submit X < Y with a filler note.

4. **Scan the full draft for banned patterns**. If any appear, remove and replace with real content.

---

## Part 3: Clean Breakpoint Pause Protocol

When a response genuinely cannot fit in a single output (large multi-file build, exhaustive audit):

### The protocol

1. **Track Y from the start**. Count total deliverables before you begin.

2. **Track X as you produce**. Keep a running count: "1 of 8 complete", "2 of 8 complete", etc. (internal; do not emit the running count unless asked).

3. **Stop at a clean boundary** as you approach the output limit. Clean boundaries:
   - End of a function (never mid-function)
   - End of a file (never mid-file)
   - End of a section (never mid-section)
   - End of a component (never mid-component)
   - Never mid-statement, mid-paragraph, mid-sentence.

4. **Emit the standardized pause line** as the final line:
   ```
   [PAUSED - X of Y complete. Send "continue" to resume from: <next section name>]
   ```

5. **On the user's next "continue" message**: resume exactly where you stopped. Pick up at `<next section name>` with NO recap, NO repetition, NO re-summarization, NO re-explaining what came before. Just continue producing.

### Example

```
...
export default CheckoutService;

[PAUSED - 3 of 6 complete. Send "continue" to resume from: CheckoutRepository]
```

Next turn (user: `continue`):

```typescript
// CheckoutRepository.ts
import { db } from './db';
...
```

No "Great, continuing from where we left off." No "As I mentioned, we're now building the repository layer." Just the code.

---

## Pre-Emission Checklist (MANDATORY)

Before emitting any substantial output, scan for:

| Check | Fail Condition |
|-------|----------------|
| Placeholder names | "John Doe", "Jane Smith", "Bob", generic "Alice and Bob" |
| Placeholder companies | "Acme", "Nexus", "SmartFlow", "TechPro", etc. |
| Cliche copy | "Elevate", "Seamless", "Unleash", "In today's fast-paced world" |
| Round stat numbers | "99.99%", "100%", "50%", "$100" as headline stat |
| Lorem Ipsum | Any dummy Latin text |
| Duplicate dates | All testimonials dated today, all posts from the same week |
| Exclamation error copy | "Oops!", "Uh oh!", any error with "!" |
| Laziness markers | `// ...`, `// rest of code`, `// TODO`, "for brevity", "and so on" |
| Incomplete deliverable | X < Y at emission time |
| Mid-function truncation | Output stops in the middle of a function/file/section |

Every failed check means rewrite that section before emitting.

---

## Composition With Other Skills

- **design-engineering** and **typography-craft** deliver polish and motion. This skill delivers hygiene. Run all three before emitting any UI work.
- **copywriting** and **copy-editing**: this skill is a post-draft gate. Copy goes through copywriting, then through this gate, then to delivery.
- **marketing-grader**: marketing-grader scores content against principles. This skill is a pre-grader filter so the grader is not scoring AI-slop.

---

## Provenance

- Leonxlnx taste-skill: https://github.com/Leonxlnx/taste-skill
- Leonxlnx output-skill: https://github.com/Leonxlnx/taste-skill/blob/main/skills/output-skill/SKILL.md
- Leonxlnx redesign-skill: https://github.com/Leonxlnx/taste-skill/blob/main/skills/redesign-skill/SKILL.md

Lessons baked into this skill:
- `leonxlnx-002` (Jane Doe Effect)
- `leonxlnx-011` (Banned LLM Output Patterns)
- `leonxlnx-012` (Clean Breakpoint Pause Protocol)

---

## Paul Bakaus AI Slop Test (added 2026-04-23)

Five human-validation steps from paul-bakaus-001, absorbed via Phase 3 absorption-search re-audit. This augments the automated-scan gates in Parts 1-3 with a cold-human-review loop.

## Part 4: The AI Slop Test (Human Validation Gate)

Before declaring any UI, page, or asset complete, run this single diagnostic:

> "If you showed this to someone cold and said 'AI made this,' would they believe you immediately?"

If the answer is yes, the output has failed. Proceed to Part 4 Steps 2–5.

### Step 1: Ship to working preview

Before the human check, render the output to its delivery form:
- UI component → browser render (not source)
- Landing page → staging URL or local server
- Email → rendered HTML in mail client
- Copy → formatted document, not raw markdown

The observer must see what the end-reader sees.

### Step 2–3: Cold human check

Show the rendered output to someone with no prior knowledge of the project. Do not describe it first, do not explain what it is trying to do.

Ask exactly: "Does this look AI-generated?"

Valid observers: a colleague not on the project, a friend, a fresh Claude session with no context. Not valid: the requester, a collaborator who reviewed earlier drafts.

### Step 4: Audit against known AI visual tells

When the observer says "yes, looks AI-generated," run a structural audit against this catalogue:

| AI Tell | Description |
|---------|-------------|
| Generic fonts | Inter/Roboto with no typographic intent; no size contrast between hierarchy levels |
| Purple gradients | Purple-to-blue or indigo hero backgrounds with white text |
| Gray text on color | Low-contrast body text on a colored background |
| Nested cards | Cards inside cards inside cards — three levels of border-radius |
| Hero-metric layout | Giant stat (e.g. "10,000+ users") centered in hero with no supporting evidence |
| Glowing dark mode | Dark background with neon-glow accents and no matte surfaces |
| Symmetrical grids | Every section centered, equal-width columns, no hierarchy through scale or asymmetry |
| Testimonials-as-cards | Three identical-width testimonial cards with headshot + name + star rating |

For each present tell, rewrite the offending element with a structurally different approach — not a reskin of the same pattern.

### Step 5: Loop until the exit criterion

Fix the identified tells (Step 4). Return to Step 1 (re-render). Run Step 2–3 again (cold show).

Exit when the observer's unprompted reaction is curiosity ("how was this made?") rather than recognition ("which AI made this?").

Do not exit because the banned-token list now passes. Exit because the human check passes.
