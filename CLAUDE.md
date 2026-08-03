# Payment Industry Wiki — Schema & Operating Rules

You are maintaining a personal knowledge base about the **Payment Industry** — how it evolves and shapes commerce. The wiki covers payment networks, fintech companies (PSPs), regulations, standards, and emerging trends, with deep technical coverage of checkout/payment integrations.

## How this file works

This root file holds the **always-needed reference**: directory layout, page-type schema, conventions, and domain guidance — plus a **Workflow Index** that routes you to detailed rule files in `rules/`.

> 🚦 **Before performing any workflow (collecting raw content, ingesting, linting, answering queries), you MUST `Read` the matching rule file in `rules/` and follow it exactly.** The Workflow Index below is for routing only — never act from its one-line summaries.

`AGENTS.md` is a thin pointer to this file, so there is a single source of truth and no drift.

## Directory structure

```text
my-wiki/
├── CLAUDE.md          # this file — schema, conventions, domain guidance, Workflow Index
├── AGENTS.md          # pointer → CLAUDE.md + rules/
├── rules/             # detailed workflow rules (read on demand)
│   ├── raw-collection.md      # manual raw creation (paste/URL/image/mixed), naming, immutability
│   ├── psp-collection.md      # automated PSP doc collection (fetch_psp.py), two-pipeline overview
│   ├── psp/                   # one file per PSP — host, discovery file, .md rule, url fixups
│   │   ├── stripe.md
│   │   ├── paypal.md
│   │   ├── adyen.md
│   │   └── metronome.md
│   ├── github-repos.md        # common GitHub authority and strategy router
│   ├── github/                # release, commit, and supplement workflow rules
│   ├── ingest.md              # raw → wiki pages (NO-BATCH, concept-audit-first, templates)
│   ├── lint.md                # wiki health, orphan ingest queue, validate_wiki.py
│   └── query-and-synthesis.md # answer queries → comparison/analysis filing
├── scripts/           # automation
│   ├── fetch_psp.py           # PSP doc fetcher (staging, diff, dating, manifest)
│   ├── collection_discovery.py # multi-source discovery reconciliation
│   ├── collection_versions.py # immutable nested raw version comparison
│   ├── collection_reporting.py # run records and generated monitor
│   ├── collect_github_repos.py # GitHub collection, comparison, approval, retry, and status CLI
│   ├── psp_config.toml        # PSP registry (extensible: add a row per new PSP)
│   ├── validate_github_collection.py # GitHub evidence, work-item, page, and status validator
│   └── validate_wiki.py       # deterministic guardrail (frontmatter/links/placeholders)
├── raw/               # immutable source documents (verbatim, never modified or summarized)
│   ├── assets/                # downloaded images/video referenced by sources
│   ├── metronome/             # provider capsule preserving documentation paths
│   ├── <slug>-YYYY-MM-DD.md   # dated raw file (new files carry a collection date)
│   └── github/                # immutable GitHub evidence grouped by company and repository
│       └── <company>/<repo>/
│           ├── snapshots/<date>-<sha>/ # one exact-SHA source capsule
│           │   ├── manifest.json
│           │   └── files/
│           ├── supplements/<date>-<sha>-<identity>/ # approved deep-source additions
│           │   ├── manifest.json
│           │   └── files/
│           └── releases/<package>/<version>/<date>/ # package release notes and manifest
├── tracking/
│   ├── collections/           # generated inventories, run records, diffs, and status
│   └── github/                # repo-registry plus generated work items, comparisons, and status
│       ├── repo-registry.toml # human-maintained collection intent
│       └── repos/<company>/<repo>/
├── wiki/              # LLM-generated pages (you own this layer)
│   ├── index.md               # ROOT catalog: PSP list + comparisons + analyses + generic concepts + overview
│   ├── <psp>-index.md         # per-PSP catalog: that PSP's sources + company + platform concepts
│   ├── metronome-index.md      # Metronome provider capsule catalog
│   ├── metronome-log.md        # Metronome collection and ingest history
│   ├── log.md                 # chronological operation log
│   ├── overview.md            # high-level payments industry overview
│   ├── companies/             # one page per company
│   ├── concepts/              # industry concepts, regulations, trends
│   ├── comparisons/           # side-by-side company comparisons
│   ├── analyses/              # filed query results and syntheses
│   │   └── <company>/github/  # company-first GitHub version analyses
│   └── sources/               # source summary pages
│       └── <company>/github/  # cumulative GitHub source pages and separate changelogs
└── llm-wiki-idea.md   # reference — the pattern this wiki follows
```

