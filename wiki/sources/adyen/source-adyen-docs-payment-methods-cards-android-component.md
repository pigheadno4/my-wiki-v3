---
title: "Adyen Android Card Component integration (v5.0.0 guide)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/android-component"
raw_files:
  - "adyen/docs/payment-methods/cards/android-component/2026-09-15.md"
tags: [adyen, cards, android, components, online-payments, tokenization]
---

## Overview

This [[adyen]] guide, last modified and captured 2026-09-15, explains adding cards to an existing **Android Components v5.0.0 or later** integration. It separates server-side Sessions and Advanced flows; earlier Component versions have a separate guide. See [[adyen-online-payments]] and [[adyen-tokenization]]. The page is a provider documentation snapshot, not evidence of a particular merchant's live enablement, PCI status, token creation, authorization, capture or settlement. See raw lines 15–39.

## Key takeaways

- Both flows require an existing Android Components integration and cards added in Customer Area. The basic `/sessions` or `/payments` card request and Component configuration need no *card-specific additional* fields; this does not waive the underlying flow's requirements. Optional configuration covers address input/lookup, CVC visibility, holder name, card types, Brazil/Korea-specific fields and installment options. Address lookup callbacks rely on the merchant's chosen external address service; the one- and two-request patterns and Android `stateOrProvince` field are detailed in raw lines 61–269. See raw lines 23–75.
- For separate debit and credit forms, set `splitCardFundingSources: true` on a **server-side** `/sessions` request or, for Advanced flow with Checkout API v53 or later, `/paymentMethods`. The Netherlands request/response examples are illustrative. The guide describes combo-card 3D Secure and automatic capture as **recommendations** because of some issuer restrictions, and says `countryCode: SE` causes debit before credit presentation in Sweden; these statements are not payment outcome or present legal-compliance proof. See raw lines 271–369. It says the Component tries card-brand recognition and, for applicable regions, renders supported co-badged brands for cardholder choice. See raw lines 371–377.
- Cards support tokenization for one-click, subscription and unscheduled card-on-file use. The page **strongly recommends** explicit shopper permission for future recurring payments; that wording is advice, not a stated universal requirement. Sessions token creation is described for Components v5.0.0+, with a special Checkout API v69-or-earlier checkbox route. Advanced flow tells the integrator to show the storage switch and pass the shopper's `data.storePaymentMethod` choice in the payment request. Token creation is associated with `recurring.token.created`; Advanced-flow text says that webhook contains `storedPaymentMethodId`, which can be reused for subsequent requests. See raw lines 379–393, 395–716 and 1019–1052, 1446–1493.
- **Material example conflict:** the Advanced-flow prose says `setShowStorePaymentField(true)` to show the storage switch, but the adjacent Kotlin example uses `setShowStorePaymentField(false)` and comments that it does not show the option. Treat the snippet as contradictory, not proof of the correct UI. See raw lines 1023–1051. The page's test examples include `test_` card values and API-library-specific snippets; they are not a full secure implementation or live credential instructions. One-click, subscription and unscheduled examples differ by recurring model and interaction fields; use the raw and linked tokenization contract for exact versions and conditions. See raw lines 395–2552.
- Before live card payments, the guide directs merchants to test, add cards in the **live** Customer Area, assess PCI DSS compliance and submit its stated SAQ A document. This is a stated checklist, not a determination that any merchant qualifies for SAQ A or has complied. The `test_` prefix is expressly for encrypted **test** card details when the client integration is not ready. See raw lines 2578–2588 and [[adyen-pci-dss-compliance]].

## Detail locators

- **Flow prerequisites, base requests and optional card configuration:** raw lines 21–127.
- **Optional address lookup callbacks, field mapping and back handling:** raw lines 129–269. The two-request prose has a malformed callback name at line 222; its sample uses `onLookupCompletion` at line 251.
- **Debit/credit split, Sweden, brand and co-badged display:** raw lines 271–377.
- **Sessions token examples, v69 exception and one-click examples:** raw lines 379–1017.
- **Advanced storage-switch conflict, token webhook, stored-card display and later payment examples:** raw lines 1019–2552. Examples mix Checkout API v70/v71/v72 and language-library versions; preserve each snippet's own version/environment.
- **Installments and pre-live testing/PCI checklist:** raw lines 2554–2588.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-pci-dss-compliance]]
- [[adyen-3d-secure]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/android-component/2026-09-15|Android Card Component guide — captured 2026-09-15]]
