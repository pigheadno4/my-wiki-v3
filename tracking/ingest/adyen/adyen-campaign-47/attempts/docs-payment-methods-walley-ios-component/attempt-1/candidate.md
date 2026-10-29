---
title: "Adyen Walley iOS Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/walley/ios-component"
raw_files:
  - "adyen/docs/payment-methods/walley/ios-component/2026-09-15.md"
tags: [adyen, walley, ios, components, sessions, advanced-flow, online-payments]
---

## Overview

This captured [[adyen]] guide adds Walley to an existing iOS Components integration. It lists Walley-specific fields for `/sessions` and `/payments`, shows v5+ versus v4.x.x Component setup, and points to test scenarios. Its requirements say Walley works with all Component versions, but the setup examples are version-specific; the page does not demonstrate a complete redirect/result lifecycle or live acceptance. [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and fields:** The guide requires an existing iOS Components integration and contacting Support to add Walley in test Customer Area. Both endpoint tables mark a working mobile `telephoneNumber` with country code, `shopperEmail`, and line-item ID, description, amount excluding tax, tax amount, tax percentage and quantity required. Description maximum is 50 characters. `company.name` is marked required **only for `walley_b2b`** and is prefilled on Walley's form; `company.registrationNumber` is relevant to B2B but its Required cell is blank. These table requirements are Walley-specific additions to the respective base flow (raw lines 21–62).
- **Versioned UI configuration:** For iOS Components v5.0.0 or later, the Sessions tab finds `.other("walley")`, creates `InstantPaymentComponent`, assigns the session as delegate and calls `initiatePayment()`. The Advanced tab uses the same B2C method lookup and component but assigns `self` as delegate. For v4.x.x, the example uses `WalleyPaymentMethod`, `WalleyComponent`, and `present(component)`. The page then says there are no further Walley-specific configuration steps. These snippets look up `walley`, not `walley_b2b`; they do not show a B2B Component lookup (raw lines 344–399).
- **Payment examples need verification:** The `/payments` examples set `paymentMethod.type` to an empty string, even though this is a Walley integration page, so they cannot be copied as complete method requests. They also show `countryCode: NO` with `EUR`; the related earlier Android Walley guide explicitly pairs NO with NOK in its discovery table, while the overview lists countries and currencies without a pairing. Do not infer this NO/EUR sample is an approved Norway setup. The curl line items do not visibly reconcile to the 1000 request amount, and language examples vary in item count. Use the actual method type, country/currency and order figures from the applicable integration evidence (raw lines 64–100, 106–343).
- **Testing scope:** Walley test-scenario guidance includes `CivRegNo` in `socialSecurityNumber` and a company name/registration example for B2B testing, with verification status in test Customer Area. This page provides no live enablement step or proof of actual transaction success (raw lines 401–414).

## Detail locators

- Identity, setup and Sessions/Payments field tables: pinned raw lines 15–62.
- Payments code samples and their blank method-type values: pinned raw lines 64–343.
- iOS v5+ Sessions/Advanced versus v4.x.x Component setup: pinned raw lines 344–399.
- Test data and related base guides: pinned raw lines 401–421.

## Related

- [[adyen-online-payments]] — provider online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-walley]] — captured Walley overview for product/country context.
- [[source-adyen-docs-payment-methods-walley-android-drop-in-earlier-versions]] — captured Android guide with an explicit Nordic country/currency discovery table; platform-specific procedures remain distinct.

## Raw Sources

- [[raw/adyen/docs/payment-methods/walley/ios-component/2026-09-15|Walley iOS Component, captured 2026-09-15]]
