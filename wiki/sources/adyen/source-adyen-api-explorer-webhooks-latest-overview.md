---
title: "Adyen Webhooks v1 API Explorer overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/overview/2026-09-15.md"
tags: [adyen, webhooks, api-explorer, event-catalog]
---

## Overview

The 2026-09-15 snapshot of Adyen's **Webhooks v1** API Explorer overview says Adyen uses webhooks for payment-status updates, newly available reports, and other subscribed events. Its General table is a catalog of `POST` event routes and one-line purposes, including authorisation, capture, refunds, disputes, payouts, orders, recurring contracts and reports. This page does not define an individual event payload or receiver response contract.

## Key takeaways

- The table labels `/AUTHORISATION` as the result of an authorisation request, `/CAPTURE` as the result of a capture request, and `/REFUND` as the result of a refund request. These are incoming webhook reference routes in this catalog, not merchant API operations to execute. See the exact event references for their fields and outcome qualifications.
- Failure and reversal have separate labels: `/CAPTURE_FAILED` is a capture request failed due to scheme rejection; `/REFUND_FAILED` and `/REFUND_NOT_CLEARED` are distinct refund failures; `/SETTLED_REVERSED`, `/REFUNDED_REVERSED`, and `/PAIDOUT_REVERSED` are listed separately. Do not treat these labels as equivalent to the other result routes, or infer success from a route name alone.
- The overview supplies no field requiredness, event-code envelope, resource/reference identifier schema, request body, response body, acknowledgement status, timing, delivery order, retry, deduplication or signature rule. The `latest` URL is the captured v1 snapshot label, not a promise about later versions or current behavior. Receipt of a listed event alone does not establish capture, settlement, payout bank receipt or another financial finality beyond the particular event's documented meaning.

## Detail locators

- Raw lines 5–7: v1 heading and subscription/purpose statement.
- Raw lines 9–24: General table, authorisation through chargeback reversal.
- Raw lines 25–48: debit, dispute, fraud, order, payout and pre-arbitration labels.
- Raw lines 49–63: recurring, refund, report, scheme arbitration, settlement reversal and technical cancellation labels.

## Related

- [[adyen]] — company route.
- [[adyen-webhooks]] — webhook concepts and family distinctions.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/overview/2026-09-15|Webhooks v1 API Explorer overview, captured 2026-09-15]]
