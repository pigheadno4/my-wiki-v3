---
title: "PayMe for API only"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payme/api-only"
raw_files:
  - "adyen/docs/payment-methods/payme/api-only/2026-09-15.md"
tags: [adyen, payme, hong-kong, api-only, qr-code, redirect, online-payments]
---

## Overview

This [[adyen]] page, metadata-modified 2019-09-06 and captured 2026-09-15, describes PayMe **API-only** payments with merchant-owned Web payment form: a **desktop/laptop QR** path and a **mobile-browser PayMe app redirect** path. It recommends implementing both for different shopper devices. It is historical method guidance, not evidence of current Hong Kong merchant eligibility or successful authorization, capture, settlement or refund. See [[adyen-online-payments]] and raw lines 15–33.

## Key takeaways

- The guide states a **Checkout API v67 minimum**, an existing API-only integration, and adding **PayMe QR in the test Customer Area**. Its payment form need not collect shopper data. For `/paymentMethods` discovery it specifies `countryCode: HK`, `amount.currency: HKD`; the response method type is `payme`. These page-specific discovery settings do not prove account enablement or wider country/currency support. See raw lines 19–46.
- Choose the shopper path by device: desktop/laptop displays QR, mobile shows an app-redirect button, and tablet may use either or both. Screen size is a **recommendation** for deciding device presentation. In the desktop `/payments` request, `paymentMethod.type: payme` and `returnUrl` are marked required; `channel` and line-item fields are listed as optional. `lineItems.sku` is available only with Checkout API **v70+**, a field-specific condition distinct from the v67 base minimum. The TEST cURL sample uses `/v72/payments`, HK/HKD and `channel: Web`. See raw lines 50–108.
- Desktop `/payments` illustrates `Pending` with a QR action carrying `qrCodeData`, `url`, `expiresAt` and `paymentData`. Render the returned `qrCodeData`; after shopper scan and completion, the page says a webhook informs the merchant of payment result. A mobile-browser shopper cannot scan that on-device code, so the page instead directs use of `action.url`. The timestamp in the sample is illustrative, not a current expiry. QR display or scan is not final authorization. See raw lines 147–175.
- Mobile `/payments` illustrates `RedirectShopper` and `action.type: redirect`, `method: GET`, `url` and `expiresAt`. Send the shopper to the returned URL; the page recommends the default/system browser over WebView for mobile compatibility. On return, POST `/payments/details` with URL-decoded `redirectResult`, then use `resultCode` to show a shopper status. The illustrated `Authorised` details response is not evidence of an actual payment. The mobile prose spells `returnURL`, whereas its requests use `returnUrl`; the Node mobile example sets `channel: "Web/iOS/Android"` while the cURL mobile example uses `channel: "Web"`. Do not copy those divergent samples as a single contract. See raw lines 177–310.
- `Cancelled` and `Refused` call for different shopper follow-up; `Pending`/`Received` remain unresolved until an **AUTHORISATION webhook**. If the shopper does not return, the guide says to wait for AUTHORISATION with `success: false` or `true` to know failure or success. This is an authorization outcome boundary, not capture or settlement proof. The sandbox can simulate `Authorised`, `OfferCancelled` on expiry, and creation `Error` by amount endings; the test table describes a **default ten-minute PayMe expiry** for the cancellation case, but does not turn the old `expiresAt` example into a current deadline. No PayMe app is needed for those sandbox tests. See raw lines 312–342.

## Detail locators

- Method scope, v67 minimum, setup and HK/HKD discovery: raw lines 15–48.
- Desktop/tablet/mobile presentation and desktop request fields; optional `sku` requires v70+: raw lines 50–76.
- Desktop TEST request, QR action and webhook handoff: raw lines 77–175.
- Mobile TEST requests, sample case/channel differences, redirect, return and details response: raw lines 177–310.
- Shopper states, no-return authorization webhooks, sandbox amount tests and ten-minute expiry statement: raw lines 312–342.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payme/api-only/2026-09-15|PayMe API-only guide — captured 2026-09-15]]
