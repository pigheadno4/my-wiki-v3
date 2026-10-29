---
title: "Bancontact Mobile Android Component v4.x.x (earlier versions) | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-mobile/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, bancontact, mobile, android, components, v4, app-switch, tokenization]
---

## Overview

This 2026-09-15-captured page is expressly the **Bancontact Mobile Android Components v4.x.x earlier-versions** guide. It adds Bancontact to an existing Android Components integration and describes an app handoff, Android return intent, server-side `/payments/details` and optional WIP recurring payments. It should not be substituted for a current Android SDK guide or for Bancontact card payments (raw lines 15–29, 395–488, 748–801).

## Key takeaways

- The guide requires an existing Android Components integration and Bancontact enabled in the test Customer Area. Its integration prerequisite links to a Sessions Components guide, while the return-intent `/payments` step links to an Advanced Components guide; this historical page does not establish one consistent Sessions or Advanced base flow (raw lines 28, 442). To receive `bcmcmobile.urlIntent`, enable **3DS2 Additional Fields** in Customer Area. `/paymentMethods` uses BE/EUR and returns `bcmc_mobile`; the form says no shopper information is needed. It shows an optional `BcmcConfiguration` example that makes holder name required, so the optional sample should not erase the no-required-form-data statement or be assumed to apply to the later QR handling automatically (raw lines 24–62).
- The `/payments` request uses `paymentMethod.type: bcmc_mobile` and a Component-derived return URL. The prose spells the request field `returnURL`, while its JSON and library examples use `returnUrl`; do not assume those casings are interchangeable, and verify the API field before implementation (raw lines 66-69, 87, 119). The sample response is `Pending` with `action.type: qrCode`, QR data and `additionalData.bcmcmobile.urlIntent`, and the page says to pass `action` to the client (raw lines 64–69, 372–393). The introductory text calls this a **Redirect Component** guide, but the actual handling section instructs `QRCodeComponent`, `qr-code` module, `QRCodeConfiguration` and `handleAction`; the response JSON is also incomplete at the closing braces. Preserve this source-level Redirect-versus-QR naming/example conflict rather than treating the snippets as validated drop-in code (raw lines 15–19, 378–391, 395–438).
- For the app return, add an `IntentFilter` matching the `adyencheckout` scheme and app host, then pass the return intent to the Component from `onCreate` or `onNewIntent` according to launch mode. The observer produces `actionComponentData`, which the app sends to the server; the server posts `actionComponentData.details` to `/payments/details`. Use its `resultCode` for the shopper display and expect an asynchronous webhook. `Pending`/`Received` means the payment is still awaiting final `AUTHORISATION`, while `Authorised`, `Cancelled`, `Error` and `Refused` have separate actions. A sample `Authorised` response is not proof of real payment success (raw lines 440–488, 719–746).
- Recurring use is conditional on Bancontact **WIP** signup, eligibility, Support enablement and transaction limits. The page strongly recommends explicit permission for future charges. It says the first consent transaction has SCA, later WIP transactions do not, and issuer liability remains with no liability shift for that first transaction. Create a token with `storePaymentMethod: true` and a shopper reference of at least three characters; after settlement, `recurring.token.created` supplies `storedPaymentMethodId`. Later `/payments` use that ID, the same shopper reference, `ContAuth` and `Subscription` or `UnscheduledCardOnFile`. Test recurring configuration needs Support (raw lines 748–805). This does not imply WIP access for all Bancontact merchants.
- The page says Bancontact Mobile has **no test platform** and recommends a EUR 0.01 live penny test; no live test was run here. The same historical page includes test Customer Area and `checkout-test` examples, so those snippets are not evidence of an available full test platform or current live capability (raw lines 29–34, 71–89, 1144–1148).

## Detail locators

- v4.x.x identity, setup, Sessions prerequisite link, BE/EUR discovery and optional Bcmc configuration: raw lines 15–62; Advanced return-intent link at line 442.
- `/payments`, `returnURL` versus `returnUrl` casing, Pending `qrCode` action and Redirect/QRCode naming conflict: raw lines 64–69, 87, 119, 372–438.
- Android return intent and server `/payments/details` handling: raw lines 440–488.
- Result-code/webhook boundary: raw lines 719–746.
- WIP eligibility, first SCA, settled-token lifecycle and later recurring fields: raw lines 748–805.
- No test platform and historical live penny-test recommendation: raw lines 1144–1148.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-bancontact|Bancontact overview (card/mobile distinction)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/android-component/earlier-versions/2026-09-15|Bancontact Mobile Android Component earlier versions, fetched 2026-09-15]]
