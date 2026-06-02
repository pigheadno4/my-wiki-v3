---
title: "Stripe Link vs PayPal Fastlane: Checkout Acceleration"
type: comparison
dimension: "checkout-acceleration"
date_created: 2026-04-22
tags: [stripe, paypal, link, fastlane, autofill, saved-payment-methods, subscriptions, recurring-payments, checkout-ux]
---

## Overview

Both Stripe Link and PayPal Fastlane solve the same problem: recognizing returning buyers and pre-filling their payment details so they don't have to re-enter a card. But they do it with fundamentally different architectures, which determines where each fits.

## UX Architecture: Enhancement vs Orchestrator

This is the most important difference. The two products have opposite mental models for where identity fits in the checkout flow.

### Stripe Link — payment form first, autofill is optional

```
Card form renders immediately
  → [optional] user clicks "Autofill" button
  → Link popup → OTP → card pre-filled
```

Link is a **progressive enhancement**. The card input renders unconditionally. The "Autofill" button appears inline within the Stripe-controlled card field. Users who ignore it get a standard card form. Users who click it get autofill. No mandatory gate, no restructuring of the checkout flow.

### PayPal Fastlane — email gates the form

```
Email field (required)
  → lookupCustomerByEmail()
  → [if member] OTP modal → profileData pre-fills form
  → [if guest] manual card entry + opt-in toggle to create profile
```

Fastlane is a **checkout orchestrator**. The email step is mandatory before the payment component renders. The entire checkout is structured around Fastlane's identity lookup. You cannot skip or defer the email step — `lookupCustomerByEmail()` must run before `FastlanePaymentComponent` is shown.

### Side-by-side

| Aspect | Stripe Link | PayPal Fastlane |
|---|---|---|
| Payment form renders | Immediately, unconditionally | After email lookup resolves |
| Identity trigger | Optional "Autofill" button | Mandatory email field |
| Non-members | Zero friction — just type card | Slight friction — email field still required |
| Drop into existing form | Drop-in, no flow change | Requires restructuring around email gate |
| Best described as | Progressive enhancement | Checkout orchestrator |

## Token Lifecycle

The products produce fundamentally different output tokens.

| | Stripe Link | PayPal Fastlane |
|---|---|---|
| Output | `pm_xxx` PaymentMethod (persistent) | `single_use_token` (ephemeral) |
| Expiry | None — PM persists until card expires | 3 hours from issuance |
| Reusable | Yes — `setup_future_usage: off_session` | No — one transaction only |
| Used by | PaymentIntents / Checkout Sessions API | Orders v2 API (`payment_source.card.single_use_token`) |

**Link is not a token layer at all.** It is an identity/autofill layer. What comes out the other end is a standard Stripe `pm_xxx` PaymentMethod object — the same object produced by any other Stripe integration path. That PM supports the full Stripe lifecycle: save, reuse, subscribe, charge off-session.

## Subscription and Recurring Payments

### Stripe Link (trivial)

Link autofill produces a PaymentMethod. Save it with `setup_future_usage: off_session` or use Setup mode, then charge indefinitely off-session:

```js
// Save during first payment
stripe.checkout.sessions.create({
  payment_intent_data: { setup_future_usage: 'off_session' }
});

// Or: save without charging
stripe.checkout.sessions.create({ mode: 'setup' });

// Subsequent recurring charge
stripe.paymentIntents.create({
  customer: 'cus_xxx',
  payment_method: 'pm_xxx',
  off_session: true,
  confirm: true,
});
```

No extra steps. The PM from the Link autofill flow is identical to one collected any other way.

### PayPal Fastlane (two-step, verified)

Fastlane's `single_use_token` cannot be reused. To enable recurring charges you must explicitly vault the card during the first transaction, then use the resulting `vault_id` for all future charges. This was verified against the sandbox.

> **Hard constraint (from PayPal docs):** "Fastlane does not support a flow where a customer or payment method is created prior to a transaction." You cannot save-then-charge (like Stripe Setup mode). You must charge-then-save.

#### Step 1 — First transaction: `single_use_token` + `store_in_vault`

**Request**
```
POST https://api-m.sandbox.paypal.com/v2/checkout/orders
```
```json
{
  "intent": "CAPTURE",
  "payment_source": {
    "card": {
      "single_use_token": "tokencc_bj_zhfxyc_vxbmgy_xjshwn_ts69wy_d25",
      "attributes": {
        "vault": { "store_in_vault": "ON_SUCCESS" },
        "customer": {}
      }
    }
  },
  "purchase_units": [{
    "amount": { "currency_code": "USD", "value": "1.00" },
    "shipping": {
      "type": "SHIPPING",
      "name": { "full_name": "Test User" },
      "address": {
        "address_line_1": "123 Main St",
        "admin_area_2": "New York",
        "admin_area_1": "NY",
        "postal_code": "10001",
        "country_code": "US"
      }
    }
  }]
}
```

**Response** `200 OK` — key fields:
```json
{
  "id": "45A69424A1436581J",
  "status": "COMPLETED",
  "payment_source": {
    "card": {
      "last_digits": "0004",
      "brand": "VISA",
      "attributes": {
        "vault": {
          "id": "0jt88057hw1618155",
          "status": "VAULTED",
          "customer": { "id": "OGKdKQVoxn" }
        }
      }
    }
  },
  "purchase_units": [{
    "payments": {
      "captures": [{
        "id": "4XJ41108B93886404",
        "status": "COMPLETED",
        "amount": { "currency_code": "USD", "value": "1.00" },
        "network_transaction_reference": {
          "id": "074101406505300",
          "network": "VISA"
        },
        "processor_response": {
          "avs_code": "A",
          "cvv_code": "M",
          "response_code": "0000"
        }
      }]
    }
  }]
}
```

