---
title: "Braintree Transaction Clone Transaction (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction/clone_transaction/node"
raw_files:
  - "braintree/docs/reference/request/transaction/clone_transaction/node-2026-09-16.md"
tags: [braintree, node-js, transactions, cloning, settlement]
---

## Overview

This Braintree Node.js reference documents `gateway.transaction.cloneTransaction()`. Cloning creates a new transaction by copying all attributes except amount from an original transaction; Braintree recommends saving and reusing payment-method or customer information in the Vault instead of cloning in most cases.

## Key takeaways

- The clone is a new transaction, not a mutation of the original. The page says it copies all original transaction attributes except amount, but it does not enumerate those copied attributes.
- Braintree marks both an amount and an option flag that submits the transaction for settlement as required. The callback and Promise examples pass an original transaction ID, amount `"10.00"`, and `options.submitForSettlement: true`; those displayed values are examples rather than a complete input schema.
- The page recommends Vault reuse of payment-method or customer information as the better practice in most cases. This is a recommendation, not a statement that cloning is unavailable.
- If the original transaction cannot be found, the page routes the failure to Braintree's `notFoundError` reference; detailed exception behavior remains in that unread reference.

> [!warning] New-transaction and copied-attribute boundary
> Treat cloning as creation of a separate transaction. The page does not identify the copied attributes individually or establish that lifecycle state, settlement outcome, processor behavior, eligibility, or side effects are identical to the original transaction.

## Detail locators

- New-transaction effect, all-attributes-except-amount copy scope, and recommended Vault alternative: `# Transaction: Clone Transaction`, lines 15-18.
- Required amount and settlement-submission option flag: `# Transaction: Clone Transaction > **IMPORTANT**`, lines 19-20.
- Callback invocation and displayed inputs: `### Callback`, lines 23-36.
- Promise invocation and displayed inputs: `### Promise`, lines 38-51.
- Missing-transaction error route: line 52.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Related operation: [[source-braintree-transaction-sale-node]]

## Related raw API references

- [[raw/braintree/docs/reference/response/transaction/node-2026-09-16|Braintree Node.js Transaction response reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/payment-methods/node-2026-09-16|Braintree Node.js payment-method guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/customers/node-2026-09-16|Braintree Node.js customer guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/exceptions/node-2026-09-16|Braintree Node.js exceptions reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction/clone_transaction/node-2026-09-16|Braintree Node.js transaction-clone request reference]] - complete collected page covering new-transaction creation, copied-attribute scope, required amount and settlement option, Vault recommendation, callback and Promise forms, and the not-found route
