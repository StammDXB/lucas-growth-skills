# AI Video Prompts

Load when: turning approved storyboard shots into text-to-video or
image-to-video prompts.

Applies to Veo, Runway, Kling, Luma Ray, Sora, Adobe Firefly Video, and any
model using similar grammar. Model rosters change constantly, so verify what
your account currently exposes rather than trusting a remembered list.

## Prompt anatomy, in this order

1. **Shot type / framing.** Extreme close-up, wide establishing, low-angle
   medium, overhead.
2. **Subject plus a distinctive detail.** Concrete specifics (material, texture,
   wardrobe, age) so it does not render generic.
3. **Single action, start to end.** One motion unfolding across the clip.
4. **Setting and time of day.**
5. **One camera move.** Dolly in, slow push, gentle crane, gimbal float, static.
   One only, and only if it serves the shot.
6. **Lighting.** Quality, direction, colour temperature.
7. **Style suffix.** The shared block appended to every shot.

## The rules that actually decide whether it renders

- **One main action per clip.** Do not stack subject motion, camera motion and
  environment motion in a five-second clip. Pick the one that matters, keep the
  others subtle or still. Dense micro-actions break coherence. This is the single
  most common cause of unusable output.
- **Concrete beats generic.** "Brass gooseneck kettle pouring a thin stream of
  water" outperforms "coffee being made."
- **Scope motion to clip length.** For five seconds, one readable beat. Static
  descriptions yield static video, so always include at least one motion cue.
- **No text, captions, or logos in the prompt.** These models render type and
  brand marks unreliably. Add them in post, always.
- **Do not name the model or the duration inside the prompt.** Duration is a
  setting; the model is a UI selection.
- **Single line, no line breaks**, so it pastes cleanly.
- **State vertical framing** in the suffix and compose for a tall frame with
  headroom.

## The style suffix

Build it **once** from the storyboard's visual theme, then append it to every
shot. This is what makes separate clips read as one film.

```
[palette] + [lighting + colour temp] + [lens/DOF] + [film look/grain] + [mood],
cinematic, 9:16 vertical
```

Worked example:

> warm sand-and-bronze palette, golden-hour motivated light ~3500K, 50mm shallow
> depth of field, subtle fine film grain, filmic contrast, serene and refined,
> cinematic, 9:16 vertical

## Image-to-video

When starting from a hero still, which gives the most control over continuity:

- The image anchors identity, wardrobe, composition and palette. Keep those stable.
- The text should drive **motion, camera move, and what changes**, not re-describe
  the scene.
- Example: "the model turns her head slowly toward the window as sheer curtains
  drift in a soft breeze, gentle slow push-in, golden-hour light warming the room,
  [style suffix]"

A reliable continuity workflow: generate one hero still, then image-to-video each
shot from a matching frame.

## Model notes

Treat the grammar above as the default and adapt lightly.

| Model | Adaptation |
|---|---|
| Veo | The template. Rewards a single well-described cinematic shot with clear motion. |
| Runway | Same structure. Make the single camera move explicit, keep subject motion clean. |
| Kling | Strong physical realism. Good for fabric, water, food. Keep motion scoped. |
| Luma Ray | Describe the motion arc start to end clearly. Follows trajectories well. |
| Sora | Handles complex physics. Still one main action per five seconds. Strong on material and fluid realism. |
| Adobe Firefly Video | Keep literal, clean, brand-safe. Short clips, no third-party likeness. Use when commercial safety matters most. |

**Commercial safety.** Where a real person's likeness could be implied, or where
the output will run as paid advertising, prefer a model with a commercial-safety
guarantee, or frame to avoid identifiable faces, or use cleared talent shot
conventionally. Do not assume a model's training data licences the output for
advertising use.

## Worked example

> Extreme close-up overhead shot of a thin stream of hot water pouring from a
> brass gooseneck kettle onto dark coffee grounds in a white ceramic dripper, the
> grounds blooming and rising as steam curls slowly upward, on a marble counter at
> golden hour, slow gentle push-in, warm motivated backlight, warm sand-and-bronze
> palette, golden-hour light ~3500K, 50mm shallow depth of field, subtle fine film
> grain, filmic contrast, serene and refined, cinematic, 9:16 vertical

Note what it does: one subject, one action (steam rising), one camera move (push
in), concrete materials (brass, ceramic, marble), and the suffix carrying
everything shared.

## Output format

Per shot:

```
SHOT [n] — [purpose]  ([t2v|i2v], [model])
Prompt:
[single-line prompt ending with the shared style suffix]
```

Once at the end:

```
STYLE SUFFIX (reused on every shot):
[the suffix]

SETTINGS:
- Model, aspect ratio, clip length, mode
- Continuity note: hero still first, then i2v per shot
```

If the user wants options, give two or three distinct variants per shot, each
self-contained and ending with the same suffix.

## Failure modes

1. **Stacked motion.** Subject moving, camera moving, environment moving. Renders as mush.
2. **Keyword soup.** A list of adjectives instead of a described shot.
3. **Text in the prompt.** Produces garbled pseudo-type.
4. **Suffix drift.** Slightly different suffix per shot, so the clips do not match.
5. **Static description.** No motion cue, so the model returns a near-still.
6. **Duration or model name inside the prompt text.** Wasted tokens, sometimes rendered literally.
7. **Over-length.** Beyond roughly 125 words, models start dropping elements.
