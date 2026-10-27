---
title: "Adyen SEPA Direct Debit Web Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit/web-component"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/web-component/2026-09-15.md"
tags: [adyen, sepa-direct-debit, web-components, sessions, advanced-flow, tokenization]
---

## Overview

This captured Adyen guide adds SEPA Direct Debit to an existing Web Components integration, separately for Sessions and Advanced server-side flows. It is a method-specific add-on, not a complete integration, proof of current merchant eligibility, mandate validity or successful collection. See [[adyen]], [[adyen-online-payments]], [[adyen-tokenization]] and the method overview [[source-adyen-docs-payment-methods-sepa-direct-debit]] for mandate, pre-debit notification, chargeback and refund conditions.

## Key takeaways

- Sessions requires an existing Web Components Sessions integration, Checkout API v68 or later, and the payment method added in Customer Area. The ordinary `/sessions` payment needs no additional SEPA-specific request or Component configuration parameters. Import `SepaDirectDebit` from `@adyen/adyen-web` and mount that Component. The no-additional-fields statement applies to the ordinary Sessions payment, not to optional token creation.
- Advanced requires an existing Web Components Advanced integration, setup in Customer Area, and handling for the guide's additional `action.type: direct` action. Its `/payments` request lists `paymentMethod.sepa.ownerName` and `paymentMethod.sepa.ibanNumber` as required; the guide says not to encrypt the IBAN value. Billing-address fields are required when the IBAN belongs to the listed non-EEA SEPA countries or territories. The example uses Checkout API v72 and shows `resultCode: Received`; that example is not evidence of final authorization, capture, settlement or cleared funds.
- If automatic capture is not used, the guide calls for delayed automatic or manual capture; it says SEPA authorizations do not expire and multiple partial captures need Support enablement. These are capture instructions after authorization, not a substitute for a SEPA mandate or debit notification.
- Both flows describe tokenization for Subscription and UnscheduledCardOnFile. Adyen strongly recommends asking explicit shopper permission for future recurring payments; this is advice in this guide, distinct from the mandate acceptance required by the method overview. A created token is delivered through `recurring.token.created` with `storedPaymentMethodId`. Later shopper-absent payments use `/payments` with the stored method, shopper reference, `shopperInteraction: ContAuth` and the matching recurring model; the Sessions flow also uses `/payments` for these later payments. Do not infer token creation or payment success merely from sending the sample request.
- The guide provides test names and IBANs and points to the test Customer Area payment list. For live acceptance it directs merchants to submit a request for SEPA Direct Debit in the live Customer Area. The snapshot and examples do not establish account approval or live readiness.

## Detail locators

- Sessions prerequisites, ordinary no-extra-parameter/configuration statements and Component import/mount: pinned raw lines 25–75.
- Sessions tokenization scope, permission advice, `/sessions` v71 sample and later webhook `/payments` route: pinned raw lines 77–111 and 286–319; UnscheduledCardOnFile sample: lines 599–627.
- Advanced prerequisites, direct action, payment fields, conditional billing address, unencrypted IBAN instruction and v72 sample `Received` response: pinned raw lines 920–1004.
- Advanced capture choices, no-expiry statement and multiple-partial-capture enablement: pinned raw lines 1006–1015. Advanced token lifecycle and shopper-absent reuse: lines 1017–1027 and 1376–1407; unscheduled sample: lines 1687–1715.
- Test data and live request: pinned raw lines 906–918 and 1994–2006. Method-overview mandate, active acceptance and pre-debit-notice conditions: [[source-adyen-docs-payment-methods-sepa-direct-debit]].

## Related

- [[adyen-online-payments]] — main provider integration concept
- [[adyen-tokenization]] — recurring-token concept
- [[source-adyen-docs-payment-methods-sepa-direct-debit]] — method-level mandate, notification and funds-risk authority

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/web-component/2026-09-15|SEPA Direct Debit Web Component, 2026-09-15]]
