# Payments Wiki Setup — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Set up a payments industry research wiki by forking the existing `my-wiki` CLAUDE.md schema, creating the directory structure, and writing seed content.

**Architecture:** Fork-and-adapt approach. The existing `my-wiki/CLAUDE.md` is a battle-tested schema covering ingest/query/lint workflows, raw file handling, frontmatter conventions, and GitHub repo ingestion. We fork it, drop the AI domain, rename `entities/` to `companies/`, add `comparisons/` as a page type, and write three seed wiki pages.

**Tech Stack:** Markdown, Obsidian-compatible wikilinks, YAML frontmatter

**Spec:** `docs/superpowers/specs/2026-04-13-payments-wiki-design.md`

---

### Task 1: Create directory structure

**Files:**
- Create: `raw/assets/` (empty directory)
- Create: `wiki/companies/` (empty directory)
- Create: `wiki/concepts/` (empty directory)
- Create: `wiki/comparisons/` (empty directory)
- Create: `wiki/analyses/` (empty directory)
- Create: `wiki/sources/` (empty directory)

- [ ] **Step 1: Create all directories**

```bash
mkdir -p raw/assets wiki/companies wiki/concepts wiki/comparisons wiki/analyses wiki/sources
```

- [ ] **Step 2: Add .gitkeep files so empty directories are tracked**

```bash
touch raw/assets/.gitkeep wiki/companies/.gitkeep wiki/concepts/.gitkeep wiki/comparisons/.gitkeep wiki/analyses/.gitkeep wiki/sources/.gitkeep
```

- [ ] **Step 3: Verify structure**

```bash
find . -type d | sort
```

Expected output should include: `./raw`, `./raw/assets`, `./wiki`, `./wiki/companies`, `./wiki/concepts`, `./wiki/comparisons`, `./wiki/analyses`, `./wiki/sources`

- [ ] **Step 4: Commit**

```bash
git add raw/ wiki/
git commit -m "chore: create wiki directory structure"
```

---

### Task 2: Fork and adapt CLAUDE.md

**Files:**
- Source: `/Users/tteng/Development/my-wiki/CLAUDE.md`
- Create: `CLAUDE.md`

- [ ] **Step 1: Copy the existing CLAUDE.md**

```bash
cp /Users/tteng/Development/my-wiki/CLAUDE.md ./CLAUDE.md
```

- [ ] **Step 2: Update the title and identity**

Change the first line from:

```markdown
# Payment Industry & AI Wiki — Schema
```

to:

```markdown
# Payment Industry Wiki — Schema
```

Change the description paragraph from:

```markdown
You are maintaining a personal knowledge base about the **Payment Industry** and **Artificial Intelligence** — how they intersect, evolve, and shape each other. The wiki covers payment networks, fintech companies, AI applications in payments (fraud detection, underwriting, personalization, etc.), regulations, standards, and emerging trends.
```

to:

```markdown
You are maintaining a personal knowledge base about the **Payment Industry** — how it evolves and shapes commerce. The wiki covers payment networks, fintech companies, regulations, standards, and emerging trends.
```

- [ ] **Step 3: Update directory structure section**

Replace the directory structure block to reflect the new layout:

```
my-wiki-v2/
├── CLAUDE.md          # this file — schema and conventions
├── raw/               # immutable source documents (verbatim original content, never modify or summarize)
│   ├── assets/        # downloaded images referenced by sources
│   ├── <repo-slug>.md # GitHub repo stub file — lint anchor + metadata
│   └── <repo-slug>/   # GitHub repo key excerpts
├── wiki/              # LLM-generated pages (you own this layer)
│   ├── index.md       # catalog of all wiki pages
│   ├── log.md         # chronological operation log
│   ├── overview.md    # high-level payments industry overview
│   ├── companies/     # one page per company
│   ├── concepts/      # industry concepts, regulations, trends
│   ├── comparisons/   # side-by-side company comparisons
│   ├── analyses/      # filed query results and syntheses
│   └── sources/       # source summary pages
└── llm-wiki-idea.md   # reference — the pattern this wiki follows
```

- [ ] **Step 4: Rename entity pages to company pages**

In the "Page types" section, rename "Entity pages (`wiki/entities/`)" to "Company pages (`wiki/companies/`)".

Update the frontmatter template — change `type: entity` to `type: company`:

```yaml
---
title: "<company name>"
type: company
tags: [<relevant tags>]
source_count: <number of sources mentioning this company>
---
```

Remove the `category: company | product | person | organization | payment-network` field — all entries in `companies/` are companies. If other entity types are needed later, they can be added.

Update the body description: overview, key products, pricing model, API/developer experience, market position, pros, cons, notable clients. Link to sources, concepts, and comparisons.

**Important:** Also search the entire file for any remaining references to `type: entity` and replace with `type: company`.

- [ ] **Step 5: Add comparison pages as a new page type**

After the concept pages section, add a new section:

```markdown
### Comparison pages (`wiki/comparisons/`)

Side-by-side company analysis. Filename: `<company-vs-company>.md`

Frontmatter:

---
title: "<Company A> vs <Company B>"
type: comparison
date_created: YYYY-MM-DD
tags: [<relevant tags>]
---

Body: side-by-side analysis on specific dimensions (pricing, API quality, market position, etc.). Use markdown tables where appropriate. All claims sourced with links to source summary pages.
```

- [ ] **Step 6: Update all entity references throughout the file**

Search and replace throughout the entire file:
- `wiki/entities/` → `wiki/companies/`
- `entity pages` → `company pages`
- `entity/concept` → `company/concept`
- `entities/concepts` → `companies/concepts`

