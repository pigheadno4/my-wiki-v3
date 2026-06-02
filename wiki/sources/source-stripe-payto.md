---
title: "Stripe: PayTo Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-payto-2025.md"
tags: [stripe, real-time-payments, payto, australia, aud, mandates, recurring, billing, connect, disputes]
---

## Summary

Overview of Stripe's PayTo — Australia-only mandate-based real-time payment method supporting one-time and recurring payments. Unique among real-time methods: supports disputes (final, non-appealable), Billing, and recurring. Identity verification required to activate.

## Key Details

**API enum**: `payto`. AUD only. AU merchant accounts only. **Identity verification required** before activation.

**Payment flows**: PayID (unique identifier linked to bank account) or Account + BSB numbers. Customer receives push notification or email to authorize mandate in banking app.

**Delayed notification**: Stripe sends final status within 60 seconds of mandate authorization (not immediate).

**Mandates** via `payment_method_options.payto.mandate_options`:
- `amount`, `amount_type` (`fixed` or `maximum`), `payment_schedule`, `purpose`, `start_date`, `end_date`, `payments_per_period`
- One-off: Stripe auto-sets all fields. Recurring: merchant specifies least permissive terms
- `purpose` inferred from MCC; can be overridden

**Bank limits**: ANZ, CBA, Westpac, Macquarie reject mandates over 25,000 AUD and mandates with no maximum amount. Westpac additionally declines high-risk merchant ad-hoc payments over 1,000 AUD. Business account coverage is lower than consumer coverage. 44 supported banks listed.

**Disputes**: Yes — **final and non-appealable** (unlike card disputes). Stripe sends `charge.dispute.created` and `charge.dispute.closed` events. Merchant must contact customer directly to resolve.

**Refunds**: Up to 2 years. Typically minutes; some banks may take several days.

**Billing**: Yes (supports subscriptions and invoices). Recurring payments: Yes. Whether `charge_automatically` is supported (unlike other real-time methods) requires verification against the accept-a-payment guide.

**Connect**: Direct, Destination, Separate charges and transfers. Capability: `payto_payments`.

**Product support**: Checkout Sessions, Payment Element, Direct API, Billing, Payment Links.

## Raw Sources

- [[stripe-payto-2025]] — verbatim webpage content (180 lines); fixed `*merchant category code (MCC)*` ×1, `*webhook*` ×1
