---
title: "Braintree Settlement Responses"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/processor-responses/settlement-responses"
raw_files:
  - "braintree/docs/reference/general/processor-responses/settlement-responses-2026-09-16.md"
tags: [braintree, settlement, processor-responses, capture, refunds]
---

## Overview

This Braintree reference classifies 4000-class processor responses for requests to capture funds and says Braintree updates the transaction status according to the processor response. It separates settled approval, settlement-pending and decline responses so a pending response is not mistaken for final settlement.

## Key takeaways

- Braintree describes 4000-class codes as indicating success or failure of a request to capture funds and says the processor response is used to update transaction status.
- Approval code `4000` is labeled `Settled`. The separate pending-request code `4002` is labeled `Settlement Pending`; it is not the settled approval and does not by itself establish final settlement.
- Decline code `4001` means the processor declined to settle the sale or refund request. The decline table also routes already-captured, already-refunded, PayPal risk, capture-amount-limit and PayPal refund/account conditions to their exact response rows.
- `4018 PayPal Pending Payments Not Supported` appears under declines, not under pending requests: it covers a PayPal pending sale or refund response that Braintree disallows, says account misconfiguration is a likely cause and directs readers to transaction details. It should not be collapsed into `4002 Settlement Pending`.

## Detail locators

- 4000-class capture-request scope and transaction-status update: `# Settlement`, lines 16-17.
- Settled approval code: `## Approvals`, lines 18-22.
- Settlement-pending response: `## Pending requests`, lines 25-29.
- Processor settlement decline and other decline categories: `## Declines`, lines 32-49.
- Disallowed PayPal pending-payment response and transaction-detail route: `## Declines`, line 41.

## Evidence limitations

> [!warning] Pending response is not final settlement
> Code `4002 Settlement Pending` is documented separately from `4000 Settled`. This response table does not establish when or whether a pending transaction will reach final settlement, confirm funds movement, or provide a general safe-retry rule. Follow the transaction's updated status and the applicable operation-specific authority before fulfillment or another capture/refund attempt.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Settlement-submission operation: [[source-braintree-transaction-submit-for-settlement-node]]
- Refund operation and settlement-failure route: [[source-braintree-transaction-refund-node]]

## Raw Sources

- [[raw/braintree/docs/reference/general/processor-responses/settlement-responses-2026-09-16|Braintree settlement responses]] - complete collected response table separating settled approval, settlement pending and decline codes
