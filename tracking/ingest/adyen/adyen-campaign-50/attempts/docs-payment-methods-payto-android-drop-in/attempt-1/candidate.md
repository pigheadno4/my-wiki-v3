---
title: "Adyen PayTo Android Drop-in integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payto/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/payto/android-drop-in/2026-09-15.md"
tags: [adyen, payto, android, drop-in, sessions, advanced-flow, subscriptions]
---

## Overview

This 2026-09-15-captured Adyen guide adds PayTo-specific steps to an **existing Android Drop-in** integration. It separates Sessions flow from Advanced flow, and one-time payments from subscription agreement setup and later subscription payments. See [[adyen]] and [[adyen-online-payments]]. Its AU/AUD values and PayID are examples and do not establish current merchant eligibility or a completed live payment.

## Key takeaways

- Both flows require an existing Android Drop-in integration, Checkout API **v70 or later**, and PayTo added in Customer Area. Advanced flow must also handle the **await** action. See raw lines 25–34 and 295–303.
- Sessions flow adds PayTo parameters to **/sessions** for a one-time payment or subscription agreement plus first payment. The subscription setup table marks shopper names, storage, recurring model, interaction, and mandate terms required. **Subsequent subscription payments can only use Advanced flow or API Only**, not the Sessions setup flow. See raw lines 38–50 and 121–140.
- In Advanced flow, **/payments** accepts one-time, subscription setup/first-payment, and subsequent subscription requests. The latter uses the stored payment method ID from the **recurring.token.created** webhook with **ContAuth**, only within the accepted agreement's conditions. See raw lines 329–349, 404–430 and 509–518.
- The shopper receives a bank notification to authorize or decline the **agreement**. Agreement acceptance and its **RECURRING_CONTRACT** notification do not establish payment success: the **AUTHORISATION** webhook can report an authorized or rejected payment on an accepted agreement. Example Advanced responses show **Pending** for initial requests and **Received** for a later request. Refunds can fail asynchronously, indicated by **REFUND_FAILED**. See raw lines 216–253, 388–402, 489–507, 545–569 and 583–613.

## Source cautions

- The Sessions subscription table marks **storePaymentMethod=true** required, but the Sessions subscription request example omits the field. Follow the table rather than treating that example as a complete request; the example also has a missing comma after shopperReference. See raw lines 129, 161–193.
- The agreement-acceptance prose names **recurringDetailReference** in **RECURRING_CONTRACT**, while the subsequent-payment table names **data.storedPaymentMethodId** in **recurring.token.created**. These are distinct stated fields and webhook sources; the page does not establish that they are interchangeable. See raw lines 218, 507 and 516.
- Test email identifiers simulate agreement and payment outcomes. They are not evidence of live bank acceptance or payment finality. See raw lines 281–293 and 615–627.

## Detail locators

- Sessions one-time parameters and response mandate defaults: raw lines 52–119.
- Sessions subscription mandate and required fields: raw lines 121–159.
- Advanced configuration and request tables: raw lines 295–357 and 404–430.
- Shopper account identifier formats: raw lines 571–581.
- Required webhook meanings and test cases: raw lines 583–627.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payto/android-drop-in/2026-09-15|Fully read PayTo Android Drop-in raw]]
