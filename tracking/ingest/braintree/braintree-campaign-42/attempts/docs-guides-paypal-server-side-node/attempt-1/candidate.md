---
title: "Braintree PayPal Server-Side Implementation (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/server-side/node"
raw_files:
  - "braintree/docs/guides/paypal/server-side/node-2026-09-16.md"
tags: [braintree, paypal, node, server-side, transactions, settlement]
---

## Overview

This 2026-09-16 Braintree website snapshot is a Node.js server-side guide for creating PayPal-backed Braintree transactions, updating a PayPal payment resource after buyer approval and before vaulting, and handling related device-data, currency, shipping, settlement and recurring-transaction conditions. It is snapshot documentation, not proof of current SDK behavior, merchant eligibility, account configuration, transaction success, capture, settlement or funding. [[braintree]] [[paypal-braintree-integration]]

## Key takeaways

- The callback and Promise examples build a sale request with `paymentMethodNonce`, optional `deviceData`, `orderId`, `options.submitForSettlement: true` and PayPal-specific custom-field/description values, then submit it through `gateway.transaction.sale(...)`. The introductory sentence at line 25 has lost the parameter and call names, so the examples are the precise captured locator rather than a reconstruction of that sentence.
- For edge cases where transaction values such as the total change after buyer approval, the guide says updated line items are essential so the final amount is correct. It places `PayPalPaymentResource.update()` after payment-resource tokenization and before `Customer.create()` vaulting. `paymentMethodNonce` is required, and the new nonce returned by `update()` must be passed to `Customer.create()` for the updated resource to be vaulted. Optional fields should be limited to what the use case changes.
- When a PayPal transaction comes from a Vault record and is not recurring, the guide advises collecting client device data and submitting it as top-level `deviceData`/`device_data` to help reduce declines. This is a conditional recommendation, not a guarantee of approval.
- The charged currency follows the `merchant_account_id` used by the transaction call. A collected shipping address must be passed with the transaction and must follow PayPal address conventions, but the captured required-field list is blank; use the linked transaction reference rather than reconstructing those fields from this snapshot.
- PayPal funds are described as captured immediately when each transaction is submitted for settlement rather than settling in batches. Settlement above the authorized amount is unavailable unless the merchant's industry and processor support settlement adjustment; exceeding the permitted limit produces a settlement response code. The page also states that multiple partial settlements can cover the total authorization for multiple physical-goods shipments, but the method name is missing from the captured sentence.
- For merchant-initiated transactions from a vaulted PayPal record while the customer is absent, custom recurring logic must include `transactionSource: "recurring"`; Braintree recurring billing is described as setting that parameter automatically.

## Detail locators

- **Creating transactions and post-approval update:** lines 23-34.
- **Supported update request example:** lines 37-101.
- **Vault-origin device-data condition and callback/Promise sale examples:** lines 103-167.
- **Vault-on-success navigation and currency behavior:** lines 169-174.
- **Shipping-address requirement, damaged field list and Seller Protection lookup:** lines 177-216.
- **Settlement timing, over-authorization limit and partial-settlement statement:** lines 218-230.
- **Recurring transaction classification and callback/Promise examples:** lines 231-266.

## Related

- Company: [[braintree]]
- Concept: [[paypal-braintree-integration]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/server-side/node-2026-09-16|Braintree PayPal server-side Node.js guide (2026-09-16 snapshot)]]
