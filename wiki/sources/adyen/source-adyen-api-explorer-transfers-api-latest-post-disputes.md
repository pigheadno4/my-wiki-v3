---
title: "Adyen Transfers API POST /disputes — raise an Issuing transaction dispute"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers-api/latest/post/disputes"
raw_files:
  - "adyen/api-explorer/transfers-api/latest/post/disputes/2026-09-15.md"
tags: [adyen, issuing, disputes, transfers-api]
---

## Overview

This 2026-09-15 Transfers API `latest` POST /disputes reference describes raising a dispute for an underlying transaction, with a reason type and disputed amount. It is an Issuing transaction-dispute resource, not the merchant acquiring dispute-defense API. The page describes a returned dispute ID for later detail updates, supporting documents, closure, chargeback submission and status lookup; creation alone is not a submitted chargeback or a won dispute. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The request requires `transactionId` and `type`. The listed types are `duplicate`, `fraud`, `notDelivered` and `other`, but the page explicitly says `other` is in beta testing and directs readers not to create or submit disputes of that type at this time. The reason-specific information objects are table-optional at the top level but required when their corresponding dispute type is used; their nested required and conditional fields are in raw lines 28–52. For `duplicate`, the duplicate transaction must have the same amount as the disputed transaction.
- Optional `disputedAmount` cannot exceed the transaction amount; omitting it disputes the entire transaction amount. If supplied, its currency and integer minor-unit value are required. For `fraud`, optional `fraudInfo.reportOnly` defaults to `false`; setting it `true` reports fraud to Adyen without further action such as a chargeback request or fee reversal. A report-only record must not be read as a chargeback or fee-reversal outcome.
- Optional `status` may be set only to `draft` on creation. `submitted` and `closed` are update states, although the schema also lists `won`, `chargeback` and `secondPresentment` as possible status values. A 200 response documents the dispute representation and marks `id` optional in the response table, while the introductory prose says raising a dispute returns an ID; retain that prose/table qualification rather than assuming every 200 body has an ID.
- The response sections list 401 authentication-required, 403 insufficient-permissions and 422 request-validation errors. The repeated error-body tables make top-level problem fields optional; within an optional `invalidFields` array, `message`, `name` and `value` are required per item. These HTTP responses do not establish later chargeback or card-scheme outcome.

> [!warning] Contradiction
> This 2026-09-15 POST reference calls `other` beta and lists only `duplicate`, `fraud`, `notDelivered`, and `other` types. The 2026-11-07 GET /disputes/{id} reference calls `other` deprecated and also lists `cancelled` and `notAsDescribed`. Both prohibit creating or submitting `other`; the captures do not establish current creation support for every type. [[source-adyen-api-explorer-transfers-api-latest-get-disputes-id]]

## Detail locators

- Purpose, follow-on uses of a dispute ID, and test/live `/btl/api/v4` server bases: raw lines 5–17. Full request schema: raw lines 19–55. The not-delivered branch has conditionally required location, return and lateness fields: raw lines 37–48.
- 200 dispute representation, including optional ARN, ID and repeated reason-specific fields: raw lines 57–98. 401, 403 and 422 error response bodies: raw lines 101–155. The pinned page contains no JSON request/response examples or separate header contract.

## Related

- [[adyen]] — provider context.
- [[adyen-issuing]] — Issuing dispute lifecycle context.
- [[source-adyen-docs-issuing-raise-disputes]] — separate Issuing dispute guide; this endpoint is the creation contract.

## Raw Sources

- [[raw/adyen/api-explorer/transfers-api/latest/post/disputes/2026-09-15|Adyen Transfers API latest POST /disputes, captured 2026-09-15]]
