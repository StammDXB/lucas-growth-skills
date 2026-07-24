# Contributing

Maintainer notes. Everything user-facing lives in `README.md`.

## Layout

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
plugin/           committed Claude Code plugin tree
dist/<job>.zip    self-contained Desktop upload, not committed
```

Claude Desktop skills cannot invoke each other at runtime and cannot share files
across skill directories, so lenses and rubrics are compiled into each skill
that declares them. Authoring stays DRY; distribution is self-contained.

## Build

| Command | What it does |
|---|---|
| `python3 scripts/build.py` | `dist/*.zip` for Claude Desktop |
| `python3 scripts/build.py --plugin` | `plugin/` for the Claude Code marketplace |
| `python3 scripts/build.py copywriting` | Build one skill |
| `python3 scripts/build.py --check` | Validate only, emit nothing |

Requires Python 3 and PyYAML (`pip3 install pyyaml`).

**Run both build targets before committing.** Forgetting `--plugin` leaves the
marketplace serving yesterday's skills. `--check` fails on that, and on any
count in `README.md`, `marketplace.json`, or `plugin.json` that disagrees with
the skills actually present.

The build also hard-fails on any reference to a file that does not exist. That
check exists because an earlier version of this repo shipped 46 references to
files that were never written.

## The bar for a new skill

A skill ships only if it beats an unaided model on blind, graded evals. Author
the eval suite in `skills/<job>/evals/` before the skill is considered done.

Two standing findings from `docs/evals/`:

- **Single-run evals cannot support a cut decision.** Identical baseline arms
  drift +/-2 assertions per case. Treat any aggregate delta under ~3
  assertion-points as noise.
- **Folklore is not the gap.** Across 24 probes in six domains on 2026-07-22, an
  unaided model corrected marketing folklore in 6/6 domains unassisted. The
  consistent failure was uncited or fabricated numbers, which is what
  `evidence-and-proof` and the do-not-cite lists target.

Six consolidated growth skills were specified and dropped on that evidence:
conversion-optimization, seo, paid-acquisition, lifecycle-retention,
pricing-revenue, measurement. `experiment-design` is the one that survived,
scoped to the gates and arithmetic the baseline actually misses. See
`docs/evals/2026-07-22-growth-probe-results.md`.

## Legacy

The 35 skills under `lucas-growth/` are the previous generation, retained until
each is either absorbed into a shipping skill or cut against the same test.
