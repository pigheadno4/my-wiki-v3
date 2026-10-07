---
title: "Braintree PayPal Order: Server-Side Implementation (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/paypal-advanced-options/paypal-order/server-side/node"
raw_files:
  - "braintree/docs/reference/general/paypal-advanced-options/paypal-order/server-side/node-2026-09-16.md"
tags: [braintree, paypal, paypal-order, node-js, vault, transactions]
---

## Overview

This [[braintree]] website-reference snapshot, collected 2026-09-16 and routed to Node.js, covers the server-side steps after a customer authenticates with PayPal for a PayPal Order. It documents turning the client nonce into a Vault payment method for a new or existing customer, optionally updating the approved PayPal payment resource before vaulting, processing the Order through Braintree transaction operations, and voiding the Order by deleting its representing payment method. The captured page does not state an exact Node SDK package version.

## Key takeaways

- After successful PayPal authentication, the page directs the merchant to create a payment method for processing transactions against the PayPal Order. It shows separate callback and Promise examples for creating a new Vault customer with `paymentMethodNonce` and for adding a payment method to an existing customer. The prose that should name some methods and parameters is damaged in the collected rendering, so use the displayed code and exact reference routes rather than reconstructing the missing text.
- For an edge case in which transaction parameters change after buyer approval, the server-side `PayPalPaymentResource.update()` call must occur after payment-resource tokenization and before `Customer.create()`. If the total changes, the page says updated line items are essential so the final amount reflects the correct total. The required `paymentMethodNonce` is supplied to the update call, which returns a new nonce that must be passed to `Customer.create()` for the updated resource to be vaulted.
- The update example displays amount, amount breakdown, currency, custom field, description, line items, order ID, payee email, shipping address and shipping options. These are sample values and supported-parameter navigation, not a claim that every field is required or that the example executed successfully.
- The page routes PayPal Order payment processing through Braintree transaction operations for sale, settlement submission, lookup, search, void and refund. Examples and navigation are not proof of successful authorization, settlement, funding, refund or payment execution.
- Currency is tied to the merchant account ID supplied in the transaction call. Passing a shipping address may make a transaction eligible for PayPal Seller Protection, and the status can be inspected on the transaction's PayPal account; neither the address nor the displayed `ELIGIBLE` example guarantees protection.
- The page says a PayPal Order is represented by a customer payment method and that voiding the Order requires deleting that payment method. Deletion is consequential. The captured sentence omits the method name after `calling`, so this source does not establish the exact deletion invocation.

## Evidence limitations

> [!warning] Snapshot, rendering and execution boundaries
> This is a 2026-09-16 Braintree-hosted, Node-routed website snapshot, not direct PayPal Orders API documentation, exact package-version evidence, current merchant eligibility or execution proof. Several collected sentences omit method or parameter names, and the final void sentence omits the deletion call; those gaps are not reconstructed here.

## Detail locators

- Payment-method purpose after PayPal authentication: `## Create payment method`, line 19.
- New-customer callback and Promise examples: `### Create a new customer with a payment method`, lines 20-57.
- Existing-customer callback and Promise examples, plus not-found navigation: `### Update an existing customer with a payment method`, lines 59-81.
- Post-approval update use case, line-item condition and update timing: `### Updating PayPal Payment Resource After Buyer Approval`, lines 82-86.
- Required input nonce, returned replacement nonce and optional-field boundary: note under `### Updating PayPal Payment Resource After Buyer Approval`, lines 89-90.
- Displayed update request fields and values: `### node`, lines 93-157.
- Transaction operation navigation: `## Process transactions`, lines 159-167.
- Merchant-account currency behavior and foreign-currency navigation: `### Currency support`, lines 170-172.
- Conditional Seller Protection eligibility and status examples: `### Seller Protection`, lines 173-190.
- Payment-method deletion requirement and missing invocation text: `## Void an order`, lines 192-194.

## Related

- Company: [[braintree]]
- Concept: [[paypal-braintree-integration]]
- Server SDK context: [[braintree-server-sdk]]
- Payment-method context: [[braintree-payment-methods]]

## Related raw API references

- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Node.js Transaction Sale request]] - unread navigation-only reference
- [[raw/braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16|Node.js Submit for Settlement request]] - unread navigation-only reference
- [[raw/braintree/docs/reference/request/transaction/find/node-2026-09-16|Node.js Transaction Find request]] - unread navigation-only reference
- [[raw/braintree/docs/reference/request/transaction/search/node-2026-09-16|Node.js Transaction Search request]] - unread navigation-only reference
- [[raw/braintree/docs/reference/request/transaction/void/node-2026-09-16|Node.js Transaction Void request]] - unread navigation-only reference
- [[raw/braintree/docs/reference/request/transaction/refund/node-2026-09-16|Node.js Transaction Refund request]] - unread navigation-only reference

## Raw Sources

- [[raw/braintree/docs/reference/general/paypal-advanced-options/paypal-order/server-side/node-2026-09-16|Braintree PayPal Order server-side implementation for Node.js]] - fully read pinned website snapshot
