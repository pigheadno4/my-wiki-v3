---
title: "Braintree Android SDK"
type: concept
category: technology
tags: [braintree, android, mobile, kotlin, paypal, venmo, cards, 3d-secure]
---

## Braintree Android SDK

Braintree Android is a modular native SDK for accepting card and alternative payments in Android applications. Payment-specific clients create authorization requests, launch any required wallet, browser, or app-switch experience, and tokenize successful returns into Braintree payment-method nonces for server processing.

## Current Baseline

The first retained modular baseline is `braintree-android@5.30.0` at exact SHA `51f183a48557d0fd00eefa541712df0c4f21ee28`. It supports Android API 23+, Java 11, and Kotlin 1.9.10.

The source includes Card, PayPal, Venmo, Google Pay, Local Payment, SEPA, 3D Secure, Data Collector, Shopper Insights, PayPal Messaging, American Express, and UIComponents modules. Capability in source does not prove merchant or buyer eligibility.

## Redirect and Nonce Model

Redirect-capable modules use a request, launcher, and result pattern. The merchant application must preserve the pending payment request, handle the app-link or deep-link return, and then tokenize the successful result. The resulting nonce belongs to a Braintree server flow, not a direct PayPal Orders API integration.

## PayPal and Venmo Boundary

PayPal and Venmo are separate Braintree modules:

- PayPal supports checkout, vault, checkout-with-vault billing agreements, recurring-billing metadata, and optional PayPal app switch with browser fallback.
- Venmo supports the Venmo app or mobile browser, single-use and multi-use requests, and conditional vaulting with a customer-scoped client token.

Venmo is not a PayPal funding-source enum in this SDK. This Braintree Venmo path is also independent from `paypal/paypal-android@2.3.0`, which does not expose a native Venmo integration in its retained source.

## `5.31.0` PayPal App-Switch Device Context

Compared with the retained 5.30.0 baseline, `braintree-android@5.31.0` automatically adds device model and available/total memory to `app_switch_context.device_info` on the PayPal authorization request. This happens only after app-switch enablement survives installed-app/resolution checks and an app-link return URL exists. Memory values are integer conversions after division by 1024 squared. If ActivityManager is unavailable, the base request is returned unchanged.

This shared path serves checkout and vault authorization; it does not change nonce/server processing or guarantee that the PayPal server selects app switch. The new helper does not inspect hasUserLocationConsent; the existing separate DataCollector request still receives that flag. This code distinction is not a privacy/compliance conclusion. See [[source-github-braintree-android]].

> [!warning] Contradiction
> The 5.31.0 release notes report Browser Switch 3.6.0, while that exact snapshot's unchanged DEPENDENCIES.md lists 3.5.1. BraintreeCore/build.gradle uses the libs.browser.switch alias, but its version catalog is outside the capsule. The resolved version and dependency behavior are therefore not independently established. Both raw authorities are linked in [[source-github-braintree-android]]; no build or runtime test was performed.

## `5.32.0` Campaigns, Recommendations and Wallet Integration

`braintree-android@5.32.0` adds optional `PayPalCheckoutRequest.campaigns` (default empty), serialized as `paypal_campaigns` containing ID objects. Beta Shopper Insights v2 adds optional `CustomerSessionRequest.payPalCampaigns`, serialized as GraphQL `paypalCampaigns` for session create/update and recommendation generation with a request object. Empty lists are omitted. These inputs associate existing campaign IDs; they do not establish campaign provisioning, eligibility or a guaranteed offer.

Shopper Insights now checks a nonempty GraphQL `errors` array before reading `data` in session and recommendation parsers. It uses the first error's message, and existing API/client handling returns a Failure. `CustomerRecommendations.expiresAt` is an optional ISO-8601-documented string, not SDK-enforced expiration or automatic refreshing. Applications should handle failures and recommendation staleness separately; do not expose unsanitized upstream errors. The feature remains beta.

The vaulted Venmo nonce branch now reads `details.commonId` into `externalId` when present, fixing one previously empty-ID path. A later `payerInfo.externalId` assignment can overwrite it, so a nonempty ID is not guaranteed. Vault authorization requirements remain unchanged.

A new public `GooglePayLauncher(ActivityResultRegistry, LifecycleOwner, Context, callback)` constructor provides a Compose-compatible entry point without requiring the existing Fragment/Activity constructor. Its KDoc requires initialization before the owner's CREATED state and launch only once CREATED is reached. It is not a new composable payment button or proof of a tested Compose flow.

PayPal/Venmo client and button KDoc now specifies a bare deep-link fallback scheme matching AndroidManifest.xml, not a full URL; this delta does not add a runtime validator. See [[source-github-braintree-android]] and [[changelog-github-braintree-android]] for exact evidence and preserved 5.30.0/5.31.0 history, including the unresolved Browser Switch discrepancy. No SDK build or payment test was performed.

## `5.33.0` Compose Card Fields

