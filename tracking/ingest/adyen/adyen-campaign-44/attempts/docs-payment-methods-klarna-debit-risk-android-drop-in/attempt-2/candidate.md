---
title: "Adyen Klarna Debit Risk Android Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna-debit-risk/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/klarna-debit-risk/android-drop-in/2026-09-15.md"
tags: [adyen, klarna-debit-risk, android, drop-in, sepa-direct-debit, recurring]
---

## Overview

This 2026-09-15 Adyen Docs guide adds Klarna Debit Risk to an existing Android Drop-in integration using Sessions or Advanced flow. It provides method-specific additions and a recurring-token route through SEPA Direct Debit; the base Drop-in implementation and payment outcomes remain outside this page. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The Sessions branch requires an existing Android Drop-in Sessions integration with Checkout API v68 or later and Klarna Debit Risk added in Customer Area. The Advanced branch requires an existing Android Drop-in Advanced integration, redirect handling for `action.type: redirect`, and Customer Area setup. Neither branch adds ordinary method-specific `/sessions` or `/payments` request fields or Drop-in configuration parameters; those statements presuppose the linked base integration.
- Recurring transactions are supported **through SEPA Direct Debit**. To create a token, the `/payments` table calls for `paymentMethod.type: directEbanking`, `returnUrl`, `countryCode`, `recurringProcessingModel`, `shopperInteraction`, non-PII `shopperReference` (at least three case-sensitive characters), and `storePaymentMethod: true`; email, phone and locale are optional in that table. The guide strongly recommends explicit shopper permission and clear schedule/amount disclosure to reduce SEPA chargebacks. It discourages SEPA CardOnFile because of chargeback risk and recommends shopper-present individual Debit Risk authorization instead.
- A `recurring.token.created` webhook returns `storedPaymentMethodId`. Later token payments are limited by this guide to shopper-absent `Subscription` or `UnscheduledCardOnFile` scenarios; their `/payments` examples use `paymentMethod.type: sepadirectdebit`, the token ID, the shopper reference, `shopperInteraction: ContAuth` and the relevant recurring model. This method transition is material: a future token charge is not presented as another Debit Risk redirect payment.
- Both initial-token tables mark `countryCode` required so the shopper can proceed in Klarna, but every initial-token example omits it. The tables describe online `shopperInteraction` as `Ecommerce`, while the initial-token examples set `ContAuth`. The curl/Node/Python/Ruby examples also serialize `storePaymentMethod` as a string, whereas the tables say to set it to true and typed examples use a boolean. Verify the intended initial-token request against the applicable API before copying these examples. These mismatches do not establish whether the API rejects the examples.
- The guide says to test with Klarna sample data and inspect test payments in Customer Area before live acceptance, then enable Klarna Debit Risk on the live merchant account. A TEST example or this checklist does not establish live availability or a completed payment.

## Detail locators

- Sessions prerequisite and no-extra-parameter/configuration statements: pinned raw lines 25–46. Advanced prerequisite and no-extra statements: lines 1059–1079.
- SEPA recurring purpose, permission advice and initial-token table: lines 48–79 and 1081–1112. Both tables require `countryCode` at lines 71/1104, but initial-token examples omit it (for example lines 85–104 and 1118–1137); their `Ecommerce` prose also conflicts with `ContAuth` examples at lines 102/1135.
- `recurring.token.created`, shopper-absent restriction and SEPA subscription/unscheduled examples: lines 429–1047 and 1462–2080.
- Test/live setup: lines 1049–1057 and 2082–2088.

## Related

- [[adyen-online-payments]] — main provider payment integration concept
- [[source-adyen-docs-payment-methods-klarna-debit-risk]] — method overview and non-settlement risk

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna-debit-risk/android-drop-in/2026-09-15|Klarna Debit Risk Android Drop-in guide, captured 2026-09-15]]
