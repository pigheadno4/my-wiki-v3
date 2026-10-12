---
title: "Adyen Redirect 3DS Android Drop-in Integration"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/redirect-3ds2/android-drop-in"
raw_files:
  - "adyen/docs/online-payments/3d-secure/redirect-3ds2/android-drop-in/2026-09-15.md"
tags: [adyen, android, drop-in, 3d-secure, 3ds2, redirect, checkout-api]
---

## Overview

This [[adyen]] guide describes adding redirect 3D Secure 2 card authentication to an existing Android Drop-in integration, for Android Drop-in v4.0.0 or later. It covers client configuration, server `/payments` parameters, redirect action handling, the shopper's return to the app, `/payments/details`, result presentation, and live endpoint routing. It is an integration guide for [[adyen-3d-secure]], not evidence of a particular payment outcome.

## Key takeaways

- The merchant configures Android Drop-in to collect the cardholder name, passes `paymentComponentData.paymentMethod` from the app to the server, and sends a `/payments` request with `channel=Android`, a Drop-in return URL, and the documented 3DS2 data. The guide's request table marks `browserInfo` with `acceptHeader` and `userAgent` as required here; it conditionally requires Visa/JCB cardholder name, shopper IP, and email or a qualifying phone number. See the raw table for precise conditions and formats.
- On `/payments`, no `action` means the guide treats the transaction as exempt or out of scope for 3DS2 and has Drop-in finish with the returned `resultCode`. With `action.type=redirect`, return `DropInServiceResult.Action` and the action so Drop-in redirects the shopper. After return to the app, send `actionComponentData.details` to the server for `/payments/details`. Do not infer authorization from the presence or absence of a redirect; use the result and asynchronous webhook outcome.
- Checkout API v67+ and v66-or-earlier have different completion steps. The guide says v67+ authorizes after shopper authentication and calls `/payments/details` to obtain the payment result; earlier versions need `paymentData` in `/payments/details` to complete payment. For v66 or earlier, its response table says to store `action.paymentData` on the server, while its later details instruction describes that value as stored locally in the client app. The snapshot therefore leaves the storage location internally inconsistent; verify the applicable version-specific integration before implementing that older handoff.
- The examples use test endpoints and test environment. For live traffic, the guide warns that `/payments` and `/payments/details` for the same payment session must use the same live endpoint region, or 3DS authentication errors may result. An `Authorised` result may still require capture when manual capture is configured.

## Detail locators

- **Scope, prerequisites, and Drop-in card configuration:** raw lines 15–66.
- **Payment request conditions and return URL:** raw lines 68–93. Multi-language request examples, with test values and library versions, occupy raw lines 95–587.
- **`/payments` action handling by Checkout API version:** raw lines 589–651.
- **Return to app and `/payments/details` version split:** raw lines 653–664. Request/response examples occupy raw lines 666–794.
- **Result codes, webhook outcome, testing, and live region warning:** raw lines 798–817.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[source-adyen-docs-online-payments-3d-secure]]
- [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-web-drop-in]]

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/android-drop-in/2026-09-15|Adyen Redirect 3DS Android Drop-in — collected 2026-09-15]]
