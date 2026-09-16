# PSP: Legacy PayPal developer documentation — collection profile

> Historical policy restored on 2026-09-15 from the “Collect PayPal new docs” discussion (019f5498-f600-7472-b942-8b290fbb127b) and its attached legacy catalog. Read with [../psp-collection.md](../psp-collection.md). **No dedicated legacy collector is implemented in main.** This is not the PayPal.ai or PayPal-new policy.

## Historical discovery and Markdown convention

- The historical catalog was served at `https://developer.paypal.com/llms.txt`. The same URL now also identifies the upgraded portal; do not assume a fresh response is the old corpus. Preserve and identify the actual catalog used before collection.
- The user supplied the legacy catalog in attachment `1a894153-66d1-4ccc-af18-b9ab12626fb5/pasted-text.txt`. Its publisher guidance was to insert `/md/` before `/docs/`, for example `/docs/checkout/standard/` → `/md/docs/checkout/standard/`, rather than append `.md`.
- Resolve relative links against the official host. Deduplicate fragment-level links to the same page while preserving fragment metadata and titles. Do not infer one raw file per heading.
- The attachment identifies `/api/rest/`, `/guides/integrate-checkout/`, and `/sdk/js/` as important route families, but does not establish their Markdown transformation. Validate them individually rather than inventing an append-`.md` rule.
- The attachment suggests `/archive/` and `/deprecated/` routes can generally be ignored. This is publisher guidance, not permission to delete existing raw: explicitly report any exclusions in the chosen inventory. Confirm collection scope before omitting historical coverage the user wants.
- Braintree is delegated to its own `llms.txt` and [braintree.md](braintree.md); it is not covered by this profile.

## Preservation and execution boundary

- Keep legacy, PayPal.ai, and PayPal-new identities separate, even when topics overlap. Existing `raw/paypal-*` filenames alone do not establish the origin; consult Source URL metadata before classifying them.
- Preserve accepted raw byte-for-byte and retain all existing versions. New collection compares content against the correct prior page; unchanged content adds no version, changed content must not overwrite history.
- Before any legacy collection, confirm the available old routes with a small sample, define the inventory and destinations, and verify Markdown content rather than HTTP status alone. Reject error/HTML wrappers and unrelated redirects; record failed pages and actual fetch URLs.
- The exact standalone collector, new raw layout, and retry policy were not implemented in the prior PayPal-new work. Do not invent a working CLI command or reuse the `.ai` command for this corpus.
- Collection stops before ingestion. This restored profile neither moves old raw nor creates wiki sources, concepts, or indexes.
