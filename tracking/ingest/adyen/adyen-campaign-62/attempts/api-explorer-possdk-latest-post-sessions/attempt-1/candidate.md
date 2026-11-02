---
title: "Adyen POS Mobile SDK POST /sessions communication session"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/possdk/latest/post/sessions"
raw_files:
  - "adyen/api-explorer/possdk/latest/post/sessions/2026-09-15.md"
tags: [adyen, mobile-pos, pos-mobile-sdk, api-explorer, sessions]
---

## Overview

This 2026-09-15 `POST /sessions` API Explorer snapshot describes establishing a mutually authenticated communication session between the **POS Mobile SDK** and Adyen payments platform. It applies to mobile in-person transactions; the page expressly excludes creating online payments sessions. This is the POS SDK `v68` test route, not an online Checkout Sessions contract. See [[adyen]] and [[adyen-mobile-pos]].

## Key takeaways

- The sole listed server is `https://checkout-test.adyen.com/checkout/possdk/v68`. The `latest` page path does not establish a later API version or a live endpoint. The page does not identify the HTTP caller or prescribe a backend architecture, though it conditionally addresses backend-built Terminal API transaction requests.
- The request-body table marks string `merchantAccount` and string `setupToken` required, and string `store` optional. The setup token is supplied by the POS Mobile SDK and identifies the SDK and device. The table specifies Android `AuthenticationService.authenticate(setupToken)` and iOS `PaymentServiceDelegate.register(with:)` callback routes to obtain it; the example includes optional `store`. The page does not separately label the request body itself required.
- The documented `201 Success` says the request was fulfilled and one or more resources created. Every **listed response property** is marked `No` in the table: `id` (session identifier), `installationId` (SDK-installation identifier), `merchantAccount`, `sdkData`, and `store`. The example shows all five, but it is not a required-field guarantee. If the Terminal API transaction request is created on a backend, the page directs using `installationId` as `MessageHeader.POIID`. It directs passing `sdkData` to the POS app so the SDK can authenticate platform responses.
- The prose calls the returned material a 'session token', while the schema lists `id` and `sdkData`, without a field literally named `sessionToken`. Do not infer which response property the prose means. A created communication session and response-authentication data are not a completed payment, payment authorization, capture, reconciliation, settlement or bank receipt.
- This page provides no session expiration, renewal, retry, failure/error response, revocation, correlation, asynchronous outcome or live enablement rule.

## Detail locators

- Purpose, mutual authentication and mobile in-person scope: raw lines 5–10.
- Test server and request fields/callbacks: raw lines 12–33.
- `201` meaning, response field requiredness and conditional POIID guidance: raw lines 34–61.

## Related

- [[adyen]]
- [[adyen-mobile-pos]]

## Raw Sources

- [[raw/adyen/api-explorer/possdk/latest/post/sessions/2026-09-15|Adyen POS Mobile SDK POST /sessions snapshot, 2026-09-15]]
