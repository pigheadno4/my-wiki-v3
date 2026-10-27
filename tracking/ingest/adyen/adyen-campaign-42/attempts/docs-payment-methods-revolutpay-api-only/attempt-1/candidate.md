---
title: "Revolut Pay API-only integration | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/revolutpay/api-only"
raw_files:
  - "adyen/docs/payment-methods/revolutpay/api-only/2026-09-15.md"
tags: [adyen, revolut-pay, wallet, api-only, redirect, capture]
---

## Overview

This 2026-09-15 Adyen child guide adds Revolut Pay to an existing API-only integration with a merchant-built payment form, Checkout API payment-method lookup, `/payments` redirect action and `/payments/details` return. It is not a complete base integration. The related [[source-adyen-docs-payment-methods-revolutpay|Revolut Pay overview]] labels the offering pilot-phase and closed beta, with eligibility-based access; this page's examples do not establish current eligibility or merchant enablement (this raw lines 15–39; overview raw lines 23–25, 36–46).

## Key takeaways

- The existing API-only integration must handle `action.type: redirect`. The shopper chooses Revolut Pay, then is sent to the Revolut app on mobile or a hosted page on desktop/laptop with QR, email, SMS and passkey sign-in options. The API-only form does **not** need to collect shopper information, although `/payments` lists optional `shopperName`, `telephoneNumber` and `shopperEmail` fields (raw lines 23–39, 322–332). The overview also describes browser checkout if the mobile app is absent, so the path is conditional rather than app-only (overview raw lines 27–30).
- For `/paymentMethods`, the page lists `amount.currency` values EUR, GBP, PLN, RON, HUF, CHF, CZK, NOK, DKK and SEK to include Revolut Pay in the response; this is a request-side list, not a guarantee that an ineligible account or shopper will see it. `/payments` requires `paymentMethod.type: revolutpay`. Its optional `shopperStatement` is a suffix appended to a merchant-name base fixed when Revolut Pay was added to the merchant account; the suffix allows up to 19 characters and Adyen recommends a complete descriptor of at most 22 characters to reduce bank truncation (raw lines 43–49, 309–332).
- The `/payments` example returns `RedirectShopper` and a GET `action.url`; send the shopper to that URL. For mobile, the source recommends the device's default browser for compatibility with multi-factor authentication and app switching; for embedded GET handling it recommends SFSafariViewController on iOS or Chrome Custom Tabs on Android over WebView. After return, POST URL-decoded `redirectResult` in `/payments/details`, then use its `resultCode` and `pspReference` (raw lines 584–650). `Authorised` is successful authorization but the page says to ship only after successful capture. `Pending`/`Received` await an `AUTHORISATION` webhook; if the shopper never returns, use that webhook to determine success or failure. Cancelled, Error (with `refusalReason`) and Refused have distinct shopper actions (raw lines 652–667).
- Capture can be manual or automatic with or without delay, depending on merchant settings. For manual or delayed automatic capture, capture an authorized Revolut Pay payment within **7 days** or authorization expires. A partial capture permanently releases the uncaptured remainder; do not assume multiple partial captures. If no capture is intended, cancel the authorization. The source gives a `/refunds` path for captured payments and a **12-month** post-capture refund window (raw lines 669–683). The overview's feature table marks recurring unavailable and its broad country/currency labels do not override this page's request-specific list or the pilot access gate (overview raw lines 32–38).
- TEST uses a simulated browser path because there is no test version of the Revolut retail app; the listed phone/passcode/approval steps are for that test environment, not a live checkout script. Live acceptance requires a request in the live Customer Area and pilot eligibility remains separate. The initial curl examples omit a line continuation before `-d`; many `/payments` language snippets call `paymentRequest` without constructing it, so verify request construction against the Checkout API rather than copying those snippets as complete code (raw lines 55–68, 338–383, 385–430, 471–492, 564–582, 685–704; overview raw lines 23, 36–38).

## Detail locators

- API-only prerequisite, shopper handoff and no required form collection: raw lines 23–39.
- `/paymentMethods` currencies and example availability response: raw lines 43–49, 309–320.
- `/payments` fields, statement descriptor and example limitations: raw lines 322–383, 385–582.
- Redirect action, safe browser recommendations and `/payments/details`: raw lines 584–650.
- Result/webhook distinctions, capture/cancel/refund: raw lines 652–683.
- TEST simulation and live request: raw lines 685–704.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-payment-capture]]
- [[source-adyen-docs-payment-methods-revolutpay|Revolut Pay overview (pilot/closed-beta access)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/revolutpay/api-only/2026-09-15|Revolut Pay API only, fetched 2026-09-15]]
