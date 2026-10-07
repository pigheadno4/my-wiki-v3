# Braintree C45 fixed-query audit J — positions 37–40

## Timing (UTC)

- Start: `2026-10-07T14:12:33Z`
- Analysis end: `2026-10-07T14:15:52Z`
- Handoff: `2026-10-07T14:15:52Z`

## Position 37 — `docs-guides-pinless-debit-optimized-debit-routing-eligibility`

**Route:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-payment-methods.md` → `wiki/sources/braintree/source-braintree-docs-guides-pinless-debit-optimized-debit-routing-eligibility.md` → `raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/eligibility-2026-09-16.md`

**Q1 — What exact scope is established, and what must not be inferred? — PASS.** The requested object/action is Braintree PINless Debit Optimized Debit Routing **eligibility and enablement contact**, and the reached evidence answers that same object rather than a neighboring integration, pricing, or transaction-execution topic. It is an unversioned Braintree website checklist for US-domiciled merchants, USD transactions, specified card inputs/BINs/networks, and an enablement contact route; it establishes no SDK/version, client/server ownership, Sandbox/Production behavior, merchant-account approval, current eligibility/enablement, pricing/savings, authorization, settlement, or funding. Locators: source lines 14–21 and 31–34; raw metadata lines 1–10 and eligibility/onboarding lines 14–39.

**Q2 — What purpose, conditions, and warnings are documented, and where is detail retrievable? — PASS.** The page's purpose is to determine whether a merchant/transaction/card combination fits the stated routing prerequisites and where to request enablement. Conditions are US domicile and USD; vaulted or keyed debit/prepaid cards or eligible Apple Pay/Google Pay card types; eligible Visa/Mastercard BINs; and STAR, NYCE, PULSE, ACCEL, or MAESTRO. Wallet naming does not make every wallet card eligible, and contacting Technical Account Management or Business Development is not proof of enablement. Exact routine detail is in raw `## Eligibility`: merchant/currency lines 16–18, payment methods/BINs lines 20–23, networks lines 25–30, wallet note lines 33–34, and `### Onboarding` lines 37–39.

## Position 38 — `docs-guides-paypal-mobile-checkout-ios-v7`

**Route:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-ios-sdk.md` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-mobile-checkout-ios-v7.md` → `raw/braintree/docs/guides/paypal/mobile-checkout/ios/v7-2026-09-16.md`

**Q1 — What exact scope is established, and what must not be inferred? — PASS.** The requested object/action is the **availability and regional eligibility** of PayPal Mobile Checkout for custom native-client integrations, and the reached evidence answers that same object rather than an iOS v7 implementation procedure. The URL is iOS-v7-routed, but the body is cross-platform and names Android v4.13+ and iOS v5.11+; it gives no exact package/revision, iOS v7 API, setup, request/callback, tokenization/server handoff, environment, account enablement, runtime behavior, or payment-lifecycle proof. Locators: source lines 14–20 and 23–29; raw metadata lines 1–10 and availability line 17.

**Q2 — What purpose, conditions, and warnings are documented, and where is detail retrievable? — PASS.** The notice says PayPal Mobile Checkout is for eligible merchants using a custom client-side integration, excludes Drop-in UI and JavaScript, and names merchants/customers in the US, Canada, Europe, and UK; customers elsewhere receive the standard PayPal web experience. The retained capture ends after introducing an unsupported-flow list, so no missing transaction/use-case exclusions may be reconstructed. Exact details are confined to raw `AVAILABILITY` lines 16–17 and `ELIGIBILITY` lines 20–22; there is no further procedure/value/schema detail in this snapshot.

## Position 39 — `docs-guides-pinless-debit-optimized-debit-routing-code-samples-sdk-node`

