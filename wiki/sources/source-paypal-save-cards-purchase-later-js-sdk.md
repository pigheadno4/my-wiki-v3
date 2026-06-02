---
title: "Save Cards for Purchase Later with the JavaScript SDK"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-cards-purchase-later-js-sdk.md"
tags: [paypal, vault, save-payment-methods, cards, javascript-sdk, card-fields, setup-token, payment-tokens, 3d-secure, purchase-later]
---

## Overview

Integration guide for saving credit/debit cards **without a purchase transaction** using the JavaScript SDK. Payer fills CardFields, card is vaulted via setup token → payment token flow. No `store_in_vault` or `createOrder` involved.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/js-sdk/cards/>

Last updated: 2025-07-01

## Key Takeaways

### When to use

Save cards for later without requiring an immediate purchase — free trials, deferred billing, off-session charges. Targets merchants who are not PCI SAQ A compliant (JS SDK handles card data via hosted fields).

### Availability

35 countries — same as all other card vault integrations.

### Supported card types

American Express, Discover, Mastercard, Visa. (Note: Diners Club and Maestro appear in the test card table but are not listed in the supported types list.)

### Flow (two-stage vault — no transaction)

1. Server: `POST /v3/vault/setup-tokens` with empty `payment_source.card: {}` → returns `setup_token`
2. Client: `createVaultSetupToken` callback returns setup token to SDK
3. Payer fills CardFields → SDK updates setup token with card details
4. `onApprove` fires with `{ vaultSetupToken }` (+ `liabilityShift` if 3DS)
5. Server: `POST /v3/vault/payment-tokens` with `token.id: vaultSetupToken, type: SETUP_TOKEN` → returns payment token + `customer.id`
6. Store payment token + `customer.id` for future charges

### Key SDK callback: `createVaultSetupToken`

**Replaces** `createOrder` — these two **cannot coexist**:

```javascript
// THROWS VALIDATION ERROR:
paypal.CardFields({
    createVaultSetupToken: () => {...},
    createOrder: () => {...}  // ← can't use both
})
```

### No verification (basic)

```javascript
const cardFields = paypal.CardFields({
    createVaultSetupToken: async () => {
        const result = await fetch("example.com/create/setup/token")
        return result.token
    },
    onApprove: ({ vaultSetupToken }) => {
        return fetch("example.com/create/payment/token", {
            body: JSON.stringify({ vaultSetupToken })
        })
    },
    onError: (error) => console.error(error)
})
```

### 3D Secure option

Pass `SCA_ALWAYS` or `SCA_WHEN_REQUIRED` in `verification_method` on setup token creation. `onApprove` returns `liabilityShift` in addition to `vaultSetupToken`. `onCancel` fires when payer closes 3DS modal (order cancelled).

### Security note

Don't expose payment token IDs client-side. Create separate IDs server-side and correlate them — prevents token enumeration by payers.

### Complete back-end integration (Express)

Two endpoints required:
- `POST /api/vault/token` — creates setup token with empty card
- `POST /api/vault/payment-token` — upgrades setup token → payment token, saves `paymentMethodToken` + `customer.id`

### Test cards (14 total)

| Number | Type |
| --- | --- |
| 371449635398431 | American Express |
| 376680816376961 | American Express |
| 36259600000004 | Diners Club |
| 6304000000000000 | Maestro |
| 5063516945005047 | Maestro |
| 2223000048400011 | Mastercard |
| 4005519200000004 | Visa |
| 4012000033330026 | Visa |
| 4012000077777777 | Visa |
| 4012888888881881 | Visa |
| 4217651111111119 | Visa |
| 4500600000000061 | Visa |
| 4772129056533503 | Visa |
| 4915805038587737 | Visa |

### Show saved payment methods

`GET /v3/vault/payment-tokens?customer_id=CUSTOMER-ID` — list all tokens for a customer. Display card brand + last 4 digits.

## Raw Sources

- [[paypal-save-cards-purchase-later-js-sdk]] — verbatim integration guide with full code samples

## Relevant Wiki Pages

- [[paypal-vault]] — Vault concept: setup token → payment token flow, stored credentials
- [[source-paypal-save-cards-js-sdk]] — Cards during-purchase JS SDK (uses `store_in_vault: ON_SUCCESS` instead)
- [[source-paypal-save-payment-methods]] — Save payment methods overview including purchase-later paths
