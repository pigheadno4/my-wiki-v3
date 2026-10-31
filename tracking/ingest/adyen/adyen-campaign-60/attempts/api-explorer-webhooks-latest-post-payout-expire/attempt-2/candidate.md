---
title: "Adyen PAYOUT_EXPIRE webhook reference"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/PAYOUT_EXPIRE"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/PAYOUT_EXPIRE/2026-09-15.md"
tags: [adyen, webhooks, payouts, deprecated]
---

## Overview

This 2026-09-15-captured Webhooks `latest` reference describes the incoming `POST /PAYOUT_EXPIRE` notification for an expired payout. The webhook is **deprecated** and does not support new integrations. Adyen directs new integrations to Transfer Webhooks and existing Payout API users to their Adyen contact for migration to the Transfers API. The page says Transfers API webhooks have more details and defined transfer states; this legacy event must not be read as a Transfers API state.

## Key takeaways

- The request-body table marks outer `live` and `notificationItems` optional. Inside a `NotificationRequestItem`, it marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required. This is nested-property requiredness as shown in the table, not a claim that the outer body or wrapper is required. `originalReference`, `paymentMethod`, `reason`, and `additionalData` are marked optional.
- The `amount` row calls it a required object but says HTTP POST `currency` and `value` are returned as URL parameters (raw line 34), whereas the example nests both inside a JSON `amount` object (raw lines 54–57). The snapshot does not reconcile those representations; it does not establish one resolved delivery format.
- `merchantReference` is the merchant's payment reference; `pspReference` is Adyen's transaction/request reference. The optional `originalReference` is described for modifications as corresponding to the original payment request. The `amount` row calls it the payment amount; this page does not separately define an expired payout amount or funds-movement state.
- `success` describes whether the `eventCode` event was executed successfully. The example has `eventCode: PAYOUT_EXPIRE` and `success: "true"`: that is an event-scoped outcome for expiry, **not** proof that the payout succeeded or reached a bank. The optional `reason` row says it explains refusal if `success=false`; the example's empty reason does not create another rule.
- Under `200 Success`, the page says webhook events are accepted on the basis of the HTTP status code. This receiver acceptance is separate from the payout state. The page gives no response body, retry, ordering, deduplication or signature rule.
- A standalone “The payout expired” link appears without an accompanying trigger or timeout explanation. Do not infer an expiry interval or a particular payout stage from it.

## Detail locators

- Raw lines 5–21: deprecation and Transfers API migration direction.
- Raw lines 23–43: fragmentary expiry link and body schema, including nested required flags and reference identities.
- Raw lines 45–71: TEST example with `PAYOUT_EXPIRE`, EUR 1000, optional `originalReference`, and event-scoped `success: "true"`.
- Raw lines 72–75: HTTP-status acceptance statement.

## Related

- [[adyen]] — company route.
- [[adyen-payouts]] — legacy payout and Transfers API context.
- [[adyen-webhooks]] — webhook receipt and family distinctions.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/PAYOUT_EXPIRE/2026-09-15|PAYOUT_EXPIRE reference, captured 2026-09-15]]
