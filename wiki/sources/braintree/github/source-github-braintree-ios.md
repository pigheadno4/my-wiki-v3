---
title: "GitHub: braintree/braintree_ios"
type: source
date_ingested: 2026-10-04
original_format: github-repo
raw_files:
  - "github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/manifest.json"
  - "github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/manifest.json"
  - "github/braintree/braintree_ios/snapshots/2026-10-04-2a9aa1e/manifest.json"
  - "github/braintree/braintree_ios/snapshots/2026-10-04-eb7f88e/manifest.json"
  - "github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/manifest.json"
tags: [braintree, ios, mobile-sdk, swift, paypal, venmo, apple-pay, github-repository]
---

## Overview

`braintree-ios@7.9.0` is the first retained exact-SHA baseline for Braintree's modular native iOS SDK. It accepts client authorization, runs payment-method-specific native or redirect flows, and returns Braintree payment-method nonces for merchant-server processing.

## Baseline and Package Structure

The retained release resolves to SHA `4e987ca19f03b65a0d303b4c3ec95e0c723be971` and requires iOS 16+, Xcode 16.2+, and Swift 5.10+. Swift Package Manager exposes separate American Express, Apple Pay, Card, Core, Data Collector, Local Payment, PayPal, PayPal Messaging, SEPA Direct Debit, Shopper Insights, 3D Secure, Venmo, and UIComponents products.

Swift Package Manager is the recommended integration path. CocoaPods remains represented but the README says support will be removed in late 2026; Carthage is supported without a long-term guarantee. These repository statements should be rechecked before time-sensitive migration guidance.

## Authorization, Configuration, and Server Handoff

Feature clients initialize with a Braintree client token or tokenization key and load merchant configuration before capability-sensitive operations. Successful flows return typed subclasses of `BTPaymentMethodNonce`. The demo sends the nonce to a merchant endpoint that creates the transaction, demonstrating that the mobile SDK is the client/tokenization layer rather than the transaction-processing server.

Authorization is not interchangeable for every feature. The retained 3D Secure implementation requires a client token for lookup. Client-side Venmo vaulting requires a client token generated with a customer ID, while ordinary tokenization surfaces can accept either authorization type.

## PayPal Checkout, Vault, and App Switch

`BTPayPalClient` supports separate Checkout and Vault request types:

- Checkout accepts amount, authorize/sale/order intent, Pay Later or Credit offers, shipping and contact controls, line items, optional billing-agreement consent, and recurring-billing metadata.
- Vault creates billing-agreement consent without a checkout amount and can also carry recurring-plan metadata.
- Both flows return a `BTPayPalAccountNonce` for Braintree server processing.

The optional PayPal app-switch path uses a merchant universal link and optional registered fallback URL scheme. Source comments mark the app-switch initializer beta and production-only. Braintree iOS v7 removes the former PayPal Native Checkout module and directs merchants to the PayPal web flow; it is not evidence for standalone `paypal/paypal-ios` behavior.

Recurring metadata and billing-agreement consent do not schedule or execute later charges. The merchant's Braintree server integration remains responsible for storing the resulting payment method and performing future transactions.

## Native Venmo Flow and Vaulting

Venmo is a dedicated Braintree module. `BTVenmoClient` requires a valid HTTPS universal link dedicated to Braintree app-switch returns. The v7 flow opens the Venmo app when installed and otherwise falls back to the buyer's default browser.

`BTVenmoRequest` distinguishes `.singleUse` from `.multiUse`. A single-use request cannot be vaulted. Automatic client-side vaulting requires `.multiUse`, `vault: true`, and a customer-scoped client token; when `vault` is false, a multi-use nonce can still be vaulted by the merchant server.

The request can carry a Venmo profile, risk correlation ID, billing or shipping address collection, final-amount status, amount breakdown, and up to 249 line items. Availability still depends on Braintree configuration and buyer eligibility. A rendered Venmo button or retained module does not prove that a merchant can present or process Venmo.

## Apple Pay Boundary

`BTApplePayClient` checks merchant/device support, creates a `PKPaymentRequest` populated with Braintree configuration, and tokenizes an authorized `PKPayment` through `v1/payment_methods/apple_payment_tokens`. The merchant supplies payment summary items and presents the Apple Pay sheet.

The demo attaches a `PKRecurringPaymentRequest`, but the retained SDK implementation only establishes Apple Pay request creation and nonce tokenization. It does not establish a subscription engine or the complete stored-token and merchant-initiated-charge lifecycle.

## Cards, 3D Secure, and Risk

