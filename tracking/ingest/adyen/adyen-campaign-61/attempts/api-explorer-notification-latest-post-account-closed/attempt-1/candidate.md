---
title: "Adyen Notification API: ACCOUNT_CLOSED webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Notification/latest/post/ACCOUNT_CLOSED"
raw_files:
  - "adyen/api-explorer/Notification/latest/post/ACCOUNT_CLOSED/2026-09-15.md"
tags: [adyen, classic-platforms, notification-api, webhooks, account-closure]
---

## Overview

This 2026-09-15 API Explorer snapshot describes Adyen's incoming `POST /ACCOUNT_CLOSED` notification when a Classic Platforms account is closed. It is an event reference, not the account-closing API operation. The linked `POST /closeAccount` operation is documented separately. [[adyen]] [[adyen-classic-platforms]] [[adyen-webhooks]]

## Key takeaways

- The notification body requires `eventDate`, `eventType`, `executingUserKey`, `live`, and a top-level `pspReference`. The latter identifies the request from which the notification originates; `live` distinguishes live from test origin (raw lines 26–30).
- `content` and its `accountCode`, `pspReference`, `resultCode`, and `status` fields are marked optional. `accountCode` is the code of the closed account; `status` is described as the new account status, with `Active`, `Inactive`, `Suspended`, and `Closed` permitted (raw lines 14–22). Do not treat optional `content` or `status` as guaranteed in every delivery.
- An optional `error` object carries failed-request information and has no value if processing produced no error. Optional `content.invalidFields` carries validation errors that would prevent requests from being processed (raw lines 16–19, 23–25). The single request example includes an `error` object and `content.resultCode: "Success"` together; it does not define a general outcome rule (raw lines 34–62).
- The response section lists HTTP 200 as a succeeded request and optional `notificationResponse`, which should be set to literal `[accepted]` to acknowledge receipt (raw lines 64–72). This receipt response is separate from account-close processing and account state. This page specifies no delivery timing, ordering, retry, deduplication, or signature rule.

## Detail locators

- Event purpose and linked closing operation: raw lines 5–7.
- Full request body field table: raw lines 9–30; example: raw lines 32–63.
- Receiver response and acknowledgment: raw lines 64–72.

## Related

- [[adyen-classic-platforms]] — Classic account model and reciprocal source route.
- [[source-adyen-api-explorer-account-latest-post-closeaccount]] — separate `POST /closeAccount` operation and its closure effects.
- [[source-adyen-docs-classic-platforms-configure-notifications]] — separate Classic notification setup and delivery guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CLOSED/2026-09-15|Notification API Explorer ACCOUNT_CLOSED capture]]
