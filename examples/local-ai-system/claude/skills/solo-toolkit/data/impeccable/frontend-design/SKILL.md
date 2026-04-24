---
name: frontend-design
description: "Use to design and build polished frontend UI for landing pages, dashboards, web apps, components, marketing sites, and interactive screens with production-grade visual quality."
license: Apache 2.0. Based on Anthropic's frontend-design skill. See NOTICE.md for attribution.
---

This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.

## Context Gathering Protocol

Design skills produce generic output without project context. You MUST have confirmed design context before doing any design work.

**Required context** — every design skill needs at minimum:
- **Target audience**: Who uses this product and in what context?
- **Use cases**: What jobs are they trying to get done?
- **Brand personality/tone**: How should the interface feel?

Individual skills may require additional context — check the skill's preparation section for specifics.

**CRITICAL**: You cannot infer this context by reading the codebase. Code tells you what was built, not who it's for or what it should feel like. Only the creator can provide this context.

## Working Modes

Choose the lightest mode that can still produce intentional design:

- **Full direction mode**: use for new pages, major redesigns, or blank-canvas work. Requires explicit audience, use case, and tone.
- **Guided polish mode**: use for improving an existing feature, page, or component when the current product context is already reasonably clear from the user request or project instructions.

In guided polish mode, do not block on perfect brand strategy. You still need enough context to avoid generic output, but you can proceed with a narrower goal: improve the existing interface while preserving the current product lane.

**Gathering order:**
1. **Check current instructions (instant)**: If your loaded instructions already contain a **Design Context** section, proceed immediately.
2. **Check the user request itself (instant)**: If the request already gives enough context for full direction mode or guided polish mode, proceed immediately.
3. **Check .impeccable.md (fast)**: If not in instructions or the request, read `.impeccable.md` from the project root. If it exists and contains the required context, proceed.
4. **Run teach-impeccable (REQUIRED)**: If none of the above sources provide enough context, you MUST run /teach-impeccable NOW before doing anything else. Do NOT skip this step. Do NOT attempt to infer context from the codebase instead.

## Fast Path

You do **not** need to stop for more context when the user has already given enough to make strong design decisions.

Proceed immediately if the request already specifies most of the following:

- product type or surface, such as landing page, dashboard, settings page, pricing page, list view, or onboarding
- target user or business context
- desired feeling, such as premium, calm, editorial, enterprise, playful, or less AI-generated
- scope, such as polish, redesign, or build from scratch

If one element is still fuzzy but the intended lane is obvious, proceed and state the assumption briefly instead of stalling the task.

## When to stop and gather more context

Pause for more context only when the missing information would materially change the visual direction, such as:

- consumer vs enterprise tension
- playful vs serious brand expression
- dashboard polish vs full product repositioning
- marketing page vs application UI ambiguity

If the task is a polish request on an existing product surface, prefer guided polish mode over mandatory re-discovery.

---

## Design Direction

Commit to a BOLD aesthetic direction:
- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work—the key is intentionality, not intensity.

Then implement working code that is:
- Production-grade and functional
- Visually striking and memorable
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

## Frontend Aesthetics Guidelines

### Typography
→ *Consult [typography reference](reference/typography.md) for scales, pairing, and loading strategies.*

Choose fonts that are beautiful, unique, and interesting. Pair a distinctive display font with a refined body font.

**DO**: Use a modular type scale with fluid sizing (clamp)
**DO**: Vary font weights and sizes to create clear visual hierarchy
**DON'T**: Use overused fonts—Inter, Roboto, Arial, Open Sans, system defaults
**DON'T**: Use monospace typography as lazy shorthand for "technical/developer" vibes
**DON'T**: Put large icons with rounded corners above every heading—they rarely add value and make sites look templated

### Color & Theme
→ *Consult [color reference](reference/color-and-contrast.md) for OKLCH, palettes, and dark mode.*

Commit to a cohesive palette. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.

**DO**: Use modern CSS color functions (oklch, color-mix, light-dark) for perceptually uniform, maintainable palettes
**DO**: Tint your neutrals toward your brand hue—even a subtle hint creates subconscious cohesion
**DON'T**: Use gray text on colored backgrounds—it looks washed out; use a shade of the background color instead
**DON'T**: Use pure black (#000) or pure white (#fff)—always tint; pure black/white never appears in nature
**DON'T**: Use the AI color palette: cyan-on-dark, purple-to-blue gradients, neon accents on dark backgrounds
**DON'T**: Use gradient text for "impact"—especially on metrics or headings; it's decorative rather than meaningful
**DON'T**: Default to dark mode with glowing accents—it looks "cool" without requiring actual design decisions

### Layout & Space
→ *Consult [spatial reference](reference/spatial-design.md) for grids, rhythm, and container queries.*

Create visual rhythm through varied spacing—not the same padding everywhere. Embrace asymmetry and unexpected compositions. Break the grid intentionally for emphasis.

