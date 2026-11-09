---
title: "Stripe: ACH SEC Codes Overview"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-ach-sec-codes-2025.md"
tags: [stripe, ach, us-bank-account, sec-codes, mandates, nacha, web, ccd, ppd, tel]
---

## Summary

Overview of Standard Entry Class (SEC) codes for ACH Direct Debit. SEC codes describe how a customer authorized an ACH transaction and are defined by Nacha. Stripe supports four SEC codes; businesses are responsible for specifying the correct code.

## Key Details

**Defaults**: WEB for consumer accounts, CCD for business accounts (when no collection method specified).

| Code | Stands for | Used when | Notes |
| --- | --- | --- | --- |
| WEB | Internet Initiated or Mobile Entry | Internet or mobile-initiated consumer transactions | Default for consumers; refunds use PPD |
| CCD | Corporate Credit or Debit Entry | Business-to-business payments | Applied to all `account_holder_type=company` PaymentMethods |
| PPD | Prearranged Payment and Deposit | Written/signed standing or single-entry consumer authorization | Requires `mandate_data.customer_acceptance.type: 'offline'` + `collection_method: 'paper'` |
| TEL | Telephone-Initiated Entry | Telephone-authorized consumer transactions | Private beta; single entries only; existing relationship required |

**PPD integration**: confirm PaymentIntent or SetupIntent with `mandate_data.customer_acceptance.type: 'offline'` and `payment_method_options.us_bank_account.mandate_options.collection_method: 'paper'`.

**TEL requirements**:
- Existing relationship (written agreement, or purchase within 2 years, or customer-initiated call)
- Commercially reasonable identity and routing number verification
- Explicit oral authorization captured via audio recording or written notice sent *before* first debit
- Specific oral authorization script required (name, amount, date, bank details, cancellation instructions)
- Single entries only — not for recurring or standing authorizations

## Raw Sources

- [[stripe-ach-sec-codes-2025]] — verbatim webpage content
