---
title: "Braintree NAB Statements and Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/nab/statements-reconciliation"
raw_files:
  - "braintree/articles/nab/statements-reconciliation-2026-09-16.md"
tags: [braintree, nab, statements, reconciliation, reporting]
---

## Overview

This collected Braintree article documents monthly Transact and Merchant statements for the page's NAB account/processor scope, Control Panel access, pricing-dependent Merchant Statement sections, daily settlement-batch reconciliation, and monthly fee reconciliation.

This is a 2026-09-16 Braintree-hosted snapshot, not independent NAB authority, current account eligibility or policy, sibling account/processor guidance, or proof that a particular transaction settled or deposit arrived. The page states no region or currency.

## Key takeaways

- NAB generates a Transact Statement for per-transaction processing fees and a Merchant Statement for other merchant-service and interchange fees each month. Merchant Statements are available in the Control Panel by the ninth of each month; access requires the `View Statements` role permission. Transact Statements are not provided there, and the article routes access requests to Braintree support.
- Merchant Statement sections depend on the pricing model. The captured page describes IC+ card-brand service-fee and card-issuer-fee breakdowns, blended-pricing transaction value and rate totals including GST, an IC+-only interchange-category breakdown, daily and monthly trends, card-product activity, and a per-merchant-account-ID store summary.
- For debit and deposit reconciliation, the article directs merchants to compare the daily Settlement Batch Summary Report, organized by settlement date, with bank statements. It says settled funds should be deposited the next day when the business banking account is with NAB, while another bank may add delay. Because fees are debited at month end, it describes deposits as gross transaction amounts that should match the settlement batch exactly.
- Fees are deducted on the last business day of each month. The article includes chargeback fees, merchant-service and interchange percentages, and per-transaction fees, and directs merchants to compare the Merchant and Transact statement fees with the monthly bank-account fee debit.

> [!warning] Bank timing and reconciliation boundary
> The next-day wording is conditional on using NAB for the business banking account, and the page warns that another bank may add delay. Report-to-statement matching is a reconciliation method, not proof that a specific settlement or bank deposit completed.

## Detail locators

- Statement types, monthly Merchant Statement availability, Control Panel path, `View Statements` permission, and the separate Transact Statement support route: `## Statements`, raw lines 17-32.
- Pricing-model-dependent Merchant Statement sections and fields: `### Merchant Statements`, raw lines 37-78.
- Daily Settlement Batch Summary comparison, settlement-date organization, bank-dependent deposit delay, and gross-deposit matching: `## Reconciliation`, raw lines 81-87.
- Monthly fee-debit timing, included fee categories, statement comparison, and assistance route: `### Fee reconciliation`, raw lines 90-96.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/nab/statements-reconciliation-2026-09-16|Braintree NAB Statements and Reconciliation article]] - complete collected snapshot covering monthly statements, pricing-dependent fee sections, settlement-batch comparison, bank-dependent deposit timing, and monthly fee reconciliation
