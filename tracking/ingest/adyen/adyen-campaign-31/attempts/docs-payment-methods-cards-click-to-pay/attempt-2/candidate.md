---
title: "Adyen Click to Pay cards"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/click-to-pay"
raw_files:
  - "adyen/docs/payment-methods/cards/click-to-pay/2026-09-15.md"
tags: [adyen, cards, click-to-pay, online-payments]
---

## Overview

Adyen Click to Pay Web integration guide for account-recognized card selection without manual card-detail entry. Card schemes store cardholder data and issue tokens. The page leads with one-off card payments but qualifies recurring support as Mastercard Click to Pay only; regular Card Component or Drop-in is a separate recurring route. The page metadata was last modified 2026-02-04 and this raw was captured 2026-09-15; none of the listed support or benefits proves current account enablement or a payment outcome.

## Key takeaways

- Sessions lists Web Drop-in or Components v5.39.0+ and Checkout API v69+; Advanced also lists API-only with a Custom Card Component. Both tabs call for cards and Click to Pay to be added in Customer Area. Advanced says a separate ClickToPay Component with a Custom Card Component needs Support or Account Manager enablement (raw lines 27–51). However, the standalone Click to Pay Component instructions explicitly call for creating a Session with `shopperEmail` and passing that Session to `AdyenCheckout` (raw lines 161–174). The page does not reconcile this Sessions instruction with the Advanced API-only table; retain both as scoped statements rather than assuming one server flow covers the other.
- Drop-in shows Click to Pay with cards when available; the Card Component embeds it, while a Custom Card Component uses a standalone Click to Pay Component. To suppress Click to Pay, the guide says to add `clicktopay` to `blockedPaymentMethods` on `/sessions` or `/paymentMethods`. The standalone component is separate from manual card-entry UI and requires its provided pay button; Adyen says a custom Click to Pay pay button is unsupported. For Card and standalone Components, mount only when the shopper chooses that option because recognition can trigger an OTP (raw lines 88–192).
- A shopper can be recognized by browser cookie or email. Sessions passes `shopperEmail`, `id` and `sessionData` from the `/sessions` response into `AdyenCheckout`; other integrations add `shopperEmail` to card configuration. The page says a Mastercard shopper without a browser cookie always gets a console HTTP 400 even if the flow continues; this is a narrowly described recognition condition, not permission to disregard other 400 responses or proof of payment success (raw lines 194–239).
- Click to Pay request examples add `srcDigitalCardId` and `srcCorrelationId` and describe automatically sent scheme/storefront IDs in a `configuration` object. Card Component/Sessions examples use `scheme`; a standalone Advanced example says `clicktopay`. The Advanced sample duplicates `paymentMethod` and has malformed JSON, while the Drop-in configuration snippet omits a comma after `merchantDisplayName`. Treat these as illustrations requiring correction and version checks, not executable request shapes. The displayed `Authorised` response is an example, not evidence of authorization, capture or settlement (raw lines 98–122, 241–353).
- Click to Pay testing needs scheme sandbox accounts and their test cards; the guide explicitly excludes Adyen test card numbers for Click to Pay. A payment may or may not require 3D Secure under normal decision-making, and chargebacks/risk settings remain card-payment concerns. Neither the benefits list nor test path establishes a guaranteed authorization rate, security result, fee outcome or live availability (raw lines 53–60, 355–391).

## Detail locators

- Purpose, one-off and Mastercard-only recurring scope: raw lines 15–25.
- Flow/version/Customer Area and Support prerequisites: raw lines 27–51.
- Integration configuration, recognition and custom-button limits: raw lines 88–239.
- Request/response fields and malformed sample boundary: raw lines 241–353.
- Scheme sandbox testing and card-payment follow-up routes: raw lines 355–391.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-network-tokenization]]
- [[adyen-tokenization]]
- [[adyen-3d-secure]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/click-to-pay/2026-09-15|Adyen Click to Pay guide snapshot]]
