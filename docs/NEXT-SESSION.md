# Next Session

Last updated: 2026-07-19

## Where things stand

10 skills build for both targets. Repo is `StammDXB/lucas-growth-skills`
(private, `main`), clean and pushed.

```
skills/     copywriting, campaign-concept, offer-design, brand-strategy,
            creative-brief, press-release, marketing-architecture-audit,
            short-form-video, ui-design-engineering, stakeholder-response
lenses/     semiotics, persuasion-frameworks, voice-and-tone, luxury-codes,
            brand-foundations, evidence-and-proof
rubrics/    one per skill
lucas-growth/  previous 35-skill generation, retained pending audit
```

Build:
```bash
python3 scripts/build.py            # dist/*.zip for Claude Desktop
python3 scripts/build.py --plugin   # plugin/ for Claude Code marketplace
python3 scripts/build.py --check    # validate only
```

**Always run both build targets before committing.** Forgetting `--plugin`
means the marketplace silently serves stale skills.

Design spec: `docs/superpowers/specs/2026-07-19-skill-system-design.md`

## The work, in priority order

### 1. Evals (partially done, see `docs/evals/2026-07-19-pilot-results.md`)

All 10 skills now have `evals/evals.json`: 80 cases, 331 assertions. **Three
were run. Seven were not.**

| Skill | Status |
|---|---|
| `copywriting` | Beats baseline, N=3. 2W 0L 6T, preference 21-3. Two open defects, repair unverified. |
| `ui-design-engineering` | Beats baseline, N=1 only. Needs confirming. |
| `marketing-architecture-audit` | Beats baseline, N=1 only. Needs confirming. |
| The other seven | **No evidence in either direction.** |

**Read the noise finding before running anything.** The identical baseline arm
drifted on 10 of 24 cases between runs, and 23% of assertions flip verdict
between replicates. A single run cannot support a cut decision, and a plausible
"finding" from one run was already withdrawn once when the next run contradicted
it. Use N>=3 with majority voting, or accept that you are reading noise.

**Do not run all seven at full breadth.** That is ~510 agents and the pilot
suggests most of it buys nothing: the ties cluster in predictable places.
Run only the hard-gate, folklore, fabrication, and negative cases per skill at
N=2, roughly 160 agents for all seven, and escalate only near the boundary.

The harness is a workflow script that fans out baseline arm, skill arm, and a
blind grader per case, then majority-votes each assertion and reports an
explicit `unstableAssertionRate`. Rebuild it from the results doc if the
session scripts are gone.

### 1b. Decide the 13 orphaned references

`build.py --check` now warns on every bundled file that SKILL.md never names.
There are 13, 72KB across 8 skills, invisible to Claude because progressive
disclosure only loads what the body asks for. Each needs a load-trigger in the
body, or removal from `skill.yaml`. The eval evidence bears on this: a skill
that beats baseline while never loading its declared lenses is an argument for
deleting the declaration.

### 2. Remove Anthropic duplicates from Claude Desktop

These are installed in Desktop and ship with Claude natively, so they only
compete for trigger space:

`mcp-builder`, `pdf`, `web-artifacts-builder` (byte-identical to Anthropic's),
plus variants of `canvas-design`, `docx`, `pptx`, `xlsx`, `skill-creator`.

Manual removal in Claude Desktop: Customize > Skills.

### 3. Audit the 16 `thinking-*` Desktop skills

Roughly 5,000 lines competing for trigger space. Several likely do not beat raw
Claude. Same baseline test as item 1. Needs evidence before cutting, not
assumption.

## Constraints learned the hard way

**WebSearch quota is session-wide.** Five parallel research agents exhausted
200/200 within minutes and three returned degraded or empty. Dispatch research
agents **sequentially, one at a time**, scoped to the artifact being built.

**When the quota dies, WebFetch against primary sources still works.** The two
best research briefs of the last session came from agents that hit the dead
quota and pivoted to fetching platform engineering blogs and original papers
directly. That is worth instructing up front.

**Desktop skills are cached locally** and can be read directly:
`~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/<uuid>/<uuid>/skills/`

## Decisions already made, do not relitigate without reason

- **Do not bulk-absorb `comms-architect`.** It bundles the ClawFu library
  (175 methodologies, 380,545 words). Its MIT frontmatter covers the wrapper,
  not the bundle. Harvest selectively with primary-source citations instead.
- **Do not vendor Anthropic skills.** They are Apache-2.0 and ship natively.
  Fifteen were previously vendored with the licence stripped; they were removed.
- **Client-specific brand systems stay out.** A client brand layer was
  genericized rather than merged, because the pack must work across businesses.
- **The validation loop is a self-check, not independent review.** Desktop has no
  subagents. Never describe it as unbiased. The only genuinely blind option is
  the opt-in fresh-chat packet.

## House standard for any new skill

SKILL.md under 500 lines, description under 1024 chars, depth in `references/`
with explicit load-triggers, a rubric with cited-evidence scoring and a two-round
stop, a clarify-first gate, and a do-not-cite list wherever the field is
folklore-heavy.
