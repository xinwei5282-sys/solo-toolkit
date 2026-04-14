# Solo Toolkit

> One skill to rule them all — for solo founders and one-person companies.

A unified Claude Code skill combining design intelligence, business analytics, market research, startup metrics, and development workflows.

## Install

```bash
npx skills add xinwei5282-sys/solo-toolkit -g -y
```

Or manually:

```bash
git clone https://github.com/xinwei5282-sys/solo-toolkit.git ~/.claude/skills/solo-toolkit
```

## What's Included

### Design Intelligence
- 67 design styles, 96 color palettes, 57 font pairings
- 25 chart types, 13 tech stack guidelines
- BM25 searchable database with Python scripts

### Business Modules
- **Business Analytics** — CSV data analysis with Python engine + HTML report template
- **Market Research** — TAM/SAM/SOM estimation, competitor mapping, persona building
- **Startup Metrics** — CAC, LTV, MRR, ARR, Rule of 40, burn multiple

### Development Workflows (rewritten from gstack methodology)
| Command | What it does |
|---------|-------------|
| `/investigate` | Root-cause debugging with hypothesis testing |
| `/review` | Pre-landing PR review (SQL safety, race conditions, LLM trust) |
| `/ship` | PR creation, CHANGELOG, merge workflow |
| `/qa` | Test → fix → verify loop with health scoring |
| `/office-hours` | YC-style startup diagnosis or builder brainstorming |
| `/plan-review` | CEO / Engineering / Design three-perspective plan review |
| `/design` | Design system creation + visual audit |
| `/retro` | Weekly engineering retrospective with metrics |
| `/document-release` | Post-ship documentation sync |
| `/careful` `/freeze` `/guard` | Safety guardrails for production |

## Structure

```
solo-toolkit/
├── SKILL.md                        # Unified entry point (all triggers)
├── scripts/
│   ├── search.py                   # BM25 design data search
│   ├── core.py                     # Search engine core
│   ├── design_system.py            # Design system generator
│   └── analyze_business_data.py    # Business data analysis
└── data/
    ├── *.csv                       # 11 design data files
    ├── stacks/*.csv                # 13 tech stack guides
    ├── business/                   # Business modules
    │   ├── business_frameworks.md
    │   ├── market-research.md
    │   ├── startup-metrics.md
    │   ├── visualization_guide.md
    │   └── report_template.html
    └── workflows/                  # Development workflows
        ├── investigate.md
        ├── review.md
        ├── ship.md
        ├── qa.md
        ├── office-hours.md
        ├── plan-review.md
        ├── design.md
        ├── retro.md
        ├── document-release.md
        └── safety.md
```

## Example: Local AI System

This repository now also includes an example configuration snapshot under:

```bash
examples/local-ai-system/
```

It captures a layered local AI setup with:

- Claude command roles
- Hermes-style routing skills
- Skills registry and audit workflow
- Structured knowledge wikis for agent systems and trading thesis

This example is meant as a reference architecture, not as the runtime source of truth.

## Pair with OpenClaw Agents

This skill provides **tools**. For **roles** (PM, Developer, Designer, etc.), pair with [OpenClaw](https://openclaw.ai) agents that share personality, methodology, and cross-project experience.

```
Roles (OpenClaw)  → ~/.openclaw/agents/     # who does the work
Skills (this)     → ~/.claude/skills/       # what tools they use
```

## License

MIT
