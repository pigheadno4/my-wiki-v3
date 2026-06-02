---
title: "Stripe: SEPA Direct Debit Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-sepa-debit-2025.md"
tags: [stripe, sepa, sepa-debit, eu, eur, iban, bank-debit, mandates, disputes, radar]
---

## Summary

Reference page for SEPA Direct Debit on Stripe. EUR-only bank debit for the SEPA region (Core scheme — both personal and business accounts). Covers settlement, debit notifications, Connect/Creditor ID, mandates, failure codes, disputes, refunds, and Radar integration.

## Key Details

**Limits**: 10,000 EUR per transaction; 10,000 EUR weekly for new users.

**Settlement**: T+6 payment success and funds available; cutoff 10:30 CET. 5-business-day refusal window after submission; most failures occur during this window.

**Business locations**: 40 countries (AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, GR, HK, HR, HU, IE, IT, JP, LI, LT, LU, LV, MT, MX, NL, NO, NZ, PL, PT, RO, SE, SG, SI, SK, US).

**Mandates**: SEPA Core scheme. Collect customer name + IBAN, present mandate for acceptance. Mandate ID accessible via `payment_method_details.sepa_debit.mandate` on Charge. Stripe learns of cancellations only when a payment fails → sets `inactive` + `mandate.updated` webhook.

**Debit notification emails**: Required by SEPA rulebook before each debit. Stripe sends automatically (using Stripe Creditor ID, always auto-sent). Custom emails must include: last 4 digits of account, mandate reference (`sepa_debit[reference]`), amount, Creditor ID, your contact info. Standard lead: 14 days; Stripe mandate allows as close as 2 days.

**Creditor ID**: Default is Stripe Creditor ID. Creditor Name priority: (1) business name, (2) custom statement descriptor, (3) default Stripe name. EU-based businesses recommended to use own Creditor ID to reduce disputes. Cannot change after live payments collected. Connect: Direct + `on_behalf_of` charge types use connected account's Creditor ID.

**Connect**: Requires `sepa_debit_payments` capability on connected accounts.

**Failure codes**: 12 codes including `refer_to_customer`, `insufficient_funds`, `debit_disputed`, `authorization_revoked`, `debit_not_authorized`, `account_closed`, `bank_account_restricted`, `debit_authorization_not_match`, `recipient_deceased`, `branch_does_not_exist`, `incorrect_account_holder_name`, `invalid_account_number`, `generic_could_not_process`.

**Disputes**:
- Up to 8 weeks: "no questions asked", automatically honored
- 8 weeks to 13 months: unauthorized debit only; Stripe provides mandate on request; not guaranteed to win
- `charge.dispute.created` webhook; dispute fee varies by settlement currency
- Final and uncontestable — must resolve directly with customer

**Refunds**: Up to 180 days; 3–4 business days to process; arrive within 5 business days. Recommended: wait 7 business days before refunding (ensures refusal window passed). Risk of double-credit if customer disputes after refund. New accounts may have refunds temporarily disabled (up to 2-day review).

**Radar**: Provides real-time ML fraud protection for SEPA, trained specifically for SEPA.

## Raw Sources

- [[stripe-sepa-debit-2025]] — verbatim webpage content; reuses 3 generic flow SVGs from `raw/assets/stripe-acss-debit-*.svg`
