---
title: "Adyen cards in Flutter Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/cards/flutter-drop-in/2026-09-15.md"
tags: [adyen, online-payments, cards, flutter, drop-in, tokenization]
---

## Overview

This [[adyen]] page, modified and captured 2026-09-15, adds **cards to an existing Flutter Drop-in integration**. It presents separate **Sessions** and **Advanced** server flows, optional card UI and debit/credit display settings, and card-token examples for one-click, subscription and unscheduled card-on-file use. It is not a standalone Flutter integration guide or evidence that a merchant has cards enabled, is PCI compliant, authorized a payment, captured funds or settled. See [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- **Prerequisites and base path:** Both flow tabs require an existing Flutter Drop-in integration and adding cards in the Customer Area. The card add-on says no card-specific extra fields for base `/sessions` (Sessions) or `/payments` (Advanced) requests and no extra base Drop-in configuration. Advanced then routes to required callbacks in its separate integration guide; this page does not define callback handling or a 3DS result. See raw lines 21–57 and 78–84.
- **Optional card behavior:** The configuration table includes name/address/CVC visibility, supported types, Korean security and social-security-number field visibility, storage UI, and BIN callbacks. `onBinLookup` is described after at least 11 digits and returns brands; `onBinValue` returns the first six digits and cites a client key. These are optional UI/API descriptions, not permission to collect or expose raw card data outside the supported integration. See raw lines 59–76.
- **Debit/credit and brand choice:** To show separate debit and credit forms, the Sessions flow sets `splitCardFundingSources: true` on server `/sessions`; Advanced sets it on `/paymentMethods` and is marked **Checkout API v53 or later**. The NL/EUR 47 examples use test Checkout v70 and v72 respectively; they are examples, not region limits or current API defaults. The guide says to set `countryCode: SE` for its Sweden debit-first presentation and recommends **3D Secure plus automatic capture** for combo-card debit due to some issuer restrictions; the latter is advice, not a universal requirement. It also describes conditional card-brand recognition and supported co-badged brand choice. See raw lines 86–192.
- **Token storage and reuse:** Cards are linked to one-click, subscription and unscheduled card-on-file tokenization. The page **strongly recommends asking explicit shopper permission** for future recurring charges and transparency about schedule/amount. Its Sessions token example uses Checkout test v71, `storePaymentMethodMode: askForConsent`, `shopperReference`, `CardOnFile` and `Ecommerce`; when a token is created, it says a `recurring.token.created` webhook is received. A token-created event is not payment authorization or settlement. The Advanced storage example uses test v72 `/payments`, zero USD amount and `test_` encrypted-card fixtures; later one-click, subscription and unscheduled examples use stored-payment-method IDs. Both one-click example sections show `shopperInteraction: ContAuth` (for example raw lines 537–550 and 1257–1263), while the subscription and unscheduled examples use `ContAuth` with their respective recurring models. These are sample values, not a resolved statement about all shopper-initiated cases. See raw lines 194–229, 519–525, 832–870, 1235–1264, 1596–1624 and 1948–1976.
- **Unresolved storage-setting and consent example differences:** The optional table names `showStorePaymentMethodField` (raw line 70), while Advanced token prose names `showStorePaymentField` (line 838); the page does not reconcile them. The Sessions curl sample uses `askForConsent` (line 227), but Java and other language samples use `enabled` (for example lines 251–260 and 435–449), even while the prose recommends explicit permission. Do not silently treat those spellings or modes as interchangeable. Checkout API v69-or-earlier instructions separately name `enableStoreDetails` (lines 521–525).
- **Test/live and PCI boundary:** The `test_` prefix is described only for testing API requests with encrypted test-card details when the client integration is unfinished. Before live card payments, the page says to test, add accepted cards in the **live** Customer Area, assess PCI DSS compliance and submit the required **Self-Assessment Questionnaire A**. The Advanced curl sample renders `storePaymentMethod` as a string `"true"` while the Java snippet uses boolean `true` (raw lines 866 and 896–905); the page does not reconcile those examples. The code blocks use test endpoints and language-library-specific versions, and do not prove a complete safe live card-data implementation or a payment outcome. See raw lines 2300–2310 and example sections above.

## Detail locators

- **Requirements, server-flow split, base fields and optional configuration:** raw lines 21–84.
- **Split funding sources, v53 gate, Sweden/3DS advice, brand/co-badged UI:** raw lines 86–192.
- **Sessions token creation, language-version examples, webhook and older API route:** raw lines 194–527.
- **Sessions one-click code examples:** raw lines 527–831.
- **Advanced token creation and test encrypted-card snippets:** raw lines 832–1234.
- **Advanced one-click, subscription and unscheduled token examples:** raw lines 1235–2299.
- **Test cards, live method setup and PCI/SAQ A gate:** raw lines 2300–2310.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-pci-dss-compliance]]
- [[source-adyen-docs-payment-methods-cards]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/flutter-drop-in/2026-09-15|Cards Flutter Drop-in guide — captured 2026-09-15]]
