---
title: "Braintree Transaction Hold In Escrow (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction/hold-in-escrow/node"
raw_files:
  - "braintree/docs/reference/request/transaction/hold-in-escrow/node-2026-09-16.md"
tags: [braintree, node-js, transactions, marketplace, escrow]
---

## Overview

This Braintree Node.js reference documents `gateway.transaction.holdInEscrow()` for Braintree Marketplace merchants. It shows callback and Promise invocations using a transaction ID and limits eligibility to transactions whose status is `authorized` or `submitted_for_settlement`.

## Key takeaways

- Braintree states that this functionality is specific to Braintree Marketplace merchants; the page does not establish availability for ordinary Braintree merchant integrations.
- Both displayed forms pass a transaction ID to `holdInEscrow()`. The callback receives `err` and `result`, while the Promise resolves a `result`, but both handlers are empty and therefore establish no result properties, success test, returned status, or completed escrow outcome.
- A transaction can be held in escrow only when its status is `authorized` or `submitted_for_settlement`. The page does not document how the transaction reached either status or what later escrow transitions occur.
- If the transaction cannot be found, the page routes the failure to the separate Node.js `notFoundError` reference.

> [!warning] Invocation is not lifecycle evidence
> The empty callback and Promise handlers show invocation shape only. They do not prove that the hold succeeded, identify a resulting transaction status, or establish release, cancellation, settlement, disbursement, timing, or failure behavior.

## Detail locators

- Transaction response-object navigation: `# Transaction: Hold In Escrow`, line 15.
- Braintree Marketplace merchant qualification: `# Transaction: Hold In Escrow`, line 17.
- Callback invocation and empty handler: `### Callback`, lines 18-21.
- Promise invocation and empty handler: `### Promise`, lines 23-26.
- Missing-transaction error route and eligible input statuses: lines 27-29.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Marketplace transaction creation route: [[source-braintree-transaction-sale-node]]

## Related raw API references

- [[raw/braintree/docs/reference/response/transaction/node-2026-09-16|Braintree Node.js Transaction response reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/braintree-marketplace/overview-2026-09-16|Braintree Marketplace overview]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/exceptions/node-2026-09-16|Braintree Node.js exceptions reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction/hold-in-escrow/node-2026-09-16|Braintree Node.js hold-in-escrow request reference]] - complete collected page covering Marketplace scope, callback and Promise invocation, not-found navigation, and eligible transaction statuses
