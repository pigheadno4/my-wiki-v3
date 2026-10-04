---
title: "Braintree BR Accepted Payment Methods"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/br/transactions/accepted-payment-methods"
raw_files:
  - "braintree/articles/br/transactions/accepted-payment-methods-2026-09-16.md"
tags: [braintree, brazil, payment-methods, cards, combo-cards, american-express, currencies]
---

## Overview

This collected Braintree BR-path article is an account-scoped retrieval route for the card brands described as accepted by default, Brazil-specific combo-card handling, locally acquired American Express processing and BRL presentment. The page metadata was updated on 2025-04-01 and the page was collected on 2026-09-16; it is snapshot evidence, not proof of current support, a particular merchant account's configuration, card or buyer eligibility, authorization, capture, settlement, funding, refund success or chargeback outcome.

## Key takeaways

- The article says the account is set up by default to accept Visa, Mastercard, Amex, Elo and Hipercard. Keep that statement scoped to this collected BR-path account article; it does not establish a universal Braintree card bundle or the configuration of an individual merchant account.
- Brazilian issuers' combo cards can be used as credit or debit. The article says the integration can specify the account type through `account_type` in 3DS and/or the transaction sale call. Because it says there is no specific combo-card indicator, Brazilian customers need a way to select the account type when needed. The page does not establish that every Brazilian card is a combo card or that supplying the field proves eligibility or successful processing.
- American Express processing is described as using local acquirers in Brazil and as configured by default for the account, without requiring the merchant to apply for a separate Amex merchant account. In this route Braintree manages Amex funding, descriptors, chargebacks and technical support, and includes Amex transactions in its statement alongside other card brands. These are snapshot account-route statements, not proof of a particular merchant's present configuration, commercial terms, funding or dispute outcome.
- The currency section says Brazilian-real presentment is supported in Brazil and that transactions use the currency associated with the merchant account, stated here as BRL. Its statement that customers should be able to purchase regardless of their bank-account currency is modal, not an eligibility or execution guarantee: the customer's bank performs conversion and may charge conversion or other fees, while refunds can become more difficult and chargebacks can increase.

> [!warning] Brazil, account and snapshot scope are material
> Keep the default card brands, combo-card UI and request-field guidance, local-acquirer Amex arrangement and BRL processing scoped to this collected BR-path article and its account wording. Do not transfer them to another region, account or processor path, or treat collection, configuration or a submitted field as proof of present support, buyer eligibility or payment execution.

> [!warning] Currency wording is modal and includes downstream risk
> "Should be able to purchase" does not establish that every foreign-currency card or buyer will be accepted. The article assigns conversion to the customer's bank, warns that the bank may charge fees, and says refund difficulty can increase chargebacks; it does not prove an exchange rate, fee, refund or dispute result for a particular transaction.

## Detail locators

- Page identity and source timestamps: source comment and frontmatter, raw lines 1-10.
- Default Visa, Mastercard, Amex, Elo and Hipercard account setup: `## Card types`, raw lines 17-26.
- Brazilian combo-card credit/debit use, `account_type` placement, absent combo-card indicator and customer account-type selection: `### Combo cards`, raw lines 29-31.
- Local-acquirer Amex processing in Brazil, default account configuration and no separate Amex merchant-account application: `### American Express`, raw lines 34-36.
- Braintree-managed Amex funding, descriptors, chargebacks, technical support and statement inclusion: `### American Express`, raw line 38.
- Brazil BRL presentment, merchant-account-currency processing, customer-bank conversion and modal purchase wording: `## Currencies`, raw lines 41-43.
- Possible bank conversion or other fees and refund-difficulty/chargeback warning: `## Currencies`, raw line 43.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Currency and merchant-account context: [[braintree-currencies]]

## Raw Sources

- [[raw/braintree/articles/br/transactions/accepted-payment-methods-2026-09-16|Braintree BR Accepted Payment Methods article]] - fully read 2026-09-16 snapshot covering default card brands, combo-card handling, local Amex processing and BRL currency handling
