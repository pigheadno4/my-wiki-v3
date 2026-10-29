---
title: "Adyen IRIS Web Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/iris/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/iris/web-drop-in/2026-09-15.md"
tags: [adyen, iris, web, drop-in, redirect, qr-code]
---

## Overview

This captured [[adyen]] guide adds IRIS to an existing Web Drop-in integration. It separates Sessions and Advanced server flows, then splits Advanced payments into issuer redirect and QR-code paths. It is a method-specific add-on; the linked base integration still supplies general checkout requirements. The snapshot and test examples do not establish current merchant enablement or a real successful payment. [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and onboarding:** Sessions requires an existing Web Drop-in Sessions integration and Checkout API v68 or later. Advanced requires an existing Web Drop-in Advanced integration configured to handle `redirect` and `qrCode` actions; that row does not state a Checkout API minimum. Both require adding IRIS in Customer Area. Before live use, the page calls for a request to the merchant's Greek bank and Adyen with the DIAS code, merchant account and associated stores, followed by live Customer Area enablement (raw lines 25–35, 68–78, 1054–1065).
- **Sessions scope:** The guide says no IRIS-specific parameters are needed when creating the base `/sessions` request. Importing `Iris` separately is optional for tree shaking. Its simulator can select Successful, Refused or Cancelled on an Adyen-hosted test page; that is simulated test behavior (raw lines 39–66).
- **Advanced issuer redirect:** Add `paymentMethod.type: iris` to `/payments`. For issuer redirect, `paymentMethod.issuer` is required and `returnUrl` is required; including the issuer ID produces a redirect URL. The 10 EUR example uses EUR 1000 minor units and issuer `PIRBGRAA`. Redirect with `action.url`; after the shopper returns, the server sends the URL-decoded `redirectResult` inside `details` to `/payments/details`, then uses its `resultCode` for shopper presentation. The example `Authorised` response is illustrative, not execution evidence (raw lines 94–129, 426–455, 694–706).
- **Advanced QR path:** Without `paymentMethod.issuer`, the `/payments` response contains QR data; `returnUrl` is not required for QR, although the QR request examples include it. The example response is `Pending` with `action.type: qrCode` and `qrCodeData`. Render the code; the shopper has 10 minutes to complete the transaction, and the guide recommends showing a timer. A webhook supplies the payment result after the shopper scans and completes payment. Do not treat `Pending`, QR display or simulator selection as final payment proof (raw lines 101–102, 708–733, 1026–1052).
- **Source example/link caveats:** In the section labeled issuer redirect, Java, PHP, C#, Go and TypeScript payment-request samples omit the issuer ID that the same page says is required for that branch; follow the branch rule rather than those sample omissions (raw lines 102, 153–253, 305–327, 403–424). Both curl payment examples put `-X POST` on a line without a continuation before `-d`, so they are not copy-ready (raw lines 112–130, 716–734). The Advanced integration requirement link contains an unresolved encoded platform template; the later action/request/import links explicitly target Advanced Web Drop-in (raw lines 76–96).

## Detail locators

- Identity, Sessions/Advanced prerequisites, optional import and onboarding: pinned raw lines 15–90.
- Advanced field table, issuer redirect request/examples and response: pinned raw lines 92–440.
- Redirect return and server details/result: pinned raw lines 442–706.
- QR request/examples, pending action, ten-minute window and webhook: pinned raw lines 708–1052.
- Simulator and live setup: pinned raw lines 1054–1065.

## Related

- [[adyen-online-payments]] — provider online payment architecture and method routes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/iris/web-drop-in/2026-09-15|IRIS Web Drop-in, captured 2026-09-15]]
