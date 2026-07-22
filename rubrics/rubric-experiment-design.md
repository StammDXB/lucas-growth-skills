# Rubric: Experiment Design

Score every line PASS or FAIL. No partial credit. Quote evidence from the draft.
Burden of proof is on PASS.

## A. The gate

**A1. Variants were not produced before the constraint was located.**
If the user asked for copy, colours, layouts or timers on a surface converting
below roughly 1%, the draft withholds them and asks for source-level conversion,
step-level drop-off, and volume. FAIL if variants appear anywhere in the output,
including as an appendix, a "here's what you asked for anyway", or a sample.

**A2. The gate was resolved, not merely mentioned.**
Naming the concern and then complying is the documented baseline failure. FAIL if
the draft flags that the constraint is probably upstream and delivers the
requested artifact regardless.

**A3. The missing inputs are named as specific pulls.**
"Send me your analytics" fails. "GA4 funnel exploration, split by session source"
passes. FAIL on any request the user could not execute the same day.

**A4. Proportionality was respected.**
A one-line question received a one-line answer with no gate, no script, no
rubric, no delivery block. FAIL on ceremony fired at a small ask.

## B. The arithmetic

**B1. Sample size came from the script, not from prose.**
FAIL on any estimated sample size, duration, or "you'll need a lot of traffic"
without `scripts/power.py` output behind it.

**B1a. The arithmetic was delivered with the gate, not after it.**
Where a conversion rate was stated, the same reply carries the computed sample
size and duration. FAIL on any promise to calculate once the other inputs arrive:
the rate alone is sufficient, and a refusal without a number reads as obstruction
rather than as the argument it is.

**B2. The MDE was set by a business question.**
The draft asked, or states, what lift would change the decision. FAIL on an MDE
picked because it produces a convenient sample size.

**B3. An unrunnable test was called unrunnable.**
Where the script refuses, the draft delivers that refusal and its alternatives.
FAIL if an impossible test is designed anyway with a caveat attached.

**B4. A reported result was recomputed, not repeated.**
Where the user quoted a lift or a p-value, the draft evaluated it independently.
FAIL if the user's figure is accepted at face value.

## C. Interpretation

**C1. The confidence interval is reported, not only the p-value.**
FAIL if a decision rests on p alone, and especially if an interval containing
zero is described as a win.

**C2. Early stopping is identified where it occurred.**
FAIL if a test below its required sample is discussed as if the p-value were
valid.

**C3. p is described correctly.**
Not "the probability the variant is better". FAIL on any restatement of the
inverse-probability error, including one carried over uncorrected from the user.

**C4. The three non-statistical checks were raised before rollout.**
Whole weeks, no mid-test changes, effect holds in the second half. FAIL if a
rollout is endorsed without them.

## D. Evidence and routing

**D1. Every figure carries source, year, and population, or was refused.**
Includes figures the model felt confident about and figures the user
pre-authorised as placeholders. One uncited benchmark fails the deliverable.

**D2. No citation-shaped attribution.**
A vendor name attached to a number that was not read is worse than no citation.
FAIL on any.

**D3. Work belonging to another skill was routed, not performed.**
If the real problem is the offer, the copy, the interface, or the brief, the
draft names the destination and stops. FAIL if it silently does that work here.

## Scoring

Fix all FAILs, re-score. Maximum two rounds. Report anything still failing
plainly.
