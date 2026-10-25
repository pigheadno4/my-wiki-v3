---
title: "Adyen Napas card iOS Redirect Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/napas-card/ios-component"
raw_files:
  - "adyen/docs/payment-methods/napas-card/ios-component/2026-09-15.md"
tags: [adyen, napas, vietnam, ios, components, cards]
---

## Overview

This [[adyen]] guide adds **Napas card** to an existing iOS Components integration. It identifies a method add-on, version-specific Component examples and test/live steps; it does not supply a full bank/gateway return, `/payments/details` or webhook outcome procedure. See [[adyen-online-payments]], [[adyen-ios-sdk]] and [[source-adyen-docs-payment-methods-napas-card]]. This is a 2026-09-15 snapshot, not proof of current merchant enablement or a successful card payment.

## Key takeaways

- The prerequisites are an existing iOS Components integration and adding Napas card in the **test Customer Area**. The page says no additional Napas-specific request fields, identifies `/sessions` as default for Components **v5.0.0+**, and links `/payments` for an additional use case. It does not state an overall Checkout API minimum or waive ordinary base-flow fields. See raw lines 21–33.
- In the **v5.0.0+** Sessions and Advanced examples, the guide looks up `.other("momo_atm")` and constructs `InstantPaymentComponent`; Sessions delegates to `session`, Advanced to `self`, then invokes `initiatePayment()`. The `momo_atm` identifier is the source's example even though the page calls the method Napas card. The separate Napas overview says Adyen offers these ATM-card payments through partner MoMo, but this guide does not explain the identifier contract; do not silently rename it or assume it covers every Napas product. See raw lines 35–72 and [[source-adyen-docs-payment-methods-napas-card]].
- For **v4.x.x**, the snippet instead uses a generic `PaymentMethod.self` lookup and `Component(...)` presentation, then states no Napas-specific Components configuration is needed. The generic symbols are a source example, not a verified drop-in implementation. Do not transfer the v5 `InstantPaymentComponent` pattern to v4 without separate evidence. See raw lines 74–90.
- The test section gives bank selection and separate test-card/OTP scenarios for **successful, blocked, insufficient-funds and amount-limit** outcomes. These are test fixtures, not real card-processing evidence or a guarantee that submitting credentials produces a particular live result. It directs status checking to the test Customer Area and says a Napas card request must be submitted in **live Customer Area** before live acceptance. This page does not detail where the shopper enters sensitive card/PIN/OTP data; the overview places those steps at the provider gateway. See raw lines 92–105 and [[source-adyen-docs-payment-methods-napas-card]].

## Detail locators

- **Prerequisite, no extra fields and endpoint/version context:** raw lines 21–33.
- **v5+ `momo_atm`, delegates and initiatePayment examples:** raw lines 35–72.
- **v4 generic Component example:** raw lines 74–90.
- **Test scenarios, test status and live request:** raw lines 92–105.

## Related

- [[adyen-online-payments]]
- [[adyen-ios-sdk]]
- [[source-adyen-docs-payment-methods-napas-card]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/napas-card/ios-component/2026-09-15|Napas card iOS Component guide — captured 2026-09-15]]
