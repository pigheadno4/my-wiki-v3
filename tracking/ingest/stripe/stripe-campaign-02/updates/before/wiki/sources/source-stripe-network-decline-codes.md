---
title: "Stripe Network Decline Codes"
type: source
date_ingested: 2026-05-09
original_format: webpage
raw_files:
  - "stripe-network-decline-codes-2026.md"
tags: [stripe, declines, network-codes, ach, becs, bacs, sepa, cash-app-pay, bank-debit, direct-debit]
---

## Summary

Reference tables mapping raw network/bank decline codes to Stripe decline codes for 7 payment methods. Covers bank debit methods (ACH, BECS, Bacs, SEPA, Canadian PAD) and Cash App Pay.

## Payment Methods Covered

| Payment Method | Code format | Notes |
| --- | --- | --- |
| ACH Direct Debit | `R01`–`R31` format | 7 codes |
| Australia BECS Direct Debit | `1`–`9` numeric | 8 codes |
| Bacs Direct Debit | Alpha/numeric | 3 sub-tables: ADDACS (mandate cancellations), ARUDD (payment returns), AUDDIS (mandate setup failures) |
| Cash App Pay | `PAYMENT_*` descriptive strings | 10 codes; 2-column table only (no explanation) |
| NZ BECS Direct Debit | `1`–`9` numeric | Same structure as AU BECS |
| Pre-authorized debit (Canada) | `900`–`915` numeric | 9 codes |
| SEPA Direct Debit | `AC*`, `MD*`, `RR*` etc. | 11 codes including SEPA-specific failure codes |

## Common Failure Codes Across Methods

| Stripe decline code | Meaning | Typical resolution |
| --- | --- | --- |
| `insufficient_funds` | Account lacks funds | Verify funds, retry |
| `account_closed` | Bank account closed | Get new account details |
| `debit_not_authorized` | No valid mandate | Collect new mandate |
| `recipient_deceased` | Account holder deceased | Verify customer status |
| `refer_to_customer` | Unspecified failure, no reason code from bank | Contact customer |
| `generic_could_not_process` | Unspecified internal failure | Contact Stripe Support |

## SEPA-Specific Codes

| Code | Stripe failure code | Meaning |
| --- | --- | --- |
| `MD02`, `BE05` | `debit_authorization_not_match` | Missing/incorrect mandate info |
| `MD06` | `debit_disputed` | Customer requested refund via bank |
| `RC01` | `branch_does_not_exist` | IBAN branch doesn't exist |
| `RR01–RR03` | `incorrect_account_holder_name` | Name/address mismatch |
| `AC13` | `generic_could_not_process` | Unidentified failure |

## Cash App Pay Codes

Raw codes are descriptive strings (e.g. `PAYMENT_DECLINED_RISK`, `PAYMENT_DECLINED_COMPLIANCE`). See [Cash App Pay error code reference](https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-code-reference#payment-processing-errors) for details.

## Related Pages

- [[stripe-declines]] — concept page (updated with network codes reference)
- [[source-stripe-decline-codes]] — Stripe decline codes (card + LPM)
- [[source-stripe-declines-overview]] — top-level declines overview

## Raw Sources

- [[stripe-network-decline-codes-2026]] — verbatim Stripe network decline codes reference page
