---
title: "Adyen Alipay iOS Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/alipay/ios-component/2026-09-15.md"
tags: [adyen, alipay, ios, components, online-payments]
---

## Overview

This [[adyen]] guide, modified and captured 2026-09-15, adds Alipay to an **existing iOS Components** integration. It separates Sessions and Advanced server-side flows, uses `InstantPaymentComponent`, and relies on existing redirect handling. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-alipay|Alipay overview]] for the dated outside-China merchant-processing boundary. This page's setup and example are not evidence of live method availability, completed return, final authorization, capture or settlement. See primary raw lines 15–36 and 81–133.

## Key takeaways

- **Sessions:** the existing iOS Components integration must use Sessions and **Checkout API v68 or later**; it must handle `action.type: redirect`, and Alipay must be added in Customer Area. This branch says no Alipay-specific `/sessions` fields or Component configuration parameters are needed. The v68+ condition is stated only in this Sessions requirements table; the Advanced table below does not state a Checkout API minimum. See raw lines 23–48 and 85–97.
- **Sessions client:** obtain the `alipay` method from the session's payment methods, then create `InstantPaymentComponent`, assign the session as delegate and call `initiatePayment()`. The sample guards method support before showing it. Initiating the Component is a shopper-flow action, not a server payment result. See raw lines 50–69.
- **Advanced:** the page requires an existing iOS Components Advanced flow, `action.type: redirect` handling and Customer Area Alipay addition; it says no Alipay-specific Component configuration or `/payments` fields. The Advanced sample creates `InstantPaymentComponent`, sets the Component's delegate to `self` and initiates it, but references `paymentMethods` without defining it within that snippet; it assumes existing integration context. The Advanced requirements' **integration-type link points to `integration=Drop-in`** despite the row saying Components, while its redirect/payment links point to Components. Keep the stated Components requirement primary and treat the link/sample as incomplete navigation/code. See raw lines 81–123.
- Both branches recommend **live penny tests** with an Alipay wallet and viewing test-payment details in **live** Customer Area. They also say a request for Alipay in live Customer Area is required before accepting live payments. These are page instructions, not proof a request was approved or a payment executed. This historical guide gives no country/currency matrix, callback result interpretation, webhook/final-status rule, refund or capture procedure; use the appropriate main integration and outcome guides. See raw lines 71–79 and 125–133.

## Detail locators

- **Sessions prerequisites, v68+ gate, request/configuration and component snippet:** raw lines 23–69.
- **Advanced prerequisites, Drop-in-link mismatch, snippet and no-extra-field statements:** raw lines 81–123.
- **Live penny-test recommendation and live method request:** raw lines 71–79, 125–133.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipay]]
- [[adyen-payment-testing]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay/ios-component/2026-09-15|Alipay iOS Component — captured 2026-09-15]]
