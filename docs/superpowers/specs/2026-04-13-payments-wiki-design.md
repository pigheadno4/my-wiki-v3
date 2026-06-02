# Payments Industry Research Wiki — Design Spec

## Overview

A personal knowledge base on the payments industry, built using the LLM Wiki pattern. The LLM incrementally builds and maintains a structured, interlinked collection of markdown files as the user ingests sources. The wiki covers major payment players (~5-10), their strengths/weaknesses, and how they compare.

**Domain**: Payments industry research — companies, concepts, comparisons
**Source types**: Web articles, company reports/PDFs, GitHub repos, images, podcast/video notes
**Viewer**: Obsidian (reading, graph view) + VS Code (working with Claude Code)
**Scale**: Focused, ~5-10 major players

## CLAUDE.md Approach

**Fork from the existing `my-wiki` CLAUDE.md** (`/Users/tteng/Development/my-wiki/CLAUDE.md`) and adapt:

### Changes from the existing schema

1. **Drop AI domain** — remove all AI-related guidance, categories, and the "intersection of payments and AI" framing. This wiki is payments-only.
2. **Rename `entities/` to `companies/`** — more intuitive for a payments-focused wiki. Entity frontmatter `category` field simplified (no `person`, `payment-network` etc. unless needed later).
3. **Add `comparisons/` directory** — new first-class page type for side-by-side company analysis. These were previously filed under `analyses/` in the old wiki.
4. **Keep `analyses/`** — for filed query results that aren't comparisons (cross-cutting syntheses, reference tables, guides).
5. **Add `overview.md` seed page** — brief payments industry landscape overview, created at init, revised as wiki grows.
6. **Update directory structure** — reflect `companies/`, `comparisons/`, and `analyses/` directories.

### What carries over unchanged

Everything else from the existing CLAUDE.md is battle-tested and should be preserved:

- **YAML frontmatter** on all page types (`type`, `tags`, `source_count`, `raw_files`, `date_ingested`, `original_format`)
- **Raw file rules** — verbatim content, immutable, tiered strategy table (pasted text, website URL, images, GitHub repos)
- **Large content handling** — don't summarize truncated content, wait for full paste
- **Image handling workflow** — save to `raw/assets/`, embed references, analyze content
- **GitHub repo ingest** — stub file + key excerpts pattern with deep-dive fallback
- **Query workflow** — wiki summaries first, raw file deep-dive with specific triggers, sweep for unlinked raw files, filing criteria
- **Lint workflow** — orphan raw file detection, accuracy spot-checks, missing `raw_files:` frontmatter checks
- **Conventions** — `[[wikilinks]]`, contradiction callouts (`> [!warning]`), evolving callouts (`> [!info]`), slugified filenames, citation style
- **Domain-specific guidance** — adapted for payments-only (payment networks as entities, regulations as concepts, etc.)

## Directory Structure

```
my-wiki-v2/
├── CLAUDE.md              # Schema — forked from my-wiki, adapted
├── raw/                   # Immutable source documents
│   ├── assets/            # Images, downloaded attachments
│   ├── <repo-slug>.md     # GitHub repo stub files
│   └── <repo-slug>/       # GitHub repo key excerpts
├── wiki/                  # LLM-generated and maintained
│   ├── index.md           # Content catalog — pages by category
│   ├── log.md             # Chronological record of operations
│   ├── overview.md        # High-level payments industry overview
│   ├── companies/         # One page per company (e.g. stripe.md)
│   ├── concepts/          # Industry concepts (e.g. interchange-fees.md)
│   ├── comparisons/       # Side-by-side company comparisons
│   ├── analyses/          # Filed query results and syntheses
│   └── sources/           # Source summary pages
└── llm-wiki-idea.md       # Original idea doc (kept for reference)
```

## Page Types

**Company profiles** (`wiki/companies/<company>.md`):
- Frontmatter: `type: company`, `tags`, `source_count`
- Body: overview, key products, pricing model, API/developer experience, market position, pros, cons, notable clients
- Cross-references to concept, comparison, and source pages

**Concept pages** (`wiki/concepts/<concept>.md`):
- Frontmatter: `type: concept`, `category: technology | regulation | trend | framework | standard`, `tags`
- Body: definition, relevance to payments, current state, key players, open questions

**Comparison pages** (`wiki/comparisons/<company-vs-company>.md`):
- Frontmatter: `type: comparison`, `date_created`, `tags`
- Body: side-by-side analysis on specific dimensions, markdown tables, sourced claims

**Analysis pages** (`wiki/analyses/analysis-<title>.md`):
- Frontmatter: `type: analysis`, `date_created`, `tags`
- Body: cross-cutting syntheses, reference tables, filed query results that aren't comparisons

**Source summaries** (`wiki/sources/source-<title>.md`):
- Frontmatter: `type: source`, `date_ingested`, `original_format`, `raw_files`, `tags`
- Body: structured summary with key takeaways, links to company/concept pages

## Seed Content

Three files created on initialization:

- **`wiki/index.md`** — category headers (Companies, Concepts, Comparisons, Analyses, Sources) with no entries yet
- **`wiki/log.md`** — initialized with wiki creation entry
- **`wiki/overview.md`** — brief payments industry landscape (networks, processors, gateways, PSPs, key players). Revised as wiki grows.

## Intentionally Excluded (for now)

- **Search tooling** — index file is sufficient at this scale
- **Marp/slide templates** — can add when presentation output is needed
- **Automation/hooks** — ingest is a manual conversation
- **Git initialization** — user can `git init` when ready
