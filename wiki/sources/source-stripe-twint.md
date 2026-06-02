---
title: "Stripe: TWINT Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-twint-2025.md"
tags: [stripe, twint, switzerland, chf, bank-redirect, recurring, disputes, connect, onboarding]
---

## Summary

Reference page for TWINT on Stripe. Switzerland-only, CHF, customer-initiated with two flows (mobile redirect or desktop QR). Supports recurring payments and disputes (rare). Max 5,000 CHF. Strict onboarding requirements and termination rights.

## Key Details

- **Customers**: Switzerland only; **Currency**: CHF; **Business**: 36 countries (European focus)
- **Max amount**: 5,000 CHF per transaction
- **Recurring**: Yes (notable for a bank redirect)
- **Disputes**: Yes — rare (25–50 per 1,000,000 transactions)
- **Refunds**: 180 days; full and partial; multiple partial refunds allowed
- **ECE**: not supported

**Two payment flows**:
1. **Mobile**: redirect to TWINT app → authorize → return
2. **Desktop**: QR code displayed on website → customer scans with TWINT app → authorize

**Onboarding requirements** (must comply *before* requesting access):
- Functional public website (not password protected)
- Legal notice/T&C showing: company name/legal form, full address, contact (email or phone)
- CHF prices displayed; Switzerland as shipping destination for physical goods
- Capability stays `pending` until verified

**Termination rights**: TWINT can suspend/terminate for non-compliance.

**Connect**: `twint_payments` capability; Direct, Destination, Separate charges supported.

## Raw Sources

- [[stripe-twint-2025]] — verbatim webpage content
