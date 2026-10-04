---
title: "Braintree NAB Settlement and Funding Timeline"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/nab/transactions/settlement-funding-timeline"
raw_files:
  - "braintree/articles/nab/transactions/settlement-funding-timeline-2026-09-16.md"
tags: [braintree, nab, settlement, funding, merchant-account]
---

## Overview

This 2026-09-16 Braintree-hosted NAB account/processor snapshot explains how card transactions move from settlement batching and processor confirmation to disbursement, with bank-qualified timing, separate Amex and PayPal handling, and a card-verification warning. It is not independent current NAB, Amex, or PayPal policy, a schedule for a sibling account route, a timing guarantee, or proof that an individual transaction settled, was disbursed, or arrived at a bank.

## Key takeaways

- Credit-card transactions are grouped into settlement batches and sent to the processing bank for settlement confirmation. The account cutoff is stated as 9:55pm AET and unchangeable; transactions submitted after it move to the next day's batch.
- Funds become ready for disbursement only after processor confirmation that the transaction settled successfully. For a business bank account also held with NAB, the stated schedules are 1–3 business days for Visa/Mastercard and 2–8 business days for American Express, both measured after submission for settlement. A different banking institution may add delay.
- The page describes the Amex schedule as experiential rather than guaranteed and says Amex controls its own cutoff times and disbursements. Apple Pay and Google Pay transactions funded by Amex are processed and disbursed with regular Amex transactions.
- PayPal manages disbursement separately from the Braintree-managed account and has a separate funding-options route.
- Separately, when Braintree card verification is enabled, the page says the gateway verifies all cards with $1 authorizations; individual verification should also use $1 because $0 attempts trigger validation error 91741.

## Detail locators

- Settlement-to-disbursement transition and fixed cutoff: lines 16 and 21–23.
- Card-brand schedules, Amex ownership qualification, and other-bank delay: lines 26–31.
- Card-verification amount and validation-error warning: lines 34–36.
- Amex-funded Apple Pay and Google Pay treatment: lines 39–41.
- Separate PayPal disbursement route: lines 44–46.

## Related

- [[braintree]]
- [[braintree-payment-platform]] — provider concept for merchant-account roles and the general post-settlement funding route.

## Raw Sources

- [[raw/braintree/articles/nab/transactions/settlement-funding-timeline-2026-09-16|Braintree NAB Settlement and Funding Timeline (2026-09-16 snapshot)]]
