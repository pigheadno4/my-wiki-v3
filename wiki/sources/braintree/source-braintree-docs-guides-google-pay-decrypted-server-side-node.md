---
title: "Braintree Google Pay Decrypted Server-Side Implementation (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/google-pay/decrypted-server-side/node"
raw_files:
  - "braintree/docs/guides/google-pay/decrypted-server-side/node-2026-09-16.md"
tags: [braintree, google-pay, decrypted-payment-data, server-side, node-js]
---

## Overview

This Braintree Google Pay guide is a Node.js-routed server-side webpage for creating a sale transaction when the merchant server has already decrypted the encrypted Google Pay payment data. It uses the decrypted card values in an `androidPayCard` request rather than the normal client-produced nonce handoff described by the sibling server-side route.

## Key takeaways

- Braintree warns that server-side decryption is not recommended because it increases risk and compliance burden, and points to the Google Pay getting-started route for its recommended integration method.
- The Callback and Promise examples pass decrypted card values to `gateway.transaction.sale()` under `androidPayCard` and request settlement submission; if the decrypted data contains an electronic commerce indicator (ECI), the page says it must be included.
- The page says the amount in the client-side payment request should reflect the amount actually authorized and submitted for settlement, while noting that transactions can still process when the amount changes during order fulfillment.

## Detail locators

- Server-side decryption risk/compliance warning and recommended-method route: opening `IMPORTANT`, lines 17-18.
- Decrypted-parameter transaction purpose and conditional ECI requirement: `## Creating transactions`, lines 21-26.
- Callback `gateway.transaction.sale()` example and decrypted `androidPayCard` fields: `### Callback`, lines 29-55.
- Promise variant of the same sale request: `### Promise`, lines 57-83.
- Client-request versus authorization/settlement amount guidance: lines 84-86.

## Scope and evidence boundary

This is a 2026-09-16 snapshot of an unversioned Braintree webpage selected through its Node.js documentation route. It assumes that the merchant server has already decrypted Google Pay payment data and is distinct from the normal Braintree client-nonce/device-data server handoff; it does not identify an exact Node package or runtime, establish environment or merchant applicability, prove current availability, or demonstrate authorization or settlement success.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- [[source-braintree-docs-guides-google-pay-server-side-node]] - separate normal server-side route for a client-produced Google Pay nonce and device data

## Raw Sources

- [[raw/braintree/docs/guides/google-pay/decrypted-server-side/node-2026-09-16|Braintree Google Pay Decrypted Server-Side Implementation - Node.js]] - complete collected webpage for merchant-decrypted card transaction parameters and warnings
