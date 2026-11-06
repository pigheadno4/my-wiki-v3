---
title: "Adyen Cloud device API synchronous Terminal API request"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/sync"
raw_files:
  - "adyen/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/sync/2026-11-07.md"
tags: [adyen, cloud-device-api, terminal-api, point-of-sale, api-explorer]
---

## Overview

This 2026-11-07 capture of the Cloud device API v1 `POST /merchants/{merchantAccount}/devices/{deviceId}/sync` reference describes sending a JSON Terminal API request to a payment device and receiving a Terminal API response synchronously. The Cloud Device API transports the message; the response's transaction meaning depends on the Terminal API response itself. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- The API credential needs the **Cloud Device API role**. The captured servers comprise a test v1 endpoint and regional live v1 endpoints for Australia, East Asia, Europe and the United States.
- Both path parameters are required: `merchantAccount` identifies the merchant account, and `deviceId` identifies the payment device. The device ID must equal `MessageHeader.POIID` in the Terminal API request. For payment terminals, the reference calls for a model–serial terminal ID; for a Mobile solution, it calls for the SDK installation ID.
- The body is a JSON object containing a Terminal API request. This page delegates its structure to the Terminal API request types and says the response returns a Terminal API response; it does not enumerate request properties or response fields here.
- The documented `200 Success` says the request succeeded. This transport-level description alone does not establish payment authorization, capture, settlement, or device eligibility; inspect the applicable Terminal API response for operation-specific results.

## Detail locators

- Purpose, body and response routing: [[raw/adyen/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/sync/2026-11-07#L5|raw lines 5–11]].
- Required credential role and test/live regional v1 servers: [[raw/adyen/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/sync/2026-11-07#L13|raw lines 13–32]].
- Required path identifiers and `POIID` match: [[raw/adyen/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/sync/2026-11-07#L34|raw lines 34–40]].
- HTTP response: [[raw/adyen/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/sync/2026-11-07#L42|raw lines 42–45]].

## Related

- [[adyen-terminal-api]] — Terminal API message semantics and Cloud Device transport boundary.
- [[source-adyen-api-explorer-cloud-device-api-latest-overview]] — separate Cloud device API v1 overview.

## Raw Sources

- [[raw/adyen/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/sync/2026-11-07|Adyen synchronous Cloud Device API reference capture, 2026-11-07]]
