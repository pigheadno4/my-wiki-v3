---
title: "Adyen Balance Platform API v2: POST recurring top-up configuration"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/recurringTopUps"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/recurringTopUps/2026-11-02.md"
tags: [adyen, balance-platform, issuing, recurring-top-ups, api]
---

## Overview

This 2026-11-02-captured Balance Platform API v2 reference describes `POST /balanceAccounts/{balanceAccountId}/recurringTopUps`, creation of a recurring top-up **configuration** for the balance account identified by the required path ID. The only displayed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. The 200 response and reported configuration ID indicate request success, but creation is asynchronous: the linked Issuing top-up-webhooks guide says this response does not necessarily confirm successful creation, and identifies the `balancePlatform.balanceAccount.recurringTopUp.created` Configuration webhook as the successful-creation signal (guide raw lines 19 and 35–41). A confirmed configuration is still distinct from a triggered direct-debit transfer, booked balance credit or payment. [[source-adyen-docs-issuing-add-manage-funds-top-ups-top-up-webhooks]] The `latest` path does not prove live availability or account eligibility. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The request table marks `counterparty` (with required `transferInstrumentId`), `description`, `topUpAmount` and `trigger` required. `description` is capped at 140 characters and longer input is cut off. `referenceForBeneficiary` is optional, restricted to letters/digits, and is sent in transfer-related webhooks. The page does not separately state whole-body requiredness.
- `topUpAmount.fixed` and `topUpAmount.target` are individually optional in this API table; when either object is supplied, its currency and minor-unit integer value are required. The linked Issuing guide says to select one of fixed or target. `trigger.threshold` is marked required within `trigger`, with required currency and minor-unit value; `trigger.schedule` is optional, but its `type` is required when the schedule object is supplied. Listed schedule types are weekdays, weekly and monthly at 07:00 in the balance account's local time zone, and null/default continuous monitoring.
- Omitted `status` defaults to `active`; `inactive` disables triggering. The 200 response returns a required configuration `id` plus the configuration fields, with `status` itself marked optional in the response table. The 200 request success and reported ID do not alone confirm asynchronous configuration creation. The created Configuration webhook is the documented success signal; even then, an active configuration does not establish that a threshold was met or funds were pulled and credited. [[source-adyen-docs-issuing-add-manage-funds-top-ups-top-up-webhooks]]
- The page lists 400, 401, 403 and 422 errors. Its 422 examples illustrate currency mismatch, disabled direct-debit top-up property, inactive holder, invalid transfer instrument, missing `receiveFromTransferInstrument` capability and unavailable route; these are examples, not a complete eligibility matrix. The reference itself does not specify a credential role, idempotency behavior or final transfer outcome.

> [!warning] Contradiction
> This API reference says a top-up is initiated when balance falls **below** `trigger.threshold` (pinned raw line 40). The linked Issuing guide's Customer Area instructions say **less than or equal to** the threshold (guide raw line 242); its API prose says below (guide raw line 99). The captured sources do not settle equality behavior. [[source-adyen-docs-issuing-add-manage-funds-top-ups-create-recurring-top-ups]]

## Detail locators

- Endpoint, TEST base, required path and request-body fields/defaults: pinned raw lines 5–42.
- Illustrative request: `## Request examples`, lines 44–69. Response schema and example: lines 70–96 and 174–203.
- Error schemas: lines 99–172. Generic and top-up-specific examples: lines 205–317.

## Related

- [[adyen-issuing]] — recurring top-up context.
- [[source-adyen-docs-issuing-add-manage-funds-top-ups-create-recurring-top-ups]] — separate requirements and lifecycle guide with threshold wording conflict.
- [[source-adyen-docs-issuing-add-manage-funds-top-ups-top-up-webhooks]] — asynchronous creation confirmation, then separate transfer and booked-credit events.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/recurringTopUps/2026-11-02|Recurring top-up POST snapshot]]