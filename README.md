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

**Shipping:** `copywriting`

Routes by artifact type (landing page, email and newsletter, social, long-form,
editing), stages the reader on awareness and market sophistication before
drafting, and validates against a written rubric before delivering.

**Lenses written:** semiotics, persuasion-frameworks, voice-and-tone,
luxury-codes

**Planned:** campaign-concept, offer-design, press-release, brand-strategy,
creative-brief, marketing-architecture-audit, plus six consolidated growth
skills. See `docs/superpowers/specs/2026-07-19-skill-system-design.md`.

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
