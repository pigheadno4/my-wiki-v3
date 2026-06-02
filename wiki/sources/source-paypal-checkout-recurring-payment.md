---
title: "PayPal Checkout: Recurring Payments"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-recurring-payment.md"
tags: [paypal, recurring-payments, subscriptions, vault, payment-tokens, payment-method-tokens-api, stored-credentials, node-js]
---

## PayPal Checkout: Recurring Payments

Official PayPal developer guide for integrating recurring payments (subscriptions, automatic billing) using the Payment Method Tokens v3 API and PayPal JS SDK vault flow.

Source URL: <https://developer.paypal.com/studio/checkout/standard/integrate> (Recurring Payment tab)

## Eligibility

- US buyers and merchants only
- Requires Payment Method Tokens v3 API (not the standard Orders API alone)

## How It Works — High Level

1. Buyer adds PayPal as a payment method → PayPal creates a **setup token**
2. Recurring Payments module shows billing terms to buyer
3. Buyer consents → setup token upgraded to a **payment method token** (vault ID)
4. Merchant uses vault ID for all future charges via Orders API

## Key Concepts

### Setup Token vs Payment Token

| Token | Purpose | Lifetime |
| ----- | ------- | -------- |
| Setup token | Buyer approval flow; holds billing plan details | 3 days (expires) |
| Payment token (vault ID) | Stored credential for future merchant-initiated charges | Persistent |

### `usage_pattern` Values

Passed in `payment_source.paypal.usage_pattern` on setup token creation. Controls how PayPal presents the recurring billing context to the buyer:

- `SUBSCRIPTION_PREPAID` — upfront subscription
- `SUBSCRIPTION_POSTPAID` — postpaid subscription
- `RECURRING_POSTPAID` — used on subsequent charges via `stored_credential`
- Unscheduled and installment patterns also supported

### `billing_plan` Object (on setup token)

Displayed to the buyer on the PayPal review page:

| Field | Description |
| ----- | ----------- |
| `name` | Plan display name |
| `billing_cycles` | Array of up to 3 cycles (trial or regular); each has `tenure_type`, `pricing_scheme`, `frequency`, `total_cycles`, `start_date` |
| `one_time_charges` | One-time fees (setup fee, product price, shipping, taxes) not part of the recurring schedule |

## Integration Flow (3 steps)

### Step 1 — Create Setup Token (`POST /api/vault`)

Server calls `vaultController.setupTokensCreate()` with:

- `usage_type: "MERCHANT"`
- `usage_pattern`: e.g. `SUBSCRIPTION_PREPAID`
- `billing_plan`: full plan details
- `experience_context.return_url` / `cancel_url`

Frontend: `createVaultSetupToken()` callback (replaces `createOrder`) — POSTs to `/api/vault`, returns `setupTokenData.id`

### Step 2 — Get Buyer Approval

Buyer reviews the billing plan in the PayPal pop-up and consents. After approval, `onApprove` fires with `data.vaultSetupToken`.

### Step 3 — Create Payment Token (`POST /api/vault/payment-tokens`)

On `onApprove`, frontend POSTs to `/api/vault/payment-tokens` with `{ payment_source: { token: { id: data.vaultSetupToken, type: "SETUP_TOKEN" } } }`.

Server calls `vaultController.paymentTokensCreate()` → returns persistent payment token (vault ID).

## Charging the Buyer (Subsequent Payments)

Use the vault ID in a standard Orders API call — no buyer interaction needed:

```javascript
payment_source: {
    paypal: {
        vault_id: "PAYMENT-TOKEN-ID",
        stored_credential: {
            payment_initiator: "MERCHANT",
            usage: "SUBSEQUENT",
            usage_pattern: "RECURRING_POSTPAID",
        },
    },
}
```

Route: `POST /api/orders` → `ordersController.ordersCreate()`

## SDK Differences vs One-time Payment

| Aspect | One-time | Recurring |
| ------ | -------- | --------- |
| JS SDK callback | `createOrder` | `createVaultSetupToken` |
| `onApprove` arg | `data.orderID` | `data.vaultSetupToken` |
| Server controller | `OrdersController` | `VaultController` + `OrdersController` |
| Script `components` | `buttons` | `buttons` (no vault component needed in script tag) |
| `enable-funding` | venmo,paylater,card | not shown (omitted) |

## Server SDK Controllers Used

- `VaultController` — `setupTokensCreate`, `paymentTokensCreate`
- `OrdersController` — `ordersCreate` (for subsequent charges)
- Note: `PaymentsController` imported but not used in recurring flow

## Notable Code Patterns

### Setup token creation (server)

```javascript
paymentSource: {
    paypal: {
        usage_type: "MERCHANT",
        usage_pattern: "SUBSCRIPTION_PREPAID",
        billing_plan: {
            billing_cycles: [{
                tenure_type: "REGULAR",
                pricing_scheme: { pricing_model: "FIXED", price: { value: "100", currency_code: "USD" } },
                frequency: { interval_unit: "MONTH", interval_count: "1" },
                total_cycles: "1",
                start_date: "2026-04-13",
            }],
            one_time_charges: {
                product_price: { value: "10", currency_code: "USD" },
                total_amount: { value: 10, currency_code: "USD" },
            },
            product: { description: "Yearly Membership", quantity: "1" },
            name: "Company",
        },
        experience_context: { return_url: "...", cancel_url: "..." },
    },
}
```

### Subsequent charge (server)

```javascript
payment_source: {
    paypal: {
        vault_id: "PAYMENT-TOKEN-ID",
        stored_credential: { payment_initiator: "MERCHANT", usage: "SUBSEQUENT", usage_pattern: "RECURRING_POSTPAID" },
    },
}
```

## Raw Sources

- [[paypal-checkout-recurring-payment]] — verbatim webpage content with full frontend + backend code samples

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[paypal-vault]] — PayPal Vault / Payment Method Tokens concept
- [[recurring-payments]] — Recurring payments concept
- [[source-paypal-checkout-getting-started]] — prerequisite setup guide
- [[source-paypal-checkout-integrate-one-time-payment]] — one-time payment integration (baseline)
