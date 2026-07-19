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

### 1. Evals (biggest real gap)

Only `copywriting` has `evals/evals.json`, and even those have never been run.
Nine skills ship unverified against the bar the spec sets:

> "If the agent already handles the entire task well without the skill, the
> skill may not be adding value."

For each skill: write 6 to 8 cases, run each **with and without** the skill,
grade assertions with cited evidence, and cut anything that does not beat
baseline. Include at least one negative case checking the skill stays out of the
way on trivial asks (see `skills/copywriting/evals/evals.json` case 8).

Expect some skills to fail. That is the point.

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
