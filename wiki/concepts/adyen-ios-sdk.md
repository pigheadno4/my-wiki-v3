---
title: "Adyen iOS SDK"
type: concept
category: technology
tags: [adyen, ios, swift, mobile, sdk, drop-in, components, apple-pay, 3d-secure]
---

## Adyen iOS SDK

Adyen iOS is a modular native checkout SDK. Its two primary integration choices are Drop-in, which presents the available payment methods as an all-in-one checkout surface, and individual Components, which let the merchant own the surrounding payment flow and UI.

## Retained baseline and updates

The first retained baseline is `adyen-ios@5.25.1` at exact SHA `5f6779b31299e3067de3a5279a816f3b8d2fbdf3`. The retained README marks 5.x active and lists iOS 12, Xcode 15, and Swift 5.7 as minimum requirements. It supports Swift Package Manager, CocoaPods, and Carthage.

This is version-qualified repository evidence, not current merchant eligibility guidance. The payment methods returned by the merchant backend, account configuration, shopper context, region, and transaction determine what can actually be offered.

The newest ingested update is `adyen-ios@5.26.0` at `da347498d07b843e5af3f9eb871376514ffdf38c` (2026-10-15 ingest). The `5.25.1` baseline and its integration knowledge remain preserved below and in [[source-github-adyen-ios]].

> [!warning] Contradiction
> The `5.26.0` release notes identify this as the last CocoaPods release and announce SPM/Carthage-only distribution afterward, while the same-tag README still advertises CocoaPods installation and the podspec remains present. This is a distribution-policy announcement, not evidence that `5.26.0` cannot be installed with CocoaPods. The discrepancy is also recorded in [[source-github-adyen-ios]].

## Integration and server boundary

Every payment Component uses an `AdyenContext` containing the client key, environment, optional payment context, and analytics configuration. A client key identifies the web service user but does not replace server credentials.

`AdyenSession` can initialize from a server-created Session and internally perform `/payments`, `/payment/details`, partial-payment, and stored-method operations. Its delegate reports completion, failure, and external-app transitions. A merchant can optionally take over the payments or additional-details step through handler protocols.

In the advanced flow, the merchant implements the payment-method, `/payments`, `/payments/details`, order, balance, and stored-method calls and passes resulting actions back to Drop-in or an action Component. The demo explicitly recommends a merchant backend and limits direct API-key use to testing.

## Module architecture

| Module | Responsibility |
| --- | --- |
| `AdyenDropIn` | Payment-method list, stored methods, selection, partial-payment reload, and action delegation |
| `AdyenSession` | Session setup and client orchestration of payments, details, orders, and stored methods |
| `AdyenCard` | Card and stored-card forms, BIN lookup, co-badged choice, installments, and card scanning integration |
| `AdyenComponents` | Apple Pay, bank debit, bank redirect, wallet, issuer-list, UPI, PayTo, and other payment Components |
| `AdyenActions` | Redirect, 3DS2, SDK, await, voucher, QR-code, and document follow-up actions |
| `AdyenEncryption` | Client-side card and bank-detail encryption using an Adyen-provided public key |
| Optional modules | Cash App Pay, Twint, WeChat Pay, SwiftUI helpers, card scanning, and delegated authentication |

Several optional paths delegate runtime behavior to separately versioned dependencies, including Adyen 3DS2, authentication, networking, WeChat Pay, Cash App Pay, and the bundled Twint SDK. Their presence in the package does not make this snapshot evidence for the complete delegated implementation. The exact `Adyen3DS2@2.4.4` runtime is independently documented in [[adyen-3ds2-ios-sdk]], while `AdyenWeChatPayInternal@2.2.0` packaging and Tencent public-header evidence belong to [[adyen-wechatpay-ios-wrapper]].

## Cards, storage, and partial payments

The Card Component supports card-brand detection, BIN lookup, holder name, billing address, storage consent, installments, country-specific fields, stored-card security code, and co-badged card choice. It filters several US debit brands from display while retaining them as supported implementation detail.

Card fields and ACH bank details are encrypted with a fetched public key before submission. The resulting `PaymentComponentData` carries payment-method details, amount, optional order, storage choice, installments, browser information when needed, and SDK analytics data. It is still input for the merchant or Session payment call, not proof that a transaction has succeeded.

Drop-in can display and remove stored methods when the corresponding delegate allows it. Partial-payment support checks a balance, creates an order, reloads payment methods against the remaining amount, and can cancel the order.

## Apple Pay and external apps

`ApplePayComponent` wraps `PKPaymentAuthorizationViewController`, validates device and network support, and submits the authorized Apple Pay token as payment details. After receiving the payment response, the integration must call `finalizeIfNeeded` for both success and failure so the Apple Pay sheet receives its terminal status.

