---
title: "Save Cards with the JavaScript SDK"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-cards-js-sdk.md"
  - "paypal-save-cards-with-purchase-sdk-v6.md"
  - "paypal-save-cards-without-purchase-sdk-v6.md"
tags: [paypal, vault, save-payment-methods, cards, 3d-secure, orders-api, webhook, expanded-checkout, card-fields, javascript-sdk-v6]
---

## Overview

Step-by-step integration guide for saving credit/debit cards during purchase using the PayPal JavaScript SDK (CardFields) and Orders v2 API. Requires Expanded Checkout approval.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/js-sdk/cards/>

Last updated: 2025-05-14

## Key Takeaways

### Availability

35 countries — same as the overview page's list plus **Japan** (see contradiction note below).

> [!warning] Contradiction — supported country count
> The save-payment-methods overview page (`source-paypal-save-payment-methods`) lists **34 countries** for card vaulting. This page lists **35**, adding **Japan**. The overview page's eligibility section should be updated to include Japan.

### Prerequisites

- Existing **Expanded Checkout** (advanced credit/debit card payments) integration — PayPal must approve the account
- Developer Dashboard: App → Sandbox App Settings → App Feature Options → Accept payments → Advanced options → **Vault** must be checked

### UX pattern — save checkbox

Add an explicit opt-in checkbox to the card form:

```html
<input type="checkbox" id="save" name="save">
<label for="save">Save your card</label>
```

Pass `document.getElementById("save").checked` in `createOrder()` to control whether vaulting is requested.

### Key request fields

**First-time save:**

```json
"payment_source": {
  "card": {
    "attributes": {
      "vault": { "store_in_vault": "ON_SUCCESS" },
      "verification": { "method": "SCA_ALWAYS" }
    }
  }
}
```

**Returning payer** (link to existing customer):

```json
"attributes": {
  "customer": { "id": "PayPal-generated customer id" },
  "vault": { "store_in_vault": "ON_SUCCESS" }
}
```

**Full example vault attributes** (from complete HTML sample):

```json
"vault": {
  "store_in_vault": "ON_SUCCESS",
  "usage_type": "PLATFORM",
  "customer_type": "CONSUMER",
  "permit_multiple_payment_tokens": true
}
```

### 3DS with vault

Pass `payment_source.card.attributes.verification.method` alongside vault:

- `SCA_ALWAYS` — triggers 3DS for every transaction
- `SCA_WHEN_REQUIRED` — triggers only when PSD2 mandate applies

Handle `liabilityShift` in `onApprove` callback.

### APPROVED vs VAULTED (same pattern as Apple Pay)

| Status | Meaning | `vault_id` available? |
| --- | --- | --- |
| `VAULTED` | Card saved | Yes — use `payment_source.card.attributes.vault.id` |
| `APPROVED` | Approved to save, in progress | No — subscribe to `VAULT.PAYMENT-TOKEN.CREATED` webhook |

`resource.id` in webhook = vault ID; `resource.customer.id` = PayPal customer ID.

### Retrieving saved cards for returning payers

Use Payment Method Tokens v3 API: `GET /v3/vault/payment-tokens?customer_id={id}` to list all saved methods, then pass selected `vault_id` to Orders API for capture.

### Test cards (sandbox)

| Card number | Type |
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

### Next steps

- Use Payment Method Tokens API for subsequent/recurring transactions
- Keep saved cards current with RTAU (real-time account updater)

## Raw Sources

- [[paypal-save-cards-js-sdk]] — full integration guide: checkbox UX, createOrder/onApprove code, first-time vs returning payer requests, APPROVED/VAULTED pattern, webhook payload, full HTML example, 14 test cards

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-vault]] — Vault concept: token types, APPROVED vs VAULTED, webhook pattern
- [[paypal-expanded-checkout]] — Expanded Checkout approval required
- [[source-paypal-save-payment-methods]] — Save payment methods overview (note: country count contradiction)
- [[source-paypal-save-applepay-js-sdk]] — Apple Pay vault guide (same APPROVED/VAULTED pattern)
- [[paypal-save-cards-with-purchase-sdk-v6]] — SDK v6 version (docs.paypal.ai): `createCardFieldsOneTimePaymentSession`, `session.isEligible()`, store_in_vault ON_SUCCESS, 35-country availability, 14 test cards, APPROVED→webhook pattern, permit_multiple_payment_tokens
- [[paypal-save-cards-without-purchase-sdk-v6]] — Save cards without purchase SDK v6: `createCardFieldsSavePaymentSession`, setup token → payment token flow, cannot mix with one-time session on same page, don't expose token IDs client-side
