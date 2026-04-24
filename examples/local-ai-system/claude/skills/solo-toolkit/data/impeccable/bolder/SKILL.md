---
name: bolder
description: Amplify safe or boring designs to make them more visually interesting and stimulating. Increases impact while maintaining usability. Use when the user says the design looks bland, generic, too safe, lacks personality, or wants more visual impact and character. Use after confirming design context through `frontend-design`, and prefer `quieter`, `arrange`, or `typeset` when the real problem is overstimulation, weak composition, or typographic blandness rather than insufficient boldness.
user-invocable: true
argument-hint: "[target]"
---

Increase visual impact and personality in designs that are too safe, generic, or visually underwhelming, creating more engaging and memorable experiences.

This is an **amplification skill**, not a permission slip for chaos. The goal is sharper emphasis, stronger identity, and more memorable composition.

## MANDATORY PREPARATION

Invoke /frontend-design — it contains design principles, anti-patterns, and the **Context Gathering Protocol**. Follow the protocol before proceeding — if no design context exists yet, you MUST run /teach-impeccable first.

Before making changes, determine whether `bolder` is the right tool:

- Use `bolder` when the interface feels timid, generic, or forgettable.
- Use `quieter` when the interface is already loud and needs restraint.
- Use `arrange` when the screen feels weak because composition and spacing are flat.
- Use `typeset` when blandness comes from generic typography rather than lack of visual courage.
- Use `overdrive` only when the user explicitly wants technically ambitious wow-factor, not just stronger visual taste.

If the main issue is poor structure, do not compensate with louder styling.

## When Not To Push Harder

Do **not** amplify aggressively if:

- the interface is already intense and only lacks refinement
- the domain depends on calm trust and low visual noise
- boldness would compete with semantic states or critical workflows
- the user asked for premium restraint, not spectacle
- the result would become trend-chasing instead of brand-specific

In those cases:
- amplify only one focal point
- fix hierarchy or composition first
- or route into a better-fit skill

## Boldening Workflow

Follow this order:

1. Identify what feels too safe
   Decide whether the problem is:
   - generic typography
   - timid scale
   - low contrast in hierarchy
   - weak color conviction
   - predictable layout
   - lack of focal point

2. Choose the hero move
   Pick one primary amplification vector:
   - typography
   - layout
   - color
   - motion
   - surface treatment

3. Increase contrast selectively
   Make the important things more important:
   - bigger hero moments
   - stronger emphasis
   - more distinctive rhythm
   - sharper differentiation between primary and secondary elements

4. Support the hero move
   Ensure the surrounding system becomes quieter or cleaner where needed so the bold move can land.

5. Verify memorability
   Check that the interface feels more distinctive, not merely more decorated.

---

## Assess Current State

Analyze what makes the design feel too safe or boring:

1. **Identify weakness sources**:
   - **Generic choices**: System fonts, basic colors, standard layouts
   - **Timid scale**: Everything is medium-sized with no drama
   - **Low contrast**: Everything has similar visual weight
   - **Static**: No motion, no energy, no life
   - **Predictable**: Standard patterns with no surprises
   - **Flat hierarchy**: Nothing stands out or commands attention

2. **Understand the context**:
   - What's the brand personality? (How far can we push?)
   - What's the purpose? (Marketing can be bolder than financial dashboards)
   - Who's the audience? (What will resonate?)
   - What are the constraints? (Brand guidelines, accessibility, performance)

If any of these are unclear from the codebase, ask the user directly to clarify what you cannot infer.

**CRITICAL**: "Bolder" doesn't mean chaotic or garish. It means distinctive, memorable, and confident. Think intentional drama, not random chaos.

**WARNING - AI SLOP TRAP**: When making things "bolder," AI defaults to the same tired tricks: cyan/purple gradients, glassmorphism, neon accents on dark backgrounds, gradient text on metrics. These are the OPPOSITE of bold—they're generic. Review ALL the DON'T guidelines in the frontend-design skill before proceeding. Bold means distinctive, not "more effects."

## Boldness Heuristics

Use these tests before increasing visual intensity:

- **Memory test**: Will this make the interface more memorable?
- **Focus test**: Does it clarify what matters most?
- **Originality test**: Is this distinctive for the brand, or just a borrowed trend?
- **Restraint test**: Are we amplifying one hero move or everything at once?
- **Usability test**: Will users still scan and act quickly?

If a move increases noise more than memory, reject it.

## Plan Amplification

Create a strategy to increase impact while maintaining coherence:

- **Focal point**: What should be the hero moment? (Pick ONE, make it amazing)
- **Personality direction**: Maximalist chaos? Elegant drama? Playful energy? Dark moody? Choose a lane.
- **Risk budget**: How experimental can we be? Push boundaries within constraints.
- **Hierarchy amplification**: Make big things BIGGER, small things smaller (increase contrast)

**IMPORTANT**: Bold design must still be usable. Impact without function is just decoration.

Before editing, explicitly write down:

- the one hero moment you are strengthening
- which supporting elements should recede so it can stand out
- what brand character the amplification should express
- what you will avoid so it does not become generic AI slop

If you cannot name the hero move in one sentence, you are probably trying to make too many things louder.

## Amplify the Design

