---
title: "GitHub: stripe/stripe-ios"
type: source
date_ingested: 2026-05-13
date_updated: 2026-07-31
original_format: github-repo
raw_files:
  - "github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/manifest.json"
  - "github-stripe-ios.md"
tags: [stripe, ios, swift, mobile, sdk, payments, apple-pay, payment-sheet, embedded-payment-element, connect, identity, financial-connections, crypto-onramp, github-repository]
---

## Overview

`stripe/stripe-ios` publishes Stripe's official modular Swift SDK for native iOS payments and adjacent products. This cumulative page preserves the legacy `25.14.0` manual capsule and adds the approved `stripe-ios@26.4.1` full baseline at commit `d9252fd0a4a6d369fa45bb06f74c4e818c914f91`.

Repository: <https://github.com/stripe/stripe-ios>

## Evidence Boundary

- The `26.4.1` capsule retains 259 documentation, build, example, public API, and implementation files, including 245 Swift files. Tests, fixtures, generated documentation, CI, and general tooling are excluded by policy.
- This is a bounded public-source capsule, not a full repository mirror. A later query that needs excluded implementation requires an immutable supplement tied to the exact SHA.
- The legacy `25.14.0` evidence is a manually selected capsule. No automated comparison exists from its SHA to `26.4.1`, so retained findings are not represented as a complete file-by-file diff.
- Public types and payment-method models do not prove merchant eligibility, geographic availability, enabled Dashboard configuration, connected-account support, or preview access.
- `PaymentSheetResult.completed` does not prove that funds moved. Fulfillment remains gated by a successful server-side Stripe payment event.

## Grounding Excerpts

> "This means the sensitive data is sent directly to Stripe instead of passing through your server."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/README.md:37`

> "The Stripe iOS SDK supports all Apple supported Xcode versions and is compatible with apps targeting iOS 15 or above."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/README.md:113`

> "The payment may still be processing at this point; don't assume money has successfully moved."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet.swift:18-23`

> "If this is set to true, make sure your integration listens to webhooks for notifications on whether a payment has succeeded or not."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetConfiguration.swift:79-82`

> "Fixed an issue where some Alipay payments incorrectly reported failure after succeeding."
>
> `raw/github/stripe/stripe-ios/releases/stripe-ios/26.4.1/2026-07-31/release-notes.md:1-3`

## Package Status

| Package | Latest ingested release | Exact SHA | Evidence status |
| --- | --- | --- | --- |
| `stripe-ios` | `26.4.1` | `d9252fd0a4a6d369fa45bb06f74c4e818c914f91` | Approved full baseline; legacy `25.14.0` retained |

This table reports wiki ingest progress, not the latest release published upstream.

## Architecture

The retained package manifest and source expose these principal layers:

1. `StripePaymentSheet` owns PaymentSheet, FlowController, Embedded Payment Element, CustomerSheet, Link configuration, appearance, and deferred confirmation.
2. `StripePayments` owns low-level PaymentIntent, SetupIntent, PaymentMethod, token, Source, Radar, microdeposit, and authentication APIs.
3. `StripeApplePay` provides a lightweight `STPApplePayContext`, including an App Clip oriented installation surface.
4. Product modules expose Connect embedded components, Financial Connections, Identity, Issuing, card scanning, and alpha Crypto Onramp coordination.
5. UIKit and SwiftUI examples demonstrate PaymentSheet, FlowController, Embedded Payment Element, and direct US bank account collection.

The package manifest includes internal support modules such as `StripeCore`, `StripeUICore`, `Stripe3DS2`, and `StripeCameraCore`. Their inclusion is inventory evidence, not a claim that their internal APIs are supported merchant surfaces.

## Core Payment Surfaces

### PaymentSheet

PaymentSheet is the prebuilt collect-and-confirm UI. It supports an existing PaymentIntent client secret, an existing SetupIntent client secret, an `IntentConfiguration` deferred flow, and a Checkout Session client secret. Callback, async, UIKit, and SwiftUI presentation paths are retained.

