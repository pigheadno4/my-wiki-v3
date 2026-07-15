# PayPal New Documentation Collection Design

**Date:** 2026-07-15

**Status:** Approved design, awaiting written specification review

**Scope:** Discovery, immutable raw collection, progress reporting, and comparison preparation for the upgraded documentation at `developer.paypal.com`

## Problem

The upgraded PayPal developer documentation is not represented by one complete download file. Its root `llms.txt` links to section-level catalogs, and those catalogs list the documentation pages whose Markdown variants can be downloaded by appending `.md`. The collection must traverse the complete catalog hierarchy rather than treating one section, such as Business Payments, as the corpus.

The existing generic PSP collector assumes a mostly flat discovery file and provider behavior expressible through configuration. That model does not fit PayPal-new's nested discovery, catalog snapshotting, coverage audit, frozen-inventory requirement, and path-preserving raw layout. It also must not replace or mix with the legacy PayPal corpus because the purpose of the new collection is to compare the two documentation generations.

The collection process therefore needs a standalone provider orchestrator that first proves what it intends to collect, then downloads only from that immutable plan. It must be fast enough for thousands of pages while remaining resumable, auditable, safe against HTML error pages, and compatible with the wiki's immutable-raw and serial-ingest rules.

## Goals

- Traverse the root PayPal catalog and every reachable PayPal `llms.txt` catalog.
- Preserve immutable copies of all discovery catalogs and the sitemap used for auditing.
- Consolidate a deterministic, deduplicated list of canonical documentation pages and Markdown download URLs before page collection begins.
- Make the frozen inventory independently reviewable and bind every collection run to its exact hash.
- Preserve the canonical URL hierarchy under `raw/paypal-new/` to prevent filename collisions and support source tracing.
- Validate response status, media type, and body shape before accepting raw Markdown.
- Preserve every accepted raw version without overwriting prior evidence.
- Record every attempt and reconcile every selected page to a terminal state.
- Support bounded-concurrency collection and targeted retry runs without rerunning successful pages.
- Keep collection automated and batch-oriented while leaving ingest human-triggered and strictly one raw source at a time.
- Retain enough stable identity and provenance metadata to build a later legacy-versus-new PayPal comparison crosswalk.

## Non-goals

- Ingesting collected pages into `wiki/` automatically.
- Creating PayPal source, company, concept, comparison, or analysis pages in this collection phase.
- Replacing or reorganizing the legacy PayPal raw corpus.
- Refactoring Stripe, Adyen, Braintree, PayPal.ai, or legacy PayPal collectors in this work.
- Treating every sitemap URL as an automatic download target.
- Solving semantic old-versus-new page matching during collection.
- Supporting partial inventories as valid collection inputs in the first version.

## Considered Approaches

### Interleaved discovery and download

The collector could download a page as soon as a catalog link is found. This minimizes intermediate artifacts but cannot prove corpus completeness before writes begin. A failed child catalog can leave a seemingly successful but incomplete raw collection, and the page queue can change during the run.

### Union of catalogs and sitemap as the download queue

The collector could merge every `llms.txt` link with every sitemap URL and fetch the union. This maximizes attempted coverage but mixes publisher-designated Markdown pages with audit-only, legacy, redirected, or non-documentation routes. It makes failures noisy and silently broadens scope.

### Frozen catalog inventory followed by collection

This is the selected approach. The catalogs define the page queue; the sitemap audits that queue. Discovery must finish, reconcile, and seal an immutable inventory before any documentation page is fetched. One inventory can then drive an initial collection run and any later retry runs.

## Locked Decisions

| Concern | Decision |
| --- | --- |
| Entry point | `scripts/fetch_paypal_new.py` is the standalone provider orchestrator. |
| Provider identity | `paypal-new` means the upgraded `developer.paypal.com` corpus and remains separate from legacy PayPal and PayPal.ai. |
| Discovery authority | The root `llms.txt` and every reachable same-host `llms.txt` define the selected page inventory. |
| Sitemap role | `sitemap.xml` is preserved and used for gap reporting, not added automatically to the page queue. |
| Phase boundary | Documentation collection refuses to start without a complete, sealed inventory. |
| Catalog parsing | For a catalog bullet, only its first Markdown link is the primary target; links in descriptions are metadata, not extra pages. |
| Deduplication | Canonical page URL is the page identity; multiple catalog appearances are retained in `discovered_from`. |
| Raw layout | The complete canonical URL path is preserved under `raw/paypal-new/`. |
| Raw retention | Accepted files are immutable; unchanged content creates no new raw file. |
| Same-day change | A second distinct version on the same date uses `-r2`, then `-r3`, rather than overwriting. |
| Run history | Inventories, attempt events, and terminal run summaries remain immutable. A retry creates a new run. |
| Ingest boundary | No collection command starts ingest. Ingest remains one complete raw file at a time. |
| Runtime | Implementation remains compatible with the repository's Python 3.9 environment. |

