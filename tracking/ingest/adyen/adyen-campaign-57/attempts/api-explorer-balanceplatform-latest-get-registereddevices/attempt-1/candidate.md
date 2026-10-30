---
title: "Adyen Balance Platform API v2: list registered SCA devices"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/registeredDevices"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/registeredDevices/2026-09-15.md"
tags: [adyen, balance-platform, issuing, sca, api]
---

## Overview

This captured API Explorer reference documents `GET /registeredDevices` on the Balance Platform API v2 test server. It retrieves a paginated list of currently registered SCA devices associated with a specified payment instrument; the payment instrument and SCA device are distinct objects. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- `paymentInstrumentId` is a required query parameter and limits the list to devices associated with that payment instrument. Optional `pageNumber` defaults to zero, and `pageSize` defaults to 20 with a maximum of 100.
- A 200 response is a successful list request. Its schema marks `data`, pagination totals and links, and device detail fields optional; listed device types are `ios`, `android`, and `browser`. It does not establish a device registration, cardholder authentication, or payment outcome.
- The reference lists 400, 401, 403, 422 and 500 errors; 401 means authentication is required and 403 means insufficient permission. Its 422 and 500 sample messages concern changing a balance account or creating a payment instrument, so they do not establish behavior or lifecycle rules for this read endpoint.
- The captured server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. The `latest` URL and test snapshot do not establish a fixed current release, live availability, or account-specific access.

## Detail locators

- Request purpose and test server: pinned raw lines 5–10.
- Required payment-instrument filter and pagination bounds: pinned raw lines 12–19.
- Successful response fields and pagination links: pinned raw lines 21–46.
- Error statuses and schemas: pinned raw lines 49–146; example payloads: lines 148–215.

## Related

- [[adyen-issuing]] — issuer-side card and SCA context.
- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-manage-devices]] — separate device-management guide; this reference only describes a list request.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/registeredDevices/2026-09-15|Captured GET /registeredDevices API Explorer page]]
