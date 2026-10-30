---
title: "Adyen Balance Platform API v2: POST /registeredDevices"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/registeredDevices"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/registeredDevices/2026-09-15.md"
tags: [adyen, balance-platform, sca, device-registration, api-reference]
---

## Overview

This 2026-09-15-captured Balance Platform API v2 test-server reference defines `POST /registeredDevices` to **initiate** registration of a user's Strong Customer Authentication (SCA) device for a payment instrument. It points to separate [[adyen-business-accounts|Business Accounts]] and [[adyen-issuing|Adyen Issuing]] registration guides. A successful request requires an SCA-eligible device; this endpoint alone does not complete enrollment.

## Key takeaways

- The request-body field table marks `paymentInstrumentId` and `strongCustomerAuthentication.sdkOutput` required. The latter is base64-encoded data obtained through the authentication SDK. `name` is optional; Adyen generates one if omitted. The table describes required properties, but does not separately state whether the whole request body is required.
- The 200 response has optional `id`, `paymentInstrumentId`, `sdkInput`, and `success` fields. `sdkInput` must be passed to the authentication SDK to **continue** registration; `success` says whether initiation succeeded, not whether the device was registered, associated, approved or used to authenticate an action.
- Errors documented here are 400 request problem, 401 authentication required, 403 insufficient permissions, 422 request validation, and 500 server processing failure. The 422 and 500 JSON examples mention payment-instrument balance-account changes or creation, unrelated to this registration operation; they do not define its device-registration error conditions. The snapshot gives no specific credential role, completion result, idempotency behavior, live availability, payment result or funds movement.

## Detail locators

- Purpose, supported product routes, eligibility and test v2 server: raw lines 5–12.
- Request property table: raw `## Parameters` / `### Request body`, lines 14–22.
- Initiation response: raw `### 200 Success`, lines 26–35.
- Error schemas: raw `### 400 Client Error` through `### 500 Server Error`, lines 38–135. Generic examples, including unrelated 422/500 prose: raw `## Response examples`, lines 137–204.

## Related

- [[adyen-business-accounts]] — Business Accounts SCA device flow.
- [[adyen-issuing]] — Adyen-issued card device flow.
- [[adyen-api-access]] — credential context; this reference names only authentication and permission errors.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/registeredDevices/2026-09-15|POST /registeredDevices captured 2026-09-15]]
