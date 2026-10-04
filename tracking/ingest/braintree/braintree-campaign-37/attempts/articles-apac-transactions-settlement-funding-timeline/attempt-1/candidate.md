---
title: "Braintree APAC Settlement and Funding Timeline"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/apac/transactions/settlement-funding-timeline"
raw_files:
  - "braintree/articles/apac/transactions/settlement-funding-timeline-2026-09-16.md"
tags: [braintree, apac, settlement, funding, disbursement, credit-cards]
---

## Overview

This collected [[braintree]] article under the APAC path describes the Braintree Direct route from a settled transaction through the merchant account to the merchant's bank account. For cards, it separates batch submission, the `Settling` state, processing-bank initiation and acknowledgment, the `Settled` state, disbursement, and later bank-account visibility.

This is a Braintree-hosted APAC snapshot. The page does not identify a country, account configuration, acquiring bank, currency, or independent bank authority, so its schedule must not be transferred to Australia, every APAC merchant, a sibling processor/account route, a merchant agreement, or current policy. It is not evidence that an individual transaction settled, was disbursed, or arrived in a bank account.

## Key takeaways

- The article starts with the prerequisite that a transaction is already settled before funds pass through the merchant account to the bank account, and says Braintree services funding because the merchant is using Braintree Direct.
- The captured card flow says transactions are submitted for settlement at 3am Central Time (US), then marked `Settling`. Braintree sends the batch to the processing bank, which initiates the funds transfer and produces a settlement acknowledgment; after Braintree receives confirmation, it marks transactions `Settled` and disburses them to the bank account. These are distinct lifecycle events, not interchangeable proof of bank arrival.
- The card-brand schedule is anchored to submission for settlement: the article says the merchant should see Visa/Mastercard funds in 1–3 business days and American Express funds in 2–8 business days. The Amex statement is expressly based on Braintree's experience; Amex sets its own cutoff and handles disbursement directly, so the page routes details to Amex.
- A separate funding statement uses transaction creation as its anchor and says funds are typically reflected within 2–5 business days. Default disbursement is every weekday excluding bank holidays; weekend or holiday funds are sent the following business day, and the article says it typically takes another business day before they are visible. Do not collapse these qualified timing statements into one guaranteed service level.
- Apple Pay and Google Pay are described as processed and disbursed alongside credit cards. PayPal instead manages disbursement separately from the Braintree-managed account; the linked PayPal funding-options page is navigation only here.

> [!warning] Event anchors and modal timing
> `Submitted for settlement`, transaction creation, settlement confirmation, disbursement, and bank-account visibility are different anchors. The article uses `should`, `typically`, and `in our experience`; none of the ranges guarantees settlement, payout, or deposit arrival for an individual transaction.

> [!warning] Captured APAC route only
> Keep the 3am Central Time batch time, brand ranges, descriptor, cadence and visibility delay within this captured APAC article. The path label alone does not establish country-wide or region-wide applicability, including Australia, and the snapshot is not current independent bank, processor, or PayPal policy.

## Detail locators

- Post-settlement prerequisite, merchant-account-to-bank-account path and Braintree Direct funding scope: `# Settlement and Funding Timeline`, raw line 16.
- Card batch submission at 3am Central Time (US), `Settling`, processing-bank transfer initiation, acknowledgment, `Settled` and disbursement sequence: `## Credit cards > ### Settlement`, raw line 24.
- Submission-anchored Visa/Mastercard and American Express ranges: `## Credit cards > ### Settlement`, raw lines 27–28.
- Experiential Amex qualification, Amex-owned cutoff and direct disbursement: `## Credit cards > ### Settlement`, raw line 30.
- Deposit descriptor: `## Credit cards > ### Funding`, raw lines 35–37.
- Creation-anchored typical range: `## Credit cards > ### Funding`, raw line 39.
- Weekday cadence, bank-holiday/weekend handling and additional visibility day: `## Credit cards > ### Funding`, raw line 41.
- Apple Pay and Google Pay alignment with card processing and disbursement: `## Apple Pay and Google Pay`, raw lines 44–46.
- Separately managed PayPal disbursement and linked funding-options route: `## PayPal`, raw lines 49–51.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Related raw API references

- [[raw/braintree/articles/apac/transactions/accepted-payment-methods-2026-09-16|Braintree APAC accepted payment methods]] - unread navigation-only destination linked for Apple Pay and Google Pay; not used as factual evidence here
- [[raw/braintree/articles/guides/payment-methods/paypal/funding-reconciliation-2026-09-16|Braintree PayPal funding and reconciliation]] - unread navigation-only destination linked for separate PayPal funding options; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/apac/transactions/settlement-funding-timeline-2026-09-16|Braintree APAC Settlement and Funding Timeline article]] - fully read captured page covering the Braintree Direct post-settlement path, card lifecycle and qualified timing anchors, deposit descriptor, disbursement cadence, wallet alignment and separate PayPal funding
