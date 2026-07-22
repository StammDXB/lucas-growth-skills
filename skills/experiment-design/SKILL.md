---
name: experiment-design
description: >-
  Decide whether a marketing test is worth running, whether a result can be
  trusted, and where the real constraint is before optimising anything. Use when
  the user wants to A/B test something, asks whether a result is significant or
  ready to call, wants to improve a page, funnel, signup flow or campaign that is
  underperforming, or says things like "variant B is winning", "is this
  statistically significant", "should we ship it", "how long should we run this",
  "our page converts at 0.4%", or asks for copy and design variants to test.
  Computes required sample size, test duration, and whether an observed result
  survives scrutiny, rather than estimating any of them.
license: MIT
compatibility: Requires Python 3.8+ to run scripts/power.py. No packages, no network.
metadata:
  version: "1.0"
---

# Experiment Design

Most marketing tests cannot answer the question they were built to answer, and
the reason is arithmetic that nobody did. This skill does the arithmetic first.

**The two failures this exists to prevent:** optimising a surface that is not the
constraint, and calling a result that a fixed-sample calculation would have
refused.

## Before anything: size the ask

If this is a quick question, a definition, a terminology check, or a small task
with no real stakes, answer it directly and stop. No gate, no script, no rubric,
no delivery block.

A one-line question about what a p-value is gets a one-line answer. Running the
steps below on it produces ceremony instead of judgement.

## Step 1: Locate the constraint before producing anything

When the user asks for variants — copy, colours, layouts, timers — on a surface
that is converting badly, **do not produce them yet.**

Every funnel has exactly one binding constraint, and work anywhere else changes
nothing. Read `references/consumer-psychology.md` for why this is the most
violated idea in marketing execution.

> **Hard gate.** Below roughly 1% on a signup, trial, or checkout page, the
> constraint is almost never button copy. It is traffic intent, offer, price, or
> a broken step. Produce nothing until you have:
>
> 1. **Conversion by traffic source.** One bad source often explains the average.
> 2. **Step-level drop-off.** Which step loses them, not the end-to-end rate.
> 3. **Total volume on that surface.** Step 2 cannot run without it.

If the user cannot supply these, say what they need to pull and where — the GA4
funnel exploration, the ad platform's landing-page report — and offer to design
the test once the numbers exist. Naming the specific pull is the deliverable.

**Withholding the variants does not mean withholding the arithmetic.** The
conversion rate alone is enough to run Step 2, and you should, in the same reply
as the gate. A refusal that carries a number — *"a copy test here needs 107,000
per arm and 43 days, so it cannot run"* — is an argument. A refusal that promises
to calculate later is a delay, and the user will read it as obstruction and go
elsewhere for the variants.

**When the ask is genuinely upstream of a test** — the proposition is weak, the
price is wrong, the audience is mismatched — say so and route it. See
*Boundaries* below.

## Step 2: Compute the test before designing it

Never estimate sample size or duration in prose. Run the script.

```bash
python scripts/power.py size --baseline 0.004 --mde 20 --daily-traffic 5000
```

`--baseline` is the current rate as a decimal (0.4% is `0.004`). `--mde` is the
smallest lift worth detecting, as a percentage, relative by default. Add
`--absolute` for percentage points.

It reports the sample per arm, the total, the days required, and refuses tests
that cannot resolve inside about four weeks.

**The MDE is a business decision, not a statistical one.** Ask what lift would
change what they do. A lift too small to act on is not worth detecting, and
detecting it costs the most traffic.

If the script says the test is not runnable, that is the answer. Deliver it,
with the alternatives it names: test a bigger swing, move to a higher-traffic
surface, or fix the constraint directly and measure the before/after honestly as
an uncontrolled change.

## Step 3: Judge a result with the same instrument

When the user reports a result, evaluate it — do not react to the number they
quote.

```bash
python scripts/power.py evaluate --a-n 340 --a-conv 100 --b-n 340 --b-conv 118 --required-n 4000
```

Pass `--required-n` whenever a fixed sample was set, because stopping early is
the most common way a real-looking result turns out not to be real.

Report the confidence interval, not just the p-value. An interval that contains
zero means "no difference" is still compatible with the data, however good the
headline lift looks.

**Three questions the arithmetic cannot answer.** Ask them before any rollout:

- Did it run whole weeks? Partial weeks compare different populations.
- Did anything else change mid-test? Traffic mix, price, a campaign launch.
- Does the effect hold in the second half of the window? An effect present only
  in the first days is usually novelty, and it decays.

## Step 4: Every number carries its source

Read `references/evidence-and-proof.md` before quoting any benchmark.

Requests here arrive shaped as "what's a good conversion rate for our industry"
and the honest answer is usually that you do not have a citable one. Name the
report that would produce a real number instead. A figure the user pulled from
their own account beats a category average, and it is the only version they can
defend.

## Step 5: Validate

Load `references/rubric-experiment-design.md`. Score every line PASS or FAIL with
quoted evidence, burden of proof on PASS. Fix, re-score, **maximum two rounds**.

This is a self-check against a written standard, not independent review.

## Boundaries

This skill owns whether to test and whether to believe. It does not own the
thing being tested.

| If the real problem is | Route to |
|---|---|
| The proposition, price, or guarantee is weak | `offer-design` |
| The words on the page, once the constraint is known | `copywriting` |
| The interface, motion, or interaction feels wrong | `ui-design-engineering` |
| No one agrees what the work is supposed to do | `creative-brief` |
| The org keeps testing instead of deciding | `marketing-architecture-audit` |

Say which one you are routing to and why. Do not run their steps here.

## Gotchas

- **Producing variants because they were asked for.** The gate in Step 1 is the
  main reason this skill exists. A page at 0.4% does not have a copy problem.
- **Quoting the user's p-value back to them.** Recompute it. Reported values are
  frequently wrong, and the arithmetic takes seconds.
- **Treating p as the probability the variant is better.** It is the probability
  of data this extreme if there were no difference. Correct this when you see it.
- **Peeking.** Checking daily and stopping on significance does not hold the
  false positive rate at 5%. It inflates it substantially.
- **Testing when the answer is already known.** A broken step, a 404, a form that
  fails on mobile — fix it. An A/B test on a defect is theatre.
- **Do not cite conversion-rate benchmarks.** Almost none trace to a named study
  with a stated population. See `references/evidence-and-proof.md`.
