# Metronome Provider Capsule Design

**Date:** 2026-07-12
**Status:** Approved design
**Scope:** Collect Metronome's English canonical documentation into an isolated raw corpus, monitor collection deterministically, and prepare a provider-scoped, parallel-capable ingest workflow. Implementation and ingest are out of scope for this specification.

## Goals

- Preserve every English canonical Metronome documentation page as immutable raw content.
- Reconcile `llms.txt` and `sitemap.xml` before collection so gaps are explicit.
- Keep Metronome independent from Stripe's existing corpus while making the Stripe ownership and Usage-based Billing relationship easy to query.
- Separate collection from ingest. Collection may be parallel; it never starts ingest automatically.
- Make unchanged-page detection, progress accounting, raw-link validation, and aggregate counts deterministic and model-independent.
- Support parallel ingest through isolated worktrees, explicit write ownership, structured handoffs, and coordinator-controlled reduction.
- Route mechanical source-summary work to a provider-neutral low-cost agent role while retaining strong-model review and synthesis gates.

## Non-goals

- Collecting the French-localized `/fr/` corpus during the pilot.
- Collecting the external Metronome blog or status site as documentation pages.
- Ingesting any collected page as part of the collection run.
- Migrating all existing Stripe and PayPal raw files, source pages, concepts, indexes, or log history into the new folder convention.
- Hard-coding DeepSeek, MiniMax, or any other single model provider into repository rules.

## Source inventory baseline

The live discovery comparison performed on 2026-07-12 established this pilot baseline:

| Category | Count |
| --- | ---: |
| English pages shared by `llms.txt` and `sitemap.xml` | 208 |
| Additional English pages found only in `sitemap.xml` | 17 |
| English canonical documentation pages selected | 225 |
| OpenAPI JSON artifacts listed by `llms.txt` | 2 |
| French-localized sitemap pages excluded | 105 |
| External blog and status targets excluded | 2 |

The counts are an observed baseline, not permanent constants. Future collection rounds report additions, removals, redirects, and language changes as discovery drift.

## Provider capsule

Metronome is a distinct provider capsule. Its physical source-of-truth boundary is `raw/metronome/`, not a directory nested below `raw/stripe/`. Wiki links express that Stripe owns Metronome and that Metronome extends Stripe's Usage-based Billing capabilities.

```text
raw/metronome/
├── _discovery/
│   └── <collection-date>/
│       ├── llms.txt
│       └── sitemap.xml
├── _artifacts/
│   ├── openapi-<collection-date>.json
│   └── openapi-plans-<collection-date>.json
├── guides/
├── api-reference/
└── integrations/

tracking/collections/metronome/
├── inventory-current.json
├── collection-status.md
├── diffs/
└── runs/
    ├── <run-id>.jsonl
    └── <run-id>-manifest.md

wiki/
├── metronome-index.md
├── metronome-log.md
├── companies/metronome.md
├── sources/metronome/
└── concepts/metronome/
```

Raw page directories preserve the documentation URL hierarchy. Dated leaf filenames preserve immutable versions, for example:

```text
raw/metronome/guides/get-started/home-2026-07-12.md
raw/metronome/guides/get-started/home-2026-08-05.md
```

If two different captures must be retained on the same date, the later one uses a deterministic revision suffix such as `home-2026-08-05-r2.md`.

## Discovery reconciliation

Before fetching documentation pages, the collector:

1. Saves dated verbatim snapshots of `llms.txt` and `sitemap.xml`.
2. Parses both sources and retains their original URLs.
3. Canonicalizes identity using hostname plus normalized path.
4. Removes a terminal `.md` for identity comparison only.
5. Normalizes trailing slashes and removes fragments and irrelevant query parameters.
6. Excludes `/fr/` pages, non-`docs.metronome.com` targets, and explicitly unsupported artifacts while recording a reason for each exclusion.
7. Selects the union of English canonical documentation pages.
8. Records whether each selected page appeared in `llms.txt`, the sitemap, or both.

Every selected inventory record contains at least:

