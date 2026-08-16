---
title: "GitHub changelog: paypal-examples/paypal-android-sdk-demo-app"
type: source
date_ingested: 2026-08-16
original_format: github-repo
raw_files:
  - "github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/manifest.json"
tags: [paypal, android, checkout, payment-links, samples, changelog, github-repository]
---

## Overview

Commit-qualified history for `paypal-examples/paypal-android-sdk-demo-app`. Durable integration findings belong in [[source-github-paypal-android-sdk-demo-app]].

## `default-branch@d1137d5` - Full Baseline (2026-06-10)

| Ref | Prior reviewed SHA | Current SHA | Ingest mode |
| --- | --- | --- | --- |
| `main` | Baseline | `d1137d5daa3a3befdcf6c72e6a1e8144bf765ba2` | Full |

The accepted 2026-08-16 capsule retains all 39 selected files totaling 80,026 bytes. This is the first managed baseline, so no prior commit comparison exists.

### Baseline scope

- Jetpack Compose cart and checkout UI using PayPal Android SDK `2.3.0`.
- Direct PayPal web checkout with SDK state restoration, browser-return finishing, and merchant-server capture.
- Direct card approval followed by merchant-server capture.
- Separate hosted Payment Link launch through a Custom Tab and verified App Link return.
- Example merchant-server create and complete calls.

### Retained limitations

- No native Venmo flow; the direct request uses only the PayPal funding source.
- Card `AuthorizationRequired` is rejected, so the sample does not complete 3DS.
- Payment Link completion trusts a return host/path and does not verify payment state before updating the UI.
- The hosted demo server, fixed sandbox Payment Link, public client ID, and debug setup are example infrastructure rather than production controls.

### Evidence and updated wiki areas

**Updated wiki areas:** cumulative repository source; PayPal Android SDK; PayPal Checkout; Payment Links; PayPal company and provider index.

**Evidence:**

- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/manifest.json`
- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/README.md`
- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/gradle/libs.versions.toml`
- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/app/src/main/java/com/firstapp/paypaldemo/paypalcheckout/PayPalViewModel.kt`
- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/app/src/main/java/com/firstapp/paypaldemo/cardcheckout/CardPaymentViewModel.kt`
- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/app/src/main/java/com/firstapp/paypaldemo/paymentlink/PayWithPaymentLinkViewModel.kt`
