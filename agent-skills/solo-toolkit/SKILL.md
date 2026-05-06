---
name: solo-toolkit
description: "Toolkit for solo founders covering UI design guidance, frontend implementation patterns, business analytics, market research, startup metrics, and practical review workflows across web and mobile products."
---
# Solo Toolkit — 一人公司能力工具箱

Comprehensive design guide for web and mobile applications. Contains 67 styles, 96 color palettes, 57 font pairings, 99 UX guidelines, and 25 chart types across 13 technology stacks. Searchable database with priority-based recommendations.

## When to Apply

Reference these guidelines when:
- Designing new UI components or pages
- Choosing color palettes and typography
- Reviewing code for UX issues
- Building landing pages or dashboards
- Implementing accessibility requirements

## Rule Categories by Priority

| Priority | Category | Impact | Domain |
|----------|----------|--------|--------|
| 1 | Accessibility | CRITICAL | `ux` |
| 2 | Touch & Interaction | CRITICAL | `ux` |
| 3 | Performance | HIGH | `ux` |
| 4 | Layout & Responsive | HIGH | `ux` |
| 5 | Typography & Color | MEDIUM | `typography`, `color` |
| 6 | Animation | MEDIUM | `ux` |
| 7 | Style Selection | MEDIUM | `style`, `product` |
| 8 | Charts & Data | LOW | `chart` |

## Quick Reference

### 1. Accessibility (CRITICAL)

- `color-contrast` - Minimum 4.5:1 ratio for normal text
- `focus-states` - Visible focus rings on interactive elements
- `alt-text` - Descriptive alt text for meaningful images
- `aria-labels` - aria-label for icon-only buttons
- `keyboard-nav` - Tab order matches visual order
- `form-labels` - Use label with for attribute

### 2. Touch & Interaction (CRITICAL)

- `touch-target-size` - Minimum 44x44px touch targets
- `hover-vs-tap` - Use click/tap for primary interactions
- `loading-buttons` - Disable button during async operations
- `error-feedback` - Clear error messages near problem
- `cursor-pointer` - Add cursor-pointer to clickable elements

### 3. Performance (HIGH)

- `image-optimization` - Use WebP, srcset, lazy loading
- `reduced-motion` - Check prefers-reduced-motion
- `content-jumping` - Reserve space for async content
- `text-layout-perf` - Use Pretext for DOM-free text measurement in virtualized lists and text-heavy UIs

### 4. Layout & Responsive (HIGH)

- `viewport-meta` - width=device-width initial-scale=1
- `readable-font-size` - Minimum 16px body text on mobile
- `horizontal-scroll` - Ensure content fits viewport width
- `z-index-management` - Define z-index scale (10, 20, 30, 50)

### 5. Typography & Color (MEDIUM)

- `line-height` - Use 1.5-1.75 for body text
- `line-length` - Limit to 65-75 characters per line
- `font-pairing` - Match heading/body font personalities

### 6. Animation (MEDIUM)

- `duration-timing` - Use 150-300ms for micro-interactions
- `transform-performance` - Use transform/opacity, not width/height
- `loading-states` - Skeleton screens or spinners

### 7. Style Selection (MEDIUM)

- `style-match` - Match style to product type
- `consistency` - Use same style across all pages
- `no-emoji-icons` - Use SVG icons, not emojis

### 8. Charts & Data (LOW)

- `chart-type` - Match chart type to data type
- `color-guidance` - Use accessible color palettes
- `data-table` - Provide table alternative for accessibility

## How to Use

Search specific domains using the CLI tool below.

---


## Prerequisites

Check if Python is installed:

```bash
python3 --version || python --version
```

