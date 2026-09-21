---
title: "Braintree Transaction Sale (Node.js)"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/node"
raw_files:
  - "braintree/docs/reference/request/transaction/sale/node-2026-09-16.md"
tags: [braintree, node-js, transactions, settlement, vault]
---

## Overview

This Braintree reference page documents the Node.js server SDK's `gateway.transaction.sale()` request for creating a transaction from an amount and a payment-method nonce, a vaulted payment-method token, or a customer's default payment method. It also routes readers to the page's worked examples for settlement submission, vault storage, merchant-account and address selection, custom fields, dynamic descriptors, and Braintree Marketplace escrow.

## Key takeaways

- A sale requires `amount` plus one of `payment_method_nonce`, `payment_method_token`, or `customer_id`; using `customer_id` selects that customer's default payment method.
- Braintree's transaction risk and fraud products require adequate supporting data, added during the Braintree SDK or GraphQL integration before those products are used.
- The Node example sets `options.submitForSettlement` to request immediate settlement submission. The page says a valid example returns `success` as true with status `submitted_for_settlement`.
- Vaulting can be requested for an existing or new customer, but the `customer` parameter is intended only when creating a new customer with a new payment method, and `store_in_vault_on_success` stores the method only after a successful transaction.
- If `merchant_account_id` is omitted, Braintree uses the default merchant account. Dynamic-descriptor acceptance and formatting vary by processor and payment path, so use the dedicated raw subsections rather than assuming the general example applies everywhere.

## Important documentation inconsistency

> [!warning] Contradiction
> Although this is the Transaction: Sale page, its successful-result example labels `result.transaction.type` as `"credit"`. Verify transaction type against the linked Transaction response documentation or current SDK implementation before relying on that example.

## Detail locators

- The `# Transaction: Sale` introductory risk/fraud paragraph at raw line 19 gives the supporting-data prerequisite and routes to Premium Fraud Management Tools guidance.
- `Examples > Storing in your vault` covers existing-customer and new-customer storage, plus the success condition for `store_in_vault_on_success`.
- `Examples > Using a vaulted payment method` and `Using a CVV-only nonce` distinguish a vaulted token, a customer's default method, and the combined token-plus-CVV-nonce case.
- `Examples > Specify merchant account ID`, `Using stored addresses`, and `Custom fields` contain the corresponding Node callback and Promise examples.
- `Examples > Dynamic descriptors` contains general processor restrictions and separate Venmo, PayPal, and Braintree Marketplace rules, including path-specific character, length, prefix, ignore, and truncation behavior.
- `Examples > Hold a Braintree Marketplace transaction in escrow on creation` shows the escrow option and states that funds are not held by default.

## Related

- Companies: [[braintree]]
- Concepts: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16]] — fully read Braintree Node.js Transaction: Sale reference page