**Route:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-payment-methods.md` → `wiki/sources/braintree/source-braintree-docs-guides-pinless-debit-optimized-debit-routing-code-samples-sdk-node.md` → `raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/sdk/node-2026-09-16.md`

**Q1 — What exact scope is established, and what must not be inferred? — PASS.** The requested object/action is **reading a routed debit-network value from a transaction result and searching optimized-routing transactions by ID/network**, and the reached evidence answers that same object rather than eligibility, routing setup, network-token behavior, or transaction authorization creation. It is an unversioned Braintree website page labeling Node snippets, not an exact Node package/version; the page establishes no credentials, gateway setup, environment, merchant eligibility/enablement, authorization success, matching results, settlement, or funding. The source also correctly preserves the material syntax boundary: website `result.transaction.debit_network` is not verified current/runnable Node syntax. Locators: source lines 14–19; raw metadata lines 1–10 and result/search snippets lines 14–38.

**Q2 — What purpose, conditions, and warnings are documented, and where is detail retrievable? — PASS.** The page illustrates a conditionally populated routed-network response field during authorization, later availability for the damaged-text `submit_for_settlement`/`void` actions, and transaction retrieval by ID or routed network. Its shown search uses `gateway.transaction.search`, `search.debitNetwork().is("STAR")`, callback iteration, and amount logging; `STAR` is illustrative and the page provides neither result completeness nor production error handling. Routine detail is in raw lines 14–24 and 26–38. The retained supporting authority confirms the warning: `braintree@3.40.0` XML responses pass through `Util.convertNodeToObject` (`http.js:158–171`), object keys are camel-cased (`util.js:67–121`), the search field is `debitNetwork` (`transaction_search.js:71–74`), and the changelog records `debitNetwork` for sale/search (`CHANGELOG.md:167–173`).

## Position 40 — `docs-guides-paypal-commerce-ios-barcode-scanning`

**Route:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-ios-sdk.md` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-commerce-ios-barcode-scanning.md` → `raw/braintree/docs/guides/paypal-commerce-ios/barcode-scanning-2026-09-16.md`

**Q1 — What exact scope is established, and what must not be inferred? — PASS.** The requested object/action is **enabling and launching UPC/QR barcode scanning in the historical PayPal Commerce iOS SDK and navigating scan matches**, and the reached evidence answers that same object rather than modern modular Braintree iOS, ordinary checkout, or payment processing. The Braintree-hosted page is unversioned and names no SDK release, OS/runtime, server behavior, environment, merchant/account enablement, or payment flow. It does not prove current availability, device support, inventory accuracy, product matches, purchase completion, or payment execution. Locators: source lines 14–16 and 31–36; raw metadata lines 1–10 and barcode body lines 14–21.

**Q2 — What purpose, conditions, and warnings are documented, and where is detail retrievable? — PASS.** For a store that supports UPC search, the page directs the app to set `enable_barcode_scanning` to `true`, check `PayPalCommerce deviceSupportsBarcodeScanning`, and invoke `PayPalCommerce scanForBarcodes`; a single match opens product detail and multiple matches open a product list. The two HTTP QR strings are snapshot examples, not production endpoints or a general QR contract. Exact configuration/API/result-navigation detail is in raw lines 16–19; QR examples are raw lines 19–21.

## Shared checks — PASS

- Manifest/selection: these are exactly C45 positions 37–40 and query group J. Each source target exists. All four current raw SHA-256 values exactly match the manifest pins: `fa6b4447…d19d06`, `f0f3358a…fb10d`, `662b95d8…afd96`, and `c37d2f17…a26e`.
- URL/provenance: for every page, the manifest canonical URL, source `canonical_url`, and raw `Source URL` agree; every raw records `Fetched: 2026-09-16` and `Discovery: llms.txt,sitemap.xml`.
- Single ownership/reciprocity: each exact raw path and canonical URL has one owner under `wiki/sources/`; root links the Braintree provider index, the provider index links each main concept, each main concept links its assigned source once, and every source links its main concept and exact pinned raw. The absent direct C45 provider-catalog rows are deferred coordinator-close work, not page failures.
- Bounded gap sweep: filename/topic matches found the expected PINless overview/integration siblings, PayPal Mobile Checkout JavaScript sibling, and PayPal Commerce overview/configuration/product-card siblings. None is needed to support the retained answers, so no unrelated sibling or old raw was promoted into evidence. Only the Node syntax warning required extra authority: the fully read `source-github-braintree-node` summary plus the four cited `deb5227` capsule locators; their current SHA-256 values match the snapshot manifest.

## Completeness result

`4/4` routes reported; `8/8` fixed questions answered; `8/8 PASS`; no content correction requested.
