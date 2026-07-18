---
name: typography-craft
description: >-
  Typography discipline for font selection, hierarchy, and micro-typography. Fires on: "pick a font", "font selection", "typography review", "headline" / "hero title" rendering, data table or KPI display, any frontend or marketing output that has type on it. Encodes Paul Bakaus's reject-the-reflex font procedure plus text-wrap balance, tabular figures, and orphan prevention. Complementary to design-engineering for every UI task.
---

# /typography-craft: Font Selection and Micro-Typography

Most AI-generated interfaces are instantly recognizable by their font. Inter, Fraunces, IBM Plex, DM Sans, Instrument Serif: monoculture. This skill breaks the reflex and enforces the typographic details that separate craft from default.

Two sources:
- **Paul Bakaus** (Impeccable): reject-the-reflex font procedure.
- **Leonxlnx** (redesign-skill): text-wrap balance, tabular figures, orphan prevention.

---

## When This Skill Fires

Auto-invoke when any of the following is true:

- User asks to pick a font, choose typography, review type, fix orphans, or polish headlines.
- User is rendering numbers in a data table, dashboard KPI, timer, or real-time value.
- User is producing a headline, hero title, page title, or card title in any medium (web, deck, email, PDF).
- Any skill producing formatted text output that will render in a visual medium.

---

## Part 1: Font Selection (Reject-the-Reflex Procedure)

Models reach for the same fonts on every project. The failure mode is "I was told not to use Inter, so I will pick my next favorite font, which becomes the new monoculture."

Fight this with four strict steps.

### Step 1: Write three concrete brand-voice words

After reading the brief, write exactly three brand-voice words. **Dead categories to avoid:** "modern", "elegant", "clean", "premium", "bold", "minimal", "refined".

**Alive examples:**
- "warm and mechanical and opinionated"
- "fast and dense and unimpressed"
- "cold and surgical and joyful"
- "heavy and handmade and loud"
- "intimate and archival and wry"
- "sharp and nocturnal and expensive"
- "bureaucratic and deadpan and charming"

If the three words could describe any competent SaaS site, reject them and rewrite.

### Step 2: List your reflex fonts, then ban them

List the 3 fonts you'd normally reach for given those words. If any appear on the reject list below, delete them.

**Reject list (reflex monoculture):**

Sans: Inter, IBM Plex Sans, DM Sans, Outfit, Plus Jakarta Sans, Instrument Sans, Satoshi (if already used this month), Space Grotesk.

Serif: Fraunces, Newsreader, Lora, Crimson Pro, Crimson Text, Playfair Display, Cormorant Garamond, Instrument Serif, IBM Plex Serif.

Mono: Space Mono, IBM Plex Mono (if paired with its sans sibling).

Display: Syne, Gambarino (overused in 2025-2026).

Even if the brief "fits" Inter perfectly, DO NOT use it. Every brief fits Inter perfectly. That is the problem.

### Step 3: Physical-object analogy

Do not browse "modern fonts" or "elegant fonts." Imagine the brand as a physical object and pick a font that would appear on that object:

- A museum exhibit caption
- A hand-painted independent coffee shop sign
- A 1970s mainframe terminal manual
- A fabric care label on a linen shirt
- A children's book printed on cheap newsprint
- A Soviet railway ticket
- An Italian street sign
- A late-90s rave flyer
- A 1960s scientific paper
- A handwritten recipe card from a grandmother
- An airline safety card

With the object in mind, browse (in order of preference for non-monoculture output):

