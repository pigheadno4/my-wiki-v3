---
title: "PayPal Checkout: Save Payment Methods for Recurring Payments"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-save-payment-methods-recurring.md"
tags: [paypal, checkout, recurring-payments, vault, rba, billing-plan, orders-api, usage-pattern, stored-credential, implementation-guide]
---

## PayPal Checkout: Save Payment Methods for Recurring Payments

The most detailed technical reference in the wiki for implementing recurring billing agreements (RBAs) using PayPal's vaulting-with-purchase flow. Covers field-level schema, 7 use case samples, implementation constraints, and error handling.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/save-payment-methods-for-recurring-payments/>

Last updated: 2025-08-11

## Key Takeaways

### Integration model: single-stage vaulting with purchase

PayPal's vaulting-with-purchase is a **single-stage process** — the initial purchase and vault token creation happen in one Create Order call. Only use the Orders v2 API (`POST /v2/checkout/orders`). Do not call APIs directly from the browser/client-side.

### `usage_pattern` field locations

| Scenario | Field path |
| -------- | ---------- |
| Initial purchase (token creation) | `payment_source.paypal.attributes.vault.usage_pattern` |
| Subsequent merchant-initiated charge | `payment_source.paypal.stored_credential.usage_pattern` |

### RBA plan data structure

Three components, all passed in the Create Order call:

1. **Plan name** — `purchase_units.items[].billing_plan.name` (max 127 chars; use customer-friendly names, not internal IDs/SKUs)
2. **Billing cycles** — `purchase_units.items[].billing_plan.billing_cycles[]` (up to 3; at least 1 must be REGULAR tenure)
3. **One-time charges** — `purchase_units.items[].billing_plan.setup_fee` + product items

### Items array structure

- Billing Plan item goes in `items[0]` with `name: "Billing Plan"`
- Product items (e.g. iPhone) go in `items[1]` (only 1 product item supported)
- **Only one `billing_plan` per order** — multiple billing plans not supported

### vault configuration required fields

```json
"payment_source.paypal.attributes.vault": {
    "store_in_vault": "ON_SUCCESS",
    "usage_type": "MERCHANT",  // or "PLATFORM"
    "usage_pattern": "SUBSCRIPTION_PREPAID"
}
```

### Billing cycle key rules

| Rule | Detail |
| ---- | ------ |
| Min regular cycles | At least 1 `tenure_type: REGULAR` required |
| Max billing cycles | 3 |
| `start_date` | Omit if billing cycle starts on creation date; only 1 cycle with `sequence=1` can have null start date |
| `total_cycles: 0` | Means infinite (no end date) |
| `pricing_model` | `FIXED`, `VARIABLE`, or `AUTO_RELOAD` (AUTO_RELOAD only for unscheduled) |

### Amount calculation rules

- Add plan price to total order amount when plan starts on creation date
- Unsupported breakdown fields: `handling`, `discount`, `shipping_discount`, `insurance`
- `purchase_units.amount.value` must equal sum of all item amounts + shipping + tax

### `stored_credential` for subsequent charges

| Field | Values | Notes |
| ----- | ------ | ----- |
| `payment_initiator` | `MERCHANT` / `CUSTOMER` | MERCHANT for merchant-initiated; CUSTOMER for payer-present |
| `usage` | `SUBSEQUENT` (recommended), `FIRST`, `DERIVED` | Use SUBSEQUENT for all recurring charges after initial |
| `usage_pattern` | any valid pattern | Same pattern as initial setup |

**Important**: `stored_credential` must also be included in Capture, Authorize, and Confirm API calls for multi-step integrations.

### Billing plan support matrix

| Usage pattern | Trial cycle | Auto reload |
| ------------- | ----------- | ----------- |
| SUBSCRIPTION | Yes | No |
| RECURRING | Yes | No |
| INSTALLMENT | Yes | No |
| UNSCHEDULED_PREPAID | No | Yes |
| UNSCHEDULED_POSTPAID | No | Yes |

### Unsupported patterns (avoid)

- Multiple items with `billing_plan` in `purchase_units.items[]`
- Multiple `purchase_units` in a single order
- `billing_plan` quantity > 1
- Multi-step order creation (must be single-step)
- Billing plan data in PATCH operations
- Setup/product price fields in Confirm, Authorize, or Capture operations

### 7 use cases with paysheet screenshots

| Use case | Key config | Image |
| -------- | ---------- | ----- |
| Subscription | 1 REGULAR cycle, `SUBSCRIPTION_PREPAID` | `paypal-rba-use-case-subscription.png` |
| Subscription with trial | TRIAL + REGULAR cycles, `SUBSCRIPTION_PREPAID` | `paypal-rba-use-case-subscription-trial.png` |
| Future start date + setup fee | Future `start_date` on REGULAR cycle, setup_fee | `paypal-rba-use-case-setup-fee.png` |
| Default subscription | Minimal config, billing plan inside item | `paypal-rba-use-case-default-sub.png` |
| Early cancellation fees | `SUBSCRIPTION_POSTPAID` | `paypal-rba-use-case-early-cancellation.png` |
| Multiple rates | 2 cycles (TRIAL → REGULAR), `INSTALLMENT_PREPAID` | `paypal-rba-use-case-multiple-rates.png` |
| Auto-reload plan | `AUTO_RELOAD` pricing_model, `reload_threshold_amount`, `UNSCHEDULED_PREPAID` | `paypal-rba-use-case-auto-reload.png` |

### Common 422 error

Missing vault credentials in subsequent transaction — ensure `billing_agreement_id` or `vault_id` is present with `stored_credential` in all subsequent requests.

## Images

- `raw/assets/paypal-rba-use-case-subscription.png`
- `raw/assets/paypal-rba-use-case-subscription-trial.png`
- `raw/assets/paypal-rba-use-case-setup-fee.png`
- `raw/assets/paypal-rba-use-case-default-sub.png`
- `raw/assets/paypal-rba-use-case-early-cancellation.png`
- `raw/assets/paypal-rba-use-case-multiple-rates.png`
- `raw/assets/paypal-rba-use-case-auto-reload.png`

## Raw Sources

- [[paypal-checkout-save-payment-methods-recurring]] — full verbatim content with field reference tables and 7 use case code samples

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-vault]] — PayPal Vault / Payment Method Tokens concept
- [[recurring-payments]] — Recurring payments concept
- [[source-paypal-checkout-recurring-payments-module]] — companion reference for `usage_pattern` taxonomy and billing plan overview
- [[source-paypal-checkout-pass-line-items]] — related: items[] structure and amount breakdown constraints
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
