# PSP: Braintree — documentation collection profile

> Approved historical design restored on 2026-09-15 from the “Collect PayPal new docs” task (019f5498-f600-7472-b942-8b290fbb127b). Read with [psp-collection.md](../psp-collection.md). A minimal standalone `scripts/fetch_braintree.py` was added for the September 16 smoke pilot. Do not run `fetch_psp.py braintree`; full collection still requires separate approval.

## Scope and discovery

- English canonical documentation under `https://developer.paypal.com/braintree/` only; GitHub repositories follow a separate workflow.
- Reconcile `https://developer.paypal.com/braintree/llms.txt` with `https://developer.paypal.com/braintree/sitemap.xml` into one deduplicated inventory. Preserve which catalog(s) advertised each URL and report catalog-only and sitemap-only entries.
- Resolve relative links and remove fragments from page identity. Keep concrete SDK/platform/version paths distinct. Record out-of-scope entries rather than silently counting them as collected.
- Fetch and preserve both discovery inputs before collection. A failed discovery input must be reported as incomplete coverage, not an empty successful catalog.

## Markdown transport

The previously verified convention inserts `/md/` after `/braintree/`, rather than appending `.md`:

```text
/braintree/docs/start/overview
  -> /braintree/md/docs/start/overview
/braintree/articles/control-panel/overview
  -> /braintree/md/articles/control-panel/overview
```

Preserve the human-facing canonical URL separately from the Markdown fetch URL. Reconfirm these routes with a small live sample before implementing or running full collection; historical route success is not proof of current availability.

## Three-stage collection and path recovery

This is **one initial collection plus two fallback rounds**, not three identical HTTP retries:

1. **Initial collection:** fetch the concrete canonical targets in the reconciled inventory through the Markdown route.
2. **Node fallback:** for unresolved targets whose route family supports SDK variants, try appending `/node` before deriving the Markdown URL.
3. **Other SDK fallbacks:** for remaining eligible unresolved targets, try applicable `/ios/v7/`, `/javascript/v3/`, and `/android/v5/` variants.

Those suffixes come from the user's historical collection experience. Validate their current applicability before full collection; do not blindly append them to every URL or to already versioned SDK routes. Record non-applicable or unresolved cases for review. Successful targets are not downloaded again in subsequent rounds.

Different SDK variants are distinct documents, not interchangeable fallback bodies. Each successful variant retains its full canonical path and gets its own raw file. Record the relationship from the failed logical parent to the recovered variants; never store Node, iOS, Android, or JavaScript content under the parent's identity. A recovered variant does not prove coverage of other SDK variants.

Keep network retry attempts separate from the three routing stages in logs. This recovered design does not prescribe an additional “three retries per candidate” multiplier.

## Raw storage, validation, and reporting

- Preserve documentation paths beneath `raw/braintree/`, excluding the host and leading `/braintree/`; retain SDK/version segments. Store dated files, for example `raw/braintree/docs/start/overview-YYYY-MM-DD.md`.
- Store discovery snapshots separately beneath `raw/braintree/_discovery/`; inventories, attempt records, failure lists, and summaries belong in `tracking/collections/braintree/`.
- Before accepting raw, verify HTTP success, expected document identity, and non-empty Markdown/plain-text content. Reject HTML shells, access-denied/not-found wrappers, and unrelated redirects even when HTTP status is 200.
- Accepted raw is immutable. Compare content hashes; unchanged content produces no new version. Retain all changed versions and never overwrite an existing same-date snapshot.
- Record original target, candidate canonical URL, actual fetch URL, routing stage, HTTP attempt/result, local path, and content hash. Record parent-to-variant recovery explicitly.
- Summarize original inventory coverage separately from additional SDK documents. Every selected original target must be accounted for as collected/unchanged, recovered through listed variants, or failed. Keep unresolved candidates in the failure list; do not report complete corpus coverage merely because the run exited successfully.

## Execution boundary

Current commands (run serially, one collector process per provider):

```bash
python3 scripts/fetch_braintree.py discover
python3 scripts/fetch_braintree.py collect --inventory tracking/collections/braintree/inventories/<id>/inventory.json --smoke
# Only after full-collection approval:
python3 scripts/fetch_braintree.py collect --inventory tracking/collections/braintree/inventories/<id>/inventory.json --all
```

Discovery retains `in-person` and GraphQL documentation, not just `docs` and `articles`; literal `$` placeholder routes are recorded as excluded. Historical/deprecated pages are not silently excluded. The fixed smoke selection has five parent targets covering articles, start, Node recovery, three client SDK variants, and GraphQL. Recovery probes are limited to unqualified `docs/guides` and `docs/reference` routes, excluding overview and already SDK-qualified routes. One HTTP attempt per candidate is recorded; there is no additional network retry multiplier. The implemented canonical validator rejects ambiguous queries and unsafe paths for explicit review.

Each run stores its selected target list, inventory hash, attempt ledger, parent results, and summary. Hashes of the inventory and discovery snapshots are checked before collection. A run can finish with failed targets: read the summary and attempts, not just the exit status. No automated resume/retry command is implemented yet. Successful variants are individually named; a parent marked recovered does not establish complete cross-SDK coverage. Incomplete interrupted runs retain their ledgers for review.

Implement only the minimum provider-specific collector needed for this policy; reuse existing versioning/reporting helpers where practical. Do not refactor unrelated PSP collectors.

Before full collection, run a small sample covering direct Markdown, Node recovery, other applicable SDK variants, and failure reporting. Confirm unchanged detection and report results for approval. Collection ends at raw files plus collection records; it never starts ingestion or edits company, source, concept, or wiki index pages.