```json
{
  "canonical_url": "https://docs.metronome.com/guides/get-started/home",
  "fetch_url": "https://docs.metronome.com/guides/get-started/home.md",
  "in_llms": true,
  "in_sitemap": true,
  "language": "en",
  "selected": true,
  "section": "guides/get-started",
  "local_path": "raw/metronome/guides/get-started/home-2026-07-12.md"
}
```

The two OpenAPI JSON URLs are collected as source artifacts but do not increase the 225-page documentation count.

## Collection state machine

Selected pages move through explicit states:

```text
discovered → pending → fetching
                         ├── collected-new
                         ├── collected-changed
                         ├── unchanged
                         ├── retry-pending
                         └── failed
```

`excluded` is terminal for a discovered target outside the selected corpus. Previously collected pages may additionally become `missing-from-discovery`, `reappeared`, or `redirected`. Removing a page from discovery never deletes its raw history.

At the end of a completed run, this invariant must hold:

```text
selected = collected-new + collected-changed + unchanged + retry-pending + failed
```

An exit code of zero does not make a run complete when this reconciliation fails.

## Retry and failure handling

Network failures, timeouts, HTTP 408, HTTP 425, HTTP 429, and HTTP 500-504 are retryable. The default policy is three attempts, respecting `Retry-After`, with configurable backoff. HTTP 403 receives one retry before failure classification.

HTTP 400, HTTP 401, HTTP 404, empty responses, invalid content types, Markdown endpoints returning error HTML, and redirects outside `docs.metronome.com` are not retried indefinitely. Every failed attempt records the URL, attempt number, status or exception, timestamp, and next action.

For sitemap-only pages, the collector derives and tries the `.md` URL. During the pilot, it records a clear failure when Markdown is unavailable rather than silently converting HTML to Markdown. Fallback policy is reviewed from real pilot failures.

## Scripted change detection and raw retention

No LLM decides whether a recollected page changed. The collector:

1. Fetches the candidate page into staging.
2. Removes only repository-owned metadata headers from both bodies.
3. Calculates a SHA-256 digest for the source body.
4. Compares the digest with the latest accepted version for the canonical URL.
5. Discards an identical candidate.
6. Saves a changed candidate under the new collection date.
7. Generates and stores a unified diff in the collection run artifacts.

Repository-owned headers are limited to:

```html
<!-- Source URL: ... -->
<!-- Fetched: ... -->
<!-- Discovery: ... -->
```

Source whitespace, headings, code blocks, and formatting are not normalized away. ETag and `Last-Modified` may reduce network work, but the body hash is authoritative.

Raw retention rules:

- Accepted raw files are immutable.
- Unchanged recollection creates no new raw file and requires no LLM work.
- Changed recollection retains every prior raw version and creates a new dated version.
- Failed collection creates no raw page.
- A same-day run never overwrites an accepted file.

## Collection monitoring

Each collection worker writes a uniquely named JSONL run fragment and never edits shared aggregate files. After all workers finish, one coordinator aggregation step regenerates:

- `tracking/collections/metronome/inventory-current.json`
- `tracking/collections/metronome/collection-status.md`
- the final round manifest

`collection-status.md` is generated, never hand-edited. It includes:

- Current counts by collection state
- Discovery reconciliation counts
- Progress by documentation section
- Failed and retry queues
- Discovery drift
- Run history
- Last successful collection time

Collection may run in parallel by non-overlapping section. It stops after raw promotion, run aggregation, validation, manifest creation, and user notification.

## Recollection and one living source page

One canonical documentation URL maps to one living source summary, regardless of how many raw versions exist. Recollection does not increase company `source_count`.

When a changed raw version is approved for ingest:

1. The agent reads the complete latest raw file.
2. The stored diff focuses attention on the delta without requiring an LLM to compare two full raw files.
3. The existing source page is updated so its main body reflects the current documentation.
4. The new raw path is prepended to `raw_files:`.
5. A concise material change entry is added to `## Change history`.
6. Concepts, company content, comparisons, and indexes are updated only when the delta affects them.
7. `source_count` remains unchanged because the source summary identity is unchanged.

The source page does not accumulate full historical summaries or inline unified diffs. Complete history remains in immutable raw versions and run artifacts.

## Source page contract

Source pages live under `wiki/sources/metronome/`. Their filename includes the full documentation path slug to avoid collisions.

