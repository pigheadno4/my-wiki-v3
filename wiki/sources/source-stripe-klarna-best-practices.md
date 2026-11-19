---
title: "Stripe: Optimize Klarna Conversion"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/klarna/best-practices"
raw_files:
  - "stripe-payments-klarna-best-practices-2026-11-07.md"
  - "stripe-klarna-best-practices-2025.md"
tags: [stripe, bnpl, klarna, conversion, best-practices, payment-method-messaging, express-checkout]
---

## Summary

Stripe's May and November 2026 Klarna best-practices guides recommend early Express Checkout Element placement, product-page Payment Method Messaging, relevant cart line items, and optional shipping and billing data. These are presentation and data-sharing recommendations that may improve the chance of Klarna offers or customer recognition. They do not promise buyer eligibility, a particular Pay in 4 offer, conversion lift, fraud-score improvement, dispute avoidance or payment success. See new raw lines 9-33.

## Recommendations and Conditions

- **Express Checkout Element:** The page says Klarna is available on it and suggests placing it early so customers can avoid re-entering shipping and billing details. This is advice, not a requirement or a guarantee of one-click completion for every buyer. See new raw lines 11-13.
- **Payment Method Messaging Element:** Show Klarna and other BNPL offers ahead of checkout; the page recommends product-detail placement. Showing a message does not establish the offer a customer will receive. See new raw lines 15-17.
- **Conditional underwriting:** Klarna's fraud and credit models consider purchase, customer and business data among other factors to decide whether a customer gets an interest-bearing or zero-interest installment offer. Sharing relevant data may increase chances of an offer such as Pay in 4; it does not compel approval. See new raw lines 19-23.
- **Payment line items:** Pass order line data about cart contents to aid customer recognition and potentially reduce unrecognized-purchase disputes. When using Checkout, Stripe says it automatically passes line items on the merchant's behalf. The page does not instruct Checkout users to submit duplicate data or guarantee dispute prevention. See new raw lines 25-29.
- **Shipping and billing:** The Klarna integration does **not require** a customer shipping or billing object. A merchant may optionally pass those addresses to help improve Klarna's customer fraud score; Klarna might cross-reference them with its customer records. The possible benefit is not a certain score change. See new raw lines 31-33.

## Dated Comparison

The 2026-05-06 guide described Klarna underwriting inputs as purchase, customer and “merchant data”; the 2026-11-07 guide uses “business data.” Both keep the same conditional offer and optional-address guidance. The wording and heading whitespace do not establish a new required field, changed underwriting rule, merchant identity, API schema or payment outcome. The current source's previous statement that optional addresses “improves” scoring was stronger than both captures and is narrowed above.

## Related Pages

- [[stripe]] — Stripe company route.
- [[stripe-klarna]] — Klarna concept and reciprocal best-practices route.
- [[source-stripe-klarna]] — payment-method overview.
- [[source-stripe-klarna-accept-payment]] — integration route and buyer flow.

## Raw Sources

- [[raw/stripe-payments-klarna-best-practices-2026-11-07|2026-11-07 Klarna best practices]] — newer full guide with business-data wording.
- [[raw/stripe-klarna-best-practices-2025|2026-05-06 Klarna best practices]] — older full guide with merchant-data wording.
