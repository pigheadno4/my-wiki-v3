---
title: "Adyen Classic Notification: ACCOUNT_UPDATED"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Notification/latest/post/ACCOUNT_UPDATED"
raw_files:
  - "adyen/api-explorer/Notification/latest/post/ACCOUNT_UPDATED/2026-09-15.md"
tags: [adyen, classic-platforms, notifications, account-updates]
---

## Overview

This 2026-09-15-captured API Explorer `Notification/latest` reference describes the incoming `POST /ACCOUNT_UPDATED` webhook Adyen sends when a Classic account is updated. Its `content.accountCode` identifies the account; this is distinct from a modern Balance Platform balance-account or account-holder event. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The request table marks the outer `content` object optional and its nested `accountCode` required. It separately marks `eventDate`, `eventType`, `executingUserKey`, `live` and outer `pspReference` required. `live` distinguishes live from test origin. The optional `content.pspReference` is described as a request reference; preserve it separately from the required outer PSP reference.
- Optional `content` fields describe the updated account and payout routing: `bankAccountUUID` couples a holder-held bank account for scheduled payouts in its currency, with other currencies sent to a matching holder bank account; `payoutMethodCode` couples a holder-held method for scheduled card payouts. `payoutSchedule.schedule=HOLD` prevents scheduled payouts while manual payouts remain possible. The same table lists `payoutSpeed` values `STANDARD` and `SAME_DAY`, but gives no same-day timing or eligibility rule.
- The table describes optional `content.invalidFields` as fields that caused `/updateAccount` to fail, and optional top-level `error` as information for a failed request. The one illustrative JSON object includes `error` and `invalidFields` alongside `content.resultCode="Success"`; it does not define how to reconcile those indicators for an actual event.
- The 200 response documents optional `notificationResponse`, set to `accepted` to acknowledge receipt. That receiver response is distinct from the account update result and from any scheduled payout or bank receipt. This page gives no delivery-order, retry, deduplication or signature contract.

## Detail locators

- Event trigger and Classic account identity: pinned raw lines 5–7; envelope and nested requiredness: `## Parameters > ### Request body`, lines 12–37.
- Payout destination, schedule, speed, request reference and failure fields: raw lines 16–32. The `HOLD` enum and manual-payout qualification appear at line 26.
- Mixed-indicator sample: `## Request examples > ### accountUpdated`, lines 41–78. It is an example, not a guaranteed success/failure combination.
- HTTP 200 acknowledgement body: `## Responses > ### 200 Success`, lines 79–87.

## Related

- [[adyen-classic-platforms]] — Classic account and notification context.
- [[source-adyen-api-explorer-account-latest-post-updateaccount]] — separate Account API update request and response.
- [[source-adyen-docs-classic-platforms-payouts-scheduled-payout]] — separate Classic guide on waiting for `ACCOUNT_UPDATED` when confirming an account schedule update.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_UPDATED/2026-09-15|ACCOUNT_UPDATED notification reference captured 2026-09-15]]
