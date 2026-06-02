---
title: "Save Cards with the Android SDK"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-cards-android-sdk.md"
tags: [paypal, android, mobile, vault, card-payments, kotlin, 3d-secure, sca, payment-tokens, save-payment-methods]
---

## Overview

Integration guide for saving credit/debit cards during purchase in Android apps using the PayPal Android SDK (Kotlin/Compose). Extends the existing advanced card payments integration with vault support.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/android-sdk/cards/>

Last updated: 2025-02-27

## Key Takeaways

### Availability

Same 35 countries as JS SDK card vault (AU, AT, BE, BG, CA, CN, CY, CZ, DK, EE, FI, FR, DE, HK, HU, IE, IT, JP, LV, LI, LT, LU, MT, NL, NO, PL, PT, RO, SG, SK, SI, ES, SE, GB, US).

### UX — Save checkbox (Compose)

```kotlin
@Composable
fun CheckoutScreen() {
  var shouldSaveCard by remember { mutableStateOf(false) }
  Column {
    Checkbox(
      checked = shouldSaveCard,
      onCheckedChange = { value -> shouldSaveCard = value }
    )
    Text("Save your card")
  }
}
```

### Create Order — first-time payer

```json
{
  "payment_source": {
    "card": {
      "attributes": {
        "vault": {
          "store_in_vault": "ON_SUCCESS"
        },
        "verification": {
          "method": "SCA_ALWAYS"
        }
      }
    }
  }
}
```

### Create Order — returning payer

Pass `customer.id` inside `payment_source.card.attributes.customer`:

```json
{
  "payment_source": {
    "card": {
      "attributes": {
        "vault": { "store_in_vault": "ON_SUCCESS" },
        "customer": { "id": "PayPal-generated-customer-id" }
      }
    }
  }
}
```

Note: unlike the JS SDK (which uses `target_customer_id` in the token request), Android SDK passes `customer.id` directly in the Create Order body.

### Android SDK — approve order

```kotlin
val coreConfig = CoreConfig("CLIENT_ID")
val cardClient = CardClient(activity, coreConfig)

val returnUrl = "com.myapp.package://example.com/return_url"
val request = CardRequest("ORDER_ID", card, returnUrl)
cardClient.approveOrder(activity, request)
```

Callbacks via `ApproveOrderListener`:
- `onApproveOrderSuccess(result: CardResult)` — proceed to server capture/authorize
- `onApproveOrderFailure(error: PayPalSDKError)`
- `onApproveOrderCanceled()` — user canceled 3DS
- `onApproveOrderThreeDSecureWillLaunch()` / `onApproveOrderThreeDSecureDidFinish()`

### APPROVED vs VAULTED

Same pattern as JS SDK/Apple Pay/Venmo — if `vault.status: APPROVED`, subscribe to `VAULT.PAYMENT-TOKEN.CREATED` webhook to get `vault.id` asynchronously.

### Subsequent payments (step 6)

1. Call `GET /v3/vault/payment-tokens?customer_id=...` to list saved cards
2. Display saved card to payer
3. Pass selected `vault.id` to Orders API for the new transaction

### Testing

Sandbox supported. Use test cards from PayPal sandbox card testing page. Steps: save card → capture → verify in sandbox merchant account → list tokens → pay with saved card.

### Next steps

- Real-time account updater (RTAU) — keeps saved cards current without payer re-entry
- Subsequent/recurring transactions: follow "Use payment method token with checkout" guide

## Raw Sources

- [[paypal-save-cards-android-sdk]] — verbatim integration guide

## Relevant Wiki Pages

- [[paypal-android-sdk]] — Android SDK overview (modules, CoreConfig, CardClient, 3DS pattern)
- [[paypal-vault]] — Vault concept: token types, APPROVED/VAULTED status, webhook
- [[source-paypal-android-card-payments]] — Base card payments Android integration (prerequisite for this guide)
- [[source-paypal-save-cards-js-sdk]] — JS SDK equivalent: checkbox UX, SCA, 14 test cards, returning payer via `data-user-id-token`
