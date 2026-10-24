---
title: "Adyen GCash API-only guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/api-only"
raw_files:
  - "adyen/docs/payment-methods/gcash/api-only/2026-09-15.md"
tags: [adyen, gcash, api-only, redirect, recurring]
---

## Overview

This 2026-09-15 [[adyen]] guide adds **GCash** to an existing **API-only Advanced-flow** integration. The merchant builds the payment-method UI and handles `action.type: redirect`; the page gives method discovery and a separate recurring-token path. The linked base integration guide supplies the full redirect/return and payment-result flow. This snapshot does not prove current PH/PHP merchant eligibility, a shopper's completed redirect, authorization, capture or settlement. [[adyen-online-payments]] [[adyen-tokenization]]

## Key takeaways

- **Base prerequisites and display:** The guide requires an existing API-only integration, redirect handling, and GCash added in Customer Area. To discover `gcash` in `/paymentMethods`, its table specifies `countryCode: PH`, `amount.currency: PHP`, an amount value, and a `channel` such as Web, iOS or Android; the illustrated response names method type `gcash`. The method appearing in a response is discovery, not payment acceptance or merchant eligibility proof. See raw lines 23–29 and 38–85.
- **Payment form and ordinary request:** The dedicated form section says to include GCash in the available-method list and that no GCash shopper information need be collected in the merchant-built form. The ordinary `/payments` section says no additional GCash-specific parameters are needed; it points to the main API-only guide for making the payment and redirect handling. The page does not provide a complete ordinary `/payments` payload or a final webhook/result contract. See raw lines 31–42 and 87–89.
- **Recurring is a separate server route:** Token creation adds `storePaymentMethod: true` and a unique `shopperReference` of **at least three characters** to `/payments`. The guide says **after the initial payment has settled** a `recurring.token.created` webhook returns `storedPaymentMethodId`; the server must receive recurring-token lifecycle events. Later token payments specify that ID, the shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. The base no-extra-fields sentence does not cover these recurring requests, and a redirect or API response does not itself yield the token. See raw lines 91–126.
- **TEST/LIVE boundary:** The guide says successful **live** GCash testing needs a real mobile number registered to a GCash account, directs test-payment checks to TEST Customer Area, and says to submit a request in LIVE Customer Area before accepting live payments. The mixed “test successful live” language and TEST request examples are not evidence of an operating GCash test or live merchant account. The API-only page does not describe GCash-provider onboarding beyond Customer Area addition and shopper account requirement. See raw lines 128–335.

> [!warning] Contradiction
> The “How it works” sketch says the shopper enters details in a merchant-built form (raw line 34), but the dedicated form section says **no shopper information needs to be collected** for GCash (raw line 40). Do not add GCash-specific fields solely from the sketch. The `/paymentMethods` table says to specify `channel`, while its example request omits it (raw lines 46–53 and 57–72); use the table/main integration for channel applicability rather than treating the example as exhaustive. The curl example also shows `-X POST` without a continuation before `-d` (raw lines 62–63), so it should not be copied literally.
>
> The ordinary `/payments` “no additional parameters” wording (raw line 89) is narrower than the recurring instructions that explicitly add token-creation and token-use fields (raw lines 100–126). Recurring snippets vary in amount (Java uses PHP 15000 while other examples use 1000) and in `returnUrl` presence (raw lines 130–324); none is universal request authority.

## Detail locators

- API-only requirement, redirect and Customer Area setup: raw lines 23–29.
- Form wording, PH/PHP/channel discovery table and example discrepancy: raw lines 31–85.
- Ordinary `/payments` statement and recurring webhook/fields: raw lines 87–126.
- Language-specific recurring TEST examples: raw lines 128–325.
- Test/live wording and live Customer Area request: raw lines 327–335.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-gcash]] — GCash overview for PH/PHP, shopper redirect/expiry and method-level capability context.
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/api-only/2026-09-15|Adyen GCash API-only snapshot]]
