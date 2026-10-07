# Braintree Campaign 43 fixed-query audit — group G

## Shared checks

- Assignment **PASS**: fixed-query group G covers manifest positions 25–28 only: `docs-guides-functions-import-data`, `docs-guides-payment-methods-node`, `docs-guides-paypal-checkout-with-vault-android-v5`, and `docs-reference-client-reference-javascript-v2-browser-support`. This was a read-only audit; no repository file was edited.
- Manifest identity and integrity **PASS**:
  - Position 25: `https://developer.paypal.com/braintree/docs/guides/functions/import-data`; raw `raw/braintree/docs/guides/functions/import-data-2026-09-16.md`; SHA-256 `96c1c37bc65d95dc7fd094fa05786ad65c4c0b6bdb5bbc1beb795c6841e70c64`.
  - Position 26: `https://developer.paypal.com/braintree/docs/guides/payment-methods/node`; raw `raw/braintree/docs/guides/payment-methods/node-2026-09-16.md`; SHA-256 `83494f64cdcb0feb2d0f23fb6df5c3ea097760cbdfa406413957552bf0c0fc5f`.
  - Position 27: `https://developer.paypal.com/braintree/docs/guides/paypal/checkout-with-vault/android/v5`; raw `raw/braintree/docs/guides/paypal/checkout-with-vault/android/v5-2026-09-16.md`; SHA-256 `e4bbf5c6b66fb5c731248b5c1a3a7322feac2d6c827dad18bb4a255200313f63`.
  - Position 28: `https://developer.paypal.com/braintree/docs/reference/client-reference/javascript/v2/browser-support`; raw `raw/braintree/docs/reference/client-reference/javascript/v2/browser-support-2026-09-16.md`; SHA-256 `9f6388e6dc7414dd4e39361752e1e36ded2b50bd673dccea181a4bab00f7ca3a`.
- Primary ownership **PASS**: each canonical URL and each pinned raw path has exactly one owner under `wiki/sources/`, and every source frontmatter value matches the manifest.
- Route and reciprocity **PASS**: every actual retrieval path resolves as `[[index]]` → `[[braintree-index]]` → main concept → source → pinned raw. Each source links its main concept and each main concept links the source. Direct C43 source rows in `braintree-index`, company counts, provider log, and other close-time aggregate rows are deferred coordinator work and are not content failures.
- Full-read and bounded-gap sweep **PASS**: the root/provider indexes, four main concepts, all four source pages, and all four pinned raws were read. The filename/topic sweep found Functions siblings, payment-method operation references, Android PayPal one-time/recurring siblings, and JavaScript v2 configuration/best-practices siblings. None was needed for a retained claim or conflict; source-listed related raws remain explicitly unread navigation rather than evidence.

## Position 25 — `docs-guides-functions-import-data`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-docs-guides-functions-import-data]]` → `[[raw/braintree/docs/guides/functions/import-data-2026-09-16]]`.

1. **Scope — PASS.** This is a Braintree-hosted Functions documentation-preview snapshot fetched 2026-09-16 from a page created/updated 2025-04-01. It covers a `dataImport` Function, illustrative JavaScript, local CLI testing, and sandbox/production-qualified deployment. No exact CLI, package, SDK, hosted-runtime version, current support, account eligibility, deployment, entity creation, payment execution, settlement, or funding may be inferred. Raw: `raw/braintree/docs/guides/functions/import-data-2026-09-16.md:1-20,23-34,77-126`.
2. **Purpose/action and limits — PASS.** The retained route accurately covers initializing `MyImportFunction`, parsing an inbound payload, returning mapped transaction attributes, normal-validation failures returning `422` errors to the caller and console, local JSON testing, and deployment that defaults to Sandbox unless Production is selected. It preserves that the displayed JavaScript/config/deploy snippets contain rendering defects and are examples, not runnable-code or success guarantees. Exact commands, example fields and environment selection remain retrievable at raw lines 23–30, 31–76, 80–102 and 104–126.

## Position 26 — `docs-guides-payment-methods-node`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-payment-methods-node]]` → `[[raw/braintree/docs/guides/payment-methods/node-2026-09-16]]`.

