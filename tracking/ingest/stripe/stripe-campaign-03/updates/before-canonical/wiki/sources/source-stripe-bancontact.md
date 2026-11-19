---
title: "Stripe: Bancontact Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-bancontact-2025.md"
tags: [stripe, bancontact, belgium, eur, bank-redirect, sepa-debit, authenticated]
---

## Summary

Reference page for Bancontact on Stripe. Belgium-only bank redirect, EUR-only, customer-authenticated with immediate notification. No native recurring — recurring requires saving as SEPA Direct Debit. No disputes (customer authentication prevents chargebacks). 180-day refund window.

## Key Details

- **Customer locations**: Belgium only
- **Currency**: EUR
- **Confirmation**: Customer-authenticated (immediate notification)
- **Recurring payments**: Only via [[stripe-sepa-debit]] — Bancontact can be saved as a SEPA Direct Debit mandate for future recurring charges
- **Disputes**: No chargebacks (customer authentication prevents them)
- **Refunds**: Up to 180 days
- **Business locations**: 40 countries (same as SEPA)
- **Invoicing**: Invite-only; ECE: unsupported

**Two payment flows**:
1. Card/web: redirect to Bancontact site → enter credentials → immediate confirmation
2. Mobile app: QR code scan → enter PIN → immediate confirmation

## Raw Sources

- [[stripe-bancontact-2025]] — verbatim webpage content; 7 flow diagram SVGs in `raw/assets/`