If Python is not installed, install it based on user's OS:

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3
```

**Windows:**
```powershell
winget install Python.Python.3.12
```

---

## How to Use This Skill

When user requests UI/UX work (design, build, create, implement, review, fix, improve), follow this workflow:

### Step 1: Analyze User Requirements

Extract key information from user request:
- **Product type**: SaaS, e-commerce, portfolio, dashboard, landing page, etc.
- **Style keywords**: minimal, playful, professional, elegant, dark mode, etc.
- **Industry**: healthcare, fintech, gaming, education, etc.
- **Stack**: React, Vue, Next.js, or default to `html-tailwind`

### Step 2: Generate Design System (REQUIRED)

**Always start with `--design-system`** to get comprehensive recommendations with reasoning:

```bash
python3 skills/solo-toolkit/scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```

This command:
1. Searches 5 domains in parallel (product, style, color, landing, typography)
2. Applies reasoning rules from `ui-reasoning.csv` to select best matches
3. Returns complete design system: pattern, style, colors, typography, effects
4. Includes anti-patterns to avoid

**Example:**
```bash
python3 skills/solo-toolkit/scripts/search.py "beauty spa wellness service" --design-system -p "Serenity Spa"
```

### Step 2b: Persist Design System (Master + Overrides Pattern)

To save the design system for hierarchical retrieval across sessions, add `--persist`:

```bash
python3 skills/solo-toolkit/scripts/search.py "<query>" --design-system --persist -p "Project Name"
```

This creates:
- `design-system/MASTER.md` — Global Source of Truth with all design rules
- `design-system/pages/` — Folder for page-specific overrides

**With page-specific override:**
```bash
python3 skills/solo-toolkit/scripts/search.py "<query>" --design-system --persist -p "Project Name" --page "dashboard"
```

This also creates:
- `design-system/pages/dashboard.md` — Page-specific deviations from Master

**How hierarchical retrieval works:**
1. When building a specific page (e.g., "Checkout"), first check `design-system/pages/checkout.md`
2. If the page file exists, its rules **override** the Master file
3. If not, use `design-system/MASTER.md` exclusively

### Step 3: Supplement with Detailed Searches (as needed)

After getting the design system, use domain searches to get additional details:

```bash
python3 skills/solo-toolkit/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**When to use detailed searches:**

| Need | Domain | Example |
|------|--------|---------|
| More style options | `style` | `--domain style "glassmorphism dark"` |
| Chart recommendations | `chart` | `--domain chart "real-time dashboard"` |
| UX best practices | `ux` | `--domain ux "animation accessibility"` |
| Alternative fonts | `typography` | `--domain typography "elegant luxury"` |
| Landing structure | `landing` | `--domain landing "hero social-proof"` |

### Step 4: Stack Guidelines (Default: html-tailwind)

Get implementation-specific best practices. If user doesn't specify a stack, **default to `html-tailwind`**.

```bash
python3 skills/solo-toolkit/scripts/search.py "<keyword>" --stack html-tailwind
```

Available stacks: `html-tailwind`, `react`, `nextjs`, `vue`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`, `jetpack-compose`

---

## Search Reference

### Available Domains

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `product` | Product type recommendations | SaaS, e-commerce, portfolio, healthcare, beauty, service |
| `style` | UI styles, colors, effects | glassmorphism, minimalism, dark mode, brutalism |
| `typography` | Font pairings, Google Fonts | elegant, playful, professional, modern |
| `color` | Color palettes by product type | saas, ecommerce, healthcare, beauty, fintech, service |
| `landing` | Page structure, CTA strategies | hero, hero-centric, testimonial, pricing, social-proof |
| `chart` | Chart types, library recommendations | trend, comparison, timeline, funnel, pie |
| `ux` | Best practices, anti-patterns | animation, accessibility, z-index, loading |
| `react` | React/Next.js performance | waterfall, bundle, suspense, memo, rerender, cache |
| `web` | Web interface guidelines | aria, focus, keyboard, semantic, virtualize |
| `prompt` | AI prompts, CSS keywords | (style name) |

### Available Stacks

| Stack | Focus |
|-------|-------|
| `html-tailwind` | Tailwind utilities, responsive, a11y (DEFAULT) |
| `react` | State, hooks, performance, patterns |
| `nextjs` | SSR, routing, images, API routes |
| `vue` | Composition API, Pinia, Vue Router |
| `svelte` | Runes, stores, SvelteKit |
| `swiftui` | Views, State, Navigation, Animation |
| `react-native` | Components, Navigation, Lists |
| `flutter` | Widgets, State, Layout, Theming |
| `shadcn` | shadcn/ui components, theming, forms, patterns |
| `jetpack-compose` | Composables, Modifiers, State Hoisting, Recomposition |

---

## Example Workflow

**User request:** "Làm landing page cho dịch vụ chăm sóc da chuyên nghiệp"

### Step 1: Analyze Requirements
- Product type: Beauty/Spa service
- Style keywords: elegant, professional, soft
- Industry: Beauty/Wellness
- Stack: html-tailwind (default)

### Step 2: Generate Design System (REQUIRED)

```bash
python3 skills/solo-toolkit/scripts/search.py "beauty spa wellness service elegant" --design-system -p "Serenity Spa"
```

**Output:** Complete design system with pattern, style, colors, typography, effects, and anti-patterns.

### Step 3: Supplement with Detailed Searches (as needed)

```bash
# Get UX guidelines for animation and accessibility
python3 skills/solo-toolkit/scripts/search.py "animation accessibility" --domain ux

