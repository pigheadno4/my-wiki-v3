# Rule: Ingest a raw file → wiki pages

> This rule governs turning **one** raw file into wiki pages. You arrived here from the CLAUDE.md Workflow Index. Collection (manual or PSP-bulk) happens first; this rule is the shared back end both pipelines converge on.

## 🛑 ONE SOURCE AT A TIME — NEVER BATCH

> Ingest exactly **one source unit per cycle**. For normal sources, the source unit is exactly one raw file. Before writing any wiki page you MUST `Read` the **full** source unit end-to-end — never from a partial read, a summary, or several source units in parallel. Complete one source unit's entire cycle (concept audit → source → company → concept → comparison → contradiction check → index → log) and mark its todos done **before** starting the next source unit.

This is the single most important rule. Batching produces shallow summaries, missed details, and malformed pages. It was confirmed in smoke testing: **no batch, process one by one, read the full raw content, then ingest.**

## Selective-ingest routing boundary

Complete canonical raw collection does not require routine source generation
for every page. Use these three dispositions:

```text
source_required  = full source generation plus independent review
raw_reference    = navigation-only raw; no routine source generation
semantic_triage  = one complete strong-model read to decide the disposition
```

`## Raw Sources` records raw pages read completely and used as factual evidence
for a source body. `## Related raw API references` records navigation-only raw
pages that were not used as factual evidence. A related raw page may establish
that a documentation target exists, but it cannot support claims about that
page's behavior until it is read completely through the applicable query,
triage, or ingest workflow.

Metadata classification from titles, URLs, documentation hierarchy, or an
inventory never authorizes facts from an unread page. Before assigning
`raw_reference`, route an endpoint to `semantic_triage` whenever metadata
cannot rule out that it is the sole authority for required request fields;
durable failure or propagation behavior; deletion or lifecycle semantics;
uniqueness or idempotency constraints; or state-transition semantics. CRUD
shape or schema-heavy content alone cannot justify `raw_reference`. A complete
triage read may still resolve to `raw_reference` when it finds no unique
durable facts that warrant a curated source.

A query may recommend promotion, but only user approval changes the disposition
to `source_required`. Once approved, a missing source is queued for generation
even when the raw hash has not changed.

## Coordinator-controlled parallel-review campaign exception

The default above remains mandatory for ordinary ingest. A campaign may defer
and reduce shared-file writes only when an exact, explicitly approved campaign
manifest **and an explicit provider-specific authorization** provide all of
these controls. A provider without its own authorization remains serial-only.

- Each worker handles exactly one source unit, reads it completely, extracts
  three to five verbatim quotes, and returns one isolated source candidate plus
  structured shared-file suggestions.
- Every first attempt receives a complete-source review by a different
  strong-model reviewer. That reviewer checks the candidate, quotes,
  contradictions, unknowns, raw link, relevant concepts and source context,
  and the semantic validity of shared-file suggestions; reviewers do not
  reread the full company page, provider index, or provider log. A bounded
  correction may use targeted diff review only when its raw hash is unchanged;
  factual or uncertain corrections require another complete-source review.
- Workers and reviewers are repository-read-only. The coordinator remains the
  only writer of canonical sources, concepts, company pages, indexes, logs,
  counts, campaign state, and commits.
- The coordinator fully rereads the source only for a disputed or uncertain
  review, a retry with unresolved content risk, a high-risk page named in the
  manifest, or a page selected for final quality sampling.
- Source units remain independent. No candidate may combine several raw pages,
  and review approval is recorded per source before canonical promotion.

Unless the provider-specific authorization permits incremental promotion,
after all reviews finish the coordinator groups reviewer-approved shared
updates by target and applies each target once instead of repeatedly editing
the same file. An incremental authorization may let the coordinator promote
one approved job while unrelated workers and reviewers continue, but it must
keep canonical writes serial, apply only that job's reviewer-approved updates,
and defer company, provider-index, provider-log, and count updates until the
campaign close:

1. Merge approved durable facts and planned source wikilinks by concept and
   apply each concept update once, before the corresponding sources.
2. Write the individually approved source pages.
3. Verify contradictions and fact-based reciprocal concept citations; repair a
   defect if one is found.
