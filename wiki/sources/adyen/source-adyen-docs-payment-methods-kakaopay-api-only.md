---
title: "Adyen KakaoPay API-only integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/kakaopay/api-only"
raw_files:
  - "adyen/docs/payment-methods/kakaopay/api-only/2026-09-15.md"
tags: [adyen, kakaopay, api-only, korea, recurring]
---

## Overview

This 2026-09-15 KakaoPay guide adds method-specific instructions to an existing **API-only Advanced Web integration**. It requires `action.type: redirect` handling and KakaoPay setup in Adyen Customer Area. The first-payment route and the optional recurring/token route have different fields and lifecycle gates. A listed method, redirect, token request or sample payment does not establish current merchant eligibility, final authorization, capture or settlement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- For `/paymentMethods` discovery, the guide specifies `countryCode: KR` and `amount.currency: KRW`; its illustrative response has type `kakaopay`. The API-only payment form need not collect additional shopper information. In the **ordinary first-payment** path, the page says no further KakaoPay-specific `/payments` parameters are needed and relies on the pre-existing redirect flow. Its 'How it works' list conditionally mentions extra item information, but the following `/payments` section provides no item fields or request example; do not infer a complete item-data schema or omit base payment fields.
- For a **recurring token**, the initial `/payments` request adds `storePaymentMethod: true` and a unique `shopperReference`. The shopper logs into Kakao and confirms the recurring transaction. Only **when the initial payment has settled** does the guide say `recurring.token.created` arrives with `shopperReference`, initial-payment `pspReference` as `eventId`, and `storedPaymentMethodId`; the merchant server must receive the token-lifecycle webhook. The page does not describe a separate consent-screen implementation, guarantee settlement or promise a token immediately on redirect/authorization.
- A later server `/payments` token charge uses `paymentMethod.storedPaymentMethodId` (also discoverable via `/listRecurringDetails`), the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` otherwise. Code samples include `paymentMethod.type: kakaopay`, amount, reference and merchant account. This is a request recipe, not proof of approval or settled funds; the base integration remains responsible for response and final-status handling.
- The examples use Adyen Checkout TEST **v72** for `/paymentMethods` and TEST **v68** for a recurring `/payments` curl request, with older language-library examples. The Java recurring amount is 15000 while curl and other examples show 1000; those values illustrate requests, not a uniform amount requirement. No explicit current minimum version or cross-version compatibility is established.
- The Test and go live section awkwardly says 'test successful KakaoPay live payments' using a real KakaoPay-registered mobile number, then directs test status checks to TEST Customer Area; it separately requires a request in **live** Customer Area before live acceptance. Preserve that TEST/LIVE wording conflict instead of treating it as a safe test method or proven live payment. No real account or payment test was performed.

## Detail locators

- API-only/redirect/Customer Area prerequisites, flow and form: raw lines 19–42. KR/KRW discovery, TEST v72 example and `kakaopay` response: raw lines 44–83. Base no-extra-fields sentence versus conditional item-information sentence: raw lines 31–36 and 85–87.
- Initial token request, shopper confirmation and **post-settlement** token-created webhook fields: raw lines 89–112. Later token request and recurring-model fields: raw lines 114–126; TEST v68 curl and versioned language examples: raw lines 128–325. Ambiguous testing and separate live Customer Area gate: raw lines 327–335.

## Related

- [[adyen-online-payments]] — main payment-flow context.
- [[adyen-tokenization]] — stored payment method and token lifecycle context.
- [[source-adyen-docs-payment-methods-kakaopay]] — separately captured KakaoPay overview; route/capability descriptions do not prove this merchant's enablement.

## Raw Sources

- [[raw/adyen/docs/payment-methods/kakaopay/api-only/2026-09-15|KakaoPay API-only guide, captured 2026-09-15]]