# Get alternative typography options if needed
python3 skills/solo-toolkit/scripts/search.py "elegant luxury serif" --domain typography
```

### Step 4: Stack Guidelines

```bash
python3 skills/solo-toolkit/scripts/search.py "layout responsive form" --stack html-tailwind
```

**Then:** Synthesize design system + detailed searches and implement the design.

---

## Output Formats

The `--design-system` flag supports two output formats:

```bash
# ASCII box (default) - best for terminal display
python3 skills/solo-toolkit/scripts/search.py "fintech crypto" --design-system

# Markdown - best for documentation
python3 skills/solo-toolkit/scripts/search.py "fintech crypto" --design-system -f markdown
```

---

## Tips for Better Results

1. **Be specific with keywords** - "healthcare SaaS dashboard" > "app"
2. **Search multiple times** - Different keywords reveal different insights
3. **Combine domains** - Style + Typography + Color = Complete design system
4. **Always check UX** - Search "animation", "z-index", "accessibility" for common issues
5. **Use stack flag** - Get implementation-specific best practices
6. **Iterate** - If first search doesn't match, try different keywords

---

## Common Rules for Professional UI

These are frequently overlooked issues that make UI look unprofessional:

### Icons & Visual Elements

| Rule | Do | Don't |
|------|----|----- |
| **No emoji icons** | Use SVG icons (Heroicons, Lucide, Simple Icons) | Use emojis like 🎨 🚀 ⚙️ as UI icons |
| **Stable hover states** | Use color/opacity transitions on hover | Use scale transforms that shift layout |
| **Correct brand logos** | Research official SVG from Simple Icons | Guess or use incorrect logo paths |
| **Consistent icon sizing** | Use fixed viewBox (24x24) with w-6 h-6 | Mix different icon sizes randomly |

### Interaction & Cursor

| Rule | Do | Don't |
|------|----|----- |
| **Cursor pointer** | Add `cursor-pointer` to all clickable/hoverable cards | Leave default cursor on interactive elements |
| **Hover feedback** | Provide visual feedback (color, shadow, border) | No indication element is interactive |
| **Smooth transitions** | Use `transition-colors duration-200` | Instant state changes or too slow (>500ms) |

### Light/Dark Mode Contrast

| Rule | Do | Don't |
|------|----|----- |
| **Glass card light mode** | Use `bg-white/80` or higher opacity | Use `bg-white/10` (too transparent) |
| **Text contrast light** | Use `#0F172A` (slate-900) for text | Use `#94A3B8` (slate-400) for body text |
| **Muted text light** | Use `#475569` (slate-600) minimum | Use gray-400 or lighter |
| **Border visibility** | Use `border-gray-200` in light mode | Use `border-white/10` (invisible) |

### Layout & Spacing

| Rule | Do | Don't |
|------|----|----- |
| **Floating navbar** | Add `top-4 left-4 right-4` spacing | Stick navbar to `top-0 left-0 right-0` |
| **Content padding** | Account for fixed navbar height | Let content hide behind fixed elements |
| **Consistent max-width** | Use same `max-w-6xl` or `max-w-7xl` | Mix different container widths |

---

## Pre-Delivery Checklist

Before delivering UI code, verify these items:

### Visual Quality
- [ ] No emojis used as icons (use SVG instead)
- [ ] All icons from consistent icon set (Heroicons/Lucide)
- [ ] Brand logos are correct (verified from Simple Icons)
- [ ] Hover states don't cause layout shift
- [ ] Use theme colors directly (bg-primary) not var() wrapper

### Interaction
- [ ] All clickable elements have `cursor-pointer`
- [ ] Hover states provide clear visual feedback
- [ ] Transitions are smooth (150-300ms)
- [ ] Focus states visible for keyboard navigation

