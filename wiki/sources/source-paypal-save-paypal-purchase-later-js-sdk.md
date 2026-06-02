---
title: "Save PayPal for Purchase Later with the JavaScript SDK"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-paypal-purchase-later-js-sdk.md"
tags: [paypal, vault, save-payment-methods, javascript-sdk, setup-token, payment-tokens, purchase-later, buttons]
---

## Overview

Integration guide for saving PayPal Wallets **without a purchase transaction** using the JavaScript SDK Buttons component and the setup token → payment token flow. Payers don't need to be present for future charges.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/js-sdk/paypal/>

Last updated: 2025-08-25

## Key Takeaways

### Availability

35 countries — same as all other PayPal Wallet vault integrations.

### Flow (setup token → payment token, no transaction)

1. Load JS SDK with `data-user-id-token` (from `POST /v1/oauth2/token` with `response_type=id_token`)
2. Returning payer: include `target_customer_id` in token request
3. Client: `window.paypal.Buttons({ createVaultSetupToken, onApprove, onError })` — **Buttons**, not CardFields
4. `createVaultSetupToken` → calls server → `POST /v3/vault/setup-tokens` with `payment_source.paypal`
5. Payer approves in PayPal pop-up
6. `onApprove({ vaultSetupToken })` → sends to server
7. Server: `POST /v3/vault/payment-tokens` with setup token → returns payment token + `customer.id`
8. Store both for future charges

### Setup token request (PayPal)

```json
{
  "payment_source": {
    "paypal": {
      "usage_type": "MERCHANT",
      "experience_context": {
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      }
    }
  }
}
```

`return_url` and `cancel_url` are required but can use filler values.

### Setup token response (PayPal-specific fields)

```json
{
  "id": "4G4976650J0948357",
  "status": "PAYER_ACTION_REQUIRED",
  "payment_source": {
    "paypal": {
      "permit_multiple_payment_tokens": false,
      "usage_pattern": "IMMEDIATE",
      "usage_type": "MERCHANT",
      "customer_type": "CONSUMER"
    }
  }
}
```

### Full frontend integration

```html
<div id="paypal-buttons-container"></div>
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT-ID&merchant-id=MERCHANT-ID"
        data-user-id-token="ID-TOKEN"></script>
<script>
window.paypal.Buttons({
    createVaultSetupToken: async () => {
        const result = await fetch("example.com/create/setup/token", { method: "POST" })
        return result.token
    },
    onApprove: async ({ vaultSetupToken }) => {
        return fetch("example.com/create/payment/token", {
            body: JSON.stringify({ vaultSetupToken })
        })
    },
    onError: (error) => console.log("An error occurred: ", error)
}).render("#paypal-buttons-container");
</script>
```

Note: `merchant-id` query param included in this guide (not shown in cards purchase-later).

### Key differences vs cards purchase-later JS SDK

| | Cards | PayPal |
| --- | --- | --- |
| SDK component | `CardFields` | `Buttons` |
| Setup token `payment_source` | `card: {}` | `paypal` with `usage_type` + `experience_context` |
| 3DS option | Yes | No |
| `merchant-id` param | Not shown | Shown |
| Payer interaction | Fills card form inline | PayPal pop-up approval |

### Key differences vs during-purchase PayPal JS SDK

| | Purchase later | During purchase |
| --- | --- | --- |
| SDK component | `Buttons` with `createVaultSetupToken` | `Buttons` with `createOrder` |
| Vault API | Setup token → payment token | Orders API `store_in_vault: ON_SUCCESS` |
| Transaction | No | Yes |

## Raw Sources

- [[paypal-save-paypal-purchase-later-js-sdk]] — verbatim integration guide with full code samples

## Relevant Wiki Pages

- [[paypal-vault]] — Vault concept: setup token → payment token flow
- [[source-paypal-save-cards-purchase-later-js-sdk]] — Cards purchase-later JS SDK (CardFields equivalent)
- [[source-paypal-save-paypal-js-sdk]] — PayPal during-purchase JS SDK (uses Orders API instead)
- [[source-paypal-save-payment-methods]] — Save payment methods overview
