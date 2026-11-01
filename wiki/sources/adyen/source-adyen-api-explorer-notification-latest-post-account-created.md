---
title: "Adyen Classic Notification: ACCOUNT_CREATED"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Notification/latest/post/ACCOUNT_CREATED"
raw_files:
  - "adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15.md"
tags: [adyen, classic-platforms, notification, accounts, webhooks]
---

## Overview

This 2026-09-15-captured API Explorer `Notification/latest` reference describes an incoming `ACCOUNT_CREATED` webhook that Adyen sends when a Classic account is created. It is a notification sent to the recipient, not the `POST /createAccount` call. The pinned operation page does not state a numeric Notification API version. Its `accountCode` and `accountHolderCode` belong to the Classic account model, separate from balance-platform account-holder and balance-account IDs. [[adyen-classic-platforms]] [[adyen]]

## Key takeaways

- In the request-body table, `eventDate`, `eventType`, `executingUserKey`, `live`, and the outer `pspReference` are marked required. `live` identifies test versus live origin. The optional `content` object can carry the new `accountCode`, `accountHolderCode`, a request `pspReference`, `resultCode`, and account `status` (permitted value `Active`). Keep the outer notification request reference distinct from the optional content reference; the page's example gives both the same illustrative value. See [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15|raw lines 11–39]] and [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15|example lines 43–80]].
- Optional `content` also lists `invalidFields` for fields that caused `/createAccount` to fail and an outer `error` object for failed request processing. The example combines `error`, `invalidFields`, `resultCode: "Success"`, and `status: "Active"`; it cannot establish a general rule that every `ACCOUNT_CREATED` payload denotes successful creation or that those fields always occur together. See [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15|raw lines 19–32 and 43–80]].
- The account payload's optional `bankAccountUUID` and `payoutMethodCode` describe payout coupling; `payoutSchedule.schedule` lists `HOLD`, which prevents scheduled payouts while still allowing manually initiated payouts. These are account details in this notification schema, not evidence that any payout was executed. See [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15|raw lines 17–28]].
- The HTTP 200 response section says to set optional `notificationResponse` to **[accepted]** to acknowledge receipt from Adyen. This acknowledgement is distinct from account creation, verification, payout eligibility, or money movement. The separate Classic creation guide says to wait for `ACCOUNT_CREATED` before business logic even if `/createAccount` returned HTTP 200; that guide supplies the creation-flow completion gate, while this event reference defines the event payload and receiver response. See [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15|raw lines 83–91]] and [[source-adyen-docs-classic-platforms-account-holders-and-accounts|Classic creation guide]].

## Detail locators

- Full event property table, including required markers, optional payout schedule and errors: [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15|raw lines 9–39]].
- Illustrative request body with conflicting success and error fields: [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15|raw lines 41–82]].
- HTTP response and acknowledgement field: [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15|raw lines 83–91]].

## Related

- [[adyen-classic-platforms]] — Classic holder/account identity and creation-flow context.
- [[source-adyen-api-explorer-account-latest-post-createaccount]] — Outbound account-creation request reference.
- [[source-adyen-docs-classic-platforms-account-holders-and-accounts]] — Separately sourced asynchronous creation gate.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15|ACCOUNT_CREATED API Explorer reference (captured 2026-09-15)]]
