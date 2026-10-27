---
title: "Adyen BACS Direct Debit React Native Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/bacs/react-native-component/2026-09-16.md"
tags: [adyen, bacs, direct-debit, react-native, components, recurring]
---

## Overview

Adyen's 2026-09-16 BACS Direct Debit React Native Component guide supplies method-specific additions to an existing Components integration. It explicitly marks Sessions flow unavailable for React Native Components and documents Advanced flow only for this method. This page-specific restriction does not negate the wrapper's general Sessions capability. See [[adyen]] and [[adyen-react-native-sdk]].

## Key takeaways

- Advanced requires an existing React Native Components integration, `Direct` action handling and BACS added in Customer Area. No BACS-specific Component configuration is required. The prerequisite row is labeled Components but its base-guide link says `integration=Drop-in`; the nearby action and payment links say Components, so the Drop-in URL is not proof of a Drop-in requirement (raw lines 25-53).
- The Advanced `/payments` table marks `shopperEmail`, `paymentMethod.type: directdebit_GB`, holder name, account number and `bankLocationId` required. The TEST v72/GBP/GB curl illustrates those fields, but lacks a shell continuation after `-X POST`, leaving `-d` outside the command as printed; it is not copy-ready shell (raw lines 53-90). The response prose calls `action.type` `Direct`, while its `Received` example contains `action.type: voucher` and a PDF mandate URL. The page does not reconcile these shapes; do not assume one response shape is guaranteed (raw lines 422-435).
- The related [[source-adyen-docs-payment-methods-bacs]] overview says the shopper confirms account ownership and agreement, can download the Direct Debit Instruction after receipt, and that clearing/settlement can take four to six days. This Component page's `Received` example is therefore not cleared funds. The overview also says chargebacks cannot be defended and scheme notice rules can expose a merchant to chargebacks (BACS overview raw lines 23-27, 35-39, 60-74).
- For recurring, Adyen recommends tokenization and strongly recommends explicit shopper permission and a transparent schedule/amount. Under the Direct Debit Guarantee, the Component page says changes in collection date or amount require advance notice; it strongly recommends notice before each payment. For initial token creation it instructs a `/payments` request with `shopperReference` and `storePaymentMethod: true`, then storing `storedPaymentMethodId` if a `recurring.token.created` webhook arrives. Later `/payments` examples use the stored ID, matching shopper reference and `shopperInteraction: ContAuth` (component raw lines 437-490).
- The page says a `Received` response can include `pspReference` and points to webhooks to track success. TEST bank details and test Customer Area status are provided. Live BACS acceptance requires a separate request in live Customer Area (raw lines 490-502).

## Detail locators

- Method-specific Sessions restriction and Advanced prerequisites: raw lines 25-47.
- Advanced required fields, TEST request examples and curl continuation gap: raw lines 49-420.
- Direct-versus-voucher response discrepancy: raw lines 422-435.
- Recurring permission, notice, token creation/reuse and webhook status: raw lines 437-490.
- Test fixtures and live request: raw lines 492-502.
- Related method-level DDI, delayed clearing, notice and chargeback conditions: BACS overview raw lines 23-27, 35-39, 60-74.

## Related raw API references

- [[raw/adyen/docs/payment-methods/bacs/2026-09-15|BACS method overview (relevant lifecycle passages read)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/react-native-component/2026-09-16|BACS Direct Debit React Native Component (2026-09-16 snapshot)]]
