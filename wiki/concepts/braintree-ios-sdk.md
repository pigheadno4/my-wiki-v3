---
title: "Braintree iOS SDK"
type: concept
category: technology
tags: [braintree, ios, mobile, swift, paypal, venmo, apple-pay, cards, 3d-secure]
---

## Braintree iOS SDK

Braintree iOS is a modular native SDK for accepting cards and alternative payment methods in iOS applications. Payment-specific clients use a Braintree client token or tokenization key, perform any required native, browser, or app-switch flow, and return a Braintree payment-method nonce for merchant-server processing.

## Current Baseline

The first retained baseline is `braintree-ios@7.9.0` at exact SHA `4e987ca19f03b65a0d303b4c3ec95e0c723be971`. It requires iOS 16+, Xcode 16.2+, and Swift 5.10+.

The package exposes separate modules for Core, Card, Apple Pay, PayPal, Venmo, Local Payment, SEPA Direct Debit, 3D Secure, Data Collector, Shopper Insights, American Express, PayPal Messaging, and UIComponents. Source availability does not establish merchant configuration, buyer eligibility, or regional availability.

## Authorization and Nonce Boundary

Feature clients initialize directly from a client token or tokenization key. Successful card, wallet, and alternative-payment flows return typed subclasses of `BTPaymentMethodNonce`; the merchant sends the nonce to a Braintree server integration to create the transaction.

Some capabilities require stronger authorization context. For example, 3D Secure lookup requires a client token, and client-side Venmo vaulting requires a client token generated with a customer ID.

## PayPal and Venmo

PayPal and Venmo are independent Braintree modules, not funding-source variants of one native client:

- PayPal supports checkout, vault, checkout-with-vault billing agreement consent, recurring-billing metadata, Pay Later or Credit offers, and an optional PayPal app-switch path. The v7 app-switch API is beta and its source comments limit it to production.
- Venmo uses a merchant HTTPS universal link, opens the Venmo app when installed, and otherwise falls back to the buyer's default browser. Requests distinguish `.singleUse` from `.multiUse`.
- Client-side Venmo vaulting requires `paymentMethodUsage: .multiUse`, `vault: true`, and a customer-scoped client token. A multi-use nonce may instead be vaulted by the merchant server; a single-use request cannot be vaulted.

The removed PayPal Native Checkout module is not the replacement path. The v7 migration guide directs merchants to Braintree's PayPal web flow.

## Apple Pay and Recurring Boundary

`BTApplePayClient` checks merchant and device support, creates a partially configured `PKPaymentRequest`, and tokenizes an authorized `PKPayment` into a Braintree Apple Pay nonce. The merchant still supplies summary items and presents the Apple Pay sheet.

The demo attaches a `PKRecurringPaymentRequest`, but the retained SDK source does not implement a subscription scheduler or a complete merchant-initiated stored-token lifecycle. Treat the recurring sheet as buyer-facing Apple Pay request metadata, not proof that subsequent charges are configured.

## Cards, 3D Secure, and UI

Card tokenization selects GraphQL when the remote Braintree configuration enables it and otherwise uses the REST card endpoint. UIComponents supplies a SwiftUI `CardFields` form with validation and merchant-controlled submission, plus branded PayPal and Venmo buttons that invoke the corresponding tokenize flows.

The 3D Secure module performs a v2 lookup and optional Cardinal challenge around a card nonce. It requires the merchant configuration JWT and a request delegate; 3D Secure v1 is explicitly unsupported.

## `7.10.0` Campaign Context and Venmo Identity

Compared with `7.9.0`, `braintree-ios@7.10.0` adds optional campaign-ID objects to the PayPal Checkout initializer (`campaigns: [BTPayPalCampaign]?`) and beta Shopper Insights session initializer (`payPalCampaigns: [ShopperInsightsCampaign]?`). Nonempty arrays encode as `paypal_campaigns` for checkout and `paypalCampaigns` in GraphQL session/recommendation inputs; nil or empty arrays are omitted. Passing campaign IDs does not establish campaign eligibility or create a campaign.

Recommendation results expose optional ISO-8601 `expiresAt` as a string, not an SDK-enforced timer. Vaulted Venmo nonce parsing now fills `externalID` from `details.commonId`; absent data can still yield nil. The non-vaulted payment-context parser continues to use `payerInfo.externalId`. See [[source-github-braintree-ios]] and [[changelog-github-braintree-ios]].

## `7.11.0` Risk Framework Packaging

`braintree-ios@7.11.0` replaces locally bundled PPRiskMagnes with the `paypal-risk-ios` 5.6.0 package/PayPalRisk product (SPM), PayPalRisk 5.6.0 pod (CocoaPods), and hosted PayPalRisk binary manifest (Carthage). Release notes describe a revoked-signing-certificate fix and a static-to-dynamic framework transition. Carthage consumers must update XCFrameworks and embed PPRiskMagnes; source import remains `PPRiskMagnes`. The snapshot establishes declarations and migration guidance, not binary signature/build/runtime proof. See [[source-github-braintree-ios]].

