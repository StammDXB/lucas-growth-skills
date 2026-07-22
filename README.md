# lucas-growth-skills

Marketing, brand, and growth skills for **Claude Desktop** and **Claude Code**.

By [Lucas Stamm](https://lucasstamm.com).

## Why this is structured the way it is

Claude Desktop skills cannot invoke each other at runtime and cannot share files
across skill directories. So shared knowledge is **compiled in at build time**
rather than chained at runtime.

```
lenses/           shared knowledge, authored once
rubrics/          validators the skills score against
skills/<job>/
  SKILL.md        lean router, under 500 lines
  skill.yaml      declares which lenses and rubrics to compile in
  references/     job-specific depth, each with a load-trigger
  scripts/        executable tools, run rather than read
  evals/          beat-the-baseline test cases
scripts/build.py  compiler
dist/<job>.zip    self-contained, ready to upload
```

Where a skill needs a deterministic answer rather than a judged one, it ships a
script instead of prose. `experiment-design/scripts/power.py` computes sample
size and evaluates results, because "you'll need a large sample" is the failure
it exists to replace.

## Build

```bash
python3 scripts/build.py              # dist/*.zip for Claude Desktop
python3 scripts/build.py --plugin     # plugin/ for the Claude Code marketplace
python3 scripts/build.py copywriting  # build one
python3 scripts/build.py --check      # validate only
```

**Run both build targets before committing.** Forgetting `--plugin` leaves the
marketplace serving yesterday's skills; `--check` now fails on that, and on any
count in `README.md`, `marketplace.json`, or `plugin.json` that disagrees with
the skills actually present.

The build also hard-fails on any reference to a file that does not exist. That
check exists because an earlier version of this repo shipped 46 references to
files that were never written.

## Install

**Claude Desktop:** run `python3 scripts/build.py`, then in Claude go to
**Customize > Skills**, click **+ Create skill**, and upload `dist/<skill>.zip`.
One skill per upload; the zip contains the skill folder at its root.

**Claude Code:** add this repo as a marketplace, then install the
`lucas-growth` plugin. It serves the committed `plugin/` tree.

## Status

**Shipping, 13 skills:**

| Skill | Job |
|---|---|
| `copywriting` | Landing pages, email, social, long-form, editing |
| `campaign-concept` | Insight to proposition to platform to executions |
| `offer-design` | Promise, mechanism, proof, risk reversal, pricing |
| `brand-strategy` | Positioning, architecture, codes, fluency diagnostic |
| `creative-brief` | Briefs that can be argued with, and interrogating existing ones |
| `press-release` | Newsworthiness scoring, releases, pitches, embargoes |
| `marketing-architecture-audit` | Coordination work versus judgment work in a marketing org |
| `short-form-video` | Script, storyboard, and AI video prompts for a vertical cut |
| `ui-design-engineering` | Animation decisions, component craft, motion performance |
| `stakeholder-response` | High-stakes replies: pushing back, declining, delivering bad news |
| `experiment-design` | Whether a test can resolve, whether a result is real, where the constraint is |
| `prize-promotions` | Permit, platform and terms gate for giveaways and prize draws |
| `prompt-master` | Tool-specific prompts for other AI systems ([vendored, MIT](NOTICE)) |

**Lenses**, compiled into whichever skills declare them: `semiotics`,
`persuasion-frameworks`, `voice-and-tone`, `luxury-codes`, `brand-foundations`,
`evidence-and-proof`, `consumer-psychology`.

## How the skills fit together

Claude Desktop skills cannot call each other, so coordination is structural
rather than runtime. Three mechanisms carry it:

1. **Shared lenses, compiled in.** Every skill that makes a claim compiles
   `evidence-and-proof`; every writing skill compiles `voice-and-tone`. One
   standard, enforced identically everywhere, resolved at build time.
2. **Routing tables.** Every skill carries a `## Boundaries` section naming
   which sibling owns adjacent work — the offer versus the copy, the brief
   versus the idea, the test versus the thing being tested. A skill that hits
   someone else's territory names the destination and stops.
3. **A shared proportionality gate.** Every skill opens by sizing the ask, so a
   one-line question gets a one-line answer instead of a full deliverable.

## Planned

Six consolidated growth skills were specified (conversion-optimization, seo,
paid-acquisition, lifecycle-retention, pricing-revenue, measurement).
**Baseline probing on 2026-07-22 did not support building them.** Across 24
probes in six domains, an unaided model corrected marketing folklore in 6/6
domains unassisted, and the only consistent failure was uncited or fabricated
numbers. `experiment-design` is the one skill that survived that test, scoped to
the gates and arithmetic the baseline actually misses. See
`docs/evals/2026-07-22-growth-probe-results.md`.

The 35 skills under `lucas-growth/` are the previous generation, retained until
each is either absorbed or cut against the beat-the-baseline test.

## Evidence standard

Every claim in a reference file is graded. Where a framework is real but its
supporting evidence is weak, the file says so. Where a widely repeated statistic
has no traceable source, it appears on a **do-not-cite** list rather than being
quietly omitted.

This matters more than it sounds: the default failure mode when an LLM writes
marketing content is confidently emitting folklore. Several references explicitly
instruct against claims the model would otherwise reach for, such as "80% of
people only read the headline" and spam trigger word avoidance.

## License

MIT. See `LICENSE`. Third-party attribution in `NOTICE`.
