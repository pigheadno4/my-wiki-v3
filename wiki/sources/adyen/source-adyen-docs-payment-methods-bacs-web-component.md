---
title: "BACS Direct Debit Web Component integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/web-component"
raw_files:
  - "adyen/docs/payment-methods/bacs/web-component/2026-09-15.md"
tags: [adyen, bacs, direct-debit, web, component, recurring, tokenization]
---

## Overview

This 2026-09-15 Adyen page describes BACS Direct Debit additions to an **existing Web Components** integration, separately for Sessions and Advanced flows. It covers shopper email and bank fields, Component initialization, recurring tokens, intermediate outcomes and TEST/live gates. It is not proof of an enabled merchant, a valid Direct Debit Instruction, or cleared funds. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions** requires an existing Web Components Sessions integration, **Checkout API v68 or later**, BACS enablement in Customer Area, and `shopperEmail` in `/sessions`. The examples use GB/GBP and a v71 TEST endpoint; the example version does not revise the v68 minimum. Import `BacsDirectDebit`, initialize/mount its Component, and add no BACS-specific configuration. See raw lines 25–45, 49–69 and 343–369.
- **Advanced** requires an existing Web Components Advanced integration and BACS enablement; its `/payments` table marks `shopperEmail`, `paymentMethod.type=directdebit_GB`, `holderName`, `bankAccountNumber` and `bankLocationId` required. The curl example uses GB/GBP and a v72 TEST endpoint. The Advanced section has no explicit Checkout API minimum of its own; do not generalize the Sessions v68 statement without checking the Advanced integration guide. See raw lines 442–494 and 497–520.
- **Action inconsistency:** Advanced requirements and prose say `action.type: Direct`, with a link whose anchor says `handle-the-redirect`; the displayed 'successful payment' response instead has `resultCode: Received` and `action.type: voucher` with a PDF mandate URL. Preserve these as a source conflict, not an implementable universal action recipe. `Received` and a `pspReference` indicate receipt; the guide says track actual success using webhooks. See raw lines 449, 853–865 and 921.
- **Recurring:** the page recommends tokenization for subscriptions. For an initial `/payments` token request add `shopperReference` and `storePaymentMethod: true`, then save `storedPaymentMethodId` from `recurring.token.created`. Later BACS debits use `/payments` with that token (or `recurringDetailReference`), the same `shopperReference`, and `shopperInteraction: ContAuth`. It strongly recommends explicit shopper permission and transparency about schedule/amount; it says advance notice is **required when date or amount changes** under the Direct Debit Guarantee and recommends notice before each debit. This page's recommendation wording is distinct from the DDI details in [[source-adyen-docs-payment-methods-bacs]]. See raw lines 374–428 and 868–921. [[adyen-tokenization]]
- **Testing/live:** a TEST account fixture and Customer Area payment list are provided. Before live BACS acceptance, the guide requires a BACS request in the **live** Customer Area; a test payment is not live enablement. The overview source explains separate DDI, four-to-six-day clearing, chargeback and advance-notice risks; none is resolved by a `Received` response. See raw lines 430–440 and 923–933.
- **Example scope:** the page shows language-library examples with differing versions for Sessions versus Advanced (for example Java v40.0.0/v41.0.0, PHP v28.3.0/v29.0.0, Node v30.0.0/v30.1.0). These are historical samples, not a universal version matrix. See raw lines 71–340 and 521–850.

## Detail locators

- Sessions requirements, email field and examples: raw lines 25–340.
- Component import, no-extra-configuration and initialization: raw lines 343–369; Advanced import/initialization: 454–477.
- Sessions recurring token and notice details, receipt outcome: raw lines 374–428.
- Advanced prerequisites, required bank fields and example versions: raw lines 442–850.
- Advanced action/response discrepancy and recurring duplicate: raw lines 853–921.
- TEST and live request gates: raw lines 430–440 and 923–933.

## Related

- [[adyen-online-payments]] — Web Component flow route.
- [[adyen-tokenization]] — stored payment method recurring route.
- [[source-adyen-docs-payment-methods-bacs]] — BACS overview, DDI, clearing and chargeback context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/web-component/2026-09-15|BACS Direct Debit Web Component, captured 2026-09-15]]
