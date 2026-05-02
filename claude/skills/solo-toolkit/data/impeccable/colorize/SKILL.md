---
name: colorize
description: Add strategic color to features that are too monochromatic or lack visual interest, making interfaces more engaging and expressive. Use when the user mentions the design looking gray, dull, lacking warmth, needing more color, or wanting a more vibrant or expressive palette. Use after confirming design context through `frontend-design`, and prefer `quieter`, `typeset`, or `arrange` when the real problem is intensity, typography, or hierarchy rather than lack of color.
user-invocable: true
argument-hint: "[target]"
---

Strategically introduce color to designs that are too monochromatic, gray, or lacking in visual warmth and personality.

This is a **purposeful color introduction skill**, not a license to make everything louder. Use it to improve meaning, hierarchy, and emotional tone.

## MANDATORY PREPARATION

Invoke /frontend-design — it contains design principles, anti-patterns, and the **Context Gathering Protocol**. Follow the protocol before proceeding — if no design context exists yet, you MUST run /teach-impeccable first. Additionally gather: existing brand colors.

Before changing anything, determine whether `colorize` is the correct tool:

- Use `colorize` when the interface lacks warmth, contrast of emphasis, or memorable visual identity.
- Use `quieter` when the interface is already too saturated or visually aggressive.
- Use `typeset` when the screen feels dull because hierarchy is weak, not because color is missing.
- Use `arrange` when the screen feels flat because spacing and composition are weak.

If the root problem is not color, do not paper over it with accent paint.

## When Not To Add More Color

Do **not** increase color intensity aggressively if:

- the brand already relies on restrained or editorial minimalism
- the interface is a dense productivity tool where too much color will hurt scanability
- the current problem is clutter, not monotony
- the added color would compete with alerts, status states, or existing semantics
- the interface already has enough color but uses it inconsistently

In those cases, either:
- refine and normalize the existing palette, or
- route into a better-fit skill.

## Colorization Workflow

Follow this order:

1. Identify the current color failure
   Decide whether the interface is suffering from:
   - no color
   - timid color
   - inconsistent color
   - color without meaning

2. Define the job of color
   Decide what color should do here:
   - improve hierarchy
   - communicate state
   - create warmth
   - establish brand memory
   - separate sections or categories

3. Choose a compact palette
   Pick one dominant color family, one supporting family if needed, and one high-contrast accent only if justified.

4. Apply color in priority order
   Start with high-leverage surfaces first:
   - primary actions
   - interactive states
   - semantic states
   - key headings / labels
   - subtle surface tints
   Decorative color comes last, not first.

5. Verify restraint
   Confirm that color improved clarity without making the screen noisier.

---

## Assess Color Opportunity

Analyze the current state and identify opportunities:

1. **Understand current state**:
   - **Color absence**: Pure grayscale? Limited neutrals? One timid accent?
   - **Missed opportunities**: Where could color add meaning, hierarchy, or delight?
   - **Context**: What's appropriate for this domain and audience?
   - **Brand**: Are there existing brand colors we should use?

2. **Identify where color adds value**:
   - **Semantic meaning**: Success (green), error (red), warning (yellow/orange), info (blue)
   - **Hierarchy**: Drawing attention to important elements
   - **Categorization**: Different sections, types, or states
   - **Emotional tone**: Warmth, energy, trust, creativity
   - **Wayfinding**: Helping users navigate and understand structure
   - **Delight**: Moments of visual interest and personality

If any of these are unclear from the codebase, ask the user directly to clarify what you cannot infer.

**CRITICAL**: More color ≠ better. Strategic color beats rainbow vomit every time. Every color should have a purpose.

## Color Heuristics

Use these tests before introducing a new hue:

- **Meaning test**: Does this color communicate something useful?
- **Hierarchy test**: Does it direct attention to the right place?
- **Consistency test**: Will this meaning stay stable across the product?
- **Restraint test**: Is there already enough color on screen?
- **Contrast test**: Will this remain legible and accessible?

If a proposed color fails most tests, do not add it.

## Plan Color Strategy

Create a purposeful color introduction plan:

- **Color palette**: What colors match the brand/context? (Choose 2-4 colors max beyond neutrals)
- **Dominant color**: Which color owns 60% of colored elements?
- **Accent colors**: Which colors provide contrast and highlights? (30% and 10%)
- **Application strategy**: Where does each color appear and why?

**IMPORTANT**: Color should enhance hierarchy and meaning, not create chaos. Less is more when it matters more.

Before editing, explicitly write down:

- dominant color family
- semantic colors you will keep or introduce
- where color will stay neutral on purpose
- which existing gray surfaces should remain gray

If you cannot name where color should *not* go, your palette is probably too broad.

## Introduce Color Strategically

Add color systematically across these dimensions:

### Semantic Color
- **State indicators**:
  - Success: Green tones (emerald, forest, mint)
  - Error: Red/pink tones (rose, crimson, coral)
  - Warning: Orange/amber tones
  - Info: Blue tones (sky, ocean, indigo)
  - Neutral: Gray/slate for inactive states

- **Status badges**: Colored backgrounds or borders for states (active, pending, completed, etc.)
- **Progress indicators**: Colored bars, rings, or charts showing completion or health

