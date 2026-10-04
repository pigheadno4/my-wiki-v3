---
title: "Braintree AU Pricing and Fees"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/au/pricing-fees"
raw_files:
  - "braintree/articles/au/pricing-fees-2026-09-16.md"
tags: [braintree, australia, pricing, fees, chargebacks]
---

## Overview

This collected Braintree AU article explains how account setup determines pricing and fee types, distinguishes transaction fees from billable event fees, and describes the page's IC+ and IC++ models. It is a 2026-09-16 snapshot of the AU documentation route, not a merchant-specific pricing agreement, a numeric rate schedule, proof of current account eligibility, or universal/current Australian policy.

## Key takeaways

- The page names transaction fees and billable event fees as its two fee types. Its transaction-fee categories are per-transaction, cross-border, Kount, chargeback, interchange, merchant-service, combined Braintree-processing, and pass-through fees; the exact definitions remain at the verified raw locator below. The cross-border definition is based on the card-issuing country relative to the business country and does not establish multi-currency or foreign-exchange treatment.
- The page contains an unresolved scope tension: it first says transaction fees apply to individual settled transactions, then says the per-transaction fee applies to all authorizations, including verifications, failed transactions, voids, and refunds. Preserve both statements rather than treating either as a complete universal rule. A merchant using its own American Express account is also said to owe Braintree's per-transaction fee on top of fees paid directly to Amex.
- Billable event fees apply to every decline, refund, two-step authorization, and card verification, and the page says multiple billable event fees can apply to one transaction. The linked statements page was not read and is navigation rather than additional evidence here.
- Pricing-model assignment occurred when the account was originally opened. IC+ combines Braintree processing and variable interchange fees; IC++ adds variable scheme fees and pass-through fees. The page says transaction-level assessments vary by card and other factors including region, and that fees for both models are deducted monthly on the last business day. No numeric rate or account-specific amount is supplied.
- A flat-rate chargeback fee set in the pricing agreement is assessed for chargebacks and pre-arbitrations. Retrievals do not produce a fee "at this time" in this snapshot; the time-qualified statement is not current-policy proof.

> [!warning] Account, model, and fee-classification scope
> Account setup and the original account signup determine the applicable pricing and model. Keep the page's settled-transaction wording alongside its broader all-authorizations per-transaction-fee wording; do not silently reconcile them or transfer this AU snapshot to another account, region, pricing model, currency arrangement, or current policy.

## Detail locators

- Account-setup dependency and assistance route: opening paragraph, line 16.
- Fee-type split: `## Fees`, lines 19-21.
- Transaction-fee scope and category definitions, including the country-based cross-border condition: `### Transaction fees`, lines 24-36.
- All-authorizations per-transaction-fee wording and own-American-Express-account treatment: `### Transaction fees`, line 38.
- Billable-event triggers and multiple-fees-per-transaction statement: `### Billable event fees`, lines 41-43.
- Account-time pricing-model assignment: `## Pricing models`, lines 46-48.
- IC+ composition, variability, transaction factors, and monthly deduction timing: `### IC+`, lines 51-55.
- IC++ composition, variability, transaction factors, and monthly deduction timing: `### IC++`, lines 58-62.
- Agreement-set flat-rate chargeback and pre-arbitration fee plus time-qualified retrieval treatment: `## Chargebacks, retrievals, and pre-arbitrations`, lines 65-67.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/articles/au/pricing-fees-2026-09-16|Braintree AU Pricing and Fees]] - fully read collected article covering account-dependent fee types, per-transaction and billable-event treatment, IC+ and IC++ models, and dispute-related fees
