---
title: "Adyen GrabPay iOS Drop-in integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/grabpay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/grabpay/ios-drop-in/2026-09-15.md"
tags: [adyen, grabpay, ios, drop-in, wallets, paylater]
---

## Overview

This [[adyen]] guide adds GrabPay to an **existing iOS Drop-in** integration with a Sessions or Advanced server-side flow. It covers Customer Area setup, PayLater request data, Drop-in configuration, and TEST/live steps. See [[adyen-online-payments]] and [[adyen-ios-sdk]]. It is a 2026-09-15 documentation snapshot, not proof of current eligibility, a configured merchant account or a completed payment.

## Key takeaways

- The guide starts from an already built **iOS Drop-in** Sessions or Advanced flow and says to add GrabPay in Customer Area before beginning. These are integration prerequisites; the page does not specify a minimum iOS SDK version. See raw lines 21–37.
- For **GrabPay PayLater**, postpaid or installments, the merchant needs to collect and send the delivery address and purchased-item information. Its API tables identify `deliveryAddress` and `lineItems` for both `/sessions` and `/payments`; doing the same for an initial **Wallet** integration is recommended for later PayLater work, not stated as a Wallet requirement. See raw lines 39–57 and 510–517.
- The `/sessions` section calls that route the default for **Web Drop-in v5.0.0 or later**, and the `/payments` section mentions an additional use case or **Web Drop-in before v5.0.0**. This is **Web** wording inside an **iOS** guide. Do not turn it into an iOS SDK/version requirement or infer a definitive endpoint rule for iOS from that wording. The examples show Checkout TEST requests (curl v69 `/sessions`; curl v72 `/payments`) and language-specific library versions, not one global API/SDK minimum. Their currency, country and return URL values are blank placeholders; the `/payments` examples use `grabpay_SG`, which is an example method value, not a universal method selector. See raw lines 50–52, 59–143, 266–311, 510–555 and 557–809.
- Both the **v5.0.0 or later** and **v4.x.x** tabs say there is no required GrabPay-specific Drop-in integration/configuration. This does not waive the existing base flow, Customer Area setup, or PayLater request fields. See raw lines 811–819.
- For testing, the page directs merchants to contact Adyen Support for **test wallet credentials**, log into the Grab simulator using the registered phone and received OTP, then check test-payment status in Customer Area. Before accepting live GrabPay payments, it says to submit a request in the **live Customer Area**. Simulator login, a request or a displayed status is not itself proof of a live successful payment, capture or settlement. See raw lines 821–830.

## Detail locators

- **Sessions/Advanced base prerequisites and Customer Area addition:** raw lines 21–37.
- **PayLater-only extra request fields; Wallet recommendation:** raw lines 39–57 and 510–517.
- **Endpoint/version wording and illustrative TEST snippets:** raw lines 50–52, 59–508 and 510–809.
- **Drop-in configuration tabs:** raw lines 811–819.
- **TEST credentials, simulator and live request:** raw lines 821–830.

## Related

- [[adyen-online-payments]]
- [[adyen-ios-sdk]]
- [[source-adyen-docs-payment-methods-grabpay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/grabpay/ios-drop-in/2026-09-15|GrabPay iOS Drop-in guide — captured 2026-09-15]]
