---
title: "Braintree AIB AF Pricing and Fees"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-af/pricing-fees"
raw_files:
  - "braintree/articles/aib-af/pricing-fees-2026-09-16.md"
tags: [braintree, aib-af, pricing, transaction-fees, refunds, chargebacks]
---

## Overview

This collected Braintree-hosted AIB AF article documents fee categories, account-selected blended, IC+, and IC++ pricing models, assessed-fee reporting, and refund and dispute-fee treatment. It is a snapshot of the AIB AF documentation route, not AIB BF coverage, independent or current bank authority, a merchant-specific contract, or a current universal rate schedule.

## Key takeaways

- The article separates ad valorem, per-transaction, chargeback, interchange, scheme, multi-currency, and cross-border fees. It says all fees are deducted from disbursements, while Braintree's processing fee applies only to successful sale transactions, not refunds, verifications, declines, gateway rejections, or voids; interchange and scheme fees may apply to any transaction. Multi-currency versus cross-border treatment depends on account setup and customer country.
- A merchant using its own American Express account is not charged an ad valorem fee by Braintree under this page's treatment, but is charged a per-transaction fee in addition to interchange and direct Amex charges.
- The pricing model was set when the account was opened, and the page routes account-specific rates to the statement's Merchant Service Charges section. Blended pricing combines fixed ad valorem and per-transaction fees, with possible debit-versus-credit differences by account setup. IC+ combines Braintree processing and variable interchange fees; IC++ adds scheme fees, with exact assessment dependent on card, merchant, sale, technology, region, and other factors.
- The AIB Transaction Fee Report is described as available on the day a transaction is disbursed and as showing fees assessed and deducted for that transaction. The linked transaction-lifecycle page is navigation only here and is not evidence that any transaction was disbursed.
- Full and partial refunds incur no additional refund fee under this page, but the original Braintree processing fees are not returned. A non-refundable chargeback fee applies to chargebacks and pre-arbitrations regardless of outcome, while retrievals do not produce that fee "at this time"; the page provides no numeric amount.

> [!warning] Account, processor, and rounding scope
> This AIB AF snapshot does not document numeric rates or a rounding rule. Do not import rounding, rates, or fee treatment from AIB BF or another processor route, infer current account eligibility, or treat linked statement, lifecycle, or dispute pages as agreeing authority without reading them.

## Detail locators

- Fee categories, account-qualified multi-currency and cross-border treatment, successful-sale processing-fee scope, interchange/scheme exception, and own-Amex-account treatment: `## Transaction fees`, lines 17-36.
- Cross-border exclusions and card-brand-by-country table: `### Special note on cross border fees`, lines 41-100.
- Account-time model selection, statement rate route, and blended, IC+, and IC++ composition and variability: `## Pricing models`, lines 103-122.
- AIB Transaction Fee Report timing, purpose, and Control Panel steps: `## Reporting`, lines 125-132.
- Original processing-fee retention after full or partial refunds: `## Refunds and credits`, lines 135-137.
- Outcome-independent chargeback/pre-arbitration fee and time-qualified retrieval exclusion: `## Chargebacks, retrievals, and pre-arbitrations`, lines 140-142.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Administration context: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/aib-af/statements-2026-09-16|Braintree AIB AF statements]] - unread navigation-only destination linked for Merchant Service Charges; not used as factual evidence here
- [[raw/braintree/articles/get-started/transaction-lifecycle-2026-09-16|Braintree transaction lifecycle]] - unread navigation-only destination linked from the reporting section; not used as factual evidence here
- [[raw/braintree/articles/aib-af/chargebacks-retrievals-prearbs-2026-09-16|Braintree AIB AF chargebacks, retrievals, and pre-arbitrations]] - unread navigation-only destination linked for dispute context; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/aib-af/pricing-fees-2026-09-16|Braintree AIB AF Pricing and Fees]] - fully read collected article covering fee categories, account-selected pricing models, cross-border exclusions, assessed-fee reporting, refunds, and dispute-fee treatment
