---
title: "Braintree Transaction Submit for Settlement (Node.js)"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction/submit-for-settlement/node"
raw_files:
  - "braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16.md"
tags: [braintree, node-js, transactions, settlement, authorization-adjustments]
---

## Overview

This Braintree reference page documents the Node.js server SDK's `gateway.transaction.submitForSettlement()` operation for explicitly submitting a transaction for settlement. It is also the retrieval route for changing the settlement amount and for conditionally adding Level 2/3 or shipping data at settlement submission.

## Key takeaways

- The callback and Promise examples call `submitForSettlement()` with a transaction ID. On success, the examples read the transaction from `result.transaction`; unsuccessful callback and Promise examples expose errors or a message.
- A merchant can specify an amount different from the total authorization amount; omitting the amount settles the entire amount. An amount below the total authorization can be submitted this way only once. Multiple partial settlements instead use separate partial-settlement functionality, which this page limits to PayPal and Venmo transactions and some credit-card transactions for select merchants.
- For eligible merchants, submitting an amount above or below the original authorized amount triggers an authorization adjustment automatically. Braintree limits authorization adjustments to select merchants and processors, records adjustment attempts on the transaction response, and routes real-time declines through validation errors; merchants should confirm eligibility with Braintree.
- Adding Level 2/3 data through submit for settlement requires internal approval. Data supplied there overrides Level 2/3 data from the sale request, and the page recommends providing it through either the sale request or settlement submission, not both.
- Sending shipping-address fields through submit for settlement also requires internal approval. Those fields override corresponding shipping-address fields from the sale request, and the page likewise recommends choosing one of the two request points.

## Important source limitation

> [!warning] Incomplete source text
> The introductory sentence is incomplete after the `options.submit_for_settlement` link (`option with, then ...`). This source does not reconstruct the omitted wording; the operation identity and examples are taken from the page title and explicit Node calls. The raw also contains incomplete Ruby-only fragments that are not used for this Node.js retrieval entry.

## Detail locators

- Explicit Node callback operation and success/error branches: `# Transaction: Submit For Settlement > ### Node`.
- Amount changes, default full amount, once-only lower-amount submission, and partial-settlement availability: `## Examples > ### Specifying settlement amount`.
- Automatic adjustment behavior, recorded adjustment details, real-time decline route, and availability: `### Specifying settlement amount > #### Authorization adjustments` and `#### Availability`.
- Approval requirement, override behavior, and full Node callback/Promise examples for supplemental transaction data: `### Specifying Level 2 and 3 data`.
- Shipping-address override and approval requirement: `### Shipping address information`.
- The Node order-ID callback and Promise examples remain in `### Specifying order ID`; the incomplete Ruby fragment there is not interpreted.

## Related

- Company: [[braintree]]
- Concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16|Braintree Node.js submit-for-settlement reference]] — fully read page covering explicit settlement submission, settlement amounts, authorization adjustments, and approval-gated supplemental data
