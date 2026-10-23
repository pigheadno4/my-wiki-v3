---
title: "Adyen Android Card Component v4.x.x integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/cards/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, cards, android, component, earlier-versions]
---

## Overview

This historical [[adyen]] guide describes adding cards to an existing Android Card Component **v4.x.x** integration using the Advanced flow. It covers selecting available card methods, client-side collection and server-side `/payments`, result presentation, optional tokenization, and test-to-live prerequisites. It is an earlier-version route, not evidence of current SDK behavior or merchant eligibility. [[adyen-online-payments]]

## Key takeaways

- The stated prerequisites are an existing Advanced-flow Android Components integration, cards added in the Customer Area, and a client key. The app's `/paymentMethods` request supplies `countryCode` and `amount.currency`; it selects `scheme` for available cards and `storedPaymentMethods` for stored-card display. The guide then adds the Card Component dependency, configures the client key in TEST, and attaches the Component view. See raw lines 23–92.
- The Component collects card information and returns `paymentComponentState.data`; the merchant passes that data to its server for a `/payments` request. The prose requires both a valid state **and the shopper proceeding to pay**, but the adjacent observer snippet calls `sendPayment` whenever `isValid` becomes true. The example is therefore not an unambiguous submit trigger. The illustrative v72 curl sample also contains a literal hint-templated `paymentMethod` key; it is not copy-ready JSON. See raw lines 94–103 and 134–167.
- The synchronous `resultCode` is for presenting a shopper result; the payment outcome also arrives asynchronously by webhook. The table distinguishes `Authorised`, `Cancelled`, `Error`, and `Refused`, allows additional 3D Secure results, and says manual capture still requires a capture action after `Authorised`. A sample `Authorised` response is illustrative, not evidence of an actual captured or settled payment. See raw lines 490–524.
- For later token payments, the page describes a shopper-selected storage switch, passing `data.storePaymentMethod` and `shopperReference` in `/payments`, then using a token. Its switch-hiding prose names `showStoredPaymentMethods`, while its neighboring Kotlin snippet calls `.setShowStorePaymentField(false)`; the field name must not be inferred from one alone. The token-payment example uses `storedPaymentMethodId`, `shopperInteraction: ContAuth`, and `recurringProcessingModel: UnscheduledCardOnFile` even though the surrounding section says the shopper proceeds to pay. Keep shopper-present and shopper-not-present uses distinct. See raw lines 526–581 and 856. [[adyen-tokenization]]
- The live checklist calls for test-card validation, enabling cards in the LIVE Customer Area, a LIVE client key, and assessment of PCI DSS compliance with the required SAQ A submission before live card acceptance. These are historical guide prerequisites, not proof that any merchant has met them. See raw lines 858–870.

## Detail locators

- Optional postal-code field configuration and its stated default: raw lines 105–132.
- Server request examples and response fields: raw lines 134–509. The snippets are versioned illustrations and contain templating artifacts.
- The requirement table points to Advanced flow, while the closing “See also” link points to a Sessions-flow Android Components guide: raw lines 23–29 and 872–874. Treat the latter as navigation, not a change to this page's Advanced-flow prerequisite.
- The stored-card section repeats a `/payments` path rather than providing a complete stored-card display procedure; its token example is at raw lines 548–581.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/android-component/earlier-versions/2026-09-15|Adyen Card Component v4.x.x integration snapshot]]
