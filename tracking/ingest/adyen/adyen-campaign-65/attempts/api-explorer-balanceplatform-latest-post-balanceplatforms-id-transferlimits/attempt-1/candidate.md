---
title: "Adyen Balance Platform API v2: Create a platform transfer limit"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balancePlatforms/(id)/transferLimits"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/balancePlatforms/(id)/transferLimits/2026-11-03.md"
tags: [adyen, balance-platform, business-accounts, transfer-limits, sca, api-reference]
---

## Overview

The 2026-11-03-captured Balance Platform API v2 TEST reference describes `POST /balancePlatforms/{id}/transferLimits` to create a transfer limit for the balance platform identified by the required path `id`. The platform ID is distinct from the returned transfer-limit `id`. This is a configuration-resource creation route; a `200` response does not by itself mean that the limit is active, that SCA is complete, or that any transfer was executed. See [[adyen]] and [[adyen-business-accounts]].

## Key takeaways

- The required body fields are `amount` (required `currency` and integer `value` in minor units), `scope` (`perTransaction` or `perDay`) and `transferType` (`instant` or `all`). The amount is the maximum per transfer or per day according to scope. Optional `reference`, `startsAt`, `endsAt` and `scaInformation` have separate roles; a future `startsAt` schedules the limit, and the page says that without `endsAt` it stays active until overridden by a new limit.
- Optional `scaInformation.exemption` lists `lowerLimit`, `notRegulated`, `setByPlatform`, `initialLimit` and `alreadyPerformed`. Optional `scaOnApproval=true` allows initiating SCA later during approval for all pending transfer limits; `false` is the stated default and means initiating SCA immediately after submitting the request. These request choices are not proof of an exemption, authentication or approval outcome.
- `200` returns required `amount`, transfer-limit `id`, `limitStatus`, `scope`, `startsAt` and `transferType`; `endsAt`, `reference` and `scaInformation` are optional. When `scaInformation` is returned, its nested `status` is marked required with `notPerformed`, `pending` and `performed` values. `limitStatus` can be `active`, `inactive`, `pendingSCA` or `scheduled`. The example returns `pendingSCA` with SCA `pending`, illustrating that successful creation need not mean active enforcement.
- The request example gives `endsAt` as `2026-08-14T00:00:00+01:00`, while the `200` response example gives `2026-08-13T23:00:00+01:00`. Both print `+01:00`; the snapshot does not explain the difference, so do not infer a timestamp-conversion or duration rule from the example.
- The captured server is TEST `/bcl/v2`. This endpoint lists `404` (one of the transfer limits could not be found) and `422` (request validation error), but no operation-specific authentication, idempotency, conflict, approval-completion or propagation guarantee. The dated schema and examples do not establish live availability, account eligibility, legal/SCA compliance, transfer authorization, booking, settlement or bank receipt.

## Detail locators

- Raw lines 5–33: operation, TEST server, required path and body schema, optional scheduling and SCA controls.
- Raw lines 35–53: request example, including its `endsAt` timestamp.
- Raw lines 54–74: `200` response fields, requiredness and status meanings.
- Raw lines 77–112: `404` and `422` problem-response schemas.
- Raw lines 114–135: `200` example with `pendingSCA` and differing `endsAt`.

## Related

- [[adyen-business-accounts]] — Business Accounts transfer-limit concept and linked setup guide; this API reference controls its own POST contract.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/balancePlatforms/(id)/transferLimits/2026-11-03|Create platform transfer limit API reference (2026-11-03)]]