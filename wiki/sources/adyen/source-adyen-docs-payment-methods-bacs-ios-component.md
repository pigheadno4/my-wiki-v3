---
title: "Adyen BACS Direct Debit iOS Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/ios-component"
raw_files:
  - "adyen/docs/payment-methods/bacs/ios-component/2026-09-15.md"
tags: [adyen, bacs, direct-debit, ios, components, tokenization]
---

## Overview

This captured Adyen guide adds BACS Direct Debit to an existing iOS Components integration using Sessions or Advanced server-side flow. It specifies method additions, not the full native integration or proof of a completed debit. See [[adyen]], [[adyen-online-payments]], [[adyen-tokenization]] and [[source-adyen-docs-payment-methods-bacs]] for the GB/GBP method overview, Direct Debit Instruction (DDI), delayed clearing and chargeback risks.

## Key takeaways

- Sessions requires an existing iOS Components Sessions integration, Checkout API v68 or later, and BACS Direct Debit added in Customer Area. The method-specific `/sessions` addition is required `shopperEmail`; no additional BACS Component configuration is listed. The Swift example checks for `BACSDirectDebitPaymentMethod`, creates `BACSDirectDebitComponent`, makes the session its delegate and presents the view controller. The v71 test curl lacks a line continuation after `-X POST`, so the following `-d` is not in the same shell command as printed.
- Advanced requires an existing integration and Customer Area setup. The requirements row labels it iOS Components but links to the iOS **Drop-in** base guide, while its action-handling link and Swift example point to Components. It says to handle an additional `action.type: Direct`, use `BACSDirectDebitComponent` with the integration as delegate, and send `/payments` with required `shopperEmail`, `paymentMethod.type: directdebit_GB`, holder name, bank account number and `bankLocationId` (sort code/routing identifier). The v72 test curl likewise omits a continuation after `-X POST`. Treat the mismatched base-guide link as a documentation conflict, not a reason to substitute Drop-in.
- The Advanced prose says the response has `action.type: Direct`, but the adjacent `Received` example has `action.type: voucher` and `PDF_MANDATE_URL`; this source does not resolve the mismatch. Do not assume a single action shape from this example. `Received` is a received request, not proof of cleared funds; the method overview describes DDI submission and a four-to-six-day clearing/settlement cycle. Follow payment status with webhooks as the recurring section instructs.
- For recurring BACS, tokenization is recommended for recurring/subscription models and explicit shopper permission is strongly recommended. Under the Direct Debit Guarantee, a changed collection date or amount requires advance notice; the guide separately recommends notice before each payment. To create a token, the initial `/payments` request includes `shopperReference` and `storePaymentMethod: true`; on `recurring.token.created`, retain `storedPaymentMethodId`. Later `/payments` use the stored method (or `recurringDetailReference` per the API v49+ wording), same shopper reference and `shopperInteraction: ContAuth`. A Sessions integration also uses `/payments` for later recurring charges. The token or `Received` examples do not establish that a debit cleared.
- Test with the supplied account number/sort code and check the test Customer Area payment list; live acceptance needs a request in the live Customer Area. A captured guide cannot establish current approval, DDI validity or successful collection.

## Detail locators

- Sessions integration, v68+, Customer Area, required email and v71 curl line-continuation issue: pinned raw lines 25–68. No additional Component configuration and Swift construction/delegate: lines 341–370.
- Advanced prerequisites and inconsistent Drop-in link versus Components action link: pinned raw lines 439–449. Component setup: lines 451–479. Required `/payments` fields and v72 request/curl issue: lines 481–523.
- Advanced response conflict, `Direct` prose versus `voucher`/mandate-PDF example: pinned raw lines 854–867.
- Sessions recurring permission, Direct Debit Guarantee notice, token creation and shopper-absent reuse: pinned raw lines 372–425; repeated Advanced route: lines 869–922.
- Test and live gates: pinned raw lines 427–437 and 924–934. Method overview's DDI/clearing/chargeback context: [[source-adyen-docs-payment-methods-bacs]].

## Related

- [[adyen-online-payments]] — main integration concept
- [[adyen-tokenization]] — recurring-token concept
- [[source-adyen-docs-payment-methods-bacs]] — BACS method, DDI, advance notice and chargeback authority

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/ios-component/2026-09-15|BACS Direct Debit iOS Component, 2026-09-15]]
