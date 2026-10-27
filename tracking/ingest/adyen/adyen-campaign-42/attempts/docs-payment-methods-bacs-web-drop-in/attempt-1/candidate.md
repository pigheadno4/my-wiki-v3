---
title: "Adyen BACS Direct Debit Web Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bacs/web-drop-in/2026-09-15.md"
tags: [adyen, bacs, direct-debit, web, drop-in, recurring]
---

## Overview

Adyen's 2026-09-15 BACS Direct Debit Web Drop-in guide adds method-specific request and tokenization instructions to an existing Web Drop-in integration. It covers both Sessions and Advanced server-side flows. The page is integration guidance; a `Received` response is not final clearing or proof of funds. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires an existing Web Drop-in Sessions integration, Checkout API v68 or later, and BACS added in Customer Area. The method-specific `/sessions` field is required `shopperEmail`. `BacsDirectDebit` is an optional individual import for tree shaking. The TEST/GBP/GB session examples use an app-style `adyencheckout://` return URL despite this Web page; treat it as a sample value, not a general Web return-URL rule (raw lines 25-68, 341-351).
- Advanced requires an existing Web Drop-in Advanced integration, BACS added in Customer Area and additional-action handling. Its `/payments` table requires `shopperEmail`, `paymentMethod.type: directdebit_GB`, account holder name, bank account number and `bankLocationId` (the bank routing/sort-code value in the sample); the optional `BacsDirectDebit` import applies here too (raw lines 422-487). The prerequisite calls the action `Direct`, but the response section says `Direct` while the shown `Received` response contains `action.type: voucher` and `PDF_MANDATE_URL`. This source does not reconcile that discrepancy; handle the actual returned action under the base integration guidance rather than assuming the example is a guaranteed shape (raw lines 428-431, 819-832).
- For recurring, Adyen recommends tokenizing details and strongly recommends explicit shopper permission and transparent schedule/amount to reduce chargeback risk. This guide additionally states that a changed collection date or amount requires advance notice under the Direct Debit Guarantee, and strongly recommends notice before each payment. The initial token instructions specifically say to make a `/payments` request with `shopperReference` and `storePaymentMethod: true`; `recurring.token.created` supplies the `storedPaymentMethodId`. Later `/payments` examples use that ID, the same shopper reference and `shopperInteraction: ContAuth` (raw lines 353-406, 834-887).
- For recurring requests, the page says `paymentMethod.recurringDetailReference` or `paymentMethod.storedPaymentMethodId` for API v49 and above; this historical wording should not erase the explicit `storedPaymentMethodId` returned by its token webhook and used in its JSON example (raw lines 374-403, 855-884).
- The page says `Received` plus `pspReference` means a payment request was received and points to webhooks to track whether it succeeded. TEST bank details and test Customer Area status are provided; live BACS acceptance requires a separate request in live Customer Area (raw lines 406-420, 887-901). The method's DDI, clearing and chargeback lifecycle belongs to [[source-adyen-docs-payment-methods-bacs]]; this page does not by itself prove funds have cleared.

## Detail locators

- Sessions requirements, required email, examples and optional import: raw lines 25-351.
- Sessions recurring token, notice, received/webhook and test/live instructions: raw lines 353-420.
- Advanced requirements, optional import, required fields and TEST request examples: raw lines 422-817.
- Advanced response action discrepancy: raw lines 819-832.
- Advanced recurring and test/live instructions: raw lines 834-901.

## Related raw API references

- [[raw/adyen/docs/payment-methods/bacs/2026-09-15|BACS overview (unread navigation)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/web-drop-in/2026-09-15|BACS Direct Debit Web Drop-in (2026-09-15 snapshot)]]