## Component Boundaries

The standalone script owns PayPal-new policy:

- Root and child catalog traversal.
- Catalog parsing and first-link extraction.
- PayPal URL normalization and `.md` derivation.
- Sitemap comparison policy.
- PayPal raw path mapping.
- Discovery sealing and collection command orchestration.

Shared collection modules own provider-independent mechanics where the current modules are suitable:

- HTTP retry, throttling, cache-busting, and response metadata.
- Content validation.
- Hashing, comparison, immutable promotion, and same-day revisions.
- JSONL event writing and summary reconciliation.

The implementation may add narrowly focused shared helpers, but it must not force PayPal-new discovery behavior into `psp_config.toml` or add PayPal-specific branches to `fetch_psp.py`.

## Artifact Layout

```text
raw/paypal-new/
+-- _discovery/
|   `-- <discovery-id>/
|       +-- root-llms.txt
|       +-- catalogs/
|       |   `-- <path-preserving catalog snapshots>
|       +-- sitemap.xml
|       `-- manifest.json
`-- <canonical parent path>/
    `-- <leaf>-YYYY-MM-DD.md

tracking/collections/paypal-new/
+-- inventories/
|   `-- <discovery-id>/
|       +-- raw-md-links.txt
|       +-- pages.jsonl
|       +-- duplicates.jsonl
|       +-- excluded-pages.jsonl
|       +-- sitemap-only.txt
|       +-- catalog-only.txt
|       +-- coverage-summary.json
|       +-- discovery-events.jsonl
|       `-- manifest.json
`-- runs/
    `-- <collection-run-id>/
        +-- manifest.json
        +-- attempts.jsonl
        +-- accepted-files.jsonl
        `-- summary.json
```

The discovery snapshot under `raw/` is immutable upstream evidence. A sealed inventory and a completed run directory under `tracking/` are immutable operational records. While a collection run is active, its event files are append-only; completion seals the run and its terminal summary. Human-readable dashboards may be generated later from those records, but the sealed records themselves are never rewritten.

## URL and Page Identity

Only HTTPS URLs on `developer.paypal.com` are eligible. Normalization:

1. Resolves relative URLs against the catalog URL.
2. Lowercases the scheme and host.
3. Collapses duplicate path separators.
4. Removes a trailing slash except for the site root.
5. Removes the fragment from file identity while preserving it in the inventory's `fragments` metadata.
6. Removes known tracking parameters. An unknown non-empty query is a discovery anomaly rather than being silently discarded.
7. Excludes external hosts from the PayPal raw queue while retaining them in the inventory and `excluded-pages.jsonl` with an explicit reason.

The normalized page URL without `.md` is `canonical_url`. `markdown_url` is produced by appending `.md` to the normalized path unless it already ends in `.md`. Two catalog entries with the same canonical URL produce one page record with merged titles, fragments, and discovery sources.

The raw relative path preserves all canonical path segments. For example:

```text
https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/additional-parameters
    -> raw/paypal-new/api/nvp-soap/payflow/integration-guide/
       additional-parameters-YYYY-MM-DD.md
```

Unsafe filesystem characters are encoded deterministically. Discovery fails sealing if two canonical URLs map to the same raw identity.

## Discovery Phase

The `discover` command performs these steps without downloading documentation page bodies:

1. Create a new discovery ID and staging directory.
2. Fetch the root `https://developer.paypal.com/llms.txt` with bounded retries and record response metadata.
3. Parse primary catalog links and place every same-host `llms.txt` target on a cycle-safe traversal queue.
4. Fetch every queued catalog, preserve its exact body, and recursively enqueue newly discovered catalogs.
5. Parse documentation bullets from every catalog, using only the first link in each bullet as the primary page target.
6. Normalize page identities, merge duplicates, derive Markdown URLs, and calculate raw destinations.
7. Fetch and preserve `sitemap.xml`, normalize its documentation URLs, and calculate sitemap-only and catalog-only sets.
8. Re-fetch the discovered catalogs and compare content hashes to detect a catalog change during traversal.
9. Validate the inventory and write deterministic sorted outputs.
10. Hash every catalog snapshot and inventory artifact, cross-reference the two output directories, then seal the discovery manifest.
11. Promote each completed directory atomically. Collection treats either directory without its sealed cross-reference partner as incomplete and refuses it.

