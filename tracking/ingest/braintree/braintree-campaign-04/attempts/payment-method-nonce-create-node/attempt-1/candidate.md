---
title: "Braintree Payment Method Nonce Create (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/payment-method-nonce/create/node"
raw_files:
  - "braintree/docs/reference/request/payment-method-nonce/create/node-2026-09-16.md"
tags: [braintree, node-js, payment-method-nonce, server-sdk, 3d-secure, paypal]
---

## Overview

This Braintree Node.js server SDK reference documents `gateway.paymentMethodNonce.create()` for creating a payment-method nonce from a payment-method token. Braintree explicitly says merchants should only create payment-method nonces server-side when using 3D Secure or Checkout with PayPal.

## Key takeaways

- The only input this page requires for nonce creation is the payment-method token.
- The callback and Promise examples both call `gateway.paymentMethodNonce.create("A_PAYMENT_METHOD_TOKEN")` and retrieve the created nonce from `response.paymentMethodNonce.nonce`.
- If the payment method cannot be found, the page routes the failure to Braintree's Node.js `notFoundError` reference.

> [!warning] Server-side creation scope
> Braintree says payment-method nonces should only be created server-side for 3D Secure or Checkout with PayPal. This reference does not broaden server-side nonce creation beyond those named use cases.

## Detail locators

- Related response object and server-side creation warning: `# Payment Method Nonce: Create`, lines 15-18.
- Required input and callback example: `# Payment Method Nonce: Create`, lines 20-26.
- Promise example: `# Payment Method Nonce: Create` > `### Promise`, lines 28-32.
- Missing-payment-method failure route: line 34, immediately after the Promise example.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Related source: [[source-braintree-payment-method-nonces]]

## Raw Sources

- [[raw/braintree/docs/reference/request/payment-method-nonce/create/node-2026-09-16|Braintree Node.js payment-method nonce create reference]] - complete page covering the server-side use-case restriction, required payment-method-token input, callback and Promise forms, and missing-payment-method failure route