Card tokenization uses GraphQL when remote configuration advertises `tokenize_credit_cards`; otherwise it uses the REST card endpoint. The card model supports billing data and optional authentication insight, while the returned card nonce includes card details and 3D Secure information.

The 3D Secure module performs a version 2 lookup and optional Cardinal challenge around a card nonce. It requires a configuration JWT, non-empty amount, and request delegate; 3D Secure v1 is explicitly unsupported. Client-side liability indicators are flow inputs and do not replace server-side transaction controls.

Data Collector uses the retained PPRiskMagnes binary dependency and returns device data for fraud tooling. Device-data collection is evidence of a risk input, not proof that a particular fraud product or rule set is active.

## Additional Payment and Presentation Modules

- Local Payment uses a web-authentication-session return flow and tokenizes the approved local-payment account.
- SEPA Direct Debit creates mandate and debit-account artifacts and returns a SEPA nonce.
- American Express looks up rewards balance from an already tokenized Amex card nonce.
- Shopper Insights has beta customer-session and recommendation APIs for PayPal and Venmo presentation. Recommendations inform ordering; they do not override merchant configuration or buyer eligibility.
- PayPal Messaging is a beta Pay Later messaging surface, not a payment session.
- UIComponents provides SwiftUI PayPal and Venmo buttons plus a card form with validation, card-brand detection, focus management, and merchant-controlled submission.

## v7 Migration and Exact `7.9.0` Change

The v7 migration moves request properties to initializers, changes feature clients to accept authorization directly, renames the Local Payment and 3D Secure start methods, makes Venmo universal-link handling mandatory, updates the PayPal app query scheme to `paypal`, and removes PayPal Native Checkout.

Exact release `7.9.0` only fixes the BraintreeUIComponents minimum deployment target to iOS 16 so it matches the other modules. Other v7 behavior is cumulative baseline knowledge from the exact-SHA snapshot, not a claim that every behavior was introduced in `7.9.0`.

## `7.10.0` Delta from `7.9.0`

Exact SHA `eb7f88e8e4ad03fcf79ce5e2926755f7934201d0` adds optional campaign context, recommendation expiry metadata and a Venmo vault identity fix. The earlier baseline above remains version-qualified historical knowledge.

- **PayPal Checkout:** both checkout initializers accept `campaigns: [BTPayPalCampaign]? = nil`. Each object carries an `id`; a nonempty array encodes as `paypal_campaigns` in `v1/paypal_hermes/create_payment_resource`. Nil and empty arrays omit the field. This propagates context, not campaign eligibility, campaign creation or a new Vault API.
- **Shopper Insights:** beta `BTCustomerSessionRequest` adds `payPalCampaigns: [ShopperInsightsCampaign]? = nil`, serialized as `paypalCampaigns` in shared GraphQL input variables. Recommendations select and return optional `expiresAt: String?`, documented as ISO-8601; the reviewed result/API code neither converts it to a Date nor enforces expiration automatically.
- **Venmo:** the vault response parser sets `BTVenmoAccountNonce.externalID` from `details.commonId`. Previously this branch populated only nonce, username and default status. Non-vaulted payment-context parsing still reads `payerInfo.externalId`; missing commonId can still produce nil. Authorization and vault eligibility requirements remain unchanged.
- **Demos:** Apple Pay, card tokenization and iDEAL move presentation into SwiftUI views embedded by UIKit controllers. Apple Pay still delegates sheet presentation and tokenization to the controller; recurring request metadata is not a subscription engine. Campaign demo fields split comma-separated IDs, trim whitespace and filter empty entries. These changes do not establish new SDK transaction capabilities.

Illustrative construction from retained public initializers (not runtime-tested; use valid merchant campaign context):

```swift
let checkout = BTPayPalCheckoutRequest(
    amount: "10.00",
    campaigns: [BTPayPalCampaign(id: campaignID)]
)
let session = BTCustomerSessionRequest(
    payPalCampaigns: [ShopperInsightsCampaign(id: campaignID)]
)
```

## `7.11.0` Delta from `7.10.0`

Exact SHA `2a9aa1e20b1d066cb97c66af3e2ccd7f17e90fc0`. Release notes attribute this update to a revoked Magnes signing certificate. SPM replaces the local PPRiskMagnes binary target with `paypal-risk-ios` exact 5.6.0 and its `PayPalRisk` product, referenced by DataCollector and 3DS targets. CocoaPods DataCollector depends on `PayPalRisk` 5.6.0; Carthage references the hosted PayPalRisk JSON manifest. DataCollector implementation is unchanged and still imports `PPRiskMagnes`.

