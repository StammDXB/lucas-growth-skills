# 📈 lucas-growth-skills

Thirteen marketing, brand, and growth skills for **Claude Desktop** and
**Claude Code**.

By [Lucas Stamm](https://lucasstamm.com).

## 🎯 The premise

Claude already writes decent marketing copy. A skill that says "write good copy"
therefore adds nothing, and most marketing skills are exactly that.

Every skill here had to beat an unaided model on blind, graded evals before it
shipped. Six planned skills failed that test and were never built.

Three things the skills add, measured rather than asserted:

| | What the unaided model does | What the skill does | Graded |
|---|---|---|---|
| 🔢 **Numbers** | Builds a revenue model on an "8-10% add-to-cart baseline" the grader traced to a vendor page that does not support it | Cites the one benchmark it can source, refuses the two it cannot, sends you to your own analytics | 5/5 vs 0/5 |
| 🚧 **Gates** | Says the 0.4% conversion problem is upstream of the button, then supplies three button colours, timer alternatives and five copy variants anyway | Names the constraint and stops there | no case lost |
| 📧 **Compliance** | Drops the unsubscribe line and invents the offer terms | Treats compliance as a copy decision, not a legal footnote | 4/4 vs 2/4 |

The grader's note on the gate case: *"it says colour is the lowest-leverage
lever and supplies three colours."* Naming a gate is baseline behaviour. Holding
it is what the skill adds.

Folklore is the exception worth naming: an unaided model already corrects most
marketing myths on its own. So the references do not re-teach that. They carry a
**do-not-cite** list instead — "80% of people only read the headline" and
spam-trigger-word avoidance included — because uncited numbers are the failure
that survives.

Full results: [`docs/evals/`](docs/evals).

## 🧰 The skills

**Shipping, 13 skills:**

| Skill | Job |
|---|---|
| ✍️ `copywriting` | Landing pages, email, social, long-form, editing |
| 💡 `campaign-concept` | Insight to proposition to platform to executions |
| 🎁 `offer-design` | Promise, mechanism, proof, risk reversal, pricing |
| 🧭 `brand-strategy` | Positioning, architecture, codes, fluency diagnostic |
| 📋 `creative-brief` | Briefs that can be argued with, and interrogating existing ones |
| 📰 `press-release` | Newsworthiness scoring, releases, pitches, embargoes |
| 🏗️ `marketing-architecture-audit` | Coordination work versus judgment work in a marketing org |
| 🎬 `short-form-video` | Script, storyboard, and AI video prompts for a vertical cut |
| 🎨 `ui-design-engineering` | Animation decisions, component craft, motion performance |
| 🤝 `stakeholder-response` | High-stakes replies: pushing back, declining, delivering bad news |
| 🧪 `experiment-design` | Whether a test can resolve, whether a result is real, where the constraint is |
| 🎟️ `prize-promotions` | Permit, platform and terms gate for giveaways and prize draws |
| 🤖 `prompt-master` | Tool-specific prompts for other AI systems ([vendored, MIT](NOTICE)) |

You do not call them by name. Describe the work — "rewrite this hero section",
"is variant B actually winning", "we want to run a giveaway in Dubai" — and
Claude loads the matching skill.

## 🚀 Install

Both apps install the same plugin straight from this repo. Nothing to build, no
zips to manage — Desktop does it through the UI, Claude Code through a command.

| | Claude Desktop | Claude Code |
|---|---|---|
| **How** | Add the marketplace in the UI | Two slash commands |
| **Build step** | None | None |
| **Gets you** | All thirteen at once | All thirteen at once |
| **Steps** | Six, below | Two, below |

### 💻 Claude Desktop, step by step

1. **🖥️ Open Claude Desktop** and go to **Customize**.
2. **🧩 Click Plugins.**
3. **➕ Click Add**, then **Add Marketplace**.
4. **📚 Choose Add from Repository.**
5. **🔗 Paste the repo URL** and confirm:

   ```
   https://github.com/StammDXB/lucas-growth-skills
   ```

6. **⬇️ Install the `lucas-growth` plugin** from the marketplace that appears.
   All thirteen skills arrive together.

**Then check it fires.** Start a chat and paste a page of copy with "make this
less generic". Expand Claude's thinking: the skill should be named there.

| Symptom | Cause | Fix |
|---|---|---|
| Marketplace adds but no skills appear | Plugin added, not installed | Open the marketplace entry and install **lucas-growth** |
| Skills installed but never fire | Code execution is off | **Settings → Capabilities → Code execution and file creation** |
| Still never fires | The ask is too small to warrant it | Expected. Every skill sizes the ask first and answers one-liners plainly |

### ⌨️ Claude Code

```
/plugin marketplace add StammDXB/lucas-growth-skills
/plugin install lucas-growth@lucas-growth
```

Skills appear as `lucas-growth:<skill>`.

### 📦 Or one skill at a time, as a zip

Only if you want a single skill rather than the pack. Needs Python 3 and PyYAML
(`pip3 install pyyaml`), because `dist/` is not committed:

```bash
git clone https://github.com/StammDXB/lucas-growth-skills.git
cd lucas-growth-skills
python3 scripts/build.py copywriting     # or omit the name for all thirteen
```

Then in Claude: **Customize → Skills → +**, upload `dist/copywriting.zip`, and
toggle it on. The zip holds the skill folder at its root, which is the structure
Claude expects.

## 🏛️ Why it is structured this way

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

### 🔍 The lenses

Authored once, compiled into whichever skills declare them:

| Lens | Loaded when |
|---|---|
| `evidence-and-proof` | Any claim about what works, or citing a framework, study or statistic |
| `voice-and-tone` | Writing in a brand voice, defining one, or diagnosing why copy sounds wrong |
| `persuasion-frameworks` | Writing anything meant to move someone to act, or building an offer |
| `consumer-psychology` | Reasoning about why someone buys, or applying a named behavioural effect |
| `brand-foundations` | Positioning, brand architecture, distinctive assets |
| `semiotics` | Category codes, or why something "feels" premium, cheap, or dated |
| `luxury-codes` | Luxury and premium work: scarcity, provenance, pricing power |

### 🔗 How the skills fit together

Coordination is structural rather than runtime. Three mechanisms carry it:

1. **Shared lenses, compiled in.** Every skill that makes a claim compiles
   `evidence-and-proof`; every writing skill compiles `voice-and-tone`. One
   standard, enforced identically everywhere, resolved at build time.
2. **Routing tables.** Every skill carries a `## Boundaries` section naming
   which sibling owns adjacent work — the offer versus the copy, the brief
   versus the idea, the test versus the thing being tested. A skill that hits
   someone else's territory names the destination and stops.
3. **A shared proportionality gate.** Every skill opens by sizing the ask, so a
   one-line question gets a one-line answer instead of a full deliverable.

## 🔨 Build

| Command | What it does |
|---|---|
| `python3 scripts/build.py` | `dist/*.zip` for Claude Desktop |
| `python3 scripts/build.py --plugin` | `plugin/` for the Claude Code marketplace |
| `python3 scripts/build.py copywriting` | Build one skill |
| `python3 scripts/build.py --check` | Validate only, emit nothing |

**Run both build targets before committing.** Forgetting `--plugin` leaves the
marketplace serving yesterday's skills; `--check` now fails on that, and on any
count in `README.md`, `marketplace.json`, or `plugin.json` that disagrees with
the skills actually present.

The build also hard-fails on any reference to a file that does not exist. That
check exists because an earlier version of this repo shipped 46 references to
files that were never written.

## 🧾 Evidence standard

Every claim in a reference file is graded. Where a framework is real but its
supporting evidence is weak, the file says so. Where a widely repeated statistic
has no traceable source, it appears on a **do-not-cite** list rather than being
quietly omitted.

This matters more than it sounds: the default failure mode when an LLM writes
marketing content is confidently emitting folklore. Several references
explicitly instruct against claims the model would otherwise reach for.

## 🚫 What was not built

Six consolidated growth skills were specified (conversion-optimization, seo,
paid-acquisition, lifecycle-retention, pricing-revenue, measurement).
**Baseline probing on 2026-07-22 did not support building them.** Across 24
probes in six domains, an unaided model corrected marketing folklore in 6/6
domains unassisted, and the only consistent failure was uncited or fabricated
numbers. `experiment-design` is the one skill that survived that test, scoped to
the gates and arithmetic the baseline actually misses. See
`docs/evals/2026-07-22-growth-probe-results.md`.

The 35 skills under `lucas-growth/` are the previous generation, retained until
each is either absorbed or cut against the same test.

## 📄 License

MIT. See `LICENSE`. Third-party attribution in `NOTICE`.
