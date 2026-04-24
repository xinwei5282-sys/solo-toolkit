---
name: llm-wiki
description: >-
  Use to build and maintain a structured markdown knowledge wiki from research
  sources, PDFs, articles, notes, and web pages; create cross-linked concept
  pages; answer questions against the wiki; and keep durable knowledge in a
  long-lived knowledge base instead of ad hoc chat notes.
---

# LLM Wiki — Karpathy Knowledge Base Pattern

> **Experimental skill — iterating.**
> Authored by Lewis Liu (lylewis@outlook.com) · Inspired by [Karpathy's llm-wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

## Core idea

Instead of RAG (re-retrieving raw docs on every query), the LLM **compiles** raw sources into a persistent, cross-linked wiki. Every ingest, query, lint, and audit pass makes the wiki richer. Knowledge compounds — and the human stays in the loop via a structured feedback channel instead of ad-hoc corrections that get lost.

- **You** own: sourcing raw material, asking good questions, steering direction, filing feedback on anything the AI got wrong.
- **LLM** owns: all writing, cross-referencing, filing, bookkeeping, and acting on your feedback.

The wiki is a living artifact with **five operations** — `compile`, `ingest`, `query`, `lint`, `audit`. Every session starts by reading `CLAUDE.md` and `wiki/index.md`.

## When to use this skill

Use `llm-wiki` when the user needs **durable knowledge**, not just a one-off answer.

Strong fit:

- building a long-lived research base on a topic over days or weeks
- organizing many sources into a reusable, cross-linked knowledge system
- answering questions from an existing wiki and improving the wiki as a side effect
- turning repeated research work into durable concept pages instead of ad hoc notes

Weak fit:

- a one-off summary with no need to preserve the result
- quick factual Q&A where normal browsing or direct reasoning is enough
- small tasks where creating or updating wiki structure would cost more than the knowledge is worth

If the user only needs a temporary answer, prefer a normal response or `summarize`. If they need reusable knowledge, use `llm-wiki`.

## Mode selection

Do not default to the heaviest workflow. Choose the smallest mode that fits:

- **Answer mode**: read the existing wiki and answer from it. Use when the user asks a question against already-ingested knowledge.
- **Ingest mode**: add one or a few sources, update summaries and the most relevant pages. Use for incremental knowledge growth.
- **Compile mode**: restructure, split, merge, and rebuild the wiki. Use only when the wiki has become messy, oversized, or hard to navigate.
- **Maintenance mode**: run `lint` or `audit` to keep quality high. Use when the user wants cleanup or correction processing.

Tie-breakers:

- if no durable artifact is needed yet, do not ingest
- if only one answer is needed, do not compile
- if the wiki structure is still healthy, do not rebuild it just because new material arrived

## Default operating rule

Prefer **answer or incremental ingest first**. Escalate to compile only when structure has clearly drifted.

The default goal is not "do everything the system can do." The default goal is "make the knowledge base meaningfully better at the lowest justified cost."

## Directory layout

```
<wiki-root>/
├── CLAUDE.md          ← Schema: scope, conventions, current articles, gaps
├── log/               ← Per-day operation log (one file per day)
│   ├── 20260409.md
│   └── 20260410.md
├── audit/             ← Human feedback inbox (one file per comment)
│   ├── 20260409-143022-claude-code-size.md
│   └── resolved/      ← Processed feedback, archived with resolution notes
├── raw/               ← Immutable source documents (LLM reads, never writes)
│   ├── articles/
│   ├── papers/
│   ├── notes/
│   └── refs/          ← Pointer files for large binaries kept outside raw/
├── wiki/              ← LLM-generated knowledge (LLM writes, you read)
│   ├── index.md       ← Master catalog — every page, structured by category
│   ├── concepts/      ← Concept/topic pages (split into subfolders when >1200 words)
│   ├── entities/      ← People, tools, papers, organizations
│   └── summaries/     ← Per-source summary pages
└── outputs/
    └── queries/       ← Query answers (promote durable ones to wiki/)
```

`CLAUDE.md` is the **schema file** — the single most important configuration. It tells the LLM the wiki's scope, naming conventions, current article list, open questions, and research gaps. Read `references/schema-guide.md` for what to put in it. Read it at the start of every session.

## Core principles

Four rules govern everything below. If a future instruction contradicts one, flag it to the user before acting.

### 1. Divide and conquer

A single concept page should **never** try to cover a complex topic end-to-end. Target: **400–1200 words per page**. When a topic would blow past that:

- Create a subfolder: `wiki/concepts/<topic>/`
- Put a short index page at `wiki/concepts/<topic>/index.md` — definition, list of sub-pages, one-line summaries
- Put each aspect in its own file: `wiki/concepts/<topic>/<aspect>.md`
- In `wiki/index.md`, show the hierarchy via indented bullets

Example layout (from a real wiki):
```
wiki/tech/claude-code/
├── index.md                         (overview + links to sub-pages)
├── Claude_Code_Architecture.md
├── Claude_Code_Agent_Framework.md
├── Claude_Code_Bridge_System.md
├── Claude_Code_Query_Engine.md
├── Claude_Code_Skills_Plugins.md
├── Claude_Code_State_Management.md
└── Claude_Code_Tool_System.md
```

One fat file covering all seven aspects would be unreadable and unlinkable. Seven focused files + an index page give you navigation, selective reading, clean backlinks, and small audit targets.

### 2. Mermaid for diagrams, KaTeX for formulas

- **Any flow, sequence, hierarchy, or state diagram** must be written in mermaid — never ASCII art. ASCII boxes rot fast and are impossible to annotate.
  ````
  ```mermaid
  flowchart LR
      A[raw/article.md] --> B[summary]
      B --> C[concept page]
      C --> D[index.md]
  ```
  ````
- **Any formula** must be written in KaTeX: inline `$f(x) = \sum_i w_i x_i$` or block `$$...$$`.

Both render in the web viewer (server-side KaTeX, client-side mermaid) and in Obsidian with default settings.

### 3. Raw file policy

Small text-based sources (md, txt, small pdfs, small images) → copy into `raw/<subfolder>/`.

Large binaries (videos, model weights, installers, datasets, large PDFs >10 MB) → **do not copy**. Instead:

- Create a pointer file at `raw/refs/<slug>.md` with:
  ```yaml
  ---
  kind: ref
  external_path: /Volumes/external/models/llama-3-70b/
  size: ~140 GB
  ---
  ```
  followed by a short description of what it is and why it matters to this wiki.
- Wiki pages cite `[[raw/refs/<slug>]]` exactly like any other source.

This keeps the wiki repo git-friendly and portable.

### 4. Audit is the human feedback surface

The wiki is AI-written; it will be wrong sometimes. The raw sources are human-written; they will contradict each other. The `audit/` directory is how humans correct both without losing the corrections in chat history.

- Humans file feedback via the Obsidian plugin or the web viewer. Each feedback is one file in `audit/` with YAML frontmatter (anchor, target, severity) and a markdown body.
- The AI **must** periodically run the `audit` op — never silently ignore `audit/*.md` files.
- When feedback is applied, the file moves to `audit/resolved/` with a `# Resolution` section appended and a log entry recorded in `log/YYYYMMDD.md`.

See `references/audit-guide.md` for the full file format and processing workflow.

---

## The five operations

Every action on the wiki is one of these five. Each appends an entry to the current day's log file (`log/YYYYMMDD.md`).

### 1. `compile`

(Re)structure wiki content from existing `raw/` material — including splitting oversized pages, merging near-duplicates, and rebuilding `index.md`.

**When to run**: after a big ingest batch, when an existing page has outgrown 1200 words, when `index.md` no longer reflects reality, or when the user says "clean up the wiki".

**Steps**:
1. Read `CLAUDE.md`, `wiki/index.md`, and every file in the target subtree.
2. For each page over ~1200 words: plan a split into `concepts/<topic>/` with an index + sub-pages. Confirm the plan with the user before writing.
3. For each pair of near-duplicate pages: propose a merge. Confirm, then rewrite.
4. Regenerate `wiki/index.md` so every page is listed exactly once.
5. Log: `## [HH:MM] compile | <what you did — files touched, splits, merges>`

### 2. `ingest`

Add a new source. **One source typically touches 5–15 wiki pages.**

Use ingest when the source is worth preserving and likely to matter again. Do not ingest disposable reading.

**Steps**:
1. Save source to the right subfolder:
   - web article → `raw/articles/<slug>.md`
   - paper → `raw/papers/<slug>.md` (extracted text for big PDFs)
   - note → `raw/notes/<slug>.md`
   - large binary → `raw/refs/<slug>.md` pointer file (see raw file policy)
2. Read the source in full.
3. Create `wiki/summaries/<slug>.md` (200–400 words — key takeaways, not a rewrite; see `references/article-guide.md`).
4. Create or update relevant concept pages in `wiki/concepts/`. Respect divide-and-conquer: if a concept page would exceed 1200 words, split instead of cramming.
5. Create or update entity pages in `wiki/entities/` for any new people / tools / papers / organizations referenced.
6. Update `wiki/index.md` so the new pages appear under the right category.
7. Log: `## [HH:MM] ingest | <slug> — <one-line description> (touched N pages)`

### 3. `query`

Answer a question **grounded in the wiki**, not general knowledge.

**Steps**:
1. Read `wiki/index.md`. Scan for relevant pages by category.
2. Read the identified pages in full; follow one level of wikilinks.
3. If the wiki doesn't have enough material, say so and suggest what to ingest next instead of making something up.
4. Synthesize the answer, citing pages inline with `[[Page Name]]`.
5. Save to `outputs/queries/<YYYY-MM-DD>-<question-slug>.md`.
6. If the answer is durable (a comparison, analysis, or new synthesis) → promote a cleaned-up version to `wiki/concepts/`, add to `index.md`.
7. Log: `## [HH:MM] query | <question-slug>` (and a separate `## [HH:MM] promote | ...` line if promoted).

Default to saving only when the answer is likely to be reused. Do not promote every decent answer into permanent wiki content.

### 4. `lint`

Health check. Run:

```bash
python3 scripts/lint_wiki.py <wiki-root>
```

The script reports:
- **Dead wikilinks** — `[[Target]]` where `Target.md` doesn't exist
- **Orphan pages** — pages with no inbound wikilinks
- **Missing index entries** — pages not listed in `wiki/index.md`
- **Frequently-linked missing pages** — `[[X]]` referenced 3+ times but no page
- **log/ shape** — stray files or wrong filenames in `log/`
- **audit/ shape** — malformed YAML frontmatter in `audit/*.md`
- **Audit target resolution** — every open audit's `target` file must exist

For each issue, propose a fix, confirm with the user, then apply. Log: `## [HH:MM] lint | <N> issues found, <M> fixed`.

### 5. `audit`

Process human feedback from `audit/`.

**Steps**:
1. Run `python3 scripts/audit_review.py <wiki-root> --open` to get a grouped list.
2. For each open audit, read the file. Use the `anchor_before` / `anchor_text` / `anchor_after` window to locate the exact range in the target file (line numbers may have drifted).
3. Decide the action:
   - **Accept**: apply the correction to the target file.
   - **Partially accept**: apply what makes sense, note the rest in the resolution.
   - **Reject**: explain why in the resolution — the feedback may be based on a misreading of scope or a contradictory source.
   - **Defer**: add to `CLAUDE.md` "Open research questions" and leave the audit in place with a comment.
4. For applied audits, append a `# Resolution` section to the audit file:
   ```markdown
   # Resolution

   2026-04-10 · accepted.
   Fixed the file count (was "~1,900", corrected to "~1,800" per commit abc123).
   Updated: tech/Claude_Code.md lines 47–48.
   ```
5. Move the file from `audit/` to `audit/resolved/`. Filename unchanged.
6. Log per resolved audit:
   ```
   ## [HH:MM] audit | resolved 20260409-143022-a1b2 — <one-line what>
   ```
7. Never delete audit files. Rejected ones still go to `resolved/` with the rejection rationale in their resolution section — that's valuable history.

## Stop rules

Stop and avoid escalating the workflow when:

- the user only needs a one-off answer
- the current question can be answered from existing pages without changing the wiki
- a source is interesting but not yet clearly worth durable storage
- compile would mostly reshuffle files without improving retrieval or understanding

This skill should compound knowledge, not create maintenance churn.

## Checkpoints

Pause and confirm before:

- scaffolding a brand-new wiki
- running a broad compile that will split or merge many pages
- promoting a query answer into permanent wiki content when durability is uncertain
- ingesting a large batch of sources with unclear long-term value

See `references/audit-guide.md` for the full audit file format.

---

## Tooling

| Tool | Purpose |
|------|---------|
| [Obsidian](https://obsidian.md) | IDE for browsing the wiki; graph view shows connections |
| **`plugins/obsidian-audit/`** | Obsidian plugin — select text → add feedback → writes to `audit/` |
| **`web/`** | Local Node.js server — preview the wiki with mermaid/math rendered; select → feedback → `audit/` |
| `scripts/scaffold.py` | Bootstrap a new wiki directory tree |
| `scripts/lint_wiki.py` | Seven-pass health check |
| `scripts/audit_review.py` | Group open/resolved audits by target file |
| [qmd](https://github.com/tobi/qmd) | Optional local semantic search (useful at >100 pages) |

The Obsidian plugin and the web viewer both write audit files in the **same format** with **the same anchor algorithm**, so feedback filed from either place can be resolved by either place.

## Starting a new wiki

```bash
python3 scripts/scaffold.py <wiki-root> "<Topic Title>"
```

Creates the full tree (including `log/<today>.md`, `audit/`, `audit/resolved/`), a blank `CLAUDE.md` based on the new template, and a blank `wiki/index.md` with the recommended category layout.

After scaffolding:
1. Fill in `CLAUDE.md` — define scope, naming conventions, initial research questions.
2. Start ingesting sources.
3. Ask questions to build up `outputs/queries/`; promote durable answers.
4. Run `lint` periodically.
5. Run `audit` whenever new feedback accumulates.

## `wiki/index.md` format

The LLM rebuilds `index.md` on every compile and touches it on every ingest. Format:

```markdown
# Index — <Topic>

> One-sentence scope of the wiki.

## 🔖 Navigation
- [[#Concepts]] · [[#Entities]] · [[#Summaries]] · [[#Open Questions]]

## Concepts
### <Category A>
- [[concepts/Foo]] — one-line summary
- [[concepts/Bar/index|Bar]] — (folder-split) one-line summary
    - [[concepts/Bar/aspect-1]] — ...
    - [[concepts/Bar/aspect-2]] — ...

### <Category B>
- ...

## Entities
- [[entities/Andrej Karpathy]] — AI researcher, author of the llm-wiki pattern

## Summaries (chronological)
- 2026-04-09 — [[summaries/llm-wiki-gist]] — Karpathy's original Gist

## Open Questions
- Q1: ...
```

Rules:
- Every wiki page must appear exactly once in `index.md`. `lint` enforces this.
- Folder-split concepts show hierarchy via indented bullets.
- `index.md` + `CLAUDE.md` together are what the AI reads at session start.

## `log/` format

See `references/log-guide.md` for full details. Minimum:

- One file per day: `log/YYYYMMDD.md`
- H1 = the date; H2 per entry with `## [HH:MM] <op> | <one-line description>`
- Ops: `compile`, `ingest`, `query`, `lint`, `audit`, `promote`, `split`, `scaffold`

Quick grep across history: `grep -rh "^## \[" log/ | tail -20`.

## Use cases

- **Research deep-dive** — reading papers/articles on a topic over weeks; the wiki evolves with your understanding, and the audit trail keeps AI mistakes from silently accumulating
- **Personal wiki** — journal entries, notes, ideas compiled into a personal encyclopedia; comment on anything you disagree with later, the AI corrects it
- **Team knowledge base** — fed by Slack threads, meeting notes, docs; team members file corrections through the web viewer
- **Reading companion** — filing each book chapter as you go; builds a rich companion wiki by the end

## References

- `references/schema-guide.md` — What to put in `CLAUDE.md`
- `references/article-guide.md` — How to write good wiki articles (length, wikilinks, mermaid, math, divide-and-conquer)
- `references/log-guide.md` — The `log/` folder convention
- `references/audit-guide.md` — Audit file format, anchor strategy, processing workflow
- `references/tooling-tips.md` — Obsidian setup, Web Clipper, qmd, plugin + web installation