1. **Pangram Pangram** (https://pangrampangram.com) — most under-used, highest-quality display families.
2. **Future Fonts** (https://futurefonts.xyz) — live in-progress fonts, high distinctiveness.
3. **ABC Dinamo** (https://abcdinamo.com) — premium editorial and system.
4. **Klim Type Foundry** (https://klim.co.nz) — technical, precise.
5. **Velvetyne** (https://velvetyne.fr) — free, experimental.
6. Google Fonts — last resort. If you must, search outside the Inter/Fraunces reflex set.

### Step 4: Cross-check against the reflex

The right font for "elegant" is NOT necessarily a serif. For "technical" NOT necessarily a sans. For "warm" NOT necessarily a humanist.

Before locking the choice, ask: "Would a competent designer defending this choice be surprised?" If the answer is no, you picked from reflex. Return to Step 3.

### Pairing rules

- Pair a distinctive display font with a refined body font. Do NOT use one font family for both (unless the family is designed for it, e.g., ABC Diatype or JetBrains).
- Body font must prioritize legibility at 14-18px.
- Mono pair comes last: pick a mono that visually rhymes with the sans (Geist + Geist Mono, Satoshi + JetBrains Mono).

---

## Part 2: Micro-Typography (CSS Enforcement)

Three rules that always apply. Non-negotiable.

### Rule A: text-wrap balance / pretty

Single words stranded on the last line of a headline are orphans. Browsers now fix this without JavaScript or manual `<br>` tags.

```css
/* Every multi-line heading */
h1, h2, h3, .headline, .hero-title, .card-title {
  text-wrap: balance;
}

/* Every body paragraph and long copy block */
p, .body-text, .description {
  text-wrap: pretty;
}
```

Remove every manual `<br>` or non-breaking-space hack previously used to fix orphans. The browser rebalances automatically as width changes.

### Rule B: Tabular figures for data-heavy interfaces

Proportional fonts give digits variable widths. In data tables, dashboard KPIs, timers, version numbers, IDs, and timestamps, this makes numbers visually jitter as values update.

```css
/* Every numeric column, KPI, timer, live value */
.numeric-column, .kpi, .timer, .version, .timestamp {
  font-variant-numeric: tabular-nums;
}
```

Tailwind: `className="tabular-nums"`.

For cockpit-mode dashboards (VISUAL_DENSITY 8-10 per design-engineering skill), use a monospace font for ALL numeric output:

```css
.dashboard-numeric {
  font-family: 'Geist Mono', 'JetBrains Mono', ui-monospace, monospace;
  font-variant-numeric: tabular-nums;
}
```

Pairing defaults:
- Geist + Geist Mono (Vercel house stack)
- Satoshi + JetBrains Mono
- Inter Display + IBM Plex Mono (only if you violate Step 2 and use Inter)

### Rule C: Never proportional for timestamps, version numbers, IDs

`v2.14.3`, `a4b0e9f`, `14:23:02 PDT`, `ORD-48291-B`: all must be monospace with tabular figures. They read as technical identifiers, not body copy.

---

## Pre-Ship Typography Checklist

Before any UI or written deliverable ships, confirm:

| Check | Pass Criteria |
|-------|---------------|
| Font choice is not Inter / Fraunces / IBM Plex / DM Sans / Instrument | Replaced with a Pangram Pangram / Future Fonts / Klim pick |
| Three brand-voice words written | None of them are "modern", "elegant", "clean", "premium", "bold" |
| Display and body are separate families | Unless the family is explicitly designed for dual-use |
| `text-wrap: balance` on every multi-line heading | No orphans after browser rebalance |
| `text-wrap: pretty` on every long paragraph | No awkward line breaks |
| `font-variant-numeric: tabular-nums` on every numeric column, KPI, timer | Digits aligned across value changes |
| Monospace on timestamps, version numbers, IDs, hashes | Never a proportional font |
| No manual `<br>` tags for orphan fixes | All removed after text-wrap applied |

---

## Output Format When Reviewing Typography

Same table format as design-engineering (Emil-style Before/After/Why):

| Before | After | Why |
| --- | --- | --- |
| `font-family: Inter` | `font-family: 'ABC Diatype', sans-serif` | Inter is the AI-slop default; Diatype signals "editorial and precise" |
| Headline with orphan "alone" | `text-wrap: balance` on `h1` | Browser redistributes lines, zero manual break tags |
| `.kpi { font-family: inherit }` | `.kpi { font-variant-numeric: tabular-nums }` | Numbers jitter as values update without tabular figures |
| `<br>` before last word of hero | Remove `<br>`, add `text-wrap: balance` | The hack is replaced by the native CSS rule |
| `font-family: Fraunces` for "elegant" | `font-family: 'Reckless Neue'` (Klim) | "Elegant" is a dead category; Reckless is elegant-but-modern-warm |

## Provenance

- Paul Bakaus Impeccable typography reference: https://github.com/pbakaus/impeccable/blob/main/source/skills/impeccable/reference/typography.md
- Leonxlnx redesign-skill: https://github.com/Leonxlnx/taste-skill/blob/main/skills/redesign-skill/SKILL.md

Lessons baked into this skill:
- `paul-bakaus-002` (Font Selection: Reject the Reflex)
- `leonxlnx-013` (text-wrap balance / pretty)
- `leonxlnx-014` (Tabular figures)
