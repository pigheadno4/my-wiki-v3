---
title: "POST /registeredDevices/{deviceId}/associations — Initiate SCA device associations | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/registeredDevices/(deviceId)/associations"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/registeredDevices/(deviceId)/associations/2026-11-03.md"
tags: [adyen, balance-platform, business-accounts, issuing, sca, device-associations, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `POST /registeredDevices/{deviceId}/associations` to initiate association of a user's registered SCA device with Adyen resources. The page gives Business Accounts and Adyen-issued cards as examples; its request schema specifically allows `PaymentInstrument` as `type`. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest`, while the server path identifies v2. See [[adyen-business-accounts]] and [[adyen-issuing]] for the respective product contexts. [Raw: lines 5–10, 20–24]

## Key takeaways

- Required string path `deviceId` identifies the SCA device. The request-body table marks `ids`, an array of up to five resource ID strings, and `type` required; the only listed `type` value is `PaymentInstrument`. The page does not separately mark the whole body required or specify an array minimum, duplicate-ID behavior, a caller-role name or an idempotency contract. Do not read the Business Accounts example as permission to send another resource type in this captured schema. [Raw: lines 12–24]
- A 200 says the request succeeded. The sole response-body field is optional string `sdkInput`, described as data to pass to the authentication SDK to continue the association process. The page does not say that 200 or an `sdkInput` completes association, user authentication, card activation, Business Account access, a payment or a transfer. It provides no final association status, callback, propagation timing or replacement/deletion behavior. [Raw: lines 26–34]
- Documented failures are 400 request-reading/understanding, 401 authentication, 403 permission, 422 validation and 500 server processing. The generic 422 and 500 examples refer to changing or creating a payment instrument, not this association result. No response example demonstrates successful SDK continuation. [Raw: lines 37–202]

## Detail locators

- Purpose, product examples, TEST v2 server, path and request IDs/type: pinned raw lines 5–24.
- 200 response and SDK continuation field: lines 26–34.
- Error headings/schemas and generic examples: lines 37–202.

## Related

- [[adyen-business-accounts]] — Business Account SCA device context.
- [[adyen-issuing]] — issued-card SCA device context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/registeredDevices/(deviceId)/associations/2026-11-03|Initiate registered-device associations — captured 2026-11-03]]