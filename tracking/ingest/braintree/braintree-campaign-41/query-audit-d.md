# Braintree C41 fixed-query audit D — positions 13–16

Result: **PASS — 8/8 fixed questions.** No content correction or extra authority read is required.

## Shared checks

- Manifest identity: all four selected raw paths and canonical URLs match their exact jobs. Recomputed SHA-256 values match the manifest: `68b3f93c…71a06`, `45f45f94…1dd98`, `695a7218…0d5`, and `8e5011e2…036a1a`.
- Route entry: `wiki/index.md:5-11` reaches `wiki/braintree-index.md`. Existing provider-index concept edges are `braintree-payment-methods` (`wiki/braintree-index.md:649`), `braintree-ios-sdk` (`:661`), and `braintree-payment-platform` (`:648`). Each concept links the assigned source, and each source links its exact pinned raw.
- Bounded gap sweep: filename and content searches covered Vault/customer, deprecated client-side encryption, PayPal Commerce iOS, In-Person hardware/coverage/setup/launch, reset/offline transactions, and P2PE terms. The selected full raws answer all eight page-scoped questions. Linked GraphQL schema, upgrade, coverage, hardware, PCI-listing, and PayPal Commerce sibling pages remain navigation or separate authority; none is needed to validate the summaries' bounded claims, so no extra full read was performed.
- Deferred close navigation, not a content failure: direct source entries are not yet in `wiki/braintree-index.md`; the new `braintree-in-person` concept and its provider-index edge are also not yet closed. The required actual routes below already resolve through existing indexed concepts. Coordinator-owned aggregate/catalog closure remains separate.

## 13 — `in-person-guides-vaulting-and-customers`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:649` → `wiki/concepts/braintree-payment-methods.md:27` → `wiki/sources/braintree/source-braintree-in-person-guides-vaulting-and-customers.md:12-42` → `raw/braintree/in-person/guides/vaulting-and-customers-2026-09-16.md`.

1. **PASS — exact scope / non-inference.** This is a 2026-09-16 snapshot of an unversioned Braintree In-Person website guide for collecting a physically presented payment method on a reader and storing it, optionally under a Braintree customer, through either a vault-only flow or an immediate-charge-plus-vault flow. It names no SDK/package version or exact GraphQL commit and does not establish present availability, merchant/account enablement, reader compatibility, consent/PCI compliance, or successful authorization, capture, settlement, or future charge. Source `:14`; raw `:1-10,14-28,31-38,54-56`.
2. **PASS — purpose, actions, conditions, warnings, detail route.** Vault-only requests produce an In-Store Context to poll; `COMPLETE` exposes a `paymentMethod.id`. Charge-and-vault adds `vaultPaymentMethodAfterTransacting` to the reader charge request, then polls a separate charge context. Future use goes through standard eCommerce charge/authorize/capture mutations and is card-not-present priced. A later use of a vaulted token originating from a card-present digital wallet is marked MIT and has the documented 24-hour authorization-expiry window; callers should inspect `authorizationExpiresAt`. `paymentMethodId` is for charging and unique per vault request, while `uniqueNumberIdentifier` is analytics-only and unavailable for PayPal/Venmo QRC; `ALWAYS` may vault even after an unsuccessful authorization attempt. Exact procedures/examples are in raw `:31-51,54-80,85-105` (purpose/pricing `:14-28`).

Object/action match: **PASS.** Reader, optional customer, asynchronous context, resulting payment method, and transaction are kept distinct; vault completion is not promoted to authorization/capture/settlement. The source also preserves the raw's prose/example disagreement over `transaction.customer` versus customer data nested under the displayed payment method and routes exact schema work outward (`source :18-23`; raw `:43-50,61-68`).

## 14 — `docs-deprecated-client-side-encryption-ios-library`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:661` → `wiki/concepts/braintree-ios-sdk.md:85` → `wiki/sources/braintree/source-braintree-docs-deprecated-client-side-encryption-ios-library.md:12-42` → `raw/braintree/docs/deprecated/client-side-encryption/ios-library-2026-09-16.md`.

3. **PASS — exact scope / non-inference.** The page explicitly documents a deprecated legacy Braintree iOS client-side-encryption library whose two components are a card-entry payment form and encryption. The iOS library works with a merchant web server using a Braintree server-side client library and does not talk to the gateway directly. No SDK release/version is named; production gateway and Sandbox are only alternative public-key sources, not proof either is configured. Do not infer current iOS/GitHub support, PCI compliance, Vault success, authorization, or payment success. Source `:14,18-21`; raw `:17-29,109-120`.
4. **PASS — purpose, actions, conditions, warnings, detail route.** Manual card entry yields both raw and encrypted dictionaries; the example sends the encrypted dictionary to the merchant server and then Braintree. Stored Venmo Touch cards instead yield a payment-method code. The example's success branch depends on a server response after valid data is added to the Vault, and error examples include CVV/AVS failure or invalid card number. Public-key initialization and asymmetric encryption mean Braintree can decrypt while the client cannot; server-side client-library submission remains required. Exact payment-form and callback procedures are raw `:30-94`, errors `:95-103`, and encryption configuration/sample `:106-152`.