`PaymentSheet.Configuration` controls merchant display, customer credentials, Apple Pay, Link, appearance, billing and shipping collection, return URLs, delayed methods, payment-method ordering, card-brand acceptance, custom methods, and external methods. These client options do not override account or Intent eligibility.

### FlowController

FlowController separates selection from confirmation for merchant-owned checkout composition. The app creates the controller, presents payment options, renders `PaymentOptionDisplayData`, and confirms from its own buy button. Current APIs include callback and async creation, presentation, confirmation, and update operations.

### Embedded Payment Element

`EmbeddedPaymentElement` puts payment-method selection directly into UIKit or SwiftUI. Its contract includes creation, configuration updates, payment-option display data, clearing selection, delegate-based height and option updates, and async confirmation. The merchant supplies the confirm button and a presenting view controller.

### CustomerSheet

CustomerSheet manages saved payment methods using Customer Session credentials. Configuration covers billing collection, preferred networks, card-brand acceptance, Apple Pay, appearance, return URLs, and card scanning. The v25 migration removed the older ephemeral-key-secret customer configuration in favor of Customer Sessions.

## Completion and Delayed Methods

`PaymentSheetResult` returns `completed`, `canceled`, or `failed`. `completed` is the end of the SDK interaction, not settlement proof. The source explicitly directs merchants to transition to a generic receipt and fulfill only after receiving a successful Stripe payment event.

`allowsDelayedPaymentMethods` enables methods that may settle later or require subsequent customer action, including bank debits and voucher-style methods. When enabled, webhook handling is mandatory for success and failure determination.

## Apple Pay

`STPApplePayContext` presents Apple Pay, creates a PaymentMethod from `PKPayment`, delegates Intent confirmation, and reports completion. It supports async delegate methods, request customization, shipping updates, coupon changes, explicit dismissal, and presentation without requiring the old retained view-controller pattern.

The `StripeApplePay` module is the lightweight option for Apple Pay-only integrations and App Clips. Apple Pay completion is still subject to server-side event verification before fulfillment.

## Low-Level Payments and Authentication

`STPAPIClient` exposes callback and async operations for PaymentMethods, tokens, legacy Sources, PaymentIntents, SetupIntents, microdeposit verification, and Radar Sessions. It also exposes Apple Pay conversions and payment-method-specific option models.

`STPPaymentHandler` confirms PaymentIntents and SetupIntents and handles redirects, app-to-app flows, and native 3DS2 authentication through `STPAuthenticationContext`. Current method names explicitly identify PaymentIntent or SetupIntent operations; older generic methods remain deprecated aliases.

The retained models cover cards, bank accounts, Link, Alipay, BLIK, Cash App Pay, PayPal, PayPay, Revolut Pay, Swish, TWINT, WeChat Pay, Wero, and other methods. Model presence is not proof that PaymentSheet supports every method or that a merchant can enable it.

## Specialized Product Modules

### Connect

`EmbeddedComponentManager` creates account onboarding, account management, payment details, notification banner, payouts, payments, and check-scanning components. Payments and Payouts became public API in `26.3.0`. The client still depends on server-created access credentials and product eligibility.

### Financial Connections

`FinancialConnectionsSheet` presents a server-created Financial Connections Session and returns session or token-oriented results. It exposes callback and async presentation and optional event handling.

### Identity

`IdentityVerificationSheet` presents document and selfie verification from a server-created Verification Session client secret. The retained API includes configuration, presentation, and explicit completed, canceled, and failed outcomes.

### Crypto Onramp

The alpha `CryptoOnrampCoordinator` covers Link account discovery and authentication, KYC, compliance identifiers, user attestation, wallet registration and ownership verification, payment-method collection, crypto payment-token creation, and checkout. Alpha and private-preview APIs must not be represented as generally available.

### Issuing

`STPPushProvisioningContext` supports adding Issuing cards to Apple Wallet. `STPPinManagementService` remains public but is deprecated in favor of Issuing Elements.

## Platform and Migration Requirements

