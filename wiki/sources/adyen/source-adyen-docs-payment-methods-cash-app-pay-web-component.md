---
title: "Adyen Cash App Pay Web Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-pay/web-component"
raw_files:
  - "adyen/docs/payment-methods/cash-app-pay/web-component/2026-09-15.md"
tags: [adyen, cash-app-pay, web, components, tokenization]
---

## Overview

This 2026-09-15-captured page, last modified in 2023, adds **Cash App Pay** to an existing Adyen Web Components integration and documents optional saved-detail payments. It is about Cash App Pay, a separate method from Cash App Afterpay. The page covers both Sessions and Advanced flows, Web Component setup, token creation and reuse, $cashtag retrieval, and token deletion notification. It is a dated method-specific add-on, not proof of current feature availability, merchant enablement, or live payment execution. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Base setup and Component:** Both flows require an existing Web Components integration at **v5.44.0 or later**, the Recurring tokens life cycle events webhook, Cash App Pay added in Customer Area, and the page's **Developer > Additional data > Payment > Save configuration** step. The page says no additional Cash App Pay API fields are needed for an ordinary payment. For v6 it shows the `CashAppPay` import and `new CashAppPay(checkout)`; for v5.x or earlier it uses `checkout.create('cashapp')`. It says to pass `amount` through `/sessions` or the `AdyenCheckout` instance for `/payments`, except zero-value authorizations (raw lines 21–95).
- **Optional UI configuration:** `enableStoreDetails` shows a shopper-choice toggle; `storePaymentMethod` saves without a toggle. Both default to false in the table. `showPayButton` also defaults false; a custom Pay button must call `.submit()`. The `onClick(actions)` handler can resolve or reject continuation. These are Component settings, not a blanket mandate to store payment details (raw lines 97–112).
- **Consent and token creation:** The page describes stored details for future recurring and card-on-file payments and says permission to save details at token creation can bypass the shopper approval step for those future payments. It **strongly recommends** explicit shopper permission and transparency about recurring timing and amount; it does not call that recommendation an absolute schema requirement or guarantee later approval. In Sessions with Checkout API **v70+**, it lists `recurringProcessingModel`, `shopperReference` and `storePaymentMethodMode`, with disabled, askForConsent and enabled modes. For **v69**, shopper choice uses `enableStoreDetails: true`; automatic storage uses `storePaymentMethodMode: enabled` in `/sessions` and `storePaymentMethod: true` in the Component. In Advanced, forward `state.data.storePaymentMethod` and send it with `shopperReference` in `/payments` to create a token (raw lines 114–159, 444–459).
- **Retrieval, $cashtag and reuse:** To show saved methods, send the same shopper reference to `/paymentMethods`, use that shopper's `storedPaymentMethods`, and pass valid Component `state.data` to the server. The page recommends including a shopper's **$cashtag** in future recurring payments for recognition; obtaining it requires `/payments/details` and enabling **Token information for digital wallets** in Customer Area. A Sessions integration wanting that detail must switch to Advanced and implement both `/payments/details` and `/payments`; the `recurring.token.created` webhook does not contain the $cashtag. For Advanced stored payments, the server sends `state.data.paymentMethod` with the tokenized-payment parameters; `paymentMethod.cashtag` is optional in the page. The sample includes `storedPaymentMethodId`, `shopperInteraction: ContAuth`, `recurringProcessingModel: CardOnFile`, and a sample `Authorised` result, not proof of a real transaction (raw lines 461–913).
- **Token deletion and environments:** The page says a shopper deletion of stored Cash App Pay details results in `recurring.token.disabled`; remove the stored token and ask for another method to avoid later failures. Use test-environment magic values for simulated scenarios, inspect the test Customer Area, and add Cash App Pay in the live Customer Area before going live (raw lines 915–941).

> [!warning] Captured example and navigation gaps
> The Sessions v70+ field table lists `shopperReference`, but its consent example requests at raw lines 161–442 omit that field. Do not copy the example as a complete token-creation contract; follow the field prose and active Checkout API schema. The v6 import link at raw line 45 selects `integration=Drop-in` even though this is a Components guide. The `/payments/details` response sample spells `merchantRreference` (line 523), and stored-payment examples use `returnUrl: "..."` (lines 574, 613, 658 and later). Treat those as illustrative source snippets. Do not infer that the example `Authorised` response or a saved token proves future authorization, settlement, or current merchant entitlement.

## Detail locators

- Both-flow prerequisites, API field scope and versioned Component initialization: raw lines 21–95.
- Optional Component configuration and `onClick`: raw lines 97–112.
- Saved-detail rationale and Sessions v70+/v69 request modes and examples: raw lines 114–449.
- Advanced token creation, stored display, $cashtag and details response: raw lines 450–531.
- Stored payment flows, request examples and example result: raw lines 533–913.
- Disabled-token webhook and test/live setup: raw lines 915–941.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-pay/web-component/2026-09-15|Cash App Pay Web Component guide, captured 2026-09-15]]
