---
title: "Braintree Customer Update (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/customer/update/node"
raw_files:
  - "braintree/docs/reference/request/customer/update/node-2026-09-16.md"
tags: [braintree, node-js, customers, payment-method, card-verification, billing-address]
---

## Overview

This Braintree Node.js request guide documents `gateway.customer.update()` for changing a customer by ID. It distinguishes ordinary attribute updates, existing-credit-card updates, new payment-method association, default-payment-method selection, billing-address handling, and optional card verification.

## Key takeaways

- New attributes are validated under the same customer rules used at creation, while any attribute omitted from the update remains unchanged.
- Updating an existing payment method through the customer-update method is limited here to credit cards and requires the existing card token in `creditCard.options.updateExistingToken`. Omitting that option creates and associates a new credit card instead; more generally, a payment-method nonce can associate a new payment method of any type with the customer.
- For billing addresses, setting the nested update-existing option updates the address. Omitting it creates a new customer address, associates the new address with the credit card, and leaves the old address attached to the customer but no longer as that card's billing address. The page also warns that some credit-card parameters have been deprecated to avoid PCI concerns around raw card data on the server.
- A customer's default payment method is selected by passing that payment method's token as `defaultPaymentMethodToken`.
- Credit-card validation runs by default, but verification does not. Braintree strongly recommends account-wide card verification before Vault storage; the manual example sets `verifyCard: true`. When Premium Fraud Management Tools are used, the page strongly recommends passing `device_data` each time a card is verified.

## Variant and detail locators

- Base update-by-ID behavior, unchanged omitted attributes, and Node callback example: `# Customer: Update`, lines 13-27.
- Existing-credit-card update, credit-card-only qualification, `updateExistingToken`, and callback/Promise examples: `## Examples > ### Update customer and existing credit card`, lines 32-85.
- Billing-address update option, deprecated raw-card parameters, and omission behavior: `### Update customer, credit card, and billing address`, lines 88-135.
- New-credit-card versus any-payment-method association: `### Update customer and create new payment method`, lines 136-181.
- Default-payment-method token selection and callback/Promise examples: `### Update default payment method`, lines 184-203.
- Validation-versus-verification default, account-wide recommendation, manual `verifyCard`, and conditional Premium Fraud Management Tools `device_data` advisory: `### Card verification`, lines 206-240.

## Collected evidence limitation

> [!warning] Missing non-card update route
> The note at lines 36-37 says only credit cards can be updated through the customer-update method and begins to direct other payment-method types elsewhere, but the collected sentence ends at `use.` without naming a method or destination. This source does not reconstruct that missing route; consult the dedicated reference for the payment-method type being updated.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/customer/update/node-2026-09-16|Braintree Node.js customer-update request guide]] - complete collected page covering unchanged omitted attributes, existing versus new payment-method behavior, billing-address handling, default selection, verification qualifications, and the retained missing-route gap