Systematically increase impact across these dimensions:

### Typography Amplification
- **Replace generic fonts**: Swap system fonts for distinctive choices (see frontend-design skill for inspiration)
- **Extreme scale**: Create dramatic size jumps (3x-5x differences, not 1.5x)
- **Weight contrast**: Pair 900 weights with 200 weights, not 600 with 400
- **Unexpected choices**: Variable fonts, display fonts for headlines, condensed/extended widths, monospace as intentional accent (not as lazy "dev tool" default)
- **Selective boldness**: Let one or two type moments carry the drama, not every heading

### Color Intensification
- **Increase saturation**: Shift to more vibrant, energetic colors (but not neon)
- **Bold palette**: Introduce unexpected color combinations—avoid the purple-blue gradient AI slop
- **Dominant color strategy**: Let one bold color own 60% of the design
- **Sharp accents**: High-contrast accent colors that pop
- **Tinted neutrals**: Replace pure grays with tinted grays that harmonize with your palette
- **Rich gradients**: Intentional multi-stop gradients (not generic purple-to-blue)

### Spatial Drama
- **Extreme scale jumps**: Make important elements 3-5x larger than surroundings
- **Break the grid**: Let hero elements escape containers and cross boundaries
- **Asymmetric layouts**: Replace centered, balanced layouts with tension-filled asymmetry
- **Generous space**: Use white space dramatically (100-200px gaps, not 20-40px)
- **Overlap**: Layer elements intentionally for depth

### Visual Effects
- **Dramatic shadows**: Large, soft shadows for elevation (but not generic drop shadows on rounded rectangles)
- **Background treatments**: Mesh patterns, noise textures, geometric patterns, intentional gradients (not purple-to-blue)
- **Texture & depth**: Grain, halftone, duotone, layered elements—NOT glassmorphism (it's overused AI slop)
- **Borders & frames**: Thick borders, decorative frames, custom shapes (not rounded rectangles with colored border on one side)
- **Custom elements**: Illustrative elements, custom icons, decorative details that reinforce brand

### Motion & Animation
- **Entrance choreography**: Staggered, dramatic page load animations with 50-100ms delays
- **Scroll effects**: Parallax, reveal animations, scroll-triggered sequences
- **Micro-interactions**: Satisfying hover effects, click feedback, state changes
- **Transitions**: Smooth, noticeable transitions using ease-out-quart/quint/expo (not bounce or elastic—they cheapen the effect)

### Composition Boldness
- **Hero moments**: Create clear focal points with dramatic treatment
- **Diagonal flows**: Escape horizontal/vertical rigidity with diagonal arrangements
- **Full-bleed elements**: Use full viewport width/height for impact
- **Unexpected proportions**: Golden ratio? Throw it out. Try 70/30, 80/20 splits

### Order Of Operations
- First strengthen the focal point
- Then widen hierarchy contrast
- Then support with color, motion, or texture
- Then remove any extra flourish that does not reinforce the main idea
- Last, check whether one quieter area is needed to make the bold area hit harder

## Checkpoints

Pause and confirm with the user before major amplification when:

- you are changing established brand expression
- you are introducing high-risk visual language the user may not want
- the interface is in a trust-heavy or regulated context
- the request could imply a broader rebrand rather than a local polish pass

If the user only said “make it bolder,” default to:
- choose one strong hero move
- increase hierarchy contrast second
- add effects last

**NEVER**:
- Add effects randomly without purpose (chaos ≠ bold)
- Sacrifice readability for aesthetics (body text must be readable)
- Make everything bold (then nothing is bold - need contrast)
- Ignore accessibility (bold design must still meet WCAG standards)
- Overwhelm with motion (animation fatigue is real)
- Copy trendy aesthetics blindly (bold means distinctive, not derivative)

## Verify Quality

Ensure amplification maintains usability and coherence:

- **NOT AI slop**: Does this look like every other AI-generated "bold" design? If yes, start over.
- **Still functional**: Can users accomplish tasks without distraction?
- **Coherent**: Does everything feel intentional and unified?
- **Memorable**: Will users remember this experience?
- **Performant**: Do all these effects run smoothly?
- **Accessible**: Does it still meet accessibility standards?

Run a final scan:

- Can users tell what the hero moment is immediately?
- Does the boldness feel chosen, not sprayed everywhere?
- If the biggest flourish were removed, would the layout still feel strong?

If not, you used decoration to compensate for weak structure.

## Output Format

When you finish, summarize the result like this:

```md
## Boldening Summary
- Hero move:
- What was amplified:
- What was simplified or quieted to support it:
- Risks checked:
- Follow-up skill if needed:
```

## Fallback

If you are unsure how far to push:

- amplify typography and hierarchy before adding exotic effects
- prefer one unforgettable move over five medium-loud ones
- keep semantic states and usability affordances stable
- use reversible token-level or layout-level changes first

Principle: **when unsure, make the hero stronger, not the whole screen louder.**

**The test**: If you showed this to someone and said "AI made this bolder," would they believe you immediately? If yes, you've failed. Bold means distinctive, not "more AI effects."

Remember: Bold design is confident design. It takes risks, makes statements, and creates memorable experiences. But bold without strategy is just loud. Be intentional, be dramatic, be unforgettable.
