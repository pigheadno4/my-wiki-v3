---
title: "GoPay Flutter Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gopay/flutter-drop-in/2026-09-15.md"
tags: [adyen, gopay, flutter, drop-in, redirect, recurring, tokenization]
---

## Overview

This 2026-09-15 page adds GoPay to an existing Adyen Flutter Drop-in integration with separate Sessions and Advanced server-side instructions. It also describes token creation and distinct `Subscription` and `CardOnFile` recurring paths. The snapshot does not establish current merchant eligibility, an executed payment or token issuance. [[adyen]] [[adyen-online-payments]] [[adyen-tokenization]]

## Key takeaways

- **Sessions:** requires an existing Flutter Drop-in Sessions flow, Checkout API v68 or later, `action.type: redirect` handling and contacting Adyen Support to add GoPay in Customer Area. The `/sessions` table marks `shopperInteractionDevice` and `channel` required. Its sample uses ID/IDR, `channel: Flutter` and a custom-scheme return URL, but renders `shopperInteractionDevice` as a top-level string containing JSON-like device data while the table's reference link nests it under `applicationInfo`; the sample is not a resolved schema recipe. No extra GoPay Drop-in configuration is stated. The **Sessions** prerequisite label links to an **Advanced** Flutter Drop-in URL; its session and redirect links use Sessions. (raw lines 25–79)
- **Advanced:** separately requires an existing Advanced Flutter Drop-in integration, redirect handling and GoPay added in Customer Area. Its `/payments` table marks `paymentMethod.type: gopay_wallet`, `browserInfo` and `channel` required. The example uses IDR but `channel: web`, Windows Chrome browser data and a web return URL on this Flutter page; these example values are not general Flutter defaults. The `RedirectShopper` response is an intermediate redirect action, not a final authorization. No extra GoPay Drop-in configuration is stated. (raw lines 364–441)
- **Token creation and Subscription:** in both sections, token creation is a separate `/payments` instruction with `storePaymentMethod: true`, a shopper reference of at least three characters and `recurringProcessingModel`. The merchant server needs recurring-token lifecycle webhook handling. After the initial payment settles, `recurring.token.created` carries `storedPaymentMethodId` for the shopper. Later `Subscription` requests use that ID, shopper reference, `ContAuth` and model `Subscription`; the page routes final payment status to an `AUTHORISATION` webhook. Its language examples leave currency, payment-method type and return URL blank, so they are incomplete templates. (raw lines 81–327, 443–689)
- **CardOnFile challenge:** later `CardOnFile` requests use the token, shopper reference, `ContAuth` and model `CardOnFile`, and explicitly redirect the shopper to GoPay for PIN entry. After return, the merchant calls `/payments/details` with `redirectResult`; the `AUTHORISATION` webhook supplies final status after processing. PIN entry, `RedirectShopper` and details return are intermediate steps. (raw lines 329–354, 691–716)
- **Environment gates:** the guide directs merchants to contact Adyen Support for GoPay testing, while live acceptance requires a separate request in the live Customer Area. The Sessions setup route says contact Support to add GoPay; the Advanced setup row instead links adding GoPay in Customer Area. These are section-specific instructions. (raw lines 33–36, 356–362, 372–374, 718–724)

## Detail locators

- Sessions prerequisites/link mismatch, device/channel table and sample-shape conflict: raw lines 29–73.
- Advanced prerequisites, fields, web-channel example and redirect response: raw lines 368–441.
- Post-settlement token creation, Subscription and incomplete code examples: raw lines 81–327 and 443–689.
- CardOnFile PIN redirect, `/payments/details` and webhook status: raw lines 329–354 and 691–716.
- Support/test and live Customer Area routes: raw lines 356–362 and 718–724.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-gopay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/flutter-drop-in/2026-09-15|GoPay Flutter Drop-in guide, 2026-09-15 snapshot]]
