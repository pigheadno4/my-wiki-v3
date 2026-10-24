---
title: "Adyen GrabPay Android Drop-in earlier versions"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/grabpay/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/grabpay/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, grabpay, android, drop-in, paylater]
---

## Overview

This 2026-09-15 [[adyen]] page is titled **GrabPay Drop-in v4.x.x integration** and documents adding GrabPay Wallet or PayLater to an existing **Advanced-flow Android Drop-in** integration. Drop-in displays the method and redirects the shopper to GrabPay. The title identifies an earlier-version guide; its language-specific TEST API/library versions are examples, not a stated universal SDK or Checkout API minimum. This snapshot does not prove current merchant/variant enablement, authorization, capture, settlement or funds receipt. [[adyen-online-payments]]

## Key takeaways

- **Method and geography:** Add GrabPay in Customer Area. `/paymentMethods` uses `countryCode` and `amount.currency`: **MY/MYR**, **SG/SGD**, or **PH/PHP** in the table. The response method type is country-specific `grabpay_XX`. Its footnote says **GrabPay PayLater is unavailable in the Philippines**; the PH row therefore cannot be used as PayLater evidence. These are dated guide conditions, not present-day account eligibility. See raw lines 21–42.
- **Wallet versus PayLater request:** Drop-in gives the Android client `paymentComponentData.paymentMethod`, which the client sends to the merchant server for `/payments`. Both routes specify a `returnUrl` from `RedirectComponent.getReturnUrl(context)`, a unique `reference` of at most 32 alphanumeric/dash/underscore characters, and the amount. **PayLater** additionally requires `deliveryAddress` and `lineItems` for GrabPay risk checks. The guide says collecting those fields is needed only for PayLater, though it recommends gathering them early for a Wallet integration that may add PayLater. Do not make that recommendation a Wallet requirement. See raw lines 44–70 and 391–404.
- **Redirect, details and webhook:** The example `/payments` response is `RedirectShopper` with a redirect `action`; the server passes the action to Drop-in. On return, Drop-in supplies `actionComponentData.details`, which the server sends in POST `/payments/details`. The details response has `resultCode` and `pspReference`; for PayLater it may also carry `additionalData.paymentMethodVariant`, whose Wallet/PayLater variant strings are listed. `Authorised`, `Cancelled`, `Refused`, and `Pending`/`Received` have distinct meanings. Pending/Received is **not final**: the guide says an AUTHORISATION webhook supplies the final result. If the shopper closes the browser and does not return, wait for webhook outcome; AUTHORISATION false/true and OFFER_CLOSED true lead to distinct order actions. See raw lines 373–389, 877–966.
- **TEST/LIVE:** For testing, the guide says to obtain test wallet credentials from Adyen Support and log in to a simulator using the registered phone number and its one-time password. It points to TEST Customer Area for status. Live acceptance requires a GrabPay request in LIVE Customer Area. This is setup guidance, not evidence of an actual provider account, test result or live approval. See raw lines 968–977.

> [!warning] Contradiction
> The requirement table explicitly says **Advanced flow**, but the introduction and closing “See also” point to **Sessions-flow** Android Drop-in guides (raw lines 19, 25 and 981). Treat those links as mismatched navigation for this page's Advanced `/payments` → redirect → `/payments/details` procedure.
>
> The Wallet and PayLater parameter lists say to derive `returnUrl` from `RedirectComponent.getReturnUrl(context)` (raw lines 68 and 400), but the language examples use a generic HTTPS checkout URL (for example raw lines 74–89 and 408–441). The examples do not establish that URL as a working Android return route. The API/library versions in snippets and TEST redirect response are example scopes, not proof of production compatibility or completed payment.

## Detail locators

- Earlier-version title, Advanced prerequisite and country/PayLater table: raw lines 15–42.
- Wallet/PayLater field distinction and server `/payments` instructions: raw lines 44–70 and 391–404.
- Wallet and PayLater language-specific example payloads: raw lines 72–370 and 406–875.
- Action, return/details and variant/result/webhook handling: raw lines 373–389 and 877–966.
- Simulator credentials and live Customer Area gate: raw lines 968–977.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/grabpay/android-drop-in/earlier-versions/2026-09-15|Adyen GrabPay Android Drop-in earlier-versions snapshot]]
