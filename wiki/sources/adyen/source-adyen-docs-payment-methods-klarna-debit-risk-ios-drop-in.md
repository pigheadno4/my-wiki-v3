---
title: "Klarna Debit Risk iOS Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna-debit-risk/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/klarna-debit-risk/ios-drop-in/2026-09-15.md"
tags: [adyen, klarna-debit-risk, ios, drop-in, sepa-direct-debit, tokenization]
---

## Overview

This [[adyen|Adyen]] guide, fetched and last-modified on 2026-09-15, describes only the Klarna Debit Risk additions to an existing iOS Drop-in integration. It separates Sessions and Advanced flows, then repeats a method-specific SEPA Direct Debit recurring-token route. This is [[adyen-online-payments]] guidance for Debit Risk, not the separate Klarna financing products; the snapshot does not establish current merchant enablement or successful payment execution. See [[source-adyen-docs-payment-methods-klarna-debit-risk|Klarna Debit Risk overview]] for its country/currency and non-settlement qualifications.

## Key takeaways

- For Sessions, the page requires an existing iOS Drop-in Sessions integration, Checkout API v68 or later, and Klarna Debit Risk added in Customer Area. It says no extra `/sessions` parameters and no Klarna Debit Risk configuration are needed for the base integration. For Advanced, it requires an existing iOS Drop-in Advanced integration, redirect handling for `action.type: redirect`, Customer Area addition, and says no extra `/payments` parameters or method configuration are needed. Those no-extra-parameter statements concern the base flow; the recurring-token section separately lists parameters.
- The guide says recurring Debit Risk transactions run through SEPA Direct Debit. It strongly recommends explicit shopper permission for recurring SEPA payments and transparent schedule/amount information to reduce chargeback risk. It limits tokenized follow-up payments to shopper-absent `Subscription` and `UnscheduledCardOnFile` cases, and recommends against SEPA Direct Debit `CardOnFile` flows because of chargeback risk.
- For token creation, the `/payments` table lists `paymentMethod.type: directEbanking`, `returnUrl`, `countryCode`, `recurringProcessingModel`, `shopperInteraction`, a non-PII `shopperReference` of at least three characters, and `storePaymentMethod: true`. The table describes shopper-present online interaction as `Ecommerce`; email, phone and locale are optional, with locale documented as local language or en-US. The token-created webhook carries `storedPaymentMethodId`; receipt of that event is distinct from a completed future payment.
- Subsequent shopper-absent `/payments` requests use `paymentMethod.type: sepadirectdebit` and the stored ID, with matching shopper reference, `shopperInteraction: ContAuth` and the applicable `Subscription` or `UnscheduledCardOnFile` model. The examples are TEST requests to Checkout API v72; library snippets name their own versions. They do not prove successful debit, settlement or chargeback protection.
- The page instructs testing in the test environment, then enabling Klarna Debit Risk on the live merchant account before live use. It does not give capture, refund or final settlement mechanics here; follow the method overview and relevant lifecycle guides for those boundaries.

> [!warning] Token-creation example conflicts with its parameter table
> The token-creation table marks `countryCode` required and describes online shopper authorization as `shopperInteraction: Ecommerce`, but the example `/payments` requests omit `countryCode` and use `ContAuth`. Several curl/language examples also serialize `storePaymentMethod` as a string although the table says `true`. Reconcile these fields against the applicable Checkout API and tokenization guidance before adapting the example; this page does not resolve the conflict.

## Detail locators

- Scope and Sessions prerequisites, API v68 floor, base request/configuration statements: pinned raw lines 15–46.
- Sessions recurring premise, permission recommendation and token-creation table: lines 50–79. Token-creation examples and webhook ID: lines 81–429; compare table lines 71, 76 and 79 with curl lines 89–104.
- Sessions follow-up shopper-absent limitation and SEPA subscription/unscheduled examples: lines 431–1047; test/live instruction: lines 1049–1057.
- Advanced redirect and setup prerequisites, base request/configuration statements: lines 1059–1081. The recurring premise, token table, examples and webhook repeat at lines 1083–1464; follow-up examples at 1466–2082; test/live instruction at 2084–2092.

## Related

- [[adyen-online-payments]] — main provider integration concept
- [[adyen-tokenization]] — provider token lifecycle concept
- [[source-adyen-docs-payment-methods-klarna-debit-risk]] — method scope and settlement risk
- [[source-adyen-docs-payment-methods-sepa-direct-debit]] — separate SEPA Direct Debit method

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna-debit-risk/ios-drop-in/2026-09-15|Klarna Debit Risk iOS Drop-in guide, fetched 2026-09-15]]
