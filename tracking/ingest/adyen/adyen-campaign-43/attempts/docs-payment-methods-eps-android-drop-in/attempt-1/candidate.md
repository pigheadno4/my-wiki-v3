---
title: "Adyen EPS Android Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/eps/android-drop-in/2026-09-15.md"
tags: [adyen, eps, android, drop-in, online-payments]
---

## Overview

An EPS-specific add-on for an existing **Android Drop-in** integration. It separates **Sessions** and **Advanced** server-side flows. The Sessions requirements name Checkout API **v68 or later**; both flows require EPS added in the Customer Area. This child page supplies the recurring mechanism absent from the EPS overview's unresolved “See note”: it describes recurring transactions **through SEPA Direct Debit**, not a generic repeat EPS redirect. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- For **Sessions**, start with an existing Android Sessions Drop-in integration using Checkout API v68+, add EPS in Customer Area, and add **no EPS-specific `/sessions` parameters** for a base payment. The only listed optional EPS configuration is `setSubmitButtonVisible(false)` to hide the submit button; its default is true. The Kotlin sample is schematic, with placeholder `value` and nested braces, so it is a locator for the option rather than copy-ready code. See raw lines 25–62.
- For **Advanced**, start with an existing Android Advanced Drop-in integration that handles an `action.type: redirect`; add EPS in Customer Area. It lists the same optional submit-button setting and **no additional EPS-specific `/payments` parameters** for a base payment. The redirect is an integration prerequisite, not evidence that returning from a bank proves authorization or settlement. See raw lines 113–149; the EPS overview describes the bank redirect journey in [[source-adyen-docs-payment-methods-eps]].
- In **both** flow sections, recurring is specifically via **SEPA Direct Debit**. The page strongly recommends explicit shopper permission and transparency about schedule and amount to reduce chargeback risk. To create a token it says to send `storePaymentMethod: true` and a unique `shopperReference` in **`/payments`**, even in the Sessions section. After settlement a `recurring.token.created` webhook supplies `storedPaymentMethodId`; the server must receive token-lifecycle events. Future `/payments` use the ID, shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. These are **tokenization-use-case additions**, so they do not contradict the no-extra-fields statements for the base EPS payment. See raw lines 64–103 and 151–190.
- Test-payment status is checked in the test Customer Area. Before live EPS acceptance, the page says to request EPS in the live Customer Area. Neither a test-list view nor the request establishes completed live enablement or payment success. See raw lines 105–111 and 192–196.

## Detail locators

- Scope and Sessions prerequisite: raw lines 15–40.
- Sessions optional configuration and SEPA recurring: raw lines 42–103.
- Advanced redirect prerequisite, optional configuration and base request: raw lines 113–149.
- Advanced repeated SEPA token guidance and test/live gate: raw lines 151–196.

## Related

- [[source-adyen-docs-payment-methods-eps]] — EPS overview and AT/EUR bank-redirect method context
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/android-drop-in/2026-09-15|EPS Android Drop-in documentation capture (2026-09-15)]]
