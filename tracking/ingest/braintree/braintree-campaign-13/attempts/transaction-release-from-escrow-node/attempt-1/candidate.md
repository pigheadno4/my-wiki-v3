---
title: "Braintree Transaction Release from Escrow (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction/release-from-escrow/node"
raw_files:
  - "braintree/docs/reference/request/transaction/release-from-escrow/node-2026-09-16.md"
tags: [braintree, node-js, transactions, marketplace, escrow]
---

## Overview

This Braintree Node.js request reference documents `gateway.transaction.releaseFromEscrow()` for releasing funds from a Braintree Marketplace transaction's escrow. It shows callback and Promise invocation by transaction ID, the `held` escrow-status prerequisite, stated fund distribution, and missing-transaction behavior.

## Key takeaways

- The page scopes this functionality specifically to Braintree Marketplace merchants. It does not establish availability for ordinary Braintree transactions or another marketplace product.
- Both Node examples call `gateway.transaction.releaseFromEscrow()` with a transaction ID. The callback body and Promise resolution handler are empty, so the page demonstrates invocation forms but does not expose a success flag, returned transaction, resulting escrow status, or other result shape.
- If the transaction cannot be found, the page routes the outcome to Braintree's Node.js `notFoundError` reference. It does not document other failure modes here.
- For a released Braintree Marketplace transaction, the page says Braintree disburses the service fee less processing fees to the master merchant account and the remaining funds to the sub-merchant on the business day after the release request is submitted.
- A transaction's `escrow_status` must be `held` before its funds can be released. This prerequisite does not itself document how funds were held, whether release can later be cancelled, or any post-release lifecycle state.

## Scope boundary

This page documents release from escrow. It does not document holding funds in escrow, cancelling a release, refunding a transaction, or a resulting transaction or escrow-status transition. The empty handlers must not be treated as evidence of those outcomes.

## Detail locators

- Braintree Marketplace merchant qualification: `# Transaction: Release From Escrow`, line 17.
- Callback and Promise `gateway.transaction.releaseFromEscrow()` invocation, empty handlers, and missing-transaction route: `### Callback` and `### Promise`, lines 18-30.
- Master-merchant/sub-merchant distribution and next-business-day timing: `# Transaction: Release From Escrow`, line 32.
- Required `held` escrow status: `# Transaction: Release From Escrow`, line 34.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Marketplace escrow-status lookup: [[source-braintree-transaction-find-node]]

## Related raw API references

- [[raw/braintree/docs/reference/request/transaction/hold-in-escrow/node-2026-09-16|Braintree Node.js Hold in Escrow reference]] - navigation-only route for the distinct hold operation; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/transaction/cancel-release/node-2026-09-16|Braintree Node.js Cancel Release reference]] - navigation-only route for the distinct cancellation operation; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction/release-from-escrow/node-2026-09-16|Braintree Node.js release-from-escrow reference]] - complete collected page covering Marketplace scope, release invocation, empty result handlers, fund distribution, timing, not-found routing, and the `held` prerequisite