Also add `comparisons/` references in **all three ingest workflows** (they all have similar entity/concept update steps):

**a. Standard ingest workflow ("Ingest a source"):**
- Rename step 4: "Create or update relevant company pages in `wiki/companies/`."
- Add new step after concepts: "Create or update relevant comparison pages in `wiki/comparisons/` if the source covers multiple companies."

**b. Image ingest workflow ("Ingest content with images"):**
- Step 6: rename `entity pages` → `company pages`, update path to `wiki/companies/`
- Add new step after concepts: "Create or update relevant comparison pages in `wiki/comparisons/` if the source covers multiple companies."

**c. GitHub repo ingest workflow ("Ingest a GitHub repository"):**
- Step 7: rename `entity pages` → `company pages`, update path to `wiki/companies/`
- Add new step after concepts: "Create or update relevant comparison pages in `wiki/comparisons/` if the source covers multiple companies."

- [ ] **Step 7: Update the analysis page type description**

In the analysis pages section, change the description from "Comparisons, syntheses, filed query results" to "Cross-cutting syntheses, reference tables, filed query results." Remove the word "Comparisons" since those now have their own dedicated page type.

- [ ] **Step 8: Update the query workflow to route comparisons correctly**

In the "Answer a query" section, step 6 ("Offer to file as analysis"), update the **Comparison** bullet:

Change from: filing comparisons as analysis pages
To: "**Comparison**: Answer compares two or more platforms/products → offer to file as a **comparison page** in `wiki/comparisons/` (not `wiki/analyses/`)."

Keep the other filing criteria (Cross-cutting, Reusable reference) pointing to `wiki/analyses/` as before.

- [ ] **Step 9: Update the index.md category references**

In the ingest and lint workflow sections, ensure references to the index mention the new categories: Companies, Concepts, Comparisons, Analyses, Sources.

- [ ] **Step 10: Drop AI domain from domain-specific guidance**

In the "Domain-specific guidance" section at the bottom:
- Remove: "AI techniques (transformers, reinforcement learning, etc.) are concepts with category `technology`."
- Remove: "When a source covers both payments and AI, prioritize documenting the intersection — how AI is applied to payments or how payment data enables AI."
- Keep: "Payment networks (Visa, Mastercard, etc.) are entities, not concepts." → update to: "Payment networks (Visa, Mastercard, etc.) are companies, not concepts."
- Keep: "Regulations (PCI DSS, PSD2, etc.) are concepts with category `regulation`."
- Keep: "Track funding rounds, acquisitions, and partnerships as timeline entries on company pages."

- [ ] **Step 11: Verify the CLAUDE.md is consistent**

Read through the full file. Ensure:
- No remaining references to `entities/` or AI
- `companies/` used consistently
- `comparisons/` mentioned in ingest, query, lint, and index workflows
- All page types documented with frontmatter templates

- [ ] **Step 12: Commit**

```bash
git add CLAUDE.md
git commit -m "feat: add CLAUDE.md schema forked from my-wiki, adapted for payments-only focus"
```

---

### Task 3: Write seed content — wiki/index.md

**Files:**
- Create: `wiki/index.md`

- [ ] **Step 1: Write index.md**

```markdown
# Wiki Index

## Companies

_(No entries yet — populated as sources are ingested)_

## Concepts

_(No entries yet)_

## Comparisons

_(No entries yet)_

## Analyses

_(No entries yet)_

## Sources

_(No entries yet)_
```

- [ ] **Step 2: Commit**

```bash
git add wiki/index.md
git commit -m "feat: add wiki index with category headers"
```

---

### Task 4: Write seed content — wiki/log.md

**Files:**
- Create: `wiki/log.md`

- [ ] **Step 1: Write log.md**

```markdown
# Wiki Log

## [2026-04-13] init | Wiki created

Payments industry research wiki initialized. Schema forked from my-wiki and adapted for payments-only focus. Directory structure created. Seed content written (index, log, overview).
```

- [ ] **Step 2: Commit**

```bash
git add wiki/log.md
git commit -m "feat: add wiki log with creation entry"
```

---

### Task 5: Write seed content — wiki/overview.md

**Files:**
- Create: `wiki/overview.md`

- [ ] **Step 1: Write overview.md**

Write a brief (~200-300 word) overview of the payments industry landscape covering:

- **Payment networks** (Visa, Mastercard, American Express) — the rails that connect issuers and acquirers
- **Payment processors** — companies that handle transaction routing and settlement
- **Payment gateways** — the interface between merchants and processors
- **Payment service providers (PSPs)** — integrated platforms that bundle gateway + processing + merchant services (Stripe, PayPal, Adyen, Square, etc.)
- **Buy Now Pay Later (BNPL)** — emerging alternative payment methods
- **Key trends** — embedded finance, real-time payments, open banking

This page will be revised as the wiki grows. It serves as initial context for the LLM to understand where new information fits.

Use `[[wikilinks]]` to reference company and concept names even though the pages don't exist yet — they'll be created during ingest and the links will resolve.

- [ ] **Step 2: Commit**

```bash
git add wiki/overview.md
git commit -m "feat: add payments industry overview seed page"
```

---

### Execution Order

Run tasks in this order:
1. **Task 1** — Create directory structure
2. **Task 2** — Fork and adapt CLAUDE.md (largest task)
3. **Task 3** — Write wiki/index.md
4. **Task 4** — Write wiki/log.md
5. **Task 5** — Write wiki/overview.md

**Note:** Git initialization is intentionally excluded from this plan per the spec. The user can `git init` and commit when ready. All commit steps in tasks above are conditional — skip them if git is not initialized.
