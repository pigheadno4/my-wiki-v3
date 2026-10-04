---
title: "Braintree Adyen Settlement and Funding Timeline"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/adyen/transactions/settlement-funding-timeline"
raw_files:
  - "braintree/articles/adyen/transactions/settlement-funding-timeline-2026-09-16.md"
tags: [braintree, adyen, transactions, settlement, funding, payouts]
---

## Overview

This collected Braintree-owned Adyen transaction article describes the path after transactions have been submitted for settlement. At the end of the day, the page says those transactions are marked `Settled` and sent to Adyen; Adyen then verifies them with the issuing banks before sending funds to the merchant.

The documented times are qualified expectations and schedules, not evidence that any individual transaction was verified, paid out or deposited.

## Key takeaways

- Issuing-bank verification occurs after Braintree marks submitted transactions `Settled` and sends them to Adyen. The page says verification is typically faster but can take 1–4 weeks.
- After verification, Adyen sends the funds; the page says the merchant should expect verified-transaction funds in its bank account within 2–3 business days of payout.
- The default payout schedule is Tuesday and Friday, excluding bank holidays. On a bank holiday, the page says funds are sent the following business day and typically take one additional business day to appear in the account.
- Alternative funding schedules are described as available through Braintree support, subject to the options available to the merchant.

> [!warning] Scheduled timing is not deposit proof
> The verification range, payout cadence and expected bank timing do not prove that a particular transaction funded or that a particular deposit arrived. This is a Braintree-owned snapshot of an Adyen processor route, not independent current Adyen authority.

## Detail locators

- End-of-day `Settled` marking, transfer to Adyen, issuing-bank verification prerequisite and qualified 1–4-week range: `# Settlement and Funding Timeline`, line 16.
- Adyen payout after verification and expected 2–3-business-day bank timing: `# Settlement and Funding Timeline`, line 18.
- Default Tuesday/Friday cadence and bank-holiday adjustment: `# Settlement and Funding Timeline`, line 20.
- Alternative schedule and support route: `# Settlement and Funding Timeline`, line 22.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/articles/adyen/transactions/settlement-funding-timeline-2026-09-16|Braintree Adyen Settlement and Funding Timeline article]] - complete collected page covering settlement handoff, issuing-bank verification, payout timing, default funding cadence, bank-holiday handling and alternative-schedule support
