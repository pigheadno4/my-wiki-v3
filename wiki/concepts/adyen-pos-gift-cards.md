---
title: "Adyen POS gift cards"
type: concept
category: technology
tags: [adyen, point-of-sale, gift-cards, terminal-api, stored-value]
---

## Definition

Adyen's dated POS gift-card payment guide uses Terminal API `Payment` messages for an activated gift card with a loaded balance. The merchant must have the method added to its Adyen account and complete provider onboarding. The guide describes two payment flows: request a partial authorization for the whole purchase when balance is unknown, or inquire about the balance first and request no more than the available amount. In either flow, another card payment or cash can cover a remainder. [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api-payment]]

## Payment boundary

The request identifies a `StoredValue` instrument of `GiftCard` type, a gift-card provider, transaction currency and requested amount. For the partial flow, `AllowPartialAuthorisation` is passed in `SaleToAcquirerData`. A response's `Success` means full authorization in this guide; `Partial` means the gift card covered only `PaymentResult.AmountsResp.AuthorizedAmount`. Calculate any remainder from requested minus authorized amount before a subsequent tender, and check the follow-up response. `SaleReferenceID` links partial payments belonging to a merchant order; `ServiceID` is a terminal-scoped unique request identity for 48 hours, not a stated idempotency guarantee.

## Scope and evidence

Provider examples, SVS-only optional `ssc`, scan/swipe/manual-entry parameters, and manual-entry mask behavior are in the source and pinned raw. The page does not state universal brand or PIN rules. Its 2022-modified, 2026-09-15-captured wording and illustrative examples do not prove current provider, method, currency, account or terminal availability, an approved payment, or safe replay of a pending request. Follow method-specific activation, balance, load, refund, void and deactivation evidence separately as those sources are reviewed.

## Sources

- [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api-void]] — Terminal API gift-card load undo guide (2020 last-modified; 2026-09-15 capture) for latest-load/24-hour limit, original POI transaction reference formats, and Reverse/Success response check.


- [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api-query-the-balance]] — 2019-modified, 2026-09-15-captured Terminal API gift-card BalanceInquiry guide for activated-card setup, card-entry fields and response balance/currency before a separate payment.


- [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api-load-a-balance]] — Terminal API gift-card load guide (2019 last-modified; 2026-09-15 capture) for adding value to an activated card and checking the stored-value response.


- [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api-activate]] — 2026-09-15 captured Terminal API `StoredValue` gift-card activation guide, including zero initial balance, entry/security-code scope, and activation response.


- [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api-refund-gift-cards]] — POS gift-card refund guide (2019 last-modified; 2026-09-15 capture) distinguishing referenced reversal and unreferenced refund-to-card request.


- [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api]] — 2026-09-15 captured POS gift-card overview for Terminal API versus Stored Value API, card/PIN entry, mall-card MIDs, and dated provider-by-operation limits.


- [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api-deactivate]] — Terminal API gift-card cashback and Givex-only deactivation guide (2019 last-modified; 2026-09-15 capture), including response and zero-balance checks.


- [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api-payment]] — Terminal API gift-card payment and two-balance-flow guide, captured 2026-09-15.
