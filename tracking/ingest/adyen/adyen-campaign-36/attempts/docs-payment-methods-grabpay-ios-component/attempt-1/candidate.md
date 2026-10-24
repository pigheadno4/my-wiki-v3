---
title: "GrabPay iOS Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/grabpay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/grabpay/ios-component/2026-09-15.md"
tags: [adyen, grabpay, ios, components, wallet, paylater, online-payments]
---

## Overview

This [[adyen]] guide, captured 2026-09-15, adds GrabPay to an **existing iOS Components** integration using Sessions or Advanced server flow. It distinguishes GrabPay **Wallet** from **PayLater** request requirements and gives versioned native Component examples. It does not establish current merchant/region/currency eligibility, a completed shopper redirect or return, authorization, capture, settlement or refund. See [[adyen-online-payments]] and raw lines 15–48.

## Key takeaways

- Either an existing **Sessions** or **Advanced** iOS Components integration and adding GrabPay in Customer Area are stated prerequisites. For **PayLater**, including postpaid or installment payments, the merchant must collect and send delivery address and purchased-item information: `deliveryAddress` and `lineItems` are marked required in both `/sessions` and `/payments` tables. Sending those fields for **Wallet** is described as a strong recommendation for future PayLater development, not a Wallet requirement. See raw lines 21–57 and 510–517.
- The `/sessions` examples use a custom-scheme `returnUrl` (`my-app://adyen`) and TEST `/v69/sessions`; the `/payments` examples use TEST `/v72/payments` and `paymentMethod.type: grabpay_SG`. Those endpoint versions and the `grabpay_SG` sample are examples, not stated minimum Checkout API versions or a complete region/method matrix. Many sample country and currency values are empty placeholders, and the illustrated order amount is 1000 while its lone line item has `amountIncludingTax: 400`; do not copy these as a complete, balanced live request. See raw lines 59–93 and 519–555.
- The page labels `/sessions` "default with Web Components v5.0.0 or later" and `/payments` for an additional use case or Web Components before v5.0.0, even though this guide is for **iOS** Components. Keep that Web-version wording as a source inconsistency; the separate native Component section gives the relevant **iOS** version split. The Java `/payments` example constructs a delivery address but never calls a setter for it on the payment request, despite the PayLater table marking it required. The Node `/sessions` samples refer to `Config` and `EnvironmentEnum` without declaring/importing them in the shown snippet. Review examples against the actual API-library version and base iOS guide. See raw lines 50–52, 266–310, 510–517, 557–604 and 457–507.
- With **iOS Components v5.0.0 or later**, the guide checks for `.other("grabpay_SG")`, creates `InstantPaymentComponent`, and assigns the **session** as delegate in Sessions or **self** in Advanced before `initiatePayment()`. Its earlier **v4.x.x** example instead uses `GrabPayPaymentMethod` and `GrabPayComponent`. It states no GrabPay-specific Component configuration beyond the illustrated setup. The presence of a method in a response and invoking the Component are not payment-outcome proof. See raw lines 811–866.
- For testing, the guide directs merchants to Adyen Support for test-wallet credentials, then logging into Grab in a simulator with a registered phone number and its one-time password. It directs test-payment status checks in the test Customer Area and a separate live Customer Area request before accepting live GrabPay. These are setup/test instructions, not evidence that any account is eligible or a payment completed. No recurring/token flow, capture or refund procedure is specified on this page; its See also links merely route to separate authorities. See raw lines 868–884.

## Detail locators

- Sessions/Advanced prerequisites and PayLater versus Wallet field scope: raw lines 21–57, 510–517.
- `/sessions` TEST cURL and language samples, return URL and blank country/currency placeholders: raw lines 59–508. Node snippet missing displayed `Config`/`EnvironmentEnum` definitions: lines 266–278 and 457–469.
- `/payments` TEST examples, `grabpay_SG`, blank currency and Java delivery-address omission: raw lines 519–809, especially 575–603.
- Native v5.0.0+ Sessions/Advanced delegates, v4.x.x Component, and no extra configuration: raw lines 811–866.
- Support-provided test credentials, simulator OTP, test status and live request: raw lines 868–877.

## Related

- [[adyen-online-payments]]
- [[adyen-ios-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/grabpay/ios-component/2026-09-15|GrabPay iOS Component guide — captured 2026-09-15]]
