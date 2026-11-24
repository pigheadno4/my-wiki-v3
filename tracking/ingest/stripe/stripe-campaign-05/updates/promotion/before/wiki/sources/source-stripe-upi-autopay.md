---
title: "Stripe: Recurring Payments (UPI AutoPay)"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-upi-autopay-2025.md"
tags: [stripe, real-time-payments, upi, india, inr, upi-autopay, e-mandate, recurring, rbi, afa, pre-debit]
---

## Summary

Overview of UPI AutoPay (e-mandate) mechanics, RBI regulatory requirements, and mandate customization. 24-hour pre-debit notification required. Stripe handles pre-debit notifications and initial charge automatically.

## Key Details

**RBI requirements** (mandatory):
1. **AFA (Additional Factor Authentication)**: customer must enter UPI PIN to authorize each mandate setup
2. **Pre-debit notification**: at least **24 hours** before each charge, customer receives SMS/app notification with exact amount + cancellation option — Stripe sends automatically

**Initial payment**: can charge up to **5 minutes** after mandate setup. SetupIntent path: Stripe debits then immediately refunds (avoids AFA on initial setup).

**Subsequent payments**: Stripe auto-sends pre-debit notification → waits 24 hours → charges. No merchant action required.

**Mandate customization** via `payment_method_options.upi.mandate_options`:

| Field | Default |
| --- | --- |
| `description` | `Subscription` |
| `amount` | 1,500,000 paise (15,000 INR max) |
| `amount_type` | `maximum` |
| `end_date` | 10 years (scheme max: 40 years) |

**Adaptive Pricing**: Stripe auto-creates e-mandate in local currency — do NOT pass mandate-specific params.

## Raw Sources

- [[stripe-upi-autopay-2025]] — verbatim webpage content (49 lines); no italic fixes needed