Release notes describe a static-to-dynamic transition: SPM requires no consumer source action; CocoaPods embeds the dynamic framework even with static linkage or no use_frameworks. Carthage consumers must run `carthage update --use-xcframeworks` and add `PPRiskMagnes.xcframework` to Embed Frameworks/copy-frameworks inputs. Binary internals/signatures were not collected or tested; migration declarations do not prove a resolved local build/signature issue.

## `7.12.0` Delta from `7.11.0`

Exact SHA `09bc25a1564b0eb8c802d2ef396ec27ceaf9cd2f`. Release notes announce Xcode 27/iOS 27 support; this is not a local build result. SPM/CocoaPods still declare an iOS 16 minimum. PayPalMessages upgrades from 1.0.0 to 2.0.0 in SPM (new URL/checksum), CocoaPods and Carthage. The binary implementation remains delegated; no messaging eligibility or frontend behavior is inferred from the version bump.

Card GraphQL/REST body files move into Models, and BTPayPalCampaign moves out of Models, all with unchanged content. CocoaPods Card source selection expands from `*.swift` to `**/*.swift` to include nested models. No card wire-format/API change is established by those moves.

The Amex demo becomes SwiftUI with in-flight action guarding, async card tokenization followed by rewards-balance lookup and nonce completion after a non-error response. An errorMessage returns before completion; incomplete balance fields log an unexpected response but still reach completion. This is a demo handoff change, not rewards redemption or transaction-processing evidence.

## `7.13.0` Delta from `7.12.0`

Exact SHA `020dfb7a7803ec3ce8b2df2a0f71e386a4bf84e3`. SPM and CocoaPods lower the deployment target to iOS 15; README/migration guidance follows, retaining Xcode 16.2 and Swift 5.10 requirements. Prior snapshots' iOS 16 floors remain historical facts.

PayPal handleReturn is now MainActor-isolated and opens a UIKit background task named BTPayPalHandleReturnTokenize around `/v1/payment_methods/paypal_accounts`. Expiration cancels the tokenization task and ends the background task; deferred cleanup ends it on ordinary completion. CancellationError or URLError.cancelled triggers failure notification and `BTPayPalError.returnBackgroundTaskExpired` (domain com.braintreepayments.BTPayPalErrorDomain, code 15); other errors retain their identity. The mapping does not independently verify OS expiry, so code 15 alone is not definitive expiry-cause evidence. This finite execution allowance does not guarantee payment completion. Weak-self app-switch/browser callback tasks handle client deallocation explicitly.

BackgroundTaskManaging moves from Analytics into shared Core with public visibility but internal/nodoc, non-semver-covered documentation; it is not a recommended merchant integration API. BTHTTP uses legacy locale language/region access before iOS 16, CVV delay uses nanosecond Task.sleep, and brand matching uses anchored NSRegularExpression instead of Swift Regex. Strict-brand matching precedes relaxed Maestro; Discover remains before UnionPay.

The Apple Pay demo wraps PKPaymentButton through UIViewRepresentable with zero corner radius. recurringPaymentRequest is gated to iOS 16+, so the new iOS 15 SDK floor does not enable recurring metadata on iOS 15. These compatibility changes do not establish a new server transaction/subscription capability.

## Evidence Boundaries

This capsule excludes tests, fixtures, CI, tooling, generated documentation, and binary framework internals. CardinalMobile, PPRiskMagnes, and PayPalMessages behavior beyond their declared versions is delegated evidence. The first exact-SHA baseline is 7.9.0; historical entries before that provide migration context, not retained version-to-version proof. Subsequent deltas have separately retained snapshots and comparisons. No build or live payment test was performed.

## Related

- [[changelog-github-braintree-ios]] - package-qualified iOS release ledger
- [[braintree-ios-sdk]] - native iOS SDK concept
- [[paypal-braintree-integration]] - Braintree PayPal boundary
- [[recurring-payments]] - later-charge requirements and evidence boundary
- [[braintree]] - company and knowledge-status page

## Raw Sources

