---
title: "Braintree Payment Method Find (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/payment-method/find/node"
raw_files:
  - "braintree/docs/reference/request/payment-method/find/node-2026-09-16.md"
tags: [braintree, node-js, payment-method, vault, paypal]
---

## Overview

This Braintree Node.js reference documents lookup of a payment method by its token through `gateway.paymentMethod.find()`. It also provides callback and Promise examples for finding a single PayPal account by token through `gateway.paypalAccount.find()`.

## Key takeaways

- The general Node.js example passes a payment-method token to `gateway.paymentMethod.find()` and receives a payment-method result in its callback. This is payment-method token lookup, not payment-method nonce lookup.
- The page states that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. Because that external policy was not part of this source, this entry preserves the limitation notice without inferring what data is hidden, retained, or returned.
- For a single PayPal account, the page directs readers to the PayPal-account `find` method and shows both callback and Promise forms using the account token. If that PayPal account cannot be found, the page routes the outcome to Braintree's Node.js `notFoundError` reference.
- The page links to the Payment Method response-object reference for result details; this source does not reconstruct that unread response schema.

## Detail locators

- Results-limitation notice: `# Payment Method: Find`, lines 16-17.
- General payment-method lookup purpose and Node.js callback example: `# Payment Method: Find > ### Node`, lines 19-24.
- Single-PayPal-account purpose and callback example: `## Examples > ### Single PayPal account > ### Callback`, lines 29-36.
- PayPal-account Promise example and missing-account error route: `## Examples > ### Single PayPal account > ### Promise`, lines 38-43.

## Related

- Company: [[braintree]]
- Concept: [[braintree-server-sdk]]
- Distinct operation: [[source-braintree-payment-method-nonce-find-node]]

## Raw Sources

- [[raw/braintree/docs/reference/request/payment-method/find/node-2026-09-16|Braintree Node.js payment-method find reference]] - complete page covering token lookup, the results-limitation notice, and the PayPal-account examples
