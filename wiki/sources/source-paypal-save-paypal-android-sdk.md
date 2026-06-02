---
title: "Save PayPal with the Android SDK"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-paypal-android-sdk.md"
tags: [paypal, android, mobile, vault, save-payment-methods, kotlin, payment-tokens, orders-api, web-checkout]
---

## Overview

Integration guide for saving PayPal Wallets during purchase in Android apps using the PayPal Android SDK. Uses `PayPalWebCheckoutClient` (browser-based web checkout) rather than `CardClient`.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/android-sdk/paypal/>

Last updated: 2025-03-06

## Key Takeaways

### Availability

Same 35 countries as all other PayPal Wallet vault integrations.

### Flow

1. Create order server-side with `payment_source.paypal.attributes.vault.store_in_vault: ON_SUCCESS`
2. Send `orderId` to Android SDK
3. `PayPalWebCheckoutClient.start(PayPalWebRequest(orderId))` — launches browser-based PayPal Web Checkout
4. Payer approves in browser, returns via deep link (`deepLinkUrlScheme`)
5. Capture/authorize order server-side → response contains `vault.id` + `customer.id`
6. Store both in your database; use `vault.id` as payment source for returning payers

### SDK setup

```kotlin
val coreConfig = CoreConfig("CLIENT_ID")
val deepLinkUrlScheme = "com.myapplication.android"
val payPalWebClient = PayPalWebClient(activity, coreConfig, deepLinkUrlScheme)

payPalWebCheckoutClient.listener = object : PayPalWebCheckoutListener {
    override fun onPayPalWebSuccess(result: PayPalWebCheckoutResult) {
        // Capture or authorize on server
    }
    override fun onPayPalWebFailure(error: PayPalSDKError) { }
    override fun onPayPalWebCanceled() { }
}

val request = PayPalWebRequest(orderId = "ORDER_ID")
payPalWebCheckoutClient.start(request)
```

### PayPal button (Compose)

```kotlin
AndroidView(
    factory = { context ->
        PayPalButton(context).apply {
            setOnClickListener {
                // Create order server-side, then call start()
            }
        }
    }
)
```

### Create Order payload

```json
{
  "payment_source": {
    "paypal": {
      "attributes": {
        "vault": {
          "store_in_vault": "ON_SUCCESS",
          "usage_type": "MERCHANT",
          "customer_type": "CONSUMER"
        }
      }
    }
  }
}
```

Identical to JS SDK PayPal vault payload. No `experience_context` shown in this guide.

### Returning payer

Use saved `vault.id` as payment source in subsequent Create Order calls — no `customer.id` passing in the order body (unlike cards where `customer.id` goes in `payment_source.card.attributes.customer`).

### APPROVED vs VAULTED

Same pattern as all other integrations — subscribe to `VAULT.PAYMENT-TOKEN.CREATED` webhook if `vault.status: APPROVED`.

### Key difference vs Android card vault

| | Cards (Android SDK) | PayPal Wallet (Android SDK) |
| --- | --- | --- |
| Client class | `CardClient` | `PayPalWebClient` |
| Listener | `ApproveOrderListener` | `PayPalWebCheckoutListener` |
| Checkout UX | Inline card fields | Browser-based Web Checkout |
| Deep link required | Yes (3DS return) | Yes (PayPal return) |
| Returning payer | `customer.id` in Create Order body | `vault.id` as payment source |

> [!warning] PayPal's own guidance
> Same as JS SDK — page warns "Don't save PayPal as a payment method during purchase" while being a guide for doing exactly that. Likely nudging toward save-without-purchase for better UX.

## Raw Sources

- [[paypal-save-paypal-android-sdk]] — verbatim integration guide

## Relevant Wiki Pages

- [[paypal-android-sdk]] — Android SDK overview (modules, CoreConfig, PayPalWebCheckoutClient)
- [[paypal-vault]] — Vault concept: token types, APPROVED/VAULTED, webhook
- [[source-paypal-save-cards-android-sdk]] — Card vault Android SDK (same SDK, different client class)
- [[source-paypal-save-paypal-js-sdk]] — JS SDK equivalent for saving PayPal Wallet
