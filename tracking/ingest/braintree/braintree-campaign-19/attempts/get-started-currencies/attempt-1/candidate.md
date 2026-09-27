---
title: "Braintree Currencies"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/get-started/currencies"
raw_files:
  - "braintree/articles/get-started/currencies-2026-09-16.md"
tags: [braintree, currencies, presentment, settlement, multi-currency, merchant-accounts]
---

## Overview

This collected Braintree guide distinguishes presentment currency, which relates to what a customer sees and is charged, from settlement currency, which is deposited into the merchant's business bank account. It routes merchants through single- and multi-currency account choices, approval and integration prerequisites, merchant-account selection, conversion effects and sandbox testing without replacing the dedicated currency reference.

## Key takeaways

- Presentment currency is customer-facing: it can be the currency displayed by the website or app and the currency charged. Braintree's page states support for more than 130 local currencies in 44 countries, but it does not enumerate or map them; the linked dedicated currency reference is the route for that detail.
- Settlement currency is the currency deposited into the business bank account. Whether a merchant can settle only in its home currency or in multiple currencies depends on account setup, and the page says available settlement currencies are typically limited to major currencies in the merchant's region.
- The default single-currency setup presents and settles in the merchant's home currency. The page warns against displaying a converted price while charging in the home currency because rate movement can make the charged amount differ from the displayed amount; exchange-rate movement can likewise make an international customer's refund differ from the original amount paid.
- A multi-currency setup is not automatic. Presenting or settling in multiple currencies is subject to relevant banking-partner approval and successful integration of the required multi-currency accounts. Additional presentment currencies use additional merchant accounts, and when presentment and settlement currencies differ, the transaction amount is converted before deposit. Depending on the bank and location, separate bank accounts may be needed for settlement currencies.
- After an additional currency is configured, the integration must specify its merchant account ID. Before live processing, the merchant should create sandbox test transactions; unless onboarding choices, relevant banking approval and the required account integration are all complete, the page says live transactions process only in the home currency regardless of checkout pricing.

> [!warning] Account, geography and live-processing boundaries
> The page's currency choices are account-, banking-partner- and region-qualified. Its statement of more than 130 local currencies in 44 countries does not identify which currency is available in which country or prove an individual merchant's eligibility. Sandbox processing does not establish live multi-currency configuration, and the 2026-09-16 collection date does not establish current support.

## Detail locators

- Presentment definition and the page's aggregate currency/country statement: `## Presentment currency`, lines 19-23.
- Settlement definition and account/region qualifications: `## Settlement currency`, lines 26-28.
- Single- versus multi-currency routing, home-currency default and displayed-price warning: `## Currency setups` through `### Single currency setups > NOTE`, lines 31-44.
- Refund exchange-rate mismatch warning: `### Single currency setups > #### Refunds`, lines 49-51.
- Multi-currency approval and account-integration prerequisites: `### Multi-currency setups` through `IMPORTANT`, lines 54-60.
- Additional presentment merchant accounts, conversion before deposit and settlement bank-account qualification: `### Multi-currency setups > #### Presentment` through `#### Settlement`, lines 65-72.
- Merchant-account-ID integration, sandbox confirmation and live home-currency fallback: `### Multi-currency setups > #### Integrating with multiple currencies`, lines 75-81.
- Sandbox merchant-account testing route: `## Testing currencies`, lines 86-88.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-currencies]]

## Related raw API references

- [[raw/braintree/docs/reference/general/currencies-2026-09-16|Braintree supported currencies reference]] - unread navigation-only page linked for the detailed currency list; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/get-started/currencies-2026-09-16|Braintree Currencies article]] - complete collected page covering presentment and settlement definitions, single- and multi-currency setups, prerequisites, conversion effects, integration and testing boundaries
