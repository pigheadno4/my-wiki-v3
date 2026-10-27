---
title: "Adyen BACS Direct Debit React Native Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bacs/react-native-drop-in/2026-09-15.md"
tags: [adyen, bacs, direct-debit, react-native, drop-in, sessions, advanced-flow, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds BACS Direct Debit to an **existing React Native Drop-in** integration, with separate Sessions and Advanced server-side instructions and recurring token steps. It is a channel-specific add-on; the [[source-adyen-docs-payment-methods-bacs]] overview supplies the Direct Debit Instruction (DDI), four-to-six-day clearing, notice and nondefendable chargeback context. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow:** Requires an existing Sessions React Native Drop-in integration, Checkout API **v68 or later**, and BACS Direct Debit added in Customer Area. The method-specific `/sessions` addition is required `shopperEmail`; no extra BACS Drop-in configuration is stated. The example uses test Checkout API **v71**, GB/GBP and a native-style return URL; it does not set an SDK version or prove current eligibility. The Sessions prerequisite label links to an **Advanced-flow URL**, while the next session-step link points to Sessions; verify the intended base guide. The displayed curl has no continuation after `-X POST`, so it is not copy-ready. (raw lines 25–68, 341–345)
- **Advanced flow:** Requires an existing Advanced React Native Drop-in integration, BACS Customer Area setup and action handling labeled `Direct`; no extra BACS configuration is stated. Its `/payments` table requires shopper email and `paymentMethod.type: directdebit_GB`, holder name, account number and `bankLocationId` (described there as the bank routing number). The test request example uses **v72** and GB/GBP. Its curl likewise lacks continuation after `-X POST`. (raw lines 414–473)
- **Action/response conflict:** Advanced prose says the response includes `action.type: Direct`, yet the adjacent “successful payment” JSON shows `resultCode: Received` with `action.type: voucher`, `paymentMethodType: directdebit_GB` and a `PDF_MANDATE_URL`. The page does not reconcile these shapes. Do not assume the example establishes the action contract or a successful, cleared debit; check actual integration authority and webhooks. The Sessions recurring text likewise says `Received` and `pspReference` mean a payment was **received**, with success tracked by webhooks. (raw lines 400, 805–818, 873)
- **Recurring and notice:** For a recurring/subscription business model, the guide **recommends** tokenizing. Its initial `/payments` token step adds `shopperReference` and `storePaymentMethod: true`; when `recurring.token.created` arrives, store `storedPaymentMethodId`. Later recurring `/payments` add that stored ID or `recurringDetailReference` (worded “for API v49 and above”), same shopper reference and `shopperInteraction: ContAuth`. This route applies even when the initial integration uses Sessions. The guide strongly recommends explicit shopper permission and advance notice before each payment; it separately states that under the Direct Debit Guarantee, **a change in collection date or amount requires advance notice**. The BACS overview carries additional scheme-notice timing and DDI duties. A token or `Received` result is no proof of funds. (raw lines 347–400, 820–873; [[source-adyen-docs-payment-methods-bacs]])
- **Test/live gate:** The page gives a test account name, account number and sort code, test Customer Area status navigation, and a required request for BACS Direct Debit in the **live** Customer Area before live acceptance. Neither test detail nor the historical snapshot proves account approval or settled funds. (raw lines 402–412, 875–885)

## Detail locators

- Sessions prerequisites, required shopper email, v71 GB/GBP sample, URL mismatch and curl formatting: pinned raw lines 25–68.
- Sessions optional configuration, token creation/reuse, guarantee notice and `Received` webhook boundary: pinned raw lines 341–400.
- Advanced prerequisites, required shopper/bank fields and v72 example: pinned raw lines 414–473.
- Advanced `Direct` prose versus `voucher` sample and `Received`: pinned raw lines 805–818.
- Advanced recurring block repeating token and notice steps: pinned raw lines 820–873.
- Test data and live request: pinned raw lines 402–412 and 875–885. Method-level DDI, settlement and chargeback risks: [[source-adyen-docs-payment-methods-bacs]].

## Related

- [[adyen-online-payments]] — provider online-payment context
- [[adyen-tokenization]] — provider recurring-token context
- [[adyen-react-native-sdk]] — broader native wrapper context, separate from this API-versioned guide
- [[source-adyen-docs-payment-methods-bacs]] — method-level DDI, clearing, notice and chargeback authority
- [[adyen]] — provider

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/react-native-drop-in/2026-09-15|BACS Direct Debit React Native Drop-in, 2026-09-15]]
