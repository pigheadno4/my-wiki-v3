---
title: "Adyen Android SDK"
type: concept
category: technology
tags: [adyen, android, kotlin, mobile, sdk, drop-in, components, sessions, jetpack-compose, google-pay, 3d-secure]
---

## Adyen Android SDK

Adyen Android is a modular native checkout SDK. Its main integration choices are Drop-in, which supplies a prebuilt payment-method selection and action flow, and individual Components, which let the merchant own the surrounding interface and orchestration. Both traditional Android Views and Jetpack Compose entry points are retained in the `adyen-android@5.20.0` baseline.

## Historical 5.20.0 baseline

| Field | Value |
| --- | --- |
| Package | `adyen-android@5.20.0` |
| Release tag | `5.20.0` |
| Exact commit | `5314fad1389a8def9d8e3377f27f7405e303faba` |
| Minimum Android API | 21 |
| Compile SDK | 36 |
| Target SDK | 36 |
| Java toolchain | 11 |
| Kotlin | 1.9.25 |

The README marks the 5.x line active. This table reports retained repository evidence, not current merchant eligibility or payment-method availability.

## `5.21.0` checkout and build changes

The full additive `adyen-android@5.21.0` ingest (SHA `405b582a7b2060aceac756eae7b6bd3757e0c084`, released 2026-10-27) preserves the historical baseline above. The Card View now restores its store-payment-details switch from `outputData.shouldStorePaymentMethod` when restoring input fields after address lookup. This is UI-state restoration, not automatic tokenization or a change to merchant consent/server ownership.

Native redirect result submission and serialization now run inside `runSuspendCatching`, with failures sent to the Component error channel and non-CheckoutException failures wrapped as ComponentException. The helper rethrows coroutine cancellation; this does not introduce automatic retry or guarantee that every app failure is caught.

The retained catalog moves Adyen 3DS2 `2.2.27` -> `2.2.28`, Kotlin `1.9.25` -> `2.3.21` and AGP `8.8.1` -> `9.4.1`, alongside AndroidX/Compose/Coroutines updates. Modules adopt shared convention plugins. The exact-SHA supplemental Java convention still explicitly sets Android Java source/target to **11**, while catalog JVM target **17** configures plain Kotlin JVM tooling and the convention build. The upstream wrapper names Gradle `9.8.0`; compile/min catalog settings remain 36/21. These are repository settings, not a universal consuming-app wrapper/JDK requirement or a successful merchant build test. Retrofit `3.0.0` is evidenced in the example-app dependency, not a replacement of SDK-core networking.

The supplemental library convention also configures an AGP 9 API-validation workaround and filters generated Compose singleton dump content. Configured validation tasks are not executed-test evidence or proof of authored API removal. The delegated 3DS2 runtime and independently pinned React Native wrapper retain their own evidence histories. See [[source-github-adyen-android]] and [[changelog-github-adyen-android]] for exact files, supplement and migration boundaries.

## `5.22.0` security and image-loading boundary

The latest ingested package evidence is `adyen-android@5.22.0` at SHA `73df6558fa5868a2c14449ac2e0c6379fc349798` (released 2026-10-30, ingested 2026-11-07). Full additive ingestion preserves both earlier version sections. Adyen's release notes say Drop-in/Components block eight compromised eMudhra intermediates on devices without Google Play services, while Play-services devices had already received Google's automatic update. This is an attributed upstream security claim; the dependency blocklist and actual certificate rejection were not independently inspected or executed here.

Retained code updates OkHttp/logging `4.12.0` -> `4.12.1`. URL image saving moves from URL.openStream to the shared cached DefaultImageLoader, which uses OkHttp; load failures are wrapped separately from malformed URLs. Bitmap recycling moves to the view-created bitmap path, avoiding the old generic save helper's recycling of loader-provided cached bitmaps. No new public checkout API, universal TLS safety, or fully leak/cancellation-safe image pipeline is established. Regression-test image download/save and error paths in the consuming app. Exact evidence and migration limits: [[source-github-adyen-android]] and [[changelog-github-adyen-android]].

## Integration and server boundary

