---
name: marketing-architecture-audit
description: >-
  Audit a marketing team for coordination work vs judgment work. Identifies which roles are
  redundant with modern AI + automation systems, produces a redundancy map, and recommends the
  specific systems that would collapse those roles. Built for hospitality groups but works for
  any marketing org. Use when the user says "audit my marketing team", "should I hire another
  marketer", "architect my marketing", "marketing team too big", "marketing architecture",
  "architecture beats headcount", or wants to know which of their marketing roles could be
  replaced by systems.
---

# Marketing Architecture Audit

**One responsibility:** Look at a marketing team, identify which roles are doing coordination work (replaceable by systems) vs judgment work (genuinely requires a human), and output a specific redundancy map with system recommendations.

**Origin:** developed for multi-brand hospitality groups, where marketing headcount grows faster than output. It generalizes to any marketing org with more than two people. Run it quarterly on your own team, or during discovery on a prospective client.

---

## Step 1: Ask the 7 questions

Ask these in sequence. Wait for answers before proceeding. Do not batch them; the user's answers to earlier questions inform how you frame later ones.

**Q1.** What does your business do, and how many brands / venues / locations are you currently operating? (This sets the scale of the architecture.)

**Q2.** List every marketing role in your current org. Include titles, whether they're full-time employees, fractional, or retainers. Include agencies. Include yourself if you hold a marketing responsibility.

**Q3.** For each role, write one sentence describing the unique human judgment that role makes. Not the outputs they produce — the judgment. Example: "Brand Manager: decides what tone we use with guests this quarter." If the sentence is hard to write, note that.

**Q4.** What are the top three marketing coordination meetings you run weekly or bi-weekly? What are they usually about? (This surfaces where handoff failures live.)

**Q5.** What percentage of your marketing team's time do you estimate goes to: (a) making decisions, (b) creating original content, (c) moving assets between tools / reformatting / briefing, (d) reporting? Rough percentages are fine.

**Q6.** What's your fully-loaded annual marketing headcount cost, including salaries, benefits, and retainers? A range is fine. Also: what's your annual tooling / software spend?

**Q7.** If you had to describe your current marketing system architecture in one paragraph, could you? If not, skip this question and note it.

---

## Step 2: Classify each role

For every role in Q2, classify into one of three categories:

### Category A — Judgment role (keep as-is)

Criteria: the sentence the user wrote in Q3 is crisp and specific. The role makes decisions machines can't make (taste, brand voice, relationships, strategy). Examples: Marketing Director making positioning calls, PR lead managing journalist relationships, Brand Manager setting quarterly tone.

**Verdict:** Keep. This role cannot be architected out.

### Category B — Hybrid role (30-50% reducible)

Criteria: the role makes some judgment calls but most of the day is coordination, briefing, reformatting. The sentence in Q3 was partially clear but vague on edges.

**Verdict:** Restructure. Human keeps the judgment slice (often 20-40% of the role). Systems handle the rest. The role may shrink to part-time or consolidate with another role.

### Category C — Coordination role (fully replaceable)

Criteria: the sentence in Q3 was hard to write, or the role's day is dominated by handoffs, status-chasing, and asset management. This includes most "Marketing Coordinator", "Digital Marketing Executive", "Marketing Operations" roles as typically scoped in mid-sized orgs.

**Verdict:** Replace with system. The human function is no longer needed at all when the architecture is in place.

---

## Step 3: Name the specific systems

