---
title: "Braintree Payment Method Grant Revocation (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/payment-method/revoke/node"
raw_files:
  - "braintree/docs/reference/request/payment-method/revoke/node-2026-09-16.md"
tags: [braintree, node-js, payment-method, grant-api, vault, limited-release]
---

## Overview

This Braintree Node.js reference documents revoking a payment-method grant made through the limited-release Grant API. The stated effect is deletion of the granted version of the payment method from the receiving merchant's Vault.

## Key takeaways

- The Grant API is currently in limited release. Braintree directs merchants to contact it to assess fit and request access; the page does not establish general merchant availability.
- The surrounding Grant API scope is controlled access by another Braintree merchant to one payment method belonging to the granting merchant's customer.
- Revoking the grant deletes the version of that payment method from the receiving merchant's Vault. This is grant revocation, not the general `paymentMethod.delete()` operation; the page does not say that it deletes the granting merchant's original payment method or cancels associated subscriptions.
- The Node example passes `theToken` to `gateway.paymentMethod.revoke()` and exposes `err` and `result` in the callback. The page supplies no result fields, success condition, failure behavior, timing, downstream transaction effect, or additional cascade.

## Detail locators

- Limited-release status and access-request route: `# Payment Method: Revoke > **AVAILABILITY**`, lines 18-19.
- Grant purpose and participating merchant/customer/payment-method scope: `# Payment Method: Revoke`, line 21.
- Revocation effect on the receiving merchant's Vault version: `# Payment Method: Revoke`, line 23.
- Node token invocation and callback shape: `### Node`, lines 24-30.

## Evidence limitations

> [!warning] Grant revocation is not payment-method deletion
> The page establishes deletion only of the receiving merchant's granted Vault version. It does not state effects on the granting merchant's original payment method, subscriptions, transactions, previously issued nonces, or other recipient state; do not import the separate payment-method deletion operation's cascade.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/payment-method/revoke/node-2026-09-16|Braintree Node.js payment-method grant revocation reference]] - complete page covering limited-release availability, controlled-grant scope, receiving-Vault deletion effect, and the token-based Node invocation
