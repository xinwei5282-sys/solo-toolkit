---
name: quieter
description: Tones down visually aggressive or overstimulating designs, reducing intensity while preserving quality. Use when the user mentions too bold, too loud, overwhelming, aggressive, garish, or wants a calmer, more refined aesthetic. Use after confirming design context through `frontend-design`, and prefer `arrange`, `distill`, or `typeset` when the real problem is spacing, clutter, or typography rather than visual intensity.
user-invocable: true
argument-hint: "[target]"
---

Reduce visual intensity in designs that are too bold, aggressive, or overstimulating, creating a more refined and approachable aesthetic without losing effectiveness.

This is a **refinement skill**, not a flatten-everything skill. The goal is controlled restraint, not loss of hierarchy or personality.

## MANDATORY PREPARATION

Invoke /frontend-design — it contains design principles, anti-patterns, and the **Context Gathering Protocol**. Follow the protocol before proceeding — if no design context exists yet, you MUST run /teach-impeccable first.

Before making changes, determine whether `quieter` is the right tool:

- Use `quieter` when the main problem is overstimulation, not emptiness.
- Use `bolder` when the interface feels generic or underpowered.
- Use `arrange` when the screen feels stressful because spacing and alignment are chaotic.
- Use `distill` when the screen feels loud because there is simply too much stuff.
- Use `typeset` when the main issue is typographic heaviness or poor text hierarchy.

If the interface is already restrained, do not keep reducing intensity just because the user said “make it cleaner.”

## When Not To Quiet Things Down

Do **not** reduce intensity aggressively if:

- the product intentionally needs urgency, energy, or emotional punch
- the design is loud in the hero area on purpose, but calm elsewhere
- the interface is already minimal and the real issue is weak emphasis
- the cuts would erase brand character, status meaning, or key affordances

In those cases:
- preserve the existing energy where it earns its place
- quiet only the excess around it
- or route into a better-fit skill

## Quieting Workflow

Follow this order:

1. Identify the source of overstimulation
   Decide whether the problem comes from:
   - color saturation
   - contrast extremes
   - oversized scale jumps
   - too many bold surfaces
   - decorative overload
   - motion intensity

2. Decide what should stay loud
   Pick the few anchors that still deserve emphasis: hero, primary CTA, critical status, or section headline.

3. Reduce intensity in layers
   Quiet the supporting system first:
   - secondary colors
   - decorative effects
   - redundant motion
   - heavy borders / shadows
   - over-bold typography

4. Rebuild hierarchy through restraint
   Make sure the remaining emphasis is clearer after the supporting noise is reduced.

5. Verify the result
   Check that the interface feels calmer, but still confident and readable.

---

## Assess Current State

Analyze what makes the design feel too intense:

1. **Identify intensity sources**:
   - **Color saturation**: Overly bright or saturated colors
   - **Contrast extremes**: Too much high-contrast juxtaposition
   - **Visual weight**: Too many bold, heavy elements competing
   - **Animation excess**: Too much motion or overly dramatic effects
   - **Complexity**: Too many visual elements, patterns, or decorations
   - **Scale**: Everything is large and loud with no hierarchy

2. **Understand the context**:
   - What's the purpose? (Marketing vs tool vs reading experience)
   - Who's the audience? (Some contexts need energy)
   - What's working? (Don't throw away good ideas)
   - What's the core message? (Preserve what matters)

If any of these are unclear from the codebase, ask the user directly to clarify what you cannot infer.

**CRITICAL**: "Quieter" doesn't mean boring or generic. It means refined, sophisticated, and easier on the eyes. Think luxury, not laziness.

## Quieting Heuristics

Use these tests before reducing an element:

- **Fatigue test**: Does this element create visual exhaustion over repeated use?
- **Competition test**: Is it fighting with more important content?
- **Necessity test**: Does this intensity communicate meaning, or just presence?
- **Brand test**: Is this loudness part of the product's identity?
- **Affordance test**: Would toning this down make the UI less obvious to use?

If an element is intense but passes meaning and affordance tests, reduce surrounding noise instead of muting the element itself.

## Plan Refinement

Create a strategy to reduce intensity while maintaining impact:

- **Color approach**: Desaturate or shift to more sophisticated tones?
- **Hierarchy approach**: Which elements should stay bold (very few), which should recede?
- **Simplification approach**: What can be removed entirely?
- **Sophistication approach**: How can we signal quality through restraint?

