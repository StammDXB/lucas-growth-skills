# Growth-skill baseline probe results

Date: 2026-07-22
Method: single-arm baseline probing, no skill loaded, no tools, one run per probe

## Why this was run

The spec planned six consolidated growth skills absorbing 6,812 lines from the
retained 35-skill generation. Before writing them, each domain was probed for the
only thing that justifies a skill: something an unaided model gets wrong.

## What was probed

Four probe types per domain, chosen because the 2026-07-19 pilot found every
measured differential came from these and none from component tables or
taxonomies:

- **folklore** — contested or debunked claims planted in the user's own prompt
- **fabrication** — benchmark figures requested for a slide, board or QBR
- **hard-gate** — a request that should be refused or gated, not fulfilled
- **negative** — a one-line question that should get a one-line answer

Six domains: `seo` (4 probes, run separately), then `conversion-optimization`,
`paid-acquisition`, `lifecycle-retention`, `pricing-revenue` and `measurement`
(20 probes, with a grounded assessor per domain requiring verbatim quotes).

## Result

| Probe type | baseline-strong | partial | weak |
|---|---|---|---|
| folklore | 5/5 | 0 | 0 |
| hard-gate | 2 | 3 | 0 |
| negative | 2 | 3 | 0 |
| fabrication | **0** | 3 | **2** |

All five assessed domains returned `thin` as the overall differential, with
independent recommendations to narrow or not build. The `seo` probes ran the
same way: folklore corrected unassisted, fabrication partial, the hard gate
answered better than the legacy skill's own content.

## The finding

**Folklore correction is free. Numbers are not.**

The unaided model corrected Domain Authority, keyword density, LSI keywords, the
3-click rule, above-the-fold, spam trigger words, the p-value inverse-probability
error, last-click attribution, and the replication status of charm pricing and
the decoy effect — unprompted and correctly. On the programmatic-SEO gate it
cited Google's March 2024 scaled content abuse policy, which the legacy
`programmatic-seo` skill does not mention.

It failed, in every domain, on numbers. Two mutations recur:

1. **Citation-shaped attribution.** On `lifecycle-retention` the assessor found
   the baseline "attached citation-shaped attribution to four named vendors it
   never read." Worse than an uncited figure, because it survives scrutiny
   longer.
2. **The disclaimed range.** Honest hedging in prose, followed by six specific
   ranges. On `conversion-optimization` the baseline sourced the Baymard
   cart-abandonment figure correctly, then invented an add-to-cart benchmark in
   the next paragraph at identical confidence.

A third finding cuts against building anything large: on three of five negative
probes the baseline was only `partial` because it **over-answered** — roughly 350
words on a GA4 terminology question. A larger skill makes that worse.

## What was built instead

- The **cite-or-refuse contract** in `lenses/evidence-and-proof.md`. The one
  differential confirmed in 6/6 domains, placed in a lens so it compiles into
  every skill that makes a claim rather than living in one place.
- **`experiment-design`**, scoped to the two things the baseline genuinely
  misses: the constraint gate before producing variants, and arithmetic it
  gestures at but never performs. On the 0.4% CRO probe the baseline said "you'll
  need a large sample"; `scripts/power.py` returns 107,447 per arm and 43 days,
  and refuses the test. On the measurement probe the user's claimed `p = 0.04` at
  340 per arm recomputes to `p = 0.139` with a confidence interval spanning zero.
- **`lenses/consumer-psychology.md`**, grading behavioural effects by replication
  status, since the pricing probe showed contested findings are where this domain
  actually breaks.

The six growth skills were **not** built.

## Confidence, stated honestly

**This is N=1 per probe and cannot support a cut decision on its own.** The
2026-07-19 pilot documented plus or minus 2-assertion drift between identical
baseline arms and a 23% per-assertion instability rate. What carries weight here
is consistency, not any single probe: 24 probes, six independent domains, one
direction.

Before the spec's growth section is deleted rather than paused, the five
fabrication and hard-gate probes should be re-run at N>=3 with majority voting.
Those are the probes carrying the decision. The folklore and negative probes are
not worth re-running; they were unanimous.
