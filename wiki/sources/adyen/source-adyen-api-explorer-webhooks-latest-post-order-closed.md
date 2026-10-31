---
title: "Adyen Webhooks: ORDER_CLOSED"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/ORDER_CLOSED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/ORDER_CLOSED/2026-09-15.md"
tags: [adyen, webhooks, online-payments, partial-payments, orders]
---

## Overview

This 2026-09-15 API Explorer `Webhooks/latest` reference headlines the incoming `ORDER_CLOSED` notification as the result of the last partial payment for an order. That heading does not exhaust the event's triggers: the separately collected [[source-adyen-docs-online-payments-partial-payments]] guide also describes `ORDER_CLOSED` with `success: false` when an incomplete order is canceled at expiry or manually. The guide supplies that lifecycle rule; this API Explorer page supplies the event schema. The POST heading is the webhook event route, not a merchant order-closing operation. The page's example has outer `success: "false"` even though `additionalData.order-1-success` is `"true"`; those values concern different levels of the example and must not be collapsed into a single payment or order success claim.

## Key takeaways

- The displayed request-body table marks `live`, `notificationItems`, and its `NotificationRequestItem` wrapper optional. Within an item, `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` are marked required. Optional `additionalData` is a generic container. See **Parameters → Request body**, raw lines 11–27.
- `eventCode` is the event type, shown as `ORDER_CLOSED` in the example. `success` describes whether that event was executed successfully; if it is `false`, the `reason` description says it includes a short refusal explanation. The example instead has an empty `reason` with outer `success: "false"`, so its empty value should not be treated as an explanation or a general rule. See raw lines 19, 26–27, and 48–54.
- `merchantReference` is the merchant's payment reference, `pspReference` is Adyen's transaction or request reference, and optional `originalReference` corresponds to an original payment request for modifications. `eventDate` is event-generation time; `live` identifies live or test origin. The `order-1-pspReference`, `order-1-paymentAmount`, `order-1-success`, and `order-1-paymentMethod` keys appear in the example `additionalData`; the table does not define them as required fields. See raw lines 14, 20–25, and 38–43.
- The reference lists `200 Success` and says webhook events are accepted on the basis of HTTP status code. Receiver acceptance is distinct from the outer event outcome, the example's partial-payment detail, and financial finality. This page gives no delivery-order, retry, deduplication, or signature-verification rules. See **Responses**, raw lines 60–63.

## Detail locators

- **Parameters → Request body, raw lines 11–27** — required markers, event/merchant/payment identifiers, timestamps, and conditional reason description.
- **Request examples → order_closed, raw lines 29–59** — test-origin example, EUR amount, per-payment `additionalData`, `ORDER_CLOSED` event code, outer `success: "false"`, and empty `reason`.
- **Responses, raw lines 60–63** — `200 Success` and HTTP status based webhook acceptance.

## Related

- [[adyen]]
- [[adyen-webhooks]]
- [[adyen-online-payments]]
- [[source-adyen-docs-online-payments-partial-payments]] — separately collected guide for completion and cancellation paths; see its **Key takeaways** and raw lines 719–745 and 1012 for `ORDER_CLOSED` outcomes.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/ORDER_CLOSED/2026-09-15|Adyen API Explorer — ORDER_CLOSED (2026-09-15)]]
