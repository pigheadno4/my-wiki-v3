---
title: "Adyen Classic API native 3DS2 parameter reference"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/api-reference-3d-secure-2"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/api-reference-3d-secure-2/2026-09-15.md"
tags: [adyen, classic-api, 3ds2, authentication, api-reference]
---

## Overview

This [[adyen]] reference catalogs 3D Secure 2 request objects and result fields for the Classic API `/authorise` integration, including native browser and app cases, challenge results, authentication-only responses, and third-party MPI data. Adyen says it no longer develops or accepts new Classic API integrations and recommends migrating to the Checkout API 3D Secure integration. Existing Classic 3DS2 support uses v40 or later of `/authorise`, `/authorise3ds2`, and `get3dsAvailability`. Use [[adyen-3d-secure]] for the broader merchant 3DS route; the [[source-adyen-docs-online-payments-3d-secure-api-reference|Checkout API 3DS2 reference]] is a separate API scope.

## Key takeaways

- The top-level table marks many 3DS2 objects optional in the request schema, but the page warns that an issuer or card scheme may require some data and omission may fail authentication. Do not read a top-level optional marker as proof that a specific transaction needs no data. For browser `deviceChannel`, the dedicated section requires the full `browserInfo` object; for app fallback to 3DS1 redirect, `userAgent` and `acceptHeader` are required if that fallback is to be supported. The page says card schemes require `billingAddress` and `shopperEmail` for browser or app implementations, while its top-level table marks those objects optional; preserve that distinction rather than recasting the table as universal runtime validation.
- `threeDS2RequestData` has conditional browser, app SDK, external-acquirer authentication-only, and scheme-specific fields. The page's later Checkout API v50/v68 notes appear inside this Classic reference; apply them only to the fields and versions they name.
- `authenticationData.authenticationOnly=true` performs 3DS2 authentication without payment authorization. An authentication-only `/authorise3ds2` response can carry `additionalData.threeDS2Result` values such as authentication value, directory transaction ID, ECI, status, and reason; these are authentication evidence, not proof of an authorized payment.
- `mpiData` is for using 3DS2 authentication data from another provider in a separate Adyen authorization. The reference defines flow- and scheme-specific `directoryResponse`, `authenticationResponse`, and ECI combinations, including Cartes Bancaires' optional ECI. A matching combination is a request-data rule, not an authorization outcome.
- The reference distinguishes `transStatus` authentication/challenge values from `transStatusReason` and `challengeCancel` codes. In `additionalData.threeDS2Result`, status `C` means a challenge is required, and reason codes 80–82 have scheme-specific meanings.

## Detail locators

- **Classic scope, migration warning, endpoints, top-level objects:** raw lines 15–51, under `# API reference` and `## 3D Secure 2 additional parameters`.
- **Account, billing, browser, card, delivery, installments, merchant risk:** raw lines 53–220, under the corresponding `##` headings; distinguish object inclusion from required child fields.
- **Third-party MPI statuses, reason and cancellation codes, combinations:** raw lines 222–347, under `## mpiData`.
- **Recurring and exemption request fields, contact data, conditional 3DS2 request fields:** raw lines 349–429, under `## recurring`, `## scaExemption`, `## shopperEmail`, `## shopperIP`, `## socialSecurityNumber`, and `## threeDS2RequestData`.
- **Challenge and authentication-only result objects:** raw lines 431–510, under `## threeDS2Result`, `## additionalData.threeDS2Result`, and `## authenticationData.authenticationOnly`.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[source-adyen-docs-online-payments-3d-secure-api-reference]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/api-reference-3d-secure-2/2026-09-15|Classic API native 3DS2 API reference — collected 2026-09-15]]