`braintree-android@5.33.0` adds a Compose `CardFields` form for number, expiration and CVV, paired with `rememberCardFieldsController(authorization, request)`. The controller exposes isFormValid and submit(callback); submission copies the entered fields into the optional Card request, calls CardClient.tokenize and returns CardFieldsResult.Success with a nonce or Failure. Merchant server processing is still required; this is not a transaction, 3DS challenge or Drop-in replacement.

The application owns its submit button and should gate it with isFormValid: controller.submit itself does not guard against invalid fields or duplicate submission. Input sanitization, brand-aware lengths, focus advancement and blur-based validation share the existing card-field validation model. Display formatting is separate from raw card values; CVV digits are masked with a 1.5-second reveal of a newly typed digit.

The controller uses rememberSaveable/TextFieldValue.Saver for number, expiration and CVV and restores ViewModel validation state. These source-level mechanics are not proof of secure storage, compliance, successful process restoration or sensitive-data clearing; submit contains no field-clearing step. Multiple forms within the same default ViewModel owner are not shown to be isolated by this helper. Before deployment, inspect host saved-state/lifecycle handling rather than treat masking as protection of underlying data. See [[source-github-braintree-android]] and [[changelog-github-braintree-android]]. No Android build, UI or payment test was performed; older evidence and unresolved dependency gaps remain intact.

## Drop-in Boundary

Website customization guidance warns against enabling Vault Manager for recurring-billing integrations because customers could delete payment methods associated with subscriptions. This is a Drop-in configuration warning, not evidence of subscription cancellation behavior or exact package compatibility. [[source-braintree-drop-in-customization-android-v5]]

`drop-in@6.17.0` is a separately versioned prebuilt UI pinned to Braintree Android `4.50.0`, not the retained modular `5.30.0` source. It presents eligible cards, PayPal, Venmo, and Google Pay and returns a nonce plus device data for server processing.

At this Drop-in baseline, PayPal defaults to vaulting, Venmo defaults to single use, and Venmo visibility requires remote enablement plus an available Venmo app switch. Saved-method retrieval and deletion require a customer-scoped client token. These statements must not be replaced with newer modular-SDK behavior without a compatible Drop-in release.

## Version Boundary

Release `5.30.0` makes the principal Kotlin suspend functions public, removes the unsupported Visa Checkout module, deprecates its remaining configuration fields, targets Android API 37 for compilation, and fixes PayPal/Venmo button sizing. Historical migration and removal notes remain context until their exact versions are separately retained.

## Related

- [[source-braintree-docs-guides-google-pay-configuration-android-v5]] - 2026-09-16 Android v5-routed website configuration guide for environment-specific Control Panel enablement, merchant-account activation routing, separate Google production work and PayPal-via-Google-Pay dual enablement; preserves a dated mobile-certificate warning and is not exact-package, current account/eligibility, client/server lifecycle or payment-execution proof

- [[source-braintree-docs-guides-google-pay-testing-go-live-android-v5]] - 2026-09-16 Android v5-routed Google Pay testing/go-live snapshot for sandbox nonce behavior, production Control Panel enablement and Google's separate production-access/app-review route; preserves a dated mobile-certificate warning and is not current eligibility, enablement, exact package/runtime, review-approval or payment-execution proof

- [[source-braintree-docs-guides-paypal-checkout-with-vault-android-v5]] - 2026-09-16 Android v5-routed website guide for one checkout that both charges and requests Billing Agreement consent for future merchant-initiated payments, with optional recurring detail fields and documented exclusions; not current exact-package support, eligibility, enablement, runtime or payment-execution proof

- [[source-braintree-docs-guides-shopper-insights-android-v5]] - 2026-09-16 Android v5-routed Shopper Insights beta guide for customer-session creation/update and consent-conditioned PayPal-or-Venmo recommendation retrieval, required Client Token initialization, recommendation presentment and presented/selected event calls; preserves the captured mobile-certificate warning and is not current availability, customer-eligibility, recommendation, event-receipt or payment-execution proof

- [[source-braintree-docs-guides-unionpay-client-side-android-v5]] - 2026-09-16 Android v5-routed website guide for UnionPay card-capability checks, client-token authorization, conditional SMS enrollment and tokenization; preserves post-enrollment field immutability and validation conditions, and is not current environment, certificate, package-support, eligibility or payment-execution proof

- [[source-braintree-docs-guides-google-pay-client-side-android-v5]] - 2026-09-16 Android v5-routed website guide for Google Pay readiness gating, authorization-request launch and callback tokenization into a nonce; preserves a request-versus-result tokenization wording mismatch and dated mobile-certificate warning, and is not current package-support, merchant/device eligibility, server-transaction, or payment-execution proof

- [[source-braintree-docs-guides-paypal-messaging-android-v5]] - 2026-09-16 Android v5-routed website guide for eligible merchants adding Pay Later offer messaging with request/view rendering and optional lifecycle callbacks; excludes Drop-in and preserves internal constructor/callback naming conflicts; not current package-support, merchant-eligibility, offer-availability, credit-approval or payment-execution evidence

