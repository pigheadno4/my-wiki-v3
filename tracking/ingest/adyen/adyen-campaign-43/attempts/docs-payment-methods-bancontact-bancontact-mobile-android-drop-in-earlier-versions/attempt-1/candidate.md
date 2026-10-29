---
title: "Bancontact mobile Android Drop-in v4.x.x integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-mobile/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, bancontact, mobile, android, drop-in, earlier-versions, qr, tokenization]
---

## Overview

This 2026-09-15 page describes **Bancontact mobile Android Drop-in v4.x.x**: a BE/EUR mobile app handoff, server `/payments` and `/payments/details`, intermediate versus final outcomes, and WIP-gated recurring tokens. It is a historical version-specific guide, not Bancontact card behavior, current app coverage or successful live-payment evidence. [[adyen]] [[adyen-online-payments]] [[adyen-android-sdk]]

## Key takeaways

- **Setup/display:** start from an Android Drop-in integration and add Bancontact in **test Customer Area**. To receive `bcmcmobile.urlIntent` in the payment response, enable **3DS2 Additional Fields** in Customer Area's Additional data settings; the setting is described here as a response-field prerequisite, not proof that the wallet flow is a card 3DS challenge. Drop-in uses `/paymentMethods` `countryCode=BE` and `amount.currency=EUR` to show Bancontact. The optional `BcmcConfiguration` sample uses a client key and TEST environment. See raw lines 15–55.
- **Payment/app action:** pass Drop-in's `paymentComponentData.paymentMethod` to the merchant server and send `/payments` with a return URL from `RedirectComponent.getReturnUrl(context)`; examples use `bcmc_mobile` and an Android app-scheme return. The curl has a literal hint-wrapped `paymentMethod` key, so it is not copy-ready JSON. The displayed `/payments` response is `Pending`, with `action.type=qrCode`, `url`, `qrCodeData` and optional `additionalData.bcmcmobile.urlIntent`; despite prose calling this a redirect, do not assume a plain `redirect` action. Pass the action to Drop-in for app handoff. See raw lines 57–86 and 369–390.
- **Completion/outcome:** after shopper return, send Drop-in `actionComponentData.details` to server-side `/payments/details`, then present its `resultCode`. The guide also calls for asynchronous webhook outcome. Its table explicitly treats **Pending/Received as order receipt, waiting for clearing**, with final result in an `AUTHORISATION` webhook; `Authorised`, `Cancelled`, `Error` and `Refused` have separate actions. A sample `Authorised` response is not proof of live success. See raw lines 392–439.
- **Recurring WIP gate:** tokenization is described through **Bancontact Wallet Initiated Program**, requiring signup and Support enablement, with company eligibility and amount limits. It says first transaction has shopper SCA/consent, later WIP transactions need no SCA, and issuer liability remains. To create a token use `storePaymentMethod=true` plus shopper reference; after **settlement** `recurring.token.created` supplies stored ID via lifecycle webhook. Subsequent `/payments` uses `bcmc_mobile`, stored ID, same shopper reference, `ContAuth`, and Subscription or UnscheduledCardOnFile. Support must configure recurring TEST. Do not generalize WIP recurring to every Bancontact merchant. See raw lines 441–498. [[adyen-tokenization]]
- **Testing limit:** the page explicitly says **Bancontact mobile does not have a test platform** and recommends a **live EUR 0.01 penny test**. This is source advice, not authorization to run a financial transaction or evidence that the test succeeded. Earlier examples contain `checkout-test`/`bcmc-test` strings; they do not establish a usable Bancontact mobile test platform in view of the explicit statement. See raw lines 69–87, 377–386 and 837–841.

## Detail locators

- v4 scope, Customer Area response-field setting, BE/EUR display and client config: raw lines 15–55.
- Server request, method/app return and historical language examples: raw lines 57–368.
- `Pending` QR/app-intent action and post-return `/payments/details`: raw lines 369–426.
- Intermediate versus final result table and webhook: raw lines 427–439.
- WIP eligibility, SCA/consent, token lifecycle and recurring request: raw lines 441–836.
- No test platform and live penny-test recommendation: raw lines 837–841.

## Related

- [[adyen-online-payments]] — Bancontact mobile payment route.
- [[adyen-android-sdk]] — historical Drop-in/app handoff context.
- [[adyen-tokenization]] — WIP recurring token path.
- [[source-adyen-docs-payment-methods-bancontact]] — card versus mobile overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/android-drop-in/earlier-versions/2026-09-15|Bancontact mobile Android Drop-in v4.x.x, captured 2026-09-15]]
