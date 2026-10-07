# Braintree C45 fixed-query audit H — positions 29–32

- UTC start: `2026-10-07T14:03:07Z`
- UTC analysis end: `2026-10-07T14:05:06Z`
- UTC handoff: `2026-10-07T14:05:13Z`
- Scope: manifest positions 29–32 only; exactly two fixed questions per page (8 total)
- Result: **PASS — 8/8 questions**

## Shared checks, sweep, and authority

- **Identity, pins, URLs, provenance, and ownership — PASS.** All four attempt-1 reviews are approved, and each promoted source is byte-equal to its reviewed candidate. Recomputed SHA-256 values match the manifest: PayPal Mobile Checkout Android v5 `2ebb17412bb3f960d482edecbc05cfd3943b3da72383dee1d4d6682a99a568ef`; Functions CLI download `e34f6b3b3266efb3a96df50ef4f4f34ae57dc4b75d9061a80b5a77c0090a7e16`; PayPal Commerce iOS installation without CocoaPods `07749e1ffeeeedc0af5e767341d56d7b8ecf9840f4d625450dff174de44d799e`; In-Person EMV receipt reference `4260907b6ac43ecf11974991f43b9221a89bbf339da1611569369ff4d2bf8a89`. For every page, manifest identity/target/URL/raw path, source frontmatter, raw `Source URL`, and factual Raw Source agree. Each raw records `Fetched: 2026-09-16` and `Discovery: llms.txt,sitemap.xml`; each exact canonical URL and primary raw path has one source owner.
- **Routes and reciprocity — PASS.** Root `wiki/index.md:11` routes to `wiki/braintree-index.md`. Provider concept rows are `wiki/braintree-index.md:877,865,878,844`; reciprocal source entries are `wiki/concepts/braintree-android-sdk.md:74`, `wiki/concepts/braintree-payment-platform.md:28`, `wiki/concepts/braintree-ios-sdk.md:83`, and `wiki/concepts/braintree-in-person.md:14`. Each source links its same main concept and exact raw. Direct C45 provider/company catalog rows remain deferred coordinator-close work, not query failures.
- **Full reads, bounded gap sweep, and extra authority — PASS.** All four canonical sources and complete pinned raws were read. The bounded filename/topic sweep covered Mobile Checkout Android/iOS/JavaScript routes, Functions CLI reference, PayPal Commerce iOS overview/setup, and In-Person receipt printing. The selected raws themselves contain the route/body mismatch, preview availability tension, historical dependency qualification, and illustrative-receipt boundary needed here. No retained answer or unresolved conflict required a sibling, linked Receipt Data Handling page, linked GitHub dependency, or older snapshot, so none was imported as factual authority.

## Position 29 — `docs-guides-paypal-mobile-checkout-android-v5` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:877` → `wiki/concepts/braintree-android-sdk.md:74` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-mobile-checkout-android-v5.md` → `raw/braintree/docs/guides/paypal/mobile-checkout/android/v5-2026-09-16.md`.

1. **Q1 scope and must-not-infer — PASS; object/action evidence matches.** This is a 2026-09-16 Braintree website snapshot on an Android v5 route, but the body is a cross-platform PayPal Mobile Checkout eligibility/availability notice. Its product/action scope is eligible merchants offering a custom client-side flow, with body-stated Android `v4.13+` and iOS `v5.11+`; it names no request, token, server operation, transaction object, environment, or particular account. The route must not be treated as exact Android v5 package/API behavior, and the snapshot does not prove current support, installed compatibility, merchant/buyer eligibility, enablement, payment execution, settlement, or funding. Source `:14-26`; raw `:1-18,23-34`.
2. **Q2 purpose, conditions/warnings, and detail route — PASS; requested availability action matches.** The page's purpose is to state who may use PayPal Mobile Checkout and where its mobile experience applies. Merchants and customers are named for the US, Canada, Europe, and UK; customers elsewhere fall back to the standard web experience. Drop-in UI, JavaScript, in-person point-of-sale, and multi-seller payments are excluded. Exact availability/version wording is raw `:17-18`, regional/fallback conditions `:23-28`, and unsupported flows `:30-34`; the server-side link at `:38` remains unread navigation. Source locators `:30-34`.

## Position 30 — `docs-guides-functions-download-cli-tool` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:865` → `wiki/concepts/braintree-payment-platform.md:28` → `wiki/sources/braintree/source-braintree-docs-guides-functions-download-cli-tool.md` → `raw/braintree/docs/guides/functions/download-cli-tool-2026-09-16.md`.

