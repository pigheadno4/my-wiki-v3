---
title: "Braintree Moneris Pricing and Fees"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/moneris/pricing-fees"
raw_files:
  - "braintree/articles/moneris/pricing-fees-2026-09-16.md"
tags: [braintree, moneris, pricing, fees, chargebacks, reporting]
---

## Overview

This collected Braintree-hosted Moneris account-route article documents fee categories, account-selected blended and IC+ pricing models, operation-specific fee treatment, dispute fees, and statement/reporting routes. It is a 2026-09-16 snapshot of this exact Braintree documentation route, not independent Moneris API or policy authority, Braintree Orchestration documentation, a merchant-specific agreement, a numeric or currency-specific rate schedule, proof of current account eligibility, or payment, settlement, disbursement, or statement-delivery proof.

## Key takeaways

- The page defines a per-transaction fee, discount rate, combined Braintree processing fees, variable issuer-assessed interchange fees, and a fixed processing-bank chargeback fee. Depending on the account's pricing model, interchange may be separate or included in Braintree processing fees. The article states no currency or numeric rate.
- Braintree's discount rate applies only to successful transactions and is deducted from daily disbursements. The per-transaction fee applies to all transactions, including refunds, authorizations except $0 authorizations, voids, and gateway rejections. These are the page's exact operation qualifications; they do not prove an individual transaction succeeded, settled, or funded.
- The pricing model was determined when the merchant originally signed up for the account. Blended pricing combines a fixed discount rate and per-transaction fee. IC+ combines Braintree processing and variable interchange fees; exact fees depend primarily on card brand and also on card type, region, and other factors. No account-specific amount is supplied.
- Refunds incur the per-transaction fee and do not return the original transaction fees. A void also incurs the per-transaction fee, but the page says fees associated with voids will be returned at the beginning of the following month. Preserve that timing and wording rather than inferring an immediate credit or which fee components are included.
- A non-refundable chargeback fee applies to chargebacks and pre-arbitrations regardless of outcome; retrievals do not incur the fee "at this time." Moneris mails statements to the business address on file 3 to 5 business days after the beginning of each month only when transactions were processed, while the listed Control Panel summaries are described as accessible at any time. These snapshot statements are not delivery guarantees or current policy.

> [!warning] Account, currency, timing, and authority scope
> Keep pricing-model selection, operation coverage, void-fee return timing, retrieval-fee wording, and statement conditions within this captured Braintree Moneris route. The page supplies no numeric rate or currency. Do not transfer it to another account, processor, region, currency setup, Braintree Orchestration, or an independent/current Moneris service or policy.

## Detail locators

- Fee categories and the pricing-model condition for interchange treatment: `## Transaction fees`, raw lines 19-28.
- Successful-transaction discount-rate condition, daily-disbursement deduction, and all-transaction per-fee scope with the $0-authorization exception: `## Transaction fees`, raw line 30.
- Account-signup pricing-model selection and account-specific help route: `## Pricing models`, raw lines 33-35.
- Blended fixed-rate composition: `### Blended`, raw lines 38-40.
- IC+ composition, interchange variability and card-brand, card-type, and region factors: `### Interchange plus (IC+)`, raw lines 43-45.
- Refund fee treatment and non-return of original transaction fees: `## Refunds and voids`, raw line 50.
- Void fee treatment and beginning-of-following-month return timing: `## Refunds and voids`, raw line 52.
- Outcome-independent chargeback and pre-arbitration fee plus time-qualified retrieval exclusion: `## Chargebacks, retrievals, and pre-arbitrations`, raw lines 55-57.
- Conditional mailed-statement timing and Control Panel summary routes: `## Reporting`, raw lines 60-64.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Related raw API references

- [[raw/braintree/articles/moneris/reconciliation-2026-09-16|Braintree Moneris reconciliation article]] - unread navigation-only destination linked for refund and void reconciliation; not used as factual evidence here
- [[raw/braintree/articles/risk-and-security/chargebacks-retrievals/overview-2026-09-16|Braintree chargebacks and retrievals overview]] - unread navigation-only destination linked for dispute lifecycle context; not used as factual evidence here
- [[raw/braintree/articles/control-panel/reporting/settlement-batch-summary-2026-09-16|Braintree Settlement Batch Summary article]] - unread navigation-only reporting destination; not used as factual evidence here
- [[raw/braintree/articles/control-panel/reporting/transaction-summary-2026-09-16|Braintree Transaction Summary article]] - unread navigation-only reporting destination; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/moneris/pricing-fees-2026-09-16|Braintree Moneris Pricing and Fees]] - fully read collected article covering fee categories, account-selected pricing models, operation-specific fees, void timing, dispute-fee treatment, and statement/reporting routes
