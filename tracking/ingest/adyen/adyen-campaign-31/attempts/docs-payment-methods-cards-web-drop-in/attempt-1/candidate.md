---
title: "Adyen Cards Web Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/cards/web-drop-in/2026-09-15.md"
tags: [adyen, cards, web-drop-in, online-payments, tokenization]
---

## Overview

This [[adyen]] guide, last modified 2023-05-26 and captured 2026-09-15, explains adding cards to an **existing** Web Drop-in integration. It branches on the merchant server's Sessions or Advanced flow and covers optional client card configuration, separate debit/credit display, card-brand recognition, and card token creation/reuse. Route through [[adyen-online-payments]]; token handling also relates to [[adyen-tokenization]]. The page's test requests and UI events are instructions and examples, not proof of merchant enablement, 3D Secure completion, authorization, capture or settlement.

## Key takeaways

- **Prerequisites and scope:** first build the matching Sessions or Advanced Web Drop-in integration and add cards in Customer Area. The guide says ordinary card use needs no extra card-specific API fields; use `/sessions` for the Sessions route (default for Drop-in v5.0.0 or later) and `/payments` for Advanced/additional use cases. Its v6 resource import is specifically for Web Drop-in v6. See raw lines 21–54.
- **Client configuration and events:** card configuration is optional and sits under `paymentMethodsConfiguration.card`. The property table has individual Web-version gates, defaults and conditions, such as `holderNameRequired` needing `hasHolderName`, partial billing address requiring `billingAddressRequired`, and address-lookup callbacks needing an external address API and full required billing address. `onSubmit` means valid form data after Pay; `onError` is for client validation and, since v5.0.0, can return objects for every component. Neither callback is payment authorization. See raw lines 56–281, especially 105–161.
- **Display features:** separate debit/credit forms use `splitCardFundingSources: true` in a Sessions `/sessions` request or an Advanced `/paymentMethods` request. Drop-in attempts brand recognition while details are entered; the co-badged section says supported brands are shown for shopper choice under applicable regional rules. This page does not determine a merchant's supported card brands or regional compliance. See raw lines 283–307.
- **Stored cards:** the page supports one-click, subscription and unscheduled card-on-file routes and **strongly recommends** explicit shopper permission for future recurring payments. Sessions token examples use `/sessions`; Advanced uses `/payments` and says to show the storage checkbox with `enableStoreDetails: true`. It says token creation yields a `recurring.token.created` webhook, with `storedPaymentMethodId` identified in the Advanced subsection. The Checkout API v69-or-earlier checkbox instruction is separately versioned. Subsequent subscription and unscheduled examples call `/payments` with stored token, `ContAuth`, and the respective recurring model; examples are not completed transactions. See raw lines 309–2473, especially 634–640, 976–985, 1382–1450 and 1810–2150.
- **Example conflicts and test limits:** Sessions token-creation snippets differ between `storePaymentMethodMode: "askForConsent"` and `"enabled"`; Advanced `storePaymentMethod` snippets use booleans and quoted strings, including `"True"`. Treat these as illustration differences, not a single verified consent or request contract. The `test_` encrypted-card values and sample amounts/currencies are test fixtures. For Web v5.20.0 or later, the page says card fields use JSON Web Encryption and the test environment needs a secure context plus allowed origin. Its dated live checklist calls for test-card checks, cards added in live Customer Area, and PCI DSS assessment plus submitted SAQ A; this page cannot certify current PCI eligibility or a live payment. See raw lines 325–631, 991–1376, 2475–2487.

## Detail locators

- Requirement and API flow: raw lines 21–54.
- Optional configuration, version gates, callbacks and external address lookup: raw lines 56–281.
- Funding-source split and brand display: raw lines 283–307.
- Sessions token creation/stored-card/one-click examples: raw lines 309–975.
- Advanced token creation and one-click examples: raw lines 976–1724.
- Subscription and unscheduled card-on-file examples: raw lines 1725–2473.
- Test, secure context and historical live checklist: raw lines 2475–2487.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-pci-dss-compliance]]
- [[adyen-3d-secure]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/web-drop-in/2026-09-15|Cards Web Drop-in guide — collected 2026-09-15]]
