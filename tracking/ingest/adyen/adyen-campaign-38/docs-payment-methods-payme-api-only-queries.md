# Retrieval checks — PayMe API-only

Q1. What is the source's purpose and scope, and what cannot be inferred? `source-adyen-docs-payment-methods-payme-api-only` describes PayMe API-only merchant Web form with desktop QR and mobile app redirect, using HK/HKD discovery and method `payme`. QR display, scan, app redirect/return, TEST examples and sandbox results do not prove current merchant eligibility, authorization, capture or settlement. Raw lines 15–58, 147–175, 177–183, 312–342.

Q2. What central capability, prerequisites and warnings matter? Existing API-only integration, test Customer Area setup and Checkout API v67+ are stated; `lineItems.sku` is optional and v70+ only. Desktop QR action is `Pending` and webhook-led; mobile action is `RedirectShopper`, with `action.url`, decoded `redirectResult` to `/payments/details`, and AUTHORISATION webhook for unresolved/no-return cases. Mobile prose uses `returnURL` but samples use `returnUrl`; Node mobile `channel: Web/iOS/Android` differs from cURL `Web`. The sandbox table says PayMe defaults to ten-minute expiry and simulates `OfferCancelled` by amount ending. Raw lines 19–46, 66–76, 147–175, 177–310, 312–342.

Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-payme-api-only]] → [[raw/adyen/docs/payment-methods/payme/api-only/2026-09-15]].