### Light/Dark Mode
- [ ] Light mode text has sufficient contrast (4.5:1 minimum)
- [ ] Glass/transparent elements visible in light mode
- [ ] Borders visible in both modes
- [ ] Test both modes before delivery

### Layout
- [ ] Floating elements have proper spacing from edges
- [ ] No content hidden behind fixed navbars
- [ ] Responsive at 375px, 768px, 1024px, 1440px
- [ ] No horizontal scroll on mobile

### Accessibility
- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] Color is not the only indicator
- [ ] `prefers-reduced-motion` respected

---

## Business Analytics Module

When analyzing business sales/revenue data from CSV files:

1. **Load data**: Ask user for CSV file path, explore columns and structure
2. **Run analysis**: `python3 skills/solo-toolkit/scripts/analyze_business_data.py <csv_path>`
3. **Interpret results**: Current state, weak areas, root causes, impact assessment
4. **Generate recommendations**: Strategic initiatives with expected impact and timeline
5. **Create report**: Use template at `skills/solo-toolkit/data/business/report_template.html`

Reference frameworks: `skills/solo-toolkit/data/business/business_frameworks.md`
Visualization guide: `skills/solo-toolkit/data/business/visualization_guide.md`

## Market Research Module

When conducting market research, follow the structured playbook at:
`skills/solo-toolkit/data/business/market-research.md`

Key steps: Define questions → Market sizing (TAM/SAM/SOM) → Free data sources → Competitor mapping → Trend analysis → Customer personas → Compile report

## Startup Metrics Module

When tracking/analyzing startup metrics, reference the comprehensive framework at:
`skills/solo-toolkit/data/business/startup-metrics.md`

Covers: Revenue metrics (MRR/ARR) → Unit economics (CAC/LTV) → Cash efficiency → SaaS/Marketplace/Consumer/B2B specific metrics → Stage-appropriate benchmarks

---

## Workflow Modules

### /investigate — 调试与根因分析
When debugging errors, fixing bugs, or investigating unexpected behavior:
Read: `skills/solo-toolkit/data/workflows/investigate.md`

### /review — 合并前代码审查
When reviewing PRs, checking diffs, or pre-landing review:
Read: `skills/solo-toolkit/data/workflows/review.md`

### /ship — 部署与 PR 工作流
When shipping, deploying, creating PRs, or merging:
Read: `skills/solo-toolkit/data/workflows/ship.md`

### /qa — 测试与修复
When QA testing, finding bugs, or testing a site:
Read: `skills/solo-toolkit/data/workflows/qa.md`

### /office-hours — 头脑风暴
When brainstorming ideas, validating concepts, or "is this worth building":
Read: `skills/solo-toolkit/data/workflows/office-hours.md`

### /plan-review — 计划审查（CEO / 工程 / 设计三视角）
When reviewing plans, architecture, or design decisions:
Read: `skills/solo-toolkit/data/workflows/plan-review.md`

### /design — 设计系统创建 & 视觉审查
When creating design systems, auditing designs, or visual QA:
Read: `skills/solo-toolkit/data/workflows/design.md`

### /retro — 周度复盘
When doing weekly retrospectives or reviewing what was shipped:
Read: `skills/solo-toolkit/data/workflows/retro.md`

### /document-release — 发版文档同步
When updating docs after shipping, syncing documentation:
Read: `skills/solo-toolkit/data/workflows/document-release.md`

### /careful /freeze /guard — 安全模式
When working with production, destructive commands, or restricting edits:
Read: `skills/solo-toolkit/data/workflows/safety.md`

---

## Text Layout Library: Pretext

When building text-heavy UIs, virtualized lists, or need DOM-free text measurement:
Read: `skills/solo-toolkit/data/pretext-reference.md`

**Quick install:** `npm install @chenglou/pretext`

**When to recommend Pretext:**
- Virtualized lists/feeds with variable-height text items
- Chat apps, editors, comment sections needing precise height calculation
- Canvas/SVG text rendering
- Preventing layout thrashing in performance-critical UIs
- Text overflow detection without DOM measurements
- Editorial layouts with text wrapping around floated elements

**Playground:** `/Users/weiran/pretext-playground/` (installed and ready to use)

---

