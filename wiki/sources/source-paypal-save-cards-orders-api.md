---
title: "Save Cards with the Orders API"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-cards-orders-api.md"
tags: [paypal, vault, card-payments, orders-api, save-payment-methods, pci-dss, 3d-secure, sca, payment-tokens]
---

## Overview

Integration guide for saving credit/debit cards during purchase using the Orders API directly (no client-side SDK). Targets merchants who are PCI SAQ D compliant — raw card data is passed in the Create Order request body.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/orders-api/cards/>

Last updated: 2025-05-13

## Key Takeaways

### When to use this path

Use the Orders API card vault when you want to save cards during checkout but are **not** PCI SAQ A compliant. This path requires **PCI SAQ D** (the highest level) since raw card numbers are passed directly to the API.

| Integration | PCI requirement | Client-side component |
| --- | --- | --- |
| JS SDK / Android / iOS | SAQ A | Yes (SDK handles card fields) |
| Orders API | **SAQ D** | No (raw card in server request) |

### Availability

35 countries — same as all other card vault integrations.

### Limitations

- Orders API supports PayPal and card payment methods only — **no Venmo**
- Requires existing advanced credit and debit card payments integration

### Create Order request (single-step capture + vault)

```json
{
  "intent": "CAPTURE",
  "payment_source": {
    "card": {
      "number": "4111111111111111",
      "expiry": "2026-02",
      "name": "Firstname Lastname",
      "billing_address": {
        "address_line_1": "2211 N First Street",
        "admin_area_2": "San Jose",
        "admin_area_1": "CA",
        "postal_code": "95131",
        "country_code": "US"
      },
      "attributes": {
        "verification": {
          "method": "SCA_WHEN_REQUIRED"
        },
        "vault": {
          "store_in_vault": "ON_SUCCESS"
        }
      }
    }
  },
  "purchase_units": [{ "amount": { "currency_code": "USD", "value": "101.00" } }]
}
```

Key differences from SDK flows:
- Raw `number` + `expiry` in the request body (SAQ D required)
- No separate "approve order" step — capture happens in the same request
- No `customer.id` field shown for returning payers (unlike SDK flows)

### 3DS handling

If `SCA_WHEN_REQUIRED` triggers authentication, response returns `status: PAYER_ACTION_REQUIRED`. Merchant must handle the payer action redirect before recapturing.

### APPROVED vs VAULTED

Same pattern as all other integrations — subscribe to `VAULT.PAYMENT-TOKEN.CREATED` webhook if `vault.status: APPROVED`.

> [!info] Doc typo
> The response sample uses `"id" = "ROaPMoZUaV"` (with `=` instead of `:`) — this is a typo in the original PayPal documentation.

### Next steps

- RTAU (real-time account updater) — keeps saved cards current
- Subsequent transactions: use `vault.id` with Orders API

## Raw Sources

- [[paypal-save-cards-orders-api]] — verbatim integration guide

## Relevant Wiki Pages

- [[paypal-vault]] — Vault concept: token types, APPROVED/VAULTED, webhook
- [[source-paypal-save-cards-js-sdk]] — JS SDK equivalent (SAQ A, client-side card fields)
- [[source-paypal-save-cards-android-sdk]] — Android SDK equivalent
- [[source-paypal-save-cards-ios-sdk]] — iOS SDK equivalent
