---
title: "Adyen Balance Platform API v2: finish SCA device registration"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/scaDevices/(deviceId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/scaDevices/(deviceId)/2026-11-03.md"
tags: [adyen, balance-platform, sca, devices, api]
---

## Overview

This 2026-11-03 Balance Platform API reference documents `PATCH /scaDevices/{deviceId}` to finish registration of a new Strong Customer Authentication (SCA) device. The listed server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the `latest` documentation route does not establish current live availability or caller eligibility. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The required string path `deviceId` identifies the SCA device being associated with a resource. The request-body table requires `sdkOutput`, a base64-encoded block obtained using Adyen's authentication SDK. The snapshot lists no other body property, query parameter, default, limit, or idempotency rule.
- The `200 Success` description says device registration was completed successfully. The response schema marks the parent `scaDevice` object optional; if present, its `id`, `name`, and `type` fields are required, with `type` one of `ios`, `android`, or `browser`. The sample response shows an iOS device but does not make the optional parent or that type guaranteed for every response.
- Completion of device registration is a device lifecycle result. This page does not say that a particular resource association is active, an SCA challenge has succeeded, or a payment or funds transfer is authorized, booked, settled, or received. It specifies no separate review/approval, propagation timing, deletion/reversal route, or version/conflict behavior. Documented failures are 400 invalid input, 401 authentication required, 403 insufficient permissions, 404 device not found, 422 validation error, and 500 server processing failure; the error tables mark parent problem fields optional while nested `invalidFields` members are required when supplied.

## Detail locators

- Purpose, TEST server, path parameter, required SDK output, and request example: pinned raw lines 5–32.
- `200` result, response field requiredness, types, and response example: pinned raw lines 33–44 and 160–173.
- Error descriptions and payload schemas: pinned raw lines 47–158.

## Related

- [[adyen-platforms]] — balance-platform context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-scadevices]] — separate captured reference for beginning SCA device registration.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/scaDevices/(deviceId)/2026-11-03|Balance Platform PATCH SCA device snapshot]]