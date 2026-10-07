---
title: "Braintree Automating Dispute Management (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/disputes/automating/node"
raw_files:
  - "braintree/docs/guides/disputes/automating/node-2026-09-16.md"
tags: [braintree, disputes, automation, webhooks, node-js]
---

## Overview

This unversioned Braintree Node.js webpage, captured 2026-09-16, presents a webhook-triggered pattern for automating part or all of a merchant dispute-management workflow. API dispute management is available only to merchants who can access disputes in the Braintree Control Panel.

## Key takeaways

- The basic sequence is to inspect an incoming webhook, confirm that it represents a newly opened dispute, take the dispute ID from the payload, retrieve the dispute object, gather and submit evidence under merchant-defined criteria, and finalize the dispute.
- The Node example narrows automation to a `DisputeOpened` notification whose retrieved dispute reason is `ProductNotReceived`. It uploads a transaction-associated shipping-confirmation PDF as an evidence document; only when that upload reports success does the example attach the uploaded document to the dispute and call finalize.
- When the retrieved dispute does not match that reason, the example instead comments that the webhook should be persisted and handled by another workflow. The shipped-goods and shipping-confirmation assumptions are specific to the illustrated ecommerce merchant rather than universal evidence requirements.

Scope and evidence boundary: this captured Node.js-family website example is not an exact SDK package/version or runtime contract, does not identify sandbox versus production, and does not itself establish current account or product availability, webhook delivery guarantees, a dispute-status transition, successful evidence submission or finalization, or a dispute outcome.

## Detail locators

- Control Panel dispute-access condition and automation purpose: opening `AVAILABILITY` block and introduction, lines 17-20.
- Basic webhook-to-finalization sequence: `## Automation with webhooks`, lines 23-32.
- Shipped-product example condition and shipping-confirmation evidence rationale: example introduction, line 34.
- Node.js `DisputeOpened` and `ProductNotReceived` checks, evidence-document upload, success-conditioned attachment and finalization, and alternate persistence branch: `### Node`, lines 37-68.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]
- Notification concept: [[braintree-webhooks]]

## Related raw API references

- Webhook parsing, Dispute Find and Dispute Finalize are linked navigation targets in the captured page; they were not used here as independent behavioral evidence.

## Raw Sources

- [[raw/braintree/docs/guides/disputes/automating/node-2026-09-16|Braintree Automating Dispute Management (Node.js) guide]] - complete captured webpage covering eligibility, the webhook-triggered dispute automation sequence, and a reason-conditioned shipping-confirmation example