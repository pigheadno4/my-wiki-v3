---
title: "Adyen Balance Platform API v2: DELETE /registeredDevices/{id}"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/registeredDevices/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/delete/registeredDevices/(id)/2026-11-03.md"
tags: [adyen, balance-platform, issuing, sca, registered-devices, api]
---

## Overview

This 2026-11-03 Balance Platform API reference describes `DELETE /registeredDevices/{id}`: removing an SCA device from the registered-device list of a specific payment instrument. The shown server is the v2 TEST base `https://balanceplatform-api-test.adyen.com/bcl/v2`; this `latest` documentation URL does not establish live access or current eligibility. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The required path `id` is the unique SCA-device identifier. The required `paymentInstrumentId` query parameter identifies the payment instrument linked to that device. The captured operation lists no request body. This route's device-registration scope should not be confused with deleting a payment instrument or with the separately documented `/scaDevices/{deviceId}` route.
- The success entry is HTTP 204 and says to use the actual response code for request status; it supplies no success-body schema. A 204 establishes success of this registration deletion request in the captured API contract, but the page gives no separate confirmation of global device removal, association propagation, future SCA behavior, card status, authorization or payment outcome.
- The page lists 400 for a request problem, 401 for required authentication, 403 for insufficient permissions, 422 for validation error and 500 for a server processing failure. It gives generic error-body schemas, but no credential-role detail, not-found status, retry/idempotency rule or deletion-timing contract.
- Generic 422 and 500 JSON examples describe payment-instrument change/creation errors rather than this deregistration operation. Do not treat those example details as endpoint-specific failure conditions.

## Detail locators

- Operation purpose, TEST base, required path and query identifiers: pinned raw lines 5–23.
- Bodyless 204 success and all error schemas: `## Responses`, lines 25–128.
- Generic illustrative error payloads: `## Response examples`, lines 130–197; the 422/500 examples concern payment-instrument operations.

## Related

- [[adyen-issuing]] — Issuing card and SCA context.
- [[source-adyen-api-explorer-balanceplatform-latest-get-registereddevices]] — separate registered-device list read.
- [[source-adyen-api-explorer-balanceplatform-latest-post-registereddevices]] — separate registration initiation.
- [[source-adyen-api-explorer-balanceplatform-latest-delete-scadevices-deviceid]] — separate SCA-device deletion route.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/delete/registeredDevices/(id)/2026-11-03|DELETE registered device, 2026-11-03 capture]]