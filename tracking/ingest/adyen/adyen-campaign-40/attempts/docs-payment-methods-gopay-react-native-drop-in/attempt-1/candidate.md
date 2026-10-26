---
title: "Adyen GoPay React Native Drop-in integration guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gopay/react-native-drop-in/2026-09-15.md"
tags: [adyen, gopay, react-native, drop-in, redirect, tokenization, recurring]
---

## Overview

This 2026-09-15 Adyen guide adds GoPay to an existing React Native Drop-in integration, with separate Sessions and Advanced server-side flows. It covers redirect prerequisites, flow-specific request fields, and tokenized Subscription versus CardOnFile payments. It is a method add-on, not a complete base integration. The captured guide does not prove current merchant eligibility, a settled payment, token creation or a completed recurring charge. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- Sessions requires an existing React Native Drop-in Sessions flow, Checkout API v68 or later, redirect handling for `action.type: redirect`, and GoPay added in Customer Area. Its `/sessions` table marks `shopperInteractionDevice` and `channel` as required additions. The prerequisite text says Sessions but links to an Advanced-flow URL; the session-creation and redirect links do target Sessions. No GoPay-specific Drop-in configuration is stated. The TEST `/v71/sessions` snippet has `shopperInteractionDevice` as malformed quoted object text and `channel: React-native`, while the table gives Web/Android/iOS examples; do not treat the sample as a validated schema or proof of channel support.
- Advanced requires an existing React Native Drop-in Advanced flow, redirect handling and Customer Area setup. Its `/payments` table marks `paymentMethod.type: gopay_wallet`, `browserInfo` and applicable `channel` as required additions. The TEST `/v72/payments` response shows `RedirectShopper` with `action.type: redirect`, an intermediate shopper handoff. The example represents `browserInfo` as malformed quoted object text and uses lowercase `channel: web` despite the table's Web/Android/iOS examples; it is not a validated React Native request. No extra GoPay-specific Drop-in configuration is stated.
- The guide says GoPay can create a token on an initial `/payments` request with `storePaymentMethod: true`, a shopper-unique `shopperReference` of at least three characters, and `recurringProcessingModel`. After the payment has **settled**, a `recurring.token.created` webhook carries `storedPaymentMethodId`, shopper reference and initial-payment PSP reference; the merchant server must receive recurring-token lifecycle webhooks. This `/payments` token step is distinct from the normal Sessions `/sessions` add-on and token creation is not established merely by sending the request.
- Subsequent `Subscription` `/payments` calls use the stored method ID, shopper reference, `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription`; the response's `resultCode` is for display and the page identifies a later `AUTHORISATION` webhook as final payment status. The Subscription examples leave currency, payment-method type and return URL blank and include old TEST API/library snippets; they are not copy-ready requests or evidence of successful charges.
- Subsequent `CardOnFile` use is a different challenge flow: GoPay requires redirecting the shopper to enter a PIN. Send stored method ID, shopper reference, `ContAuth` and `CardOnFile`; `RedirectShopper` and a URL are intermediate, followed by `/payments/details` with `redirectResult` after the shopper returns, then the `AUTHORISATION` webhook for final status. Shopper PIN entry and returned details do not alone prove authorization, capture or settlement.
- For testing, contact Adyen Support; before LIVE acceptance, submit a GoPay request in the live Customer Area. The page's TEST examples and Support link do not establish test-account readiness or live enablement.

## Detail locators

- Sessions prerequisites, required-added field table, malformed example and no-extra-configuration statement: pinned raw lines 25–79.
- Initial token conditions and settlement-gated recurring webhook: pinned raw lines 81–102 and 443–464.
- Subscription request fields, incomplete examples and webhook-outcome boundary: pinned raw lines 104–327 and 466–689.
- CardOnFile PIN challenge, redirect/details/webhook sequence: pinned raw lines 329–354 and 691–716.
- Advanced prerequisites, required-added field table, malformed TEST request and redirect response: pinned raw lines 364–441.
- TEST Support and LIVE Customer Area gates: pinned raw lines 356–362 and 718–724.

## Related

- [[adyen-online-payments]] — main provider concept and redirect/payment-state context
- [[adyen-tokenization]] — provider token and recurring lifecycle
- [[source-adyen-docs-payment-methods-gopay]] — method overview and separate eligibility/feature scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/react-native-drop-in/2026-09-15|GoPay React Native Drop-in guide, 2026-09-15]]
