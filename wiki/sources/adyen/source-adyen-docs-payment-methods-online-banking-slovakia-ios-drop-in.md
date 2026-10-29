---
title: "Adyen Online banking Slovakia iOS Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-slovakia/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-slovakia/ios-drop-in/2026-09-15.md"
tags: [adyen, online-banking-slovakia, ios, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds Online banking Slovakia to an existing iOS Drop-in integration. It covers Sessions and Advanced flow additions, with Advanced issuer selection and bank redirect handling. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-slovakia]] for the separate SK/EUR method overview.

## Key takeaways

- **Sessions:** use an existing iOS Drop-in Sessions flow with **Checkout API v68 or later** and add Online banking Slovakia in Customer Area. The page says no additional method parameters are needed for `/sessions` and no extra method configuration is needed. Base integration requirements still apply. See raw lines 25–56.
- **Advanced:** use an existing iOS Drop-in Advanced flow, add the method in Customer Area, and handle `action.type: redirect`. No additional method configuration is specified. The `/payments` addition marks `paymentMethod.issuer` required as the shopper-selected issuing bank. The TEST v72 examples use `paymentMethod.type: onlineBanking_SK`, issuer `cs`, EUR and an HTTPS `returnUrl`; `cs` and the URL are examples, not a universal issuer or native-app callback. The v68 minimum appears only in the Sessions requirements row on this page. See raw lines 58–107.
- The page says to test with **real payment details and small amounts**, check test Customer Area **Payments > Payment list**, and add the method in Customer Area to accept live payments. That is a historical instruction, not evidence of a completed test, current merchant eligibility, or live operation. See raw lines 50–56 and 398–406.
- Example-library details are versioned separately and should not be mixed into the method requirement: the Go block labels library v10.4.0 but imports `/v9/` paths. Use the SDK version actually in the integration. See raw lines 263–272.

## Detail locators

- Sessions prerequisites, no extra request/configuration parameters, and test/live: raw lines 25–56.
- Advanced prerequisites, redirect requirement, issuer field and TEST curl example: raw lines 58–107.
- Language-specific TEST request examples: raw lines 109–396.
- Repeated test/live instructions: raw lines 398–406.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-slovakia]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-slovakia/ios-drop-in/2026-09-15|Fully read Online banking Slovakia iOS Drop-in raw]]
