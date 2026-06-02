---
title: "PayPal Android SDK: Integrate Card Payments"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-android-card-payments.md"
tags: [paypal, android, mobile, card-payments, kotlin, 3d-secure, sca, native-payments, web-payments, fraud-protection, maven, orders-api]
---

## PayPal Android SDK: Integrate Card Payments

Official integration guide for accepting PayPal, credit, and debit card payments in Android apps using the PayPal Mobile Android SDK.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/android/>

Last updated: 2025-07-31

## Key Takeaways

### Three payment modules (Kotlin)

| Module | Gradle artifact | Status | Notes |
| ------ | --------------- | ------ | ----- |
| `card-payments` | `com.paypal.android:card-payments` | Active | Inline card fields in your UI |
| `paypal-native-payments` | `com.paypal.android:paypal-native-payments` | **Deprecated** (July 2024, EOL July 2025) | Migrate to `paypal-web-payments` |
| `paypal-web-payments` | `com.paypal.android:paypal-web-payments` | Active | Browser-based checkout inside app |

Plus: `payment-buttons` (PayPal-branded buttons) and `fraud-protection` (device fingerprinting).

### Card Payments flow (8 steps)

1. Add `card-payments` dependency
2. Create `CardClient(CoreConfig("CLIENT_ID", Environment.SANDBOX))`
3. Server creates order via Orders v2 API → returns `ORDER_ID`
4. Build `Card(number, expirationMonth, expirationYear, securityCode, billingAddress)` object
5. Build `CardRequest(orderID, card, returnUrl = "myapp://return_url", sca = SCA.SCA_ALWAYS)`
6. Register `myapp://` scheme in `AndroidManifest.xml` with `launchMode="singleTop"` + `onNewIntent`
7. Call `cardClient.approveOrder(activity, cardRequest)` → implement `ApproveOrderListener`
8. On `onApproveOrderSuccess` → server calls `POST /v2/checkout/orders/ORDER_ID/capture` or `/authorize`

### SCA parameter on `CardRequest`

| Value | Behaviour |
| ----- | --------- |
| `SCA.SCA_WHEN_REQUIRED` (default) | 3DS challenge only when required |
| `SCA.SCA_ALWAYS` | 3DS challenge on every transaction |

### `ApproveOrderListener` callbacks

- `onApproveOrderSuccess(result: CardResult)` — ready to capture/authorize
- `onApproveOrderFailure(error: PayPalSDKError)` — inspect error
- `onApproveOrderCanceled()` — 3DS flow canceled
- `onApproveOrderThreeDSecureWillLaunch()` — 3DS about to launch
- `onApproveOrderThreeDSecureDidFinish()` — 3DS completed

### Web Payments flow (recommended for PayPal buttons)

```kotlin
val payPalWebCheckoutClient = PayPalWebCheckoutClient(activity, config, returnUrl)
val request = PayPalWebCheckoutRequest("ORDER_ID",
    fundingSource = PayPalWebCheckoutFundingSource.PAYPAL) // PAYPAL, PAY_LATER, PAYPAL_CREDIT
payPalWebCheckoutClient.start(request)
```

Implements `PayPalWebCheckoutListener` with `onPayPalWebSuccess`, `onPayPalWebFailure`, `onPayPalWebCanceled`.

### Native Payments — migration warning

`PayPalNativePayments` requires Cardinal Commerce Maven repo with hardcoded credentials in build.gradle. **Deprecated July 2024, EOL July 2025** — do not use for new integrations.

### Fraud Protection

`PayPalDataCollector.collectDeviceData()` — collect before starting payment, pass `clientMetadataId` to server. Set `hasUserLocationConsent = true` only if user has granted location permission per Google Play policies. Do not cache or store the result.

### Billing address reduces 3DS challenges

Passing `billingAddress` in the `Card` object can reduce the number of authentication challenges the buyer faces.

### AndroidManifest.xml requirements

Both Card Payments and Web Payments require:
- `android:launchMode="singleTop"`
- Intent filter with `android:scheme="myapp"` (or your custom scheme)
- `android:exported="true"` (required for API 31 / Android 12+)
- `onNewIntent` override in the activity

## Images

- `raw/assets/paypal-android-native-checkout-first-time-01.png` — deprecated Native Checkout first-time flow (screen 1)
- `raw/assets/paypal-android-native-checkout-first-time-02.png` — deprecated Native Checkout first-time flow (screen 2)
- `raw/assets/paypal-android-native-checkout-returning.png` — deprecated Native Checkout returning customer flow

## Raw Sources

- [[paypal-android-card-payments]] — verbatim webpage content + downloaded images

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout (web equivalent — CardFields)
- [[source-paypal-expanded-checkout-integrate]] — Web CardFields integration (parallel to this Android guide)
