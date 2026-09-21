---
title: "Braintree Payment Method Update (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/payment-method/update/node"
raw_files:
  - "braintree/docs/reference/request/payment-method/update/node-2026-09-16.md"
tags: [braintree, node-js, payment-method, vault, card-verification, paypal]
---

## Overview

This Braintree Node.js request reference documents updating a stored payment method by token. It covers billing-address replacement or reuse, the limited PayPal-account update surface, default-payment-method selection, credit-card verification, and nonce-based credit-card updates.

## Key takeaways

- `gateway.paymentMethod.update()` identifies the stored payment method by token. If it cannot be found, the operation returns Braintree's linked `notFoundError`.
- For billing addresses, `billingAddress.options.updateExisting: true` updates the existing address and therefore also affects any other payment methods associated with that same address. Omitting `updateExisting` creates a new address and leaves the old address in the customer's Vault; an existing customer address can instead be selected by `billingAddressId`.
- A PayPal account update is limited to changing its associated token or making it the customer's default payment method. This call can make only a credit card or PayPal account the default; Braintree recommends the separate customer-update route. The collected sentence for other payment-method types is damaged after naming `default_payment_method_token`, so this source does not reconstruct the missing destination.
- Credit-card validations run by default, but verification does not. Account-enabled AVS/CVV checks run during payment-method update and can be skipped with `verifyCard: false`; manual verification uses `verifyCard: true`. When Premium Fraud Management Tools are used, Braintree strongly recommends supplying `device_data` whenever a card is verified.
- For a credit-card update using a nonce, a field already supplied by the client inside nonce data should not also be passed explicitly. The nonce must not be associated with a customer; a nonce created with a customer ID in its authorization raises the linked cannot-update-card error. Passing raw card data together with a nonce is possible but discouraged: explicit fields take precedence and remaining attributes come from the nonce.

## Detail locators

- Base Node update call and token position: `# Payment Method: Update > ### Node`, lines 22-32.
- Existing-address mutation, shared-address effect, omitted-`updateExisting` behavior, and `billingAddressId` reuse: `## Examples > ### Update billing address` through `## Update with existing billing address`, lines 37-108.
- PayPal-account token restriction: `### Updating a PayPal account token`, lines 110-125.
- Type-specific default selection, damaged non-card destination, and recommended customer-update route: `## Make default`, lines 127-149.
- Validation, verification, AVS/CVV, `verifyCard`, and Premium Fraud Management Tools guidance: `### Card verification`, lines 152-178.
- Nonce plus additional parameters, duplicate-field warning, customer-association restriction, verification-transaction/CVV condition, and raw-data precedence: `### Updating with a nonce and additional parameters` through `### Payment method nonces vs. raw card data`, lines 181-239.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/payment-method/update/node-2026-09-16|Braintree Node.js payment-method update reference]] - complete page covering stored payment-method updates, billing-address behavior, PayPal and default-selection limits, verification conditions, and nonce handling
