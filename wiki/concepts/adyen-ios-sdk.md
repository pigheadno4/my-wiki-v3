---
title: "Adyen iOS SDK"
type: concept
category: technology
tags: [adyen, ios, swift, mobile, sdk, drop-in, components, apple-pay, 3d-secure]
---

## Adyen iOS SDK

Adyen iOS is a modular native checkout SDK. Its two primary integration choices are Drop-in, which presents the available payment methods as an all-in-one checkout surface, and individual Components, which let the merchant own the surrounding payment flow and UI.

## Current baseline

The first retained baseline is `adyen-ios@5.25.1` at exact SHA `5f6779b31299e3067de3a5279a816f3b8d2fbdf3`. The retained README marks 5.x active and lists iOS 12, Xcode 15, and Swift 5.7 as minimum requirements. It supports Swift Package Manager, CocoaPods, and Carthage.

This is version-qualified repository evidence, not current merchant eligibility guidance. The payment methods returned by the merchant backend, account configuration, shopper context, region, and transaction determine what can actually be offered.

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

Several optional paths delegate runtime behavior to separately versioned dependencies, including Adyen 3DS2, authentication, networking, WeChat Pay, Cash App Pay, and the bundled Twint SDK. Their presence in the package does not make this snapshot evidence for the complete delegated implementation.

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

## Related

- [[source-github-adyen-ios]] - cumulative exact-SHA repository evidence
- [[changelog-github-adyen-ios]] - package-qualified release ledger
- [[source-github-adyen-web]] - independently versioned browser SDK
- [[adyen-react-native-sdk]] - wrapper baseline that pins Adyen iOS `5.25.1`
- [[co-badged-cards]] - cross-provider card-network choice
- [[adyen]] - company and knowledge-status page
