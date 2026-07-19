# Storyboard

Load when: turning an approved script into a shot-by-shot visual plan.

## Step 1: Lock the shared visual theme

Define **one theme every shot must respect.** Pull it from the brand's visual
system if one exists; otherwise propose a coherent look and say you are
proposing it.

- **Palette.** The three to five controlling colours.
- **Lighting.** Quality, direction, colour temperature.
- **Lens character.** Focal length feel plus depth of field.
- **Film look.** Grain, contrast, grade.
- **Motion language.** The family of camera moves allowed, **and what is banned.**

The banned list matters as much as the allowed list. "Slow dolly, gentle crane,
gimbal float; no whip-pans, no fast cuts" is a usable instruction. "Cinematic" is
not.

This theme becomes the **style suffix** that the prompt stage appends to every
shot. See `ai-video-prompts.md`.

## Step 2: Break into shots

For 15 to 25 seconds, plan **four to six shots**. Default is four by five
seconds for a 20-second piece.

**One main action per shot.** Do not stack subject motion, camera motion and
environment motion into a five-second clip. Fewer, readable beats render far
more reliably in AI video models, and cut better in conventional production too.

Per shot, specify:

| Field | What to write |
|---|---|
| Shot and time | "Shot 2 (5-10s)" |
| Purpose | The beat it serves: hook, immersion, promise, CTA |
| Composition | Framing, subject placement, negative space, vertical |
| Camera move | One move, from the allowed motion language |
| Lighting | How the theme's lighting applies here |
| Subject and action | Who or what, plus the single action that unfolds |
| VO / TEXT | The script line landing on this shot |
| Transition | How it cuts to the next |

## Step 3: Sequence for continuity

- Hold colour and lighting consistent across every shot.
- **Vary shot scale for rhythm** (detail, wide, medium, brand frame) while
  keeping the same visual DNA. Identical scale across four shots reads as flat.
- The first shot must deliver the hook image **within its first second**.
- Reserve the final shot for the brand frame and CTA line, added in post.

## Step 4: Audio and post

- Per-shot sound design cue, only where it matters.
- Music direction: tempo and texture, for the whole piece.
- Caption style, added in post. **Never baked into generated video.**

## Output

```
# Storyboard — [Title]
[20s] · 9:16 · [4] shots × [5]s

## Visual Theme  (becomes the style suffix)
- Palette / Lighting / Lens / Film look
- Motion language: [allowed] | [banned]

## Shots
### Shot 1 (0-5s) — Hook
- Composition / Camera / Lighting
- Subject and action: [single action]
- VO/TEXT: "[line]"
- Transition: [...]

[continue]

## Audio & Post
- Music, sound design, captions, transitions

## Why this works
[2-3 sentences on the logic of the shot order]
```

## Failure modes

1. **No banned-motion list.** "Cinematic" is not direction.
2. **Stacked motion in one shot.** The dominant cause of unusable AI renders.
3. **Uniform shot scale.** Four medium shots read as flat regardless of content.
4. **Hook image arriving late.** If it lands at second three, the scroll already happened.
5. **Text baked into generated video.** Always add in post.
6. **Theme drift.** Shot four lit differently from shot one, so the clips do not read as one film.
7. **More shots than seconds support.** Six shots in 15 seconds gives 2.5s each, too short to read.
