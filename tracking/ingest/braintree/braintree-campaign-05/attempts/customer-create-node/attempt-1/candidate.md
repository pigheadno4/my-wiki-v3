---
title: "Braintree Customer Create (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/customer/create/node"
raw_files:
  - "braintree/docs/reference/request/customer/create/node-2026-09-16.md"
tags: [braintree, node-js, customers, payment-method, card-verification, custom-fields]
---

## Overview

This Braintree Node.js request guide documents `gateway.customer.create()` for creating a customer alone, with a payment method, or with a credit card and billing address. It routes implementers to optional customer-ID, payment-method token, card-verification, billing-address, and custom-field variants while retaining validation and setup qualifications.

## Key takeaways

- A merchant may supply its own customer ID, and the page says customer IDs are case insensitive.
- When creating a payment method with the customer, success is conditioned on the applicable customer and credit-card or PayPal-account validations passing, and on a supplied credit card passing verification when verification is requested. If no payment-method token is supplied, the gateway generates one; a custom integration may instead choose the token.
- Card validation runs by default, but card verification does not. Braintree strongly recommends enabling account-wide verification before cards are stored in the Vault; the manual example sets `verifyCard: true`.
- Premium Fraud Management Tools users are strongly advised to pass `device_data` each time they verify a card. Custom fields must be configured in the Control Panel before they are used through the API.

## Variant and detail locators

- Base Node.js callback and returned `result.success` / `result.customer.id` reads: `# Customer: Create > ### Node`, lines 24-40.
- Merchant-supplied customer ID, callback, and Promise variants: `## Examples > ### Specify your own customer ID`, lines 46-69.
- Payment-method creation, validation conditions, generated/custom tokens, callback, and Promise variants: `## Examples > ### Customer with a payment method`, lines 77-106.
- Payment method with a nested billing address: `#### Customer with a payment method and billing address`, lines 109-153.
- Default validation-versus-verification behavior, account-wide recommendation, manual `verifyCard` examples, and the Premium Fraud Management Tools `device_data` advisory: `#### Card verification`, lines 155-192.
- Control Panel prerequisite and callback/Promise custom-field examples: `### Use custom fields`, lines 197-242.

## Collected evidence limitations

> [!warning] Incomplete transaction note
> The opening NOTE at lines 20-21 says that a different route may be preferable when creating a transaction and customer together, but the collected sentence is missing the action and option names (`usewith either theoroptions`). This source does not reconstruct them; use the dedicated transaction reference before implementing that combined flow.

> [!info] Missing blank-customer example
> The `### Blank customer` section at lines 72-75 states that a blank customer can be created when only a payment method is being stored, but the collected page contains no invocation beneath that heading. It therefore does not supply a usable blank-customer Node.js example.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/customer/create/node-2026-09-16|Braintree Node.js customer-create request guide]] - complete collected page covering customer creation variants, validation and verification qualifications, Control Panel-configured custom fields, and retained missing-prose/example gaps
