---
title: "GitHub: paypal-examples/paypal-ios-sdk-demo-app"
type: source
date_ingested: 2026-08-16
original_format: github-repo
raw_files:
  - "github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/manifest.json"
tags: [paypal, ios, checkout, cards, payment-links, swiftui, samples, github-repository]
---

## Overview

`paypal-examples/paypal-ios-sdk-demo-app` is a SwiftUI checkout sample pinned to commit `047a50ec97d9881af84ca3fb03d1d23e859a86f4`, committed on 2025-07-28. It contrasts direct PayPal iOS SDK checkout for PayPal and cards with a separately launched PayPal-hosted Payment Link.

Repository: <https://github.com/paypal-examples/paypal-ios-sdk-demo-app>

## Evidence Boundary

- The immutable capsule retains all 25 selected files totaling 84,280 bytes, with no policy exclusions.
- The Xcode project accepts PayPal iOS SDK versions from `2.0.0` up to, but not including, `3.0.0`. No retained lockfile identifies the exact resolved patch version.
- The direct PayPal path explicitly uses funding source `.paypal`; it does not demonstrate native Venmo checkout.
- The public client ID, hosted demo server, fixed sandbox Payment Link, sample card values, and return handler are example infrastructure rather than production controls.
- Repository behavior is version-specific implementation evidence. Current availability, merchant eligibility, and App Store policy require separate verification.

## Grounding Excerpts

> "Its primary purpose is to demonstrate two integration options to accept payments in iOS Apps through PayPal:"
>
> `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/README.md:3-7`

> "This is required for order fulfillment and reconciliation."
>
> `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/README.md:55-57`

> "This function replicates a way a merchant may go about creating an order on their server and is not part of the SDK flow."
>
> `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/PayPalDemo/Networking/DemoMerchantAPI.swift:16-20`

> "After completion, app is notified via webhook callback"
>
> `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/README.md:215-217`

## Direct PayPal Checkout

The app asks its merchant server to create an order, initializes `PayPalWebCheckoutClient`, and starts an async `PayPalWebCheckoutRequest` with funding source `.paypal`. It collects device data before checkout and sends the resulting `PayPal-Client-Metadata-Id` to the merchant server when completing the order. Cancellation is distinguished with `PayPalError.isCheckoutCanceled`.

The merchant server still owns order creation and the final `CAPTURE` or `AUTHORIZE` call. The app contains no PayPal API secret. This flow does not expose Venmo, Pay Later, PayPal Credit, subscriptions, or vaulting.

## Direct Card Checkout

The card path creates an order through the merchant server, uses `CardRequest` with `.scaWhenRequired`, awaits `CardClient.approveOrder`, records whether 3DS was attempted, and then completes the order through the merchant server with device data.

Unlike the independently collected Android demo, this sample does not deliberately reject a 3DS-required result. Its async SDK approval flow is therefore the stronger 3DS reference of the two samples, but the repository still does not demonstrate production liability-shift decisions or server-side payment verification.

> [!warning] Retained card-form defect
> The CVV field observes changes to `cardNumber` and calls `updateCardNumber` instead of validating CVV. The form also starts with sandbox card data. Production integrations must replace this sample UI and avoid embedding test payment credentials.

## Payment Link and Universal Link

The alternative path opens a hardcoded sandbox Payment Link with `UIApplication.shared.open`. The app registers the demo server as an associated domain and forwards `onOpenURL` to `CheckoutCoordinator.handleReturnURL`.

The return handler checks only that the path equals `/success`, reads the `amt` query parameter, and then displays completion. It does not validate the host, transaction ID, status, PDT response, webhook, or trusted server-side payment state.

> [!warning] Return URL is not settlement evidence
> The iOS return handler is weaker than the Android sample because it does not even check the expected host. Production apps must bind the return to their own verified domain and confirm the payment through trusted server-side records, APIs, PDT validation, or webhooks before fulfillment.

## Documentation and Build Gaps

- The README says the demo supports one-time and recurring payments, but the retained Swift code implements no subscription creation, approval, activation, or lifecycle handling. Its recurring section describes shareable PayPal Subscriptions plan links rather than an in-app subscription implementation.
- The README says the app is notified through a webhook callback, but the retained app implements only `onOpenURL`; no webhook consumer or merchant-server webhook code is present.
- The README lists iOS 15+, while the Xcode project sets the deployment target to iOS 17.2.
- The Xcode project repeats the same `CheckoutFlow.swift` build-file entry four times in the Sources phase.
- Broad README language about in-app purchases does not establish App Store policy compliance. See [[source-paypal-ios-in-app-purchases]] and verify current Apple rules for the app, region, and goods type.

## Related

- Company: [[paypal]]
- iOS SDK: [[paypal-ios-sdk]]
- Checkout: [[paypal-checkout]]
- Payment Links: [[paypal-payment-links]]
- SDK source: [[source-github-paypal-ios]]
- Repository history: [[changelog-github-paypal-ios-sdk-demo-app]]
- Android counterpart: [[source-github-paypal-android-sdk-demo-app]]

## Raw Sources

- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/manifest.json` - immutable exact-SHA baseline
- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/README.md` - scope, setup, Payment Link, PDT, and webhook claims
- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/PayPalDemo/ViewModels/PayPalViewModel.swift` - PayPal approval, device data, cancellation, and completion
- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/PayPalDemo/ViewModels/CardPaymentViewModel.swift` - card approval, 3DS-attempt state, and completion
- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/PayPalDemo/CheckoutCoordinator.swift` - Payment Link launch and return handling
- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/PayPalDemo/Networking/DemoMerchantAPI.swift` - merchant-server boundary
- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/paypal-ios-sdk-demo-app.xcodeproj/project.pbxproj` - SDK range, deployment target, and build entries
