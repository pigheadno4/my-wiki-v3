---
title: "Braintree ACH Direct Debit"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/ach"
raw_files:
  - "braintree/articles/guides/payment-methods/ach-2026-09-16.md"
tags: [braintree, ach, direct-debit, bank-accounts, payment-methods]
---

## Overview

This collected Braintree guide documents ACH Direct Debit as a US banking-network payment method that debits a customer's bank account rather than processing through a card brand. It is a retrieval route for the page's merchant-availability criteria, required account verification, delayed batch lifecycle, return and dispute exposure, setup boundary and bank-account recurring-use limit; the 2026-09-16 snapshot does not itself confirm current merchant eligibility or enablement.

## Key takeaways

- The page limits availability to US merchants transacting in USD through Braintree Direct, in good standing, and able to build a custom client-side JavaScript v3 integration. It explicitly says ACH is not available in Drop-in UI. Qualifying merchants are directed to contact Braintree to enable ACH Direct Debit in sandbox.
- A bank account must be verified before money is collected. The guide offers instant verification, network check, micro-transfers and independent check, and recommends a backup method; method-specific fees, timing, customer actions and risk qualifications remain at the raw locators below.
- ACH processing is batch based and does not use card-style authorization or capture. The page describes a three-business-day return wait before disbursement, two additional business days for funds to reach the merchant bank, and the possibility of later returns being deducted from a subsequent disbursement. A displayed `Settled` status therefore does not establish irreversibility.
- The guide says refunds are limited to transactions with `Settled` status. Its void guidance is internally unresolved: one passage says ACH transactions cannot be voided at any lifecycle point, while the next says merchants can contact support to enable voiding and that timing depends on the transaction circumstances.
- Bank accounts can be vaulted, but the page says Braintree recurring billing does not support repeat payments with bank accounts. Setup requires application-code changes and ACH Direct Debit enablement in the Control Panel.

## Evidence boundaries

> [!warning] Delayed and reversible outcome
> Do not treat submission, the three-business-day checkpoint, `Settled` status or disbursement as proof that an ACH debit is final. The page documents returns after the ordinary window, bank-account blocking for specified return codes, standard unauthorized-dispute windows and longer warranty-claim periods; use the exact raw sections before designing fulfillment, retry, dispute or reinitiation behavior.

> [!warning] Conflicting void guidance
> Preserve both page statements rather than converting either into a universal rule: the guide first says ACH transactions cannot be voided at any lifecycle point, then says support can enable the ability to void in circumstances whose timeline varies. Verify the applicable account and transaction behavior with Braintree before relying on a void path.

## Detail locators

- ACH identity and merchant eligibility: `# ACH Direct Debit`, line 16, and `## Availability`, lines 21-33.
- Required verification and the four method routes: `## Verification methods`, lines 38-76; account-ownership and debit-block return risks: lines 79-92.
- Batch-processing boundary, settlement/funding timeline and status meanings: `## Processing`, lines 97-118; day-by-day lifecycle: lines 120-153.
- Fees and conflicting void/refund guidance: `### Fees`, lines 156-158, and `### Voids and Refunds`, lines 161-169.
- Late returns, return-code handling and blocked-account scope: `### Returns`, lines 172-216.
- Unauthorized-dispute windows, extended claims and authorization-evidence route: `### Disputes`, lines 223-263.
- Vaulting, recurring-billing limit and setup route: lines 267-272.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Recurring-use boundary: [[recurring-payments]]

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/ach-2026-09-16|Braintree ACH Direct Debit guide]] - complete collected page covering availability, verification, delayed processing, returns, disputes, vaulting, recurring-use limits and setup
