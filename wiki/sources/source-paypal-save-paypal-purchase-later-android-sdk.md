---
title: "Save PayPal for Purchase Later with the Android SDK"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-paypal-purchase-later-android-sdk.md"
tags: [paypal, android, mobile, vault, save-payment-methods, kotlin, setup-token, payment-tokens, purchase-later, web-payments]
---

## Overview

Integration guide for saving PayPal Wallets **without a purchase transaction** in Android apps using the PayPal Android SDK. Uses `PayPalWebCheckoutClient.vault()` with a `PayPalWebVaultRequest`.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/android-sdk/paypal/>

Last updated: 2025-02-27

## Key Takeaways

### Availability

35 countries — same as all other PayPal Wallet vault integrations.

### Module

`paypal-web-payments` (not `card-payments`):

```groovy
// Groovy
implementation 'com.paypal.android:paypal-web-payments:<CURRENT-VERSION>'
```

### Flow

1. Server: `POST /v3/vault/setup-tokens` with `payment_source.paypal` + `experience_context`
   - Response status: `PAYER_ACTION_REQUIRED` (unlike cards which return `CREATED`)
2. Client: `PayPalWebVaultRequest(setupTokenResponse.setupTokenId)`
3. `PayPalWebCheckoutClient.vault(vaultRequest)` — same client as web payments, vault-specific method
4. `vaultListener` callbacks fire: `onPayPalWebVaultSuccess/Failure/Canceled`
5. Server: `POST /v3/vault/payment-tokens` with setup token → payment token + `customer.id`
6. Store both for future charges

### Client-side SDK

```kotlin
val coreConfig = CoreConfig(CLIENT_ID)
val vaultRequest = PayPalWebVaultRequest(setupTokenResponse.setupTokenId)

val paypalClient = PayPalWebCheckoutClient(activity, coreConfig, URL_SCHEME)
paypalClient.vaultListener = this
paypalClient.vault(vaultRequest)

override fun onPayPalWebVaultSuccess(result: PayPalWebVaultResult) { }
override fun onPayPalWebVaultFailure(error: PayPalSDKError) { }
override fun onPayPalWebVaultCanceled() { }
```

### Setup token request

```json
{
  "payment_source": {
    "paypal": {
      "usage_type": "PLATFORM",
      "experience_context": {
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      }
    }
  }
}
```

> [!warning] `usage_type` difference
> This guide uses `usage_type: PLATFORM` — the during-purchase Android PayPal vault guide uses `usage_type: MERCHANT`. The JS SDK purchase-later PayPal guide also uses `usage_type: MERCHANT`. This discrepancy may be intentional (platform-facilitated payments vs direct merchant) or a doc inconsistency — verify before deploying.

### Key differences vs Android PayPal during-purchase vault

| | During purchase | Purchase later |
| --- | --- | --- |
| SDK method | `PayPalWebCheckoutClient.start()` | `PayPalWebCheckoutClient.vault()` |
| Request object | `PayPalWebRequest(orderId)` | `PayPalWebVaultRequest(setupTokenId)` |
| Listener | `PayPalWebCheckoutListener` | `vaultListener` (`onPayPalWebVaultSuccess/Failure/Canceled`) |
| Vault API | Orders API `store_in_vault: ON_SUCCESS` | Setup token → payment token |
| `usage_type` | `MERCHANT` | `PLATFORM` |
| Setup token status | N/A | `PAYER_ACTION_REQUIRED` |

### Key differences vs Android cards purchase-later vault

| | Cards | PayPal |
| --- | --- | --- |
| Module | `card-payments` | `paypal-web-payments` |
| Client | `CardClient` | `PayPalWebCheckoutClient` |
| Method | `vault()` | `vault()` |
| Request | `CardVaultRequest` | `PayPalWebVaultRequest` |
| Listener | `CardVaultListener` | `vaultListener` |
| Setup token status | `CREATED` | `PAYER_ACTION_REQUIRED` |
| Returning customer in setup token | Yes (`customer.id` in body) | No |

## Raw Sources

- [[paypal-save-paypal-purchase-later-android-sdk]] — verbatim integration guide

## Relevant Wiki Pages

- [[paypal-android-sdk]] — Android SDK overview (modules, CoreConfig, PayPalWebCheckoutClient)
- [[paypal-vault]] — Vault concept: setup token → payment token flow
- [[source-paypal-save-paypal-android-sdk]] — PayPal during-purchase Android vault (`start()` not `vault()`)
- [[source-paypal-save-cards-purchase-later-android-sdk]] — Cards purchase-later Android vault (CardClient equivalent)