```yaml
---
title: "Metronome: Get started"
type: source
date_ingested: 2026-07-12
date_updated: 2026-08-05
canonical_url: "https://docs.metronome.com/guides/get-started/home"
original_format: webpage
raw_files:
  - "metronome/guides/get-started/home-2026-08-05.md"
  - "metronome/guides/get-started/home-2026-07-12.md"
tags: [metronome, usage-based-billing, getting-started]
---
```

`date_ingested` remains the first-ingest date. Optional `date_updated` records the latest source-page update.

Required body sections are:

```markdown
## Overview
## Key takeaways
## Details
## Change history
## Related
## Raw Sources
```

`## Raw Sources` contains path-qualified Obsidian links to every retained raw version, newest first:

```markdown
- [[raw/metronome/guides/get-started/home-2026-08-05|2026-08-05 snapshot - latest]]
- [[raw/metronome/guides/get-started/home-2026-07-12|2026-07-12 snapshot - initial collection]]
```

The source page therefore provides a deterministic deep-dive path when a future query needs more detail than the summary contains.

## Wiki ownership contracts

### `wiki/metronome-index.md`

The Metronome index is the canonical query router for ingested Metronome content. It contains coverage, company, concepts, grouped source summaries, related platforms, and operations links. It does not list pending raw pages as if they were ingested sources.

Coverage counts and source entries are generated from source metadata and approved ingest receipts. Concepts and their descriptions remain curated.

### `wiki/companies/metronome.md`

The company page owns the company and platform overview, major capabilities, API model, market position, Stripe acquisition timeline, relationship with Stripe Billing, and links to concepts and sources. A script recalculates `source_count` from actual source summaries. Workers never increment it manually.

### `wiki/concepts/metronome/`

The initial concept set is:

- `metronome-usage-based-billing.md`
- `metronome-event-ingestion.md`
- `metronome-billable-metrics.md`
- `metronome-products-and-rate-cards.md`
- `metronome-customers-and-contracts.md`
- `metronome-credits-and-commits.md`
- `metronome-invoicing.md`
- `metronome-alerts-and-notifications.md`
- `metronome-reporting-and-analytics.md`
- `metronome-integrations.md`

Platform-specific concept filenames keep the `metronome-` prefix even inside the folder so basename links remain globally unique. Generic concepts remain outside the provider folder and link to platform-specific implementations without duplicating them.

### `wiki/metronome-log.md`

The provider log is newest-first. It contains one summary entry per collection round and one entry per completed source ingest or source update. Detailed attempts, diffs, model routing, and token accounting remain in tracking receipts rather than the query-facing wiki log.

### Root and Stripe navigation

`wiki/index.md` links to `metronome-index` under a provider-oriented heading and links to the Metronome company page. `wiki/stripe-index.md` links to Metronome under a small related-platforms section. Neither duplicates the Metronome source catalog or concept list.

The existing `wiki/log.md` may become a lightweight log router in a separate migration. The Metronome pilot does not rewrite its historical entries.

## Parallel ingest architecture

Parallel ingest uses a coordinator-controlled map-and-reduce workflow. It is a controlled extension of the existing serial ingest rule: every worker handles one raw file at a time and reads it completely, while multiple isolated workers may operate concurrently on disjoint write sets.

### Coordinator preparation

The coordinator:

1. Selects only successfully collected new or changed raw pages.
2. Groups pages into coherent topical shards.
3. Predicts the concept touch set for each shard.
4. Creates one worktree and branch per worker or topic shard, not per raw page.
5. Writes a focused job brief containing exact raw paths, allowed files, forbidden shared files, output schema, and validation requirements.
6. Assigns one owner per concept for the ingest wave.

### Parallel source workers

Each worker processes its queue serially. For each raw page it completes a full read, extracts grounding quotes, creates or updates the unique source summary, validates its work, writes an ingest receipt, and commits before starting the next page.

Workers may edit:

- Assigned source summaries
- Metronome-specific concepts they exclusively own
- Their unique worktree-local receipts

Workers may not edit:

- `wiki/companies/metronome.md`
- `wiki/metronome-index.md`
- `wiki/metronome-log.md`
- Root index or log files
- Generic concepts or comparisons
- Concepts leased to another worker

### Ingest receipt

