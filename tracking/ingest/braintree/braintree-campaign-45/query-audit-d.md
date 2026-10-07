# Braintree C45 fixed-query audit D — positions 13–16

- UTC start: `2026-10-07T13:47:01Z`
- UTC analysis end: `2026-10-07T13:48:35Z`
- UTC handoff: `2026-10-07T13:49:39Z`
- Scope: manifest positions 13–16 only; exactly two fixed questions per page (8 total)
- Result: **PASS — 8/8 questions**

## Shared checks, sweep, and authority

- **Identity, pins, URLs, provenance, and ownership — PASS.** The four attempt-1 reviews are approved. Recomputed SHA-256 values match the manifest: Channel API errors `83569fadbc81358c18de44c21a0af853f5f0de51ccdbd57197415c44cadf7822`; Elo Node route `6cb49b3b7be1cd1ad037b9aa631648a22b7b3585ae4842075a9d4035570f70d4`; PayPal Credit Android v5 route `65715de57cf56b36cca3edb6e99c9ad7e262196ecaa7d45dc508f1a62f2d0fc5`; PayPal Commerce iOS URL specs `170f5768ec362732ea2edb9890e45aee854f771a8968a4c1b6ea04c9eac2fc31`. For each page, manifest canonical URL/raw path, source `canonical_url`/`raw_files`, raw `Source URL`, and factual `Raw Sources` agree. Each raw says `Fetched: 2026-09-16` and `Discovery: llms.txt,sitemap.xml`; exact raw-path and canonical-URL lookups find one source owner.
- **Routes and reciprocity — PASS.** Root `wiki/index.md:11` routes to `wiki/braintree-index.md`; provider concept rows are at `wiki/braintree-index.md:865-866,877-878`. Each main concept reciprocally links its source at `wiki/concepts/braintree-payment-platform.md:30`, `wiki/concepts/braintree-payment-methods.md:33`, `wiki/concepts/braintree-android-sdk.md:74`, or `wiki/concepts/braintree-ios-sdk.md:83`; each source links the same main concept and exact raw. Direct C45 provider/company catalog rows remain deferred coordinator-close work, not query failures.
- **Full reads, bounded gap sweep, and extra authority — PASS.** All four canonical sources and four pinned primary raws were read completely. The bounded filename/topic sweep covered PayPal Commerce Channel API siblings, Elo overview/client/configuration/testing routes, PayPal Credit/Pay Later and iOS sibling routes, and PayPal Commerce iOS overview/setup. No retained answer needed a sibling's behavior, older snapshot, or conflict resolution, so no extra authority was imported or read as factual evidence. The Android page's `3.17.2` Javadoc URL, replacement Pay Later guide, and other linked pages remain navigation only.

## Position 13 — `docs-guides-paypal-commerce-channel-api-handling-error-responses` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:865` → `wiki/concepts/braintree-payment-platform.md:30` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-commerce-channel-api-handling-error-responses.md` → `raw/braintree/docs/guides/paypal-commerce-channel-api/handling-error-responses-2026-09-16.md`.

1. **Scope and non-inference — PASS.** This is a collected, unversioned Braintree website guide for handling PayPal Commerce Channel API error responses. The action is request correction before retry after a 4XX client error; the page identifies neither a request/response schema object, endpoint, API/SDK version, client/server placement, environment, retailer/channel/merchant account, nor a payment lifecycle operation. It must not be generalized into a retry rule for other Braintree APIs or taken as current availability, enablement, request execution, order/payment success, settlement, or funding evidence. Source `:14-20`; raw `:1-18`.
2. **Purpose, consequential conditions/warnings, and detail route — PASS.** Any non-2XX response is classified as an error; for 4XX, the general instruction is to update the request before retrying. The list is expressly non-exhaustive and includes five 400 examples (inventory, shipping destination, payment-method authorization, shipping-address fields, request-body format), a 403 for expired access or retailer revocation, and a 404 for missing SKU. It provides no per-error remedy or success guarantee. Exact codes, identifiers, and descriptions are at raw `:16-26`; source locators are `:18-27`.

## Position 14 — `docs-guides-elo-server-side-node` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:866` → `wiki/concepts/braintree-payment-methods.md:33` → `wiki/sources/braintree/source-braintree-docs-guides-elo-server-side-node.md` → `raw/braintree/docs/guides/elo/server-side/node-2026-09-16.md`.

