---
title: "Adyen Classic Payment API POST /authorise3d — complete 3DS authorisation"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/authorise3d"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/authorise3d/2026-09-15.md"
tags: [adyen, classic-payment-api, 3d-secure, authorisation, migration]
---

## Overview

This 2026-09-15 API Explorer snapshot describes **Classic Payment API** `POST /authorise3d`, which completes payment authorisation following an authenticated 3D Secure session using issuer-returned `md` and `paResponse`. Its captured server is the **v68 test** Payment endpoint, despite `latest` in the canonical route. Adyen marks this endpoint **inactive** and unsupported for new integrations, routes new integrations to Checkout API `/payments/details`, and directs existing integrations to migrate. See [[adyen-3d-secure]] and [[adyen]].

## Key takeaways

- The request-body table marks `md` (issuer-returned payment-session identifier), `paResponse` (issuer-returned PaRes), and `merchantAccount` as required properties. The opening paragraph likewise says the endpoint must receive the two issuer parameters. The example supplies those plus `shopperIP`; an illustrative example is not a complete catalog of conditional requirements.
- Other body fields are marked optional at the top level, but the descriptions add conditions: `billingAddress` for browser/mobile 3DS2, browser information for web 3DS, certain contact/IP fields for Visa/JCB 3DS2 cases, `threeDS2RequestData.deviceChannel` within that object, and app SDK or browser notification fields in their specified 3DS2 scenarios. The long nested schema and its exact conditions remain at the raw locators. Recommendations for risk/account information are not unconditional requirements.
- `threeDSAuthenticationOnly: true` requests 3DS2 authentication without payment authorisation; the similarly named `threeDS2RequestData.authenticationOnly` has its own conditional description. The response's `AuthenticationFinished` and `AuthenticationNotRequired` codes therefore must not be read as authorised payments.
- A `200 Success` means the API request succeeded, not necessarily that the payment was authorised. The optional `resultCode` can describe `Authorised`, refusal/error, partial authorisation, further shopper action, pending or `Received` states, or authentication-only states; `refusalReason` qualifies failures, and `pspReference` identifies the transaction/request. `Authorised` is an authorisation state, not capture or settlement evidence.
- The reference also documents `400`, `401`, `403`, `422`, and `500` error schemas; the response examples are generic for `400`, `401`, and `500`. No successful authorisation example or live execution is established by this snapshot. Its Classic schema must not be transferred to the Checkout `/payments/details` route merely because that route is named as the migration successor.

## Detail locators

- Purpose, inactive/new-integration warning, migration route, and v68 test server: raw lines 5–18.
- Required `md`, `merchantAccount`, `paResponse`; 3DS2 address/browser/phone and other conditional request fields: raw lines 22–259, especially 74–90, 130–165, 183–184, 203–229, 259.
- Example body: raw lines 263–273.
- `200` response fields, `pspReference`, `resultCode` alternatives and refusal meaning: raw lines 274–297.
- HTTP error schemas and generic examples: raw lines 300–406.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-3d-secure]]
- Classic-to-Checkout migration guide: [[source-adyen-docs-online-payments-upgrade-your-integration-migrate-to-checkout-api]]
- Checkout successor reference: [[source-adyen-api-explorer-checkout-latest-post-payments-details]]

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/authorise3d/2026-09-15|Classic Payment API POST /authorise3d (2026-09-15)]]
