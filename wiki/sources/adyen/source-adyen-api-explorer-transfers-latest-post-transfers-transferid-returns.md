---
title: "Adyen Transfers API v4 return a transfer"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/(transferId)/returns"
raw_files:
  - "adyen/api-explorer/transfers/latest/post/transfers/(transferId)/returns/2026-11-07.md"
tags: [adyen, transfers-api, transfer-returns, balance-platform]
---

## Overview

This 2026-11-07-captured Transfers API `latest` reference documents `POST /transfers/{transferId}/returns` on the v4 Test server. It initiates a return of previously transferred funds without creating a new `transferId`; the path identifies the original transfer. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The request requires an `amount` object with three-character ISO `currency` and integer `value` in minor units. The page states no minimum, maximum, or relationship between the requested amount and the original transfer; this absence does not establish that partial returns are allowed.
- Optional `reference` is the caller's internal reference for the return; Adyen generates a unique reference if omitted and uses it in instruction-status communication. The reference recommends unique values per instruction. Optional `Idempotency-Key` is a unique message identifier with a maximum of 64 characters; the page does not define retry or deduplication behavior.
- The `200` response schema marks `id` (return identifier), `reference`, `status` (`Authorised` or `Declined`), and `transferId` (original transfer identifier) optional. The `Authorised` example is illustrative. A successful HTTP response or `Authorised` value is not evidence of booked funds, completed return, beneficiary receipt, or bank settlement.
- The reference lists `401` authentication, `403` permission, `422` validation, and `500` server-processing errors. It does not state a required caller role, eligibility/capability gate, lifecycle timing, reversal route, asynchronous event contract, or version-conflict behavior. This Test snapshot does not establish current Live availability or a completed financial outcome.

## Detail locators

- Return purpose, v4 Test server and original-transfer path ID: raw lines 5–17.
- Optional idempotency header, request fields, reference generation and example: raw lines 20–45.
- `200` response fields and example: raw lines 46–57, 159–171.
- Error status meanings and schemas: raw lines 60–157.

## Related

- [[adyen-platforms]] — platform transfer and payout source route.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/post/transfers/(transferId)/returns/2026-11-07|Transfers API return POST, captured 2026-11-07]]
