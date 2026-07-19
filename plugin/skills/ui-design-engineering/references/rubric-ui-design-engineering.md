# Rubric: UI Design Engineering

Score every line PASS or FAIL. No partial credit. Quote evidence. Burden of
proof is on PASS.

## A. Decision quality

**A1. The decision to animate was made, not assumed.**
For each animation, state what it explains. Motion that only decorates is a FAIL.

**A2. High-frequency interactions are fast or unanimated.**
Anything a user triggers dozens of times per session must be near-instant. FAIL
on a 300ms flourish on a repeated action.

**A3. The before and after states are named.**
FAIL if the transition was built without stating what changed.

## B. Implementation

**B1. Only cheap properties are animated.**
Transform and opacity pass. Width, height, top, left, margin are a FAIL unless
justified with a stated reason.

**B2. Easing or spring values were chosen, not defaulted.**
FAIL on a bare framework default with no reasoning.

**B3. One motion idea per interaction.**
Stacked simultaneous animations on a single element are a FAIL.

**B4. Interruption is handled.**
What happens if the user acts mid-animation. FAIL if the animation blocks input
or cannot be reversed.

## C. Gates

**C1. Reduced motion is respected.**
`prefers-reduced-motion` handled. This is a preference, not an edge case. FAIL if
absent.

**C2. Keyboard operable.**
Every interactive element reachable and operable without a pointer.

**C3. Focus is visible and managed.**
FAIL on removed focus rings, or focus lost after a state change.

**C4. No frame-rate hazard.**
No layout thrash, no animating during scroll without need, no unbounded
simultaneous animations.

## D. Direction

**D1. A visual direction is committed to.**
FAIL on the hedged middle. "Minimal but rich" is two directions pretending to be
one.

**D2. Existing system conventions are obeyed.**
If tokens, spacing scale, or motion conventions exist, the work uses them. FAIL
on inventing a parallel system.

## E. Review output, when reviewing

**E1. Findings are specific.**
Each names the element, the problem, and the fix. "Feels off", "needs polish",
"looks dated" are a FAIL.

**E2. Ordered by impact.**
The highest-impact issue leads. FAIL on an undifferentiated list.

**E3. Says what to leave alone.**
A review that finds everything wrong is a rewrite in disguise. FAIL if nothing
is affirmed.

## Scoring

Fix all FAILs, re-score. Maximum two rounds. Report anything still failing
plainly.
