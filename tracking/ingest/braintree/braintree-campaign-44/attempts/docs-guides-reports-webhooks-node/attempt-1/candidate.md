---
title: "Braintree Webhook Reports (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/reports/webhooks/node"
raw_files:
  - "braintree/docs/guides/reports/webhooks/node-2026-09-16.md"
tags: [braintree, reporting, webhooks, disbursements, nodejs]
---

## Overview

This 2026-09-16 capture is the unversioned Braintree Node.js website guide to building merchant-owned reports from webhook notifications. After webhook receipt is configured, the guide has the merchant collect and store selected notification details by trigger; the feature is available only when Braintree manages funding for the merchant account. See [[braintree]] and [[braintree-webhooks]].

## Key takeaways

- The general workflow is to configure at least one destination URL, parse incoming notifications, and store details from `WebhookNotification` objects for the selected trigger. The page offers subscription-cancellation, dispute-versus-sales chargeback-ratio, and disbursement funding reports as examples, not guaranteed report outputs.
- A disbursement or disbursement-exception webhook includes a disbursement object. Unlike transaction or subscription objects, the guide says that object has no alternative gateway retrieval route.
- To find transactions associated with a disbursement, the Node.js examples parse the incoming `bt_signature` and `bt_payload`, read transaction IDs from the disbursement payload, and pass those IDs to a gateway transaction search. Callback and Promise forms remain in the pinned raw.
- The page links separately to sandbox disbursement-exception triggering; that navigation does not broaden this guide into production execution evidence.
- **Scope boundary:** this captured website guide documents a merchant-built reporting pattern, not current account eligibility or evidence that a webhook was delivered or a report completed.

## Detail locators

- Feature availability and webhook-report purpose: `# Webhooks`, lines 14-20.
- Illustrative report triggers and the destination/parse/store workflow: `# Webhooks` and `## General workflow`, lines 20-33.
- Disbursement-object retrieval constraint and sandbox exception route: `## Disbursements`, lines 36-42.
- Incoming POST parameters, associated-transaction procedure, and callback/Promise examples: `## Transactions associated with a disbursement`, lines 45-81.
- Reference navigation: `## See also`, lines 84-88.

## Related

- [[braintree]]
- [[braintree-webhooks]]
- [[source-braintree-docs-guides-reports-custom-node]]
- [[source-braintree-webhooks-disbursement-node]]
- [[source-braintree-webhooks-parse-node]]
- [[source-braintree-transaction-search-node]]

## Related raw API references

- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Webhook receipt overview]]
- [[raw/braintree/docs/reference/general/webhooks/overview-2026-09-16|Webhook triggers reference]]
- [[raw/braintree/docs/guides/webhooks/create/node-2026-09-16|Create webhooks (Node.js)]]
- [[raw/braintree/docs/guides/webhooks/parse/node-2026-09-16|Parse webhooks (Node.js)]]
- [[raw/braintree/docs/guides/braintree-marketplace/testing-go-live/node-2026-09-16|Braintree Marketplace testing and go-live (Node.js)]]
- [[raw/braintree/docs/reference/request/transaction/search/node-2026-09-16|Transaction search (Node.js)]]
- [[raw/braintree/docs/reference/general/searching/search-results/node-2026-09-16|Search results]]
- [[raw/braintree/docs/reference/general/webhooks/disbursement/node-2026-09-16|Disbursement webhook details (Node.js)]]

## Raw Sources

- [[raw/braintree/docs/guides/reports/webhooks/node-2026-09-16|Braintree Webhook Reports (Node.js), captured 2026-09-16]]