## Page types

### Source summaries (`wiki/sources/`)

One page per ingested source. Filename: `source-<slugified-title>.md` (source-page slugs are **not** dated, even though their raw files may be).

Frontmatter:

```yaml
---
title: "<source title>"
type: source
date_ingested: YYYY-MM-DD
original_format: article | paper | report | transcript | notes | webpage | github-repo | image
raw_files:
  - "<filename in raw/ directory, e.g. stripe-invoicing-overview-2026-06-02.md>"
  - "<additional/older dated version, newest first if multiple>"
tags: [<relevant tags>]
---
```

Body: structured summary with key takeaways, relevant quotes, and links to company/concept pages. Body headings start at `##` — the frontmatter `title:` field serves as the document's H1 in Obsidian.

The `raw_files:` frontmatter field is plain strings used by the lint workflow (grep-friendly), listed **newest dated version first** when a source has been re-collected. For Obsidian navigation, also include a **Raw Sources** section at the bottom of the body with `[[wikilinks]]` to each raw file:

```markdown
## Raw Sources
- [[paypal-checkout-getting-started-2026-06-02]] — verbatim webpage content
- [[paypal-checkout-integrate-server-side-shipping-2026-06-02]] — server-side shipping tab variant
```

Obsidian resolves wikilinks by shortest matching filename, so the `.md` extension is omitted and no path prefix is needed.

### Company pages (`wiki/companies/`)

Payment companies and platforms. Filename: `<slugified-name>.md`

Frontmatter:

```yaml
---
title: "<company name>"
type: company
tags: [<relevant tags>]
source_count: <number of source summary pages (wiki/sources/) mentioning this company — one per source page, not per raw file>
---
```

Body: overview, key products, pricing model, API/developer experience, market position, pros, cons, notable clients, timeline of developments. Link to sources, concepts, and comparisons.

### Concept pages (`wiki/concepts/`)

Technologies, frameworks, regulations, trends. Filename: `<slugified-concept>.md`

Frontmatter:

```yaml
---
title: "<concept name>"
type: concept
category: technology | regulation | trend | framework | standard
tags: [<relevant tags>]
---
```

Body: definition, relevance to payments, current state, key players, open questions. Link to companies and sources.

**Naming**: prefix platform-specific concepts with the company slug (e.g., `paypal-vault.md`, `stripe-radar.md`, `adyen-marketpay.md`). Generic industry concepts need no prefix (e.g., `disputes.md`, `recurring-payments.md`, `3d-secure.md`). When in doubt, ask: "does this concept exist independently of one platform?" If yes, no prefix.

### Comparison pages (`wiki/comparisons/`)

Side-by-side company analysis on a **specific dimension**. Each comparison page covers one focused topic — not everything about a company pair.

Filename: `<company-vs-company>-<dimension>.md` (e.g., `stripe-vs-paypal-subscriptions.md`, `stripe-vs-paypal-apple-pay.md`, `stripe-vs-adyen-pricing.md`)

Frontmatter:

```yaml
---
title: "<Company A> vs <Company B>: <Dimension>"
type: comparison
dimension: "<dimension being compared, e.g. subscriptions, apple-pay, bnpl, pricing>"
date_created: YYYY-MM-DD
tags: [<relevant tags>]
---
```

