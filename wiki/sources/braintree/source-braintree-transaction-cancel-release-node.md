---
title: "Braintree Transaction Cancel Release (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction/cancel-release/node"
raw_files:
  - "braintree/docs/reference/request/transaction/cancel-release/node-2026-09-16.md"
tags: [braintree, node-js, transactions, marketplace, escrow]
---

## Overview

This Braintree Node.js reference documents `gateway.transaction.cancelRelease()` for Braintree Marketplace merchants. It applies after an escrowed Marketplace transaction has previously been released and allows that release to be cancelled while the transaction's `escrow_status` is `release_pending`.

## Key takeaways

- The functionality is specific to Braintree Marketplace merchants; the page does not establish availability for ordinary Braintree merchant integrations.
- The callback and Promise examples pass a transaction ID to `cancelRelease()`. They show generic result handlers but no result properties, success condition, returned status, or completed lifecycle outcome.
- The eligible state is narrow: an escrowed Braintree Marketplace transaction must have been previously released, and its `escrow_status` must still be `release_pending`.
- Cancelling a release is not documented here as a refund or transaction cancellation. The page does not state the resulting escrow status or any settlement, disbursement, buyer-funds, or later-release effect.
- If the transaction cannot be found, the page routes the failure to the separate Node.js `notFoundError` reference.

> [!warning] Cancel-release is not refund evidence
> This operation cancels a previously requested escrow release under the stated `release_pending` condition. Do not treat its name or generic result handlers as proof of a refund, transaction cancellation, returned escrow status, or completed downstream outcome.

## Detail locators

- Transaction response-object navigation: `# Transaction: Cancel Release`, line 15.
- Braintree Marketplace merchant qualification: line 17.
- Callback invocation and generic result handler: `### Callback`, lines 18-23.
- Promise invocation and generic result handler: `### Promise`, lines 25-31.
- Missing-transaction route and prior-release plus `release_pending` eligibility: lines 32-34.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Prior escrow-placement operation: [[source-braintree-transaction-hold-in-escrow-node]]
- Distinct refund operation: [[source-braintree-transaction-refund-node]]

## Related raw API references

- [[raw/braintree/docs/reference/response/transaction/node-2026-09-16|Braintree Node.js Transaction response reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/braintree-marketplace/overview-2026-09-16|Braintree Marketplace overview]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/braintree-marketplace/create/node-2026-09-16|Braintree Node.js Marketplace transaction-creation guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/statuses-2026-09-16|Braintree status reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/exceptions/node-2026-09-16|Braintree Node.js exceptions reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction/cancel-release/node-2026-09-16|Braintree Node.js cancel-release request reference]] - complete collected page covering Marketplace scope, callback and Promise invocation, not-found navigation, and the prior-release plus `release_pending` condition
