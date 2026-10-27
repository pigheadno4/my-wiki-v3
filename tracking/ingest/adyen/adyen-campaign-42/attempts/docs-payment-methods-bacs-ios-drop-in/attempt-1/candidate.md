---
title: "Adyen BACS Direct Debit iOS Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bacs/ios-drop-in/2026-09-15.md"
tags: [adyen, bacs, direct-debit, ios, drop-in, tokenization]
---

## Overview

This captured Adyen guide adds BACS Direct Debit to an existing iOS Drop-in integration through a Sessions or Advanced server-side flow. It gives method-specific additions, not a complete integration or proof that a debit has settled. See [[adyen]], [[adyen-online-payments]], [[adyen-tokenization]] and [[source-adyen-docs-payment-methods-bacs]] for the GB/GBP method overview, Direct Debit Instruction (DDI), clearing cycle and chargeback risks.

## Key takeaways

- Sessions requires an existing iOS Drop-in Sessions integration, Checkout API v68 or later, and BACS Direct Debit added in Customer Area. It adds required `shopperEmail` to `/sessions` and no BACS-specific Drop-in configuration. The v71 test curl omits a line continuation after `-X POST`, so its `-d` line is not part of the same shell command as printed.
- Advanced requires an existing iOS Drop-in Advanced integration, Customer Area setup and handling of the documented additional `action.type: Direct` action. It adds required `shopperEmail`, `paymentMethod.type: directdebit_GB`, holder name, bank account number and `bankLocationId` to `/payments`; no extra Drop-in configuration is listed. The v72 curl sample also omits a continuation after `-X POST`.
- The Advanced prose says the response has `action.type: Direct`, but the adjacent `Received` example shows `action.type: voucher` with `PDF_MANDATE_URL`. The page does not resolve the mismatch, so the example cannot establish a single action shape. Its recurring section says to use webhooks to track whether a payment succeeds. `Received` does not demonstrate cleared funds; the method overview says DDI/payment submission can take four to six days to clear and settle.
- For recurring BACS, tokenization and explicit shopper permission are strongly recommended. Under the Direct Debit Guarantee, a changed collection date or amount requires advance notice; the page separately recommends notice before every payment. Initial `/payments` token creation adds shopper reference and `storePaymentMethod: true`; when `recurring.token.created` arrives, store its `storedPaymentMethodId`. Later `/payments` use that stored method (or `recurringDetailReference` per the API v49+ wording), the same shopper reference and `shopperInteraction: ContAuth`. Sessions integrations use `/payments` for later recurring payments too. A token or `Received` sample does not prove that a debit cleared.
- The guide provides BACS test bank details and a test Customer Area status route. Live acceptance needs a request in the live Customer Area; this snapshot does not establish merchant approval, DDI validity or successful collection.

## Detail locators

- Sessions prerequisites, v68+, required email, v71 example and missing curl continuation: pinned raw lines 25–67. No additional Drop-in configuration: lines 340–344.
- Advanced prerequisites, `Direct` handling, no configuration, required bank/email fields and v72 curl issue: pinned raw lines 415–475.
- Advanced response conflict between `Direct` prose and `voucher`/mandate-PDF example: pinned raw lines 806–819.
- Sessions recurring permission and changed-amount/date notice, token creation/webhook and recurring request: pinned raw lines 346–399; repeated Advanced route: lines 821–874.
- Test and live gates: pinned raw lines 401–413 and 876–888. DDI and delayed-clearing context: [[source-adyen-docs-payment-methods-bacs]].

## Related

- [[adyen-online-payments]] — main integration concept
- [[adyen-tokenization]] — recurring-token concept
- [[source-adyen-docs-payment-methods-bacs]] — BACS method, DDI, notice and chargeback authority

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/ios-drop-in/2026-09-15|BACS Direct Debit iOS Drop-in, 2026-09-15]]
