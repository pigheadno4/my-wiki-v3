---
title: "Payment-linked loyalty program | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/loyalty-program/payment-linked-loyalty"
raw_files:
  - "adyen/docs/unified-commerce/loyalty-program/payment-linked-loyalty/2026-09-15.md"
tags: [adyen, unified-commerce, loyalty, customer-recognition, point-of-sale]
---

## Overview

This Adyen tutorial sketches **payment-linked loyalty across online and in-person stores** so a merchant can use its existing loyalty system without requiring a separate loyalty card or app. It assumes the merchant can already create customer profiles and recognize returning customers across channels, and has its own loyalty system for registration, points and reward eligibility. The guide's examples are dated (last modified 2024-10-01; captured 2026-09-15) and do not demonstrate a live merchant's consent, identity match, payment outcome or loyalty reconciliation. [[adyen]] [[adyen-unified-commerce]] [[adyen-pos-loyalty]]

## Key takeaways

- **Online:** before purchase, the merchant checks shopper-provided contact details against stored `shopperEmail`, queries its loyalty database for membership/reward state, and shows a registration or redemption prompt as appropriate. The example then sends a Checkout API `/payments` request with a separate `shopperReference` and shows `resultCode: Authorised`/`pspReference` before the merchant updates its loyalty record keyed by email. The email, shopper reference, payment PSP reference and loyalty-account record have different roles; the sample is not evidence they are automatically linked or that every response is authorized. See **Online loyalty**, pinned raw lines 30–98.
- **In-person synchronous:** the POS first makes a Terminal API **CardAcquisition** request; its response may carry a card `alias` in `AdditionalResponse`. The merchant uses that alias to query its loyalty database before payment, can ask the shopper on the terminal to register or redeem, and can adjust the transaction value for a chosen reward before a distinct Terminal API payment request. A successful payment response in the example precedes a merchant loyalty-balance update. Card acquisition and terminal input are not financial authorization, and the alias is an identifier for merchant matching here, not raw PAN or a payment token. See pinned raw lines 100–205 and 207–540.
- The terminal registration example asks `GetConfirmation`; only `Input.ConfirmedFlag: true` proceeds to registration. If the merchant lacks the shopper's email, a separate `GetText` request gets `Input.TextInput`; the guide recommends email for cross-channel linking but allows phone or another unique identifier instead. This opt-in is described for **loyalty registration** and does not itself establish marketing permission, retention rules, or broader card-data consent. See pinned raw lines 207–375.
- **In-person asynchronous:** the POS initiates payment, then uses a later `AUTHORISATION` webhook with card `alias` in `additionalData` to update the merchant's loyalty record. The merchant must enable alias return in webhook additional data. This path cannot show real-time points/rewards at the in-store purchase, and the merchant must arrange another registration channel. The sample's `success: true` is illustrative; handle real payment/webhook state before awarding points. See pinned raw lines 100–110 and 542–647.
- **Example boundary:** several snippets are not a validated end-to-end exchange. The `InputRequest` examples use `MessageCategory: Payment` in the header even though their bodies are shopper input, and one displayed `GetConfirmation` response is wrapped as `SaleToPOIRequest`. The synchronous PaymentRequest's `CardAcquisitionReference.TransactionID` differs from the preceding card-acquisition response's `POITransactionID.TransactionID`. Treat those fields as example conflicts; obtain the actual original acquisition identifier and verify the dedicated Terminal API/input contract before implementing. The asynchronous payment response's `AdditionalResponse` example writes `aliasA37317672402294` without an equals sign, while the webhook lists `alias` as a separate key; do not parse that illustrative string literally. See pinned raw lines 138–195, 221–294, 302–371, 476–510 and 592–645.

## Detail locators

- **Requirements** (pinned raw lines 23–28) — existing cross-channel profile/recognition capability and merchant-owned loyalty system.
- **Online loyalty** (pinned raw lines 30–98) — contact-to-`shopperEmail` lookup, loyalty prompt, Checkout `/payments` sample with `shopperReference`, illustrative `Authorised` response and loyalty update.
- **In-person loyalty → Synchronous → Step 1: Recognize customer** (pinned raw lines 100–197) — pre-payment CardAcquisition request, `AdditionalResponse` alias and merchant lookup.
- **Synchronous → Step 2: Request customer input** (pinned raw lines 199–464) — terminal GetConfirmation/GetText prompts, registration and reward choice, plus example-header/response inconsistencies.
- **Synchronous → Step 3: Continue with payment** (pinned raw lines 466–540) — separate Terminal API PaymentRequest, acquisition-reference mismatch, example payment response and loyalty update.
- **In-person loyalty → Asynchronous** (pinned raw lines 542–647) — later webhook path, alias enablement, lack of real-time in-store messaging and illustrative AUTHORISATION payload.

## Related

- [[adyen-unified-commerce]] — primary cross-channel merchant proposition.
- [[adyen-pos-loyalty]] — POS-specific loyalty recognition and terminal interaction route.
- [[adyen-pos-shopper-engagement]] — terminal prompts and inputs, separate from payment authorization.
- [[adyen-terminal-api]] — card-acquisition, input and payment message identities.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/loyalty-program/payment-linked-loyalty/2026-09-15|Payment-linked loyalty tutorial, fetched 2026-09-15]]