**Store from this response:**
- `vault.id` → `0jt88057hw1618155` (used in every subsequent charge)
- `vault.customer.id` → `OGKdKQVoxn` (used to list/manage saved payment methods)
- `network_transaction_reference.id` → `074101406505300` (required for `previous_network_transaction_reference` in recurring charges)

#### Step 2 — Recurring charge: `vault_id` only, no browser, no Fastlane SDK

**Request**
```
POST https://api-m.sandbox.paypal.com/v2/checkout/orders
```
```json
{
  "intent": "CAPTURE",
  "payment_source": {
    "card": {
      "vault_id": "0jt88057hw1618155",
      "stored_credential": {
        "payment_initiator": "MERCHANT",
        "payment_type": "RECURRING",
        "usage": "SUBSEQUENT",
        "previous_network_transaction_reference": {
          "id": "074101406505300",
          "network": "VISA"
        }
      }
    }
  },
  "purchase_units": [{
    "amount": { "currency_code": "USD", "value": "9.99" },
    "description": "Monthly subscription renewal"
  }]
}
```

**Response** `200 OK`:
```json
{
  "id": "5HD644172F404305B",
  "status": "COMPLETED",
  "payment_source": {
    "card": { "brand": "VISA", "last_digits": "0004" }
  },
  "purchase_units": [{
    "payments": {
      "captures": [{
        "status": "COMPLETED",
        "amount": { "currency_code": "USD", "value": "9.99" }
      }]
    }
  }]
}
```

**At this point Fastlane is completely out of the picture.** The recurring charge is a pure server-to-server PayPal Orders API call.

> [!warning] `stored_credential` schema correction
> The PayPal Vault concept page listed `usage_pattern: "RECURRING_POSTPAID"` as the field for the Orders API. This is **incorrect for the Orders API** — `usage_pattern` belongs to the Payment Method Tokens v3 API setup flow. The Orders API `stored_credential` object requires `payment_type: "RECURRING"` (not `usage_pattern`). Verified against sandbox: omitting `payment_type` returns `MISSING_REQUIRED_PARAMETER`. See [[paypal-vault]].

### Subscription comparison

| | Stripe Link | PayPal Fastlane |
|---|---|---|
| Save without charging | Yes — `mode: 'setup'` or Setup Intents | No — must transact first |
| Save during payment | `setup_future_usage: 'off_session'` | `store_in_vault: ON_SUCCESS` in order request |
| Recurring token type | Same `pm_xxx` PaymentMethod | Different — `vault_id`, not Fastlane token |
| Network txn ref required | No | Yes — must store from first capture response |
| Recurring charge API | PaymentIntents (same as first charge) | Orders v2 with `stored_credential` block |
| Fastlane involved in renewals | N/A — Link is just autofill | Not at all — `vault_id` is standalone |

## Customization and Constraints

| | Stripe Link | PayPal Fastlane |
|---|---|---|
| Fonts | Full Appearance API — any CSS | 9 allowed families only (Arial, Verdana, Tahoma, Trebuchet MS, Times New Roman, Georgia, Garamond, Courier New, Brush Script MT) |
| Colors | Full CSS via Appearance API | `StyleOptions` object; WCAG AA auto-enforced (contrast ratio ≥ 4.5:1) |
| "Powered by" branding | Optional | `FastlaneWatermarkComponent` is **mandatory** |
| Geography | Global | US buyers only |
| Domain validation | None | Required in production (`DOMAINS` param); sandbox: omit |

## Integration Fit

| Scenario | Stripe Link | PayPal Fastlane |
|---|---|---|
| Drop into existing card form | Natural fit | Requires restructuring around email gate |
| Billing update / card-on-file (no charge) | Natural fit — Setup mode | Not supported — must charge first |
| Guest e-commerce checkout | Works | Purpose-built for this |
| SaaS subscription billing | Native — PM persists, subscribe directly | Two-step: charge first, vault, then recurring |
| Non-US buyers | Yes | No |

## Related Pages

- [[stripe-link-authentication-element]] — Link Authentication Element: dual-purpose email + autofill, combining with other elements
- [[stripe-saved-payment-methods]] — Stripe save/reuse: allow_redisplay, Setup mode, off-session charging
- [[stripe-subscriptions]] — Stripe Subscriptions: full lifecycle, provisioning, customer portal
- [[paypal-fastlane]] — Fastlane concept: guest/member flows, integration pattern, SDK methods
- [[paypal-vault]] — PayPal Vault: vault_id lifecycle, stored_credential, usage_pattern (Tokens API) vs payment_type (Orders API)
- [[source-paypal-fastlane-getting-started]] — Fastlane raw source: full SDK reference, OTP sandbox codes, vaulting, 3DS

## Sources

- [[source-paypal-fastlane-getting-started]] — Fastlane SDK methods, single_use_token, store_in_vault, vault reference
- [[source-stripe-link-authentication-element]] — Link Authentication Element: email/auth dual purpose, prefill, combining
- [[source-stripe-save-and-reuse-elements]] — Stripe Setup mode: save without charging, SetupIntents
- [[source-stripe-save-during-payment-elements]] — Stripe save during payment: setup_future_usage, CustomerSession
- [[source-stripe-payment-element]] — Payment Element: Link autofill, combining elements, layout options