### Accent Color Application
- **Primary actions**: Color the most important buttons/CTAs
- **Links**: Add color to clickable text (maintain accessibility)
- **Icons**: Colorize key icons for recognition and personality
- **Headers/titles**: Add color to section headers or key labels
- **Hover states**: Introduce color on interaction
- **Selection states**: Active nav items, tabs, and selected filters can carry stronger color than idle states

### Background & Surfaces
- **Tinted backgrounds**: Replace pure gray (`#f5f5f5`) with warm neutrals (`oklch(97% 0.01 60)`) or cool tints (`oklch(97% 0.01 250)`)
- **Colored sections**: Use subtle background colors to separate areas
- **Gradient backgrounds**: Add depth with subtle, intentional gradients (not generic purple-blue)
- **Cards & surfaces**: Tint cards or surfaces slightly for warmth

**Use OKLCH for color**: It's perceptually uniform, meaning equal steps in lightness *look* equal. Great for generating harmonious scales.

### Data Visualization
- **Charts & graphs**: Use color to encode categories or values
- **Heatmaps**: Color intensity shows density or importance
- **Comparison**: Color coding for different datasets or timeframes

### Borders & Accents
- **Accent borders**: Add colored left/top borders to cards or sections
- **Underlines**: Color underlines for emphasis or active states
- **Dividers**: Subtle colored dividers instead of gray lines
- **Focus rings**: Colored focus indicators matching brand

### Typography Color
- **Colored headings**: Use brand colors for section headings (maintain contrast)
- **Highlight text**: Color for emphasis or categories
- **Labels & tags**: Small colored labels for metadata or categories

### Decorative Elements
- **Illustrations**: Add colored illustrations or icons
- **Shapes**: Geometric shapes in brand colors as background elements
- **Gradients**: Colorful gradient overlays or mesh backgrounds
- **Blobs/organic shapes**: Soft colored shapes for visual interest

Decorative color is allowed only after hierarchy, semantics, and interaction states already feel correct.

## Balance & Refinement

Ensure color addition improves rather than overwhelms:

### Maintain Hierarchy
- **Dominant color** (60%): Primary brand color or most used accent
- **Secondary color** (30%): Supporting color for variety
- **Accent color** (10%): High contrast for key moments
- **Neutrals** (remaining): Gray/black/white for structure

### Accessibility
- **Contrast ratios**: Ensure WCAG compliance (4.5:1 for text, 3:1 for UI components)
- **Don't rely on color alone**: Use icons, labels, or patterns alongside color
- **Test for color blindness**: Verify red/green combinations work for all users

### Cohesion
- **Consistent palette**: Use colors from defined palette, not arbitrary choices
- **Systematic application**: Same color meanings throughout (green always = success)
- **Temperature consistency**: Warm palette stays warm, cool stays cool

### Order Of Operations
- First fix semantic state colors
- Then fix primary interaction emphasis
- Then tint surfaces and neutrals
- Then tune decorative accents
- Last, remove any extra color that no longer earns its place

**NEVER**:
- Use every color in the rainbow (choose 2-4 colors beyond neutrals)
- Apply color randomly without semantic meaning
- Put gray text on colored backgrounds—it looks washed out; use a darker shade of the background color or transparency instead
- Use pure gray for neutrals—add subtle color tint (warm or cool) for sophistication
- Use pure black (`#000`) or pure white (`#fff`) for large areas
- Violate WCAG contrast requirements
- Use color as the only indicator (accessibility issue)
- Make everything colorful (defeats the purpose)
- Default to purple-blue gradients (AI slop aesthetic)

## Checkpoints

Pause and confirm with the user before major palette shifts when:

- you are changing established brand colors
- you are repurposing existing semantic meanings
- the interface is in a regulated or operational domain where color carries real status meaning
- the request implies a rebrand rather than a feature polish

If the user asked only for “more color,” default to:
- improve emphasis first
- warm up neutrals second
- add decorative color last

## Verify Color Addition

Test that colorization improves the experience:

- **Better hierarchy**: Does color guide attention appropriately?
- **Clearer meaning**: Does color help users understand states/categories?
- **More engaging**: Does the interface feel warmer and more inviting?
- **Still accessible**: Do all color combinations meet WCAG standards?
- **Not overwhelming**: Is color balanced and purposeful?

Run a final scan:

- Can a user identify the primary action in under 2 seconds?
- Do status colors still read instantly?
- If decorative accents were removed, would the screen still work?

If the answer to the last question is no, you used decoration to cover a hierarchy problem.

## Output Format

When you finish, summarize the decision like this:

```md
## Colorization Summary
- Dominant palette:
- Semantic colors:
- Where color was added:
- Where neutrality was preserved:
- Accessibility / risk check:
- Follow-up skill if needed:
```

## Fallback

If brand guidance is missing or palette confidence is low:

- keep semantic colors conventional
- tint neutrals subtly rather than introducing many saturated accents
- avoid rebranding the product by accident
- prefer reversible token-level changes over ad hoc one-off colors

Principle: **when unsure, add meaning before adding intensity.**

Remember: Color is emotional and powerful. Use it to create warmth, guide attention, communicate meaning, and express personality. But restraint and strategy matter more than saturation and variety. Be colorful, but be intentional.
