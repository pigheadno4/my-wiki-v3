---
title: "Braintree PayPal Best Practices"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/best-practices"
raw_files:
  - "braintree/articles/guides/payment-methods/paypal/best-practices-2026-09-16.md"
tags: [braintree, paypal, checkout, vaulting, recurring-payments, user-experience]
---

## Overview

This collected Braintree article organizes Pay with PayPal experience guidance into One-Time Checkout, Vaulted Payments and Recurring Payments. It is a retrieval route for choosing among those page-defined use cases, presenting the PayPal button and review page, handling upstream shipping choices, and finding the article's vaulting and recurring-review qualifications; routine integration steps remain in the raw locators and linked implementation guides.

## Key takeaways

- The page assigns One-Time Checkout to most purchases, Vaulted Payments to stored-PayPal repeat use for fast, low-value purchases, and Recurring Payments to subscriptions and automated billing. These are article-level use-case recommendations, not proof that an account, SDK or buyer is currently eligible.
- For one-time payments, the article recommends PayPal button placement on cart and product-detail surfaces as an upstream shortcut and separately describes placement after merchant-collected details during checkout. It says the PayPal button should be the buyer's final checkout action, with the buyer redirected to an order-success page after approval.
- The article attributes a distinct presentation requirement to the PayPal User Agreement: PayPal and Venmo must be treated equally with other payment methods for logo placement, flow and fees, shown prominently, and not placed later than another payment method. Do not generalize the article's other "best practices" into contractual requirements.
- In upstream flows where the buyer has not supplied an address or delivery choice, the shipping-address callback lets PayPal show price including shipping and tax, while the shipping-options callback lets the buyer select delivery and updates the cart amount. The page says the address callback may be unnecessary when shipping fees do not change or do not apply, but says to use the options callback for physical goods even when only one delivery method exists.
- The Vaulted Payments section recommends that flow only for business models with average transactions below $40 and recommends One-Time Payments for the vast majority of business models. It frames vaulting around mobile-first, high-frequency, low-average-value online-to-offline services; its Native SDK, PopUp Bridge and future JavaScript App Switch statements are snapshot-scoped routes, not current compatibility proof.
- The Recurring Payments section covers regularly initiated merchant payments such as subscriptions, automatic bills, auto-reloads and installments. Its review-page guidance says the order card should display plan information and a recurring indicator before the buyer accepts the terms; the article does not define the full recurring billing, token, charge or cancellation lifecycle.

## Evidence boundaries

> [!warning] Requirement, recommendation and snapshot scope
> Preserve the article's modal language. The presentation standards are stated as User Agreement requirements; many placement and implementation items are recommendations or examples. The immutable 2026-09-16 collection does not establish current product availability, merchant approval, SDK compatibility, App Switch support, conversion results or buyer eligibility.

> [!warning] Keep the three flows distinct
> One-Time Checkout, Vaulted Payments and Recurring Payments have different stated use cases. Storing PayPal for repeat purchases is not itself a recurring-billing engine, and the recurring review page is not evidence of later-charge execution or lifecycle behavior.

## Detail locators

- Three Pay with PayPal use cases and their intended roles: `### Pay with PayPal use cases`, lines 25-48.
- One-Time Payment purpose and audience: `## Pay with PayPal for One-Time Payments > ### Overview`, lines 51-66.
- Upstream button presentation, User Agreement standards, Pay Later placement and JavaScript `data-page-type` route: `### Presenting the PayPal button > #### Upstream presentment`, lines 74-117.
- Shipping-address callback effect, upstream condition and fixed-or-inapplicable-fee exception: `#### Enable shipping address callback`, lines 120-132.
- Shipping-options callback effect, physical-goods guidance and upstream condition: `#### Enable shipping options callback`, lines 137-151.
- Merchant-checkout ordering, final-action guidance, server-side buyer-data route, review-page setup, shipping and line-item categories: `#### Checkout presentment` through `#### Optimize your buyer's PayPal Checkout experience`, lines 154-193.
- Vaulted Payments low-value recommendation, O2O audience, onboarding categories and platform-specific login routes: `## Pay with PayPal for Vaulted Payments`, lines 196-240.
- Recurring-payment identity, intended audience and review-page plan-information guidance: `## Pay with PayPal for Recurring Payments`, lines 243-264.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Checkout context: [[paypal-checkout]]
- Recurring-payment context: [[recurring-payments]]

## Related raw API references

- [[raw/braintree/docs/guides/paypal/checkout-with-paypal/javascript/v3-2026-09-16|Braintree PayPal One-Time Payments JavaScript v3 guide]] - unread navigation-only implementation route; not used as factual evidence here
- [[raw/braintree/docs/guides/paypal/pay-later-offers/javascript/v3-2026-09-16|Braintree Pay Later Offers JavaScript v3 guide]] - unread navigation-only route linked for messaging placement; not used as factual evidence here
- [[raw/braintree/docs/guides/paypal/recurring-payments/javascript/v3-2026-09-16|Braintree PayPal Recurring Payments JavaScript v3 guide]] - unread navigation-only implementation route; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/paypal/best-practices-2026-09-16|Braintree PayPal Best Practices article]] - complete collected page covering one-time, vaulted and recurring Pay with PayPal experience guidance
