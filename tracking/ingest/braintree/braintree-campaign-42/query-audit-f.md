# Braintree C42 fixed-query audit — Group F

- Campaign: `braintree-campaign-42`
- Assigned manifest positions: 21–24
- Started (UTC): `2026-10-07T00:57:00Z`
- Completed (UTC): `2026-10-07T01:04:54Z`
- Verdict: **PASS — 8/8 fixed questions passed**

## Shared checks

- **Pins and ownership — PASS.** Recomputed SHA-256 values match the manifest for Android testing/go-live `2050d3a0…82e9`, Android Vault `16c02b57…5fd2`, Apple Pay iOS `e8b6fc6b…627c`, and lodging Node `f4ec9428…6712`. Each manifest URL equals its source frontmatter URL and raw Source URL; every pin has exactly one `raw_files` source owner.
- **Full reads, bounded authority and routes — PASS.** The four canonical sources and four pinned raws were read completely. One actual root → Braintree index → concept → source → raw route is recorded per page below; position 22 uses the existing Braintree PayPal integration hub to reach the main PayPal Vault concept. Every source/main-concept pair is reciprocal. No related-raw section exists on these sources, and exact-path/URL sweeps found no conflicting owner or alternate copy. The nearby Google Pay testing filename and other SDK/platform variants were not used as authority.
- **Non-inference and deferred close work — PASS.** No current-provider, sibling-platform, direct PayPal/Apple, package/GitHub, eligibility, execution, settlement, funding, or interchange-result inference was imported. Routine examples, fields, validation codes, and setup steps remain at precise raw locators. Direct provider-index source rows and company/catalog aggregation are absent but are the campaign-wide coordinator-close task, not a selected-page content failure. Extra factual authority reads: none.

## Position 21 — `docs-guides-paypal-testing-go-live-android-v5`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:718` → `wiki/concepts/braintree-android-sdk.md:74` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-testing-go-live-android-v5.md:12-42` → `raw/braintree/docs/guides/paypal/testing-go-live/android/v5-2026-09-16.md:1-289`.

1. **PASS — Exact scope and non-inference.** This is Braintree's captured **Android v5 website route** for mocked versus linked PayPal Sandbox testing, eligibility-conditioned App Switch testing, and the separate server-side move to Braintree Production. It does not state an exact Android package release and does not prove current SDK behavior, account linking or eligibility, payment success, settlement, deposit, or funding. Evidence: source `:14-22`; raw `:14-48,93-103,163-188,282-286`.
2. **PASS — Central action, material conditions, warnings, and detail route.** Mocked testing stays in Braintree Sandbox; linked testing needs a same-country PayPal Business Sandbox account/app and must not use the business account as buyer, while some fake nonces may stop working. Sandbox state and credentials do not transfer; Production requires recreated settings and server credentials, then only limited low-value real-method sales submitted for settlement and checked through deposit, with real debits and fees. The source preserves the flattened App Switch use-case ambiguity and the out-of-place JS-SDK sentence instead of treating either as Android behavior. Exact setup, cases, credentials, server examples, and live-test cautions remain at source `:24-33` and raw `:51-160,163-279,282-286`.

## Position 22 — `docs-guides-paypal-vault-android-v5`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:729` → `wiki/concepts/paypal-braintree-integration.md:145` → `wiki/concepts/paypal-vault.md:335` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-vault-android-v5.md:12-40` → `raw/braintree/docs/guides/paypal/vault/android/v5-2026-09-16.md:1-327`.

3. **PASS — Exact scope and non-inference.** This is Braintree's collected **Android SDK v5 website guide** for a PayPal pre-approved vaulted-payment flow, with a captured `com.braintreepayments.api:paypal:5.2.0` dependency example. It is not the standalone PayPal Android SDK or Payment Method Tokens API, and the example coordinate and dated guide do not prove current compatibility, merchant/buyer eligibility, vault success, or a later charge outcome. Evidence: source `:14-23`; raw `:14-30,55-73`.
4. **PASS — Central action, material conditions, warnings, and detail route.** The app initializes `PayPalLauncher`/`PayPalClient`, creates and launches a `PayPalVaultRequest`, persists the pending request, handles the return, and tokenizes success to `PayPalAccountNonce`, with cancellation/failure as separate outcomes. The source retains the March 30, 2026 certificate warning as snapshot wording, requires device data for non-recurring Vault transactions, warns that Vault itself does not show amount/currency, and preserves the raw's `>SINGLE_TOP` prose versus `SINGLE_TOP` code-comment conflict. Exact code, shipping/support statements and app-switch navigation remain at source `:25-31` and raw `:75-191,193-324`.

## Position 23 — `docs-guides-apple-pay-client-side-ios-v7`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:708` → `wiki/concepts/braintree-apple-pay.md:22` → `wiki/sources/braintree/source-braintree-docs-guides-apple-pay-client-side-ios-v7.md:12-39` → `raw/braintree/docs/guides/apple-pay/client-side/ios/v7-2026-09-16.md:1-335`.

5. **PASS — Exact scope and non-inference.** This is a captured Braintree **iOS v7 custom client-side Apple Pay website guide**: PassKit request and authorization are tokenized by Braintree into a nonce for merchant-server processing. It explicitly excludes iOS v7 Drop-in and is not direct Apple authority, a current certificate/support statement, present merchant/device/network eligibility, or payment success. Evidence: source `:14-22`; raw `:17-24,32-94,115-143,291-324`.
6. **PASS — Central action, material conditions, warnings, and detail route.** After certificate/Merchant ID setup, the app checks availability, builds a `PKPaymentRequest`, keeps manual request values synchronized with gateway/environment configuration, presents Apple Pay, tokenizes `PKPayment`, sends the nonce server-side, and reflects the server `Transaction.sale` result. The source retains Drop-in lifecycle dates, the already-past certificate notice as captured wording, and MPAN's iOS 16+/Visa-recurring qualification plus possible DPAN fallback for unsupported networks. Exact request fields and recurring/automatic-reload/deferred examples remain at source `:24-30` and raw `:55-69,145-258,261-335`.

## Position 24 — `docs-reference-general-lodging-data-node`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:715` → `wiki/concepts/braintree-server-sdk.md:53` → `wiki/sources/braintree/source-braintree-docs-reference-general-lodging-data-node.md:12-43` → `raw/braintree/docs/reference/general/lodging-data/node-2026-09-16.md:1-263`.

7. **PASS — Exact scope and non-inference.** This is an **unversioned Braintree website Node.js reference** for optional lodging industry data, with displayed callback and Promise `gateway.transaction.sale()` examples. Its possible lower-interchange statement is limited to qualifying US-merchant Visa/Mastercard transactions and account eligibility must be checked with Customer Success; it is not a current Node package, eligibility, rate, authorization, settlement, funding, or interchange-outcome claim. Evidence: source `:14-22`; raw `:14-23,121-189`.
8. **PASS — Central action, material conditions, warnings, and detail route.** The examples send `industryType: Transaction.IndustryData.Lodging` plus lodging `data`; only one industry type is allowed, and the four highlighted fields are required **to qualify for reduced interchange**, not unconditionally required request properties. The source preserves damaged operation prose, table snake_case versus example camelCase, additional-charge uniqueness/required fields, and validation-code boundaries without converting the catalog into current SDK/runtime behavior. Exact field shapes, examples and errors remain at source `:24-34` and raw `:24-118,121-189,191-263`.

## Close result

No affected-question correction is required. All four pages preserve exact Braintree website/SDK-family scope, central action, material qualifications and warnings, non-inference boundaries, reciprocal main-concept discoverability, and a precise raw detail route.
