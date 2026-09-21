---
title: "Braintree Customer Delete (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/customer/delete/node"
raw_files:
  - "braintree/docs/reference/request/customer/delete/node-2026-09-16.md"
tags: [braintree, node-js, customers, payment-method, subscriptions]
---

## Overview

This Braintree Node.js reference documents `gateway.customer.delete()` for deleting a customer by customer ID. It also identifies the operation's cascading effects on the customer's associated payment methods and recurring billing subscriptions.

## Key takeaways

- Delete the customer by passing its ID to `gateway.customer.delete()`.
- When a customer is deleted, all associated payment methods are also deleted.
- All recurring billing subscriptions associated with that customer are canceled.

> [!warning] Cascading deletion
> Customer deletion affects more than the customer record: the page states that every associated payment method is deleted and every associated recurring billing subscription is canceled. This page does not state cancellation timing or any refund, proration, or paid-term outcome.

## Detail locators

- Customer-ID input and both cascading effects: `# Customer: Delete`, lines 15-16.
- Node.js callback invocation: `# Customer: Delete > ### Node`, lines 17-21.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/customer/delete/node-2026-09-16|Braintree Node.js customer-delete reference]] - complete page covering deletion by customer ID, associated payment-method deletion, recurring billing subscription cancellation, and the Node.js invocation