| Requirement | `26.4.1` baseline |
| --- | --- |
| iOS | 15+ |
| iOS 13/14 fallback | `stripe-ios@25.17.0` |
| Catalyst | macOS 12+ |
| Package managers | Swift Package Manager and CocoaPods supported |
| Carthage | Binaries published, but CLI integration no longer officially tested |

Version 26 raises the deployment target from iOS 13 to iOS 15. Version 25 broadly adopts async APIs and strict-concurrency annotations, makes Customer Sessions and Confirmation Tokens generally available, renames several payment APIs, and removes deprecated Source-era behaviors. Applications crossing either major version must follow `MIGRATING.md` and regression-test payment completion, redirects, 3DS, delayed methods, saved methods, Apple Pay, and Swift concurrency.

## Version History

### `stripe-ios@26.4.1`

The exact patch fixes some successful Alipay payments being incorrectly reported as failures. It does not introduce the broader architecture summarized above.

### Accumulated `25.15.0--26.4.0` Context

- `25.15.0--25.17.0` adds Onelink, saved-card art, Identity manual capture, richer Crypto Onramp errors, and the `InstantBankPaymentsController` rename.
- `26.0.0` raises the minimum iOS version to 15.
- `26.1.0--26.2.0` fixes Swift Package Manager and CustomerSheet issues and revises alpha Crypto Onramp attestation and error contracts.
- `26.3.0` adds alpha wallet-ownership verification, private-preview standalone Link APIs, and public Connect Payments/Payouts components.
- `26.4.0` makes `STPAPIClient.betas` public and separates private-preview Link SetupIntent confirmation.

These milestones come from the cumulative changelog, not automated comparisons against every intermediate release.

### Legacy `stripe-ios@25.14.0`

The May 2026 manual capsule established the modular SDK, PaymentSheet, FlowController, Embedded Payment Element, CustomerSheet, Apple Pay, low-level API bindings, 3DS handling, localization, and the iOS 13 platform floor. Those findings remain queryable and are extended rather than replaced.

## Integration Guidance

- Prefer PaymentSheet for a maintained prebuilt checkout, FlowController for merchant-owned composition, and Embedded Payment Element for inline payment-method UI.
- Create Intents and customer or session credentials on the backend; return only publishable configuration and client secrets to the app.
- Treat `completed` as completion of the SDK interaction, not settlement evidence; fulfill from successful server-side events.
- Verify payment-method, country, currency, connected-account, and preview eligibility independently of public API presence.
- Use Apple in-app purchase APIs for digital products or services consumed in the app, subject to current policy and regional rules.
- Review `MIGRATING.md` before major upgrades and pin `25.17.0` when iOS 13 or 14 support remains mandatory.

## Related

- Company: [[stripe]]
- Concept: [[stripe-ios-sdk]]
- Native counterpart: [[source-github-stripe-android]]
- React Native bridge: [[source-github-stripe-react-native]]
- Higher-level billing SDK: [[source-stripe-billing-ios-sdk]]
- History: [[changelog-github-stripe-ios]]

## Raw Sources

- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/manifest.json` - exact-SHA `26.4.1` bounded source capsule
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.4.1/2026-07-31/manifest.json` - package-qualified release record
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.4.1/2026-07-31/release-notes.md` - exact upstream release note
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/README.md` - purpose, security, modules, policy boundary, and requirements
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/MIGRATING.md` - major-version migration requirements
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/CHANGELOG.md` - cumulative upstream release history
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/Package.swift` - product, target, dependency, and platform inventory
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet.swift` - result and prebuilt-sheet contract
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetConfiguration.swift` - configuration and delayed-method boundary
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetFlowController.swift` - custom-flow contract
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElement.swift` - inline element lifecycle
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripeApplePay/StripeApplePay/Source/ApplePayContext/STPApplePayContext.swift` - Apple Pay lifecycle
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePayments/StripePayments/Source/API Bindings/STPAPIClient+Payments.swift` - low-level payment operations
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift` - confirmation, redirects, and 3DS handling
- `raw/github-stripe-ios.md` - legacy `25.14.0` capsule pointer
