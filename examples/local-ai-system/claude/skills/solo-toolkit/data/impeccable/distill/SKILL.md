---
name: distill
description: Strip designs to their essence by removing unnecessary complexity. Great design is simple, powerful, and clean. Use when the user asks to simplify, declutter, reduce noise, remove elements, reduce cognitive load, or make a UI cleaner and more focused. Use after confirming design context through `frontend-design`, and prefer routing into `clarify`, `arrange`, `normalize`, or `harden` when the real problem is copy, layout drift, consistency, or resilience rather than excess.
user-invocable: true
argument-hint: "[target]"
---

This skill removes unnecessary complexity from designs, revealing the essential elements and creating clarity through ruthless simplification.

It is a **reduction skill**, not a blank-slate redesign skill. Use it when the right answer is "less, clearer, tighter," not "more expressive" or "more ambitious."

## MANDATORY PREPARATION

Invoke /frontend-design — it contains design principles, anti-patterns, and the **Context Gathering Protocol**. Follow the protocol before proceeding — if no design context exists yet, you MUST run /teach-impeccable first.

Before making changes, also determine whether `distill` is the right tool:

- Use `distill` when the interface has too much stuff.
- Use `clarify` when the main problem is confusing copy.
- Use `arrange` when the main problem is spacing, alignment, and composition.
- Use `normalize` when the main problem is design-system drift.
- Use `harden` when the main problem is overflow, edge cases, and production robustness.

If the problem is mixed, you may still start with `distill`, but explicitly separate what you will remove here versus what another skill should clean up next.

## When To Refuse Simplification

Do **not** simplify aggressively if any of these are true:

- The domain is inherently complex and users need dense information to do their job.
- The interface is already minimal, and the real issue is poor hierarchy rather than excess.
- The user asked for expressive, editorial, premium, or high-drama design rather than reduction.
- The proposed cuts would hide critical controls, warnings, status, or compliance information.

In those cases, say simplification would create regression and either:
- reduce only presentation noise, or
- route into a more appropriate skill.

## Distillation Workflow

Follow this sequence in order:

1. Confirm the primary task
   Identify the single most important user goal on the screen. If there are multiple competing goals, rank them.

2. Audit everything on screen
   Categorize each major section, control, or content block as:
   - essential
   - supportive
   - distracting
   - redundant

3. Choose the reduction strategy
   Decide whether each non-essential item should be:
   - removed
   - hidden behind progressive disclosure
   - merged with another element
   - demoted visually

4. Simplify without breaking the task
   Apply reductions across information architecture, layout, visual styling, copy, and interaction flow.

5. Verify the result
   Check that the main task became faster, clearer, and lower-friction without losing critical capability.

6. Report what changed
   Summarize what was removed, what was retained, and why.

## Assess Current State

Analyze what makes the design feel complex or cluttered:

1. **Identify complexity sources**:
   - **Too many elements**: Competing buttons, redundant information, visual clutter
   - **Excessive variation**: Too many colors, fonts, sizes, styles without purpose
   - **Information overload**: Everything visible at once, no progressive disclosure
   - **Visual noise**: Unnecessary borders, shadows, backgrounds, decorations
   - **Confusing hierarchy**: Unclear what matters most
   - **Feature creep**: Too many options, actions, or paths forward

2. **Find the essence**:
   - What's the primary user goal? (There should be ONE)
   - What's actually necessary vs nice-to-have?
   - What can be removed, hidden, or combined?
   - What's the 20% that delivers 80% of value?

If any of these are unclear from the codebase, ask the user directly to clarify what you cannot infer.

**CRITICAL**: Simplicity is not about removing features - it's about removing obstacles between users and their goals. Every element should justify its existence.

## Distillation Heuristics

Use these tests while deciding what to cut:

- **Duplication test**: Is this information already visible elsewhere?
- **Decision test**: Does this element help the user make a real decision?
- **Frequency test**: Is this used often enough to deserve prime real estate?
- **Urgency test**: Does the user need this before completing the primary task?
- **Comprehension test**: Would removing this make the screen easier to parse in 3 seconds?

If an element fails most tests, it should probably be removed or demoted.

## Plan Simplification

Create a ruthless editing strategy:

- **Core purpose**: What's the ONE thing this should accomplish?
- **Essential elements**: What's truly necessary to achieve that purpose?
- **Progressive disclosure**: What can be hidden until needed?
- **Consolidation opportunities**: What can be combined or integrated?

**IMPORTANT**: Simplification is hard. It requires saying no to good ideas to make room for great execution. Be ruthless.

Before editing, write down:

- the primary action
- the 1-3 supporting actions that must remain visible
- the items you intend to remove, merge, or hide

If you cannot state those clearly, you are not ready to simplify yet.

## Simplify the Design