The Sessions flow starts from a Session created by the merchant backend. `CheckoutSessionProvider` performs the SDK setup call, and Drop-in or an individual Component can then handle payments, additional details, balance checks, partial-payment orders, and stored-method removal through the Session endpoints. A merchant can take over a Session call, but after takeover the remaining required callbacks must be implemented consistently.

The advanced flow starts from `/paymentMethods` and delegates `/payments` and `/payments/details` to the merchant's `DropInService` or Component callbacks. `PaymentComponentData` contains SDK-derived and shopper-entered fields, but the source explicitly assigns completion of the rest of the payment request to the merchant server.

## Module architecture

| Surface | Responsibility |
| --- | --- |
| `drop-in` / `drop-in-compose` | Prebuilt payment-method list, Activity Result launchers, stored methods, actions, and partial-payment flow |
| `components-core` / `components-compose` | Shared models, configuration, callbacks, provider lifecycle, analytics, and Compose adapters |
| `sessions-core` | Session setup, payments, payment details, balance, order, cancellation, and token-disable calls |
| `card` / `cse` | Card UI, BIN and brand detection, dual-brand selection, installments, address fields, and client-side encryption |
| `action-core`, `redirect`, `3ds2`, `await`, `qr-code`, `voucher` | Follow-up action dispatch and method-specific action handling |
| Payment-method modules | ACH, Bacs, Blik, Boleto, issuer-list banking, Pay by Bank, PayTo, SEPA, UPI, gift cards, and other local methods |
| External SDK adapters | Google Pay, Cash App Pay, Twint, WeChat Pay, and Adyen 3DS2 |

Compose Components retain lifecycle and saved-state owners, create one Component per lifecycle by default, and allow a key when multiple instances are needed. `AdyenComponent` bridges the existing Component view into Compose; Drop-in Compose wraps the same Activity Result contracts rather than implementing a separate payment engine.

## Cards, storage, and partial payments

The Card Component supports six- or eight-digit BIN callbacks, brand lookup, dual-brand selection, card scanning, holder name, billing address and address lookup, storage choice, installments, country-specific fields, and stored-card CVC policy. Debit funding sources suppress installments in the retained implementation.

Card and generic fields are encrypted with an Adyen public key before submission. Encryption narrows exposure of sensitive fields but does not replace server-side payment creation, result verification, compliance controls, or fulfillment logic.

Drop-in separates stored and regular methods, checks method availability, can remove supported stored methods, and represents gift-card and remaining-amount state during partial payments. Sessions can check balances, create or cancel orders, refresh payment methods, and continue from a partially paid order.

## Actions and delegated runtimes

The SDK handles redirect, 3DS2 fingerprint and challenge, SDK, await, QR-code, and voucher actions. The 3DS2 adapter validates required tokens, coordinates fingerprint and challenge results, and can configure an out-of-band app-return URL, but the underlying runtime comes from `com.adyen.threeds:adyen-3ds2@2.2.27`. That exact delegated runtime is independently documented in [[adyen-3ds2-android-sdk]].

Google Pay delegates to Google Play Services Wallet, Cash App Pay to Pay Kit, Twint to its Android SDK, and WeChat Pay to Tencent's SDK. Their adapters and configuration are evidence for the Adyen integration boundary only; source presence does not prove merchant enablement, regional eligibility, device availability, or complete delegated behavior.

## Analytics and release boundary

Drop-in and Component analytics are enabled by default from the 5.x line. `AnalyticsLevel.NONE` suppresses Drop-in/Component events, while the implementation retains an initial setup level used to obtain a checkout-attempt identifier. Release `5.20.0` documents one change: compile and target SDK support moved to API 36. Broader SDK behavior on this page is accumulated baseline evidence and must not be attributed solely to that release.

## Related

- [[source-adyen-docs-payment-methods-bancontact-bancontact-card-android]] — 2026-09-15 Bancontact card Android chooser routing to Drop-in and prebuilt Component child guides.


- [[source-adyen-docs-payment-methods-bancontact-bancontact-card-android-drop-in]] — Bancontact card Android Drop-in v5.0.0+ Sessions/Advanced guide; base requests need no extra method fields, while recurring tokenization is WIP-gated and the token arrives after settlement.


