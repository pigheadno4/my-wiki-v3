---
title: "Adyen Affirm iOS Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/affirm/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/affirm/ios-drop-in/2026-09-15.md"
tags: [adyen, affirm, ios, drop-in, online-payments]
---

## Overview

Adyen's Affirm add-on guide for an existing **iOS Drop-in** integration. It presents both Sessions and Advanced server-side prerequisites: build the corresponding iOS Drop-in integration and add Affirm in the Customer Area before beginning. This is integration documentation, not evidence of merchant enablement, shopper financing eligibility, or a successful live payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The API reference says `/sessions` is the default with Drop-in v5.0.0 or later; its `/payments` tab is for an additional use case. Both tables mark shopper name, telephone number, and email as required. `countryCode` is required for transactions in Canada or the UK because omission defaults to US. For Canadian and US addresses, `stateOrProvince` is required, while it is optional for UK addresses; a missing delivery address defaults to billing address. Line items are optional but recommended by the page to improve approval rates. See raw lines 39–56 and 758–771.
- The copied request examples illustrate US/USD test calls: `/sessions` at Checkout API v69 and `/payments` at v72, with an `affirm` payment-method type in the latter. These are examples, not a platform availability or transaction guarantee. The displayed curl bodies contain annotation text embedded in the `billingAddress` and `deliveryAddress` property names, so they should not be copied as literal JSON. See raw lines 58–117 and 773–835.
- The optional configuration section describes `allowedCountries` (default US/CA; example adds GB), prefilled personal/address data, and field visibility (`hidden`, `readOnly`, `editable`; read-only fields need matching prefilled information). **Scope conflict:** although this page is labeled iOS, this section links to a Web Drop-in guide and uses TypeScript/JavaScript `AdyenCheckout`/`Dropin` mounting examples. Treat those snippets as Web-oriented examples, not established iOS SDK configuration. See raw lines 1251–1384.
- After goods are sent, the page says to capture within 28 days or the authorization expires; capture starts the shopper's installment schedule. For an order fulfilled at a lower amount, its stated procedure is full capture followed by a refund of the difference. Test credentials come from Affirm; live acceptance additionally requires an Affirm request in the live Customer Area and Affirm live credentials. See raw lines 1386–1398.

## Detail locators

- Requirements and method setup: raw lines 21–37.
- Sessions parameters and request examples: raw lines 39–756.
- Payments parameters and request examples: raw lines 758–1249. Some copied library examples show Web channel despite the iOS title; use the iOS integration guide for platform-specific implementation.
- Optional configuration, Web example mismatch, capture, and go-live conditions: raw lines 1251–1398.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/affirm/ios-drop-in/2026-09-15|Affirm iOS Drop-in documentation capture (2026-09-15)]]
