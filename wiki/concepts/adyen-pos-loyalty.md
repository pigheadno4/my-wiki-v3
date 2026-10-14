---
title: "Adyen POS loyalty"
type: concept
category: technology
tags: [adyen, point-of-sale, loyalty, shopper-recognition]
---

## Definition

Adyen's 2026-09-15 POS loyalty overview describes a merchant loyalty pattern in which card-acquisition or payment-response identifiers can be used to recognize a shopper without a physical loyalty card. A merchant may offer a recognized shopper a discount or purchase-history recommendation, or enroll an unrecognized shopper at a payment terminal. The merchant must create and maintain backend customer profiles containing the response data it uses for recognition and any other needed details. [[source-adyen-docs-point-of-sale-loyalty]]

## Evidence boundary

The overview routes to separate guides for request-supplied shopper reference/email and card alias, and for loyalty-account data linked to an NFC wallet pass. It does not say these identifiers are interchangeable, persistent across all channels, raw PAN, network payment tokens, or proof of consent. It does not specify privacy retention, SCA, account permissions, enrollment fields, matching accuracy, benefit application, or a completed payment.

The separately reviewed cross-channel profile guide now documents a merchant-maintained CRM record combining contact details, card alias or PAR, shopper reference and consented saved-method tokens, readable and writable across the merchant's sales channels. It does not establish automatic cross-channel identity matching, raw PAN sharing, token-use permission, retention policy, or a completed payment. [[source-adyen-docs-unified-commerce-loyalty-program-create-profiles]]


## Sources

- [[source-adyen-docs-unified-commerce-loyalty-program]] — 2026-09-15 cross-channel loyalty overview that routes card-alias and merchant-profile recognition to separate implementation guides for online and in-person journeys.


- [[source-adyen-docs-unified-commerce-loyalty-program-recognize-customers]] — 2026-09-15 cross-channel guide's in-store CardAcquisition alias lookup, optional stored shopper reference, new-card ambiguity and follow-on payment.


- [[source-adyen-docs-unified-commerce-loyalty-program-create-profiles]] — Cross-channel merchant-CRM profile guide (2026-09-15 capture) for consent, POS GetText and payment fields, identifier enablement, and alias versus saved-method-token boundaries.


- [[source-adyen-docs-unified-commerce-loyalty-program-payment-linked-loyalty]] — Cross-channel payment-linked loyalty tutorial (2024 last-modified; 2026-09-15 capture) with distinct synchronous POS card-acquisition/terminal-input and asynchronous post-payment webhook routes.


- [[source-adyen-docs-point-of-sale-loyalty-wallet-passes]] — Apple Wallet NFC loyalty-pass guide (2026-09-15 snapshot) for Terminal API payment/redeem flows, card-acquisition handoff, pass-server/key setup and shopper-reference boundaries.


- [[source-adyen-docs-point-of-sale-loyalty-payment-data]] — Adyen 2026-09-15 Terminal API loyalty guide for consented shopper IDs, card alias versus NFC-wallet account reference, pre-payment card acquisition, Estonia ID cards and after-payment webhook updates.


- [[source-adyen-docs-point-of-sale-loyalty]] — 2026-09-15 POS loyalty overview and the two child-guide routes.
