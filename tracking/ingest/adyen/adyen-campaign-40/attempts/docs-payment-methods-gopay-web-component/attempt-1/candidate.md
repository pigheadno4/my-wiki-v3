---
title: "GoPay Web Component | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/web-component"
raw_files:
  - "adyen/docs/payment-methods/gopay/web-component/2026-09-15.md"
tags: [adyen, gopay, web, components, redirect, tokenization, recurring]
---

## Overview

This [[adyen]] guide adds GoPay to an existing Web Components integration through either Sessions or Advanced server-side flow. Both paths use the Web `Redirect` Component for `gopay_wallet` and require redirect handling. The page also describes token creation and distinct later Subscription and CardOnFile requests; the token is reported only after the initial payment settles. See [[adyen-online-payments]] and [[adyen-tokenization]]. This dated page does not establish current merchant eligibility, a completed payment, or a token actually issued.

## Key takeaways

- **Sessions:** Requires an existing Web Components Sessions integration, Checkout API v68 or later, `action.type: redirect` handling, and GoPay added in Customer Area. Its `/sessions` table marks `shopperInteractionDevice` and a relevant `channel` as required; the example uses `IDR` and `countryCode: ID`, which are example context rather than this page's eligibility matrix. It imports `Redirect`, says no extra GoPay Component configuration is needed, and constructs the Component for `gopay_wallet`. See raw lines 25–103.
- **Advanced:** Requires an existing Web Components Advanced integration, redirect handling, and Customer Area setup. It imports the same `Redirect` class. The `/payments` table marks `paymentMethod.type: gopay_wallet`, `browserInfo`, and a relevant `channel` as required. Its illustrative response has `RedirectShopper` and `action.type: redirect`, an intermediate handoff rather than final payment authorization. No Advanced Checkout API minimum or Web SDK version is stated here. See raw lines 388–481.
- **Create token after an initial payment:** The recurring section says GoPay supports token payments and calls for `storePaymentMethod: true`, a unique `shopperReference` of at least three characters, and `recurringProcessingModel` in a `/payments` request, plus a server able to receive recurring-token lifecycle webhooks. After the initial payment **settles**, a `recurring.token.created` webhook supplies `storedPaymentMethodId` for that shopper. The method page does not describe token issuance at redirect, initial authorization, or every attempted payment. See raw lines 105–126 and 483–504.
- **Later payment models differ:** For `Subscription`, the page lists the stored method ID, shopper reference, `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription` on `/payments`, then describes a shopper-facing `resultCode` and later `AUTHORISATION` webhook as final status. For `CardOnFile`, it also lists `ContAuth` in the request but explicitly requires a GoPay redirect so the shopper enters a PIN, followed by `/payments/details` with `redirectResult` and a later final-status `AUTHORISATION` webhook. Preserve that shopper challenge even though the sample request says `ContAuth`. See raw lines 128–140, 345–378 and 506–756.
- **Test and live:** The guide directs merchants to Adyen Support and GoPay's knowledge base for testing. It says a separate GoPay request in the live Customer Area is needed before live acceptance. These are setup instructions, not test or live outcome evidence. See raw lines 380–386 and 758–764.

> [!warning] Incomplete or malformed snippets
> The Sessions curl block lacks a continuation after `-X POST` and renders `shopperInteractionDevice` as a quoted, nested JSON-like string; the Advanced curl block likewise lacks a continuation and renders `browserInfo` as a quoted nested object. Both `Redirect` snippets show `type:gopay_wallet` as an unquoted identifier. Subscription request examples leave currency, payment method type and return URL blank. These snippets are not copy-ready working requests or evidence that the sample payment/token succeeded. See raw lines 49–73, 99–103, 142–343, 416–465 and 520–721.

## Detail locators

- Sessions prerequisites, required fields, import and Component initialization: raw lines 25–103; Advanced equivalents: raw lines 388–481.
- Token request fields and post-settlement webhook: raw lines 105–126 and 483–504.
- Subscription fields/examples and webhook boundary: raw lines 128–351 and 506–729; CardOnFile PIN redirect, details request and webhook: raw lines 353–378 and 731–756.
- Testing and live request: raw lines 380–386 and 758–764. This page contains no complete country/currency eligibility matrix.

## Related

- [[adyen-tokenization]] — stored-payment-method lifecycle and merchant-server boundaries.
- [[adyen-webhooks]] — final outcome and recurring-token event context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/web-component/2026-09-15|GoPay Web Component, 2026-09-15 snapshot]]
