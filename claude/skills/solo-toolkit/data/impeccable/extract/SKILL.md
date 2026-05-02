---
name: extract
description: Extract and consolidate reusable components, design tokens, and patterns into your design system. Identifies opportunities for systematic reuse and enriches your component library. Use when the user asks to create components, refactor repeated UI patterns, build a design system, or extract tokens.
user-invocable: true
argument-hint: "[target]"
---

Identify reusable patterns, components, and design tokens, then extract and consolidate them into the design system for systematic reuse.

Use this when the right move is to turn repeated UI decisions into shared system assets, not just to refactor code for cleanliness.

## Extraction Workflow

Follow this order:

1. identify repeated patterns or values
2. decide whether they deserve extraction now
3. choose the correct shared level:
   - token
   - primitive
   - reusable component
   - documented pattern
4. design the shared API and naming
5. migrate existing usages
6. document and validate the result

## Discover

Analyze the target area to identify extraction opportunities:

1. **Find the design system**: Locate your design system, component library, or shared UI directory (grep for "design system", "ui", "components", etc.). Understand its structure:
   - Component organization and naming conventions
   - Design token structure (if any)
   - Documentation patterns
   - Import/export conventions
   
   **CRITICAL**: If no design system exists, ask before creating one. Understand the preferred location and structure first.

2. **Identify patterns**: Look for:
   - **Repeated components**: Similar UI patterns used multiple times (buttons, cards, inputs, etc.)
   - **Hard-coded values**: Colors, spacing, typography, shadows that should be tokens
   - **Inconsistent variations**: Multiple implementations of the same concept (3 different button styles)
   - **Reusable patterns**: Layout patterns, composition patterns, interaction patterns worth systematizing

3. **Assess value**: Not everything should be extracted. Consider:
   - Is this used 3+ times, or likely to be reused?
   - Would systematizing this improve consistency?
   - Is this a general pattern or context-specific?
   - What's the maintenance cost vs benefit?

## Plan Extraction

Create a systematic extraction plan:

- **Components to extract**: Which UI elements become reusable components?
- **Tokens to create**: Which hard-coded values become design tokens?
- **Variants to support**: What variations does each component need?
- **Naming conventions**: Component names, token names, prop names that match existing patterns
- **Migration path**: How to refactor existing uses to consume the new shared versions

**IMPORTANT**: Design systems grow incrementally. Extract what's clearly reusable now, not everything that might someday be reusable.

Before editing, explicitly write down:

- what is being extracted
- why it deserves extraction now
- where the shared version should live
- what old implementations will be retired

## Choose The Shared Level

Route each opportunity to the smallest shared layer that solves the real problem:

- **Token**: extract when the repeated thing is a value or rule, such as color, spacing, radius, typography, shadow, or motion timing
- **Primitive**: extract when the repeated thing is a low-level building block with stable structure, such as button, input, badge, avatar, stack, or surface
- **Reusable component**: extract when the repeated thing is a composed UI pattern with a clear job and repeated usage, such as stat card, section header, empty state, filter bar, or settings row
- **Documented pattern**: extract when teams need a shared recipe or usage guidance, but the implementation should stay local for now

Use these tie-breakers:

- if the duplication is mostly visual values, prefer tokens first
- if the duplication is mostly structure, props, and accessibility behavior, prefer a primitive or reusable component
- if the pattern is still evolving across contexts, document it before freezing it into code
- if a shared abstraction would need many escape hatches on day one, it is probably too early

## When Not To Extract

Do not extract just because two things look similar.

Avoid extraction when:

- the pattern appears only once or twice with no near-term reuse
- the implementations share appearance but not responsibility
- the abstraction would hide meaningful product differences
- the likely shared API is vague, bloated, or full of boolean switches
- the design system source of truth is still unstable
- the migration cost is high but the consistency win is small

Prefer to wait, document, or only extract tokens when the reuse signal is still weak.

## Extract & Enrich

Build improved, reusable versions:

- **Components**: Create well-designed components with:
  - Clear props API with sensible defaults
  - Proper variants for different use cases
  - Accessibility built in (ARIA, keyboard navigation, focus management)
  - Documentation and usage examples
  
- **Design tokens**: Create tokens with:
  - Clear naming (primitive vs semantic)
  - Proper hierarchy and organization
  - Documentation of when to use each token
  
- **Patterns**: Document patterns with:
  - When to use this pattern
  - Code examples
  - Variations and combinations

**NEVER**:
- Extract one-off, context-specific implementations without generalization
- Create components so generic they're useless
- Extract without considering existing design system conventions
- Skip proper TypeScript types or prop documentation
- Create tokens for every single value (tokens should have semantic meaning)

## Migrate

Replace existing uses with the new shared versions:

- **Find all instances**: Search for the patterns you've extracted
- **Replace systematically**: Update each use to consume the shared version
- **Test thoroughly**: Ensure visual and functional parity
- **Delete dead code**: Remove the old implementations

## Stop Rule

Stop the extraction pass when:

- the highest-value repeated pattern has been consolidated
- the next candidate would require speculative API design
- the remaining differences are intentional product distinctions
- the cleanup starts producing more indirection than clarity

Do not keep extracting just because more similarities can be found. The goal is a cleaner system, not a larger one.

## Document

Update design system documentation:

- Add new components to the component library
- Document token usage and values
- Add examples and guidelines
- Update any Storybook or component catalog

Remember: A good design system is a living system. Extract patterns as they emerge, enrich them thoughtfully, and maintain them consistently.

## Checkpoints

Pause and confirm before:

- creating a new design-system area where none exists
- introducing a shared API with broad usage impact
- deleting several bespoke implementations with uncertain parity
- collapsing patterns that look similar but serve different product jobs

## Output Format

```md
## Extraction Summary
- Pattern extracted:
- Shared level:
- New location:
- Usages migrated:
- Old code removed:
- Risks / follow-up:
```

## Fallback

If extraction value is unclear:

- extract tokens before extracting full components
- document the pattern before codifying it
- prefer reversible refactors over system-wide rewrites
- leave the implementation local and note the reuse signal to revisit later

Principle: **extract proven reuse, not imagined reuse.**
