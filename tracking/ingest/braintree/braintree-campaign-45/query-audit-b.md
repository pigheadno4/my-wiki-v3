# Braintree C45 fixed-query audit — group B (positions 5–8)

Scope: read-only audit of four pinned website pages; exactly two predetermined questions per page. UTC start: `2026-10-07T13:37:04Z`; analysis end: `2026-10-07T13:38:48Z`; handoff: `2026-10-07T13:38:48Z`.

## Shared evidence checks — PASS

The four manifest pins match the files byte-for-byte: Android migration `82dfb04d7323f088e0c152541459c3a5afc404cefe61adc5751b4e2773c14114`, iOS migration `a8b0a274d0ed745801abbaa979a8509841710f7e9cf5e6d813e223804847709f`, Apple Pay overview `ffa4e98b36b6f7282c9a058e7c5b61de510af9ca04fa905cda50fecd41bb5766`, and optimized debit routing overview `7ce857c4cd974e6f4d6a7262a614a830641f5a354a3b41c12368836f08895ad3`. For every page, manifest `canonical_url` = source frontmatter URL = raw line 1 URL; manifest raw path and source target match; exactly one source owns the raw in `raw_files`; and the source's `Raw Sources` link resolves to that same raw. Root `wiki/index.md:11` routes to the provider index; `wiki/braintree-index.md:866-878` routes to the four main concepts; each concept links back to its source (`braintree-android-sdk.md:74`, `braintree-ios-sdk.md:85`, `braintree-apple-pay.md:24`, `braintree-payment-methods.md:25`), while every source links to its main concept. Direct provider-index source rows remain coordinator-close work and are not failures.

The bounded filename/URL sweep covered the PayPal SDK migration, Apple Pay, and optimized-debit-routing families. It found separate JavaScript migration, Apple Pay configuration/client/testing, and optimized-routing eligibility/integration/workflow/reference pages, but the pinned raws fully answer these scope/overview questions and no external conflict or missing requested field was retained. Accordingly, no additional raw authority or older snapshot was read or used.

## 1. PayPal SDK migration route — Android v5

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:877` → `wiki/concepts/braintree-android-sdk.md:74` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-paypal-sdk-migration-guide-android-v5.md` → `raw/braintree/docs/guides/paypal/paypal-sdk-migration-guide/android/v5-2026-09-16.md`.

**Q1 — scope and must-not-infer: PASS.** Object/action match: the requested object is the Braintree website page at the Android v5 route, but the captured document body is a `checkout.js`-to-PayPal-JS-SDK migration notice for **JavaScript v3 custom PayPal integrations**, not native Android. It excludes JavaScript v2, Android, iOS, Drop-in UI, and new PayPal web integrations; it names no environment or account scope. Do not infer any Android v5 migration procedure, Android package/version behavior, current SDK support, merchant eligibility, hosted behavior, or payment result. Raw locators: URL/route `:1,7`; document/action identity `:6,14`; JavaScript-v3 condition `:17-18`; exclusions `:20-26`.

**Q2 — purpose/action, conditions, and detail retrieval: PASS.** The stated purpose/action is migration from `checkout.js` to the PayPal JS SDK, but this pinned body performs only applicability triage and expressly tells native Android users that the guide is not relevant. No migration procedure, parameter, value, or schema is present in this raw; the only further destination is the Braintree JavaScript SDK reference link. Raw locators: action title `:6,14`; applicability and warnings `:17-26`; sole reference route `:31-34`.

## 2. PayPal SDK migration route — iOS v7

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:878` → `wiki/concepts/braintree-ios-sdk.md:85` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-paypal-sdk-migration-guide-ios-v7.md` → `raw/braintree/docs/guides/paypal/paypal-sdk-migration-guide/ios/v7-2026-09-16.md`.

