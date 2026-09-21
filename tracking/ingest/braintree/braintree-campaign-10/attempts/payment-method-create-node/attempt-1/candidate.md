---
title: "Braintree Payment Method Create (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/payment-method/create/node"
raw_files:
  - "braintree/docs/reference/request/payment-method/create/node-2026-09-16.md"
tags: [braintree, node-js, payment-methods, vault, verification, payment-method-nonce]
---

## Overview

This Braintree Node.js reference documents creating a payment method for an existing customer with `gateway.paymentMethod.create()`. It is the retrieval entry for the operation's prerequisites and its default, billing-address, duplicate-prevention, card-verification, and nonce-versus-raw-data qualifications; complete option shapes and examples remain in the raw page.

## Key takeaways

- The page states that creating a payment method for an existing customer requires only the customer ID and a payment-method nonce. It separately links to customer creation as another route for creating a payment method.
- When a customer has multiple payment methods, the first one created is the default; the page shows `makeDefault: true` for making the new method the default. The default is used for transactions created with a customer ID.
- A supplied billing address is ignored for a PayPal account and overrides an address supplied during nonce creation. The page also shows the separate existing-address-ID form.
- Duplicate rejection is optional and does not apply uniformly: the page says `failOnDuplicatePaymentMethod` is ignored for PayPal, Pay with Venmo, Apple Pay, Google Pay, and ACH payment methods. It does not define the comparison or matching rules used to identify a duplicate.
- Braintree runs credit-card validations by default but does not perform card verification by default. The page strongly recommends account-wide card verification; its manual route uses `verifyCard: true`. When Premium Fraud Management Tools are used, it also strongly recommends passing `device_data` each time a card is verified.
- Although raw card data and a payment-method nonce can be passed together, the page recommends passing only a nonce. If both are supplied, individually supplied fields take precedence and remaining attributes come from the nonce.

> [!warning] Payment-type and verification boundaries
> Do not generalize duplicate rejection to the payment methods for which this page says the option is ignored, or treat ordinary credit-card validation as card verification. For Premium Fraud Management Tools, keep the page's `device_data` recommendation attached specifically to each card-verification attempt.

## Detail locators

- Existing-customer prerequisite, required inputs, and Node callback invocation: `# Payment Method: Create` and `### Node`, lines 17-30.
- Custom-token behavior and Drop-in restriction: `### Specify a token`, lines 35-58.
- First-created default and `makeDefault` callback/Promise examples: `### New default payment method`, lines 60-87.
- New billing-address precedence and PayPal exclusion: `### New payment method with billing address`, lines 89-116.
- Existing billing-address-ID forms: `### New payment method with existing billing address`, lines 118-141.
- Duplicate-rejection option and payment-method exclusions: `### Preventing duplicate payment methods`, lines 143-170.
- Default credit-card validation versus verification, manual verification, and Premium Fraud Management Tools `device_data` guidance: `### Card verification`, lines 172-202.
- Nonce-versus-raw-card recommendation and field precedence: `### Payment method nonces vs. raw card data`, lines 205-209.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Related source: [[source-braintree-payment-method-nonces]]

## Related raw API references

- [[raw/braintree/docs/reference/response/payment-method/node-2026-09-16|Braintree Node.js payment-method response reference]] - navigation-only response-object destination; not used as factual evidence here
- [[raw/braintree/docs/guides/payment-method-nonces-2026-09-16|Braintree payment-method nonces guide]] - navigation-only nonce authority; not used as factual evidence here
- [[raw/braintree/docs/guides/credit-cards/server-side/node-2026-09-16|Braintree Node.js server-side credit-card guide]] - navigation-only card-verification destination; not used as factual evidence here
- [[raw/braintree/docs/guides/premium-fraud-management-tools/server-side/node-2026-09-16|Braintree Node.js Premium Fraud Management Tools guide]] - navigation-only `device_data` destination; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/request/payment-method/create/node-2026-09-16|Braintree Node.js payment-method-create request reference]] - complete collected page covering creation prerequisites, defaults, billing addresses, duplicate prevention, verification, and nonce/raw-data precedence
