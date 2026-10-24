---
title: "PayPay for API only"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay/api-only"
raw_files:
  - "adyen/docs/payment-methods/paypay/api-only/2026-09-15.md"
tags: [adyen, paypay, api-only, redirect, japan]
---

## Overview

This 2026-09-15 Adyen guide describes adding PayPay to an **existing API-only integration**. It requires redirect handling and Customer Area method setup, shows JP/JPY payment-method discovery, and gives TEST simulator versus LIVE app/IP instructions. It is an add-on guide, not evidence that any merchant is enabled or transaction succeeded. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Prerequisites are an existing API-only Advanced/Web integration, redirect handling for `action.type: redirect`, and PayPay added in Customer Area. The merchant builds the payment form; the page links its base request/redirect behavior to the main integration guide. (raw lines 19–29, 31–42)
- For `/paymentMethods`, the guide specifies `countryCode: JP`, `amount.currency: JPY`, and `amount.value` in minor units so PayPay can appear. The TEST v72 example illustrates those values and a response `paymentMethod.type: paypay`; it does not establish current merchant eligibility or a mandatory API-version floor. `shopperLocale: jp-JP` appears in the example, not in the stated parameter table. (raw lines 44–84)
- The numbered flow says to include additional information about purchase items in the payment request, but both the payment-form and `/payments` sections state that no extra parameters are needed. This unresolved prose conflict matters for item-data requirements; do not infer an item schema or treat the no-extra-parameters sentence as settling it. The flow also places fulfillment after the payment-request step without showing a final result, so that sequence is not proof of authorization or a safe fulfillment trigger. (raw lines 31–40, 86–88)
- In TEST, the page names two DGFT acquirer accounts (AUTHFlow and SALEFlow) and says the redirect leads to a DGFT simulator, without needing the PayPay app. It points to test Customer Area for status checks. For LIVE integration, it states that an activated PayPay smartphone app must be accessed through a Japan local IP address. These are environment-specific instructions, not live approval or payment, capture, settlement, or webhook proof. (raw lines 90–101)
- The curl discovery illustration has `-X POST` followed immediately by `-d` on the next line without a continuation slash. Treat that shell snippet as illustrative and verify syntax before reuse. (raw lines 56–70)

## Detail locators

- API-only/redirect/Customer Area prerequisites and abbreviated flow: raw lines 19–42.
- JP/JPY discovery parameters and TEST v72 response example: raw lines 44–84.
- Contradictory item-information versus no-extra-parameters wording: raw lines 31–40 and 86–88.
- TEST simulator accounts/status and LIVE app/Japan-IP condition: raw lines 90–101.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paypay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/api-only/2026-09-15|Adyen PayPay API-only, 2026-09-15 snapshot]]
