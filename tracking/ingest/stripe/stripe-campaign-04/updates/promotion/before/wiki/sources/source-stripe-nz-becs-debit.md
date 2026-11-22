---
title: "Stripe: New Zealand BECS Direct Debit Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-nz-becs-debit-2025.md"
tags: [stripe, nz-becs, becs, new-zealand, nzd, bank-debit, mandates, disputes]
---

## Summary

Reference page for New Zealand BECS Direct Debit on Stripe. NZ-only bank debit requiring a mandate (DDA). Covers settlement, mandates, email notification requirements, disputes, and refunds. API enum: `nz_bank_account`.

## Key Details

**Settlement**: T+2 payment success and funds available; cutoff 18:20 Pacific/Auckland.

**Mandates (DDAs)**: Direct Debit Authorities. Require account holder name, email, bank account number + NZ BECS Direct Debit Service T&C agreement. Customer can cancel via bank or merchant → new mandate required.

Mandate event: `mandate.updated` fires when canceled or permanently failed → `status` becomes `inactive`.

**Email notification requirements** (mandatory):
- **Mandate confirmation**: within 5 days of establishing mandate. Must include: mandate date, Stripe NZ Limited (auth code 3143978) statement, link to NZ Direct Debit Service T&Cs, bank name, account number, account name, signatory name (if different), your contact info (address, email, phone).
- **Pre-debit notification**: on the day of every PaymentIntent confirmation. Must include: payment amount, Stripe NZ Limited debit statement, debit date, "Stripe New Zealand Limited" bank statement notice, your contact info.

Custom emails require contacting Stripe support (cannot self-serve disable).

**Disputes**:
- Up to 9 months if customer isn't satisfied the DDA authorizes the debit
- Up to 120 days if pre-debit notification wasn't sent, or amount/date differs from notification
- `charge.dispute.created` event fired; Stripe immediately removes funds

**Refunds**: 90-day window; 3–5 business days to process. Labeled as credit (not refund) on bank statement. Risk of double-credit if refund issued while dispute in flight.

**Product support**: Connect, Checkout, Payment Links, Subscriptions, Invoicing, Elements (all — no ECE restriction mentioned).

**Billing Retries** (private preview): auto-retry for insufficient funds on subscription or one-off invoices.

## Raw Sources

- [[stripe-nz-becs-debit-2025]] — verbatim webpage content; reuses 3 generic flow SVGs from `raw/assets/stripe-acss-debit-*.svg`
