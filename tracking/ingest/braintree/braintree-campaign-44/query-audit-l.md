# Braintree C44 fixed-query audit — group L

- Scope: approved C44 positions 45–48; eight predetermined queries.
- Result: **PASS — 8/8 queries**.
- Completed UTC: `2026-10-07T13:09:44Z`

## Shared checks

- **Approval, pins and provenance — PASS.** Fastlane Setup, Guides Overview, and Generic Webhook Reference are approved at attempt 1; Reports Overview is approved at attempt 2 after its optional-grouping wording and central reporting route were corrected. Recomputed SHA-256 matches the manifest: `8ccff6b371491f21328b7af93e6f4ba90d61278376fe1aac45c0c34621cd7c16`, `66d856e8008b7f264a1b91ad9afa71347c545ca05b4df24881dd718d3d8af50e`, `b488055c857a800fb299781880be7315c1eddd585440bb4a8fc23ceb2938a6d5`, and `31226ffd1f1d180bad3055c326b0dc419b2d3da831b29b399774a964f8d4e2ed`. Manifest URL, source `canonical_url`, raw `Source URL`, `raw_files`, and `Raw Sources` agree; each raw records `Fetched: 2026-09-16` and `Discovery: llms.txt,sitemap.xml`. Promoted source content matches its accepted candidate (JSON extraction adds only a terminal blank line where present).
- **PRIMARY ownership, provenance and reciprocity — PASS.** Each exact primary raw path and canonical URL has one source owner; none is duplicated as supporting raw. Routes resolve through `wiki/index.md:11`, the Braintree provider index concepts at `wiki/braintree-index.md:846,865,871,883`, the reciprocal concept entries, the source, and the exact primary raw. Direct provider-catalog entries also exist at `wiki/braintree-index.md:65-68`. Source-to-concept reciprocity is present at source lines `36`, `36`, `37`, and `37`; deferred catalog work is therefore not a query failure.
- **Full reads and bounded gap sweep — PASS.** The root/provider indexes, four sources, four pinned raws, and the relevant Fastlane, payment-platform, reporting, webhooks, and Control Panel concepts were read. One bounded filename/topic sweep covered the linked Fastlane implementation routes, reporting siblings, Control Panel reporting overview, and generic webhook creation/parsing routes. The primary raws are sufficient for all retained claims; those sibling raws remain navigation only, so no supporting raw was used without a full evidentiary read. No illustrative syntax creates a false claim, material misuse, or runnable/outcome guarantee.

## Position 45 — `docs-guides-fastlane-setup-integration` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:846` → `wiki/concepts/paypal-fastlane.md:91` → `wiki/sources/braintree/source-braintree-docs-guides-fastlane-setup-integration.md` → `raw/braintree/docs/guides/fastlane/setup-integration-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's captured 2026-09-16, unversioned website setup page for enabling PayPal Fastlane in a Braintree Sandbox account. It identifies no exact Web, PHP, Ruby, client, or server SDK/package version; its account object/action is to create a Sandbox account if needed and turn on Fastlane under Account Settings → Customer Checkout. Do not infer Production or current eligibility/enablement, saved-profile or payment-method lifecycle, implementation steps hidden in the diagram, authentication, tokenization, Vault storage, or payment execution. Source `:14-16,20-23`; raw `:17-23,27-47`.
2. **Purpose, action, conditions, warnings and detail route — PASS.** The page is an enablement orientation: establish the Sandbox account, turn on Fastlane, review the CSP warning after recent SDK changes, use the advanced-options route for exact CSP configuration, and continue to the client-side guide. The PHP/Ruby bullets are change-summary notes, not setup code or a version guarantee. Source `:20-31`; raw `:17-23,27-33,38-47`.

## Position 46 — `docs-guides-overview` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:865` → `wiki/concepts/braintree-payment-platform.md:28` → `wiki/sources/braintree/source-braintree-docs-guides-overview.md` → `raw/braintree/docs/guides/overview-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's captured 2026-09-16, unversioned developer-guides landing page, not a product, API, or SDK contract. Its documentation objects are Basics, Payment Method Types, Tools, and Additional Features, and its action is navigation between quick-start guidance and the separate API reference. It names no SDK/version, client/server placement, environment, account qualification, payment object, or executable operation. Do not infer current payment-method support or eligibility, product prerequisites, security properties, successful integration, timing, or operational outcomes. Source `:14,18-22`; raw `:14-40`.
2. **Purpose, action, conditions, warnings and detail route — PASS.** The central purpose is fast familiarization with essentials; readers seeking customization or API mechanics are directed to the reference section. The four category descriptions are orientations only, with no material prerequisite or guarantee to import. Source `:14,18-31`; raw `:16,18,23-40`.

## Position 47 — `docs-guides-reports-overview` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:883` → `wiki/concepts/payment-reconciliation-reporting.md:111` → `wiki/sources/braintree/source-braintree-docs-guides-reports-overview.md` → `raw/braintree/docs/guides/reports/overview-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's captured 2026-09-16, unversioned reports overview spanning API-facing reporting and additional Control Panel support routes. It names no SDK language/version, client/server responsibility, environment, account type, or Control Panel role. Its objects/actions are date-scoped Settlement Batch Summary sales/credit totals with optional custom-field grouping, merchant-built transaction/customer reporting, and webhook-trigger information collected after receipt setup. Do not infer current eligibility, successful configuration or report generation, data completeness, delivery timing, reconciliation sufficiency, settlement, disbursement, funding, or payment execution. Source `:14,18-24`; raw `:16,19-26`.
2. **Purpose, action, conditions, warnings and detail route — PASS.** The page routes readers among three API reporting patterns and separate Control Panel reporting articles. The material conditions are that custom-field grouping is optional and webhook-based reporting starts only after webhook receipt is configured; subscription cancellation is only the supplied example. Dedicated pages own query fields, exports, delivery semantics, roles, timing, and account-specific eligibility. Source `:18-32`; raw `:16,19-26`.

## Position 48 — `docs-reference-general-webhooks-overview` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:871` → `wiki/concepts/braintree-webhooks.md:67` → `wiki/sources/braintree/source-braintree-docs-reference-general-webhooks-overview.md` → `raw/braintree/docs/reference/general/webhooks/overview-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's captured 2026-09-16, unversioned generic webhook-reference index, not a PayPal Commerce Channel API contract or language-SDK integration guide. Its object is a webhook notification with `kind`, `timestamp`, and one type-specific attribute; its actions are inspecting `kind` and parsing a notification, with invalid signature as the stated failure. It names no SDK/version, client/server implementation, environment, account qualification, acknowledgement, retry, or delivery-time contract. Do not infer product enablement, merchant eligibility, event occurrence, universal payload shape, delivery/order guarantees, or a specific parsing method. Source `:14,18-24`; raw `:16,19-56`.
2. **Purpose, action, conditions, warnings and detail route — PASS.** The page maps `kind` to trigger families, makes exact trigger conditions kind-specific, states the three common/type-specific attribute roles, and warns that parsing an invalid signature raises an exception. Category links are navigation; dedicated authorities own event-specific triggers and operational delivery semantics. Source `:18-32`; raw `:19-23,25-46,49-56`.

## Query tally

| Page | Q1 exact scope | Q2 purpose/actions/conditions/detail route |
| --- | --- | --- |
| Fastlane — Setup and Integration | PASS | PASS |
| Guides Overview | PASS | PASS |
| Reports Overview | PASS | PASS |
| Generic Webhook Reference Overview | PASS | PASS |

No correction or additional supporting authority is required. **Verdict: PASS — 4/4 pages, 8/8 fixed questions.**