Body: side-by-side analysis on the specific dimension. Use markdown tables where appropriate. All claims sourced with links to source summary pages. Link to relevant concept pages (e.g., `[[subscriptions]]`, `[[apple-pay]]`) and company pages.

Multiple comparisons between the same pair are expected — each gets its own page. The index groups them by company pair for easy browsing.

### Analysis pages (`wiki/analyses/`)

Cross-cutting syntheses, reference tables, filed query results. Filename: `analysis-<slugified-title>.md`

Frontmatter:

```yaml
---
title: "<analysis title>"
type: analysis
date_created: YYYY-MM-DD
tags: [<relevant tags>]
---
```

## Conventions

- **Links**: use Obsidian-style `[[wikilinks]]` for cross-references between wiki pages.
- **Tags**: use lowercase, hyphenated tags (e.g. `fraud-detection`, `real-time-payments`, `payment-gateway`).
- **Slugs**: lowercase, hyphenated filenames (e.g. `stripe.md`, `pci-dss.md`, `interchange-fees.md`).
- **Citations**: when referencing a source, link to the source summary page — e.g. `[[source-visa-annual-report-2025]]`.
- **Contradictions**: when new information contradicts existing wiki content, note it explicitly with a `> [!warning] Contradiction` callout and update both pages.
- **Confidence**: for claims that are uncertain or evolving, use `> [!info] Evolving` callouts.

## Raw file rules (canonical — full detail in `rules/raw-collection.md`)

- `raw/` is the **source of truth**: verbatim original content, exactly as received. Summaries belong in `wiki/sources/`, never in `raw/`.
- Raw files are **immutable** — never modify an accepted raw file after creation.
- **New raw files carry a collection date**: `raw/<slug>-YYYY-MM-DD.md`. The pre-existing undated files are the baseline and migrate to dated naming naturally when re-collected.
- Always create the raw file(s) **before** the source summary.
- `raw_files:` lists filenames relative to `raw/`, newest dated version first.
- GitHub evidence separates one immutable exact-SHA snapshot under `raw/github/<company>/<repo>/snapshots/` from package release records under `raw/github/<company>/<repo>/releases/`. Generated comparisons, work items, and status stay in `tracking/github/`.

## Workflow Index

> 🚦 **You MUST `Read` the linked rule file and follow it exactly before acting. This table is routing only.**

| Workflow | When | Read first |
| --- | --- | --- |
| Collect raw content (manual) | user pastes text, gives a URL, or attaches images | `rules/raw-collection.md` |
| Collect raw content (PSP bulk) | grabbing many pages from a PSP's docs (Stripe/PayPal/Adyen/…) | `rules/psp-collection.md` + `rules/psp/<psp>.md` |
| Collect or compare a GitHub repository | registry row, repository URL, package release, snapshot, or comparison | `rules/github-repos.md` + routed `rules/github/<strategy>.md` |
| Ingest an approved GitHub work item | one approved SHA group using full or delta mode | `rules/github-repos.md` + routed strategy rule + `rules/ingest.md` |
| **Ingest a raw file → wiki pages** | any raw file ready to become wiki pages | `rules/ingest.md` ⚠️ **ONE SOURCE AT A TIME — NEVER BATCH** |
| Lint the wiki | periodic health check, orphan sweep, accuracy/staleness | `rules/lint.md` |
| Answer / compare / analyze | a question, comparison, or cross-cutting synthesis | `rules/query-and-synthesis.md` |

## Domain-specific guidance

- **Payment networks** (Visa, Mastercard, etc.) are companies, not concepts.
- **Regulations** (PCI DSS, PSD2, etc.) are concepts with category `regulation`.
- Track funding rounds, acquisitions, and partnerships as timeline entries on company pages.
- **PSPs are a registry, not a fixed set.** Stripe, PayPal, and Adyen are covered today; Airwallex, Braintree, and others can be added by appending a row to `scripts/psp_config.toml` and a file under `rules/psp/`. Nothing in these rules hardcodes a fixed PSP list.
