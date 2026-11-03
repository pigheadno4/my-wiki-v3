---
title: "Adyen Balance Platform API v2: DELETE /scaDevices/{deviceId}"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/scaDevices/(deviceId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/delete/scaDevices/(deviceId)/2026-11-03.md"
tags: [adyen, balance-platform, issuing, sca, devices, api]
---

## Overview

This 2026-11-03-captured Balance Platform API v2 reference documents `DELETE /scaDevices/{deviceId}` for deleting one Strong Customer Authentication (SCA) device. Its only listed server is the TEST base `https://balanceplatform-api-test.adyen.com/bcl/v2`; the `latest` documentation URL does not establish live availability or a particular caller's eligibility. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The required string path parameter `deviceId` is the unique identifier of the SCA device to delete. The page documents no request body, query parameter, conditional input, default, limit, idempotency key or specific caller role.
- A 204 response says the device was deleted successfully and has no documented response body. This is deletion of the SCA **device** resource identified by `deviceId`; the page does not state that a card payment instrument, account holder or separate SCA association is deleted, nor when any linked state or authentication availability changes.
- The page lists 400 invalid input, 401 authentication required, 403 insufficient permissions, 404 device not found, 422 request validation and 500 server error. Their error schemas make top-level fields optional and mark the `invalidFields` child properties required only within that optional array's objects. A 404 is a documented failure, not a successful repeat deletion.
- This captured endpoint does not specify retry or reversal behavior, propagation timing, asynchronous confirmation, version/conflict handling, device enrollment or association effects. A successful deletion response is not proof of a completed SCA challenge, card authorization, regulatory compliance or financial outcome.

## Detail locators

- Endpoint, TEST server, required `deviceId` path ID and 204 success: pinned raw lines 5–22.
- Error descriptions and schema fields: `## Responses`, lines 25–136, including 404 at lines 82–98. The capture has no response examples.

## Related

- [[adyen-issuing]] — Issuing and SCA device context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-scadevices]] — separate SCA device registration initiation reference.
- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-manage-devices]] — separate device management guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/delete/scaDevices/(deviceId)/2026-11-03|Balance Platform DELETE SCA device snapshot]]