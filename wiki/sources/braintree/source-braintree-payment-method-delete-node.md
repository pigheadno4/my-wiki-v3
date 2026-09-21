---
title: "Braintree Payment Method Delete (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/payment-method/delete/node"
raw_files:
  - "braintree/docs/reference/request/payment-method/delete/node-2026-09-16.md"
tags: [braintree, node-js, payment-method, vault, subscriptions]
---

## Overview

This Braintree Node.js reference documents deleting a payment method by its token with `gateway.paymentMethod.delete()`. The operation has an immediate destructive subscription consequence: all subscriptions associated with the payment method are canceled, and the customer forfeits any remaining days already paid for.

## Key takeaways

- Delete the payment method by passing its token to `gateway.paymentMethod.delete()`.
- Deletion immediately cancels all subscriptions associated with that payment method.
- The customer forfeits any remaining days already paid for; this consequence should be considered before invoking deletion.

## Detail locators

- Deletion by token and subscription consequences: `# Payment Method: Delete`, lines 15-16.
- Node.js invocation: `### Node`, lines 17-20.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/payment-method/delete/node-2026-09-16|Braintree Node.js payment-method delete reference]] - complete page covering token-based deletion, immediate associated-subscription cancellation, paid-day forfeiture, and the Node.js invocation
