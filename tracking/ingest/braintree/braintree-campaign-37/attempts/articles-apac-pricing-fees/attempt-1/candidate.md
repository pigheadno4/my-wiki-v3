---
title: "Braintree APAC Pricing and Fees"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/apac/pricing-fees"
raw_files:
  - "braintree/articles/apac/pricing-fees-2026-09-16.md"
tags: [braintree, apac, pricing, fees, reporting, refunds, chargebacks]
---

## Overview

This collected Braintree-hosted APAC article describes fee categories, account-selected blended and IC++ pricing models, an APAC Transaction Detail Report, and refund, void, chargeback, pre-arbitration, and retrieval fee treatment. It is a 2026-09-16 snapshot of this exact APAC documentation route, not Australian or AIB coverage, a merchant-specific agreement, proof of current account eligibility, or a current universal rate schedule.

## Key takeaways

- All fees are described as deducted from disbursements before bank deposit. The per-transaction fee applies to all approved and declined authorizations, verifications, voids, and gateway rejections, while the ad valorem rate applies to settled transactions. The article says refunds do not incur a fee, then separately says a full refund credits all but the original per-transaction fee; preserve both statements rather than treating the retained original fee as a new refund-processing fee.
- The pricing model was determined when the merchant signed up. Blended pricing combines a fixed ad valorem rate and per-transaction fee, with rates potentially varying by payment method and presentment currency depending on account setup. IC++ adds interchange and scheme fees; those variable rates are determined by card networks and issuing banks, and exact fees depend on card type plus merchant, presentment-currency, sale, processing-technology, region, and other factors.
- The article states that multi-currency transactions on IC++ incur an additional 1% conversion fee. This is exact-route snapshot evidence only; it must not be transferred to an Australian, AIB, or other processor/account variant or presented as current policy.
- An APAC Transaction Detail Report is generated for each day on which transactions settle, usually about three business days after the transaction date. It covers settled transactions by batch, their associated fees, and chargebacks with case numbers and amounts; the timing is stated as usual, not guaranteed.
- Chargebacks and pre-arbitrations incur a nonrefundable flat fee regardless of outcome, determined by settlement currency: 30 SGD, 160 HKD, or 90 MYR. Retrievals do not result in this fee "at this time." These time-qualified snapshot amounts do not establish a current fee, another currency's treatment, or an account-specific contract.

> [!warning] Exact-route pricing conflict and scope
> This APAC page applies a per-transaction fee to all authorizations, verifications, voids, and gateway rejections. That operation scope differs from collected AIB and other processor/account pricing variants, so the variants must remain separate and this snapshot does not resolve which treatment applies to a particular merchant. Do not import Australia or AIB rates, models, reporting, rounding, refund, or dispute rules. The page also pairs "refunds do not incur any fees" with retention of the original per-transaction fee after a full refund; retain that distinction rather than claiming every original fee is returned.

## Detail locators

- Fee definitions, possible pricing-model bundling, disbursement deduction, operation-specific per-transaction treatment, settled-transaction ad valorem scope, and refund statement: `## Transaction fees`, lines 17-28.
- Account-signup model determination and support route: `## Pricing models`, lines 31-33.
- Blended composition and account-qualified payment-method and presentment-currency variation: `### Blended`, lines 36-40.
- IC++ composition, variable interchange and scheme ownership, transaction-level factors, and the additional multi-currency conversion fee: `### IC++`, lines 43-49.
- APAC Transaction Detail Report trigger, usual timing, and contents: `## Reporting`, lines 54-63.
- No-new-fee refund wording, separate void fee, and full-refund credit excluding the original per-transaction fee: `## Refunds and credits`, lines 66-70.
- Outcome-independent chargeback/pre-arbitration fee, settlement-currency amounts, and time-qualified retrieval exclusion: `## Chargebacks, retrievals, and pre-arbitrations`, lines 73-82.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Related raw API references

- [[raw/braintree/articles/apac/statements-reconciliation-2026-09-16|Braintree APAC Statements and Reconciliation]] - unread navigation-only destination linked for report context; not used as factual evidence here
- [[raw/braintree/articles/apac/chargebacks-retrievals-prearbs-2026-09-16|Braintree APAC Chargebacks, Retrievals, and Pre-Arbs]] - unread navigation-only destination linked for dispute context; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/apac/pricing-fees-2026-09-16|Braintree APAC Pricing and Fees]] - fully read collected article covering fee categories, account-selected pricing, reporting timing and contents, refunds, voids, and settlement-currency-specific dispute fees
