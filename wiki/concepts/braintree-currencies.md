---
title: "Braintree Currencies"
type: concept
category: technology
tags: [braintree, currencies, presentment, settlement, multi-currency, merchant-accounts]
---

## Braintree Currencies

Braintree's collected currency guide distinguishes presentment currency, which relates to the currency displayed to and charged to a customer, from settlement currency, which is deposited into the merchant's business bank account. Account setup determines whether either context can use multiple currencies, and available settlement currencies are typically limited to major currencies in the merchant's region. [[source-braintree-get-started-currencies]]

## Setup and live-processing boundary

Single-currency accounts present and settle in the merchant's home currency by default. Multi-currency acceptance is not automatic: it is subject to relevant banking-partner approval and successful integration of the required multi-currency accounts. Additional presentment currencies use additional merchant accounts; after an additional currency is configured, the integration must specify its merchant account ID. The guide recommends sandbox transactions to confirm configuration and says that, without the documented onboarding choices, approvals and integration, live transactions process only in the home currency regardless of checkout pricing.

The page states support for more than 130 local currencies in 44 countries but does not enumerate or map them. It also warns that displaying a converted price while charging in the home currency can produce a charged amount different from the display as rates move, and that exchange-rate movement can make an international customer's refund differ from the original amount paid. Treat the collected snapshot as a retrieval route, not proof of current currency coverage or merchant eligibility.

## Sources

- [[source-braintree-auth-multi-currency-node]] - connected-merchant presentment-currency creation and listing route limited to Braintree Auth signups, with all-payment-method support conditions and a preserved Amex-specific qualification
- [[source-braintree-payment-methods-paypal-setup-guide]] - PayPal-specific multi-currency setup route requiring a Braintree merchant account per accepted currency, PayPal foreign-currency configuration and merchant-account selection during processing, with blocking and fee tradeoffs

- [[source-braintree-get-started-currencies]] - presentment and settlement definitions, single- and multi-currency setup choices, account and approval prerequisites, conversion effects, live-processing fallback and exact raw-detail routes
