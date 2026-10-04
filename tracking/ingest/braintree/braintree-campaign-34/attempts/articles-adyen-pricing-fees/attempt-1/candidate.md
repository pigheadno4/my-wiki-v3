---
title: "Braintree Adyen Pricing and Fees"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/adyen/pricing-fees"
raw_files:
  - "braintree/articles/adyen/pricing-fees-2026-09-16.md"
tags: [braintree, adyen, pricing, fees, reporting, chargebacks]
---

## Overview

This collected Braintree-hosted article describes fee categories, an IC++ pricing model, American Express account paths, and fee-reporting boundaries for merchants whose documented processor context is Adyen. It is a snapshot of Braintree's Adyen-processor documentation, not independent Adyen pricing authority and not a schedule of current or universal Adyen rates.

## Key takeaways

- The page defines markup, commission, per-transaction, interchange, scheme, and chargeback fee categories. In its documented account scope, markup, per-transaction, interchange, and scheme fees apply to successful transactions, while refunds, verifications, voids, and gateway rejections receive only the per-transaction fee. It says fees are calculated and deducted with payout; when presentment and settlement currencies differ, calculation uses the converted settlement amount.
- The stated standard model for Adyen merchants is IC++, composed of markup or applicable commission, a per-transaction fee, interchange, and scheme fees. Interchange and scheme fees are variable and not determined by Braintree; actual fee application depends primarily on card type and may also vary with merchant type, cost of sale, processing technology, region, and other factors. The snapshot gives fee categories and treatment, not numeric rates or a merchant-specific contract schedule.
- By default, the documented account processes American Express through Adyen's aggregated Amex account and uses an Adyen-and-Amex-determined commission instead of the standard markup. A merchant may instead apply directly to Amex; under that alternative, Amex manages funding, descriptors, chargebacks, and related support. This account choice must not be generalized to every merchant or region.
- The Settlement Details Report is generated upon payout and shows assessed and deducted transaction fees. The monthly Adyen invoice covers transactions settled during the invoice month, whereas the Settlement Details Report covers transactions paid to the account; the article warns that the invoice totals will not match that report and that the invoice is only a high-level snapshot, not a reconciliation source.
- Refunds and credits incur the standard per-transaction fee, and original-charge transaction fees are not returned for refunded transactions. Chargebacks and pre-arbitrations incur a non-refundable fee regardless of outcome, while retrievals do not incur that fee in this snapshot. Exact fee categories, assessment rules, report instructions, and transaction-type treatment remain at the verified raw locators below.

## Detail locators

- Fee-category definitions, successful-transaction treatment, non-sale operation treatment, payout deduction, and converted-settlement-amount basis: `## Transaction fees`, lines 17-31.
- Aggregated Adyen Amex account default, commission treatment, and direct-Amex alternative responsibilities: `## American Express`, lines 34-38.
- IC++ components and card, merchant, cost-of-sale, processing-technology, region, and other pricing factors: `## Pricing model`, lines 41-43.
- Settlement Details Report purpose and Control Panel steps: `### Settlement Details Report`, lines 49-56.
- Monthly Adyen invoice timing, coverage mismatch, and reconciliation warning: `### Adyen invoice`, lines 59-65.
- Refund and credit fee treatment, including non-return of original transaction fees: `## Refunds and credits`, lines 70-72.
- Non-refundable chargeback and pre-arbitration fee, outcome independence, and retrieval exclusion: `## Chargebacks, retrievals, and pre-arbitrations`, lines 75-77.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Reporting context: [[braintree-control-panel]]
- Currency context: [[braintree-currencies]]

## Related raw API references

- [[raw/braintree/articles/adyen/transactions/settlement-funding-timeline-2026-09-16|Braintree Adyen settlement and funding timeline]] - unread navigation-only destination linked for payout timing; not used as factual evidence here
- [[raw/braintree/articles/risk-and-security/chargebacks-retrievals/overview-2026-09-16|Braintree chargebacks and retrievals overview]] - unread navigation-only destination linked for dispute lifecycle context; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/adyen/pricing-fees-2026-09-16|Braintree Adyen Pricing and Fees]] - fully read collected article covering fee categories and transaction treatment, Amex account paths, IC++ qualifications, reporting, refunds, and dispute-related fees
