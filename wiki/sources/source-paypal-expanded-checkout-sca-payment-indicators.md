---
title: "PayPal Expanded Checkout: SCA Payment Indicators"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-sca-payment-indicators.md"
tags: [paypal, expanded-checkout, sca, stored-credential, recurring-payments, card-on-file, payment-initiator, psd2, orders-api]
---

## PayPal Expanded Checkout: SCA Payment Indicators

Reference for the `stored_credential` object in the Orders v2 API — the mechanism for providing SCA/PSD2 context on card-on-file and recurring payments. Includes full value tables and 11 use case scenarios across one-time, recurring, and unscheduled payment types.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/sca-payment-indicators/>

Last updated: 2024-12-03

## Key Takeaways

### What it is

`stored_credential` is a nested object under `payment_source.card` in the Orders v2 Create Order request. It tells PayPal (and card networks) the context of a card-on-file transaction — who initiated it, what type it is, and whether it's a first or subsequent use of saved credentials. Required for SCA-regulated markets (PSD2/Europe) to avoid rejected transactions.

### The 4 fields

**`payment_initiator`** (Required)

| Value | When to use |
| ----- | ----------- |
| `CUSTOMER` | Buyer is present and initiating the payment |
| `MERCHANT` | Merchant initiates without buyer present; requires prior consent |

**`payment_type`** (Required)

| Value | Description |
| ----- | ----------- |
| `ONE_TIME` | Default when no `stored_credential` sent |
| `RECURRING` | Series of payments on a fixed time interval (variable amounts ok) |
| `UNSCHEDULED` | Merchant-initiated, not on fixed schedule (e.g. top-up when balance falls below threshold) |

**`usage`**

| Value | Description |
| ----- | ----------- |
| `FIRST` | Saving card/token for future use — collect buyer consent |
| `SUBSEQUENT` | Previously saved card/token being used |
| `DERIVED` | PayPal determines FIRST vs SUBSEQUENT from available data |

**`previous_transaction_reference`** — PayPal transaction ID from the original agreement. Proves an established contract with the payer.

**`previous_network_transaction_reference`** — For migrations from non-PayPal processors; provides the prior network transaction ID + network name.

**`network_transaction_reference`** — Card network reference (ID + NETWORK required; DATE optional). Returned in responses for use in future requests.

### Use case matrix

**One-time transactions:**

| Scenario | initiator | type | usage |
| -------- | --------- | ---- | ----- |
| Single payment, no save intent | CUSTOMER | ONE_TIME | DERIVED |
| Single payment, saving card | CUSTOMER | ONE_TIME | FIRST |
| Single payment, using saved card | CUSTOMER | ONE_TIME | SUBSEQUENT |

**Recurring / subscription:**

| Scenario | initiator | type | usage |
| -------- | --------- | ---- | ----- |
| Sign-up, card not yet saved | CUSTOMER | RECURRING | FIRST |
| Sign-up, card already saved | CUSTOMER | RECURRING | SUBSEQUENT |
| Subsequent recurring charge | MERCHANT | RECURRING | SUBSEQUENT |
| Migrating from non-PayPal processor | MERCHANT | RECURRING | SUBSEQUENT |

**Unscheduled (e.g. top-up):**

| Scenario | initiator | type | usage |
| -------- | --------- | ---- | ----- |
| Sign-up, card not yet saved | CUSTOMER | UNSCHEDULED | FIRST |
| Sign-up, card already saved | CUSTOMER | UNSCHEDULED | SUBSEQUENT |
| Subsequent unscheduled charge | MERCHANT | UNSCHEDULED | SUBSEQUENT |
| Migrating from non-PayPal processor | MERCHANT | UNSCHEDULED | SUBSEQUENT |

### Key patterns

- **Any merchant-initiated charge** (recurring or unscheduled) → `payment_initiator: MERCHANT` + `usage: SUBSEQUENT` + `previous_transaction_reference`
- **First save during checkout** → `payment_initiator: CUSTOMER` + `usage: FIRST`
- **Migration from another processor** → `payment_initiator: MERCHANT` + `usage: SUBSEQUENT` + `previous_network_transaction_reference`
- `DERIVED` is only valid for one-time customer-initiated payments with no save intent

## Raw Sources

- [[paypal-expanded-checkout-sca-payment-indicators]] — verbatim webpage content with full field tables and 11 use case scenarios

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[recurring-payments]] — recurring payments concept (stored_credential is central to merchant-initiated charges)
- [[paypal-vault]] — vault concept (payment tokens used with SUBSEQUENT usage)
- [[source-paypal-expanded-checkout-rtau]] — RTAU references this page for subsequent payment scenario examples
- [[source-paypal-expanded-checkout-customize-overview]] — full customization catalog
