---
title: "Braintree Managing PayPal Disputes via the API (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/disputes/paypal-disputes/node"
raw_files:
  - "braintree/docs/guides/disputes/paypal-disputes/node-2026-09-16.md"
tags: [braintree, paypal, disputes, node-js, evidence]
---

## Overview

This unversioned Braintree Node.js webpage, captured 2026-09-16, explains the PayPal-specific evidence requirements for managing a PayPal dispute after it is reflected in the Braintree gateway. It applies only to merchants who can access disputes in the Braintree Control Panel and uses Braintree dispute operations rather than documenting the direct PayPal Disputes API.

## Key takeaways

- Once a PayPal dispute is reflected in the Braintree gateway, the page says merchants can use the same Braintree API calls used for credit-card disputes to find or search for it, check its status and respond. The differentiating requirement is the evidence: the response must declare an evidence type and use categorized evidence through the Add Text Evidence call.
- Set the evidence category to `EVIDENCE_TYPE` and its content to `PROOF_OF_FULFILLMENT`, `PROOF_OF_REFUND` or `OTHER`. Additional text evidence uses the applicable category; file evidence is first uploaded to Braintree and then attached to the dispute. The full category inventory and Node examples remain in the raw locators below.
- Evidence can be added repeatedly, but the dispute must be finalized before the reply-by date in its details. Only after finalization does the page say the response and evidence are sent for review; Braintree warns that an unfinalized response will not be forwarded to the deciding party after the deadline. This snapshot does not prove current merchant access, successful forwarding, review outcome or a dispute win.
- `PROOF_OF_FULFILLMENT` applies when a shipped product was reported as fraud or not received and additionally requires `CARRIER_NAME` plus `TRACKING_NUMBER` and/or `TRACKING_URL`. Multiple tracking sets need integer `sequence_number` values so related information can be grouped.
- `PROOF_OF_REFUND` applies when the transaction has already been refunded and additionally requires a Braintree or PayPal `REFUND_ID`; multiple refunds are added in separate Add Text Evidence requests. The page directs merchants to use `OTHER` only when they lack the required evidence for the other types; its additional categories are optional, and the page's comparative win-language is guidance rather than an outcome guarantee.

## Detail locators

- Control Panel dispute-access prerequisite: `# Managing PayPal Disputes via the API > AVAILABILITY`, lines 17-18.
- Braintree-gateway scope, shared dispute operations and PayPal-specific categorized-evidence requirement: opening paragraphs, lines 20-25.
- Evidence-type declaration, text/file evidence sequence, repetition, finalization deadline and forwarding warning: `## Responding with evidence`, lines 26-45.
- Three evidence types and the qualification that some types require additional evidence: `### Specifying an evidence type`, lines 48-58.
- Fulfillment conditions, required carrier/tracking categories and grouping with integer `sequence_number`: `#### Proof of fulfillment evidence type`, lines 59-67.
- Node.js fulfillment example with two tracking groups: first `### Node`, lines 68-113.
- Refund condition, required refund identifier, multiple-refund handling and Node.js example: `#### Proof of refund evidence type`, lines 115-138.
- `OTHER` condition, optional additional categories, qualified comparative guidance and Node.js example: `#### Other evidence type`, lines 140-157.
- Complete category/content values and `sequence_number` purpose: `### Argument reference`, lines 159-171.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]

## Related raw API references

- Dispute Add Text Evidence, Document Upload Create, Dispute Add File Evidence and Dispute Finalize are linked navigation targets in the captured guide; those targets are not evidence for this entry.

## Raw Sources

- [[raw/braintree/docs/guides/disputes/paypal-disputes/node-2026-09-16|Braintree Managing PayPal Disputes via the API (Node.js) guide]] - complete captured webpage covering eligibility, categorized PayPal evidence, Node examples, file-evidence navigation and deadline-bound finalization
