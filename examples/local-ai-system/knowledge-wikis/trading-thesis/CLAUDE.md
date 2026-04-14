# Trading Thesis Knowledge Base

> Schema document — read at the start of every session together with `wiki/index.md`.
> Update after every major compile, ingest batch, or structural change.

## Scope

What this wiki covers:
- Trading theses for stocks, sectors, and recurring market patterns
- Company, sector, catalyst, and risk concept pages that support long-term decision quality
- Durable research notes that should outlive a single trading day
- Links between strategy concepts, market structure, and individual theses

What this wiki deliberately excludes:
- Pure intraday chatter and disposable trade notes
- Broker execution logs or account bookkeeping
- Generic investing education unless it directly supports a thesis in this wiki
- Software development and agent-system knowledge

## Operations

This wiki follows the llm-wiki skill's five operations: `compile`, `ingest`, `query`, `lint`, `audit`.
Every operation appends an entry to `log/YYYYMMDD.md`.

## Naming conventions

- **Concept pages** (`wiki/concepts/`): Title Case noun phrases.
- **Folder-split concepts** (`wiki/concepts/<topic>/`): used when a topic exceeds ~1200 words. Contains `index.md` + one file per aspect.
- **Entity pages** (`wiki/entities/`): Proper names.
- **Summary pages** (`wiki/summaries/`): kebab-case source slug.

All pages require YAML frontmatter: `title`, `type`, `created`, `updated`, `sources`, `tags`.

### Diagrams and formulas
- All diagrams are **mermaid**. No ASCII art.
- All formulas are **KaTeX** (inline `$...$` or block `$$...$$`).

### Raw file policy
- Small text sources → copy into `raw/<subfolder>/`.
- Large binaries → create a pointer file at `raw/refs/<slug>.md` with `kind: ref` and `external_path` fields. Do not copy the binary.

## Current articles

This list must stay aligned with `wiki/index.md`.

### Concepts
- `Trading Thesis Framework`
- `Risk Triggers`
- `Catalyst Tracking`

### Entities
*(none)*

### Summaries
*(none)*

## Open research questions

- What makes a thesis durable enough to promote from notes into a concept or entity page?
- How should sector-level research link to individual company theses?
- What is the cleanest boundary between daily technical analysis and long-term thesis maintenance?

## Research gaps

Sources to ingest:
- [ ] Existing personal market notes — baseline material for the first concept pages
- [ ] A sample company thesis note — used to define entity-page structure
- [ ] A reusable risk checklist — used to standardize downside tracking

## Audit backlog

*(none — run `python3 scripts/audit_review.py <wiki-root> --open` to refresh)*

## Notes for the LLM

- Language: zh with English ticker and finance terms when necessary
- Tone: analytical, concise, decision-support oriented
- Depth: medium-to-deep, focused on usable investment reasoning
- Handling contradictions: state both, cite each, add to Open Research Questions.
