---
title: "Adyen API-only raw-card integration (historical guide)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/raw-card-data"
raw_files:
  - "adyen/docs/payment-methods/cards/raw-card-data/2026-09-15.md"
tags: [adyen, cards, api-only, raw-card-data, pci, online-payments, historical]
---

## Overview

This [[adyen]] guide, last modified **2022-08-09** and captured 2026-09-15, describes an **API-only card integration with a merchant-built UI that collects raw card data**. The stated gate is **full PCI compliance**; merchants without it are directed to pre-built UI or a custom encrypted-card integration (raw lines 15–21). It requires an API-only integration and adding intended cards in the **test Customer Area** before following the examples (raw lines 23–28). This is a historical guide in [[adyen-online-payments]], not evidence that a merchant is compliant, enabled for LIVE, or has safely handled card data.

## Key takeaways

- The form table lists card number, expiry month/year, security code and cardholder name as required in this guide (raw lines 30–40). The server-side **/payments** section uses raw **scheme** card fields and has an optional co-badged brand and a mobile-native-3DS2 SDK-version field qualified by its trigger (raw lines 308–321). The many request examples are test-environment illustrations, not complete or verified safe production implementations.
- For a card with two identified brands **that the merchant supports**, the shopper must choose the brand; if the merchant supports only one, the page says to let the shopper use that one (raw lines 42–48, 306). The **/cardDetails** guide uses at least eight PAN digits; it says full PAN gives the best result, and omitting **supportedBrands** makes Adyen assume all card brands are supported (raw lines 46–57). These claims are source-bound and do not establish any account's actual brands or present regional legal obligations.
- The **/payments** response has a **resultCode** and the page says a payment outcome also arrives asynchronously in a webhook (raw lines 669–703). Its listed card result codes are **Authorised, Cancelled, Error and Refused**; Error/Refused direct readers to **refusalReason**, manual capture still needs a separate capture after Authorised, and 3DS may produce additional result codes (raw lines 694–703). A sample **Authorised** response is illustrative, not an executed authorization, capture or settlement.
- Optional separate debit/credit presentation requires **Checkout API v53+** and uses **splitCardFundingSources** in **/paymentMethods** and **paymentMethod.fundingSource** in **/payments** (raw lines 705–810). The Netherlands/EUR example is not general availability proof. The Brazil 3DS/automatic-capture statement is a recommendation; the Sweden debit-first statement is dated provider guidance (raw lines 810–816).
- Cards are described as supporting tokenization for **one-click, subscription and unscheduled card-on-file** payments. The page **strongly recommends** explicit shopper permission for future recurring charges, rather than stating that permission is a new schema field (raw lines 818–828). It shows shopperReference-based stored-card retrieval and a CVC prompt, then example token payment models (raw lines 1223–1256, 1258–2339). Creating a token or presenting its example ID is not proof of consent, storage or a later charge.
- **Example conflict:** the “one click” token-creation example uses **UnscheduledCardOnFile** and represents **storePaymentMethod** as a string in curl/Node/Python while other language examples use a boolean (raw lines 830–855, 1010–1039, 1101–1135, 861–904). The unscheduled-payment narrative links to a **subscription** anchor (raw lines 1980–1984). Do not copy these mismatched examples as a validated token flow.
- Before LIVE use, this page says to test with test cards, add accepted cards in the live Customer Area, **assess PCI DSS compliance and submit SAQ D** (raw lines 2341–2349). That is this 2022-modified raw-card guide's stated gate, not proof of completed assessment or a current universal PCI classification.

## Detail locators

- Identity, full-PCI alternative and initial API-only/test setup: raw lines 15–28.
- Required form fields and co-badged **/cardDetails** decision, parameters and examples: raw lines 30–306; note optional **countryCode** row combines shopper-country and terminal-location wording at raw line 56.
- Server **/payments** shape, mixed-version language examples and sample response: raw lines 308–688.
- ResultCode/webhook, manual capture and 3DS additional-result boundaries: raw lines 690–703.
- Debit/credit split version, fields and regional notes: raw lines 705–816.
- Tokenization advice, creation examples, stored-card display and later payment examples: raw lines 818–2339.
- Test and LIVE checklist with SAQ D statement: raw lines 2341–2349.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-pci-dss-compliance]]
- [[adyen-tokenization]]
- [[adyen-3d-secure]]
- [[co-badged-cards]]
- [[source-adyen-docs-payment-methods-cards]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/raw-card-data/2026-09-15|Full pinned raw-card API-only guide]]