- 7.13.0 snapshot: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/manifest.json`
- 7.13.0 release: `raw/github/braintree/braintree_ios/releases/braintree-ios/7.13.0/2026-10-04/manifest.json` and `raw/github/braintree/braintree_ios/releases/braintree-ios/7.13.0/2026-10-04/release-notes.md`
- 7.12.0--7.13.0 comparison: `tracking/github/repos/braintree/braintree_ios/comparisons/braintree-ios/7.12.0--7.13.0/comparison.json`
- 7.13.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Package.swift`
- 7.13.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Braintree.podspec`
- 7.13.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/README.md`
- 7.13.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/V7_MIGRATION.md`
- 7.13.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreePayPal/BTPayPalClient.swift`
- 7.13.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreePayPal/BTPayPalError.swift`
- 7.13.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreeCore/UIApplication+BackgroundTaskManaging.swift`
- 7.13.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreeCore/BTHTTP.swift`
- 7.13.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreeUIComponents/CardFields/Shared/CardBrand.swift`
- 7.13.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreeUIComponents/CardFields/CVVField/CVVFieldViewModel.swift`
- 7.13.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Demo/Application/Features/ApplePayView.swift`

- 7.12.0 snapshot: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/manifest.json`
- 7.12.0 release: `raw/github/braintree/braintree_ios/releases/braintree-ios/7.12.0/2026-10-04/manifest.json` and `raw/github/braintree/braintree_ios/releases/braintree-ios/7.12.0/2026-10-04/release-notes.md`
- 7.11.0--7.12.0 comparison: `tracking/github/repos/braintree/braintree_ios/comparisons/braintree-ios/7.11.0--7.12.0/comparison.json`
- 7.12.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/files/Braintree.podspec`
- 7.12.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/files/Package.swift`
- 7.12.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/files/Cartfile`
- 7.12.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/files/Demo/Application/Features/AmexView.swift`
- 7.12.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/files/Sources/BraintreeCard/Models/CreditCardGraphQLBody.swift`
- 7.12.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/files/Sources/BraintreeCard/Models/CreditCardPOSTBody.swift`
- 7.12.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/files/Sources/BraintreePayPal/BTPayPalCampaign.swift`

- 7.11.0 snapshot: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-2a9aa1e/manifest.json`
- 7.11.0 release: `raw/github/braintree/braintree_ios/releases/braintree-ios/7.11.0/2026-10-04/manifest.json` and `raw/github/braintree/braintree_ios/releases/braintree-ios/7.11.0/2026-10-04/release-notes.md`
- 7.10.0--7.11.0 comparison: `tracking/github/repos/braintree/braintree_ios/comparisons/braintree-ios/7.10.0--7.11.0/comparison.json`
- 7.11.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-2a9aa1e/files/Package.swift`
- 7.11.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-2a9aa1e/files/Braintree.podspec`
- 7.11.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-2a9aa1e/files/Cartfile`
- 7.11.0 implementation: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-2a9aa1e/files/Sources/BraintreeDataCollector/BTDataCollector.swift`

- 7.10.0 snapshot: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-eb7f88e/manifest.json`
- 7.10.0 release: `raw/github/braintree/braintree_ios/releases/braintree-ios/7.10.0/2026-10-04/manifest.json` and `raw/github/braintree/braintree_ios/releases/braintree-ios/7.10.0/2026-10-04/release-notes.md`
- 7.9.0--7.10.0 comparison: `tracking/github/repos/braintree/braintree_ios/comparisons/braintree-ios/7.9.0--7.10.0/comparison.json`
- Campaign request: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-eb7f88e/files/Sources/BraintreePayPal/BTPayPalCheckoutRequest.swift`
- Campaign encoding: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-eb7f88e/files/Sources/BraintreePayPal/Models/PayPalCheckoutPOSTBody.swift`
- Shopper Insights encoding: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-eb7f88e/files/Sources/BraintreeShopperInsights/Models/Variables.swift`
- Recommendation expiry: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-eb7f88e/files/Sources/BraintreeShopperInsights/V2/BTCustomerRecommendationsAPI.swift`
- Venmo identity: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-eb7f88e/files/Sources/BraintreeVenmo/BTVenmoAccountNonce.swift`

- Snapshot manifest: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/manifest.json`
- Release manifest: `raw/github/braintree/braintree_ios/releases/braintree-ios/7.9.0/2026-08-01/manifest.json`
- Release notes: `raw/github/braintree/braintree_ios/releases/braintree-ios/7.9.0/2026-08-01/release-notes.md`
- README: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/README.md`
- Repository changelog: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/CHANGELOG.md`
- v7 migration guide: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/V7_MIGRATION.md`
- Package manifest: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/Package.swift`
- PayPal source: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/Sources/BraintreePayPal/`
- Venmo source: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/Sources/BraintreeVenmo/`
- Apple Pay source: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/Sources/BraintreeApplePay/`
- 3D Secure source: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/Sources/BraintreeThreeDSecure/`
- UIComponents source: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/Sources/BraintreeUIComponents/`
