# Provider rule: PayPal-new developer documentation

> Main-checkout documentation restored on 2026-09-15. **Implementation and collected data remain in `.worktrees/paypal-new-collection/`; this update does not merge them.** All commands and raw/tracking paths below are relative to that worktree, not main. Recheck worktree status before execution. Read this main profile as the maintained policy; the worktree copy is its historical implementation reference.
>
> Use this provider rule with `rules/psp-collection.md`. It governs the upgraded documentation on `developer.paypal.com` through `scripts/fetch_paypal_new.py`.

## Identity and boundary

- Provider ID: `paypal-new`
- Documentation host: `https://developer.paypal.com`
- Raw root: `raw/paypal-new/`
- Tracking root: `tracking/collections/paypal-new/`
- Collector: `scripts/fetch_paypal_new.py`

Keep this corpus separate from the legacy PayPal raw collection and from `docs.paypal.ai`, which continues to follow `rules/psp/paypal-ai.md`. Collection does not create PayPal company, concept, source, index, comparison, analysis, or ingest-log pages.

## Discovery authority

- Root catalog: `https://developer.paypal.com/llms.txt`
- Coverage audit: `https://developer.paypal.com/sitemap.xml`
- Follow every same-host `llms.txt` reached from the root, recursively and with cycle protection.
- Do not hard-code the current section names or counts.
- For each Markdown bullet, select only the first link. Links in its description are metadata, not extra page targets.
- Re-fetch all catalogs after traversal. A missing, malformed, redirected, or changed catalog prevents inventory sealing.

## Transport and route validation

Live verification on 2026-07-15 showed that PayPal's edge can return two different corpora for the same root URL: the new nested catalog and a legacy flat document. Protocol and User-Agent headers alone do not select the route consistently. The collector therefore uses a stateful `curl_cffi` browser session, rotates fresh sessions with cache-busted root probes until the root contains same-host child `llms.txt` catalogs, and then reuses only that accepted session for the complete traversal. The session is safe for the collector's threaded page downloads.

Install the provider-specific, Python-3.9-compatible dependency into the environment that will run the collector:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-paypal-new.txt
```

The dependency remains provider-specific; Stripe, Adyen, legacy PayPal, PayPal.ai, Braintree, and other collectors keep their own transport logic.

The route qualifier makes up to 20 fresh-session root probes and records every probe in the root attempt facts. The longer window limits false failures from PayPal's probabilistic edge assignment; rejected legacy responses do not incur backoff. After qualification, catalog requests retain four-attempt retry behavior, including transient legacy 404 responses for a child catalog that the new root explicitly advertises. If qualification or any required catalog still fails, discovery writes only `.staging-<discovery-id>` diagnostics and exits nonzero. Rerun discovery later; never seal a partial hierarchy, substitute sitemap pages, or collect from a failed run.

## Frozen inventory

`discover` must finish before any documentation body is fetched. It preserves every catalog and the sitemap beneath:

```text
raw/paypal-new/_discovery/<discovery-id>/
```

It writes the sealed queue and audit artifacts beneath:

```text
tracking/collections/paypal-new/inventories/<discovery-id>/
```

`raw-md-links.txt` is the deterministic one-URL-per-line Markdown queue. `pages.jsonl` is the authoritative inventory with canonical URL, Markdown URL, raw identity, titles, fragments, catalog memberships, and selection state. The manifest hashes every inventory artifact and the raw discovery manifest. Collection must reject unsealed, partial, unstable, or hash-mismatched input.

Failed discovery writes only non-sealed `.staging-<discovery-id>` diagnostics under tracking. It never produces an accepted inventory or raw discovery snapshot.

## Canonical URL and raw path

- Select only HTTPS pages on `developer.paypal.com`.
- Remove `.md`, fragments, and known tracking parameters from canonical identity; retain fragments as metadata.
- An unknown query parameter blocks sealing rather than being silently discarded.
- Merge duplicate canonical pages while retaining every title and `discovered_from` catalog.
- Derive the fetch URL by appending `.md` to the canonical URL.
- Preserve every canonical path segment beneath `raw/paypal-new/`.

Example:

```text
https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/additional-parameters
  -> raw/paypal-new/api/nvp-soap/payflow/integration-guide/
     additional-parameters-YYYY-MM-DD.md
```

Accepted raw files are immutable. Unchanged content creates no new file. A second distinct version collected on the same date uses `-r2`, then `-r3`.

## Commands

```bash
# Traverse all catalogs, snapshot them, audit the sitemap, and seal the queue.
.venv/bin/python scripts/fetch_paypal_new.py discover

# Collect the complete sealed queue only after the smoke gate is approved.
.venv/bin/python scripts/fetch_paypal_new.py collect \
  --inventory tracking/collections/paypal-new/inventories/<discovery-id>/pages.jsonl

# Retry eligible failures from a prior run without downloading successes again.
.venv/bin/python scripts/fetch_paypal_new.py retry --run <collection-run-id>

# Derive aggregate status across runs bound to one inventory.
.venv/bin/python scripts/fetch_paypal_new.py status \
  --inventory tracking/collections/paypal-new/inventories/<discovery-id>/pages.jsonl
```

## Validation and retry

Accept a page only when it returns HTTP 200, stays on the expected PayPal Markdown identity, uses a supported plain-text/Markdown media type, and has a non-empty documentation-shaped body. Reject HTML shells, HTML or Markdown not-found wrappers, access-denied pages, unexpectedly short bodies, and catalog-shaped responses before raw promotion.

Every network attempt and exactly one terminal page result are appended to the run ledger. Terminal states are `new`, `changed`, `unchanged`, `http-failed`, `network-failed`, `invalid-content`, and `path-conflict`. Run totals must reconcile exactly.

`retry` creates a new immutable run. It selects HTTP/network failures and pages missing a terminal result. `invalid-content` requires the explicit `--include-invalid-content` option after review. It never reopens or rewrites the prior run.

## Sitemap audit

The `llms.txt` hierarchy defines the initial selected queue. The sitemap is preserved and compared with it:

- Catalog-only pages stay selected and are reported.
- Sitemap-only pages are written to `sitemap-only.txt` but are not downloaded automatically.
- Promoting sitemap-only URLs requires a separately reviewed supplemental inventory or a later rule change.

## Smoke-test gate

After successful discovery, collect a deterministic ten-page sample spanning catalogs:

```bash
.venv/bin/python scripts/fetch_paypal_new.py collect \
  --inventory tracking/collections/paypal-new/inventories/<discovery-id>/pages.jsonl \
  --limit 10 \
  --workers 2
```

Run the same smoke selection again to prove unchanged detection and raw immutability. Report its terminal counts, failures, raw paths, and validation results. Stop and request approval before collecting the complete multi-thousand-page inventory.

## Collection to ingest boundary

Every command in this collector stops after discovery or raw collection records. It never starts ingest. A successful discovery or smoke run does not authorize full collection or ingest.

When ingest is later requested, follow `rules/ingest.md`: read one raw file completely, audit existing concepts and source placement, update the wiki, validate it, and only then move to the next raw source. Never batch-ingest this corpus.

## Comparison readiness

The later historical suggestion to map missing Markdown API exports to existing OpenAPI evidence, with HTML only as a last fallback, was not approved as a collection extension. Do not automatically fetch HTML, collect repositories, or create a new `paypal-new-*` concept hierarchy. Those decisions remain separate from this collection policy.

Preserve canonical URL, path identity, titles, catalog memberships, content hash, and raw-version history. A later legacy-versus-new PayPal crosswalk is derived from those facts; it must not rename, replace, or merge either raw corpus.
