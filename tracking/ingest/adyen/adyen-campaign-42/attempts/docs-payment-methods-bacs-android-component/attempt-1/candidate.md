---
title: "BACS Direct Debit Android Component | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/android-component"
raw_files:
  - "adyen/docs/payment-methods/bacs/android-component/2026-09-15.md"
tags: [adyen, bacs, direct-debit, android, components, recurring]
---

## Overview

This 2026-09-15 Adyen guide adds BACS Direct Debit to an existing Android Components integration. It separates Sessions and Advanced server-side flows, with Component launch, request fields and tokenized recurring instructions. It is an add-on, not the base Android integration or the full BACS scheme/mandate authority. See the related [[source-adyen-docs-payment-methods-bacs|BACS overview]] for the Direct Debit Instruction (DDI), clearing delay and chargeback context (this raw lines 15–25, 508–516; overview raw lines 23–27, 60–74).

## Key takeaways

- Sessions requires an existing Android Components Sessions integration, Checkout API v68 or later, and BACS addition in Customer Area. It marks `shopperEmail` required on `/sessions`; its examples use GB/GBP and an Android app-scheme return URL. Compose includes `bacs` and `components-compose` modules, while non-Compose includes `bacs`; both create `BacsDirectDebitComponent`. An optional `setSubmitButtonVisible` setting defaults to true (raw lines 25–45, 47–68, 341–439). The curl example omits a continuation before `-d`, so it is not a copy-ready shell command (raw lines 51–68).
- Advanced requires an existing Android Components Advanced integration with additional-action handling and BACS enabled in Customer Area. It uses the same Compose/non-Compose modules, Component and optional submit-button setting, but gets its payment method from `/paymentMethods` rather than a Checkout Session. Its `/payments` table marks `shopperEmail`, `paymentMethod.type: directdebit_GB`, holder name, bank account number and bank routing/sort code `bankLocationId` required (raw lines 508–632). The Advanced curl also lacks a continuation before `-d` (raw lines 638–661).
- For recurring use, the guide recommends tokenization and **strongly recommends** explicit shopper permission and transparent schedule/amount; it does not label that recommendation as the entire DDI rule. It separately says the Direct Debit Guarantee requires advance notice if the collection date or amount changes, and strongly recommends notice before each payment. Initial token creation adds `shopperReference` and `storePaymentMethod: true` to `/payments`; save `storedPaymentMethodId` from `recurring.token.created`. Later recurring `/payments` use the token/reference plus `shopperReference` and `shopperInteraction: ContAuth` (raw lines 441–494, 1008–1061). The related overview states shoppers confirm ownership/agreement and Adyen submits their DDI; clearing and settlement can take four to six days, and BACS chargebacks cannot be defended (overview raw lines 23–27, 60–74).
- Advanced prose says `action.type: Direct`, but its purported successful response example contains `resultCode: Received` and `action.type: voucher` with `PDF_MANDATE_URL`. Treat this as an unresolved prose/example conflict; do not silently replace either value with the other or interpret `Received` as cleared/settled funds. The recurring section explicitly says webhooks track whether a received payment succeeds (raw lines 514–515, 993–1006, 1061; overview raw lines 23–27).
- The page provides TEST account details and asks merchants to check test payment status in Customer Area. It says a separate request in the **live** Customer Area is needed before live BACS acceptance. The historical examples and labels do not prove current availability, live enablement, successful debit or valid DDI (raw lines 496–506, 1063–1073).

## Detail locators

- Sessions prerequisites, `shopperEmail` and example request: raw lines 25–68.
- Sessions Compose/non-Compose imports, configuration and launch: raw lines 341–439.
- First recurring/token route, notice language and test/live gate: raw lines 441–506.
- Advanced prerequisites, imports, Component and required `/payments` fields: raw lines 508–632.
- Advanced request examples, conflicting response and recurring/token route: raw lines 634–1061.
- Advanced TEST details and live gate: raw lines 1063–1073.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-bacs|BACS overview (DDI, clearing and chargeback context)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/android-component/2026-09-15|BACS Direct Debit Android Component, fetched 2026-09-15]]