Cash App Pay can request one-time and on-file grants and requires a redirect URL. Twint uses its own SDK and callback scheme. WeChat Pay requires a real device, configured URL-query schemes, and its independently versioned SDK. These native handoffs require app-return handling and must not be inferred from the generic presence of a payment-method model alone.

## Actions, analytics, and privacy

`AdyenActionComponent` routes redirect, native redirect, 3DS2 fingerprint and challenge, delegated authentication, SDK, await, voucher, QR-code, and document actions to specialized Components. Redirects may use an in-app browser or external application and return additional details for the next payment-details call.

Analytics configuration can disable event analytics, but the initial analytics request remains part of the configured level. The privacy manifest declares product interaction for analytics plus user ID, contact, payment, name, email, phone, and address data for app functionality; it marks these categories as not linked and not used for tracking.

The SDK can identify native iOS, React Native, or Flutter wrappers for analytics. Release `5.25.1` fixes a component-form layout problem affecting cross-platform SDK integrations, but the release note does not identify a specific changed source file in this first baseline.

## Version-qualified changes in `5.26.0`

- **Apple Pay after a partial payment:** Drop-in's `PreApplePayComponent.order` now forwards reads and writes to its wrapped `ApplePayComponent`. The existing manager assigns the partial-payment order, and Apple Pay submission includes that order in `PaymentComponentData`. This fixes order propagation for the remaining-amount payment, not a new Apple Pay payment method or proof of successful authorization.
- **CVC value versus display:** Previously the formatter truncated only the formatted display while numeric sanitization could retain extra digits. It now caps the sanitized value as well: four digits for Amex, three for other or unknown brands. Single-character edits exceeding that limit are rejected; multi-character replacements pass to the formatter. The default standalone validator still accepts three to four digits; brand-bound validators enforce the selected brand's length.
- **Currency conversion:** `AmountFormatter` uses an uppercase currency-code lookup table maintained in the SDK, with system ICU/CLDR fallback for absent codes. Conversion APIs retain `localeIdentifier` for compatibility but no longer use it to choose decimal places; display localization remains. This is source-derived behavior, not a release-note claim or new currency-eligibility list.
- **Presentation:** Safe-area toolbar constraints, form content/frame layout guides, explicit margins and keyboard-frame settling address adaptive layouts. Taller keyboard frames publish immediately; shorter/hidden frames settle for 0.15 seconds. Default inactive text titles and separators use `#757575` in light mode and `#8E8E93` in dark mode, without changing custom overrides or the generic secondary-label/separator colors.
- **Demo app returns:** The SwiftUI demo handles a URL at scene connection and subsequent URL callbacks, forwarding it to `RedirectComponent` and conditionally Cash App Pay. The UIKit AppDelegate adds scene configuration; its new UIKit SceneDelegate is outside the retained capsule, so the full UIKit scene-return path is not established here.

Evidence and exact file links: [[source-github-adyen-ios]] and [[changelog-github-adyen-ios]]. No SDK build, device, accessibility, wallet or payment execution was performed.

## Related

- [[source-adyen-docs-payment-methods-kakaopay-ios-component]] — 2026-09-15 iOS Components Sessions/Advanced KakaoPay guide for redirect prerequisites, recurring-token creation and TEST/LIVE wording boundaries.


- [[source-adyen-docs-payment-methods-paypay-ios-component]] — 2026-09-15 PayPay-specific iOS Components Sessions/Advanced guide for redirects, TEST simulator and LIVE app/IP conditions, with unresolved `None`/configuration and Advanced-link examples.


- [[source-adyen-docs-payment-methods-paypal-ios-drop-in]] — 2026-09-15 PayPal guide for existing iOS Drop-in, covering Sessions/Payments request context, webhook outcomes, recurring-account permissions and capture-dependent refunds.


- [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-ios-5-0-0]] — 2026-09-15 snapshot of Adyen's v4.10.1-or-earlier to iOS v5.0.0 online-checkout migration guide for callbacks, `AdyenContext`, Component/Drop-in settings, Apple Pay and card brand types; Checkout API v69 is recommended, while the iDEAL note is for later v5.9.0.


- [[source-github-adyen-ios]] - cumulative exact-SHA repository evidence
- [[changelog-github-adyen-ios]] - package-qualified release ledger
- [[adyen-3ds2-ios-sdk]] - independently versioned native 3DS2 runtime
- [[adyen-wechatpay-ios-wrapper]] - independently versioned Tencent SDK wrapper used by WeChat Pay
- [[source-github-adyen-web]] - independently versioned browser SDK
- [[adyen-react-native-sdk]] - wrapper baseline that pins Adyen iOS `5.25.1`
- [[co-badged-cards]] - cross-provider card-network choice
- [[adyen]] - company and knowledge-status page