1. **Scope and non-inference — PASS.** This is an unversioned Braintree Elo server-side guide on the Node route. At capture it covered a limited release for select merchants using the page-relative “latest” JavaScript v3 and server SDKs and directed merchants to request access. Its object/action is a server `Transaction` sale using a client-tokenized nonce and device data, with settlement submission in the examples. It names no exact Node package/runtime/API version and no explicit Sandbox/Production scope; it does not establish current Elo support, merchant/environment enablement, repository behavior, or transaction/settlement success. Source `:14,18-22`; raw `:14-23,26-39,44-57`.
2. **Purpose, consequential conditions/warnings, and detail route — PASS.** After successful client tokenization, the merchant passes the nonce to its server, includes client-collected device data, and calls `gateway.transaction.sale`. Callback and Promise examples use illustrative amount `10.00`, `paymentMethodNonce`, `deviceData`, and `submitForSettlement: true`, then branch on `result.success`; the examples do not prove a result. Limited-release/select-merchant access is consequential. Exact access wording is raw `:17-18`, handoff is `:21-23`, callback request/result handling is `:24-40`, and Promise handling is `:42-58`; source locators are `:18-29`.

## Position 15 — `docs-guides-paypal-paypal-credit-android-v5` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:877` → `wiki/concepts/braintree-android-sdk.md:74` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-paypal-credit-android-v5.md` → `raw/braintree/docs/guides/paypal/paypal-credit/android/v5-2026-09-16.md`.

1. **Scope and non-inference — PASS.** This 2026-09-16 Braintree website snapshot is routed as Android v5, but its body is generic PayPal Credit orientation and explicitly deprecated. The product/object is the reusable PayPal Credit line presented through checkout; the action is offering it via PayPal client integration and Vault or Checkout flow navigation. The body specifies no Android request type, method, code, server transaction, environment, or lifecycle result. The route and unread `PayPalRequest` Javadoc URL containing `3.17.2` do not establish an exact current SDK/package contract, merchant or buyer eligibility, financing approval, server processing, or payment execution. Source `:14-24`; raw `:14-18,22,25-50`.
2. **Purpose, consequential conditions/warnings, and detail route — PASS.** The page calls PayPal Credit an instant, reusable credit line shown as an additional checkout button; PayPal UI presents available financing, including US Easy Payments and UK Instalments only if enabled for the merchant's PayPal account. Prerequisites are a completed PayPal client-side integration and either Vault or Checkout flow. The controlling warning is deprecation in favor of Pay Later offers; “similar to regular PayPal payments” supplies no actionable procedure. Deprecation is raw `:17-18`, product/account condition `:22`, prerequisites `:25-34`, high-level integration wording `:39-41`, and navigation `:44-50`; source locators are `:18-34`.

## Position 16 — `docs-guides-paypal-commerce-ios-url-specs` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:878` → `wiki/concepts/braintree-ios-sdk.md:83` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-commerce-ios-url-specs.md` → `raw/braintree/docs/guides/paypal-commerce-ios/url-specs-2026-09-16.md`.

1. **Scope and non-inference — PASS.** This is a Braintree-hosted, unversioned PayPal Commerce iOS URL-format snapshot for client-side deep links into the historical Commerce experience. The object is an app-specific PayPal Commerce URL scheme and its product, variant, category, or search URL; the action is formatting a deep link. It is distinct from the modular Braintree iOS SDK and documents no merchant-server payment operation, SDK release, supported iOS version, environment, account eligibility, or runtime validation. It must not be read as current availability, app configuration, successful deep-link handling/navigation, or payment execution. Source `:14-23`; raw `:1-16,19-22`.
2. **Purpose, consequential conditions/warnings, and detail route — PASS.** All documented URLs must use the app's PayPal Commerce scheme obtained from the Commerce Panel; `pypl-acme://` is illustrative. The page defines `/product/<product_linking_id>`, `/product/variant/<product_variant_sku>`, `/category/<fully_qualified_category_slug>`, and `/search?<search_type>=<search_term>`, naming `upc`, `name`, and catchall `q`. These are formatting examples, not acceptance or navigation guarantees. Scheme requirement/lookup is raw `:16-17`; exact path patterns, identifiers, search types, and examples are raw `:19-22`; source locators are `:20-31`.

## Completeness and handoff

- Query tally: Channel API errors PASS/PASS; Elo Node PASS/PASS; PayPal Credit Android v5 PASS/PASS; PayPal Commerce iOS URL specs PASS/PASS.
- Material failures or corrections requested: none.
- Repository files modified: none. Audit artifact only: `/tmp/braintree-c45-query-audit-d.md`.

**Verdict: PASS — 4/4 pages, 8/8 fixed questions.**