For every Category B and Category C role, propose the specific system that replaces the coordination work. Use this mapping as the starting point (adapt to user's specific context):

| Coordination work observed | System that replaces it |
|---|---|
| Writing briefs, managing designer handoffs | Visual system: brand-locked templates + AI image generation (nano-banana / Gemini) for variations |
| Drafting captions, reformatting posts across channels | Content system: weekly calendar reading from a single source of truth, AI-drafted captions reviewed before publish |
| Managing paid campaigns, reporting on spend | Ads system: Google Ads + Meta Ads integration (MCP or API) feeding performance back to decision layer |
| Chasing assets across tools, coordinating campaign launches | Orchestration system: calendar-driven workflow that handles dependencies automatically |
| Pitching to journalists, monitoring press mentions | PR system: journalist database + pitch templates + automated press monitor (e.g., Meltwater, Google Alerts, trend radar) |
| Reporting, dashboards, weekly slides | Reporting system: live dashboard pulling from GA4 + paid platforms + CRM, replaces the weekly slide deck |

For each proposed system, include:
- **Rough build cost** (one-time or recurring, AED or USD)
- **Who owns it** (typically the remaining judgment role, not a new hire)
- **Timeline to get it running** (most are 1-3 weeks of focused work)

---

## Step 4: Run the AED math

Based on Q6, calculate:

1. **Current fully-loaded cost** (salaries + retainers + tooling)
2. **Architected cost** (judgment roles kept at current salary, Category C roles removed, tooling increased by estimated system cost)
3. **Annual delta** (savings from architecture)
4. **Payback period** on one-time system build costs

Be honest. If the user's answer to Q6 is vague, ask for tighter numbers before running the math. Do not fabricate.

---

## Step 5: Output the Architecture Canvas

Deliver the audit as a single structured report:

```
# Marketing Architecture Audit: {user's company / brand}

## Summary
You currently operate a {N}-role marketing function at roughly {AED/USD X}/year fully loaded.
An architected alternative runs with {M} roles and {K} systems at roughly {AED/USD Y}/year.
Annual delta: {AED/USD Z} ({percentage}% reduction).

## Role Classification

| Role | Category | Verdict | Notes |
|---|---|---|---|
| [Role 1] | A (Judgment) | Keep | {one-sentence judgment they make} |
| [Role 2] | B (Hybrid) | Restructure | {what to keep, what to replace} |
| [Role 3] | C (Coordination) | Replace with system | {which system below} |
...

## Recommended Systems

### System 1: {name}
- **Replaces:** {roles / work}
- **Build cost:** {AED X one-time + AED Y/month tooling}
- **Owner:** {remaining judgment role}
- **Timeline:** {weeks}

### System 2: {name}
...

## The AED Math

- Current fully-loaded cost: {AED X/year}
- Architected cost: {AED Y/year}
- Annual delta: {AED Z/year}
- Payback on system builds: {months}

## Risk Notes
{Any caveats — e.g., if the user has a Brand Manager with irreplaceable relationships, or a PR lead whose journalist relationships took 10 years to build, surface that. Systems don't replace relationships.}

## First three moves (if you wanted to start this week)
1. {most obvious quick win}
2. {next-highest-leverage move}
3. {the harder one that pays off long-term}
```

---

## Rules

- **Be honest about what systems can and can't do.** Don't oversell AI. Systems do coordination; humans do taste, relationships, and non-obvious judgment.
- **Respect the user's context.** A 20-person marketing org in a hotel group operates differently from a 3-person F&B group. Don't apply one template to both.
- **Don't fabricate numbers.** If the user can't provide a salary range, ask them to check a public benchmark (Hays GCC Salary Guide, GulfTalent, Glassdoor) rather than invent.
- **Default to architecture, not to firing.** The outcome the user wants is leverage, not a layoff. Most Category C roles can be retrained into Category A/B work if the person wants to learn. Say that explicitly in the report.

---

## If the user's situation is out of scope

This skill is designed for internal marketing teams, typically 3-15 people, at operating businesses (not pure SaaS startups, not solo founders).

- If they have 1-2 people total: the advice is different. Tell them to skip the audit, and instead focus on ONE thing they can build (most likely: a content system). Do not run the full audit.
- If they have 50+ people: the audit applies, but the per-role classification is more nuanced. Offer to do it but flag that a deeper engagement is better suited.
- If they're a solo founder: this skill isn't for them. Redirect to a different kind of advice.

---

## Validate before delivering

Load `references/rubric-marketing-architecture-audit.md`. Score every line PASS
or FAIL, quoting evidence from your own draft. Burden of proof is on PASS. Fix
every failure, re-score, **maximum two rounds**. Anything still failing after
two rounds is a real constraint: state it in the delivery note rather than
looping or quietly dropping it.

This is a self-check against a written standard. It is not independent review,
and must not be described as one.

## Delivery note

After the report, add three lines and no more:

```
Assumed    inputs you had to assume rather than were given
Confidence which classifications are firm and which are provisional
Open       what would need checking before acting on this
```

Do not show the rubric scoring or the revision rounds. The user wants the audit,
not the machinery.
