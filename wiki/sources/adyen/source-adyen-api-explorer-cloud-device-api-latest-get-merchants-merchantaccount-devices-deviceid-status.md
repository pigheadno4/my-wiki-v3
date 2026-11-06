---
title: "Adyen Cloud Device API: get a device's cloud connection status"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/devices/(deviceId)/status"
raw_files:
  - "adyen/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/devices/(deviceId)/status/2026-11-07.md"
tags: [adyen, cloud-device-api, point-of-sale, device-status]
---

## Overview

This November 2026 capture of the Cloud Device API v1 reference describes `GET /merchants/{merchantAccount}/devices/{deviceId}/status`: check whether a specified payment terminal or Mobile-solution SDK installation ID has an active cloud connection. This is connection state, not a Terminal API transaction or payment outcome. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- The API credential needs the **Cloud Device API role**. Both path parameters are required: `merchantAccount` identifies the merchant account; `deviceId` is a terminal ID in `[terminal model]-[serial number]` format for a payment terminal, or the SDK installation ID for a Mobile solution. No request body, query parameter, default, or idempotency rule is stated in this reference.
- The listed servers use `/v1`: one TEST endpoint and Live endpoints for Australia, East Asia, Europe, and the United States. The reference does not say that a listed endpoint proves account-specific Live availability.
- A `200` response can report `deviceId` and `status`, but the response table marks both fields optional. The listed status values are `ONLINE` and `OFFLINE`, indicating an active cloud connection or its absence; the `ONLINE` example is illustrative. Neither value establishes payment authorization, capture, settlement, or device readiness for a particular transaction.
- The reference lists `401 Unauthorized` and `403 Forbidden`, each with an optional error-body envelope and conditionally present validation fields. It does not define retry, reversal, asynchronous processing, or a connection-state propagation guarantee.

## Detail locators

- Purpose, required role and TEST/regional Live `/v1` servers: [[raw/adyen/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/devices/(deviceId)/status/2026-11-07#L5|raw lines 5–28]].
- Required path identities and optional `200` response fields/status values: [[raw/adyen/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/devices/(deviceId)/status/2026-11-07#L30|raw lines 30–47]].
- `401`/`403` response schemas and `200`/error examples: [[raw/adyen/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/devices/(deviceId)/status/2026-11-07#L50|raw lines 50–123]].

## Related

- [[adyen-terminal-api]] — Cloud Device transport and Terminal API message boundary.
- [[source-adyen-api-explorer-cloud-device-api-latest-overview]] — API family and transport overview.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/devices/(deviceId)/status/2026-11-07|Captured Cloud Device API v1 GET device status reference]]
