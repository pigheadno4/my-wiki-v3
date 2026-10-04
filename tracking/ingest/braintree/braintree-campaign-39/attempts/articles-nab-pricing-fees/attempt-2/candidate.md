---
title: "Braintree NAB Pricing and Fees"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/nab/pricing-fees"
raw_files:
  - "braintree/articles/nab/pricing-fees-2026-09-16.md"
tags: [braintree, nab, pricing, fees, multi-currency, refunds, chargebacks]
---

## Overview

This collected Braintree-hosted NAB article describes transaction-fee categories, account-selected blended and IC+ pricing models, multi-currency settlement and withdrawal treatment, refunds, and dispute fees. It is a 2026-09-16 snapshot of this exact account/processor route, not a numeric rate schedule, merchant-specific agreement, current independent NAB policy, or authority for a sibling account or processor route.

## Key takeaways

- The page defines merchant-service, per-transaction, chargeback, interchange-and-scheme, GST, and multi-currency transaction fees. It says the per-transaction fee applies to all authorizations, expressly including verifications, failed transactions, and refunds. One section says NAB deducts named processing and chargeback fees monthly on the last business day; the later chargeback section gives a different timing described below.
- Outside the multi-currency transaction fee, the page states there is no additional fee for accepting non-AUD currencies. It lists USD, CAD, EUR, HKD, JPY, NZD, SGD, and GBP as major currencies that settle like-for-like; when those deposited funds are withdrawn or transferred, it says they are converted to AUD and NAB charges $20 AUD. Other currencies automatically convert to AUD before settlement at a daily Visa/Mastercard-determined rate. These statements are route-specific snapshot evidence, not a current rate or eligibility guarantee.
- The source uses two descriptions for the $20 AUD funding fee: one says it applies to that day's disbursement, while another says it applies per transfer/withdrawal. Preserve that wording tension rather than inferring whether multiple transfers on one day produce one or multiple charges.
- The pricing model was determined at account signup. Blended pricing combines a merchant-service fee with a per-transaction fee; IC+ adds variable interchange and scheme fees. Depending on account setup, blended rates may vary by payment method and presentment currency, while IC+ transaction costs depend on card type and other factors. The page provides no numeric model rates.
- Under both models, a refund incurs an additional per-transaction fee. The page says the original merchant-service fee is returned under blended pricing; under IC+, it says the original merchant-service and interchange fees are returned. A flat chargeback fee set in the pricing agreement applies to chargebacks and pre-arbitrations only when the merchant loses or accepts the dispute or lets it expire, and is shown as a separate debit. This section says chargeback fees are debited as applicable throughout the month alongside monthly processing fees, conflicting with the earlier statement that chargeback fees are deducted on the last business day; the snapshot does not resolve that timing conflict.

> [!warning] Exact-route, funding-fee, and chargeback-timing scope
> Do not transfer these NAB-route operation, model, currency, refund, dispute, or debit-timing rules to another processor/account route or present them as current independent bank policy. The source's "that day's disbursement" and "per transfer/withdrawal" descriptions of the $20 AUD conversion fee are not silently reconciled here. Nor are its chargeback-fee timing statements: one places deduction on the last business day, while another says debit occurs as applicable throughout the month alongside monthly processing fees.

## Detail locators

- Fee categories, all-authorization per-transaction-fee scope, and the last-business-day NAB deduction statement that includes chargeback fees: `## Transaction fees`, lines 17-31.
- Major-currency like-for-like settlement list, AUD withdrawal conversion and fee, and minor-currency pre-settlement conversion: `## Multi-currency fees`, lines 34-50.
- Account-signup model assignment and help route: `## Pricing models`, lines 53-55.
- Blended composition, account-qualified variation, and refund treatment: `### Blended`, lines 58-64.
- IC+ composition, cost factors, and refund treatment: `### Interchange plus (IC+)`, lines 67-71.
- Second funding-fee description and non-Braintree-control qualification: `## Funding fees`, lines 74-76.
- Control Panel reporting routes: `## Reporting`, lines 79-81.
- Agreement-set chargeback/pre-arbitration fee trigger, separate-debit treatment, and throughout-the-month wording that conflicts with line 31's last-business-day timing: `## Chargebacks and pre-arbitrations`, lines 84-86.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/articles/nab/pricing-fees-2026-09-16|Braintree NAB Pricing and Fees]] - fully read collected article covering fee categories, account-selected pricing models, multi-currency settlement and withdrawal conditions, refunds, reporting routes, and dispute-fee treatment
