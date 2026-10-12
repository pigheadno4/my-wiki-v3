---
title: "Redirect 3DS2 iOS Drop-in integration | Adyen Docs"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/redirect-3ds2/ios-drop-in"
raw_files:
  - "adyen/docs/online-payments/3d-secure/redirect-3ds2/ios-drop-in/2026-09-15.md"
tags: [adyen, ios, drop-in, cards, 3d-secure, 3ds2, redirect, checkout-api]
---

## Overview

This Adyen webpage describes redirect 3D Secure 2 card authentication in an existing iOS Drop-in integration. It routes the merchant from card-field configuration and server-side `/payments` parameters through Drop-in's redirect action, app return, server-side `/payments/details`, result presentation, and asynchronous payment webhook. The captured page is a 2026-09-15 snapshot whose own `last_modified` metadata is 2021-05-11; its SDK links and multi-language API examples are versioned examples, not evidence of current SDK behavior.

## Key takeaways

- The merchant first needs its iOS Drop-in and backend integration and cards enabled in the test Customer Area. The guide recommends collecting holder name and billing address for authentication performance. Drop-in supplies `data.paymentMethod` in `didSubmit`; the app passes it to the merchant server, which makes `/payments` with the iOS channel, an app return URL, browser information, and other required or conditionally required 3DS fields. Consult the parameter table for scheme-specific conditions, including Visa and JCB.
- If `/payments` has no `action`, this guide describes the transaction as exempt or out of scope for 3DS authentication and routes the `resultCode` to shopper presentation. For `action.type=redirect`, the merchant passes the action to the iOS app; Drop-in handles the redirect. The app informs Drop-in of its custom-URL return through `RedirectComponent.applicationDidOpen(from:)`, then `didProvide` supplies details for the merchant server's `/payments/details` request.
- The page distinguishes Checkout API v67 and later, where it says authorization happens after shopper authentication and `/payments/details` obtains the payment result, from earlier versions where the request containing payment data completes the payment. Use the returned `resultCode` for the shopper-facing result; an asynchronous webhook also reports the outcome. An `Authorised` card result still requires capture when manual capture is configured.
- On live endpoints, all API requests for one payment session must use the same live endpoint region. Mixing regions between `/payments` and `/payments/details` may cause 3DS authentication errors.

## Detail locators

- `## Requirements`, `## Collect additional parameters in your payment form`, and `## Show the available cards in your payment form` — existing integration, card setup, holder-name and billing-address guidance, `/paymentMethods`, and iOS configuration.
- `## Make a payment` — client/server handoff, parameter table with unconditional and conditional fields, versioned sample requests, and no-action versus redirect-action response routing.
- `## Handle the redirect result` — iOS app-delegate callback, `didProvide` data, server-side `/payments/details`, and Checkout API version distinction.
- `## Present the payment result` — synchronous result codes, asynchronous webhook, and manual-capture qualification.
- `## Test and go live` — test scenario navigation, go-live route, and same-region live endpoint warning.

## Related

- Company: [[adyen]]
- Concept: [[adyen-3d-secure]]
- Related native integration concept: [[adyen-ios-sdk]]
- Web counterpart: [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-web-drop-in]]

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/ios-drop-in/2026-09-15|2026-09-15 snapshot — iOS Drop-in redirect 3DS2 guide]]