- [[source-braintree-docs-guides-paypal-pay-later-offers-android-v5]] - 2026-09-16 Android v5-routed website guide for requesting Pay Later presentation with `PayPalCheckoutRequest.shouldOfferPayLater`, subject to buyer and merchant eligibility and a prohibition on extra promotional messaging; not current package-support, offer-availability, or payment-execution proof

- [[source-braintree-docs-guides-paypal-client-side-android-v5]] - 2026-09-16 Android v5-routed website guide for PayPal account/return-routing prerequisites, direct client initialization, and SDK-managed XML or Compose button tokenization into a nonce; includes a dated mobile-certificate warning and is not current package-support, eligibility, or payment-execution proof

- [[source-braintree-docs-guides-paypal-testing-go-live-android-v5]] - 2026-09-16 Android v5-routed Braintree PayPal testing/go-live snapshot for mocked versus linked sandbox testing, eligibility-conditioned app-switch fallback, sandbox/production isolation, server credential transition and limited real-payment production checks; not current eligibility, SDK/runtime behavior, linked-account state or execution/settlement/deposit proof

- [[source-braintree-docs-guides-paypal-recurring-payments-android-v5]] - 2026-09-16 Android v5-routed website guide for constructing a PayPal recurring Billing Agreement request with plan metadata and routing its token to later Braintree server payment operations; not current package-support, direct PayPal or transaction-outcome evidence

- [[source-braintree-docs-guides-venmo-client-side-android-v5]] - 2026-09-16 Android v5 website guide for SDK-managed buttons and custom Venmo request/launch/return/tokenization, with usage-scoped consent and vaulting, order-summary compliance, device-data and server-handoff conditions; not current SDK support or payment-execution proof

- [[source-braintree-docs-guides-paypal-checkout-with-paypal-android-v5]] - 2026-09-16 Android v5 website guide for PayPal one-time checkout request, launch, activity-return handling, tokenization and eligibility-conditioned app-switch browser fallback; nonce receipt is a client handoff, not current package-support or transaction-lifecycle proof
- [[source-braintree-premium-fraud-management-tools-client-side-android-v5]] - Android v5-routed Data Collector guide for device-data collection, server-request handoff, consent and location-disclosure responsibility, plus a historical mobile-certificate notice; not current package-support or named fraud-product evidence
- [[source-braintree-3d-secure-advanced-options-android-v5]] - Android v5-routed advanced 3DS webpage snapshot for client liability-result handling and specialized verification options; its embedded Drop-in lifecycle notice is not modular SDK package-compatibility evidence
- [[source-braintree-drop-in-customization-android-v5]] - Android v5-routed Drop-in customization guide for saved-method, Vault Manager, card-form, and fraud-tool configuration; source-specific lifecycle and package-version boundaries apply
- [[source-braintree-drop-in-setup-and-integration-android-v5]] - Android v5-routed Drop-in setup snapshot for client authorization, method-specific prerequisites, customer-scoped saved-method lookup, browser-switch overrides, and its source-specific 2026/2027 lifecycle notice; not proof of modular v5 package compatibility or current support

- [[source-braintree-credit-cards-client-side-android-v5]] - Android v5 website guide to standard Card Fields UI ownership, SDK 5.29.0-or-higher `ui-components` prerequisite, client authorization, tokenization and nonce handoff; not current package-support or execution evidence
- [[source-braintree-authorization-tokenization-key-android-v5]] - historical Android v5 client-authorization guide for static reduced-privilege tokenization keys, their lifecycle, environment binding, and capability limits; not current SDK-support evidence
- [[source-braintree-client-sdk-setup-android-v5]] - historical Android client SDK v5 setup snapshot for captured environment requirements, modular dependencies, return routing, authorization choices, and the dated mobile-certificate warning; not current package support
- [[source-braintree-client-sdk-migration-android-v5]] - historical website guide for migrating Braintree Android SDK v4 integrations to v5; not current package-support evidence
- [[source-braintree-client-sdk-deprecation-policy-android-v5]] - historical website-policy snapshot for Android client-SDK semantic versioning, release-time platform support, and status/deprecation-date lookup; current package support remains under separate GitHub evidence
- [[source-braintree-paypal-messaging-javascript-v3]] - snapshot route whose retained body states Pay Later Messaging availability for merchants using the latest native iOS and Android SDKs, requires native-app integration eligibility and excludes Drop-in

- [[source-github-braintree-android]] - cumulative exact-SHA implementation evidence
- [[changelog-github-braintree-android]] - package-qualified release ledger
- [[source-github-braintree-android-drop-in]] - independently versioned prebuilt Android Drop-in baseline
- [[changelog-github-braintree-android-drop-in]] - package-qualified Android Drop-in release ledger
- [[braintree-web-sdk]] - independently versioned browser SDK
- [[braintree-web-drop-in]] - independently versioned prebuilt browser UI
- [[paypal-android-sdk]] - standalone PayPal Android SDK and Venmo contradiction boundary
- [[braintree]] - company page
