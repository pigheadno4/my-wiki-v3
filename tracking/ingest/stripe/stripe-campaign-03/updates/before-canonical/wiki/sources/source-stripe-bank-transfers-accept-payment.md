---
title: "Stripe: Accept a Bank Transfer"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-bank-transfers-accept-payment-2025.md"
tags: [stripe, bank-transfers, payment-intents, customer-balance, webhooks, checkout, reconciliation]
---

## Summary

End-to-end integration guide for accepting bank transfer payments via Elements (PaymentIntents) and Checkout. Covers underpayment/overpayment handling, PaymentIntent lifecycle events, reconciliation modes, payment instruction emails, and testing.

## Key Details

**Prerequisites**: must associate a Customer object — bank transfers unavailable on PaymentIntents without a customer.

**PaymentIntent creation** — `payment_method_types: ['customer_balance']` with:

| Region | `bank_transfer.type` | Notes |
| --- | --- | --- |
| US | `us_bank_transfer` | |
| UK | `gb_bank_transfer` | |
| EU | `eu_bank_transfer` + `country: 'FR'` | IBAN localized to customer's country; ES unavailable |
| JP | `jp_bank_transfer` | requires `return_url` |
| MX | `mx_bank_transfer` | requires `return_url` |

Or use `automatic_payment_methods: { enabled: true }` (recommended; handles method selection automatically).

If customer balance already covers amount → PaymentIntent immediately `succeeded`.

**PaymentIntent status lifecycle**:

| Event | Status | Description |
| --- | --- | --- |
| `payment_intent.requires_action` | `requires_action` | Balance insufficient; instruct customer to send transfer with `amount_remaining` |
| `payment_intent.partially_funded` | `requires_action` | Partial payment received; instruct customer to send remaining amount |
| `payment_intent.succeeded` | `succeeded` | Payment complete |

Partially funded PaymentIntents aren't reflected in account balance until complete. Can update `amount` and re-confirm to accept partial payment.

**Reconciliation**: automatic by default (uses reference code + amount). Override per customer: `cash_balance.settings.reconciliation_mode = 'manual'`.

**Underpayment**: PaymentIntents partially funded; invoices remain open until full amount received.
**Overpayment**: excess kept in customer cash balance.

**Payment instruction emails**: enable from Dashboard → sent when balance insufficient at confirmation or when transfer doesn't cover pending payments.

**Checkout constraints**: payment mode only (no subscription/setup); single currency; one-time line items only; customer must be specified in session; delayed notification method.

**Testing** — simulate incoming transfer:

```bash
# API
POST /v1/test_helpers/customers/{id}/fund_cash_balance
  -d reference=REF-4242 -d amount=1000 -d currency=usd

# CLI
stripe test_helpers customers fund_cash_balance {CUSTOMER_ID} \
  --amount=1099 --reference=DVGBG97TZ6ZV --currency=usd
```

**Live mode**: each customer gets unique virtual bank account details. Test mode uses invalid (non-unique) details.

## Raw Sources

- [[stripe-bank-transfers-accept-payment-2025]] — verbatim webpage content (2180 lines); fixed 12× `_italic_` → `*italic*`; downloaded 3 CDN SVG diagrams to `raw/assets/`
