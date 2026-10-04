---
title: "Braintree AIB BF Pricing and Fees"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-bf/pricing-fees"
raw_files:
  - "braintree/articles/aib-bf/pricing-fees-2026-09-16.md"
tags: [braintree, aib-bf, pricing, fees, refunds, rounding]
---

## Overview

This collected Braintree-hosted article at the exact AIB BF route describes transaction-fee categories, account-selected pricing models, fee reporting, transaction-level rounding, refund credits, and dispute-related fees. The AIB BF path label is retained without interpreting or expanding it. This is a snapshot of that exact Braintree documentation variant, not AIB AF coverage, a merchant-specific contract or rate schedule, proof of current account eligibility, or independent current bank policy.

## Key takeaways

- The article defines discount-rate, per-transaction, interchange, scheme, chargeback, multi-currency, cross-border, and Kount fees. Whether interchange, scheme, and Kount fees are separate or included in Braintree processing fees depends on the pricing model; multi-currency versus cross-border treatment depends on account setup and customer country. The card-brand-specific cross-border exception table remains at the verified raw locator below.
- The page says all fees are deducted from daily disbursements and apply only to successful sale transactions, not refunds, verifications, declines, gateway rejections, or voids. That is the page's own exact AIB BF scope and should not be transferred to AIB AF or another account or processor variant.
- Pricing was determined when the account was opened. The statement's Pricing Schedule identifies IC+ as "Interchange Plus" and otherwise identifies the account as blended; the page separately describes blended fixed-rate treatment, IC+ with variable interchange, and IC++ with variable interchange and scheme fees. It does not provide merchant-specific numeric rates.
- Processing rates are not displayed in the Control Panel; the article points to the statement for the specific discount rate and per-transaction fee. It also points to a monthly Transaction Fee Report for assessed fees on a sale. Those links establish navigation only; this source does not assert that either destination agrees with the pricing page beyond the link labels.
- Braintree processing fees are rounded down at transaction level when a remainder extends past the penny. As a result, multiplying a rate by total monthly settled sales can differ slightly from the statement's fee details.
- A refund does not add a new fee, and the article generally says the original Braintree transaction fees are not returned after a full or partial refund. It then qualifies that treatment: depending on pricing model and the date processing began, Braintree may credit its processing fees when a transaction is fully refunded.
- The snapshot says a non-refundable chargeback fee applies to chargebacks and pre-arbitrations regardless of outcome, while retrievals do not result in that fee "at this time." It supplies no amount here, and the time-qualified treatment is not current or universal bank-policy evidence.

> [!warning] Exact variant and refund qualification
> Keep this evidence on the exact AIB BF route and do not transfer its model, fee, exemption, refund, rounding, or dispute treatment to AIB AF, another account or region, or current bank policy. Preserve both refund statements: original fees are generally retained, while a pricing-model- and processing-start-date-dependent credit may apply to a fully refunded transaction.

## Detail locators

- Fee-category definitions, pricing-model inclusion, multi-currency versus cross-border conditions, successful-sale scope, daily-disbursement deduction, excluded operations, and statement rate lookup: `## Transaction fees`, lines 17-36.
- Card-brand-specific cross-border exception note and country table: `### Special note on cross border fees`, lines 39-98.
- Account-opening model determination, statement identification, and blended, IC+, and IC++ composition and variability: `## Pricing models`, lines 101-118.
- Monthly Transaction Fee Report availability and Control Panel navigation: `## Reporting`, lines 121-130.
- Transaction-level round-down and monthly-total discrepancy: `## Rounding down`, lines 133-137.
- General original-fee retention and the conditional full-refund credit qualification: `## Refunds and credits`, lines 140-144.
- Outcome-independent chargeback and pre-arbitration fee plus time-qualified retrieval treatment: `## Chargebacks, retrievals, and pre-arbitrations`, lines 147-149.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Administration context: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/aib-bf/statements-reporting-2026-09-16|Braintree AIB BF Statements and Reporting]] - unread navigation-only destination linked for statement and fee-report access; not used as factual evidence here
- [[raw/braintree/articles/aib-bf/chargebacks-retrievals-prearbs-2026-09-16|Braintree AIB BF Chargebacks, Retrievals, and Pre-Arbs]] - unread navigation-only destination linked for dispute context; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/aib-bf/pricing-fees-2026-09-16|Braintree AIB BF Pricing and Fees]] - fully read collected article covering fee categories, account-selected pricing models, reporting links, transaction-level rounding, qualified refund treatment, and dispute-related fees
