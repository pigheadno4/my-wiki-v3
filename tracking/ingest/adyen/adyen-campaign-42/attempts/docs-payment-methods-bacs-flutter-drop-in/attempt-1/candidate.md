---
title: "BACS Direct Debit Flutter Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bacs/flutter-drop-in/2026-09-15.md"
tags: [adyen, bacs, direct-debit, flutter, drop-in, recurring, tokenization]
---

## Overview

This 2026-09-15 Adyen page gives BACS Direct Debit additions to an **existing Flutter Drop-in** integration, separately for Sessions and Advanced server-side flows. It covers shopper email and bank fields, recurring tokens, asynchronous outcome tracking, TEST details and the live Customer Area gate. It is not evidence of a valid Direct Debit Instruction, live enablement, or cleared funds. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** the requirements say existing Flutter Drop-in Sessions, **Checkout API v68 or later**, and Support addition of BACS in Customer Area; the prerequisite link itself points to an **Advanced** Flutter guide, while the create-session link points to Sessions. Add required `shopperEmail` to `/sessions`; no BACS-specific Drop-in configuration is required. The GB/GBP examples use a v71 TEST endpoint, not a new minimum. See raw lines 25–45, 49–69 and 341–345.
- **Advanced:** requires existing Flutter Drop-in Advanced and BACS addition in Customer Area; the `/payments` table marks `shopperEmail`, `paymentMethod.type=directdebit_GB`, `holderName`, `bankAccountNumber` and `bankLocationId` required. No BACS-specific Drop-in configuration is needed. The GB/GBP example uses a v72 TEST endpoint; the Advanced subsection does not give its own API version minimum. See raw lines 414–445 and 449–472.
- **Action/response conflict:** Advanced requirements and prose say `action.type: Direct`, while the displayed 'successful payment' example says `resultCode: Received` and gives `action.type: voucher` with a PDF mandate URL. The action link is a `handle-the-redirect` anchor. Preserve this inconsistency; it is not a reliable universal action-handling recipe. `Received` plus `pspReference` means receipt, with actual success tracked by webhooks. See raw lines 423, 805–817 and 873.
- **Recurring:** this guide recommends tokenization for subscriptions: on the initial `/payments` request add `shopperReference` and `storePaymentMethod: true`, retain `storedPaymentMethodId` from `recurring.token.created`, then use `/payments` with token (or `recurringDetailReference`), same shopper reference and `ContAuth`. It strongly recommends explicit permission and clarity on schedule/amount; it says advance notice **must** be given if collection date or amount changes under the Direct Debit Guarantee, and recommends advance notice before each payment. Do not turn recommendation into a separate stated mandate rule; [[source-adyen-docs-payment-methods-bacs]] covers DDI context. See raw lines 347–400 and 820–873. [[adyen-tokenization]]
- **TEST/live:** use the shown test bank details and Customer Area payment list for TEST. A live BACS request in **live** Customer Area is required before accepting live payments. A test payment and `Received` response do not establish clearing; the BACS overview separately describes DDI, four-to-six-day clearing and chargeback exposure. See raw lines 402–412 and 875–885.
- **Examples:** language SDK snippets have separate historical versions for Sessions and Advanced (for example Java v40.0.0/v41.0.0, PHP v28.3.0/v29.0.0 and Node v30.0.0/v30.1.0). They are not a current cross-language support matrix. See raw lines 71–338 and 473–802.

## Detail locators

- Sessions requirements, mismatched prerequisite link, email and request examples: raw lines 25–338.
- Sessions no-extra-config, token/notice lifecycle and receipt result: raw lines 341–400.
- Advanced setup, no-extra-config, required bank fields and language examples: raw lines 414–802.
- Advanced action/response discrepancy and recurring duplicate: raw lines 805–873.
- TEST and live request gates: raw lines 402–412 and 875–885.

## Related

- [[adyen-online-payments]] — Flutter Drop-in integration route.
- [[adyen-tokenization]] — BACS recurring-token flow.
- [[source-adyen-docs-payment-methods-bacs]] — overview, Direct Debit Instruction, clearing and chargeback context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/flutter-drop-in/2026-09-15|BACS Direct Debit Flutter Drop-in, captured 2026-09-15]]
