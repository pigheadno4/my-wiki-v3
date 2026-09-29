---
title: "Braintree PayPal Credit"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal-credit"
raw_files:
  - "braintree/articles/guides/payment-methods/paypal-credit-2026-09-16.md"
tags: [braintree, paypal-credit, financing, payment-methods, deprecated]
---

## Overview

This pinned Braintree snapshot describes PayPal Credit as a reusable credit line selected at checkout, but the page itself is marked deprecated and directs readers to the separate Pay Later offers guide. It is a retrieval route for the legacy page's stated product identity, US/UK availability and currency limits, customer credit-approval flow, additional financing-option qualifications and PayPal-setup boundary; it is not evidence for current Pay Later offers or generic PayPal checkout behavior.

## Key takeaways

- The collected page is explicitly deprecated and directs readers to Braintree's Pay Later offers guide. PayPal Credit and that successor documentation remain separate evidence targets.
- On this page, PayPal Credit is an instant, reusable credit line that customers can use at checkout. It says customers may pay over time while the merchant receives 100% up front, with the merchant paying its normal PayPal transaction fee.
- The page limits stated availability to merchants selling to customers in the United States or United Kingdom, with USD as the only supported currency for US customers and GBP as the only supported currency for UK customers. For UK customers, it says merchants need Financial Conduct Authority authorization and should check with their Sales or Account manager before offering PayPal Credit.
- Customers select PayPal Credit at checkout, complete an application, accept PayPal's terms and receive a credit decision; use is subject to credit approval.
- The page separately names Easy Payments in the US and Instalments in the UK as customizable PayPal Credit financing options and says to contact Braintree first about pricing and qualifications. Enabling PayPal Credit requires changes to an existing PayPal setup, with full integration instructions delegated to the linked developer documentation.

## Evidence boundaries

> [!warning] Deprecated and snapshot-scoped
> This is an immutable page collected on 2026-09-16, and its own deprecation notice redirects to a different Pay Later offers guide. Do not treat its availability, pricing, offer names or setup wording as proof of current support, merchant enablement or successor-offer terms.

> [!warning] Product and integration boundaries
> PayPal Credit on this page is a named credit-line offering, not a synonym for every Pay Later offer and not the whole PayPal checkout integration. The page's reference to an existing PayPal setup does not establish that generic PayPal checkout alone enables PayPal Credit.

## Detail locators

- Page deprecation and Pay Later offers redirect: opening `**IMPORTANT**`, lines 17-18.
- PayPal Credit identity, customer financing, merchant funding and fee statement: introductory paragraph, line 22.
- US/UK availability, currency limits and UK FCA authorization: `## Availability`, lines 25-31.
- Customer application flow and credit-approval condition: `### Customer availability`, lines 36-42.
- Easy Payments and Instalments naming plus pricing/qualification contact route: `## Additional financing options`, lines 47-53.
- Existing-PayPal-setup boundary and full-integration-doc route: `## Setup`, lines 58-60.
- Optional web-banner presentation route: `### Banners`, lines 63-67.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Separate successor-offer concept: [[paypal-pay-later]]

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/paypal-credit-2026-09-16|Braintree PayPal Credit guide]] - complete collected page covering the deprecated offering, stated availability, customer approval, financing options, setup and banners
