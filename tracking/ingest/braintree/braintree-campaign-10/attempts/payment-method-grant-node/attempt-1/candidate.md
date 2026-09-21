---
title: "Braintree Payment Method Grant (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/payment-method/grant/node"
raw_files:
  - "braintree/docs/reference/request/payment-method/grant/node-2026-09-16.md"
tags: [braintree, node-js, payment-method, grant-api, limited-release]
---

## Overview

This Braintree Node.js reference documents the limited-release Grant API operation for giving another Braintree merchant controlled access to one of the granting merchant's customer's payment methods. The example uses the recipient's access token and returns a payment-method nonce for the recipient.

## Key takeaways

- The Grant API is currently in limited release. Braintree directs merchants to contact it to assess fit and request API access; the page does not establish general merchant availability.
- The stated scope is controlled access by another Braintree merchant to one payment method belonging to the granting merchant's customer. It does not grant generic access to the customer, all Vault payment methods, or the merchant account, and it does not describe transfer of ownership, deletion, or revocation.
- The Node example initializes `BraintreeGateway` with `accessTokenForRecipient`, then calls `gateway.paymentMethod.grant()` with `the_payment_method_token`. Its options example sets `allow_vaulting: false` and `include_billing_postal_code: true`; this page does not define those options' defaults or broader permission effects.
- The callback reads `grantResult.paymentMethodNonce.nonce` into `nonceToSendToRecipient`. The page does not establish nonce lifetime, reuse, transaction success, payment authorization, or settlement.

## Detail locators

- Limited-release status and access-request route: `# Payment Method: Grant > **AVAILABILITY**`, lines 17-18.
- Grant purpose and participating merchant/customer/payment-method identities: `# Payment Method: Grant`, lines 20-21.
- Recipient access-token gateway initialization: `### Node`, lines 22-26.
- Payment-method token, displayed options, and returned nonce handoff: `### Node`, lines 27-37.

## Evidence limitations

> [!warning] Controlled grant, not generic permission
> This page establishes only the named controlled-access grant and the displayed Node handoff. It does not define account-wide permissions, payment-method ownership transfer, revocation or deletion behavior, option defaults, or downstream payment outcomes.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/payment-method/grant/node-2026-09-16|Braintree Node.js payment-method grant reference]] - complete page covering limited-release availability, participating identities, controlled-access scope, and the recipient-token/nonce example
