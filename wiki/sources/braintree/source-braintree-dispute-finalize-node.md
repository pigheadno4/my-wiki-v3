---
title: "Braintree Dispute Finalize (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/dispute/finalize/node"
raw_files:
  - "braintree/docs/reference/request/dispute/finalize/node-2026-09-16.md"
tags: [braintree, node-js, disputes, evidence]
---

## Overview

This Braintree Node.js reference documents finalizing a dispute by ID with `gateway.dispute.finalize()`. Finalization is the required action for submitting the dispute's evidence to the banks, and API dispute management is restricted to merchants who can access disputes in the Braintree Control Panel.

## Key takeaways

- Managing disputes through the API is available only to merchants who can access disputes in the Braintree Control Panel.
- The page limits finalization to disputes with status `Open`. Finalization submits the evidence to the banks and updates the dispute status to `Disputed`.
- The page marks the finalize call as required for evidence to be submitted on the dispute; adding or preparing evidence alone is not established here as submission.
- The Node example calls `gateway.dispute.finalize("a_dispute_id")`. A successful finalization produces a successful result; otherwise the example traverses validation errors.

## Detail locators

- Dispute response-object route and Control Panel access restriction: `# Dispute: Finalize`, lines 13-17.
- `Open` eligibility, evidence submission to the banks, and transition to `Disputed`: `# Dispute: Finalize`, line 19.
- Required finalize call for evidence submission: `# Dispute: Finalize > IMPORTANT`, lines 20-21.
- `gateway.dispute.finalize()` invocation: `# Dispute: Finalize > first ### Node`, lines 24-27.
- Success outcome and validation-error traversal: `# Dispute: Finalize`, lines 28-45.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]

## Related raw API references

- [[raw/braintree/docs/reference/response/dispute/node-2026-09-16|Braintree Node.js Dispute response reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/dispute/finalize/node-2026-09-16|Braintree Node.js dispute-finalize request reference]] - complete collected page covering access availability, `Open` eligibility, required evidence submission, the transition to `Disputed`, and result handling
