---
title: "Adyen 3D Secure 2 API reference"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/api-reference"
raw_files:
  - "adyen/docs/online-payments/3d-secure/api-reference/2026-09-15.md"
tags: [adyen, 3d-secure, 3ds2, checkout-api, authentication, api-reference]
---

## Overview

This [[adyen]] 3D Secure 2 parameter reference covers Checkout API v41 or later, including additional data for `/payments`, `/payments/details`, and `/sessions`. It distinguishes required, conditionally required, recommended, and optional request data, then gives object fields, challenge-flow data, authentication statuses, and third-party MPI data combinations. Classic integrations are routed to a separate reference. Use [[adyen-3d-secure]] for the wider merchant integration context.

## Key takeaways

- Requiredness varies by integration, scheme, issuer, and use case. Some omitted objects can cause authentication failure. The top-level table marks `browserInfo` required, while its dedicated section says the full object except `javaScriptEnabled` is required for Web and recommends the object for iOS/Android to support possible redirect routing. Consult the relevant table and channel-specific section together.
- For browser-based Web transactions, the reference conditionally requires `origin` and warns that an absent or incorrect value prevents proper handling of the 3DS2 action. For Visa and JCB it calls for `shopperEmail` or a qualifying phone number, and `shopperIP` across web and mobile; it says malformed phone numbers are dropped from authentication submission. See the exact conditions and formats in the raw object table.
- `authenticationData.authenticationOnly=true` triggers standalone 3DS2 authentication without proceeding to payment authorization. `authenticationData.threeDSRequestData.dataOnly` is available from Checkout API v69; v68 or earlier uses `additionalData.threeDSDataOnly`. `nativeThreeDS=preferred` indicates native when available, but Adyen may still select redirect; the `/payments` and `/sessions` trigger contexts differ.
- Adyen discourages `authenticationData.attemptAuthentication`, which overrides Dynamic 3D Secure settings; `never` can lead to decline where regulations require authentication. It also discourages `scaExemption` because it overrides Adyen's exemption logic. These are conditional request choices, not general requirements to force an exemption or native flow.
- For a separate Adyen authorization using third-party 3DS2 authentication, `mpiData` is required and the reference says to include all fields received from that provider. The raw lists `transStatus` and scheme-specific `transStatusReason`, `challengeCancel`, and expected MPI value combinations. Authentication status here does not establish payment authorization.

## Detail locators

- **Scope, endpoints, and requiredness legend:** raw lines 17–42.
- **Top-level object conditions:** raw lines 44–69, including `origin`, `returnUrl`, email/phone/IP, and exemption behavior.
- **Account and authentication controls:** raw lines 71–155, including v68 phone-field deprecations, authentication-only, data-only, and native/redirect selection.
- **Browser and other object fields:** raw lines 157–259, including channel-specific `browserInfo`, addresses, installments, and merchant risk data.
- **Third-party MPI and status values:** raw lines 260–379, including scheme-specific combinations and EMVCo mappings.
- **Card, app/browser 3DS request fields, and challenge objects:** raw lines 380–460, including native SDK version, external-acquirer standalone conditions, `notificationURL`, and `/payments/details` data.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[source-adyen-docs-online-payments-3d-secure]]
- [[source-adyen-docs-online-payments-3d-secure-authorize-mpidata]]
- [[source-adyen-docs-online-payments-3d-secure-standalone-authentication]]

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/api-reference/2026-09-15|Adyen 3D Secure 2 API reference — collected 2026-09-15]]