4. Update the company page, provider index, provider log, and calculated counts
   once for the campaign.

Incremental promotion never weakens the approval gate: a candidate remains
non-canonical until its own independent review is approved. A pause stops new
promotion work but preserves already promoted approved jobs and their attempt
evidence. Campaign-close validation still covers the complete promoted set.

Concept updates still precede the corresponding canonical source promotion.
Company and provider indexes are exhaustive reverse catalogs; a concept cites a
source when that source contributes a durable fact. A navigation-only source
link does not force a reciprocal concept citation.

Validation is layered rather than repeated globally after every page:

- Worker handoff: raw hash, canonical URL, result schema, and verbatim quotes.
- Reviewer handoff: complete-source review and candidate/suggestion approval.
- Campaign close: validate every promoted source and touched concept, then run
  provider count, link, duplicate-entry, raw-hash, and capsule checks once.
- The coordinator alone exhaustively checks the company page, provider index,
  provider log, links, and counts once at campaign close; it does not perform
  a default third full-source read.
- Run the full unit suite when code, rules, or validators changed. A
  documentation-only mature campaign uses the targeted and capsule checks.

The immutable approved manifest records three distinct audit job IDs before
execution: one standard page, the longest or schema-heaviest page, and one
ordinary manifest sample. Any material partial or fail expands the audit to
every campaign page.
Broken links, duplicate index/company entries, hashes, and counts are always
checked across the complete campaign.

For GitHub, the source unit is exactly one approved SHA work item, which may
contain multiple package releases sharing that SHA. Read the complete current
source and changelog pages, every assigned release record and comparison, the
snapshot manifest, and every assigned raw file in full before writing wiki
content. Do not claim to have read the whole upstream repository.

## MANDATORY setup

> Use `TodoWrite` to create **one todo item per step below** before starting any work. Mark each item completed as you finish it — never batch completions. The **concept audit (step 2) must be completed and marked done before any other page is created.**

1. **Read the full raw file.** Open the entire raw file. For GitHub, read the approved work item and every assigned source page, changelog, release record, comparison, snapshot manifest, and raw file per `github-repos.md`. Do not summarize from a partial read.
   - **Grounding gate:** before writing anything, extract **3–5 verbatim quotes** (with their location in the raw file) that the summary will rest on. This forces grounding and cuts hallucination — especially important on cheaper models.

## Phase 2 — Wiki ingest (after Phase 1 raw file is approved)

2. **Concept audit (FIRST, MANDATORY).** Scan `wiki/concepts/` for any existing page covering the same topic as the source.
   - If a related concept page exists: update it now with new facts from the source. Do not defer.
   - If no concept page exists for a major new product or topic area: create one now, before moving to step 3.
   - Use the decision table below to decide whether a new concept page is warranted.
3. **Source summary page** in `wiki/sources/` (filename `source-<slug>.md`, **not** dated):
   - New source page → include `raw_files:` in frontmatter with the dated raw filename.
   - Adding to an existing source page (e.g., a re-collected/changed version, or a 2nd raw file on the same topic) → prepend the new dated raw filename to the existing `raw_files:` list (**newest first**), and add the new content/delta to the body.
   - GitHub source page → keep one cumulative `wiki/sources/<company>/github/source-github-<repo>.md` page plus `changelog-github-<repo>.md`. List each nested snapshot manifest as its root-relative path under `raw/` in `raw_files:` (for example, `github/paypal/paypal-js/snapshots/2026-07-20-a1b2c3d/manifest.json`, newest first). Link package release records, comparisons, and exact raw files with path-qualified repository-root paths; do not use an unqualified `[[manifest]]` link.
