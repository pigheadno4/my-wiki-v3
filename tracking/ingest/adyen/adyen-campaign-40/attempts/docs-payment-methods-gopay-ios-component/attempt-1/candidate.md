---
title: "GoPay iOS Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/gopay/ios-component/2026-09-15.md"
tags: [adyen, gopay, ios, components, redirect, recurring, tokenization]
---

## Overview

This 2026-09-15 guide adds GoPay to an existing Adyen iOS Components integration in Sessions or Advanced flow. It uses `InstantPaymentComponent` with method `gopay_wallet`, then describes distinct token creation, `Subscription` and challenged `CardOnFile` recurring paths. These instructions do not prove current merchant eligibility, a completed payment or token issuance. [[adyen]] [[adyen-online-payments]] [[adyen-ios-sdk]] [[adyen-tokenization]]

## Key takeaways

- **Sessions setup:** requires an existing iOS Components Sessions integration, Checkout API v68 or later, `action.type: redirect` handling and GoPay added in Customer Area. Its `/sessions` table marks `shopperInteractionDevice` and `channel` required; the example uses `channel: iOS`, ID/IDR and a custom-scheme return URL. The `shopperInteractionDevice` table link nests it under `applicationInfo`, while the sample renders a top-level string containing JSON-like device data (including Chrome values), so the sample is not a resolved schema recipe. No extra GoPay Component configuration is stated. The snippet selects `.other("gopay_wallet")`, uses `InstantPaymentComponent`, sets the Session delegate and initiates payment. (raw lines 25–101)
- **Advanced setup:** requires an existing iOS Components Advanced integration, redirect handling and Customer Area addition; its Components prerequisite label links to an Advanced **Drop-in** page. The `/payments` table marks `paymentMethod.type: gopay_wallet`, `browserInfo` and `channel` required. Its example uses IDR but has browser information for a Windows Chrome browser and `channel: web` on this iOS page; these are sample values, not iOS defaults. It selects the same method in `InstantPaymentComponent` with the merchant object as delegate. The `RedirectShopper` response is an intermediate redirect action. (raw lines 386–484)
- **Token creation and Subscription:** in both flow sections, the page separately tells the merchant to create a token through `/payments` with `storePaymentMethod: true`, a shopper reference of at least three characters and `recurringProcessingModel`; the merchant server must receive recurring-token lifecycle webhooks. After the initial payment has settled, `recurring.token.created` carries `storedPaymentMethodId` and shopper reference. A later `Subscription` payment uses that stored ID, shopper reference, `ContAuth` and model `Subscription`. The page points to `resultCode` for shopper display and an `AUTHORISATION` webhook for final status. Its language samples leave currency, method type and return URL blank; they are incomplete examples, not executable templates. (raw lines 103–349, 486–732)
- **CardOnFile challenge:** the `CardOnFile` variant also uses the stored ID, shopper reference, `ContAuth` and model `CardOnFile`, but specifically requires redirecting the shopper to GoPay for PIN entry. After return, the merchant calls `/payments/details` with `redirectResult`; final status comes through an `AUTHORISATION` webhook. A `RedirectShopper` response, PIN entry or details response alone is not settlement proof. (raw lines 351–376, 734–759)
- **Environment gate:** the page directs merchants to Adyen Support to test GoPay and requires a separate GoPay request in the live Customer Area before accepting live payments. The instructions report no observed test/live payment in this retained snapshot. (raw lines 378–384, 761–767)

## Detail locators

- Sessions prerequisites, device/channel table and inconsistent example shape: raw lines 29–73; Session Component initialization: raw lines 75–101.
- Advanced prerequisite misroute, required-looking method/browser/channel table, example values and redirect response: raw lines 390–484.
- Recurring token-after-settlement lifecycle, Subscription and incomplete samples: raw lines 103–349 and 486–732.
- CardOnFile PIN redirect, `/payments/details` and final webhook: raw lines 351–376 and 734–759.
- Support test route and live Customer Area request: raw lines 378–384 and 761–767.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-ios-sdk]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-gopay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/ios-component/2026-09-15|GoPay iOS Component guide, 2026-09-15 snapshot]]
