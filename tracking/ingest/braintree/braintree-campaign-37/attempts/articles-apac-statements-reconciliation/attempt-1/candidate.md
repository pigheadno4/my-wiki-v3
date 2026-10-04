---
title: "Braintree APAC Statements and Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/apac/statements-reconciliation"
raw_files:
  - "braintree/articles/apac/statements-reconciliation-2026-09-16.md"
tags: [braintree, apac, statements, reconciliation, reporting]
---

## Overview

This collected Braintree APAC article documents monthly statements, their summary and fee sections, Daily Disbursement Details, the daily APAC Transaction Detail Report, and a fee-qualified method for reconciling report totals with bank-account deposits.

This is a 2026-09-16 Braintree-hosted snapshot for the article's APAC scope, not current account eligibility, independent bank authority, an Australian transfer guide, a current bank timing guarantee, or proof that a particular transaction or deposit settled or arrived. Keep its currency, pricing, fee, cutoff, and disbursement-timing statements within the captured account and document scope.

## Key takeaways

- The article says the previous month's statement becomes available on the fourth day of each month. Statement access uses the Control Panel Reports area, and users who cannot access or see it need the `View Statements` role permission.
- Statement sections summarize disbursement activity, processing counts, and charged fees. The Fee Details section includes discount-based Braintree fees and credits, chargeback fees, authorization fees, and other adjustments. Its authorization-fee calculation cutoff is 2:45 a.m. HKT on the second-to-last day of the month; later authorizations are billed the following month.
- Daily Disbursement Details amounts are shown in the account's settlement currency. The captured article describes the disbursement date as generally two to three days after transaction creation and one day before the APAC Transaction Detail Report settlement date; when daily debits exceed credits, Total Disbursed is zero and the negative balance rolls to the next day. These are article-level timing and balance descriptions, not a current bank guarantee or deposit proof.
- The daily APAC Transaction Detail Report lists transactions and chargebacks by settlement batch and settlement date, including currency, card type, and associated fees. For reconciliation, the article directs the merchant to pull the report for the date funds were disbursed. Access requires the `Create, Run, and Download Reports` role permission.
- The article's daily reconciliation method compares sale and chargeback amounts with account deposits and says settlement amounts less fees and chargeback amounts should match the deposit. The report's Fees column covers transaction fees only: it excludes authorization and chargeback fees, and chargebacks therefore show a zero fee in that report. The article routes chargeback-fee calculation to the flat chargeback fee for the applicable currency and says the first disbursement of the month also requires subtracting statement-listed authorization fees. Do not transfer that fee arithmetic to a different pricing or account arrangement without account-specific confirmation.

> [!warning] APAC snapshot and account scope
> Preserve the captured APAC account, settlement-currency, pricing, fee-cutoff, and timing context. This page does not establish Australian transfer mechanics, current eligibility, current independent bank policy, or a bank-arrival guarantee.

> [!warning] Reconciliation is not deposit proof
> Matching statement or report values to a bank-account entry is a reconciliation method. It does not prove that a particular transaction settled or that a specific deposit reached the account.

## Detail locators

- Monthly statement availability, Control Panel path, and `View Statements` permission: `## Statements`, raw lines 17-28.
- Disbursement Summary, Processing Summary, and Fee Details purposes: raw lines 33-52.
- Authorization-fee cutoff and following-month billing: raw line 54.
- Settlement-currency qualification, disbursement fields, general date relationship, and negative-balance rollover: `### Daily Disbursement Details`, raw lines 57-70.
- Daily reconciliation description and funding-descriptor example: `## Reconciliation`, raw lines 73-79.
- APAC Transaction Detail Report contents, settlement-date organization, same-disbursement-date instruction, permission, and download path: `### Downloading the APAC Transaction Detail Report`, raw lines 82-93.
- Reconciliation arithmetic, transaction-fee-only limitation, chargeback-fee treatment, currency-qualified flat-fee route, and monthly statement route: `### Daily reconciliation`, raw lines 96-100.
- First-disbursement authorization-fee adjustment: raw lines 103-104.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/apac/statements-reconciliation-2026-09-16|Braintree APAC Statements and Reconciliation article]] - complete collected snapshot covering monthly statements, settlement-currency disbursement details, the APAC Transaction Detail Report, and fee-qualified daily reconciliation