## `7.12.0` Compatibility and Messaging Dependency

`braintree-ios@7.12.0` release notes announce Xcode 27/iOS 27 support; SPM and CocoaPods still declare an iOS 16 minimum in this snapshot. PayPalMessages moves from 1.0.0 to 2.0.0 across SPM, CocoaPods and Carthage. This dependency update alone does not establish new messaging eligibility or binary behavior. Card request-model and campaign-model paths move without content changes; CocoaPods expands its Card source glob recursively. The Amex demo becomes SwiftUI, tokenizes a card, requests rewards balance and passes the tokenized nonce to the completion callback on its non-error response path. See [[source-github-braintree-ios]]; not build/payment proof.

## `7.13.0` iOS 15 and PayPal Return Handling

`braintree-ios@7.13.0` lowers the declared minimum from iOS 16 to iOS 15 in SPM, CocoaPods, README and migration guidance; Xcode 16.2 and Swift 5.10 remain the documented floor. Older iOS 16 declarations above describe their retained versions, not the new release.

PayPal return tokenization now runs on MainActor and wraps its account POST in a finite UIKit background task. Expiry cancels the request task and ends background execution; cleanup also ends it on completion. CancellationError or URLError.cancelled maps to `BTPayPalError.returnBackgroundTaskExpired` (code 15), without an independent expiry-cause check. Do not treat this error alone as proof of OS expiry or promise unlimited background completion. Other request errors retain their identity.

Locale, card-brand regex and CVV-delay implementations adopt iOS 15-compatible APIs. The Apple Pay demo wraps the native PKPaymentButton, and its recurringPaymentRequest remains explicitly gated to iOS 16+. A lower SDK floor does not enable that recurring metadata on iOS 15. See [[source-github-braintree-ios]] and [[changelog-github-braintree-ios]]; not build or payment proof.

## Prebuilt iOS Drop-in


`BraintreeDropIn@9.14.0` is an independently versioned UIKit payment-selection package, not part of the `braintree-ios@7.9.0` release. It supports iOS 12+, Xcode 15+, and Swift 5.9 and requires the older `braintree_ios` 5.27 dependency line. Do not apply modular v7 behavior to this Drop-in baseline without a compatible release.

Drop-in can present cards, PayPal, Venmo, Apple Pay, saved methods, vault management, and card 3D Secure. Most selections return a nonce for merchant-server processing. Apple Pay is an exception: selection returns only the method type, after which the merchant presents the Apple Pay sheet and tokenizes the payment separately. Venmo is listed only when remote configuration enables it and the Venmo app is available for app switch; the default generated Venmo request sets `vault = true`.

The repository includes SwiftUI wrapper examples but does not officially support SwiftUI. A future cross-platform mobile Drop-in comparison should combine this source with the independently ingested Android Drop-in evidence.

## Version Boundary

The v7 migration moves request properties into initializers, changes feature clients to direct authorization initializers, renames Local Payment and 3D Secure start methods, requires universal-link handling for Venmo, and removes PayPal Native Checkout. Exact release `7.9.0` only aligns the BraintreeUIComponents minimum deployment target with iOS 16; broader v7 behavior comes from the cumulative exact-SHA baseline.

## Related

- [[source-braintree-docs-guides-shopper-insights-ios-v7]] - 2026-09-16 Braintree website iOS v7 route for beta Shopper Insights customer-session creation/update, PayPal or Venmo recommendations, qualified checkout presentment and display/selection analytics; preserves consent, client-token, SDK-availability and historical certificate conditions, and is not current availability, merchant eligibility, recommendation-result or payment-execution proof

- [[source-braintree-docs-guides-paypal-vault-ios-v7]] - 2026-09-16 Braintree website iOS v7 route for PayPal vault-request tokenization and nonce handoff, with required device data for non-recurring Vault transactions, separately qualified App Switch navigation, merchant-displayed amount/currency and a dated certificate warning; not current SDK support, enablement or payment-execution proof

- [[source-braintree-docs-guides-paypal-messaging-ios-v7]] - 2026-09-16 Braintree website iOS v7 route for adding Pay Later messages through `BTPayPalMessagingView`, preserving the page's latest-native-SDK wording, Drop-in exclusion, eligible-country and merchant/integration conditions, message-editing prohibition, category restrictions, and optional lifecycle callbacks; not current availability, eligibility, runtime-rendering or payment-execution proof

- [[source-braintree-docs-guides-paypal-app-switch-ios-v7]] - 2026-09-16 Braintree website iOS v7 route for beta PayPal App Switch setup and checkout/vault opt-in, including US/custom-integration eligibility, authentication-session fallback, Universal Link returns and specially conditioned Sandbox testing; preserves the website-versus-implementation environment conflict and does not establish current support, enablement or payment execution

