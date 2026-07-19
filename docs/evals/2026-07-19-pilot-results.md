# Eval pilot results

Date: 2026-07-19
Harness: with/without baseline comparison, blind grading, majority vote

## What was measured

Three skills of ten. `copywriting`, `ui-design-engineering`, and
`marketing-architecture-audit`. The other seven have authored suites and **no
evidence in either direction**.

Each case ran twice: a baseline arm (no skill, no tools, answer directly) and a
skill arm (reads SKILL.md and any references it directs). A third agent graded
both blind, per assertion, with a verbatim quote required for every verdict,
then gave a holistic preference. Arm order alternated so grader position bias
cancels.

## The methodology finding, which outranks the results

**Single-run evals cannot support a cut decision.** Running the identical
baseline arm twice, same prompts, nothing changed, drifted on **10 of 24
cases**, +/-2 assertions per case, 13 assertion-points total. At N=3 the
per-assertion instability rate was **23%**: nearly a quarter of graded
assertions flipped verdict between replicates.

Consequences:
- Treat any aggregate delta under ~3 assertion-points as noise.
- A result is attributable only when a specific change has a causal path to
  the specific case that moved.
- The holistic preference metric is more stable than assertion counts and
  should carry more weight in a cut decision.

This was not theoretical. A content fix was drafted against a run-1 reading
("copywriting over-interrogates") and withdrawn when run 2 contradicted it.

## Results

### copywriting, N=3 majority vote

| | |
|---|---|
| Majority assertions | 30/32 skill vs 27/32 baseline |
| Case record | 2W 0L 6T |
| Holistic preference | skill 21, baseline 3 (of 24 gradings) |
| Instability | 15/64 assertions (23%) |

Beats baseline. Loses no case.

Where the skill wins: email compliance as a copy decision (4/4 vs 2/4, baseline
drops the unsubscribe and fabricates offer terms), diagnosis over rewriting
(4/4 vs 3/4), folklore correction.

**The skill fabricates nothing, anywhere.** Baseline invents statistics in case
1 and a founding story in case 6. This is the single clearest differential in
the pilot and it is an integrity property, not a style preference.

Two open defects, both from the draft-first change:
- case 1: asks its follow-up question in only 1 of 3 runs
- case 7: ships the requested deliverable in 0 of 3 runs (baseline also 0/3)

A repair is committed but **unverified**.

### ui-design-engineering, N=1 (noise-limited)

31/34 vs 27/34, 4W 0L 4T, preference 6-1. Directionally the cleanest skill in
the pack: no lenses, no delivery ceremony, and the only pilot skill to pass its
negative case clean on the first run. Needs N=3 to confirm.

### marketing-architecture-audit, N=1 (noise-limited)

31/33 vs 18/33, 6W 1L 1T, preference 7-1. The largest raw gap in the pilot,
driven by refusing to produce redundancy verdicts from thin information.
Needs N=3 to confirm.

## Structural findings that need no eval

1. **13 bundled reference files ship with no load-trigger**, 72KB across 8
   skills. `build.py` checked only that referenced files exist, never that
   bundled files are referenced. `validate_no_orphans` now warns. The fix is a
   content decision: give each file a load-trigger, or stop declaring it.

2. **`stakeholder-response` contradicted itself.** STEP 5 said "no strategic
   note" while DELIVERY NOTE mandated one and rubric D1 failed its absence.
   Fixed, including the rubric, so the contradiction does not relocate.

3. **The house standard had no proportionality escape hatch.** Both skills that
   failed their negative case did so by firing a full clarify sequence and
   delivery note at a one-line question. Fixed across all 10 skills.

4. **Descriptions are genuinely distinct.** Zero shared quoted trigger phrases,
   max pairwise vocabulary overlap 10%.

## What the authoring agents found, unprompted

Every suite author was asked where they could *not* find a differential. Nine
independent answers converged:

**Load-bearing:** hard gates and refusals, do-not-cite lists, named countable
procedures, domain compliance knowledge, no-fabrication rules.

**Not load-bearing:** component tables, taxonomies, delivery-format templates,
and "score against the rubric" steps. Several noted the rubric self-check is
*structurally unobservable*, since the skills instruct that the scoring never
be shown, so no blind grader can detect whether it ran.

This is a testable hypothesis about the whole pack, not just the three
measured skills, and it predicts where the remaining seven will be weak.

## Cheaper path for the remaining seven

Running all seven at N=3 across 8 cases each is ~510 agents. The pilot suggests
most of that spend buys nothing, because the ties cluster in predictable places.

Recommended instead: run only the **hard-gate, folklore, fabrication, and
negative** cases per skill, which is where every measured differential
actually came from, at N=2. That is roughly 3-4 cases per skill instead of 8,
about 160 agents total for all seven, and it targets the exact claim each skill
makes about why it exists. Escalate to full N=3 only for skills that land near
the boundary.
