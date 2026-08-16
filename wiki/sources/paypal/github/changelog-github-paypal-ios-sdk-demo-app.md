---
title: "GitHub changelog: paypal-examples/paypal-ios-sdk-demo-app"
type: source
date_ingested: 2026-08-16
original_format: github-repo
raw_files:
  - "github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/manifest.json"
tags: [paypal, ios, checkout, payment-links, samples, changelog, github-repository]
---

## Overview

Commit-qualified history for `paypal-examples/paypal-ios-sdk-demo-app`. Durable integration findings belong in [[source-github-paypal-ios-sdk-demo-app]].

## `default-branch@047a50e` - Full Baseline (2025-07-28)

| Ref | Prior reviewed SHA | Current SHA | Ingest mode |
| --- | --- | --- | --- |
| `main` | Baseline | `047a50ec97d9881af84ca3fb03d1d23e859a86f4` | Full |

The accepted 2026-08-16 capsule retains all 25 selected files totaling 84,280 bytes. This is the first managed baseline, so no prior commit comparison exists.

### Baseline scope

- SwiftUI cart and checkout UI using PayPal iOS SDK `>=2.0.0,<3.0.0`; the exact resolved patch is not retained.
- Direct PayPal web checkout with cancellation handling, device-data collection, and merchant-server completion.
- Direct card approval with SCA when required, 3DS-attempt reporting, and merchant-server completion.
- Separate hosted Payment Link launch and Universal Link return.
- README guidance for one-time links, PayPal Subscriptions plan links, PDT, and webhooks.

### Retained limitations

- No native Venmo flow; the direct request uses only `.paypal`.
- No implemented recurring-payment or webhook callback flow despite README claims.
- Payment Link completion trusts only `/success` and `amt`; it does not validate host or payment state.
- README iOS 15+ support conflicts with the Xcode project's iOS 17.2 deployment target.
- The card form miswires CVV change handling and includes sandbox card defaults.
- Broad in-app-purchase language is not App Store policy authority.

### Evidence and updated wiki areas

**Updated wiki areas:** cumulative repository source; PayPal iOS SDK; PayPal Checkout; Payment Links; PayPal company and provider index.

**Evidence:**

- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/manifest.json`
- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/README.md`
- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/PayPalDemo/ViewModels/PayPalViewModel.swift`
- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/PayPalDemo/ViewModels/CardPaymentViewModel.swift`
- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/PayPalDemo/CheckoutCoordinator.swift`
- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/PayPalDemo/Networking/DemoMerchantAPI.swift`
- `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/2026-08-16-047a50e/files/paypal-ios-sdk-demo-app.xcodeproj/project.pbxproj`