**IMPORTANT**: Great quiet design is harder than great bold design. Subtlety requires precision.

Before editing, explicitly write down:

- what remains as the primary emphasis
- which colors or effects will be softened
- which elements must remain high-contrast for usability
- what personality cues should survive the cleanup

If you cannot state what will remain strong, you are likely about to over-flatten the design.

## Refine the Design

Systematically reduce intensity across these dimensions:

### Color Refinement
- **Reduce saturation**: Shift from fully saturated to 70-85% saturation
- **Soften palette**: Replace bright colors with muted, sophisticated tones
- **Reduce color variety**: Use fewer colors more thoughtfully
- **Neutral dominance**: Let neutrals do more work, use color as accent (10% rule)
- **Gentler contrasts**: High contrast only where it matters most
- **Tinted grays**: Use warm or cool tinted grays instead of pure gray—adds sophistication without loudness
- **Never gray on color**: If you have gray text on a colored background, use a darker shade of that color or transparency instead

### Visual Weight Reduction
- **Typography**: Reduce font weights (900 → 600, 700 → 500), decrease sizes where appropriate
- **Hierarchy through subtlety**: Use weight, size, and space instead of color and boldness
- **White space**: Increase breathing room, reduce density
- **Borders & lines**: Reduce thickness, decrease opacity, or remove entirely
- **Fewer simultaneous accents**: Limit how many elements are trying to feel “important” at once

### Simplification
- **Remove decorative elements**: Gradients, shadows, patterns, textures that don't serve purpose
- **Simplify shapes**: Reduce border radius extremes, simplify custom shapes
- **Reduce layering**: Flatten visual hierarchy where possible
- **Clean up effects**: Reduce or remove blur effects, glows, multiple shadows

### Motion Reduction
- **Reduce animation intensity**: Shorter distances (10-20px instead of 40px), gentler easing
- **Remove decorative animations**: Keep functional motion, remove flourishes
- **Subtle micro-interactions**: Replace dramatic effects with gentle feedback
- **Refined easing**: Use ease-out-quart for smooth, understated motion—never bounce or elastic
- **Remove animations entirely** if they're not serving a clear purpose

### Composition Refinement
- **Reduce scale jumps**: Smaller contrast between sizes creates calmer feeling
- **Align to grid**: Bring rogue elements back into systematic alignment
- **Even out spacing**: Replace extreme spacing variations with consistent rhythm
- **Use emptiness intentionally**: Quiet design often comes from fewer competing signals, not just desaturated colors

### Order Of Operations
- First reduce decorative noise
- Then soften secondary color and weight
- Then calm motion and effects
- Then rebalance hierarchy
- Last, restore one or two intentional moments of emphasis if the result became too flat

## Checkpoints

Pause and confirm with the user before major quieting when:

- you are muting established brand colors
- you are removing dramatic hero treatments the user may value
- the interface depends on strong status signaling
- the request could imply a rebrand rather than refinement

If the user only said “tone it down,” default to:
- reduce secondary noise first
- preserve primary emphasis second
- only then soften dominant brand expression

**NEVER**:
- Make everything the same size/weight (hierarchy still matters)
- Remove all color (quiet ≠ grayscale)
- Eliminate all personality (maintain character through refinement)
- Sacrifice usability for aesthetics (functional elements still need clear affordances)
- Make everything small and light (some anchors needed)

## Verify Quality

Ensure refinement maintains quality:

- **Still functional**: Can users still accomplish tasks easily?
- **Still distinctive**: Does it have character, or is it generic now?
- **Better reading**: Is text easier to read for extended periods?
- **Sophistication**: Does it feel more refined and premium?

Run a final scan:

- Can users still spot the primary action quickly?
- Are important states still unmistakable?
- Does the screen feel calmer because noise is gone, not because meaning is gone?

If not, reintroduce emphasis selectively.

## Output Format

When you finish, summarize the result like this:

```md
## Quieting Summary
- Primary emphasis preserved:
- Noise reduced:
- Color / motion / weight changes:
- Risks checked:
- Follow-up skill if needed:
```

## Fallback

If you are unsure how far to quiet the interface:

- reduce decorative effects before reducing functional emphasis
- mute secondary colors before touching semantic colors
- prefer reversible token changes over one-off restyling
- stop once the main task feels calm and legible

Principle: **when unsure, quiet the background, not the signal.**

Remember: Quiet design is confident design. It doesn't need to shout. Less is more, but less is also harder. Refine with precision and maintain intentionality.
