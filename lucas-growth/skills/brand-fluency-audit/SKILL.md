---
name: brand-fluency-audit
description: >-
  Audit any brand asset (logo, headline, hero image, tagline, landing page) on
  processing fluency — how fast a target consumer decodes the meaning. Low
  fluency compounds across assets and costs measurable brand equity via lost
  perceived authenticity. Uses 5-second test methodology with 5-outsider panel.
  Use for "fluency audit", "decode time", "5-second test", "brand asset audit",
  "is this headline clear enough", "why does this logo feel off".
---

# Skill: brand-fluency-audit

**One responsibility:** Score one or more brand assets on processing fluency using decode-time measurement and the 5-second / 5-outsider test, then recommend redesign or accept based on the evidence threshold.

**This skill does NOT:** design new assets (that is `brand-identity` or `copywriting`), define brand strategy, or audit brand compliance against an existing system (that is `brand-compliance`).

---

## Step 1: Resolve Brand Context + Load Foundation (MANDATORY — Never Skip)

1. **Determine brand context:**
   - If the audit brief names a client → set `brand_context` = client name
   - If already operating in a client folder → set `brand_context` = that client
   - If neither → set `brand_context` = the primary brand of the current project
   - If ambiguous → ask using AskUserQuestion: "Whose asset is this?"

2. **Resolve foundation path:**
   - Locate the project's brand foundation directory (brand guidelines, positioning,
     audience, tone-of-voice docs). Common locations: `brand/`, `_foundation/`,
     `docs/brand/`. Ask the user if none is discoverable.

3. **Load foundation files:**
   For each `.md` file in the resolved path:
   a. Read ONLY the content above the first `---` separator (the routing header)
   b. Check the "Load this file when:" line against this audit task
   c. Load the FULL file ONLY if the criteria match
   d. Skip all files where the criteria do not match

Files most likely to match for a brand fluency audit:
- Brand identity / brand system — current archetype and personality, to calibrate what "clear" means for this brand
- Audience — who the 5-outsider panel should approximate
- Positioning — what the brand claims, so the audit tests "does the asset decode to the correct position?"

The intelligence lives in the foundation files, not in this skill. Never hardcode brand or audience assumptions here.

---

## Step 2: Load Asset Under Audit

1. Read the asset(s) under audit — file path, URL, or inline image.
2. Confirm the brand is not already famous enough to supply fluency from memory (aided recall above 60% in the target segment per foundation context). If it is, recommend skipping the audit and stop.

---

## Step 3: Decode-Time Measurement

For each asset:
1. Present it to yourself cold (no context).
2. Measure the seconds until the meaning is clear — what does this brand do, or what is this headline claiming.
3. Record the decode time and the first-guess meaning.

Thresholds:
- Decode time <= 2 seconds: high fluency — proceed to Step 4 for consumer validation only if high-stakes.
- Decode time 2-5 seconds: medium fluency — mandatory Step 4 validation.
- Decode time > 5 seconds OR requires prior context: low fluency — skip to Step 5 recommendation.

---

## Step 4: 5-Second / 5-Outsider Test

Show the asset to five people outside the company for exactly 5 seconds, then ask: "What does this brand do?" or "What is this headline claiming?"

Pass criteria:
- >= 4 of 5 correctly identify the meaning: PASS — asset has sufficient fluency.
- 2-3 of 5 correct: BORDERLINE — recommend redesign unless famous-brand exception applies.
- <= 1 of 5 correct: FAIL — redesign required.

Record each respondent's answer verbatim for the report.

---

## Step 5: Recommendation

Write the audit report to the project's audits folder under the resolved brand context with:

```
## Brand Fluency Audit — {asset-name}
- Asset type: {logo | headline | hero image | tagline | other}
- Decode time (cold read): {X} seconds
- 5-outsider test results: {N}/5 correct
- Verdict: {PASS | BORDERLINE | FAIL}
- Recommendation: {accept | redesign with explicit meaning on first viewing | validate with wider panel}
- Evidence: Luffarelli, Mukesh & Mahmood (2019), JMR 56(5), 862-878
- Source lesson: jonathan-luffarelli-003
```

---

## Step 6: Redesign Brief (if FAIL or BORDERLINE)

Generate a redesign brief for the designer or copywriter. The brief must specify:
- The target decode time (<= 2 seconds).
- The literal signal that should be explicit on first viewing (what the brand does, or what the headline is claiming).
- The banned patterns: clever abstractions that require prior context, puns that depend on category knowledge, visual metaphors requiring two-step interpretation.
- The fame-exception override clause: only accept a low-fluency redesign if the brand reaches >60% aided recall in the audience foundation context.

---

## Step 7: Composition with brand-identity

If the audited asset is a logo and the verdict is FAIL, recommend running `/brand-identity` Section 3d (Logo Descriptiveness Gate) to establish whether the verdict should be DESCRIPTIVE, ABSTRACT, or EITHER before commissioning a redesign. The fluency audit diagnoses the problem; brand-identity §3d prescribes the verdict.

---

## Mechanism cited

Luffarelli, Mukesh & Mahmood (2019), *Journal of Marketing Research* 56(5), 862-878. Descriptive logos scored 6.24 on authenticity versus 4.55 for non-descriptive logos on a 7-point scale. The mechanism is a two-step cognitive chain: easier-to-process stimuli feel more authentic, and authenticity drives brand equity. The mechanism generalizes beyond logos — any brand asset that is easier to decode borrows the same authenticity lift.
