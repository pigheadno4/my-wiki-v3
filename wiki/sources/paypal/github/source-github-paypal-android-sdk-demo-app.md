---
title: "GitHub: paypal-examples/paypal-android-sdk-demo-app"
type: source
date_ingested: 2026-08-16
original_format: github-repo
raw_files:
  - "github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/manifest.json"
tags: [paypal, android, checkout, cards, payment-links, jetpack-compose, samples, github-repository]
---

## Overview

`paypal-examples/paypal-android-sdk-demo-app` is a Jetpack Compose checkout sample pinned to commit `d1137d5daa3a3befdcf6c72e6a1e8144bf765ba2`, committed on 2026-06-10. It contrasts direct PayPal Android SDK checkout for PayPal and cards with a separately launched PayPal-hosted Payment Link.

Repository: <https://github.com/paypal-examples/paypal-android-sdk-demo-app>

## Evidence Boundary

- The immutable capsule retains all 39 selected files totaling 80,026 bytes, with no policy exclusions.
- The sample depends on PayPal Android SDK `2.3.0`; it is an implementation example at this exact SHA, not current product-availability or merchant-eligibility authority.
- The direct PayPal path explicitly uses `PayPalWebCheckoutFundingSource.PAYPAL`. This repository does not demonstrate native Venmo checkout.
- The sample's public client ID and hosted demo server are example infrastructure. Production credentials, endpoints, order validation, capture verification, and fulfillment remain merchant responsibilities.

## Grounding Excerpts

> "Direct SDK integration offers a seamless in-app checkout using native components."
>
> `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/README.md:5-8`

> "This app makes server-side PayPal API calls via a merchant server that uses the PayPal Typescript Server SDK, which is in beta."
>
> `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/README.md:18-20`

> "No 3DS logic here: If a flow requires 3DS, it won't be handled."
>
> `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/app/src/main/java/com/firstapp/paypaldemo/cardcheckout/CardPaymentViewModel.kt:21-28`

> "NOTE: This is purely an example. Adapt it to match your real merchant server's endpoints."
>
> `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/app/src/main/java/com/firstapp/paypaldemo/service/DemoMerchantAPI.kt:12-18`

> "The final 'finish' must still happen in handleOnNewIntent => finishPayPalCheckout."
>
> `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/app/src/main/java/com/firstapp/paypaldemo/paypalcheckout/PayPalViewModel.kt:55-60`

## Direct PayPal Checkout

The app creates a `CAPTURE` order through its merchant server, constructs `PayPalWebCheckoutRequest` with the PayPal funding source, and starts `PayPalWebCheckoutClient`. A successful browser presentation is not payment completion: the app saves `instanceState`, waits for the return intent, calls `finishStart()`, and only then asks the merchant server to capture the returned order ID.

`SavedStateHandle` restores the SDK instance state after process loss. The UI handles both a new intent and lifecycle resume so a browser return can be processed after a warm return or cold start. `NoResult` returns the UI to a retryable idle state.

This flow demonstrates PayPal web checkout only. It does not expose Pay Later, PayPal Credit, or Venmo even though those capabilities may exist elsewhere in the independently versioned SDK or product documentation.

## Direct Card Checkout

The card path creates an order on the merchant server, constructs `CardRequest` with `SCA_WHEN_REQUIRED`, approves through `CardClient`, and captures through the merchant server after `CardApproveOrderResult.Success`.

> [!warning] Incomplete 3DS handling
> The request can require authentication, but the sample deliberately treats `AuthorizationRequired` as an error. A production integration must present and finish the 3DS challenge before capture; this sample is not a complete SCA implementation.

## Payment Link Checkout

The alternative path opens a hardcoded sandbox Payment Link in an Android Custom Tab. The app is registered for the demo server's verified HTTP/HTTPS App Link, handles both `onNewIntent` and lifecycle resume, and marks its UI complete when the returned URI has the expected host and a path containing `success`.

> [!warning] Return URI is not settlement evidence
> This sample does not retrieve or verify the Payment Link transaction before showing completion. A matching return host/path is navigation evidence only; merchants must verify payment state through trusted server-side records, APIs, or webhooks before fulfillment.

The Payment Link path is operationally separate from the direct SDK path: it does not create or capture the order through `DemoMerchantAPI`, and its link is pre-created rather than generated dynamically.

## Merchant-Server Boundary

The app sends purchase units to an example Heroku server to create and complete orders. The repository itself warns merchants to adapt these endpoints. Its fixed catalog values, public client ID, print logging, error handling, and hosted server must not be copied as production controls.

## Related

- Company: [[paypal]]
- Android SDK: [[paypal-android-sdk]]
- Checkout: [[paypal-checkout]]
- Payment Links: [[paypal-payment-links]]
- SDK source: [[source-github-paypal-android]]
- Repository history: [[changelog-github-paypal-android-sdk-demo-app]]

## Raw Sources

- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/manifest.json` - immutable exact-SHA baseline
- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/README.md` - sample scope, setup, and integration choices
- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/gradle/libs.versions.toml` - PayPal Android SDK `2.3.0` dependency
- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/app/src/main/java/com/firstapp/paypaldemo/paypalcheckout/PayPalViewModel.kt` - PayPal create, browser return, restore, and capture flow
- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/app/src/main/java/com/firstapp/paypaldemo/cardcheckout/CardPaymentViewModel.kt` - card approval, capture, and incomplete 3DS branch
- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/app/src/main/java/com/firstapp/paypaldemo/paymentlink/PayWithPaymentLinkViewModel.kt` - Payment Link return handling
- `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/2026-08-16-d1137d5/files/app/src/main/AndroidManifest.xml` - custom-scheme and verified App Link registration