1. **Scope — PASS.** This is a Braintree-hosted, unversioned Node.js-routed website snapshot fetched 2026-09-16. It defines customer-owned Vault payment methods and routes create, update, find, delete, and later token-based transaction creation, but names no exact Node SDK/package version. It does not prove present support, merchant/customer eligibility, account configuration, successful Vault storage, verification, transaction execution, or related-object delete effects. Raw: `raw/braintree/docs/guides/payment-methods/node-2026-09-16.md:1-16,19-47,52-147`.
2. **Purpose/action and limits — PASS.** The source preserves the existing-customer create route from a client-supplied single-object token, the separate Customer Create path, token use in Transaction Sale, the account-wide card-verification recommendation, default-method and billing-address update behavior, the returned find object, and payment-method deletion. It correctly treats callback/Promise snippets as examples and deletion as destructive only at the named method level; cascade, recovery and reversibility require the unread operation reference. Exact parameters and examples remain at raw lines 19–47, 52–114, 117–131 and 134–147.

## Position 27 — `docs-guides-paypal-checkout-with-vault-android-v5`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-android-sdk]]` → `[[source-braintree-docs-guides-paypal-checkout-with-vault-android-v5]]` → `[[raw/braintree/docs/guides/paypal/checkout-with-vault/android/v5-2026-09-16]]`.

1. **Scope — PASS.** This is a Braintree Android v5-family website snapshot fetched 2026-09-16 from a page updated 2026-06-03. It documents client request construction for PayPal Checkout with Vault, not an exact Android artifact version or current support. It does not establish merchant/buyer eligibility, enablement, authorization return, tokenization, server transaction, Vault association, later merchant-initiated payment, settlement, or funding. Raw: `raw/braintree/docs/guides/paypal/checkout-with-vault/android/v5-2026-09-16.md:1-21,24-37,89-97`.
2. **Purpose/action and limits — PASS.** The central purpose is preserved: one standard checkout collects an immediate payment while requesting Billing Agreement consent for future merchant-initiated payments, unlike Billing Without Purchase signup. The enabling condition is `PayPalCheckoutRequest.shouldRequestBillingAgreement = true`; the default is `false`. Optional agreement/recurring fields and the consequential `amountBreakdown` exclusions when recurring details are present are retained, while exact types/defaults/examples stay at raw lines 29–97. Request construction and a consent prompt are not outcome proof.

## Position 28 — `docs-reference-client-reference-javascript-v2-browser-support`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-web-sdk]]` → `[[source-braintree-docs-reference-client-reference-javascript-v2-browser-support]]` → `[[raw/braintree/docs/reference/client-reference/javascript/v2/browser-support-2026-09-16]]`.

1. **Scope — PASS.** This is a historical Braintree JavaScript v2 client-reference snapshot fetched 2026-09-16 from a page created/updated 2025-04-01. It covers page-specific desktop/mobile browser, webview and hybrid-runtime support statements for the v2 SDK. It is not a current browser matrix, current package/lifecycle statement, exact retained GitHub-package claim, merchant eligibility evidence, hosted-runtime proof, or payment-execution proof. Raw: `raw/braintree/docs/reference/client-reference/javascript/v2/browser-support-2026-09-16.md:1-16,17-69`.
2. **Purpose/action and limits — PASS.** The source routes the precise historical inventories while preserving consequential warnings: all-IE Quirks Mode is unsupported; IE 9/10 require customer-enabled TLS 1.2 after Braintree ended TLS 1.0/1.1 support; PayPal has Android-before-4.4 and iOS webview issues that Braintree says it will not fix; system-browser/approved browser-view alternatives are recommended; and named hybrid runtimes are neither tested nor developed for and may malfunction outside browser security policies. Exact lists and caveats remain at raw lines 17–34, 35–52, 53–66 and 67–69.

## Close

- Result: **8/8 answers PASS**.
- Corrections: none.
- Blockers: none.
- Audit started: `2026-10-07T11:41:08Z`.
- Audit ended: `2026-10-07T11:44:53Z`.
