---
title: "Adyen Dispute webhooks v4 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/dispute-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/dispute-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, issuing, disputes, webhooks]
---

## Overview

This 2026-09-15-captured API Explorer overview labels the family **Dispute webhooks v4**. Adyen says these webhooks inform the recipient about creation or update of raised disputes and chargebacks resulting from raised disputes. It lists `balancePlatform.dispute.created` and `balancePlatform.dispute.updated` incoming POST event routes. The overview is a catalog, not an event payload schema or evidence of a dispute outcome. The `latest` route does not independently verify a current version. See [[adyen]], [[adyen-issuing]] and [[adyen-webhooks]].

## Key takeaways

- The two listed event types concern a raised dispute's creation or update. The page does not define their triggers beyond those descriptions, required fields, status values, resource IDs, amounts, chargeback stage, or response/acknowledgement schema; follow the separate event references for those details.
- Mention of resulting chargebacks does not say that either listed event means a chargeback was won, lost, booked or reversed. Receipt of a notification is not evidence of a financial outcome.

## Detail locators

- Family label, scope and purpose: pinned raw lines 5–9.
- Listed event routes: `## Endpoints > ### General`, lines 11–17.

## Related

- [[source-adyen-docs-issuing-raise-disputes-manage-disputes]] — separate guide to draft, submitted and closed raised-dispute transitions.

## Related raw API references

- [[raw/adyen/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.created/2026-09-15|Dispute-created event reference]] — navigation only; separate event schema.
- [[raw/adyen/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.updated/2026-09-15|Dispute-updated event reference]] — navigation only; separate event schema.

## Raw Sources

- [[raw/adyen/api-explorer/dispute-webhooks/latest/overview/2026-09-15|Dispute webhooks v4 overview snapshot]]
