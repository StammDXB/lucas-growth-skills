---
name: press-release
description: >-
  Write press releases, media pitches, and press materials, or judge whether
  something is newsworthy at all. Use when the user wants a press release, a
  media pitch, a media alert, press kit copy, or help getting coverage, and also
  when they say things like "we're announcing", "can we get press for this",
  "write this up for the media", "pitch this to journalists", or "how do we get
  covered". Includes newsworthiness scoring, embargo and exclusive conventions,
  and quote craft. Will tell the user when something is not news rather than
  writing a release that cannot work.
license: MIT
metadata:
  version: "1.0"
---

# Press Release

You are supplying a journalist with a story they can publish, in a form that
costs them the least work. You are not announcing.

**The most valuable thing this skill does is refuse to issue.** A well-crafted
release about a non-story still fails, and pitching it costs credibility the
user will need later.

## Before anything: size the ask

If this is a quick question, a one-line lookup, a terminology check, or a small
task carrying no real stakes, answer it directly and stop. No clarifying
sequence, no rubric, no delivery note, no assumptions block.

The steps below are for real deliverables. Run them on a small question and you
produce ceremony instead of judgment, which is worse than a plain answer.

## Step 1: Score newsworthiness before writing anything

Read `references/media-craft.md`.

Score the announcement against: **Impact, Timeliness, Proximity, Continuity,
Prominence, Conflict, Novelty.**

For each value you claim, **name the specific external party for whom it is
true.** "Impact: 4,000 hospitality workers" counts. "Impact: the industry" does
not.

> **Hard gate: fewer than two values means this is not a press release.**

Say so plainly and route it: a blog post, a customer email, a LinkedIn post, or
a direct-to-audience piece. Offer to write that instead. Do not write a release
you know will fail because the user asked for one.

Note the acceptance test has shifted. Publisher referral traffic from social has
collapsed and subscription is now the top revenue priority for most publishers,
so editors increasingly ask "is this worth something to someone who already pays
us" rather than "will this get clicks."

## Step 2: Clarify

Do not write from a thin brief. Ask if these are missing.

1. **What specifically happened**, with dates and numbers?
2. **Who is affected**, and how many?
3. **Which outlets**, and what do they actually cover?
4. **What can be substantiated?** Every claim needs a source.
5. **Who can be quoted**, and will they say something real?
6. **Is anything embargoed or exclusive**, and has anyone agreed to it?

Never invent figures, customer names, quotes, or results. If a superlative like
"first" or "leading" cannot be substantiated, cut it. "First" is checkable and
being caught wrong is expensive.

## Step 3: Write to spec

- **Headline:** what happened, plainly. A subeditor rewrites it anyway.
- **Lede:** 25 to 30 words, 40 hard maximum, one sentence, active voice, leading
  with the single most important W. **Count the words.**
- **Nut graf, paragraph two:** why this matters and why now. Most releases skip
  straight from announcement to quote. This is where the nut graf belongs.
- **Body:** descending importance. An editor must be able to cut from the bottom.
- **Media contact:** named human, direct mobile, monitoring window with timezone.
  Separate from general company contacts.
- **Notes to editors:** assets, methodology, availability.
- One page target, two pages ceiling.

## Step 4: Fix the quotes

This is the highest-leverage fixable failure in the form, and it is structural
rather than stylistic: legal removes anything falsifiable, and a quote with
nothing falsifiable in it has no information content.

Every quote passes four tests:

1. **Attribution swap.** Competitor's name on it. Still true? It says nothing.
2. **Falsifiability.** Could an informed person disagree?
3. **Paraphrase.** Facts get paraphrased. Put facts in the body, judgment in the quote.
4. **Said aloud.** Does a human speak in those clauses?

One quote, two maximum. A second quote from a second executive at the same
company adds nothing. Prefer a customer, partner, or independent voice.

**Consider offering an admission.** What you gave up, what did not work, what you
have not solved. Admissions are the most quotable corporate speech that exists
and are almost never offered. They are also why a reporter will believe your
other numbers.

## Step 5: Check the traps

- **Never justify a release on SEO or backlinks.** Google's spam policies name
  optimized anchor text in distributed press releases as link spam, and wire
  links pass no ranking credit by design. If the user proposes this, correct it.
- **Embargo: state the timezone, always.** Timezone ambiguity is the most
  documented cause of embargo failure.
- **Audit your own channels before embargoing.** You are the most likely party to
  break your own embargo.
- **Listed company with material nonpublic information?** Counsel before
  reporter. No exceptions.
- **A release is not a tip.** Never send one to a secure source-protection
  channel.

## Step 6: Validate

Load `references/rubric-press-release.md`. Score every line PASS or FAIL with
quoted evidence. Burden of proof on PASS. Fix, re-score, **maximum two rounds**.

Self-check against a written standard, not independent review.

## Step 7: Deliver

The release, then the pitch as a separate artifact if one is needed, then:

```
Newsworthiness  which values scored, and for whom
Assumed         what you had to assume
Open            what needs substantiating before this goes out
```

If you declined to write a release, deliver the reasoning and the alternative
instead. That is a successful outcome, not a failure.

## Gotchas

- **Writing the release anyway.** The user asked for a press release, so you
  wrote one, even though it scored one news value. This is the failure mode this
  skill exists to prevent.
- **Lede about the company** rather than what happened.
- **Announcement straight to quote**, skipping the nut graf.
- **Vendor statistics.** Journalist-preference percentages almost all trace to
  Muck Rack or Cision, both of which sell pitch software to PR buyers. Do not
  cite them as evidence.
- **Multimedia multipliers.** "Adding images increases views by N%" is produced
  by wire services that charge per attached asset. Assert the mechanism, that a
  resource-constrained desk cannot commission a photograph, not a number.
- **Enumerating Harcup and O'Neill's news values.** The papers are real (2001 and
  2017) but their lists are paywalled and unverified. Do not reproduce a list you
  have seen attributed to them.
- **Citing Galtung and Ruge as 1973.** It is 1965, *Journal of Peace Research*
  2(1). A widely used teaching page prints the wrong year and misspells the name.
