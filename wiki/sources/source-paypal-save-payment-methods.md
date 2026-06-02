---
title: "Save Payment Methods (Overview)"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-payment-methods.md"
  - "paypal-save-payment-methods-during-purchase.md"
  - "paypal-save-paypal-js-sdk.md"
  - "paypal-save-venmo-js-sdk.md"
  - "paypal-save-payment-methods-purchase-later.md"
tags: [paypal, vault, payment-tokens, tokenization, save-payment-methods, cards, venmo, recurring-payments]
---

## Overview

Overview page for PayPal's Save Payment Methods feature — how merchants can vault cards, PayPal wallets, and Venmo for future use. Covers both save-during-purchase and save-for-later flows.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/>

Last updated: 2025-05-09

## Key Takeaways

### Two vault modes

| Mode | When saved | Payer present? | Use case |
| --- | --- | --- | --- |
| **With transaction** | At checkout | Yes | Faster future checkouts |
| **Without transaction** | Outside checkout | No | Free trial → charge later; off-session charges |

### Supported payment methods

- Credit and debit cards
- PayPal Wallets
- Venmo

### Payer flow

1. Payer begins checkout and chooses to save payment method
2. Merchant identifies payer with a **unique customer ID** — passed to PayPal on return visits
3. PayPal payments require a **billing agreement**; card payments do not
4. On return visits, each saved method shows as a **one-click button**

### Eligibility

Card vaulting requires **Expanded Checkout approval**. Supported in 34 countries:

Australia, Austria, Belgium, Bulgaria, Canada, China, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Hong Kong, Hungary, Ireland, Italy, Japan, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Singapore, Slovakia, Slovenia, Spain, Sweden, United Kingdom, United States

> [!warning] Contradiction — country count
> This overview page originally listed 34 countries. The save-cards JS SDK page (`source-paypal-save-cards-js-sdk`) lists 35, adding **Japan**. Japan has been added above to reflect the more specific page.

### Integration options

| Path | What can be saved | Integration |
| --- | --- | --- |
| **Save during purchase** | Cards + PayPal + Venmo | JS SDK |
| **Save during purchase** | Cards + PayPal only | Orders API |
| **Save during purchase** | Cards + PayPal only | Android SDK |
| **Save during purchase** | Cards + PayPal only | iOS SDK |
| **Save for purchase later** | Cards + PayPal only | Vault Payment Methods API |

> [!info] Venmo vault limitation
> Venmo can be saved during purchase via JS SDK only — not via Orders API, Android SDK, iOS SDK, or save-for-purchase-later. Cards and PayPal only for all other paths.

> [!warning] Pay Later + vault
> To continue offering Pay Later at checkout when integrating vault, you must use **Billing With Purchase** — not Billing Agreement. Billing With Purchase offers the same functionality and is compatible with existing payment options.

### JS SDK client-side vs client+server

- **Client-side only** (standard Checkout): saves PayPal Wallets only
- **Client + server-side** (Expanded Checkout): saves cards and Venmo in addition to PayPal

### APIs involved

- **Orders API** (`/docs/api/orders/v2/`) — save during purchase
- **Payment Method Tokens API** (`/docs/api/payment-tokens/v3/`) — save for purchase later
- Requires **Expanded Checkout** approval for card saving

## Save for purchase later (overview)

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/>

Last updated: 2025-02-27

Save without purchase — charge payers after a set time (e.g. free trial → billing). Payer does not need to be present.

| Integration | Side | Saves |
| --- | --- | --- |
| JavaScript SDK | Client or server-side | PayPal + cards |
| Payment Method Tokens API | Server-side only | PayPal + cards |
| Android SDK | Client-side | PayPal + cards |
| iOS SDK | Client-side | PayPal + cards |

**No Venmo** for any purchase-later path.

**JS SDK caveat**: client-side only integration saves PayPal Wallets only — need client+server (Expanded Checkout) to also save cards.

## JS SDK — Save PayPal Wallet during purchase

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/js-sdk/paypal/>

