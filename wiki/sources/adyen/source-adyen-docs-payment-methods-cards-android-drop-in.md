---
title: "Adyen Cards with Android Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/cards/android-drop-in/2026-09-15.md"
tags: [adyen, cards, android, drop-in, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds cards to an **existing Android Drop-in** integration. It is labeled for Drop-in **v5.0.0** (released October 2023), with a separate earlier-version guide. Both Sessions and Advanced server-side flows require an existing Drop-in integration at least v5.0.0 and cards added in Customer Area. [[adyen]] [[adyen-android-sdk]]

## Key takeaways

- The page says cards need no additional card-specific `/sessions` or `/payments` request fields or Drop-in configuration for the relevant flow. Optional configuration covers CVC display, cardholder name, supported brands, address fields and installments; address lookup depends on merchant-chosen external address APIs and Drop-in callbacks. This does not replace the underlying flow's server, client and payment-result handling.
- Separate debit and credit forms use `splitCardFundingSources: true` in the server's `/sessions` request for Sessions, or `/paymentMethods` for Advanced (the latter stated as Checkout API v53+). The page gives combo-card examples, Sweden-specific display guidance, brand recognition and co-badged-brand selection. Those examples do not prove current regional or method eligibility.
- For storing cards, the page routes to standard tokenization parameters and recommends explicit shopper permission for future recurring charges. Sessions examples create a card token and describe `recurring.token.created`; Advanced asks for `setShowStorePaymentField(true)` and uses `/payments`, with a later webhook carrying `storedPaymentMethodId`. Subsequent one-click, subscription and unscheduled card-on-file examples use distinct `recurringProcessingModel` values; a token or example request is not proof of authorization, capture or settlement.
- The examples are not one consistent, version-neutral implementation: the Sessions token-creation cURL/Node examples use `storePaymentMethodMode: askForConsent`, whereas Java/PHP/C#/Python/Ruby/TypeScript examples use `enabled`; the page also mixes test Checkout API v70, v71 and v72 and different server-library versions. For Checkout API v69 or earlier it separately points to `enableStoreDetails` for the storage checkbox. Follow the chosen flow and API/SDK version, and check consent behavior against the tokenization guide.
- Before live card payments, the page calls for test payments, adding accepted cards in the live Customer Area, PCI DSS assessment and SAQ A submission. Its SAQ A instruction is documentation guidance for this Drop-in path, not evidence that an individual merchant qualifies or is compliant. The `test_` encrypted-card examples are for test requests, not live card-data handling.

## Detail locators

- Page version, Sessions/Advanced prerequisites, and no-extra-card-fields/configuration statements: [[raw/adyen/docs/payment-methods/cards/android-drop-in/2026-09-15|Android cards Drop-in raw]], lines 15–59.
- Optional configuration, address fields, one/two-request lookup callbacks and snippets (including `sendAdressLookupResult` versus `sendAddressLookupResult` spelling): [[raw/adyen/docs/payment-methods/cards/android-drop-in/2026-09-15|Android cards Drop-in raw]], lines 61–246.
- Debit/credit split, Checkout API v53+ Advanced condition, Sweden/combo-card guidance, brand recognition and co-badging: [[raw/adyen/docs/payment-methods/cards/android-drop-in/2026-09-15|Android cards Drop-in raw]], lines 248–354.
- Recurring overview, explicit-permission recommendation, Sessions token examples, `recurring.token.created` and v69-or-earlier note: [[raw/adyen/docs/payment-methods/cards/android-drop-in/2026-09-15|Android cards Drop-in raw]], lines 356–689.
- Sessions one-click examples and their library versions: [[raw/adyen/docs/payment-methods/cards/android-drop-in/2026-09-15|Android cards Drop-in raw]], lines 691–994.
- Advanced storage request, client switch, encrypted test details, server examples and token webhook: [[raw/adyen/docs/payment-methods/cards/android-drop-in/2026-09-15|Android cards Drop-in raw]], lines 996–1398.
- Advanced one-click, subscription and unscheduled card-on-file examples: [[raw/adyen/docs/payment-methods/cards/android-drop-in/2026-09-15|Android cards Drop-in raw]], lines 1400–2463.
- Installment options and test/live/PCI steps: [[raw/adyen/docs/payment-methods/cards/android-drop-in/2026-09-15|Android cards Drop-in raw]], lines 2465–2499.

## Related

- [[adyen-android-sdk]] — native Drop-in architecture and server boundary.
- [[adyen-tokenization]] — stored-card consent, token lifecycle and later charges.
- [[adyen-pci-dss-compliance]] — integration-specific validation and eligibility qualifications.
- [[adyen-online-payments]] — server/client/webhook architecture and payment-result handling.

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/android-drop-in/2026-09-15|Adyen Cards Android Drop-in guide (2026-09-15 snapshot)]]
