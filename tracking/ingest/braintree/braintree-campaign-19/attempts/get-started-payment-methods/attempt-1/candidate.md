---
title: "Braintree Payment Methods and Eligibility"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/get-started/payment-methods"
raw_files:
  - "braintree/articles/get-started/payment-methods-2026-09-16.md"
tags: [braintree, payment-methods, cards, digital-wallets, eligibility]
---

## Overview

This collected Braintree getting-started article is a retrieval guide to the payment-method categories and merchant or customer qualifications stated on the page. It covers ACH Direct Debit, Apple Pay, Google Pay, card types, PayPal, Local Payment Methods, Venmo and Secure Remote Commerce, while separately recording Samsung Pay and Visa Click to Pay deprecation boundaries. Its links route to dedicated integration guides; link presence is not evidence for those guides' behavior or for current support.

## Key takeaways

- The page states that most US merchants can accept ACH Direct Debit from participating customers. For Apple Pay it names most merchants in the US, Canada, Europe, Australia and APAC, subject to processor settings; for Google Pay it names those regions and requires Google approval.
- The collected snapshot says Samsung Pay has been deprecated. It separately states that Visa Click to Pay would no longer be supported effective January 20, 2026, and that transactions attempted with it after that date would receive a `Payment method not supported` error and risk decline.
- For cards, the page says US merchant accounts bundle Visa, Mastercard, Discover, UnionPay, JCB and sometimes American Express by default, while most international merchant accounts bundle Visa and Mastercard. Amex acceptance requires indicating interest on the application or contacting Braintree. Online debit cards from a major card brand are handled like credit cards and run as credit because online PIN acceptance is unavailable.
- Dual-branded cards can run on either card-brand network supported in the merchant's region; the page's Elo example can therefore appear as a Discover transaction. Special-use cards such as HSA, FSA or P-Cards require the merchant account to have an appropriate merchant category code.
- PayPal is described as available to most Braintree merchants. Local Payment Methods are framed for cross-border customers with settlement into the merchant's PayPal account. Venmo is qualified to US merchants and the page names iOS, Android and desktop customer paths. Secure Remote Commerce is described as a limited release for eligible merchants.

## Evidence limitations

> [!warning] Internal Secure Remote Commerce conflict
> The opening note equates Visa Click to Pay with Secure Remote Commerce and states that support ends January 20, 2026, but the final section describes Secure Remote Commerce as currently in limited release to eligible merchants. The collected page does not resolve that conflict, so neither statement is treated as proof of current support.

> [!warning] Collected support and deprecation boundaries
> The page uses current-tense support wording, but this is an immutable 2026-09-16 snapshot and does not establish present availability, merchant enablement, buyer eligibility or processor configuration. An additional callout after the Samsung Pay statement says that "This guide has been deprecated" and routes to a Pay Later offers guide, but the collected rendering does not identify which guide the callout refers to; this source preserves that ambiguity rather than attributing it to the entire payment-method page or another specific method.

## Detail locators

- Visa Click to Pay end-of-support date, attempted-transaction error and decline risk: opening `**NOTE**`, lines 14-15.
- Page purpose and separate integration-overview route: `# Payment Methods`, line 20.
- ACH Direct Debit customer and US-merchant qualification: `## ACH Direct Debit`, lines 23-25.
- Apple Pay region and processor-setting qualification: `## Apple Pay`, lines 28-30.
- Google Pay region and Google-approval qualification: `## Google Pay`, lines 33-35.
- Samsung Pay deprecation and the unresolved adjacent guide-deprecation callout: `## Samsung Pay`, lines 38-44.
- US and international default card-brand bundles plus Amex action: `## Card types > ### Credit cards`, lines 49-54.
- Online debit handling, dual-branded routing and MCC-qualified special-use cards: `## Card types`, lines 57-69.
- PayPal availability and Local Payment Methods settlement scope: `## PayPal` and `## Local Payment Methods`, lines 72-79.
- Venmo device, funding-source and US-merchant scope: `## Venmo`, lines 82-84.
- Secure Remote Commerce wallet purpose and limited-release eligibility: `## Secure Remote Commerce`, lines 87-89.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]

## Related raw API references

- [[raw/braintree/docs/guides/payment-method-types-overview-2026-09-16|Braintree payment-method-types integration overview]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/guides/payment-methods/ach-2026-09-16|Braintree ACH Direct Debit guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/guides/payment-methods/apple-pay-2026-09-16|Braintree Apple Pay guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/guides/payment-methods/google-pay-2026-09-16|Braintree Google Pay guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/guides/payment-methods/paypal/overview-2026-09-16|Braintree PayPal guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16|Braintree Local Payment Methods guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/guides/payment-methods/venmo-2026-09-16|Braintree Venmo guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16|Braintree Secure Remote Commerce guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/guides/payment-methods/paypal-pay-later-offers-2026-09-16|Braintree Pay Later offers guide]] - navigation only; linked by the unresolved deprecation callout and not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/articles/get-started/payment-methods-2026-09-16|Braintree Payment Methods article]] - complete collected page covering the listed payment-method categories, eligibility qualifications, card scope and deprecation notices
