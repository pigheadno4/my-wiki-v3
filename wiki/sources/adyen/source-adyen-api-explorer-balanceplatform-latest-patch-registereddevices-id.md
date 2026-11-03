---
title: "Adyen Balance Platform API v2: Complete SCA device registration"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/registeredDevices/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/registeredDevices/(id)/2026-11-03.md"
tags: [adyen, balance-platform, sca, device-registration, api]
---

## Overview

Captured Balance Platform API v2 TEST reference for `PATCH /registeredDevices/{id}`. The operation validates device authentication data to complete SCA-device registration for a Business Account or an Adyen-issued card. It follows an earlier `POST /registeredDevices`, whose response supplies the device `id`. See [[adyen]], [[adyen-business-accounts]] and [[adyen-issuing]].

## Key takeaways

- Path `id` is the required SCA-device identifier. The request-body table marks `paymentInstrumentId` and `strongCustomerAuthentication` required, with required nested `sdkOutput` from the authentication SDK; it does not separately state whole-body requiredness. Optional `name` identifies the device to users, and Adyen generates one if omitted. The reference gives no query parameters, limits or idempotency contract.
- The 200 response has an optional `success` boolean. The API field description says it specifies whether registration was initiated successfully, while the operation heading and description call this completion. The [[source-adyen-docs-business-accounts-register-sca-devices|Business Accounts]] and [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-register-devices|Issuing]] guides separately instruct the server to check for `success: true` after PATCH before treating registration as complete; a bare 200 or omitted `success` should not be promoted to that confirmation.
- Errors listed are 400 request problem, 401 authentication required, 403 insufficient permissions, 422 request validation and 500 server failure. The generic 422 and 500 examples describe payment-instrument changes/creation, not SCA-device-registration conditions. The page gives no named credential role, association-propagation time, later authentication outcome, card activation, payment or funds result.

> [!warning] Contradiction
> This API reference calls PATCH a registration-completion operation (pinned raw lines 5–7), but its optional `success` field describes successful initiation (line 36). The two product guides require `success: true` for completion (Business Accounts guide raw lines 690–692; Issuing registration guide raw lines 658–660). Preserve this wording mismatch and use the guide's explicit success check for that guide's flow; the API response alone does not document a separate subsequent state transition.

## Detail locators

- Purpose, TEST server, prior POST-derived device ID and request fields: pinned raw lines 5–26.
- 200 optional `success` field and listed errors: pinned raw lines 28–136.
- Generic error examples, including unrelated 422 and 500 wording: pinned raw lines 138–205.
- Product-guide finalization: Business Accounts registration guide raw lines 451–461 and 690–694; Issuing device-registration guide raw lines 419–445 and 658–660.

## Related

- [[adyen-business-accounts]] — Business Account SCA context.
- [[adyen-issuing]] — Adyen-issued card SCA context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-registereddevices]] — earlier registration initiation and device ID.
- [[source-adyen-docs-business-accounts-register-sca-devices]] — Business Accounts SDK and server finalization flow.
- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-register-devices]] — Issuing SDK and server finalization flow.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/registeredDevices/(id)/2026-11-03|Captured PATCH /registeredDevices/{id} API reference (2026-11-03)]]