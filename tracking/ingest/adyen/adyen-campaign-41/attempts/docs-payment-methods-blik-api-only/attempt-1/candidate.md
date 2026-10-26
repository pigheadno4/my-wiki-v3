---
title: "BLIK for API only | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/blik/api-only"
raw_files:
  - "adyen/docs/payment-methods/blik/api-only/2026-09-15.md"
tags: [adyen, blik, api-only, one-click, tokenization]
---

## Overview

This 2026-09-15 snapshot of an Adyen BLIK API-only add-on covers a merchant-built payment form, BLIK with a shopper-entered six-digit code, and a BLIK One Click consent/token route. It assumes an existing API-only integration, says BLIK works with all Checkout API versions, and requires BLIK to be added in the test Customer Area before testing. Its `/paymentMethods` discovery and `/payments` instructions use PL and PLN (raw lines 17–26, 28–50, 418–441).

## Key takeaways

- For BLIK with code, the form offers BLIK and collects `blikCode`. The merchant requests `/paymentMethods` with `countryCode: PL` and a PLN amount, then sends `paymentMethod.type: blik` and the entered six-digit `paymentMethod.blikCode` in `/payments` (raw lines 28–50). The v68 curl payload and versioned language-library blocks are examples, not a minimum API-version requirement (raw lines 25, 52–360).
- The documented `/payments` response is `Pending` with an `action` for a waiting screen while the shopper completes the payment in the BLIK app. The `AUTHORISATION` webhook's success field supplies the later success or failure outcome; `Pending` is not authorization success. A `Refused` response can occur, for example, with an incorrect code (raw lines 362–404).
- The One Click tab asks `/paymentMethods` for a shopper reference and describes a recognizable issuer label. To request consent for later code-free payments, it lists `shopperReference`, `storePaymentMethod: true`, and `recurringProcessingModel: CardOnFile` on a code-bearing initial `/payments` request. After shopper consent, it says a separately enabled Recurring tokens life cycle webhook of type `recurring.token.created` carries `storedPaymentMethodId`, `eventId`, and `shopperReference` (raw lines 418–441, 509–517). This section does not give a distinct subsequent code-free `/payments` payload.
- The One Click tab has internal tensions: the earlier BLIK-with-code discovery text makes stored BLIK conditional on prior signup, but the One Click text states `storedPaymentMethods.type: blik` unconditionally; the prose names `additionalData.BLIK.APP_LABEL` while the example shows `Blik.APP_LABEL`. Its curl sample omits a comma after `recurringProcessingModel` and quotes `storePaymentMethod` as a string despite the prose's `true`; do not copy that sample as validated JSON (raw lines 43, 426, 450–453, 517–529).
- The code route says to use test code `999000`, meet BLIK guidelines, and test end to end; BLIK must be added in live Customer Area before live acceptance. The One Click live instructions additionally say to seek BLIK certification and enablement (raw lines 406–416, 532–545).

## Detail locators

- API-only prerequisite and test Customer Area setup: raw lines 21–26.
- BLIK-with-code form, discovery, request and versioned examples: raw lines 28–50, 52–360.
- Pending/action response, waiting screen and asynchronous authorization outcome: raw lines 362–404.
- BLIK One Click discovery, consent request, example limitations and token webhook: raw lines 418–529.
- Route-specific test and live gates: raw lines 406–416, 532–545.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/blik/api-only/2026-09-15|BLIK for API only, fetched 2026-09-15]]
