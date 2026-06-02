---
title: "Stripe: Bank Transfer Payments"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-bank-transfers-2025.md"
tags: [stripe, bank-transfers, customer-balance, payments, ach, sepa, swift, wire, connect]
---

## Summary

Overview page for Stripe's bank transfer payment method. Covers the virtual account / customer balance model, business location eligibility by currency, international wires, refunds, funding instructions, sender information API, disputes, Connect support, and full product/API support tables.

## Key Details

**Model**: virtual bank account number → customer pushes funds → held in customer cash balance → reconciled to invoices/payments.

**Currencies**: EUR, GBP, JPY, MXN, USD. See concept page for business locations by currency.

**Customer balance**: unreconciled funds auto-returned at 75 days; swept to merchant Stripe balance at 90 days. EU EUR: beneficiary name must match registered business name exactly.

**API enum**: `customer_balance`. PaymentIntents only (no SetupIntents, no manual capture, no redirect).

**International wires** (US only): SWIFT, 3–5 business days, no refunds. USD only for US accounts.

**Refunds**: to customer bank account or back to cash balance. Requires bank account details (collected from transfer or via email).

**Disputes**: USD (ACH, ≤5 days) and CAD only. All other currencies irreversible.

**Sender info**: `stripe.customers.retrieveCashBalanceTransaction()` — `type: 'funded'` with region-specific fields (BIC/IBAN for EU, sort_code for GB, CLABE for MX, ACH/wire network for US).

**Connect**: all charge types; `on_behalf_of` unsupported; direct charges require capability activation.

**Unsupported**: Payment Links, International transfers, Express/Mobile Checkout Elements, Customer Portal.

## Raw Sources

- [[stripe-bank-transfers-2025]] — verbatim webpage content (409 lines); fixed `_Connect_` → `*Connect*`