The advertised page counts in the root catalog are recorded and compared with parsed primary-link counts, but they are publisher metadata rather than the source of truth. A mismatch is a visible coverage anomaly and does not alone block sealing. Sealing is blocked by a missing catalog, parser failure, unresolved URL, unknown query semantics, unstable catalog hash, duplicate raw identity, or inconsistent inventory hash. A well-formed external primary link is excluded and reported rather than treated as an invalid PayPal page.

An incomplete discovery writes diagnostics to staging for the operator but does not produce a sealed manifest accepted by `collect`. The first version provides no `--allow-partial` bypass.

## Frozen Inventory Contract

`raw-md-links.txt` contains one selected Markdown URL per line in deterministic lexical order. It is the simple full raw-link list for human inspection and external tooling.

`pages.jsonl` is the authoritative machine-readable plan, sorted by canonical URL. It includes selected PayPal pages and explicitly excluded primary links so discovery accounting remains complete. A selected page record includes at least:

```json
{
  "canonical_url": "https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/additional-parameters",
  "markdown_url": "https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/additional-parameters.md",
  "raw_identity": "api/nvp-soap/payflow/integration-guide/additional-parameters",
  "discovered_from": [
    "https://developer.paypal.com/developer-resources/llms.txt"
  ],
  "catalog_titles": [
    "Processors That Require Additional Transaction Parameters"
  ],
  "fragments": [],
  "selection": "selected"
}
```

Inventory files contain stable discovery facts, not mutable collection status. Status belongs in collection run events. `raw-md-links.txt` contains only records whose selection is `selected`; `excluded-pages.jsonl` explains all excluded primary links. The discovery manifest records the SHA-256 digest, record count, and byte count of each output. `collect` verifies all recorded hashes before making a page request.

## Sitemap Audit Boundary

The catalog inventory remains authoritative for the initial download queue:

- Catalog-and-sitemap pages are selected normally.
- Catalog-only pages remain selected and are reported for visibility.
- Sitemap-only pages are written to `sitemap-only.txt` but are not selected.
- URLs that cannot be normalized into eligible documentation routes are recorded as audit anomalies.

Expanding collection to sitemap-only pages requires a later explicit design decision or reviewed supplemental inventory. This prevents coverage auditing from silently becoming scope expansion.

## Collection Phase

The `collect` command accepts the path to one sealed inventory. It:

1. Verifies the discovery manifest and all inventory hashes.
2. Creates a collection run bound to the discovery ID and `pages.jsonl` hash.
3. Selects all inventory records, or a deterministic smoke-test subset when `--limit` is supplied.
4. Fetches Markdown pages with configurable bounded concurrency.
5. Honors `Retry-After` and uses capped exponential backoff with jitter for transient failures.
6. Validates each response before staging it.
7. Compares the validated body with the latest accepted version for the same canonical identity.
8. Records unchanged content without creating a raw file.
9. Promotes new or changed content atomically to its path-preserving raw destination.
10. Appends one event for every network attempt and one terminal result for every selected page.
11. Writes accepted-file records and a reconciled terminal summary.

The collector may prepend the repository-standard source URL and fetched-date HTML comments. Content hashes used for change comparison exclude those generated provenance lines.

Accepted terminal states are:

- `new`
- `changed`
- `unchanged`
- `http-failed`
- `network-failed`
- `invalid-content`
- `path-conflict`

Every page selected by a run must reach exactly one terminal state. The summary is valid only when:

```text
selected = new + changed + unchanged + http-failed
         + network-failed + invalid-content + path-conflict
```

A run can finish as `complete` or `complete-with-failures`; it cannot claim success with unreconciled pages.

## Validation and Raw Promotion

A page is accepted only when all of the following hold:

- The final HTTP status is 200.
- Redirects remain within the approved PayPal host and resolve to an expected Markdown identity.
- The media type and body are compatible with plain text or Markdown.
- The body is non-empty and above a conservative minimum size.
- The body is not an HTML shell, HTML error page, access-denied page, or known not-found wrapper.
- The page does not unexpectedly contain another catalog instead of documentation content.
- The raw destination remains beneath `raw/paypal-new/`.

Validation occurs in staging. A rejected response is logged but never written into the accepted raw tree. Promotion never overwrites a file. If a same-day destination already exists with the same content hash, the result is unchanged. If it contains different content, the collector selects the next immutable revision suffix.

## Retry and Recovery

Retrying failures creates a new collection run rather than reopening or editing the prior run. The new run references `retry_of`, the same inventory hash, and the terminal failure records that selected its queue.

```bash
python scripts/fetch_paypal_new.py retry --run <collection-run-id>
```

Only `http-failed`, `network-failed`, and optionally reviewed `invalid-content` records are eligible. Successful and unchanged pages are never downloaded merely because a retry run was requested. Aggregate inventory status is derived across all runs bound to the same inventory.

## CLI Contract