**Q1 — scope and must-not-infer: PASS.** Object/action match: the requested object is the Braintree website page at the iOS v7 route, while its captured body is a `checkout.js`-to-PayPal-JS-SDK notice limited to **JavaScript v3 custom PayPal integrations** and explicitly excluding iOS. JavaScript v2, Android, Drop-in UI, and new PayPal web integrations are excluded too; no environment or account scope is defined. Do not infer an iOS v7 migration, native API/package behavior, current support, merchant enablement, or payment execution. Raw locators: URL/route `:1,7`; document/action identity `:6,14`; JavaScript-v3 condition `:17-18`; exclusions `:20-26`.

**Q2 — purpose/action, conditions, and detail retrieval: PASS.** The title states a `checkout.js`-to-PayPal-JS-SDK migration, but the captured body contains only scope triage and says the page is irrelevant to iOS SDK users. It has no migration steps, values, fields, or schema; only a Braintree JavaScript SDK reference link remains. Raw locators: action title `:6,14`; applicability and warnings `:17-26`; sole reference route `:31-34`.

## 3. Apple Pay overview

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:867` → `wiki/concepts/braintree-apple-pay.md:24` → `wiki/sources/braintree/source-braintree-docs-guides-apple-pay-overview.md` → `raw/braintree/docs/guides/apple-pay/overview-2026-09-16.md`.

**Q1 — scope and must-not-infer: PASS.** Object/action match: this is Braintree's unversioned Apple Pay overview for processing Apple Pay in-app through its iOS SDK and during Safari web checkout through JavaScript SDK v3. The embedded iOS destination is the historical `/ios/v6/` route; no package version, environment, account, merchant configuration, or transaction object is specified. Do not infer iOS v7/current-package behavior, present merchant/device/browser/card eligibility, configuration completion, or successful payment. Raw locators: identity `:1,6-7,14`; supported-device qualification `:16`; processing action and exact SDK/channel routes `:18`.

**Q2 — purpose/action, conditions, and detail retrieval: PASS.** The page's central action is choosing the Braintree route for Apple Pay acceptance: iOS SDK for in-app and JavaScript SDK v3 for Safari web checkout. Supported iOS/macOS devices and a separate compatibility/availability article qualify the overview. The raw contains no configuration, client/server handoff, API fields, test values, or lifecycle result; it routes to SDK setup and JavaScript v3 configuration instead. Raw locators: compatibility condition `:16`; action/channel routing `:18`; setup navigation `:23-27`; next configuration route `:29`.

## 4. PINless Debit optimized debit routing overview

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:866` → `wiki/concepts/braintree-payment-methods.md:25` → `wiki/sources/braintree/source-braintree-docs-guides-pinless-debit-optimized-debit-routing-overview.md` → `raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/overview-2026-09-16.md`.

**Q1 — scope and must-not-infer: PASS.** Object/action match: this is an unversioned Braintree merchant/product overview whose object is an eligible debit-card transaction and whose action is routing it through lower-cost PINless debit networks. Scope is United States merchants on interchange pricing; no SDK, version, client/server role, environment, or API object is defined. Do not infer present eligibility or enablement, a particular routed network, authorization/settlement/funding success, or guaranteed savings. Raw locator: complete scope and routing action `:16`; qualified benefit `:18`; eligibility and split-shipment statements `:20-21`.

**Q2 — purpose/action, conditions, and detail retrieval: PASS.** The central purpose is lower-cost eligible debit routing that may reduce transaction fees. Routing also considers authorization rate, network availability, and latency; optimized routing is subject to eligibility, and split-shipment transactions are stated as supported. The raw gives no enablement procedure, API request/response, value table, or schema; its only detail route is the eligibility link. Raw locators: routing purpose/conditions `:16`; non-guaranteed benefit wording `:18`; eligibility route and split-shipment note `:20-21`.

## Tally

Exactly eight answers reviewed: **8/8 PASS**. No hash, URL, identity, ownership, reciprocity, object/action, or retrievability failure was found.
