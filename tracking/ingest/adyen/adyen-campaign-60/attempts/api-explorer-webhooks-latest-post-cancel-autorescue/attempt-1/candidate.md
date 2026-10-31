---
title: "Adyen Webhooks: CANCEL_AUTORESCUE"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/CANCEL_AUTORESCUE"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/CANCEL_AUTORESCUE/2026-09-15.md"
tags: [adyen, webhooks, online-payments, auto-rescue, cancellation]
---

## Overview

This 2026-09-15 snapshot of Adyen's API Explorer `Webhooks/latest` reference describes the incoming `CANCEL_AUTORESCUE` notification: the Auto Rescue process was canceled. It documents the event notification, not the merchant's cancellation request. The example shows `success: "false"` with a reason that no Auto Rescue process was found for a rescue reference; that example does not establish every possible cancellation outcome.

## Key takeaways

- The displayed request-body table marks top-level `live`, `notificationItems`, and the nested `NotificationRequestItem` wrapper optional. Within a notification item, `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` are marked required. See **Parameters → Request body**, raw lines 11–27. Do not turn the example's `additionalData.hmacSignature` into a required field.
- `success` describes whether the `eventCode` event executed successfully. If `success` is `false`, `reason` includes a short refusal explanation. The example is specifically a `CANCEL_AUTORESCUE` event with `success: "false"`; receipt of the event alone is not proof that cancellation succeeded. See raw lines 26–27 and 31–57.
- `merchantReference` identifies the merchant's payment, `pspReference` identifies Adyen's transaction or request, and optional `originalReference` corresponds to the original payment request for modifications. `eventDate` is the event-generation timestamp; `live` identifies live versus test origin. See raw lines 14 and 20–25.
- The reference lists a `200 Success` response and states that webhook events are accepted on the basis of HTTP status code. This is receiver acceptance, separate from the cancellation outcome. The page does not specify delivery order, retry, deduplication, signature-verification, or payment finality rules. See **Responses**, raw lines 58–61.

## Detail locators

- **Parameters → Request body, raw lines 11–27** — displayed field types and required markers, identifiers, event outcome, and conditional reason.
- **Request examples → cancel_autorescue, raw lines 29–57** — test-origin example with EUR amount, `CANCEL_AUTORESCUE` event code, original and PSP references, a no-process reason, and `success: "false"`.
- **Responses, raw lines 58–61** — `200 Success` and HTTP status based webhook acceptance.

## Related

- [[adyen]]
- [[adyen-webhooks]]
- [[adyen-online-payments]]
- [[adyen-card-auto-rescue]]
- [[source-adyen-docs-online-payments-auto-rescue-sepa]]

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/CANCEL_AUTORESCUE/2026-09-15|Adyen API Explorer — CANCEL_AUTORESCUE (2026-09-15)]]
