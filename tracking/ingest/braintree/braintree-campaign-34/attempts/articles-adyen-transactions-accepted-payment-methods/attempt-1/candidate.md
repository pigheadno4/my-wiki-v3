---
title: "Braintree Adyen Accepted Payment Methods"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/adyen/transactions/accepted-payment-methods"
raw_files:
  - "braintree/articles/adyen/transactions/accepted-payment-methods-2026-09-16.md"
tags: [braintree, adyen, payment-methods, cards, currencies, merchant-accounts]
---

## Overview

This collected Braintree article is an Adyen-processor retrieval route for the account's default card types and merchant-account currency behavior. It documents the Braintree-hosted processor setup represented by this page, not universal payment-method availability across Adyen products or a Braintree Orchestration integration.

## Key takeaways

- The article says the account is configured by default to accept Visa, Mastercard and American Express. American Express is limited to a subset of currencies, and the merchant is directed to contact Braintree to determine whether the available options meet its needs. These are account- and currency-qualified statements from this Adyen-processor article, not a universal Adyen availability claim.
- A transaction is processed in the currency associated with the merchant account. When the customer's bank account uses another currency, the customer's bank converts the charge and may impose conversion or other fees; the article also warns that refunds become more difficult and may increase chargebacks.
- To charge directly in another supported currency, the article directs the merchant to request an additional merchant account, work with Customer Success to determine applicable presentment and settlement currencies, and update the integration to specify the new merchant account ID after setup.

> [!warning] Processor and account scope are material
> Keep the card list, American Express currency condition and currency-account instructions scoped to this collected Braintree Adyen-processor article. Do not transfer them to another processor, region or merchant account, or treat account setup as proof of successful transaction processing, conversion, refund, settlement or funding.

## Detail locators

- Default Visa, Mastercard and American Express card types: `## Card types`, raw lines 17-24.
- American Express limited-currency condition and contact route: `## Card types`, raw line 26.
- Merchant-account currency processing, customer-bank conversion, possible fees and refund/chargeback warning: `## Currencies`, raw line 31.
- Additional merchant-account request and applicable presentment/settlement-currency guidance: `## Currencies`, raw line 33.
- Integration update to specify the new merchant account ID after additional-currency setup: `## Currencies`, raw line 35.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Currency and merchant-account context: [[braintree-currencies]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/articles/adyen/pricing-fees-2026-09-16|Braintree Adyen pricing and fees article]]
- [[raw/braintree/docs/reference/general/currencies-2026-09-16|Braintree currencies reference]]

## Raw Sources

- [[raw/braintree/articles/adyen/transactions/accepted-payment-methods-2026-09-16|Braintree Adyen Accepted Payment Methods article]] - fully read 2026-09-16 snapshot covering account-default card types, the American Express currency condition and merchant-account currency setup
