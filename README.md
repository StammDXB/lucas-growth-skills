# lucas-growth-skills

Marketing, brand, and growth skills for **Claude Desktop**.

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
  evals/          beat-the-baseline test cases
scripts/build.py  compiler
dist/<job>.zip    self-contained, ready to upload
```

## Build

```bash
python3 scripts/build.py              # build all
python3 scripts/build.py copywriting  # build one
python3 scripts/build.py --check      # validate only
```

The build hard-fails on any reference to a file that does not exist. That check
exists because an earlier version of this repo shipped 46 references to files
that were never written.

## Install into Claude Desktop

1. `python3 scripts/build.py`
2. In Claude, go to **Customize > Skills**, click **+ Create skill**
3. Upload `dist/<skill>.zip`

One skill per upload. The zip contains the skill folder at its root.

## Status

**Shipping, 7 skills:**

| Skill | Job |
|---|---|
| `copywriting` | Landing pages, email, social, long-form, editing |
| `campaign-concept` | Insight to proposition to platform to executions |
| `offer-design` | Promise, mechanism, proof, risk reversal, pricing |
| `brand-strategy` | Positioning, architecture, codes, fluency diagnostic |
| `creative-brief` | Briefs that can be argued with, and interrogating existing ones |
| `press-release` | Newsworthiness scoring, releases, pitches, embargoes |
| `marketing-architecture-audit` | Coordination work versus judgment work in a marketing org |

**Lenses**, compiled into whichever skills declare them: `semiotics`,
`persuasion-frameworks`, `voice-and-tone`, `luxury-codes`, `brand-foundations`,
`evidence-and-proof`.

**Planned:** six consolidated growth skills (conversion-optimization, seo,
paid-acquisition, lifecycle-retention, pricing-revenue, measurement). See
`docs/superpowers/specs/2026-07-19-skill-system-design.md`.

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
