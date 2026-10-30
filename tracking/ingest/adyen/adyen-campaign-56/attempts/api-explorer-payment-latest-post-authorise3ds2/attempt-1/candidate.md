---
title: "Adyen Payment API POST /authorise3ds2 (captured v68)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/authorise3ds2"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/authorise3ds2/2026-09-15.md"
tags: [adyen, payment-api, classic-api, 3ds2, authorisation]
---

## Overview

This captured [[adyen]] **Payment API** reference describes `POST /authorise3ds2` for completing payment authorisation after an authenticated 3D Secure 2 session. The listed server is `https://pal-test.adyen.com/pal/servlet/Payment/v68`. The endpoint is marked inactive and unsupported for new integrations; the page directs new integrations to Checkout API `/payments/details` and existing users to migrate. This Payment API contract must not be read as the Checkout endpoint's schema. See [[adyen-3d-secure]].

## Key takeaways

- Introductory prose says the endpoint must receive both `threeDS2Token` and `threeDS2Result`, but the request table marks each `No`, and the supplied request example contains the token without a result. Preserve this inconsistency; do not infer a universally sufficient request from the example or silently treat the table as overriding the prose.
- The request table marks `amount`, `merchantAccount`, and `reference` required. Inside `amount`, `currency` and `value` are required. The `threeDS2RequestData.deviceChannel` nested field is marked required if that object is supplied; app, browser, Visa/JCB, recurring, and authentication-only routes carry further conditional fields in the table. `billingAddress` is described as required for 3DS2 browser and mobile implementations, while `browserInfo` is required for web 3DS integrations.
- `threeDSAuthenticationOnly=true` means authentication without payment authorisation. A `200` response is an API success, while `resultCode` distinguishes `AuthenticationFinished`, `Authorised`, `ChallengeShopper`, `IdentifyShopper`, `Pending`, `Received`, `Refused`, and other outcomes. `Authorised` is an authorisation state, not evidence of capture or settlement. `pspReference` identifies the Adyen transaction/request; `refusalReason` applies to refusals or errors.
- The page documents HTTP 400, 401, 403, 422, and 500 error schemas and examples for 400, 401, and 500. Those examples do not exhaust failure behavior. The inactive status and test v68 server bound this captured reference; `latest` in the URL does not establish current support or live execution.

## Detail locators

- Purpose, inactive/migration warning, and server: raw lines 5–18.
- Request body and conditional 3DS fields: raw lines 22–275; request example: lines 277–294.
- `200` response and result codes: raw lines 295–318. HTTP error schemas and examples: lines 321–427.

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/authorise3ds2/2026-09-15|Payment API Explorer POST /authorise3ds2 capture]]
