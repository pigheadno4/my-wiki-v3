---
title: "PayPal Checkout: Recurring Payments Module"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-recurring-payments-module.md"
tags: [paypal, checkout, recurring-payments, vault, setup-token, payment-tokens, usage-pattern, billing-plan, orders-api, us-only]
---

## PayPal Checkout: Recurring Payments Module

Official PayPal reference for the recurring payments module — the most comprehensive source on `usage_pattern` values, billing plan structure, and the two integration paths (save with/without purchase).

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/recurring-payments-module/>

Last updated: 2025-08-14

## Key Takeaways

### Two integration paths

| Path | API | When |
| ---- | --- | ---- |
| Save without purchase | Payment Method Tokens v3 API (`/v3/vault/setup-tokens`) | Free trials, postpaid, no immediate charge |
| Save with purchase | Orders v2 API (`/v2/checkout/orders`) | Subscription starts immediately on sign-up |

### `usage_pattern` — complete reference

This is the most complete `usage_pattern` reference in the wiki:

| Type | Amount | Frequency | Duration | Values |
| ---- | ------ | --------- | -------- | ------ |
| Subscription | Fixed | Regular | None | `SUBSCRIPTION_PREPAID`, `SUBSCRIPTION_POSTPAID` |
| Recurring | Variable | Regular | None | `RECURRING_PREPAID`, `RECURRING_POSTPAID` |
| Unscheduled | Fixed or variable | Variable | None | `UNSCHEDULED_PREPAID`, `UNSCHEDULED_POSTPAID` |
| Installment | Fixed | Defined | Fixed | `INSTALLMENT_PREPAID`, `INSTALLMENT_POSTPAID` |

PREPAID = charged before delivery; POSTPAID = charged after delivery.

### Which field carries `usage_pattern`?

| Scenario | Field |
| -------- | ----- |
| Save without purchase (setup) | `payment_source.paypal.usage_pattern` |
| Save with purchase (setup) | `payment_source.paypal.attributes.vault.usage_pattern` |
| Subsequent merchant-initiated charge | `payment_source.paypal.stored_credential.usage_pattern` |

### Three merchant choices for recurring metadata

1. Pass `usage_pattern` + `billing_plan.name` → buyer sees full plan details
2. Pass `usage_pattern` only → buyer sees generic recurring flow (no plan details)
3. Pass neither → non-recurring flow — **not recommended** for recurring transactions

### User action: Setup Now vs Continue (without purchase)

- `Setup Now` → buyer redirected to merchant confirmation page (typical)
- `Continue` → buyer redirected to merchant checkout (when further steps needed)

### `billing_plan` for save-with-purchase

When saving during purchase, the billing plan goes inside `purchase_units.items[]` as a separate line item with a `billing_plan` object — not inside `payment_source.paypal`. This is different from the save-without-purchase path (where it's inside `payment_source.paypal.billing_plan`).

### Token lifecycle

```
POST /v3/vault/setup-tokens → SETUP-TOKEN-ID (expires 3 days)
  → buyer approves (approve link from response)
POST /v3/vault/payment-tokens → persistent payment token
  → use vault_id in POST /v2/checkout/orders for recurring charges
```

### Payment Method Tokens API operations

- Retrieve: `GET /v3/vault/payment-tokens/{id}`
- List customer tokens: `GET /v3/vault/customer/payment-tokens`
- Delete: `DELETE /v3/vault/payment-tokens/{id}`

## Contradictions / additions vs earlier sources

> [!info] Expanding
> This page adds `UNSCHEDULED_PREPAID`, `UNSCHEDULED_POSTPAID`, `INSTALLMENT_PREPAID`, `INSTALLMENT_POSTPAID` to the `usage_pattern` table — these weren't present in [[source-paypal-checkout-recurring-payment]] which only listed `SUBSCRIPTION_PREPAID/POSTPAID` and `RECURRING_POSTPAID`. This page is the authoritative reference for the full set of 8 values.

## Raw Sources

- [[paypal-checkout-recurring-payments-module]] — verbatim webpage content with full API request/response samples

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-vault]] — PayPal Vault / Payment Method Tokens concept
- [[recurring-payments]] — Recurring payments concept
- [[source-paypal-checkout-recurring-payment]] — technical integration guide (basic vault flow)
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
