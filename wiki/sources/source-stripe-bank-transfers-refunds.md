---
title: "Stripe: Refund Bank Transfer Payments"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-bank-transfers-refunds-2025.md"
tags: [stripe, bank-transfers, refunds, customer-balance, payments]
---

## Summary

Four refund flows for bank transfer payments: payment → customer bank, payment → customer cash balance, cash balance → customer bank, and canceling pending refunds. Covers refund status lifecycle, constraints, international wire limitation, and test helpers.

## Key Details

**Four refund flows**:
1. **Payment → customer bank**: Stripe requests bank details via email; customer has 45 days to respond. Fee may apply per refund.
2. **Cancel pending payment refund**: cancel while still in `requires_action` via `stripe.refunds.cancel({ refund: id })`.
3. **Payment → customer cash balance**: immediate, free. `stripe.refunds.create({ payment_intent, destination: 'customer_balance' })`.
4. **Cash balance → customer bank**: `stripe.refunds.create({ amount, currency, customer, origin: 'customer_balance', instructions_email? })`.

**Refund status lifecycle**:

| Event | Status |
| --- | --- |
| Refund created | `requires_action` |
| Customer submits bank details | `pending` |
| Funds arrive at bank | `succeeded` |
| Bank rejects transfer | `requires_action` |
| 45 days without bank details | `failed` → `refund.failed` event |
| Canceled from `requires_action` | `canceled` |

**Constraints**:
- Customer email required (or specify `instructions_email` in API call)
- 45-day window for customer to submit bank details
- 180-day refund window from payment creation
- International (SWIFT) refunds: **not supported** — manual process

**Cash balance refund API**: `stripe.refunds.create({ amount, currency, customer: CUSTOMER_ID, origin: 'customer_balance' })`

**Test helper**: `POST /v1/test_helpers/refunds/{id}/expire` — simulate 45-day expiry. Test bank accounts provided per region.

## Raw Sources

- [[stripe-bank-transfers-refunds-2025]] — verbatim webpage content (270 lines); downloaded 5 CDN images to `raw/assets/`