**DO**: Create visual rhythm through varied spacing—tight groupings, generous separations
**DO**: Use fluid spacing with clamp() that breathes on larger screens
**DO**: Use asymmetry and unexpected compositions; break the grid intentionally for emphasis
**DON'T**: Wrap everything in cards—not everything needs a container
**DON'T**: Nest cards inside cards—visual noise, flatten the hierarchy
**DON'T**: Use identical card grids—same-sized cards with icon + heading + text, repeated endlessly
**DON'T**: Use the hero metric layout template—big number, small label, supporting stats, gradient accent
**DON'T**: Center everything—left-aligned text with asymmetric layouts feels more designed
**DON'T**: Use the same spacing everywhere—without rhythm, layouts feel monotonous

### Visual Details
**DO**: Use intentional, purposeful decorative elements that reinforce brand
**DON'T**: Use glassmorphism everywhere—blur effects, glass cards, glow borders used decoratively rather than purposefully
**DON'T**: Use rounded elements with thick colored border on one side—a lazy accent that almost never looks intentional
**DON'T**: Use sparklines as decoration—tiny charts that look sophisticated but convey nothing meaningful
**DON'T**: Use rounded rectangles with generic drop shadows—safe, forgettable, could be any AI output
**DON'T**: Use modals unless there's truly no better alternative—modals are lazy

### Motion
→ *Consult [motion reference](reference/motion-design.md) for timing, easing, and reduced motion.*

Focus on high-impact moments: one well-orchestrated page load with staggered reveals creates more delight than scattered micro-interactions.

**DO**: Use motion to convey state changes—entrances, exits, feedback
**DO**: Use exponential easing (ease-out-quart/quint/expo) for natural deceleration
**DO**: For height animations, use grid-template-rows transitions instead of animating height directly
**DON'T**: Animate layout properties (width, height, padding, margin)—use transform and opacity only
**DON'T**: Use bounce or elastic easing—they feel dated and tacky; real objects decelerate smoothly

### Interaction
→ *Consult [interaction reference](reference/interaction-design.md) for forms, focus, and loading patterns.*

Make interactions feel fast. Use optimistic UI—update immediately, sync later.

**DO**: Use progressive disclosure—start simple, reveal sophistication through interaction (basic options first, advanced behind expandable sections; hover states that reveal secondary actions)
**DO**: Design empty states that teach the interface, not just say "nothing here"
**DO**: Make every interactive surface feel intentional and responsive
**DON'T**: Repeat the same information—redundant headers, intros that restate the heading
**DON'T**: Make every button primary—use ghost buttons, text links, secondary styles; hierarchy matters

### Responsive
→ *Consult [responsive reference](reference/responsive-design.md) for mobile-first, fluid design, and container queries.*

**DO**: Use container queries (@container) for component-level responsiveness
**DO**: Adapt the interface for different contexts—don't just shrink it
**DON'T**: Hide critical functionality on mobile—adapt the interface, don't amputate it

### UX Writing
→ *Consult [ux-writing reference](reference/ux-writing.md) for labels, errors, and empty states.*

**DO**: Make every word earn its place
**DON'T**: Repeat information users can already see

---

## The AI Slop Test

**Critical quality check**: If you showed this interface to someone and said "AI made this," would they believe you immediately? If yes, that's the problem.

A distinctive interface should make someone ask "how was this made?" not "which AI made this?"

Review the DON'T guidelines above—they are the fingerprints of AI-generated work from 2024-2025.

---

## 使用方式

当用户说下面这些话时，应优先加载本 skill：

- “帮我做一个更像真实产品的页面”
- “把这个后台界面做得更高级一点”
- “优化这个 dashboard / 看板 / 列表页的视觉和交互”
- “做一个不那么像 AI 的原型 / 展示页”
- “这个页面要有更强的设计感和产品感”
- “把这个组件做得更像产品级界面”
- “帮我把这个界面从能用改成好用、好看、像上线产品”

### 强触发场景

只要用户正在做以下类型的事情，就应优先评估并考虑加载本 skill，而不是先直接进入通用实现：

- 创建或重做 web 页面、组件、看板、仪表盘、原型、展示页
- 优化视觉层级、布局节奏、字体、颜色、动效、交互细节
- 需要明显提升“产品感 / 高级感 / 设计感 / 非 AI 味”
- 需要在功能正确之外，把界面做得更像可上线的真实产品
- 需要在响应式、可访问性、性能约束下同时兼顾审美

如果任务涉及“把功能做出来”和“把界面做漂亮”，优先先用本 skill 定义设计方向，再进入实现。

---

## Implementation Principles

Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details.

Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices across generations.

Remember: the model is capable of extraordinary creative work. Don't hold back—show what can truly be created when thinking outside the box and committing fully to a distinctive vision.

## Checkpoints

Pause and confirm with the user before:

- materially changing the brand expression or visual direction
- choosing between multiple plausible aesthetic directions
- turning a “polish this” request into a full redesign

## Output Format

```md
## Frontend Design Direction
- Audience / use case:
- Aesthetic direction:
- Hero move:
- Key typography / color / layout choices:
- Constraints:
```

## Fallback

If design context is missing or ambiguous:

- use guided polish mode if the product lane is already clear
- gather only the missing context that would change the design direction
- avoid inferring brand personality from code alone
- make only the smallest safe visual decisions until direction is confirmed

Principle: **distinctive execution depends on explicit intent.**
