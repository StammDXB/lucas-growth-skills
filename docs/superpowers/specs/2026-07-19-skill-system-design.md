# Design: Claude Desktop Skill System

Date: 2026-07-19
Status: Approved for planning
Target: Claude Desktop / claude.ai only (not Claude Code)

## 1. Problem

The repo holds 35 skills salvaged from a private workspace. Two problems:

1. **Wrong coverage.** The 35 are a growth/performance stack (CRO, SEO, paid,
   email, retention, analytics). The disciplines actually needed are largely
   absent: semiotics, luxury fundamentals, creative offer design, campaign
   conceptualization, press release craft, creative copywriting. Only
   `marketing-psychology` and `brand-fluency-audit` touch that territory.
2. **Unproven quality.** The skills were LLM-generated without domain grounding,
   which is the documented number one authoring pitfall. None has been tested
   against a no-skill baseline, so none is known to add value.

Goal: a disciplined, orchestrated system of skills that are generic across
businesses and offers, but deeply specific to the job each performs.

## 2. Verified constraints

All verified against official sources. These are binding.

| Constraint | Source |
|---|---|
| No subagents, no agent dispatch in Desktop | [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) |
| Skills cannot explicitly reference or invoke other skills. Claude may compose them automatically, but this is not a designable mechanism | [Create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) |
| SKILL.md under 500 lines and 5,000 tokens | [Specification](https://agentskills.io/specification) |
| `description` max 1024 chars, carries the entire triggering burden | [Optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions) |
| `name` max 64 chars, lowercase/digits/hyphens, must match directory name | [Specification](https://agentskills.io/specification) |
| Progressive disclosure: metadata always loaded, body on activation, `references/` on demand | [Specification](https://agentskills.io/specification) |
| Upload is a ZIP with the skill folder at root, one skill per upload | [Create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) |
| Available on Free, Pro, Max, Team, Enterprise | [Create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) |

### 2.1 Consequences

- **Every skill must be self-contained.** No runtime chaining. Shared knowledge
  is compiled in at build time.
- **A true independent Judge is impossible in a single Desktop conversation.**
  What is possible, and what Anthropic documents, is a validation loop against a
  bundled rubric file. This is a grounded self-check. It will be named honestly
  as such and never presented as independent review.
- **Depth cannot live in SKILL.md.** It lives in `references/` with explicit
  load-triggers.

## 3. Architecture

Author once, compile into self-contained distributables.

```
SOURCE (git)
  lenses/                    single source of truth for shared knowledge
  rubrics/                   shared validators
  skills/<job>/
    SKILL.md                 lean router, under 500 lines
    skill.yaml               declares which lenses and rubrics to compile in
    references/              job-specific depth, each with a load-trigger
    evals/evals.json         test cases and assertions
  scripts/build.py           compiler
DIST
  <job>.zip                  self-contained, Desktop-ready
```

`build.py` reads each `skill.yaml`, copies declared lenses and rubrics into that
skill's `references/`, validates frontmatter and line limits, and emits a ZIP
with the skill folder at root.

### 3.1 Why compile rather than chain

Skills cannot reference each other. Duplicating lens content by hand would drift
out of sync across 13 skills. Compilation gives DRY authoring and self-contained
shipping at once. Cost: a rebuild and re-upload when a lens changes.

## 4. Skill anatomy standard

Every job skill follows the same shape.

```
SKILL.md
  frontmatter: name, description (trigger-optimized), license, metadata
  When to use / when not to use
  Clarify-first gate
  Routing table: artifact type -> which reference to load
  Procedure
  Gotchas
  Output template
  Validation step
```

### 4.1 Clarify-first gate

Every skill opens with a required check. If the job cannot be done well without
information the user has not supplied (audience, positioning, offer, channel,
constraints, proof available), the skill asks before producing. It does not
guess and does not fall back on generic assumptions.

This is a hard rule. A confident generic deliverable is worse than a question.

### 4.2 The control loop

Anthropic's documented "validation loop" pattern, adapted to the three roles.
The scaffolding is internal. The user sees a clean deliverable.

```
BUILD     Draft with creative latitude. Track assumptions and uncertainties
          internally. Do not surface scaffolding.

VALIDATE  Load rubrics/<job>.md. Score every line PASS or FAIL.
          Each verdict cites specific evidence quoted from the draft.
          No partial credit. Burden of proof is on PASS.

REVISE    Fix every FAIL. Re-score. Maximum 2 rounds.

DELIVER   Clean deliverable, then a short plain-language quality note.
          Anything still failing after 2 rounds is stated openly,
          never hidden or quietly dropped.
```

Stop condition: 2 revision rounds. After that the skill surfaces what it could
not fix and why, rather than looping.

### 4.3 Honest labelling

The quality note says "checked against <rubric>", not "independently reviewed".
For high-stakes work the skill offers an optional blind review: it emits a
compact packet containing the brief, the rubric name, and the artifact with no
reasoning attached, which the user can paste into a fresh conversation. That is
genuinely unbiased because the new context never saw the draft being made.

## 5. Lenses

Bodies of knowledge, compiled into jobs that declare them. Never trigger alone.

| Lens | Consumers |
|---|---|
| `semiotics` | campaign-concept, brand-strategy, copywriting, press-release |
| `luxury-codes` | all creative jobs, pricing-revenue |
| `consumer-psychology` | offer-design, copywriting, conversion-optimization, pricing-revenue |
| `persuasion-frameworks` | copywriting, offer-design, press-release |
| `voice-and-tone` | every writing job |
| `brand-foundations` | campaign-concept, brand-strategy, copywriting |
| `evidence-and-proof` | every job that makes a claim |

Lens content is researched and cited. Where evidence quality is contested (for
example replication failures in behavioural science), the lens states this
explicitly rather than presenting shaky findings as settled.

## 6. Job skills

### Creative and brand (new)

| Skill | Job |
|---|---|
| `copywriting` | Write copy, routing by artifact type |
| `campaign-concept` | Insight to platform idea to executions |
| `offer-design` | Construct commercially strong offers |
| `press-release` | Media materials that editors will run |
| `brand-strategy` | Positioning, architecture, codes |
| `creative-brief` | Write the brief that briefs the work |
| `marketing-architecture-audit` | Audit a marketing org for coordination work versus judgment work |

### Growth (consolidated from the existing 35)

| Skill | Absorbs |
|---|---|
| `conversion-optimization` | page, form, popup, signup-flow, onboarding, paywall CRO |
| `seo` | seo-audit, ai-seo, programmatic-seo, schema-markup, site-architecture, competitor-alternatives |
| `paid-acquisition` | paid-ads, ad-creative |
| `lifecycle-retention` | email-sequence, churn-prevention |
| `pricing-revenue` | pricing-strategy, revops |
| `measurement` | analytics-tracking, ab-test-setup |

### Disposition of the remaining 15

Every one of the 35 must have a stated destination. The 20 above are absorbed
into growth jobs. The remaining 15:

| Current skill | Disposition |
|---|---|
| `copy-editing` | Into `copywriting` as its editing mode |
| `social-content` | Into `copywriting` as social artifact types |
| `marketing-ideas` | Into `campaign-concept` |
| `launch-strategy` | Into `campaign-concept` |
| `lead-magnets` | Into `offer-design` |
| `free-tool-strategy` | Into `offer-design` |
| `referral-program` | Into `lifecycle-retention` |
| `brand-fluency-audit` | Into `brand-strategy` as a diagnostic mode |
| `marketing-psychology` | Becomes the `consumer-psychology` lens |
| `ai-output-hygiene` | Splits: AI-tell detection into the `voice-and-tone` lens, the rest into the `copywriting` rubric |
| `marketing-architecture-audit` | Survives standalone as a 13th job. It audits an organization, not an artifact, so it does not fit any other job. |
| `typography-craft` | Deferred. Design discipline with no job to attach to yet. Retained in source, not built or shipped in phases 1 to 4. |
| `santa-review` | Delete. Superseded by the per-skill validation loop in section 4.2. |
| `click-path-audit` | Delete. Frontend debugging, not a marketing discipline. Out of scope for this system. |
| `nano-pdf` | Delete. A utility wrapper around an external CLI, not a discipline, and it depends on a tool that may not exist in Desktop. |

This yields **13 job skills and 7 lenses**, with 3 deletions and 1 deferral.

All dispositions marked "into" remain subject to the baseline test in section 7.
Absorption is not automatic: if the absorbed material does not help the
receiving skill beat baseline, it is cut rather than carried.

## 7. Quality bar

A skill ships only when all of the following hold.

1. **Beats baseline.** Documented evidence it outperforms Claude with no skill
   on the same prompts. Anthropic: "If the agent already handles the entire task
   well without the skill, the skill may not be adding value." This is the
   primary cut criterion for the existing 35.
2. **Grounded.** References cite real, verifiable sources. No invented
   frameworks, practitioners, or statistics. Contested evidence flagged.
3. **Triggers correctly.** Description tested against roughly 20 labelled
   queries with a train/validation split, 3 runs each, using trigger rate.
4. **Within limits.** SKILL.md under 500 lines and 5,000 tokens. Description
   under 1024 characters.
5. **References real.** Every referenced file exists and carries a load-trigger
   stating when to read it. This repo previously shipped 46 references to files
   that never existed. That failure must not recur.
6. **Rubric present.** A written validator, not a vague quality gesture.

## 8. Phasing

**Phase 1: copywriting, end to end.** The reference implementation. Exercises
multi-artifact routing, three compiled lenses, rubric, evals, description
tuning, and the build script. Reviewed before anything else is built.

**Phase 2: remaining creative cluster.** campaign-concept, offer-design,
press-release, brand-strategy, creative-brief, marketing-architecture-audit.

**Phase 3: growth consolidation.** Audit the 35 against the baseline test.
Merge survivors into the 6 growth jobs. Delete what fails.

**Phase 4: system hardening.** Cross-skill consistency, description
disambiguation across the full set, packaging and install documentation.

## 9. Risks

| Risk | Mitigation |
|---|---|
| Research produces generic content, the known pitfall | Require citations. Reject any claim that cannot be traced to a real source. |
| 13 descriptions collide and trigger wrongly | Phase 4 disambiguation pass, with near-miss negative queries per skill |
| Rubric self-check ratifies its own work | Evidence citation required per line, burden of proof on PASS, plus the opt-in blind review for high stakes |
| Build step drifts from dist | Build is the only path to dist. Never hand-edit dist. |
| Scope overrun | Phase 1 gated on review before Phase 2 starts |

## 10. Open questions

- Whether the mcpmarket leaderboard survey changes the discipline map. It
  returned HTTP 429 during design and has not yet been surveyed.
- Whether Desktop imposes an undocumented limit on installed skill count.
- Whether any growth skills survive the baseline test, which determines how much
  of Phase 3 is consolidation versus deletion.