Every source job produces a structured receipt containing:

- Job and canonical source identity
- Raw path and source page path
- Completion status
- Grounding quotes with raw locations
- Proposed concept, company, index, and log updates
- Files changed
- Validation command and result
- Commit identifier
- Agent role, actual model provider and model, token usage when available, and review status

Receipts are durable file handoffs. The main conversation receives only concise statuses and references to those files.

### Review and merge

The coordinator reviews each worker's receipt and commit range, verifies the allowed write set, confirms validation, and rejects incomplete work. Approved work is merged or cherry-picked; files are not manually copied between worktrees.

### Concept reduction

After source summaries merge, concept synthesis can run in parallel by concept. Each reducer receives every approved fact packet for exactly one concept. No two reducers edit the same concept in one wave. Generic concepts and cross-provider comparisons run in a later cross-cutting wave.

### Coordinator finalization

Only the coordinator updates the Metronome company page, index, log, root navigation, calculated counts, and overall ingest progress. This prevents source-count races and conflicting aggregate edits.

## Provider-neutral model routing

The workflow defines roles and quality gates rather than binding to a vendor:

| Work | Model tier |
| --- | --- |
| Hashes, diffs, inventories, link checks, counts | Scripts; no LLM |
| Grounded first-pass source summaries and receipts | Low-cost ingest worker |
| Provider-specific concept synthesis | Mid-tier or strong model based on complexity |
| Generic concepts, contradictions, comparisons | Strong model |
| Merge review, failed-job repair, final audit | Strong coordinator or reviewer |

The logical low-cost role is `cheap_ingester`. Its configured model may be DeepSeek, MiniMax, a local model, or an efficient OpenAI model when the runtime exposes a compatible provider interface. Provider credentials and provider-routing configuration remain outside the repository.

Before selecting a default low-cost model, run a representative pilot covering short guides, long guides, API references, code/schema-heavy pages, and a changed-page update. Measure quote accuracy, unsupported claims, raw-link correctness, validator pass rate, coordinator repair time, total cost, turns, and elapsed time. Token price alone does not decide the winner.

## Deterministic validation

Validation must be extended to support nested raw paths and provider folders. The Metronome capsule is valid only when scripts confirm:

- Every selected URL has a collection state.
- Collection totals reconcile.
- Every ingested canonical URL maps to exactly one source page.
- Every `raw_files:` entry exists under `raw/`.
- `raw_files:` and `## Raw Sources` contain the same versions newest first.
- Every indexed source page exists and every source page appears in the Metronome index.
- The calculated company `source_count` matches actual source summaries.
- Every successful ingest receipt has a provider-log entry.
- Nested orphan detection finds every collected but un-ingested Metronome page.
- No two workers own the same concept in one wave.
- No worker modifies files outside its declared write set.
- Re-running collection creates no duplicate raw files.

## Pilot sequence

1. Implement nested-path-aware collection, monitoring, hashing, manifests, and validation.
2. Reconcile the live discovery sources and confirm the selected English inventory.
3. Smoke-test representative URLs, including sitemap-only pages.
4. Run the initial collection and resolve failures until every selected URL has a terminal state.
5. Create the empty Metronome wiki capsule and navigation links.
6. Benchmark low-cost ingest candidates on a representative source set.
7. Run one controlled parallel ingest wave using worktrees, receipts, review, concept reduction, and coordinator finalization.
8. Audit quality, cost, conflicts, and recovery behavior before scaling to the remaining corpus.

## Acceptance criteria

- English canonical scope and exclusions are reproducible from discovery snapshots.
- Raw files are immutable, dated, path-preserving, and diffed without LLM involvement.
- Unchanged recollection consumes no ingest-model tokens.
- Collection status and failures remain visible and arithmetically reconciled.
- Collection never automatically triggers ingest.
- Every source summary has a durable deep link to every raw version.
- One canonical URL retains one source summary across recollections.
- Parallel workers operate in isolated worktrees with explicit write ownership.
- Shared synthesis and aggregate edits have single owners.
- Low-cost workers are provider-neutral and protected by deterministic validation and strong review gates.
- The pilot demonstrates acceptable accuracy, cost, merge safety, and recoverability before full-scale ingest.
