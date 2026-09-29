---
title: "Braintree PayPal Pay Later Offers"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal-pay-later-offers"
raw_files:
  - "braintree/articles/guides/payment-methods/paypal-pay-later-offers-2026-09-16.md"
tags: [braintree, paypal, pay-later, bnpl, installment-payments, messaging]
---

## Overview

This collected Braintree guide describes PayPal Pay Later offers used with PayPal Checkout: short-term interest-free payments, longer-term monthly installments and other special financing for buyers, while merchants are paid up front. It is a retrieval route for the page's country-dependent offer table, merchant and customer eligibility boundaries, Checkout with Vault enablement route, and Pay Later messaging rules. It is not a generic PayPal Checkout setup guide or the dedicated PayPal Credit guide, and the 2026-09-16 snapshot does not establish current offer terms, merchant enablement or buyer eligibility.

## Key takeaways

- The page says Pay Later offers are included with PayPal Checkout at no additional cost except in the US. Treat that wording as page-scoped snapshot evidence; the page does not state the US cost or establish current pricing.
- Offer names, purchase ranges, installment structures and legal or credit qualifications differ by customer country in the page's US, UK, France, Australia, Germany, Italy and Spain table. The UK row includes PayPal Credit as a country-specific offer and says merchants offering PayPal Credit Instalments cannot also offer Pay in 3; this does not make Pay Later offers and PayPal Credit interchangeable products or replace the separate PayPal Credit guide.
- The page says consumers in the listed countries are eligible across most integrations, while merchant eligibility differs by merchant location and integration. It directs merchants to the PayPal overview and account support for details, and requires contacting PayPal to enable Pay Later offers on Checkout with Vault.
- Customers select **Pay Later** in checkout and their eligibility is then determined in seconds. This is an eligibility decision, not a guarantee that every customer, cart or displayed offer qualifies.
- Pay Later messaging dynamically presents an offer based on the purchase. The page requires showing the Pay Later button whenever Pay Later messaging is presented and prohibits merchants from creating additional content, wording, marketing or other material to encourage use of the product.

## Evidence boundaries

> [!warning] Snapshot and country scope
> Do not generalize one country's offer, amount range, installment schedule, credit qualification or regulatory note to another country, and do not treat collection success as current availability. Use the country table at lines 18-28 for the collected terms, then verify current terms and individual merchant eligibility through the linked authority.

> [!warning] Product and checkout scope
> Pay Later offers are presented through PayPal Checkout, but this page does not document generic PayPal Checkout setup or payment execution. Its UK row mentions PayPal Credit with separate coexistence and regulatory conditions; do not collapse PayPal Credit into the broader Pay Later offer identity.

> [!warning] Messaging restriction
> Showing promotional messaging is not buyer approval or payment completion. Keep the required Pay Later button and the prohibition on merchant-created promotional material attached to any messaging guidance.

## Detail locators

- Pay Later offer identity, merchant-up-front payment and the page's PayPal Checkout cost statement: `# PayPal Pay Later Offers`, line 16.
- Country-specific offer names, ranges, schedules and legal or eligibility notes: `# PayPal Pay Later Offers`, table at lines 18-28.
- Consumer-versus-merchant availability and Checkout with Vault enablement: `## Availability`, lines 31-35.
- Customer selection and seconds-based eligibility decision: `### Customer availability`, lines 38-40.
- Existing PayPal setup and full integration routes: `## Setup`, lines 43-45.
- Dynamic messaging, Pay Later button requirement and placement guidance: `### Pay Later messaging`, lines 48-52.
- Prohibition on additional merchant-created promotional content: `### Pay Later messaging`, IMPORTANT notice at lines 55-56.

## Related

- Company: [[braintree]]
- Main payment-method route: [[braintree-payment-methods]]
- Product concept: [[paypal-pay-later]]
- Broader checkout context: [[paypal-checkout]] (separate from this offer guide)

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/paypal-pay-later-offers-2026-09-16|Braintree PayPal Pay Later Offers guide]] - complete collected page covering offer identity, country table, availability, setup and messaging boundaries
