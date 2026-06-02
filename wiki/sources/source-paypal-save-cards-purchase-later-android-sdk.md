---
title: "Save Cards for Purchase Later with the Android SDK"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-cards-purchase-later-android-sdk.md"
tags: [paypal, android, mobile, vault, card-payments, kotlin, setup-token, payment-tokens, 3d-secure, purchase-later]
---

## Overview

Integration guide for saving credit/debit cards **without a purchase transaction** in Android apps using the PayPal Android SDK. Uses `CardVaultRequest` + `CardClient.vault()` (not `approveOrder()`).

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/android-sdk/cards/>

Last updated: 2025-03-11

## Key Takeaways

### Availability

35 countries — same as all other card vault integrations.

### Supported card types

American Express, Discover, Mastercard, Visa.

### Flow

1. Server: `POST /v3/vault/setup-tokens` with empty `payment_source.card: {}`
   - New customer: no `customer` field
   - Returning customer: include `customer.id` in request body
   - Response: `status: CREATED` (not `PAYER_ACTION_REQUIRED`)
2. Client: build `Card` + `CardVaultRequest(setupTokenID, card)`
3. `CardClient.vault(context, cardVaultRequest)` → `CardVaultListener`
4. `onVaultSuccess(result: CardVaultResult)` → send `result.setupTokenID` to server
5. Server: `POST /v3/vault/payment-tokens` → payment token + `customer.id`
6. Store both for future charges

### Gradle dependency

```groovy
dependencies {
    implementation 'com.paypal.android:card-payments:<CURRENT-VERSION>'
}
```

### Android SDK — vault call

```kotlin
val config = CoreConfig(clientID = "CLIENT_ID", environment = .live)
val cardClient = CardClient(config = config)
cardClient.cardVaultListener = object : CardVaultListener {
    override fun onVaultSuccess(result: CardVaultResult) {
        // result.setupTokenID → send to server to create payment token
    }
    override fun onVaultFailure(error: PayPalSDKError) { }
}
cardClient.vault(context, cardVaultRequest)
```

Note: source has typo `environemnt` (not `environment`) — preserved in raw file.

### Key differences vs during-purchase Android card vault

| | During purchase | Purchase later |
| --- | --- | --- |
| SDK method | `CardClient.approveOrder()` | `CardClient.vault()` |
| Listener | `ApproveOrderListener` | `CardVaultListener` |
| Vault API | Orders API `store_in_vault: ON_SUCCESS` | Setup token → payment token |
| Returning customer | `customer.id` in Create Order body | `customer.id` in setup token request body |
| Response status | `VAULTED` / `APPROVED` | `CREATED` |

### Key differences vs cards purchase-later JS SDK

| | JS SDK | Android SDK |
| --- | --- | --- |
| Client component | `CardFields` | `CardVaultRequest` + `CardClient.vault()` |
| Listener | `onApprove` callback | `CardVaultListener` |
| 3DS option | Yes (SCA_ALWAYS/WHEN_REQUIRED in setup token) | Yes (handled by vault method) |

### Security note

Don't expose payment token IDs client-side — same guidance as JS SDK.

## Raw Sources

- [[paypal-save-cards-purchase-later-android-sdk]] — verbatim integration guide

## Relevant Wiki Pages

- [[paypal-android-sdk]] — Android SDK overview (modules, CoreConfig, CardClient)
- [[paypal-vault]] — Vault concept: setup token → payment token flow
- [[source-paypal-save-cards-android-sdk]] — Android card vault during purchase (uses `approveOrder()`)
- [[source-paypal-save-cards-purchase-later-js-sdk]] — JS SDK equivalent