4. **Company pages** in `wiki/companies/` — create or update. Update `source_count`.
5. **Concept pages** in `wiki/concepts/` — create or update per the decision table.
6. **Comparison pages** in `wiki/comparisons/` — only if the source **substantively compares** two or more companies (pricing differences, feature comparisons, migration guides). A passing mention of multiple companies does not warrant one.
7. **Contradiction check** — compare against existing wiki content; flag with a `> [!warning] Contradiction` callout on both pages.
8. **Update the index** — add/update entries in the **per-PSP index** `wiki/<psp>-index.md` for PSP-specific pages, and in the **root** `wiki/index.md` for cross-cutting pages (comparisons, analyses, generic concepts). See `lint.md` for the split rule.
9. **Append an entry to `wiki/log.md`.**
10. **Self-check** — run `python scripts/validate_wiki.py <the pages you touched>` and fix anything it flags (missing frontmatter fields, `raw_files:` that don't exist, unresolved wikilinks, leftover placeholders).

### Concept page decision table

| Situation | Action |
| --- | --- |
| New topic area — first source on this subject | Always create a concept page |
| New PayPal/Stripe/Adyen (or other PSP) product not yet in `wiki/concepts/` | Create a concept page |
| Supplementary page — 2nd+ source on an already-covered topic | Update the existing concept page instead |
| Thin content — setup guides, test values, troubleshooting, error code tables | Skip concept page; update existing one only if new concrete facts emerge |

**Naming reminder**: prefix platform-specific concepts with the company slug (e.g., `paypal-vault.md`). Generic industry concepts need no prefix (e.g., `disputes.md`, `agentic-commerce.md`). Ask: "does this concept exist independently of one platform?" If yes, no prefix. If 3+ source pages exist on a topic with no concept page, that is a gap — create the concept page. **Generic concept pages link to platform-specific implementations, they do not duplicate them** — e.g., `disputes.md` explains the concept and links to `[[source-paypal-disputes-api]]`; it does not re-list all 9 PayPal endpoints.

## Copy-paste templates

> Fill the blanks — do not paraphrase the structure. (Templates make output reliable across models.)

**Source page frontmatter:**

```yaml
---
title: "<source title>"
type: source
date_ingested: <YYYY-MM-DD>
original_format: <article | paper | report | transcript | notes | webpage | github-repo | image>
raw_files:
  - "<slug>-<YYYY-MM-DD>.md"
tags: [<tag>, <tag>]
---
```

**Source page body skeleton:**

```markdown
## Overview
<2–4 sentences: what this source is and why it matters>

## Key takeaways
- <takeaway grounded in a quote you extracted>
- <takeaway>

## Details
<structured detail: products, parameters, limits, flows — grounded in the raw file>

## Related
- Companies: [[<company>]]
- Concepts: [[<concept>]]

## Raw Sources
- [[<slug>-<YYYY-MM-DD>]] — <one-line description>
```

## Worked example (raw excerpt → finished page)

**Raw excerpt** (`raw/stripe-payment-intents-2026-06-02.md`):
> "A PaymentIntent transitions through statuses: `requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `succeeded`. Use the `client_secret` to complete the payment on the client."

**Finished `wiki/sources/source-stripe-payment-intents.md`:**

```markdown
---
title: "Stripe PaymentIntents API"
type: source
date_ingested: 2026-06-02
original_format: webpage
raw_files:
  - "stripe-payment-intents-2026-06-02.md"
tags: [stripe, payment-intents, checkout]
---

## Overview
The PaymentIntents API tracks a payment's lifecycle on Stripe from creation to completion.

## Key takeaways
- A PaymentIntent moves through statuses: `requires_payment_method` → `requires_confirmation` → `requires_action` → `processing` → `succeeded`.
- The `client_secret` completes the payment client-side.

## Related
- Companies: [[stripe]]
- Concepts: [[stripe-payment-intents]]

## Raw Sources
- [[stripe-payment-intents-2026-06-02]] — verbatim docs page
```

## Task → model routing (cost-efficient, quality-preserving)

When using cheaper models (DeepSeek/GLM) for volume, route by judgment level:

| Task | Judgment level | Model tier |
| --- | --- | --- |
| Bulk source-page summaries (templated) | low — fill a template from one raw file | **cheap model OK** |
| Frontmatter / index/log line edits | low — mechanical | **cheap model OK** |
| Concept page synthesis / merging | high — cross-source judgment | **strong model** |
| Contradiction detection | high — cross-page reasoning | **strong model** |
| Comparison / analysis pages | high — multi-source synthesis | **strong model** |
| Lint triage (what to fix, staleness) | high — judgment | **strong model** |

Regardless of model, **every output must pass `scripts/validate_wiki.py`** — that deterministic guardrail is what keeps quality high when a cheaper model misses a field or a link.
