---
title: "Braintree Customers Guide (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/customers/node"
raw_files:
  - "braintree/docs/guides/customers/node-2026-09-16.md"
tags: [braintree, node-js, customers, vault, payment-methods]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes the customer object as a gateway record for storing and organizing one or more payment methods. Through Node.js callback and Promise examples, it introduces customer creation, update, ID lookup and deletion. This is a documentation snapshot with no exact Node package version; it does not prove current account enablement, exact SDK/runtime behavior, API success or a payment outcome.

## Key takeaways

- A customer can be created without a payment method when the applicable customer validations pass. The displayed names and contact fields are example inputs rather than a complete request contract.
- When planning to use Risk Products, the captured guide says to include the customer's email and phone information. This is page-qualified guidance, not a universal customer-create schema requirement.
- A customer can instead be created with a payment-method nonce. The guide conditions success on customer and payment-method validations and, when card verification is enabled, successful verification of the payment method.
- Braintree strongly recommends account-wide verification before cards are stored in the Vault. The page presents manual `verify_card: true` as an alternative choice, not as a universal request requirement.
- Existing customers can be updated or found by customer ID. For either operation, the guide routes a missing customer to `notFoundError`; the find call returns a Customer response object.
- Deleting by customer ID deletes the customer and its payment methods according to this guide. The dedicated [[source-braintree-customer-delete-node|customer-delete authority]] additionally states that all associated recurring billing subscriptions are canceled; it does not state cancellation timing or any refund, proration or paid-term effect.

> [!warning] Destructive and evidence boundaries
> Customer deletion removes associated payment methods according to this guide. The dedicated [[source-braintree-customer-delete-node|customer-delete authority]] additionally states that all associated recurring billing subscriptions are canceled, without specifying cancellation timing, refunds, proration or paid-term effects. The successful values shown in examples are illustrative documentation, not evidence that an account is enabled or that any request or payment succeeded.

## Detail locators

- Customer-object purpose and its one-to-many payment-method relationship: `# Customers`, line 20. The conditional guidance to include customer email and phone when planning to use Risk Products, plus routes to complete request and response detail, is at lines 22-23.
- Customer-only creation and its validation condition: `## Create`, lines 25-29. Callback and Promise field examples are at lines 32-62.
- Creation with a payment method, callback and Promise examples, and the combined validation/verification condition: `### Create with payment method`, lines 64-94.
- Account-wide card-verification recommendation and manual-verification choice: `**NOTE**`, lines 97-100.
- Customer-ID update examples and missing-customer behavior: `## Update`, lines 103-131.
- Customer-ID lookup, missing-customer behavior and returned Customer response-object route: `## Find`, lines 134-154.
- Destructive customer-and-payment-method deletion, callback/Promise examples and missing-customer behavior: `## Delete`, lines 157-175.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Dedicated create reference: [[source-braintree-customer-create-node]]
- Dedicated update reference: [[source-braintree-customer-update-node]]
- Dedicated find reference: [[source-braintree-customer-find-node]]
- Dedicated destructive delete reference: [[source-braintree-customer-delete-node]]

## Related raw API references

- [[raw/braintree/docs/reference/request/customer/create/node-2026-09-16|Customer create request reference]]
- [[raw/braintree/docs/reference/request/customer/update/node-2026-09-16|Customer update request reference]]
- [[raw/braintree/docs/reference/request/customer/find/node-2026-09-16|Customer find request reference]]
- [[raw/braintree/docs/reference/request/customer/delete/node-2026-09-16|Customer delete request reference]]
- [[raw/braintree/docs/reference/response/customer/node-2026-09-16|Customer response reference]]
- [[raw/braintree/docs/reference/general/validation-errors/all/node-2026-09-16|Node.js validation-errors reference]]
- [[raw/braintree/articles/control-panel/vault/card-verification-2026-09-16|Vault card-verification article]]

## Raw Sources

- [[raw/braintree/docs/guides/customers/node-2026-09-16|Braintree Customers guide (Node.js route)]] - complete collected website page for the customer-object purpose and create, update, find and delete lifecycle
