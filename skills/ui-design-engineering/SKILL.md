---
name: ui-design-engineering
description: >-
  Design and build interface details that make software feel considered:
  animation decisions, component craft, transforms, gestures, motion
  performance, and visual direction. Use when the user is building or reviewing
  UI, wants something animated, asks why an interaction feels wrong or cheap,
  wants a component to feel polished, or says things like "make this feel
  better", "should this be animated", "review this UI", "add a transition",
  "this feels janky", or "make it look high-end". Covers React, CSS, and
  framework-agnostic motion. Not for information architecture or user research.
license: MIT
metadata:
  version: "1.0"
---

# UI Design Engineering

Most of what makes an interface feel good is invisible. Users do not notice the
details individually; they notice the aggregate and call it quality.

> "All those unseen details combine to produce something that's just stunning,
> like a thousand barely audible voices all singing in tune." — Paul Graham

Craft encoded largely from Emil Kowalski's work on UI animation and component
design.

## Three ideas the rest follows from

**Taste is trained, not innate.** It is the ability to see beyond the obvious and
recognise what elevates. You build it by studying great work, reverse-engineering
animations, and asking why something feels good.

**Unseen details compound.** When a feature behaves exactly as someone assumes it
should, they proceed without a second thought. That is the goal, not applause.

**Beauty is leverage.** People choose tools on overall experience, not just
function. Good defaults and good motion are real differentiators, and they remain
underused.

## Step 1: Clarify before building

Ask if these are not clear. Building the wrong interaction well is worse than
building the right one plainly.

1. **What is the user trying to do**, and what is the state before and after?
2. **What platform and stack**, and what is already in use for motion?
3. **Is this net-new or a fix?** If a fix, what specifically feels wrong?
4. **Any existing design system**, tokens, or motion conventions to obey?

If the user says "make it feel better" with no specifics, ask what feels wrong.
The answer is usually one thing, not everything.

## Step 2: Decide whether to animate at all

This is the highest-leverage decision, and the default answer is more often "no"
than people expect.

Animate when motion **explains** something: where an element came from, what
changed, what is now interactive, that a system is working. Do not animate to
decorate, and do not animate anything the user triggers dozens of times a
session unless it is very fast.

Load `references/animation.md` for the full decision framework, spring
configuration, staggering, and how to debug motion that feels wrong.

## Step 3: Route by task

| Task | Load |
|---|---|
| Any transition, spring, stagger, or "should this animate" | `references/animation.md` |
| Building or reviewing a component, especially reusable | `references/components.md` |
| Transforms, clip-path animation, gestures, drag | `references/css-technique.md` |
| Frame rate, jank, reduced motion, keyboard, screen readers | `references/performance-and-a11y.md` |
| Committing to a visual direction | `references/visual-styles.md` |

`performance-and-a11y.md` is a gate, not a polish pass. Read it on any UI work,
not only when something is slow.

## Step 4: Commit to a visual direction

If the work needs an aesthetic and none is defined, pick a mode from
`references/visual-styles.md` and commit to it. The two modes there are opposed
on purpose.

**Hedging between them produces the generic middle**, which is the single most
common reason work reads as unfinished. "Modern but warm, minimal but rich" is
two directions pretending to be one.

## Step 5: Validate

Load `references/rubric-ui-design-engineering.md`. Score every line PASS or FAIL
with quoted evidence. Burden of proof on PASS. Fix, re-score, **maximum two
rounds**. State anything still failing.

Self-check against a written standard, not independent review.

## Step 6: Deliver

For **new work**: the implementation, then

```
Decisions   what you animated and what you deliberately did not, and why
Open        anything needing a design token, an asset, or a product call
```

For **a review**: lead with the single highest-impact issue, then the rest in
priority order. Each item names the specific problem, why it matters, and the
fix. "This feels off" is not a review finding.

Never show the rubric scoring or the revision rounds.

## Gotchas

- **Animating because you can.** Motion that explains earns its place. Motion
  that decorates costs frame budget and patience.
- **Animating high-frequency actions.** Anything triggered dozens of times per
  session must be near-instant or absent.
- **Easing chosen by name, not by feel.** Defaults exist to be replaced.
- **Animating layout properties.** Transform and opacity are cheap; width,
  height, top and left are not.
- **Ignoring reduced motion.** A preference, not an edge case.
- **The generic middle.** Two visual directions hedged into one.
- **Reviewing with adjectives.** "Clean", "modern", "polished" are not findings.
  Name the element, the problem, and the fix.
