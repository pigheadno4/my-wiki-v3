---
title: "Stripe iOS SDK"
type: concept
category: framework
tags: [stripe, ios, swift, mobile, sdk, payments, apple-pay, payment-sheet, embedded-payments]
---

## Overview

`stripe-ios` is Stripe's official modular Swift SDK for native iOS payments and adjacent products. The retained history covers the legacy `25.14.0` capsule and the approved `stripe-ios@26.4.1` baseline at commit `d9252fd0a4a6d369fa45bb06f74c4e818c914f91`.

Version `26.4.1` requires iOS 15 or later. Apps that still target iOS 13 or 14 must remain on `25.17.0`. The SDK supports Swift Package Manager and CocoaPods; Carthage binaries continue to be published but are no longer officially tested.

## Security and fulfillment boundary

Sensitive payment details are sent directly to Stripe instead of passing through the merchant server. The merchant backend still owns secret-key operations, including creating Intents and issuing customer or session credentials.

`PaymentSheetResult.completed` means that the customer completed the SDK payment or setup interaction. The payment may still be processing, so order fulfillment must wait for a successful Stripe payment event. This boundary is especially important when `allowsDelayedPaymentMethods` enables bank debits, vouchers, or methods that require later customer action.

## Module architecture

| Module | Purpose |
| --- | --- |
| `StripePaymentSheet` | PaymentSheet, FlowController, Embedded Payment Element, CustomerSheet, Link, appearance, and payment-method configuration |
| `StripePayments` | Low-level PaymentIntent, SetupIntent, PaymentMethod, token, source, Radar, and next-action APIs |
| `StripePaymentsUI` | Card fields, card forms, and lower-level payment UI |
| `StripeApplePay` | Lightweight Apple Pay integration, including App Clip support |
| `StripeConnect` | Embedded connected-account onboarding, management, payments, payouts, and check scanning |
| `StripeFinancialConnections` | Financial-account collection and token/session results |
| `StripeIdentity` | Native identity-document and selfie verification |
| `StripeIssuing` | Issuing PIN and Apple Wallet provisioning APIs |
| `StripeCryptoOnramp` | Alpha Link, KYC, wallet, payment-method, and crypto-checkout coordination |
| `Stripe` | Umbrella product containing the payment modules and Issuing |

The package manifest also contains internal dependencies such as `StripeCore`, `StripeUICore`, `Stripe3DS2`, and `StripeCameraCore`. Their presence does not make every internal API a supported merchant integration surface.

## Payment UI choices

### PaymentSheet

PaymentSheet provides a prebuilt collect-and-confirm flow. It can load an existing PaymentIntent or SetupIntent client secret, use an intent configuration that asks the merchant backend to create or confirm an Intent after collection, or initialize from a Checkout Session client secret.

`PaymentSheet.Configuration` controls merchant display, customer credentials, Apple Pay, Link, appearance, billing and shipping collection, delayed methods, payment-method order, card-brand acceptance, custom methods, and external methods.

### FlowController

FlowController separates payment-option selection from confirmation so the merchant can own the surrounding checkout UI. It exposes sync, callback, and async APIs for creation, option presentation, confirmation, and updates.

### Embedded Payment Element

`EmbeddedPaymentElement` places payment-method selection directly in a UIKit or SwiftUI hierarchy. It supports creation, configuration updates, payment-option display data, clearing selection, and async confirmation. The merchant owns the confirm button and presenting view controller.

### CustomerSheet

CustomerSheet manages saved payment methods. Current configuration covers Customer Session credentials, billing collection, card-brand acceptance, Apple Pay, preferred networks, and card scanning. Customer Sessions replaced the older ephemeral-key-only configuration in the v25 migration.

## Apple Pay

`STPApplePayContext` creates a Stripe PaymentMethod from a `PKPayment`, asks the delegate for confirmation details, and reports completion. It supports UIKit, SwiftUI-compatible presentation, async delegate methods, request customization, shipping and coupon changes, and explicit dismissal.

The lightweight `StripeApplePay` module is intended for integrations that do not need the larger payment UI, including App Clips. Apple Pay UI completion remains subject to the same server-side fulfillment boundary as other payment methods.

## Low-level payments and authentication

`STPAPIClient` exposes callback and async operations for:

- creating PaymentMethods, tokens, and legacy Sources;
- retrieving and confirming PaymentIntents and SetupIntents;
- updating PaymentMethods;
- verifying Intents with microdeposits; and
- creating Radar Sessions.

`STPPaymentHandler` confirms Intents and handles redirects, app-to-app flows, and native 3DS2 authentication through an `STPAuthenticationContext`. Its modern method names use `confirmPaymentIntent`, `confirmSetupIntent`, and `handleNextAction`; older generic names remain deprecated aliases.

The retained source models many payment-method bindings, but a public enum or model does not prove that a method is enabled for a particular merchant, country, currency, Intent mode, or connected account.

## Specialized products

### Connect

`EmbeddedComponentManager` creates account onboarding, account management, payment details, notifications, payouts, payments, and check-scanning components. Payments and Payouts became public API in `26.3.0`; merchant availability and server-created access credentials must be verified separately.

### Financial Connections and Identity

`FinancialConnectionsSheet` returns session or token-oriented results from a server-created Financial Connections Session client secret. `IdentityVerificationSheet` presents native verification from a server-created Verification Session client secret. Neither client surface replaces backend creation or result verification.

### Crypto Onramp

The alpha `CryptoOnrampCoordinator` supports Link account discovery and authentication, KYC, compliance identifiers, user attestation, wallet registration and ownership verification, payment-method collection, crypto payment-token creation, and checkout. Alpha and preview APIs must not be represented as generally available.

### Issuing

`STPPushProvisioningContext` supports adding Issuing cards to Apple Wallet. `STPPinManagementService` remains available but is deprecated in favor of Issuing Elements.

## Platform and migration history

| Version | Important boundary |
| --- | --- |
| `26.4.1` | Fixes some successful Alipay payments being incorrectly reported as failures |
| `26.4.0` | Makes `STPAPIClient.betas` public for preview API-version flags |
| `26.3.0` | Adds alpha wallet-ownership verification, private-preview standalone Link APIs, and public Connect Payments/Payouts components |
| `26.0.0` | Raises the minimum deployment target from iOS 13 to iOS 15 |
| `25.17.0` | Last documented release for iOS 13 and 14 |
| `25.0.0` | Adds async APIs broadly, makes Customer Sessions and Confirmation Tokens generally available, and removes several deprecated payment APIs |
| `25.14.0` | Legacy wiki baseline retained for historical queries |

The exact `26.4.1` patch is narrow. Broader architecture and migration findings come from the complete retained `26.4.1` capsule and cumulative changelog, not from that patch note alone.

## App Store boundary

The SDK README states that digital products or services consumed inside the app, including subscriptions, game currency, premium content, and feature unlocks, must use Apple's in-app purchase APIs. Stripe can process other eligible payment scenarios. Current Apple policy and regional exceptions still require separate verification.

## Sources

- [[source-github-stripe-ios]] - cumulative GitHub source for `stripe/stripe-ios`
- [[changelog-github-stripe-ios]] - package-qualified release history
- [[source-stripe-billing-ios-sdk]] - separate private-preview BillingSDK with buy buttons, entitlements, and customer portal APIs
- [[stripe-android-sdk]] - native Android counterpart