- [[source-braintree-docs-guides-paypal-testing-go-live-ios-v7]] - 2026-09-16 Braintree website iOS v7 route for mocked versus linked PayPal sandbox testing, eligibility-qualified App Switch with `ASWebAuthenticationSession` fallback, and production credentials kept in server-side configuration with a dedicated Account Admin API-user warning and unchanged client-token configuration; preserves real-card/fee warnings and the unresolved website-versus-exact-SHA App Switch environment scope, and is not sibling-platform, current-availability, direct-PayPal, execution, settlement or funding proof

- [[source-braintree-docs-guides-paypal-checkout-with-paypal-ios-v7]] - 2026-09-16 website iOS v7 route for PayPal one-time checkout request tokenization, optional customization and App Switch navigation, preserving the historical mobile-certificate warning and the linked iOS v6 App Switch boundary; not current exact-package behavior, direct PayPal authority or payment-execution proof

- [[source-braintree-docs-guides-venmo-client-side-ios-v7]] - 2026-09-16 Braintree website iOS v7 Venmo client guide for app/browser return callbacks, single-use versus multi-use tokenization, nonce and device-data handoff to separate server transaction creation, and eligibility/Sandbox prerequisites; preserves the page's iOS `7.0.0+` versus `6.17.0+` certificate-notice conflict and does not establish current support, enablement or payment execution

- [[source-braintree-docs-guides-paypal-commerce-ios-setup]] - historical, unversioned PayPal Commerce iOS SDK setup snapshot for CocoaPods, Commerce Panel OAuth configuration, URL/app-delegate callbacks, optional platform integrations and store presentation; distinct from modular `braintree-ios` and its GitHub evidence, and not current enablement or payment proof

- [[source-braintree-docs-deprecated-client-side-encryption-ios-library]] - deprecated legacy iOS payment-form and client-side-encryption snapshot with merchant-server/gateway and production-versus-sandbox key boundaries; not current SDK support, PCI-compliance, authorization, or payment proof
- [[source-braintree-local-payment-methods-configuration-ios-v7]] - website iOS v7-routed Local Payment Methods prerequisite checklist for linked PayPal account, client authorization, client/server/webhook responsibilities and environment-specific success, preserving the historical certificate deadline and exact-package/execution boundaries
- [[source-braintree-local-payment-methods-client-side-custom-ios-v7]] - website iOS v7 custom Local Payment Methods document route with SDK/request locators, a captured undefined start argument, an omitted result body and separately qualified server-notification alternatives
- [[source-braintree-drop-in-customization-ios-v7]] - 2026-09-16 website snapshot from an iOS v7 Drop-in customization route, retained for lifecycle and SDK-routing notices; the route is not evidence of iOS v7 Drop-in support

- [[source-braintree-drop-in-setup-and-integration-ios-v7]] - captured iOS v7-routed Drop-in setup snapshot whose body says v7 is not supported through Drop-in, routes Drop-in users to v5, and carries dated 2026/2027 lifecycle and migration notices; not current support or payment-processing evidence
- [[source-braintree-credit-cards-client-side-ios-v7]] - website iOS v7 standard client-side guide to Card Fields setup, validity-driven merchant submission, nonce/error completion and server handoff
- [[source-braintree-authorization-tokenization-key-ios-v7]] - iOS v7 website guide to static, reduced-privilege tokenization-key authorization and its environment, lifecycle, capability, and historical certificate boundaries
- [[source-braintree-client-sdk-migration-ios-v7]] - website v6-to-v7 migration-guide snapshot for the native iOS SDK; not current package-support evidence
- [[source-braintree-client-sdk-setup-ios-v7]] - collected iOS v7 client-SDK setup guide for platform requirements, installation routing, app-return setup and location-permission configuration, with dated certificate and security notices
- [[source-braintree-client-sdk-deprecation-policy-ios-v7]] - historical iOS-routed website policy for relative OS support, client-SDK lifecycle categories and version-status lookup routes; not current v7 support evidence
- [[source-braintree-paypal-messaging-javascript-v3]] - snapshot route whose retained body states Pay Later Messaging availability for merchants using the latest native iOS and Android SDKs, requires native-app integration eligibility and excludes Drop-in

- [[source-github-braintree-ios]] - cumulative exact-SHA implementation evidence
- [[changelog-github-braintree-ios]] - package-qualified release ledger
- [[source-github-braintree-ios-drop-in]] - independently versioned prebuilt iOS Drop-in baseline
- [[changelog-github-braintree-ios-drop-in]] - package-qualified iOS Drop-in release ledger
- [[braintree-android-sdk]] - independently versioned native Android SDK
- [[braintree-web-sdk]] - independently versioned browser SDK
- [[paypal-braintree-integration]] - Braintree PayPal processing boundary
- [[recurring-payments]] - consent, storage, and later-charge requirements
- [[braintree]] - company page
