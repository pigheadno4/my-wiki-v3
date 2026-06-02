---
title: "Stripe: Pre-Authorized Debit Payments in Canada (ACSS)"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-acss-debit-2025.md"
tags: [stripe, acss, acss-debit, canada, cad, bank-debit, mandates, pad, disputes]
---

## Summary

Reference page for Canadian pre-authorized debits (PADs) on Stripe via ACSS. Covers settlement, mandates, payment schedules, disputes, refunds, statement descriptors, and Connect. Business accounts in CA and US can accept PADs from Canadian bank account holders.

## Key Details

**Currency**: CAD (primary); USD supported but risky — most banks can't process cross-currency debits, results in delayed failure.

**Settlement**: T+4 payment success, T+5 funds available; cutoff 17:00 US/Eastern.

**Verification**: instant bank verification via Stripe-hosted flow, or microdeposits (rare fallback). Verification required.

**Mandates (PAD agreements)**: governed by Payments Canada Rule H1. Requires institution number, transit number, account number, name, email. First debit initiated immediately after mandate acceptance. Mandate confirmation email must be sent ≤5 days after acceptance.

**Payment schedules** (mandatory per mandate):

| Schedule | Use case |
| --- | --- |
| `interval` | Predictable debits — specific dates, regular basis, or trigger events (with `interval_description`) |
| `sporadic` | Infrequent/irregular; requires express customer authorization at time of payment |
| `combined` | Both interval and sporadic debits |

**Transaction type**: `personal` or `business` (required on each mandate).

**`default_for`**: set to `['invoice', 'subscription']` for Invoicing/Subscriptions reuse without new mandate.

**Debit notification emails**: required by Payments Canada — mandate confirmation + pre-debit notice before each charge. Stripe sends automatically; can opt-out for custom emails (all types must be supported, not just one).

**Disputes**:
- Personal accounts: up to 90 calendar days, "no questions asked"
- Business accounts: up to 10 business days
- Final and uncontestable — Stripe sends both `charge.dispute.created` and `charge.dispute.closed` simultaneously

**Transaction failures**: can fail post-confirmation (insufficient funds, invalid account, debits disabled). If PaymentIntent already `succeeded`, failure creates dispute with reason `insufficient_funds`, `incorrect_account_details`, or `bank_cannot_process`. Stripe charges a failure fee.

**Refunds**: 180-day window; ~3 business days. Labeled as credit, not refund, on bank statement. Risk of double-credit if customer also disputes while refund is in flight.

**Statement descriptors**: truncated to 15 alphanumeric chars. Dynamic via `statement_descriptor` on PaymentIntent. `on_behalf_of` causes merchant name to come from connected account.

**Product support**: Connect, Checkout (not subscription mode), Subscriptions, Invoicing, Elements (PaymentIntent path only; not Checkout Sessions API; not ECE/Mobile PE).

**Billing Retries** (private preview): auto-retry for insufficient funds on subscription/one-off invoices.

## Raw Sources

- [[stripe-acss-debit-2025]] — verbatim webpage content; 3 flow diagram SVGs in `raw/assets/`
