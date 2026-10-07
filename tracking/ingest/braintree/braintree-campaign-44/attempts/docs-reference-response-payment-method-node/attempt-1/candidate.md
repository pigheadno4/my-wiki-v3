---
title: "Braintree Payment Method Response Reference (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/payment-method/node"
raw_files:
  - "braintree/docs/reference/response/payment-method/node-2026-09-16.md"
tags: [braintree, node-js, payment-methods, response-objects]
---

## Overview

This collected Braintree Node.js website response reference is an orientation page for the generic Payment Method object. It routes readers to the listed payment-method-type response pages and shows how returned objects are checked for customer-default status and distinguished by runtime class.

## Key takeaways

- The page directs type-specific attribute lookup to the linked Android Pay Card, Apple Pay Card, Credit Card, PayPal Account, US Bank Account, Venmo Account and Visa Checkout Card response objects; the links are navigation, not a shared property schema.
- In the Node.js example, `paymentMethod.default` is the value inspected to determine whether that returned payment method is the customer's default.
- To distinguish returned payment-method types, the page says to inspect the object's class; its callback and promise examples use `instanceof` checks for `braintree.CreditCard`, `braintree.PayPalAccount`, `braintree.ApplePayCard` and `braintree.AndroidPayCard`.

> [!warning] Incomplete containing-response sentence
> The captured sentence `Payment method objects included in other responses (such as) may be any of these types.` has no example after `such as`. This snapshot therefore does not identify or exhaustively enumerate the containing response families.

## Detail locators

- Generic-object identity and links to type-specific response objects: `# Payment Method`, lines 14-26.
- Damaged containing-response sentence and callback/promise examples returning `customer.paymentMethods`: lines 28-42.
- Customer-default check: `### Default`, lines 47-53.
- Runtime-class type check, including callback and promise examples: `### Determine payment method type`, lines 55-95.

## Scope and boundaries

This is a 2026-09-16 snapshot of an unversioned Node.js documentation route. It describes response-object consumption: the shown `customer.find` and `paymentMethod.find` calls are examples whose returned values are inspected, not a request-schema contract. The route names no exact SDK package version or environment, and its type links and examples do not establish product availability or a payment outcome.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/response/payment-method/node-2026-09-16|Braintree Payment Method response reference - Node.js]] - complete collected page containing the type navigation, default check and runtime-class examples
