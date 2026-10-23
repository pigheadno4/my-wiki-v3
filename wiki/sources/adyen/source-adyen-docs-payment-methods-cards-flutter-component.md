---
title: "Adyen Cards in Flutter Components (Sessions and Advanced)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/cards/flutter-component/2026-09-15.md"
tags: [adyen, cards, flutter, components, online-payments, tokenization]
---

## Overview

This [[adyen]] guide adds cards to an **existing Flutter Components integration**. It splits server ownership between Sessions (`/sessions`) and Advanced (`/payments`), with cards added in Customer Area before starting either route. The page says cards need no additional card-specific request fields or mandatory Component configuration on top of those parent flows; optional card controls and tokenization are separate. Its code blocks use test endpoints and versioned examples, not a complete or proven live implementation. See [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- Sessions requires an existing Flutter Components Sessions flow and added cards; Advanced requires its own existing Flutter Components flow and added cards. The page's basic request/configuration statements are scoped to each parent flow. Sessions then initializes/shows the Component; Advanced adds its required callbacks. See raw lines 21–84.
- Optional UI controls include cardholder name, address, CVC, supported card types, storage choice and stored-card CVC. `onBinLookup` requires at least 11 entered digits and returns brands; `onBinValue` returns the first six and requires a client key. Debit/credit splitting is set in server requests (`/sessions` or Advanced `/paymentMethods`, the latter labeled Checkout API v53+); country and amount examples are illustrative. Combo-card 3DS and automatic capture are **strong recommendations**, while the Sweden debit-first statement is the page's dated local-legislation claim. Co-badged display and brand recognition are separately described. See raw lines 59–192.
- For recurring card use, the page lists one-click, subscription and unscheduled card-on-file. It **strongly recommends** explicit shopper permission for future recurring charges, rather than declaring it a universal mandatory field. Sessions storage examples show `storePaymentMethodMode` as both `askForConsent` and `enabled`; do not treat these differing examples as one identical consent behavior. A created token is reported by `recurring.token.created` webhook, which is token evidence, not payment authorization or settlement. Checkout API v69-or-earlier has its own `enableStoreDetails` checkbox route. See raw lines 194–525.
- Advanced storage text names `showStorePaymentField`, while the optional configuration table names `showStorePaymentMethodField`; this captured page does not reconcile those names. Its zero-amount `/payments` examples use `test_` encrypted-card placeholders, `Ecommerce`, `CardOnFile` and storage parameters; they are test examples, not permission to submit raw card data or a guarantee that a token was stored. Advanced stored-card display first uses the same `shopperReference` in `/paymentMethods`; later card-token examples use `storedPaymentMethodId` and distinguish CardOnFile, Subscription and UnscheduledCardOnFile. The one-click examples use `ContAuth` even while labeled one-click; verify the intended shopper-initiated versus subsequent-payment model against the dedicated tokenization guide. See raw lines 832–2308.
- Before live card payments, the guide says to test, add accepted cards in live Customer Area, assess PCI DSS compliance and submit the required Self-Assessment Questionnaire A. These stated gates do not establish actual compliance, merchant enablement, successful 3DS, authorization, capture or settlement. See raw lines 2310–2320.

## Detail locators

- Flow prerequisites and no-additional-card-fields/configuration statements: raw lines 21–84.
- Optional configuration, BIN callbacks, debit/credit split, combo/co-badged behavior: raw lines 59–192.
- Sessions token creation, conflicting consent examples and token webhook: raw lines 194–525; Sessions one-click examples: raw lines 527–830.
- Advanced storage-field mismatch, test-only creation examples, stored-card lookup, CardOnFile/subscription/unscheduled examples: raw lines 832–2308.
- Test-to-live and PCI checklist: raw lines 2310–2320.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/flutter-component/2026-09-15|Cards Flutter Component guide, 2026-09-15 capture]]