- [[source-adyen-docs-payment-methods-sepa-direct-debit-android]] — 2026-09-15 SEPA Android chooser for Drop-in and SepaComponent children plus Sessions/Advanced base guides; source qualifies chooser redirect wording against the Component child's direct action.


- [[source-adyen-docs-payment-methods-sepa-direct-debit-android-component]] — 2026-09-15 Android Components SEPA guide for Sessions and Advanced flows, account fields, capture and shopper-absent recurring tokens.


- [[source-adyen-docs-payment-methods-blik-android]] — 2026-09-15 BLIK Android chooser for Drop-in and Redirect Component child guides plus two Sessions base integration routes.


- [[source-adyen-docs-payment-methods-twint-android]] — 2026-09-15 TWINT Android chooser for Drop-in and Redirect Component child guides plus Sessions/Advanced base integration routes.


- [[source-adyen-docs-payment-methods-blik-android-drop-in]] — 2026-09-15 BLIK Android Drop-in v5.0.0 Sessions/Advanced method-addition guide with no extra BLIK fields/configuration and separate TEST/live gates.


- [[source-adyen-docs-payment-methods-pay-by-bank-us-android-drop-in]] — 2026-09-15 Pay by Bank (US) Android Drop-in Sessions/Advanced add-on with stated 5.70.0 prerequisite, ACH capture risk and Plaid live gate; see source for countryCode wording.


- [[source-adyen-docs-payment-methods-pay-by-bank-us-android-component]] — 2026-09-15 Pay by Bank (US) Android Components Sessions/Advanced add-on with version-qualified module setup, ACH capture risk and Plaid live gate; see source for version and countryCode tensions.


- [[source-adyen-docs-payment-methods-ideal-android]] — 2026-09-15 iDEAL | Wero Android chooser for Drop-in and IdealComponent child guides plus Sessions/Advanced main integration routes.


- [[source-adyen-docs-payment-methods-ideal-android-drop-in]] — 2026-09-15 iDEAL | Wero Android Drop-in Sessions/Advanced add-on with SEPA recurring-token and qualified TEST/live routes.


- [[source-adyen-docs-payment-methods-mobilepay-android]] — 2026-09-15 MobilePay Android chooser linking Drop-in and InstantPaymentComponent child guides plus Sessions/Advanced main guides.


- [[source-adyen-docs-payment-methods-alipay-plus-android-component]] — Alipay+ Android redirect Components guide for existing Sessions/Advanced integrations with Compose or view attachment and unspecified SDK dependency versions (2026-09-15 snapshot).


- [[source-adyen-docs-payment-methods-online-banking-thailand-android-component]] — 2026-09-15 Android `MolpayComponent` Sessions/Advanced guide for Online banking Thailand redirect setup, version-qualified prerequisites, Compose/View integration and TEST/live gates.


- [[source-adyen-docs-payment-methods-napas-card-android-component-earlier-versions]] — historical v4.x.x Advanced Android Redirect Component guide for Napas card, with unresolved `momo_atm` method-type wording and webhook result boundaries.


- [[source-adyen-docs-payment-methods-napas-card-android-drop-in-earlier-versions]] — historical v4.x.x Napas card Android Drop-in Advanced guide for VN/VND discovery, redirect and webhook-qualified outcomes; MoMo example type and Sessions-link discrepancies remain in the source.


- [[source-adyen-docs-payment-methods-google-pay-android-component-migrate]] — 2026-09-15 Google Pay Android Component guide for optional earlier-5.x.x to 5.9.x migration, View/Compose attachment, button submission and initialization-time availability errors; migration examples do not establish current SDK behavior or payment outcome.


- [[source-adyen-docs-payment-methods-cards-android-drop-in-earlier-versions]] — historical Android Cards Drop-in v4.x.x Advanced-flow guide for card display, server payments, results and stored-card examples; Sessions links and save-switch naming conflict require qualification.


- [[source-adyen-docs-payment-methods-cards-android-drop-in]] — 2026-09-15 cards guide for existing Android Drop-in v5.0.0+ Sessions or Advanced flows, with card configuration, split funding, tokenization and test/live boundaries.


