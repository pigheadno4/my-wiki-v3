---
title: "Braintree Dispute Accept (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/dispute/accept/node"
raw_files:
  - "braintree/docs/reference/request/dispute/accept/node-2026-09-16.md"
tags: [braintree, node-js, disputes]
---

## Overview

This Braintree Node.js reference documents accepting a dispute by ID with `gateway.dispute.accept()`. API dispute management is restricted to merchants who can access disputes in the Braintree Control Panel, and the page preserves an important alternate-evidence route when the disputed transaction was already refunded.

## Key takeaways

- Managing disputes through the API is available only to merchants who can access disputes in the Braintree Control Panel.
- The collected page says that only disputes in a particular status can be accepted, but the status value is missing from the rendered sentence (`status of.`). This source does not reconstruct the missing eligibility value; consult the current dispute-status authority before relying on status eligibility.
- If the merchant has already refunded the disputed transaction, the page explicitly says not to accept the dispute. It directs the merchant to submit file or text evidence of the refund instead.
- The Promise example calls `gateway.dispute.accept("a_dispute_id")`. A successful acceptance produces a successful result; otherwise the page directs readers to validation errors.

## Detail locators

- Dispute response-object route and Control Panel access restriction: `# Dispute: Accept`, lines 13-17.
- Damaged status-eligibility sentence and prior-refund do-not-accept warning with evidence alternatives: `# Dispute: Accept`, lines 19-21.
- `gateway.dispute.accept()` Promise invocation: `# Dispute: Accept > first ### Promise`, lines 22-25.
- Success outcome and validation-error result handling: `# Dispute: Accept`, lines 26-37.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]

## Related raw API references

- [[raw/braintree/docs/reference/response/dispute/node-2026-09-16|Braintree Node.js Dispute response reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/dispute/add-text-evidence/node-2026-09-16|Braintree Node.js add-text-evidence request reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/dispute/accept/node-2026-09-16|Braintree Node.js dispute-accept request reference]] - complete collected page covering access availability, damaged status eligibility, the prior-refund warning, acceptance invocation, and result handling
