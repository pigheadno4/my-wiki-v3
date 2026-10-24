---
title: "Adyen Touch'n Go iOS Component integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/touchngo/ios-component"
raw_files:
  - "adyen/docs/payment-methods/touchngo/ios-component/2026-09-15.md"
tags: [adyen, touchngo, ios, components, wallets]
---

## Overview

This [[adyen]] method guide adds Touch'n Go to an **existing iOS Components** integration, with separate Sessions/Advanced base-flow prerequisites and version-specific Component creation. See [[adyen-online-payments]] and [[adyen-ios-sdk]]. This captured guide is not evidence of current merchant enablement or a completed payment.

## Key takeaways

- Sessions and Advanced tabs each require the corresponding **existing iOS Components** integration and say to contact Adyen Support to add Touch'n Go in Customer Area before beginning. The page does not give a Checkout API minimum. See raw lines 21–37.
- Its API section says **no additional Touch'n Go-specific fields** are needed. It links `/sessions` as the default for **Components v5.0.0 or later** and `/payments` for an additional use case; optional general-payment-method fields remain possible. Do not read that as a claim that the merchant needs no base flow or server request. See raw lines 39–44.
- For **iOS Components v5.0.0+**, the examples check for payment method `.other("touchngo")`, instantiate `InstantPaymentComponent`, retain it, set the delegate, and call `initiatePayment()`. In the Sessions example the delegate is `session`; in Advanced it is `self`. This is method/component setup, not payment authorization or a complete app-return/outcome contract. See raw lines 46–83.
- The **v4.x.x** example instead looks up `TouchnGoPaymentMethod` and presents `TouchnGoComponent` with `FormComponentStyle`. The page then says no further Touch'n Go-specific Components configuration is required. Do not generalize the v4 type/constructor to v5 or the v5 delegate pattern to v4. See raw lines 85–101.
- The guide directs test payment status checks to the test Customer Area, and requires contacting Support to add Touch'n Go in the **live Customer Area** before live acceptance. A status-list check or Support request is not evidence that a specific authorization or settlement succeeded. This page does not detail app return, `/payments/details`, QR expiry, webhook timing or final payment status. See raw lines 103–113.

## Detail locators

- **Sessions/Advanced prerequisites and Support setup:** raw lines 21–37.
- **No extra method fields and endpoint context:** raw lines 39–44.
- **v5+ InstantPaymentComponent and delegate split:** raw lines 46–83.
- **v4.x.x specialized component:** raw lines 85–101.
- **Test status and live addition:** raw lines 103–107.

## Related

- [[adyen-online-payments]]
- [[adyen-ios-sdk]]
- [[source-adyen-docs-payment-methods-touchngo]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/touchngo/ios-component/2026-09-15|Touch'n Go iOS Component guide — captured 2026-09-15]]