Object/action match: **PASS.** Payment-form collection, local encryption, merchant-server transport, gateway decryption, and Vault result are separate actions; the summary does not convert an example Vault success into a payment outcome.

## 15 — `docs-guides-paypal-commerce-ios-setup`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:661` → `wiki/concepts/braintree-ios-sdk.md:83` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-commerce-ios-setup.md:12-45` → `raw/braintree/docs/guides/paypal-commerce-ios/setup-2026-09-16.md`.

5. **PASS — exact scope / non-inference.** This is a Braintree-hosted, unversioned PayPal Commerce iOS SDK setup snapshot fetched 2026-09-16 (page timestamps 2025-04-02). It covers the `PayPalCommerce` CocoaPods/Git route, Commerce Panel OAuth client, Objective-C app-delegate configuration/callbacks, optional Apple Pay and platform features, and modal/embedded/standalone store presentation. It is not the modular `braintree-ios` SDK, names no SDK release or Sandbox/Production environment, and does not establish current platform/device support, app/account eligibility, enablement, provisioning, payment-method eligibility, or payment success. Source `:14-16`; raw `:1-10,17-54,249-290`.
6. **PASS — purpose, actions, conditions, warnings, detail route.** The app is added in Commerce Panel, receives client ID/secret, imports/configures the SDK at launch, and the page says those credentials must be obfuscated. Apple Pay additionally requires an Apple merchant ID/certificate, Commerce Panel enablement, Xcode capability, and merchant-ID configuration. Historical `Info.plist` transport, query-scheme, shortcut, camera/contact/photo settings are page-specific, not a modern universal baseline. Returning-user email and PayPal login require custom URL schemes and URL forwarding; multiple apps sharing a store require separate OAuth clients. Push, Spotlight, 3D Touch, Facebook-login routing, and three store presentation modes are separately located. Raw detail: install/OAuth `:17-54`; Apple Pay and plist `:55-158`; login/URL callback `:160-191`; optional integrations `:192-248`; presentation and multi-app condition `:249-290`.

Object/action match: **PASS.** OAuth-client creation, SDK launch configuration, Apple Pay merchant configuration, app-delegate event forwarding, login callback handling, and UI presentation remain distinct; setup examples are not treated as store provisioning or payment execution.

## 16 — `in-person-reference-faq`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:648` → `wiki/concepts/braintree-payment-platform.md:32` → `wiki/sources/braintree/source-braintree-in-person-reference-faq.md:14-53` → `raw/braintree/in-person/reference/faq-2026-09-16.md`.

7. **PASS — exact scope / non-inference.** This is an unversioned Braintree In-Person FAQ snapshot collected 2026-09-16, covering reader hardware, integrated POS, attended deployment, testing, captured territory, production preparation, ordering, network/account concerns, destructive reset, and a captured P2PE-listing statement. It is broad operational guidance, not an SDK/firmware contract or current proof of inventory, geography/use-case eligibility, account approval, enablement, PCI status for a deployment, connectivity, authorization, settlement, funding, or launch. Source `:16-18,41-43`; raw `:1-16,19-150`.
8. **PASS — purpose, actions, conditions, warnings, detail route.** The captured models are P400, M400, E285, and V400m; third-party-acquired Verifone devices cannot be reused because Braintree provisions software/keys, and transactions require POS integration. Semi-attended use requires staff monitoring; unattended vending/fuel was unsupported. E285 guidance is 2.4 GHz Wi-Fi and more than 20% battery. The captured US/Puerto Rico/USVI territory claim is snapshot-scoped. Production transition requires SE/IE coordination, account/reader preparation, and code review; hardware can have lead times. Reader communications must pass the onsite firewall. Resetting deletes network, offline certificate, screensaver configuration, and stored offline transactions and is discouraged in production. Exact raw detail: hardware/POS/deployment `:19-62`; troubleshooting/geography/IVR `:65-95`; launch/order/network/AMEX `:98-140`; reset/P2PE `:143-150`.

Object/action match: **PASS.** Supported-device statements, provider provisioning, POS initiation/response handling, staff attendance, account/production coordination, reader networking, and destructive reset effects are not conflated. Linked coverage, test, descriptor, AMEX, settlement, and PCI pages remain navigation rather than imported evidence.

## Handoff

- Content outcome: PASS, 8/8; no affected-question correction.
- Repository writes: none. Only this report was created in `/tmp`.
- `analysis_end_utc`: `2026-10-06T15:14:30Z`
- `handoff_utc`: `2026-10-06T15:14:30Z`
