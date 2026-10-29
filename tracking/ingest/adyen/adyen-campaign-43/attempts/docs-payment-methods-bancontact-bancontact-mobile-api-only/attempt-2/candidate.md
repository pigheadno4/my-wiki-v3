---
title: "Bancontact Mobile API-only integration | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile/api-only"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-mobile/api-only/2026-09-15.md"
tags: [adyen, bancontact, mobile, api-only, qr-code, app-switch, tokenization]
---

## Overview

This captured Bancontact Mobile guide (fetched 2026-09-15; source `last_modified` 2025-02-04) describes a **Web API-only** merchant-built checkout for payments completed in the shopper's Bancontact Pay app. It separates desktop QR and mobile app-switch paths, then gives optional Bancontact Wallet Initiated Program (WIP) recurring-token steps. This is not a card-data or generic Bancontact integration guide and does not prove current method or WIP eligibility (raw lines 1–25, 48–60, 1013–1032).

## Key takeaways

- The page requires an existing Web API-only integration at minimum version **53** and Bancontact added in the test Customer Area. To receive `bcmcmobile.urlIntent` in the response, enable **3DS2 Additional Fields** under **Developers > Additional data > 3D Secure**. The API-only form need not collect shopper information. If using `/paymentMethods`, request `countryCode: BE` and `amount.currency: EUR`; the method type shown is `bcmc_mobile` (raw lines 21–46). These request parameters are not proof that an account or shopper is enabled.
- For desktop/laptop, show a QR code from `/payments` `action.qrCodeData`; for mobile, provide a button that opens the Bancontact app using `additionalData.bcmcmobile.urlIntent`; tablet can use either or both. The page recommends screen size to choose the presentation. The payment request examples use `paymentMethod.type: bcmc_mobile`. Both desktop and mobile prose bullets spell the return field `returnURL`, while their `/payments` JSON examples use `returnUrl`; verify the Checkout API field before implementing because the source does not reconcile this casing conflict (raw lines 65, 85, 413, 433). The mobile example also contains `action.url` and `action.qrCodeData`, but the prose directs the app switch to `urlIntent`, whose availability depends on the Additional data setting; do not substitute the redirect URL silently (raw lines 28–31, 718–754).
- Both payment-initiation examples show `resultCode: Pending`, and the shopper has **15 minutes** to complete the payment; showing the timer is recommended. Desktop QR completion is reported through `AUTHORISATION` webhooks: `success: false` means do not proceed, `success: true` means proceed. For mobile app return, POST the URL-decoded `redirectResult` in `/payments/details`; its `resultCode` informs the shopper-facing result, with asynchronous webhook outcome also supplied. `Pending`/`Received` after details mean the final result is still unknown and comes through `AUTHORISATION`, not that the order can be fulfilled (raw lines 370–405, 718–754, 985–1011). The mobile `/payments/details` sample `Authorised` is an illustration, not proof of a live authorization (raw lines 990–1001).
- Recurring payments are conditional on Bancontact **WIP** signup, eligibility and Support enablement; WIP provides One-Click Pay and merchant-initiated recurring/subscription billing and applies transaction amount limits. The page says first-transaction consent and SCA precede later no-SCA transactions and describes issuer liability/no liability shift for that initial flow. Explicit shopper permission for future recurring charges is **strongly recommended**. To create a token, set `storePaymentMethod: true` and a shopper reference of at least three characters on `/sessions` or `/payments`; after the initial payment settles, `recurring.token.created` carries `storedPaymentMethodId`. Later WIP `/payments` include that token, shopper reference, `ContAuth` and `Subscription` or `UnscheduledCardOnFile`. Test recurring setup also needs Support (raw lines 1013–1070). WIP conditions do not make ordinary Bancontact Mobile payments automatically recurring-capable for every merchant.
- The page says Bancontact Mobile has **no test platform** and recommends a **EUR 0.01 live penny test**. That recommendation is historical documentation, not authorization to run a live payment. The same guide shows test Customer Area setup and `checkout-test` example requests; preserve this test-example versus no-platform tension and verify any current testing path separately. No actual test or live payment was performed for this source (raw lines 25–31, 71–87, 417–435, 1409–1414).

## Detail locators

- API-only v53, test-area/additional-data setup and BE/EUR method discovery: raw lines 21–46.
- Device-specific QR/app path and desktop request/result/webhook: raw lines 48–65, 370–405.
- Mobile `urlIntent`, 15-minute window, return/details and result codes: raw lines 718–754, 985–1011.
- WIP eligibility, initial SCA, token creation after settlement and recurring token request: raw lines 1013–1070.
- No test platform and historical live penny-test recommendation: raw lines 1409–1414.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/api-only/2026-09-15|Bancontact Mobile API only, fetched 2026-09-15]]