1. **Q1 scope and must-not-infer — PASS; object/action evidence matches.** This is a Braintree Functions documentation-preview page for the Functions CLI. The object is the CLI and the documented actions are generating, testing, and deploying a Function, with historical global-install and Braintree-account login examples. It identifies no exact CLI/package or Node/runtime version, SDK/client-server placement, deployment environment, account eligibility, Function result, or payment object. Do not infer current npm publication/support, successful installation/login/authentication/deployment, or payment execution. Source `:14-20`; raw `:14-22,25-33`.
2. **Q2 purpose, conditions/warnings, and detail route — PASS; requested CLI actions match.** The central purpose is CLI-assisted Function generation, testing, and deployment. The controlling warning is that preview access was request-only and the CLI was not yet on npm, despite the adjacent “available via npm” wording and `npm install -g @braintree/functions-cli` example; the inquiry route is `functions-requests@braintreepayments.com`. The install and `btfns login` commands are examples, not outcome proof. Preview/purpose/warning are raw `:17-22`; installation is `:25-28`; login is `:29-33`. Source locators `:24-28`.

## Position 31 — `docs-guides-paypal-commerce-ios-installation-without-cocoapods` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:878` → `wiki/concepts/braintree-ios-sdk.md:83` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-commerce-ios-installation-without-cocoapods.md` → `raw/braintree/docs/guides/paypal-commerce-ios/installation-without-cocoapods-2026-09-16.md`.

1. **Q1 scope and must-not-infer — PASS; object/action evidence matches.** This is an unversioned Braintree-hosted manual-installation page for the historical PayPal Commerce iOS SDK without CocoaPods. Its object/action is copying the `PayPalCommerce` directory into an app project and installing the listed dependencies. It gives no PayPal Commerce release, iOS/runtime environment, merchant/account scope, server transaction object, or payment action. It is distinct from the modern modular Braintree iOS SDK and must not be treated as current package requirements, security/support status, build/runtime compatibility, enablement, or payment-execution evidence. Source `:14-26`; raw `:14-19`.
2. **Q2 purpose, conditions/warnings, and detail route — PASS; requested manual-install action matches.** The central procedure is manual copy plus installation of every listed dependency. The versions are expressly those tested against, including Braintree `v4.3`, not current minima or compatibility guarantees. Three libraries are already compiled into PayPal Commerce, and the app must reference `PayPalCommerce-Acknowledgements.md` for licensing attribution; the linked repositories/file remain unread navigation. Copy action is raw `:16`; tested-version condition and dependency values `:17-29`; built-in libraries `:32-37`; acknowledgements requirement `:40-42`. Source locators `:30-33`.

## Position 32 — `in-person-reference-emv-receipt-reference` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:844` → `wiki/concepts/braintree-in-person.md:14` → `wiki/sources/braintree/source-braintree-in-person-reference-emv-receipt-reference.md` → `raw/braintree/in-person/reference/emv-receipt-reference-2026-09-16.md`.

1. **Q1 scope and must-not-infer — PASS; object/action evidence matches.** This is an unversioned Braintree In-Person website reference whose object is a merchant-varying example receipt with a visual overlay relating its data elements to EMV compliance; its action is guiding receipt producers to include necessary EMV and customer information. It identifies no SDK/API/version, Sandbox/Production environment, market/card/network/account eligibility, device/printer, transaction schema, or processing action. The example must not be read as a complete textual field specification, a universal receipt template, compliance proof for another merchant, or printing/delivery/payment/settlement/funding evidence. Source `:14-28`; raw `:14-26`.
2. **Q2 purpose, conditions/warnings, and detail route — PASS; requested receipt-production action matches.** The central purpose is to explain receipt data-element roles through an overlaid example while retaining the producer's responsibility to include all necessary information. The example expressly varies by merchant. The captured text does not enumerate the image fields: raw `:28` embeds three images, so no field inventory is inferred. Purpose is raw `:16`, producer condition `:19-23`, and merchant variation `:26`; Receipt Data Handling at `:23` remains unread navigation. Source locators `:32-36`.

## Completeness and handoff

- Query tally: Mobile Checkout PASS/PASS; Functions CLI PASS/PASS; PayPal Commerce iOS manual installation PASS/PASS; EMV receipt reference PASS/PASS.
- Material failures or corrections requested: none.
- Repository files modified: none. Audit artifact only: `/tmp/braintree-c45-query-audit-h.md`.

**Verdict: PASS — 4/4 pages, 8/8 fixed questions.**
