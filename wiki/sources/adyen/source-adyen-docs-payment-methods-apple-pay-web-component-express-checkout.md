---
title: "Adyen Apple Pay Web Component express checkout"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/web-component/express-checkout"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/web-component/express-checkout/2026-09-15.md"
tags: [adyen, apple-pay, web-component, express-checkout]
---

## Overview

This [[adyen]] guide adds an **Apple Pay express checkout** option to an existing **Advanced-flow Web Components v6** integration. The button can request shopper billing/shipping contact details to prefill checkout, while callbacks adjust displayed shipping choices and totals. It presumes Apple Pay is added in Customer Area, an Apple Pay certificate is set up with Adyen or the merchant, and the base Apple Pay Web Component integration exists. The page is an add-on, not a complete server payment or outcome flow. [[adyen-online-payments]]

## Key takeaways

- The guide says **v6.10.0+** of the Component can offer Apple Pay on supported third-party browsers; earlier versions have device/browser compatibility limits delegated to another guide. It requires the **API Clientside Encryption Payments role for live processing** and separately routes live certificate/domain setup to the Apple Pay Web Component guide. The page does not establish availability for a particular browser, shopper, merchant, or certificate. See raw lines 27–35 and 230–234.
- Express configuration sets `isExpress: true`; `requiredBillingContactFields` allows only `postalAddress` here, while the example asks for shipping postal address, name, phonetic name, phone, and email. Its `countryCode: 'US'` is an example value, not a universal country restriction. The flow says to check `isAvailable()` before mounting, which is a client availability check, not authorization or live-account proof. See raw lines 39–89 and 201–218.
- For **shipping-address changes**, the callback receives the selected contact and should return updated line items, shipping methods and total, or an error for a rejected address. For **shipping-method changes**, it returns updated line items and total. The examples write a new total to `ApplePayAmountHelper` client application state. They do **not** show recalculating and authorizing a matching amount on the merchant server or updating the eventual payment request, so the examples alone cannot establish charged-amount consistency. See raw lines 91–179 and 272–319.
- `onAuthorized` receives Apple Pay shopper information **before** `onSubmit`; the handler must resolve or reject to continue. Its name describes a wallet event here, not final Adyen payment authorization. The sample logs raw/preformatted data and immediately resolves, but the prose calls for checks before continuing. Do not treat that log line or automatic resolution as a privacy-reviewed validation implementation. The page contains no final payment-status or webhook/capture/settlement procedure. See raw lines 181–199 and 321–327.
- The examples are schematic and internally inconsistent: the shipping-contact update table says `newShippingMethod` (singular) while code sends `newShippingMethods` (plural); the mount fragments alternate `applePay`, `applepay`, and `applePayComponent`, though only `applepay` is defined in the combined sample. Helpers such as `fetchNewShippingMethods` and `createApplePayTotal` are placeholders. Verify actual API names and implement validation/amount synchronization in the base integration before use. See raw lines 99–105, 110–140, 203–218, and 260–338.
- Testing uses Apple's sandbox test cards and Adyen Customer Area test status; live use has the separate API-role and Apple Pay certificate go-live steps. Test-card display or `isAvailable()` is not proof of a successful live authorization or capture. See raw lines 220–234.

## Detail locators

- Required integration, browser-version and certificate prerequisites: raw lines 25–35.
- Express contact fields and client event/update examples: raw lines 67–199.
- Availability/mount and test/live gate: raw lines 201–234.
- Consolidated HTML/JavaScript example with name mismatches: raw lines 236–339.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-apple-pay-web-component]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/web-component/express-checkout/2026-09-15|Adyen Apple Pay Web express checkout snapshot]]