Last updated: 2025-08-25

### Flow

1. Merchant generates a **user ID token** via `POST /v1/oauth2/token` with `response_type=id_token`
2. Pass the token to the JS SDK via `data-user-id-token` attribute on the script tag
3. Create order with `payment_source.paypal.attributes.vault.store_in_vault: ON_SUCCESS`
4. Payer approves via PayPal Checkout (billing agreement)
5. Capture/authorize order → response contains `vault.id` + `customer.id`
6. Store the PayPal-generated `customer.id` for returning payers

### Returning payer

Pass `target_customer_id` (PayPal-generated, not your internal ID) in the token request. The SDK automatically renders saved PayPal methods as one-click buttons.

### Create Order payload (key fields)

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

### APPROVED vs VAULTED

If capture returns `vault.status: APPROVED` (not `VAULTED`), the vault ID isn't available yet. Subscribe to the `VAULT.PAYMENT-TOKEN.CREATED` webhook to receive the `vault.id` asynchronously.

> [!warning] PayPal's own guidance
> This page includes a warning: *"Don't save PayPal as a payment method during purchase"* and links to the Best Practices guide. This contradicts the page's own purpose — the warning likely nudges toward "save without purchase" for better UX, not a prohibition.

## JS SDK — Save Venmo during purchase

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/js-sdk/venmo/>

Last updated: 2025-03-25

### Key differences from PayPal Wallet vault

| | PayPal Wallet | Venmo |
| --- | --- | --- |
| Availability | 35 countries | **US only** |
| Sandbox support | Yes | **No — live environment only** |
| Payer app | PayPal Checkout | Venmo app (QR code fallback on desktop) |
| payment_source field | `paypal` | `venmo` |

### Incompatible JS SDK callbacks

`onShippingAddressChange`, `onShippingChange`, and `onShippingOptionsChange` **cannot** be used with Venmo vault.

### Venmo Create Order payload

```json
{
  "payment_source": {
    "venmo": {
      "attributes": {
        "vault": {
          "store_in_vault": "ON_SUCCESS",
          "usage_type": "MERCHANT"
        }
      }
    }
  }
}
```

Note: `customer_type` is absent from the Venmo payload (present in PayPal Wallet payload).

### Venmo capture response fields

- `payment_source.venmo.user_name` — Venmo handle (@firstnamelastname)
- Full address returned in capture response (unlike PayPal Wallet which returns only `country_code`)

### Venmo APPROVED vs VAULTED

Same pattern as PayPal/Apple Pay/cards — subscribe to `VAULT.PAYMENT-TOKEN.CREATED` webhook if `vault.status: APPROVED` is returned.

## Raw Sources

- [[paypal-save-payment-methods]] — verbatim webpage content with vault mode comparison, payer flow, supported methods, 34-country eligibility list, integration option table
- [[paypal-save-payment-methods-during-purchase]] — during-purchase overview: 4 integration paths, JS SDK client-only vs client+server distinction, Billing With Purchase warning for Pay Later
- [[paypal-save-paypal-js-sdk]] — JS SDK guide for saving PayPal Wallets: user ID token, `data-user-id-token`, `target_customer_id`, Create Order vault payload, APPROVED/VAULTED status, webhook
- [[paypal-save-venmo-js-sdk]] — JS SDK guide for saving Venmo: US-only, no sandbox, QR code desktop fallback, incompatible callbacks, Venmo-specific response fields
- [[paypal-save-payment-methods-purchase-later]] — Purchase-later overview: 4 integration paths (JS SDK/Tokens API/Android/iOS), no Venmo, JS SDK client-only saves PayPal only
- See also: [[source-paypal-save-applepay-js-sdk]] — Apple Pay vault detail guide

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-vault]] — PayPal Vault concept page (token types, setup token → payment token flow, stored_credential fields)
- [[paypal-expanded-checkout]] — Expanded Checkout approval required for card vaulting
- [[recurring-payments]] — off-session vault use case
