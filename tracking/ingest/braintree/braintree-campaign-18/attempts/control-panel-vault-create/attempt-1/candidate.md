---
title: "Braintree Control Panel: Create New Customers"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/vault/create"
raw_files:
  - "braintree/articles/control-panel/vault/create-2026-09-16.md"
tags: [braintree, control-panel, vault, customers, payment-methods, card-verification]
---

## Overview

This collected Braintree article documents creating a new customer Vault record through the Control Panel, either with or without a payment method. It identifies transaction-time and direct Vault creation routes, the Control Panel's credit-card-only payment-method boundary, and the separate API route; it does not document adding a payment method to an existing customer or the authorization and settlement behavior of a transaction.

## Key takeaways

- A Control Panel user can create a Vault record by selecting `Store in Vault` while creating a transaction or by navigating to `Vault` and choosing `New Customer`. The article also links to a separate API route for customer creation; these navigation choices do not establish equivalent API and Control Panel behavior.
- Direct Control Panel creation lets the user save a customer with or without a payment method. If a payment method is included, the article requires a credit-card number and expiration date. At the collected snapshot, only credit-card payment methods can be stored through the Control Panel; other payment methods must use the separate API route.
- Braintree recommends collecting additional customer details even when no payment method is included, and presents fraud mitigation, processing cost, customer service and chargeback-dispute benefits as reasons. These are recommendations and possible uses, not guaranteed outcomes.
- When saving a credit or debit card with the new Vault record, the article recommends card verification. If card verification is enabled and the account has multiple merchant accounts, the user can select the merchant account used for verification. This page does not establish that verification succeeded or that a purchase was authorized.
- Depending on account setup, CVV may also be required during record creation, but Braintree says it never stores that value. An optional billing address is used for applicable configured AVS rules; the page recommends storing street address and ZIP code.

> [!warning] Customer, payment-method and transaction boundaries
> This page creates a new Vault customer record, optionally with one credit card at creation. Do not treat customer creation without a payment method as stored-payment-method creation, or treat the transaction-time `Store in Vault` route or recommended card verification as evidence of a successful payment authorization or settlement. The page does not document adding a payment method later to an existing customer. Preserve the credit-card-only Control Panel boundary and the statement that CVV is never stored.

## Detail locators

- Control Panel transaction-time and `Vault` > `New Customer` routes plus the separate API route: `# Create New Customers`, lines 14-22.
- With-versus-without-payment-method choice and required card number and expiration date: `## New record requirements`, lines 25-33.
- Recommended customer details and the stated reasons for collecting more information: `## New record requirements` and `## Customer details`, lines 33-50.
- Control Panel credit-card-only boundary, verification recommendation, merchant-account selection and conditional-but-never-stored CVV: `## Payment method details`, lines 53-71.
- Optional billing address, applicable configured AVS rules and recommended address fields: `## Billing address`, lines 76-83.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- API customer-creation context: [[source-braintree-customer-create-node]]
- Control Panel context: [[source-braintree-control-panel-transaction-create]], [[source-braintree-control-panel-vault-card-verification]]

## Related raw API references

- [[raw/braintree/articles/control-panel/transactions/create-2026-09-16|Braintree Control Panel Create a Transaction article]] - unread navigation-only destination for the transaction-time `Store in Vault` route; not used as factual evidence here
- [[raw/braintree/docs/reference/request/customer/create/node-2026-09-16|Braintree Node.js customer-create request reference]] - unread navigation-only collected API route for separate customer creation; not used as factual evidence here
- [[raw/braintree/articles/control-panel/vault/card-verification-2026-09-16|Braintree Control Panel Card Verification article]] - unread navigation-only destination for the verification recommendation; not used as factual evidence here
- [[raw/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules-2026-09-16|Braintree AVS and CVV Rules article]] - unread navigation-only authority for configured address-verification rules; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/vault/create-2026-09-16|Braintree Control Panel Create New Customers article]] - complete collected page covering new Vault customer creation with or without a card, card and CVV boundaries, verification guidance and optional billing-address use
