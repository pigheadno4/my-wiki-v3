---
title: "PATCH /registeredDevices/{deviceId}/associations — Complete an SCA device association | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/registeredDevices/(deviceId)/associations"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/registeredDevices/(deviceId)/associations/2026-11-03.md"
tags: [adyen, balance-platform, sca, registered-devices, issuing, business-accounts, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `PATCH /registeredDevices/{deviceId}/associations` to complete an association between a user's registered SCA device and an Adyen resource. It validates the registered device's authentication data. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest` while the server path identifies `v2`. The page gives additional Business Accounts and Adyen-issued cards as examples; see [[adyen-business-accounts]] and [[adyen-issuing]] for those contexts.

## Key takeaways

- Required string path `deviceId` identifies the SCA device. The request table requires `ids`, an array of resource identifiers capped at five strings; `strongCustomerAuthentication`, whose required `sdkOutput` is base64-encoded authentication SDK data; and `type`, whose only listed value is `PaymentInstrument`. The page lists no query parameters, request defaults or idempotency key. [Raw: lines 14–28]
- The 200 response is labeled request success. Its body requires `type`, while `deviceId` and the associated resource `ids` are optional fields. Although the endpoint is described as completing an association, this response does not report a separate association status or a later SCA challenge result. [Raw: lines 5–9, 30–40]
- Errors listed are 400 request-reading/understanding, 401 authentication, 403 insufficient permissions, 422 validation and 500 server processing. No exact credential role, duplicate-association behavior, prior-association replacement rule, propagation timing, deletion or reversal path is specified here. The generic 422 and 500 examples concern payment-instrument update/creation, not this association's result. [Raw: lines 43–208]
- Completing a device-resource association is distinct from authenticating a later transaction, activating a card, approving a transfer, booking funds or proving compliance. The dated TEST v2 snapshot does not establish current live availability or eligibility for any particular user or resource. [Raw: lines 5–40]

## Detail locators

- Purpose, authentication-data validation and TEST v2 server: pinned raw lines 5–12.
- Path ID, required request fields and five-ID maximum: lines 14–28.
- 200 response shape: lines 30–40.
- Errors and generic examples: lines 43–208.

## Related

- [[adyen-business-accounts]] — Business Accounts SCA device context.
- [[adyen-issuing]] — issued-card SCA device context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/registeredDevices/(deviceId)/associations/2026-11-03|PATCH registered-device associations — captured 2026-11-03]]