Systematically remove complexity across these dimensions:

### Information Architecture
- **Reduce scope**: Remove secondary actions, optional features, redundant information
- **Progressive disclosure**: Hide complexity behind clear entry points (accordions, modals, step-through flows)
- **Combine related actions**: Merge similar buttons, consolidate forms, group related content
- **Clear hierarchy**: ONE primary action, few secondary actions, everything else tertiary or hidden
- **Remove redundancy**: If it's said elsewhere, don't repeat it here
- **One screen, one job**: If a screen is trying to do multiple unrelated jobs, separate them

### Visual Simplification
- **Reduce color palette**: Use 1-2 colors plus neutrals, not 5-7 colors
- **Limit typography**: One font family, 3-4 sizes maximum, 2-3 weights
- **Remove decorations**: Eliminate borders, shadows, backgrounds that don't serve hierarchy or function
- **Flatten structure**: Reduce nesting, remove unnecessary containers—never nest cards inside cards
- **Remove unnecessary cards**: Cards aren't needed for basic layout; use spacing and alignment instead
- **Consistent spacing**: Use one spacing scale, remove arbitrary gaps

### Layout Simplification
- **Linear flow**: Replace complex grids with simple vertical flow where possible
- **Remove sidebars**: Move secondary content inline or hide it
- **Full-width**: Use available space generously instead of complex multi-column layouts
- **Consistent alignment**: Pick left or center, stick with it
- **Generous white space**: Let content breathe, don't pack everything tight
- **Fewer containers**: Prefer spacing and headings over wrappers, dividers, and boxes

### Interaction Simplification
- **Reduce choices**: Fewer buttons, fewer options, clearer path forward (paradox of choice is real)
- **Smart defaults**: Make common choices automatic, only ask when necessary
- **Inline actions**: Replace modal flows with inline editing where possible
- **Remove steps**: Can signup be one step instead of three? Can checkout be simplified?
- **Clear CTAs**: ONE obvious next step, not five competing actions

### Content Simplification
- **Shorter copy**: Cut every sentence in half, then do it again
- **Active voice**: "Save changes" not "Changes will be saved"
- **Remove jargon**: Plain language always wins
- **Scannable structure**: Short paragraphs, bullet points, clear headings
- **Essential information only**: Remove marketing fluff, legalese, hedging
- **Remove redundant copy**: No headers restating intros, no repeated explanations, say it once

### Code Simplification
- **Remove unused code**: Dead CSS, unused components, orphaned files
- **Flatten component trees**: Reduce nesting depth
- **Consolidate styles**: Merge similar styles, use utilities consistently
- **Reduce variants**: Does that component need 12 variations, or can 3 cover 90% of cases?

## Checkpoints

Pause and confirm with the user before making high-impact cuts when:

- you are removing visible features rather than only reducing presentation noise
- you are hiding advanced controls behind disclosure
- you suspect different user segments rely on the dense version
- the interface touches admin, finance, medical, legal, or operational workflows

If the user did not ask for destructive feature reduction, default to:
- remove redundancy first
- demote secondary content second
- hide advanced options third
- delete capabilities last

**NEVER**:
- Remove necessary functionality (simplicity ≠ feature-less)
- Sacrifice accessibility for simplicity (clear labels and ARIA still required)
- Make things so simple they're unclear (mystery ≠ minimalism)
- Remove information users need to make decisions
- Eliminate hierarchy completely (some things should stand out)
- Oversimplify complex domains (match complexity to actual task complexity)

## Verify Simplification

Ensure simplification improves usability:

- **Faster task completion**: Can users accomplish goals more quickly?
- **Reduced cognitive load**: Is it easier to understand what to do?
- **Still complete**: Are all necessary features still accessible?
- **Clearer hierarchy**: Is it obvious what matters most?
- **Better performance**: Does simpler design load faster?

Run a final "3-second scan":

- If a new user glanced at the screen for 3 seconds, would they know:
  - what this screen is for?
  - what to do first?
  - what matters most?

If not, keep simplifying or reintroduce structure where clarity was lost.

## Document Removed Complexity

If you removed features or options:
- Document why they were removed
- Consider if they need alternative access points
- Note any user feedback to monitor

Use this output format:

```md
## Distillation Summary
- Primary task:
- Removed:
- Hidden / deferred:
- Kept visible:
- Risk check:
- Next recommended cleanup skill:
```

## Fallback

If context is missing or the right cuts are unclear:

- do not guess the product strategy
- simplify only obvious redundancy and noise
- leave a note about what requires user confirmation
- prefer reversible changes over irreversible removal

Principle: **when unsure, reduce surface noise first, not capability.**

Remember: You have great taste and judgment. Simplification is an act of confidence - knowing what to keep and courage to remove the rest. As Antoine de Saint-Exupéry said: "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away."
