---
title: "Adyen Issuing: manage SCA registered devices"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/manage-devices"
raw_files:
  - "adyen/docs/issuing/3d-secure/oob-auth-sdk/manage-devices/2026-09-15.md"
tags: [adyen, issuing, sca, devices, 3d-secure]
---

## Overview

Adyen's Issuing guide (last modified 2022-11-30; captured 2026-09-15) describes how to look up a card's registered SCA device, associate further card payment instruments with an already registered device, and deregister a device from a specific card. These are Balance Platform Configuration API and client authentication steps for issuer-side SCA device management, not evidence of a completed card payment. The API credential needs the **Bank SCA Webservice Role**.

## Key takeaways

- Look up devices with `GET /registeredDevices?paymentInstrumentId=<card ID>`; the response includes device ID, name, card payment instrument ID and type. The guide's GET prose and curl example conflict with its language-library snippets, which invoke registration methods. Follow the endpoint-level guide and verify library calls against the relevant SDK/API version.
- A previously registered device can authenticate multiple card payment instruments. Each payment instrument can be linked to only one device; the guide allows up to five payment instrument IDs **per association request**, not a five-card device maximum.
- To associate cards, the server POSTs `/registeredDevices/{deviceId}/associations` with `ids` and `type: PaymentInstrument`; it sends the returned encoded `sdkInput` to the client for `authenticate()`. The client returns `sdkOutput` to the server, which PATCHes the same device's association with the same IDs, `type`, and `strongCustomerAuthentication.sdkOutput`. The SDK's challenge result alone is not proof of completed association; the guide says to check each card's registered devices after a successful API response.
- For a card already linked to a device, the POST may return 422 “Device limit reached”; get and deregister existing card associations before retrying. A 422 “Challenge not found” usually means the client challenge device and PATCH device ID differ. Client `NotAllowedError` may follow cancellation; the guide allows the same `sdkInput` for retry in the same session.
- Deregistration uses `DELETE /registeredDevices/{id}` with the target card's `paymentInstrumentId` query parameter. For a device linked to multiple cards, make a separate request for each; the guide treats HTTP 204 with no content as success.

## Detail locators

- Role, lookup parameter and response fields: raw lines 25–41 and 218–254.
- Association limits and server POST: raw lines 256–262; encoded challenge/client flow: 470–567; verification after PATCH: 813–829.
- Association failure examples and remedies: raw lines 831–898.
- Per-card DELETE parameters and success response: raw lines 900–918 and 1071. Curl and SDK snippets show test environment and version-specific examples; inspect the raw before using them.

## Related

- [[adyen-issuing]] — Issuing concept and source route.
- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk]] — OOB Authentication SDK overview.
- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-install-sdk-mobile]] — SDK installation prerequisites.
- [[source-adyen-docs-issuing-manage-access-webservice-roles]] — API credential role catalogue.

## Raw Sources

- [[raw/adyen/docs/issuing/3d-secure/oob-auth-sdk/manage-devices/2026-09-15|Adyen manage SCA registered devices guide, captured 2026-09-15]]
