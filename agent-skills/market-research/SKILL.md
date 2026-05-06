---
name: market-research
description: "Use for market research, market sizing, customer segment analysis, industry trends, demand validation, TAM/SAM/SOM, and landscape scans before product strategy or planning."
phase: discover
version: "2.1.0"
updated: 2026-04-24
license: Apache-2.0
metadata:
  category: research
  frameworks: [triple-diamond, lean-startup, design-thinking]
  author: product-on-purpose
---
<!-- PM-Skills | https://github.com/product-on-purpose/pm-skills | Apache 2.0 -->
# Market Research

Market research clarifies whether a market is attractive, how it is segmented, what customers actually need, and where real demand or white space may exist. Unlike a competitor-focused brief, market research starts with the market itself: customer problems, demand signals, market structure, growth drivers, and strategic implications.

## When to Use

- Before entering a new market or category
- When validating whether a product idea addresses real demand
- When sizing a market before planning roadmap or GTM strategy
- When identifying customer segments and their distinct needs
- During strategy reviews to understand market direction and timing
- When a team needs market context before doing competitor analysis

## When Not to Use

- If the main goal is feature-by-feature competitor comparison, use `competitive-brief`
- If the user only wants a one-off summary of a source, use `summarize`
- If the output should become a long-lived topic library, pair with `llm-wiki`

## Instructions

When asked to conduct market research, follow these steps:

1. **Define the Research Scope**
   Clarify the market, geography, customer segment, and time horizon. Distinguish whether the ask is about total market attractiveness, a narrow wedge, customer demand, or category trends.

2. **Map the Customer and Problem**
   Identify key customer segments, the jobs they are trying to get done, their current alternatives, and the pain points that matter enough to drive adoption or spending.

3. **Estimate Market Size**
   Develop TAM / SAM / SOM or another clearly stated sizing approach. Be explicit about whether estimates are top-down, bottom-up, or analogy-based. Show assumptions and confidence levels.

4. **Analyze Market Structure**
   Describe the category shape: incumbent types, substitute solutions, buyer roles, procurement model, pricing norms, and major barriers to entry.

5. **Assess Demand Signals**
   Look for evidence of urgency and willingness to pay: search trends, customer complaints, review patterns, job postings, funding, regulation changes, migration behavior, or workflow pain.

6. **Identify Trends and Tailwinds**
   Summarize major shifts shaping the market: technology changes, macro forces, policy, buyer behavior, distribution changes, or cost structure shifts.

7. **Extract Strategic Implications**
   Translate observations into action: whether to enter, what wedge to choose, which segment to prioritize, what risks to watch, and what questions still need validation.

8. **Note Confidence Levels**
   Separate verified facts from inference. Market research often combines hard data with directional judgment; make that boundary visible.

## Output Format

Use the template in `references/TEMPLATE.md` to structure the output.

## Quality Checklist

Before finalizing, verify:

- [ ] Scope is clearly defined (market, segment, geography, time horizon)
- [ ] Customer segments and problems are explicitly described
- [ ] Market size method and assumptions are shown
- [ ] Trends are specific and relevant, not generic filler
- [ ] Demand signals are evidence-based where possible
- [ ] Strategic implications are actionable, not just descriptive
- [ ] Sources and confidence levels are documented

## Examples

See `references/EXAMPLE.md` for a completed example.

## Checkpoints

Pause and confirm with the user before:

- narrowing the market scope more tightly than the user implied
- turning a market scan into a competitor brief
- presenting speculative sizing as if it were verified

## Output Format

At minimum, structure the response around:

```md
## Market Research Summary
- Market definition:
- Target segment:
- Market size method:
- Demand signals:
- Key trends:
- Strategic implications:
- Confidence / unknowns:
```

## Fallback

If the market boundary or available evidence is unclear:

- make the scope narrower, not broader
- separate hard data from directional inference
- state which assumptions need validation next

Principle: **honest directional research is more useful than fake precision.**
