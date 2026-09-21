---
title: "Braintree Dispute Remove Evidence (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/dispute/remove-evidence/node"
raw_files:
  - "braintree/docs/reference/request/dispute/remove-evidence/node-2026-09-16.md"
tags: [braintree, node-js, disputes, evidence]
---

## Overview

This Braintree Node.js reference documents removing one evidence item from a dispute with `gateway.dispute.removeEvidence()`. Removal is limited to disputes with status `Open`, requires both dispute and evidence identifiers, and is distinct from submitting or finalizing evidence.

## Key takeaways

- Managing disputes through the API is available only to merchants who can access disputes in the Braintree Control Panel.
- Evidence can be removed only while the dispute has status `Open`.
- The Node example passes a dispute ID and an evidence ID to `gateway.dispute.removeEvidence()`.
- If the evidence is removed from the dispute, the result is successful; otherwise the page directs readers to validation errors. The page does not state that removal submits remaining evidence, finalizes the dispute, or changes its status.

## Detail locators

- Control Panel access restriction: `# Dispute: Remove Evidence > AVAILABILITY`, lines 16-17.
- Removal purpose and `Open`-status restriction: `# Dispute: Remove Evidence`, line 19.
- `gateway.dispute.removeEvidence()` call with dispute and evidence IDs: `# Dispute: Remove Evidence > first ### Node`, lines 20-26.
- Successful-removal result and validation-error guidance: `# Dispute: Remove Evidence`, line 27.
- Promise success/error handling: `# Dispute: Remove Evidence > second ### Node`, lines 28-37.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]

## Related raw API references

- [[raw/braintree/docs/reference/response/dispute/node-2026-09-16|Braintree Node.js Dispute response reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/dispute/remove-evidence/node-2026-09-16|Braintree Node.js dispute-evidence removal reference]] - complete collected page covering access availability, `Open`-status eligibility, dispute and evidence identifiers, removal outcome, and validation-error handling
