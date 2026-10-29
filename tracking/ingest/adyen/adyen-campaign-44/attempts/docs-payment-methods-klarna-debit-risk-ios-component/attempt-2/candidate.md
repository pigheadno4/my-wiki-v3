---
title: "Klarna Debit Risk iOS Component | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna-debit-risk/ios-component"
raw_files:
  - "adyen/docs/payment-methods/klarna-debit-risk/ios-component/2026-09-15.md"
tags: [adyen, klarna-debit-risk, ios, components, sepa-direct-debit]
---

## Overview

This 2026-09-15 guide describes **Klarna Debit Risk** additions to an existing Adyen iOS Components integration, separately for Sessions and Advanced server flows. It is a method-specific add-on, not a full iOS integration guide or the consumer Klarna Pay later/Pay over time/Pay now guide. Both flows require redirect handling (`action.type: redirect`) and adding Klarna Debit Risk in Customer Area. Sessions requires Checkout API v68 or later; the Advanced table does not state that version floor. See [[adyen-online-payments]] and [[adyen]].

## Key takeaways

- The guide says there are no extra Klarna Debit Risk parameters for an ordinary `/sessions` request or Advanced `/payments` request, and no additional method configuration. Its iOS initialization prose and Swift snippets in **both** flows use a `None` class and a `directEbankingConfiguration` variable, although no such configuration is defined in this guide. Treat these as unresolved source placeholders/conflicts and verify the actual Component type/configuration against the applicable iOS SDK before implementation. The Advanced requirement's main-integration link also targets `integration=Drop-in` while its label says iOS Components.
- Recurring Klarna Debit Risk is described as **SEPA Direct Debit tokenization**, not a reusable Klarna financing payment. The guide strongly recommends explicit shopper permission and clear schedule/amount disclosure to reduce SEPA chargeback risk. It advises against SEPA Direct Debit for `CardOnFile` because of chargeback risk and recommends a shopper-present Klarna Debit Risk payment for individual payments.
- To create the token, the recurring section's `/payments` table specifies `paymentMethod.type: directEbanking`, `returnUrl`, `countryCode`, `recurringProcessingModel`, `shopperInteraction`, a non-PII `shopperReference` of at least three case-sensitive characters, and `storePaymentMethod: true`. Email, phone and locale are optional in that table. A later `recurring.token.created` webhook provides `storedPaymentMethodId`; no request example alone proves token creation. The table describes online `shopperInteraction` as `Ecommerce`, but its token-creation code examples use `ContAuth`; retain that discrepancy instead of treating either sample as an unqualified rule. Some JSON examples put boolean-like `storePaymentMethod` values in strings, while typed examples use a boolean.
- Subsequent token payments are limited by the guide to **shopper-absent** `Subscription` and `UnscheduledCardOnFile` scenarios. They use `paymentMethod.type: sepadirectdebit` with the stored ID, matching `shopperReference`, `shopperInteraction: ContAuth` and the selected `recurringProcessingModel`. They are processed as SEPA Direct Debit payments. The example EUR amount and test credentials are fixtures, not country/currency eligibility or live execution evidence.
- Test in the provider's test environment, check test statuses in Customer Area, and enable Klarna Debit Risk on the **live merchant account** before live use. These are setup instructions, not proof of enablement or payment outcome.

## Detail locators

- Sessions prerequisites, no extra ordinary fields/configuration, redirect action and problematic initialization: `## Sessions flow Component`, raw lines 25–73.
- Sessions recurring purpose, permission recommendation, token-creation table and versioned TEST snippets: `## Recurring payments`, lines 75–457. The table's `Ecommerce` wording and code's `ContAuth` differ at lines 103 and 129.
- Shopper-absent token reuse, `sepadirectdebit` Subscription and UnscheduledCardOnFile examples: Sessions lines 458–1074.
- Advanced requirements and duplicate initialization conflict, no extra ordinary `/payments` fields: `## Advanced flow Component`, lines 1084–1131. Its main integration link at line 1092 points to Drop-in despite the Components label.
- Advanced recurring table and examples repeat the Sessions pattern and conflict: lines 1132–2131. Read the exact API-library version and test/live endpoint in the needed language sample; snippets are not proof of SDK behavior.
- Test and live account setup: lines 1076–1082 and 2133–2139.

## Related

- [[adyen-online-payments]] — provider online-payment architecture and lifecycle.
- [[adyen-tokenization]] — token lifecycle context; this page's method-specific route remains authoritative for its claims.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna-debit-risk/ios-component/2026-09-15|2026-09-15 Klarna Debit Risk iOS Components Sessions and Advanced guide]]
