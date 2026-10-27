---
title: "BACS Direct Debit Android Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bacs/android-drop-in/2026-09-15.md"
tags: [adyen, bacs, direct-debit, android, drop-in, recurring]
---

## Overview

This 2026-09-15 Adyen guide adds BACS Direct Debit to an existing Android Drop-in integration. It separates Sessions and Advanced server-side flows and covers method-specific request fields, optional Drop-in configuration and tokenized recurring use. It does not replace the base integration or the [[source-adyen-docs-payment-methods-bacs|BACS overview]] for DDI/mandate, clearing and chargeback rules (this raw lines 15–25, 431–439; overview raw lines 23–27, 60–74).

## Key takeaways

- Sessions requires an existing Android Drop-in Sessions integration, Checkout API v68 or later and BACS enabled in Customer Area. It marks `shopperEmail` required on `/sessions`; examples use GB/GBP and an Android app-scheme return URL. The optional `setSubmitButtonVisible` configuration hides the submit button when false and defaults to true (raw lines 25–44, 46–67, 340–360). The curl example lacks a line continuation before `-d` and should not be copied unchanged (raw lines 50–67).
- Advanced requires an existing Android Drop-in Advanced integration, additional-action handling and BACS in Customer Area. Its action-handling link points to `#handle-the-redirect` while labeling `action.type: Direct`. Its `/payments` table marks `shopperEmail`, `paymentMethod.type: directdebit_GB`, holder name, bank account number and `bankLocationId` (bank routing/sort code) required. The submit-button option is repeated (raw lines 431–475). Its curl example also lacks a continuation before `-d` (raw lines 481–504).
- For recurring BACS, the guide recommends tokenization and **strongly recommends** explicit shopper permission and transparency about schedule and amount. It separately says advance notice **must** be given if collection date or amount changes under the Direct Debit Guarantee and strongly recommends notice before each payment. To create a shopper token, add `shopperReference` and `storePaymentMethod: true` to an initial `/payments` request and save `storedPaymentMethodId` from `recurring.token.created`; later `/payments` requests use that token, shopper reference and `shopperInteraction: ContAuth` (raw lines 362–415, 851–904). The overview says shoppers confirm account ownership/agreement and Adyen submits the DDI, with clearing and settlement taking four to six days; BACS chargebacks cannot be defended (overview raw lines 23–27, 60–74).
- Advanced prose says the response includes `action.type: Direct`, but the example labeled successful has `resultCode: Received` and `action.type: voucher` with `PDF_MANDATE_URL`. Preserve this source conflict rather than treating the PDF voucher, the Direct label or `Received` as a universal final success path. The recurring instructions say to use webhooks to track whether a received payment succeeded (raw lines 836–849, 904).
- The TEST section supplies an account name, account number and sort code and points to Customer Area for test status. The page requires a separate request in the **live** Customer Area before live BACS acceptance. Examples and the historical snapshot do not prove current enablement, a valid DDI, a completed debit or settled funds (raw lines 417–429, 906–916; overview raw lines 23–27).

## Detail locators

- Sessions prerequisites, required email and sample request: raw lines 25–67.
- Sessions optional configuration, recurring token flow and test/live gate: raw lines 340–429.
- Advanced prerequisites, action label/link, optional config and required `/payments` fields: raw lines 431–475.
- Advanced request examples and Direct/voucher response conflict: raw lines 477–849.
- Advanced recurring/token route, webhook outcome and test/live gate: raw lines 851–916.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-bacs|BACS overview (DDI, clearing and chargeback context)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/android-drop-in/2026-09-15|BACS Direct Debit Android Drop-in, fetched 2026-09-15]]
