---
title: "GCash Flutter Drop-in integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gcash/flutter-drop-in/2026-09-15.md"
tags: [adyen, gcash, flutter, drop-in, recurring]
---

## Overview

This 2026-09-15 Adyen guide describes adding **GCash** to an existing **Flutter Drop-in** integration. It separates Sessions and Advanced redirect prerequisites, ordinary request/configuration scope, a conditional recurring-token sequence, and TEST/live directions. It documents setup and example calls, not an observed payment, settled token or live acceptance. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions base:** the text requires an existing Sessions-flow Flutter Drop-in integration, **Checkout API v68 or later**, handling `action.type: redirect`, and contacting Adyen Support to add GCash in Customer Area. It says no GCash-specific `/sessions` parameters or Flutter Drop-in configuration are needed for the ordinary flow. The integration-type hyperlink nevertheless points to an **Advanced-flow** URL, while the redirect and session links point to Sessions; follow the flow-specific text and verify the base guide. (raw lines 25–48)
- **Advanced base:** the page requires an existing Advanced-flow Flutter Drop-in, redirect handling, and GCash added in Customer Area. It states no additional GCash-specific configuration or ordinary `/payments` parameters. This section does not state a Checkout API minimum. Unlike the Sessions table's Support-contact direction, its setup row links directly to add-payment-methods; the page does not reconcile those setup paths. (raw lines 298–320)
- **Recurring is a separate conditional path in both sections:** the token-creation `/payments` request includes `storePaymentMethod: true` and a unique `shopperReference` of at least three characters. After the initial payment **has settled**, the page says a `recurring.token.created` webhook carries shopper identity, initial-payment `eventId` and `storedPaymentMethodId`; the merchant server must receive token lifecycle events. Later token payments use `paymentMethod.storedPaymentMethodId`, the original shopper reference, `shopperInteraction: ContAuth`, and `Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed contracts. The base no-extra-parameter wording does not remove these conditional recurring fields. (raw lines 50–87, 322–359)
- **Examples and environments:** the recurring snippets show `gcash`, PHP currency, TEST environments and placeholder merchant/credential/token values; the curl examples use a v68 `/payments` URL, not a stated Advanced API floor. Amounts differ between Java (PHP 15000) and most other samples (PHP 1000). No sample response establishes authorization, capture, settlement or a successful token charge. (raw lines 89–286, 361–558)
- **TEST/LIVE wording:** under “Test and go live,” the page says testing **successful GCash live payments** requires a real GCash-registered mobile number. It also directs readers to a **test** Customer Area payment list and Support for testing issues, then says a request in **live** Customer Area is needed before live acceptance. This mixed wording does not prove a TEST success path, a live approval or a completed charge. (raw lines 288–296, 560–568)

## Detail locators

- Sessions prerequisites, link mismatch and no-extra-configuration statements: raw lines 25–48.
- Sessions token creation, settlement-gated webhook and later-payment fields: raw lines 50–87.
- Sessions multi-language TEST examples and test/live directions: raw lines 89–296.
- Advanced prerequisites, setup difference and base request/configuration statements: raw lines 298–320.
- Advanced recurring fields and examples: raw lines 322–558.
- Advanced test/live wording: raw lines 560–568.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-gcash]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/flutter-drop-in/2026-09-15|Adyen GCash Flutter Drop-in, 2026-09-15 snapshot]]
