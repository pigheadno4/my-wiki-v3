---
title: "Stripe: Bank Debits"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-bank-debits-2025.md"
tags: [stripe, bank-debits, ach, bacs, sepa, au-becs, nz-becs, acss, mandates]
---

## Summary

Overview of Stripe's 6 bank debit payment methods, with product and API support matrices. Bank debits pull funds directly from customer bank accounts. Confirmation takes several business days.

## 6 Methods and API Enums

| Method | API enum | Region |
| --- | --- | --- |
| ACH / Instant Bank Payments | `us_bank_account` | US |
| Bacs Direct Debit | `bacs_debit` | UK |
| AU BECS Direct Debit | `au_becs_debit` | Australia |
| NZ BECS Direct Debit | `nz_bank_account` | New Zealand |
| Pre-authorized debit (Canadian PADs) | `acss_debit` | Canada |
| SEPA Direct Debit | `sepa_debit` | EEA |

## Key Properties (all methods)

- No manual capture support; no redirect required
- Express Checkout Element: unsupported for all

## Notable Caveats

**Bacs**: PaymentIntents require mandate via Stripe-owned flow (Checkout/Payment Element/Payment Links); SetupIntents not supported via Payment Element — use Checkout setup mode.

**Canadian PADs**: not in Payment Links, Mobile Payment Element, Checkout subscription mode, or deferred intent creation.

**Use cases**: recurring B2B, large consumer payments (rent/tuition). **Not suitable** for immediate delivery (takes business days) or dispute-sensitive businesses.

## Raw Sources

- [[stripe-bank-debits-2025]] — verbatim webpage content (product support table, API support table, migration notes)
