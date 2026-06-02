---
title: "GitHub: paypal/paypal-android"
type: source
date_ingested: 2026-04-13
original_format: github-repo
raw_files:
  - "github-paypal-android.md"
tags: [paypal, android, mobile, kotlin, card-payments, web-payments, fraud-protection, payment-buttons, maven, orders-api, 3d-secure]
---

## GitHub: paypal/paypal-android

Source code for the PayPal Mobile Android SDK — Kotlin modules for card, PayPal web, fraud protection, and payment button integrations.

Repo URL: <https://github.com/paypal/paypal-android>

Commit SHA: `2685f88374fa09c17e5af6f3ea88ba622d940901` | Reviewed: 2026-04-13

## Key Takeaways from Source

### `CardClient` constructor — takes `Context` (not just `CoreConfig`)

The doc shows `CardClient(config)` but the actual constructor is:

```kotlin
CardClient(context: Context, configuration: CoreConfig)
```

The `Context` is used internally for analytics and the `DataVaultPaymentMethodTokensAPI`.

### `CardClient` has instance state management

```kotlin
val instanceState: String  // serialise to Base64 JSON for process kill recovery
fun restore(instanceState: String)  // restore from saved state
```

This is important for apps that need to survive process death during the 3DS browser flow.

### `PayPalWebCheckoutFundingSource` — only 3 values (not 4)

The actual enum in source has **3 values** (not 4 as the docs imply):

| Value | Effect |
| ----- | ------ |
| `PAYPAL` | Standard PayPal one-time checkout |
| `PAY_LATER` | Shows Pay Later offers to eligible customers |
| `PAYPAL_CREDIT` | Shows PayPal Credit revolving line to eligible customers |

> [!warning] Contradiction
> The official docs reference Venmo as a funding source for `PayPalWebPayments`, but `PayPalWebCheckoutFundingSource` in source has no `VENMO` value. Venmo may be handled separately or only available in `Venmo` module.

### Demo ViewModels — complete integration patterns

`ApproveOrderViewModel.kt` (232 lines) shows the full card payment flow:
1. Create order via `CreateOrderUseCase` (server call)
2. Build `Card` + `CardRequest`
3. Call `cardClient.approveOrder(activity, cardRequest)`
4. Handle `ApproveOrderListener` callbacks
5. On success: call `CompleteOrderUseCase` (capture/authorize)

`PayPalWebViewModel.kt` (160 lines) shows the full web payment flow:
1. Create order
2. Build `PayPalWebCheckoutRequest(orderID, fundingSource)`
3. Call `payPalWebCheckoutClient.start(request)`
4. On `onPayPalWebSuccess`: call `CompleteOrderUseCase`

### `SDKSampleServerAPI.kt` — server endpoint contract

All REST calls the demo app makes to the merchant server:
- `POST /orders` — create order
- `POST /orders/{id}/capture` — capture
- `POST /orders/{id}/authorize` — authorize
- Vault flows: create setup token, create payment token, get payment token

### Migration guides

- `MOBILE_CHECKOUT_MIGRATION_GUIDE.md` — migrate from deprecated `PayPalNativePayments` to `PayPalWebPayments`
- `v2_MIGRATION_GUIDE.md` — v1 → v2 breaking changes

## Files Saved

See stub file for full path list and per-file descriptions: [[github-paypal-android]]

## Raw Sources

- [[github-paypal-android]] — stub file with repo metadata and file navigation table
- Detail directory: `raw/github-paypal-android/`

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-android-sdk]] — PayPal Android SDK concept page
- [[source-paypal-android-card-payments]] — official integration guide (docs layer above this source)
