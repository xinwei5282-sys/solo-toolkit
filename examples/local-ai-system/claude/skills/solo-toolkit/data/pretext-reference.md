# Pretext — Text Layout Library Reference

> Pure JavaScript/TypeScript library for measuring and laying out multiline text without DOM measurements.
> By chenglou. GitHub: https://github.com/chenglou/pretext

## When to Recommend

- Text-heavy UIs requiring precise height calculation (chat apps, editors, comment sections)
- Virtualized lists/feeds with variable-height text items
- Canvas/SVG text rendering (games, diagrams, custom renderers)
- Preventing layout thrashing / reflows in performance-critical scenarios
- Text overflow detection without DOM measurements
- Manual line-by-line text layout (text wrapping around images, editorial layouts)

## Installation

```bash
npm install @chenglou/pretext
```

## Core API

### `prepare(text, font, fontSize, lineHeight, width, options?)`
One-time text analysis and measurement. Returns a prepared object for fast subsequent layout calls.
- ~19ms for initial analysis
- Font must be a loaded web font or system font (avoid `system-ui` on macOS)

### `layout(prepared, width)`
Pure arithmetic height calculation. Returns the total height of the text block.
- ~0.09ms per call (200x faster than DOM measurement)
- Width can differ from the `prepare()` call

### `prepareWithSegments(text, font, fontSize, lineHeight, width)`
Rich structure for manual layouts. Returns line-level data with text content, width, and cursor positions.

### `layoutWithLines(prepared, width)` / `walkLineRanges(prepared, width)` / `layoutNextLine(prepared, width)`
Line-by-line control for custom rendering.

## Key Features

| Feature | Detail |
|---------|--------|
| Performance | ~0.09ms per layout (pure arithmetic, no DOM) |
| Language Support | All languages, emojis, bidirectional text (Arabic, Hebrew) |
| Render Targets | DOM, Canvas, SVG |
| Line Control | Access individual line data for custom rendering |
| No Reflows | Prevents layout thrashing in virtualization |
| Modes | `normal` (default) and `pre-wrap` (textarea-like) |

## Usage Patterns

### 1. Height Measurement Without DOM

```typescript
import { prepare, layout } from '@chenglou/pretext';

const prepared = prepare(text, 'Inter', 16, 24, containerWidth);
const height = layout(prepared, containerWidth);
// Use height for virtualization, animation, etc.
```

### 2. Virtualized List with Variable-Height Items

```typescript
// Pre-measure all items without rendering
const heights = items.map(item => {
  const prepared = prepare(item.text, font, fontSize, lineHeight, width);
  return layout(prepared, width);
});
// Feed heights to virtual scroller
```

### 3. Text Wrapping Around Floated Elements

```typescript
import { prepareWithSegments } from '@chenglou/pretext';

const segments = prepareWithSegments(text, font, fontSize, lineHeight, width);
// Manually lay out lines, adjusting width per line to avoid floated image
```

### 4. Text Overflow Detection

```typescript
const prepared = prepare(text, font, fontSize, lineHeight, width);
const actualHeight = layout(prepared, width);
const isOverflowing = actualHeight > maxHeight;
```

## Limitations

- Targets standard text config: `white-space: normal`, `word-break: normal`, `overflow-wrap: break-word`
- `pre-wrap` mode available for textarea-like behavior
- Avoid `system-ui` font on macOS (inconsistent metrics)
- Requires font to be loaded before `prepare()` call

## Demo Patterns (from chenglou.me/pretext/)

- **Accordion** — Smooth height animation without layout thrashing
- **Bubbles** — Chat-like variable-width text measurement
- **Dynamic Layout** — Text reflowing around floating elements
- **Editorial Engine** — Full editorial text layout
- **Justification Comparison** — Text justification algorithms
- **Rich Text** — Rich text with inline styles
- **Masonry** — Text-aware masonry grid layout
