---
name: short-form-video
description: >-
  Turn an idea into a complete short-form video package: script, shot-by-shot
  storyboard, and paste-ready AI video prompts for a vertical Reel, TikTok, or
  Short. Use when the user wants to make a reel, create a short video, storyboard
  something, write a video script or hook, needs voiceover or on-screen copy, or
  wants AI video prompts for Veo, Runway, Kling, Luma, Sora, or Firefly. Also use
  when they hand over a campaign idea and want it turned into video, or say
  things like "turn this into a reel", "what would the shots be", or "write me
  the prompt for this". Covers premium and hospitality video as well as
  direct-response.
license: MIT
metadata:
  version: "1.0"
---

# Short-Form Video

One pipeline, four stages, run in order. Each stage feeds the next, and skipping
a stage shows up two stages later as clips that do not cut together.

```
Brief  →  Script  →  ⏸  →  Storyboard  →  ⏸  →  Prompts
         what it says       how it looks        how it renders
```

Run all four unless the user explicitly wants only one. If they ask for "the
prompt", they usually still need the theme locked first, or the shots will not
match.

## The two checkpoints

**When you are running the full pipeline, you stop twice and wait for a human
answer.** Once after the script, once after the storyboard. These are marked ⏸
in the steps below.

The reason is cost asymmetry. Reversing a hook costs one paragraph. Reversing it
after six shots and six prompts costs the whole package, and by then the user is
attached to work they watched you build.

**When the checkpoints apply:** any run that will produce more than one stage.

**When they do not:** a single-stage request ("just write me the hook"), or
anything the size-the-ask gate above already answers directly. One checkpoint per
stage boundary, never more.

## Before anything: size the ask

If this is a quick question, a one-line lookup, a terminology check, or a small
task carrying no real stakes, answer it directly and stop. No clarifying
sequence, no rubric, no delivery note, no assumptions block.

The steps below are for real deliverables. Run them on a small question and you
produce ceremony instead of judgment, which is worse than a plain answer.

## Step 1: Clarify

Do not start without these. Infer only what is safely inferable, and state what
you inferred.

Required:
1. **The one thing it must land.** Not a list. One.
2. **Who it is for**, and where they will see it.
3. **One CTA**, or explicitly none if it is a brand piece.
4. **Brand voice and visual system**, if any exist.

Defaults if unstated: 20 seconds, 9:16 vertical, four shots of five seconds.
Say you are using them.

**Register is a decision, not a default.** Ask whether this is premium, where the
hook works through intrigue and restraint, or direct-response, where loudness
converts. Getting this wrong makes everything downstream wrong.

If the brand has a defined voice, load `references/voice-and-tone.md`. If it is
premium or luxury, load `references/luxury-codes.md` before writing anything: the
rules genuinely invert, and a discount CTA on a brand film undoes the film.

## Step 2: Script

Load `references/script.md`.

The load-bearing move is the **three-second rule**: design a visual hook, a
verbal hook, and a text hook that land simultaneously. Most weak reels have one
of the three.

Pick one structure and map every beat to seconds. Mark each line **VO** (spoken)
or **TEXT** (on-screen, added in post) so the storyboard knows what it is placing.

> **⏸ Checkpoint 1 — the idea.** Present the script and stop. Ask: *"Approve this
> script, or change the hook, the angle, or the CTA?"* Offer one alternative hook
> so approval is a choice rather than a rubber stamp.
>
> Do not storyboard until they answer. If they approve with a change, restate the
> change in one line before continuing, so a misread is caught here and not four
> shots later.

## Step 3: Storyboard

Load `references/storyboard.md`.

Lock **one visual theme** every shot obeys: palette, lighting, lens, film look,
and a motion language that names both what is allowed and **what is banned**.
"Cinematic" is not direction. "Slow dolly and gimbal float; no whip-pans" is.

Then break into four to six shots. **One main action per shot.** Vary shot scale
for rhythm. The hook image must land inside the first second.

> **⏸ Checkpoint 2 — the look.** Present the visual theme and the shot table, and
> stop. Ask: *"Approve this direction, or refine any shot?"* Name the one shot you
> are least sure of and say why, so the review has somewhere to start.
>
> Do not write prompts until they answer. Prompts inherit the theme wholesale, so
> an unapproved theme becomes six unapproved prompts.

## Step 4: Prompts

Load `references/ai-video-prompts.md`.

Build the **style suffix once** from the visual theme and append it to every
shot. That suffix is what makes separate clips read as one film; drift in it is
the most common reason a set does not cut together.

Follow the prompt anatomy in order, keep each prompt to a single line, and never
put text, captions, or logos in the prompt. Those render unreliably and belong
in post.

## Step 5: Validate

Load `references/rubric-short-form-video.md`. Score every line PASS or FAIL with
quoted evidence from your own output. Burden of proof on PASS. Fix, re-score,
**maximum two rounds**. State anything still failing.

This is a self-check against a written standard, not independent review.

## Step 6: Deliver

Script, storyboard, and prompts as three clean blocks, then:

```
Assumed   what you inferred rather than were told
Open      what needs a real asset, a cleared face, or a brand decision
```

Do not show the rubric scoring or the revision rounds.

## Production notes worth raising unprompted

- **Commercial safety.** If this will run as paid advertising or implies a real
  person's likeness, flag it. Prefer a commercial-safe model, frame to avoid
  identifiable faces, or use cleared talent. Do not assume generated output is
  licensed for advertising.
- **Captions in post, always.** Never baked into generated video.
- **Music.** Tempo and texture direction, not a track name you cannot licence.

## Boundaries

This skill does not own adjacent work. When the real problem sits
elsewhere, name the destination and stop rather than half-doing it here.

| If the real problem is | Route to |
|---|---|
| There is no idea yet, only a brief | `campaign-concept` |
| The script is really long-form or written copy | `copywriting` |
| The brand's codes are undefined | `brand-strategy` |

## Sources

Read `references/voice-and-tone.md` when the register of the writing is in question, or before judging whether a draft sounds human.
Read `references/luxury-codes.md` when the brand sits at a premium or luxury tier.
Read `references/persuasion-frameworks.md` when choosing the persuasion structure for a piece.
Read `references/evidence-and-proof.md` before quoting any statistic, benchmark or research finding, and before naming a framework or an expert.

## Gotchas

- **Running past a checkpoint.** Presenting the script and continuing into the
  storyboard in the same reply is not a checkpoint. Stopping and waiting is.
- **Skipping to prompts.** Without a locked theme, four good clips will not cut
  together. This is the most common and most expensive failure.
- **Stacked motion.** Subject, camera and environment all moving in a five-second
  clip renders as mush.
- **Suffix drift.** A slightly different suffix per shot breaks continuity
  invisibly until you assemble.
- **One hook instead of three.**
- **Uniform shot scale.** Four medium shots read flat regardless of content.
- **Two CTAs.**
- **Wrong register.** Direct-response loudness on a premium brand, or precious
  restraint on an impulse product.
- **Text in the prompt.** Produces garbled pseudo-type every time.
- **Assuming a model roster.** These change constantly. Verify what the user's
  account exposes rather than asserting a list.