## Impeccable — 前端设计质量系统

基于 Impeccable (by Paul Bakaus) 的前端设计质量工具集，消除 AI slop，提升 UI 品质。

### 核心参考

#### /frontend-design — 设计原则与反模式参考
When building web components, pages, or applications with high design quality:
Read: `skills/solo-toolkit/data/impeccable/frontend-design/SKILL.md`
Reference files in: `skills/solo-toolkit/data/impeccable/frontend-design/reference/`

#### /teach-impeccable — 项目设计上下文初始化
When setting up design context for a new project (one-time setup):
Read: `skills/solo-toolkit/data/impeccable/teach-impeccable/SKILL.md`

### 审查与评估

#### /audit — 技术质量审查
When running accessibility, performance, theming, responsive, and anti-pattern checks:
Read: `skills/solo-toolkit/data/impeccable/audit/SKILL.md`

#### /critique — UX 设计评审
When evaluating design quality with quantitative scoring (Nielsen heuristics):
Read: `skills/solo-toolkit/data/impeccable/critique/SKILL.md`
Reference files in: `skills/solo-toolkit/data/impeccable/critique/reference/`

### 排版与配色

#### /typeset — 排版优化
When improving typography, font choices, hierarchy, sizing, and readability:
Read: `skills/solo-toolkit/data/impeccable/typeset/SKILL.md`

#### /colorize — 配色优化
When adding color to monochromatic designs or improving color strategy:
Read: `skills/solo-toolkit/data/impeccable/colorize/SKILL.md`

### 布局与结构

#### /arrange — 布局与间距优化
When fixing layout, spacing, visual rhythm, and monotonous grids:
Read: `skills/solo-toolkit/data/impeccable/arrange/SKILL.md`

#### /adapt — 响应式适配
When adapting designs for different screen sizes, devices, and contexts:
Read: `skills/solo-toolkit/data/impeccable/adapt/SKILL.md`

### 风格调节

#### /polish — 最终润色
When doing final quality pass before shipping (alignment, spacing, consistency):
Read: `skills/solo-toolkit/data/impeccable/polish/SKILL.md`

#### /bolder — 加强设计感
When amplifying safe or boring designs to be more visually interesting:
Read: `skills/solo-toolkit/data/impeccable/bolder/SKILL.md`

#### /quieter — 降低视觉强度
When toning down overstimulating designs while preserving quality:
Read: `skills/solo-toolkit/data/impeccable/quieter/SKILL.md`

### 动效与交互

#### /animate — 动效增强
When adding purposeful animations and micro-interactions:
Read: `skills/solo-toolkit/data/impeccable/animate/SKILL.md`

#### /delight — 趣味体验
When adding moments of joy, personality, and memorable touches:
Read: `skills/solo-toolkit/data/impeccable/delight/SKILL.md`

#### /overdrive — 极致效果
When pushing interfaces past conventional limits (shaders, spring physics, scroll-driven):
Read: `skills/solo-toolkit/data/impeccable/overdrive/SKILL.md`

### 内容与文案

#### /clarify — UX 文案优化
When improving error messages, labels, microcopy, and instructions:
Read: `skills/solo-toolkit/data/impeccable/clarify/SKILL.md`

#### /onboard — 引导流程设计
When designing onboarding flows, empty states, and first-run experiences:
Read: `skills/solo-toolkit/data/impeccable/onboard/SKILL.md`

### 工程质量

#### /optimize — 性能优化
When diagnosing and fixing UI performance (loading, rendering, animations):
Read: `skills/solo-toolkit/data/impeccable/optimize/SKILL.md`

#### /harden — 健壮性增强
When improving error handling, i18n, text overflow, and edge cases:
Read: `skills/solo-toolkit/data/impeccable/harden/SKILL.md`

### 重构与提取

#### /distill — 精简设计
When stripping designs to their essence by removing unnecessary complexity:
Read: `skills/solo-toolkit/data/impeccable/distill/SKILL.md`

#### /extract — 提取设计系统
When extracting reusable components, design tokens, and patterns:
Read: `skills/solo-toolkit/data/impeccable/extract/SKILL.md`

#### /normalize — 规范化对齐
When realigning UI to match design system standards and tokens:
Read: `skills/solo-toolkit/data/impeccable/normalize/SKILL.md`
