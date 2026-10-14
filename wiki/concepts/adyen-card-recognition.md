---
title: "Adyen POS Card Recognition"
type: concept
category: technology
tags: [adyen, point-of-sale, card-recognition, card-acquisition]
---

## Definition

Adyen's dated POS card-recognition overview describes using payment data to check which card a shopper presents for a specific journey. It lists parking entry/exit, a same-card check before unreferenced refund, gift-card detection and tax-free-shopping assessment as examples. The common preparation route is card acquisition, which can provide card and shopper identifiers before a next action without itself making a payment.

## Evidence boundary

This overview does not define the identifiers' field semantics, prove a person's civil identity, establish consent/privacy or tax-refund compliance, or authorize a payment or refund. Use [[source-adyen-docs-point-of-sale-card-acquisition]] for the Terminal API acquisition and follow-up payment/cancellation mechanics. [[adyen-tokenization]] covers stored credentials for later payments, a separate use. The 2020-modified page captured 2026-09-15 does not prove current merchant, card, scheme or regional eligibility.

## Sources

- [[source-adyen-docs-point-of-sale-shopper-recognition-identification]] — 2026-09-15 Terminal API card-alias parking example for arrival/departure CardAcquisition, merchant-record matching, canceled first acquisition and separate referenced payment.


- [[source-adyen-docs-point-of-sale-shopper-recognition-before-refund]] — Adyen same-card precheck before a Terminal API unreferenced refund (2021-modified, 2026-09-15 capture): alias/amount lookup, Refund card acquisition, separate referenced-to-acquisition payment request, and asynchronous refund outcome.


- [[source-adyen-docs-point-of-sale-shopper-recognition-tax-free-shopping]] — 2026-09-15 TFS secure-card-capture guide for Global Blue, consent-gated encrypted-card notification, optional terminal acquisition, Mobile eligibility check, POS-issued form and provider refund boundary.


- [[source-adyen-docs-point-of-sale-shopper-recognition]] — Adyen POS card-recognition use-case overview, last modified 2020-03-27 and captured 2026-09-15, with pre-payment card-acquisition and separate scenario routes.
