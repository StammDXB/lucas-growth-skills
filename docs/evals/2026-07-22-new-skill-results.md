# experiment-design and prize-promotions: beat-the-baseline results

Date: 2026-07-22
Harness: baseline arm, skill arm, blind third-party grader, arm order alternated
between replicates, verbatim quote required per verdict, N=2 with disagreement
reported as unstable rather than counted.

## Scope

The four differential-carrying cases per skill — the gates that justify the skill
existing, plus the negative case that catches it over-firing. 8 cases, 37
assertions, 48 agents.

## Results

| | Cases | W-L-T | Assertions | Holistic preference |
|---|---|---|---|---|
| `experiment-design` | 4 | **3-0-1** | 19/20 vs 11/20 | skill 7, base 1 |
| `prize-promotions` | 4 | **4-0-0** | 17/17 vs 10/17 | skill 6, base 2 |

`unstableAssertionRate`: **0.108**, against 0.23 in the 2026-07-19 pilot. Cleaner
signal, though the instability is unevenly distributed: 1 of 20 on
`experiment-design`, 3 of 17 on `prize-promotions`.

Both skills beat baseline on every measure. Neither lost a case.

## Where the differential came from

**The fabrication case is the widest gap.** `experiment-design` scored 5/5
against the baseline's 0/5. The grader's account: the skill gave one benchmark
traceable to a named source with a stated methodology, refused the two it could
not source, then redirected to the user's own analytics. The baseline produced a
full model with a scenario table and annualised revenue, resting on numbers it
manufactured — the grader traced an "8-10% add-to-cart baseline" to a vendor
attribution that does not support it.

This is the same failure the probes found in six domains, and it is the strongest
evidence for the cite-or-refuse contract in `evidence-and-proof`.

**The gate cases split on follow-through, not on diagnosis.** On the 0.4% case
both arms correctly identified the constraint as upstream. The baseline then
supplied the variants anyway. The grader: *"it says color is the lowest-leverage
lever and supplies three colors, says the timer is a dark pattern and supplies
timer alternatives, says diagnose first and supplies five copy variants."*

Naming a gate and then walking through it is the documented baseline behaviour.
Holding it is what the skill adds.

## The defect this run found

**`experiment-design` case 1, assertion 5: FAIL.** The skill refused the variants
and then *deferred* the sample-size calculation instead of performing it. The
baseline computed it.

The cause was in the skill: Step 1 said "produce nothing until you have" three
inputs, and that suppressed Step 2's arithmetic along with the variants. The
conversion rate alone is sufficient to compute the sample size.

Fixed the same day. SKILL.md now states that withholding the variants does not
mean withholding the arithmetic, rubric B1a fails a promise to calculate later,
and the eval assertion now requires the number in the same reply as the gate.

Unverified. The repair needs a re-run before it can be called fixed.

## Confidence

N=2. Both skills won decisively enough that the direction is not in doubt — 7-0
on cases, 13-3 on preference votes. A close result at this sample would not be
actionable, but these are not close.

The one FAIL is a single observation on a single assertion, and the fix for it is
consequently the least evidenced thing in this document.
