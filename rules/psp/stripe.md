# PSP: Stripe — collection profile

> Used with [psp-collection.md](../psp-collection.md) and `scripts/psp_config.toml`. Historical catalog-union design restored on 2026-09-15 from the “Collect PayPal new docs” task (019f5498-f600-7472-b942-8b290fbb127b). **The approved policy below exceeds current script support; restoring it does not implement or run collection.**

## Docs collection

| Field | Value |
| --- | --- |
| Doc host | `docs.stripe.com` |
| Discovery inputs | `https://docs.stripe.com/llms.txt` and `https://docs.stripe.com/sitemap.xml` |
| Full corpus | Not used by this policy; availability was last checked in the older 2026-06-02 profile |
| `.md` rule | Append `.md` to any doc URL, e.g. `https://docs.stripe.com/payments/quickstart.md` |
| Raw filename | `raw/stripe-<slug>-YYYY-MM-DD.md` |

Notes:
- `llms.txt` opens with a Stripe-authored instruction header (about checking npm/pip for the latest SDK version) before the `## Docs` link list — skip the header, parse the link list.
- Sections include Payments, Checkout, Payment Methods, Link, Billing, Elements, Connect, Issuing, Radar, Terminal, Tax, Invoicing, Identity, Financial Connections, and Treasury. Discover current sections dynamically; do not hard-code historical page counts. `--section` is not implemented in the current script.

## Approved discovery and collection policy

1. Fetch and preserve both discovery inputs. If the sitemap is an index, follow its in-scope child sitemaps. A failed input means incomplete discovery, not an empty successful catalog.
2. Resolve links and select English canonical documentation on `docs.stripe.com`. Normalize page versus `.md` identity, remove fragments, and deduplicate while retaining original URLs and discovery memberships. Do not silently collapse meaningful query variants; unresolved identities must be reported for review.
3. Form the **union** of in-scope llms and sitemap pages. Report overlap, llms-only, sitemap-only, and excluded entries. Unlike the PayPal-new audit-only sitemap policy, Stripe's approved policy includes in-scope sitemap-only documentation targets.
4. Save the reconciled inventory before fetching bodies. Derive each Markdown fetch URL by appending `.md` once. Do not treat sitemap assets, external links, or non-English variants as documentation targets.
5. Fetch and validate each selected page before accepting raw. Reject HTML shells, empty/error pages, and unrelated redirects even if HTTP status is 200. Record failures rather than saving them as documentation.
6. Compare content with the prior raw version. Unchanged content creates no new snapshot; new or changed content creates a dated immutable raw file. Preserve all prior versions and never overwrite an accepted file.
7. Record per-page outcomes, fetch/canonical URLs, local raw paths, and failures. Reconcile selected targets against successful, unchanged, and failed outcomes before reporting coverage. Collection stops before ingestion.

This restores the discovery policy only. Existing flat Stripe raw paths remain unchanged; no directory migration, new framework, or full collection is authorized by this document update.

## Current implementation boundary

- `python scripts/fetch_psp.py stripe` currently reads only the configured `llms.txt`, extracting absolute links already ending in `.md`. It does **not** implement the sitemap union or the complete validation/reporting policy above.
- Supported scoping options are `--source`, `--limit`, and `--dry-run`; `--from`, `--section`, and `--urls` are not implemented in this script.
- A successful legacy-script run proves only its selected llms targets were attempted, not full union coverage. Inspect its error list and discovery results separately from its exit code.
- Implement and validate the missing policy before claiming full Stripe documentation coverage. First verify a small sample from overlap, llms-only, and sitemap-only groups that actually exist, including unchanged detection and failure reporting; obtain approval before full collection. Do not refactor unrelated PSP collectors.

## Known `url_fixups`

- None confirmed yet. Add `[pattern, replacement]` pairs to the `[stripe]` table in `psp_config.toml` as malformed links are found during runs.

## Known GitHub integration repos (manual path — see `github-repos.md`)

Not in `llms.txt`; ingest via the GitHub repo workflow:
- `stripe/stripe-node` (`raw/github-stripe-node.md`)
- `stripe/stripe-ios` (`raw/github-stripe-ios.md`)
- `stripe/stripe-android` (`raw/github-stripe-android.md`)
- `stripe/stripe-react-native` (`raw/github-stripe-react-native.md`)
- `stripe/react-stripe-js` (`raw/github-react-stripe-js.md`)
- Stripe Postman collection (`raw/github-stripe-postman.md`)

## Wiki placement

- Per-PSP index: `wiki/stripe-index.md`
- Company page: `wiki/companies/stripe.md`
- Platform concepts: `stripe-*` (e.g., `stripe-radar`, `stripe-payment-intents`)