The first version provides:

```bash
python scripts/fetch_paypal_new.py discover
python scripts/fetch_paypal_new.py collect --inventory <pages.jsonl>
python scripts/fetch_paypal_new.py collect --inventory <pages.jsonl> --limit 10
python scripts/fetch_paypal_new.py retry --run <collection-run-id>
python scripts/fetch_paypal_new.py status --inventory <pages.jsonl>
```

`discover` seals a collection plan. `collect` consumes that exact plan. `retry` creates a new run for terminal failures. `status` derives aggregate counts and unresolved pages without changing source records. A combined `sync` command is deferred until the two phase-specific commands have proven reliable.

## Collection and Ingest Boundary

The collector ends after raw promotion, terminal reconciliation, and a user-facing summary. It does not create or edit wiki source pages, indexes, concepts, comparisons, analyses, or ingest logs.

Later ingest follows `rules/ingest.md`: one raw file is read completely, concept placement is audited, wiki pages are updated, validation runs, and only then may the next raw file begin. The frozen inventory and collection logs may order the ingest queue, but they do not authorize batch ingest.

## Rules and Documentation Changes

Implementation updates only the rules needed to make the new workflow discoverable and accurate:

- Add `rules/psp/paypal-new.md` as the provider-specific contract mapped to `scripts/fetch_paypal_new.py`.
- Update `rules/psp-collection.md` so it defines shared PSP collection invariants and permits standalone provider collectors instead of claiming all providers use one generic script.
- Update the `CLAUDE.md` directory tree and Workflow Index to route PayPal-new collection to its provider rule.
- Leave `AGENTS.md` as the thin pointer to `CLAUDE.md` and `rules/`.
- Keep the existing `rules/psp/paypal.md` path temporarily, but label it explicitly as PayPal.ai to prevent confusion. Renaming other provider rules or rewriting their collectors is outside this phase.

The PayPal-new provider rule documents discovery sources, first-link parsing, sitemap policy, canonical URL rules, raw layout, CLI commands, validation, retry, smoke-test, and collection-to-ingest boundary. It links to the generic rule rather than duplicating generic invariants.

## Testing Strategy

Deterministic unit and integration-style fixture tests cover:

- Root-to-child and recursive catalog traversal.
- Cycle detection and duplicate catalog links.
- First-link extraction when a bullet description contains additional Markdown links.
- Canonical URL normalization, fragments, unknown query parameters, and external links.
- Duplicate page merging with multiple `discovered_from` values.
- Path-preserving raw mapping and collision rejection.
- Stable sorting and identical inventory hashes for identical inputs.
- Missing, malformed, or changing catalogs preventing inventory sealing.
- Sitemap-only and catalog-only audit output without sitemap scope expansion.
- Manifest tampering causing `collect` to refuse execution.
- HTML 404, access-denied, empty, and catalog-shaped response rejection.
- New, changed, unchanged, and same-day revision behavior.
- Retry selection excluding prior successes.
- Terminal-state reconciliation and aggregate status across runs.
- Enforcement that no page raw file is written during discovery and no wiki file is written during collection.

Network smoke testing uses a small deterministic sample spanning multiple catalogs. It is separate from the default test suite, does not assert unstable corpus counts, and must pass before a full initial collection is proposed.

## Acceptance Criteria

The design is implemented successfully when:

1. A discovery run starts from the root catalog and dynamically traverses every reachable same-host catalog without a hard-coded section list.
2. Every catalog and the sitemap are preserved in an immutable discovery snapshot with hashes and retrieval metadata.
3. The script produces a deterministic complete `raw-md-links.txt` and machine-readable `pages.jsonl` before downloading a page body.
4. Collection refuses incomplete, unstable, malformed, or hash-mismatched inventories.
5. Sitemap-only URLs are visible but excluded from the initial download queue.
6. Accepted pages preserve their canonical path beneath `raw/paypal-new/` and never overwrite prior versions.
7. Invalid or HTML responses never enter the accepted raw tree.
8. Every selected page has one terminal result, and run totals reconcile exactly.
9. A retry run selects only eligible failures and preserves all earlier run records.
10. Collection never starts ingest or edits the wiki knowledge layer.
11. The rules clearly route PayPal-new to its standalone collector without changing `AGENTS.md` into a second source of truth.

## Comparison Readiness

Collection preserves canonical URLs, normalized path identities, catalog titles, discovery memberships, content hashes, and version history. These fields are sufficient inputs for a later deterministic candidate crosswalk between legacy PayPal and PayPal-new.

That later comparison should be a separate derived workflow. It may combine exact path matches, normalized title matches, redirect evidence, and semantic review, but it must not rename or merge raw files merely to force an old-versus-new match.
