---
title: "Adyen payment capture"
type: concept
category: technology
tags: [adyen, online-payments, capture, authorization, webhooks]
---

## Adyen payment capture

Adyen captures online payments automatically without delay by default. For payment methods that support separate capture, a merchant can use delayed automatic capture or manual capture after authorization.

## Manual and partial capture

A manual capture request identifies the authorization and the amount to capture. Its immediate `received` response is asynchronous acknowledgment, so webhook processing is required to determine the outcome. A single partial capture cancels the unclaimed amount; multiple partial captures retain the balance and require separate enablement.

## Outcome boundary

A successful `CAPTURE` webhook means the request was valid and submitted onward, not that rejection is impossible. A rare later `CAPTURE_FAILED` event can report a card-scheme or issuer rejection. Refusal details are operational evidence and must not be exposed to shoppers.

## Related

- [[source-adyen-api-explorer-payment-latest-post-capture]] — 2026-09-15-captured inactive Classic Payment API v68 test-server `/capture` contract for original authorization reference, amount, modification receipt and Checkout migration route; receipt is not final capture outcome.


- [[source-adyen-docs-payment-methods-affirm-web-component]] — Affirm Web Component method-specific capture within 28 days after authorization; capture starts installments, and lesser fulfillment calls for capture then refund of the difference (2026-09-15).


- [[source-adyen-docs-payment-methods-sepa-direct-debit-flutter-drop-in]] — Advanced Flutter Drop-in SEPA guide for delayed/manual capture when auto-capture is off, stated nonexpiring authorization and Support-enabled multiple partial captures (2026-09-15 capture).


- [[source-adyen-docs-payment-methods-pay-by-bank-us-ios-drop-in]] — iOS Drop-in method guide warns that Plaid authorization checks do not hold funds and even immediate ACH capture can fail for insufficient funds (2026-09-15 capture).


- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-capture-failure-reasons]] — Classic capture/refund failure scenarios, Customer Area diagnosis and failure-specific Adyen/merchant retry or new-authorization paths (2026-09-15 snapshot).


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-capture-a-recurring-payment]] — 2026-09-15 inactive Classic API guide to capturing an already authorized recurring payment through `/capture`, with authorization-reference and asynchronous-result boundaries.


- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-capture]] — dated Classic `/capture` guide for payment/capture references, receipt versus webhook outcomes, and partial-capture conditions (2026-09-15 snapshot).


- [[source-adyen-docs-online-payments-capture-failure-reasons]] — Adyen webpage snapshot (2026-09-15) for card-scheme capture/refund failure reasons, refusal fields, and qualified recovery paths

- [[source-adyen-docs-online-payments-capture]] — Adyen webpage snapshot (2026-09-15) for capture modes, request handling, and asynchronous webhook outcomes
- [[adyen]] — provider overview and knowledge status
