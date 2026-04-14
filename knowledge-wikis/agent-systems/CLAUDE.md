# Agent Systems Knowledge Base

> Schema document — read at the start of every session together with `wiki/index.md`.
> Update after every major compile, ingest batch, or structural change.

## Scope

What this wiki covers:
- Local agent system architecture
- Claude command roles and OpenClaw persona layering
- Global skills, project-private skills, and routing-layer design
- Memory tiering across session context, knowledge-base, and knowledge-wikis
- Hermes-inspired orchestration patterns adapted into the current local stack

What this wiki deliberately excludes:
- Generic AI theory not tied to the local agent system
- Day-to-day product implementation details unless they alter shared agent architecture
- Trading research content that belongs in `trading-thesis`
- UI case studies that belong in project docs or design-focused knowledge stores

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
- `Local Agent Stack`
- `Skills Audit`

### Entities
*(none)*

### Summaries
*(none)*

## Open research questions

- How should routing-layer checks become more automatic instead of purely procedural?
- What is the cleanest migration boundary between `knowledge-base` and `knowledge-wikis`?
- Should project-private skills adopt a shared metadata schema for easier global auditing?

## Research gaps

Sources to ingest:
- [ ] Hermes Agent architecture docs — compare local adaptation choices against upstream runtime design
- [ ] OpenClaw internal docs — clarify migration and coexistence boundaries more explicitly
- [ ] Hindsight memory docs — clarify overlap and separation from structured wiki knowledge

## Audit backlog

*(none — run `python3 scripts/audit_review.py <wiki-root> --open` to refresh)*

## Notes for the LLM

- Language: zh with technical English terms when useful
- Tone: neutral, architectural, explanatory
- Depth: deep technical, but organized for future retrieval
- Handling contradictions: state both, cite each, add to Open Research Questions.