- [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-android-5-0-0]] - Adyen Docs Android v4.13.3-or-earlier to v5.0.0 migration guide for Drop-in and Components (2026-09-15 snapshot)


- [[source-github-adyen-android]] - cumulative exact-SHA repository evidence
- [[changelog-github-adyen-android]] - package-qualified release ledger
- [[adyen-3ds2-android-sdk]] - independently versioned native 3DS2 runtime
- [[adyen-ios-sdk]] - independently versioned native iOS SDK
- [[adyen-react-native-sdk]] - wrapper baseline that pins Adyen Android `5.19.0`, not this page's newer `5.20.0`
- [[source-github-adyen-web]] - independently versioned browser SDK
- [[co-badged-cards]] - version-qualified dual-brand implementation evidence
- [[adyen]] - company and knowledge-status page

## Sources

- [[source-adyen-docs-payment-methods-bancontact-bancontact-card-android-component-earlier-versions]] — historical Android v4.x.x `BcmcComponent`/Redirect Component flow, client-side encrypted details and server `/payments/details` handoff (2026-09-15 capture).


- [[source-adyen-docs-payment-methods-bancontact-bancontact-mobile-android-drop-in-earlier-versions]] — historical v4 Android Drop-in `bcmc_mobile` app/QR action and server `/payments/details` return handoff (2026-09-15 capture).


- [[source-adyen-docs-payment-methods-bacs-android]] — BACS Android Drop-in-versus-Components chooser and base Sessions/Advanced route links (2026-09-15); method children supply setup details.


- [[source-adyen-docs-payment-methods-ach-direct-debit-android]] — ACH Android Drop-in-versus-Components chooser and base Sessions/Advanced guide links (2026-09-15); child guide determines actual method setup.


- [[source-adyen-docs-payment-methods-ach-direct-debit-android-drop-in]] — Android Drop-in ACH optional submit, address and save-details UI defaults for Sessions/Advanced (2026-09-15); US/PR address-code example is scoped to UI configuration.


- [[source-adyen-docs-payment-methods-ach-direct-debit-android-component]] — ACH Android Component module, optional Compose dependency, UI defaults, Sessions-versus-Advanced payment-method source and per-screen Compose key (2026-09-15).


- [[source-adyen-docs-payment-methods-blik-android-drop-in-earlier-versions]] — 2026-09-15 captured historical BLIK Android Drop-in v4 guide, v3.8.0+ requirement and redirect/details/webhook flow; source flags mismatched prerequisite and request examples.


- [[source-adyen-docs-payment-methods-twint-android-component]] — 2026-09-15 TWINT Android Components Sessions (Checkout API v68+) and Advanced add-on with redirect/sdk actions, configurable storage UI and recurring token route; field-spelling caveat in source.


- [[source-adyen-docs-payment-methods-promptpay-android]] — 2019-modified, 2026-09-15-captured PromptPay Android chooser for Drop-in/Components child guides and two Sessions base guides; child pages own method behavior.


- [[source-adyen-docs-payment-methods-duitnow-android-drop-in]] — 2026-09-15 DuitNow Android Drop-in Sessions/Advanced add-on with no extra method fields/configuration and separate test/live setup; no outcome flow documented.


- [[source-adyen-docs-payment-methods-duitnow-android-component]] — 2019-modified, 2026-09-15-captured DuitNow Android Components Sessions (5.0.0+) and Advanced add-on with Support setup, instant component and qualified MYR request examples.


- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/manifest.json` - exact-SHA source capsule
- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/README.md` - purpose, lifecycle, installation, and analytics defaults
- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/drop-in/src/main/java/com/adyen/checkout/dropin/DropIn.kt` - Sessions and advanced Drop-in contracts
- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/sessions-core/src/main/java/com/adyen/checkout/sessions/core/internal/data/api/SessionService.kt` - client Session operations
- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/components-core/src/main/java/com/adyen/checkout/components/core/PaymentComponentData.kt` - payment request and server boundary
- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/card/src/main/java/com/adyen/checkout/card/internal/ui/DefaultCardDelegate.kt` - card, encryption, installments, and dual-brand behavior
- `raw/github/adyen/adyen-android/releases/adyen-android/5.20.0/2026-08-01/release-notes.md` - API-level change
