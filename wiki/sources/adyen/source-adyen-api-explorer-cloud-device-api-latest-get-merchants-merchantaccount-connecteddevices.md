---
title: "Adyen Cloud Device API: list connected devices for a merchant"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/connectedDevices"
raw_files:
  - "adyen/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/connectedDevices/2026-11-07.md"
tags: [adyen, cloud-device-api, point-of-sale, devices]
---

## Overview

Captured Cloud Device API v1 `GET /merchants/{merchantAccount}/connectedDevices` reference from [[adyen]]. It lists payment terminal IDs or Mobile solution SDK installation IDs belonging to a specified merchant account that have an active cloud connection. An optional `store` query parameter narrows the list to a store under that merchant account. The API credential needs the Cloud Device API role.

## Key takeaways

- `merchantAccount` is the required path identifier; `store` is an optional store ID query filter. The documented 200 response has an optional `uniqueDeviceIds` array. Terminal IDs use a model–serial format; Mobile solutions use SDK installation IDs.
- This read reports active cloud connection in the captured response. It is not a device boarding, payment authorization, or settlement result. The reference also documents 401 Unauthorized and 403 Forbidden responses.

## Detail locators

- Servers (test and regional live v1 endpoints): raw lines 13–28.
- Parameters and 200 response schema: raw lines 30–51. The `uniqueDeviceIds` property is marked optional.
- 401/403 error schemas and examples: raw lines 54–89 and 109–133; 200 example: raw lines 91–107. Example IDs and error details are samples, not guaranteed values.

## Related

- [[adyen-terminal-api]] — Terminal API message interface and Cloud Device transport distinction.

## Raw Sources

- [[raw/adyen/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/connectedDevices/2026-11-07|Cloud Device API connected devices, 2026-11-07]]
