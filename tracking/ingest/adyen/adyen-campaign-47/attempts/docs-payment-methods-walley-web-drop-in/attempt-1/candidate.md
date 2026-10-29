---
title: "Adyen Walley Web Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/walley/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/walley/web-drop-in/2026-09-15.md"
tags: [adyen, walley, web, drop-in, sessions, advanced-flow, online-payments]
---

## Overview

This captured [[adyen]] guide adds Walley to an existing Web Drop-in integration. It gives Walley-specific `/sessions` and `/payments` request fields, says no extra Walley Drop-in configuration is required, and points to test scenarios. It does not describe a full redirect/result lifecycle or prove merchant live enablement. [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and fields:** The page requires Web Drop-in **v3.23.0 or later** and contacting Support to add Walley in **test** Customer Area. Both endpoint tables mark a working mobile `telephoneNumber` with country code, `shopperEmail`, and line-item ID, description, amount excluding tax, tax amount, tax percentage, and quantity required. The description maximum is 50 characters. `company.name` is required **only for `walley_b2b`** and prefilled on Walley's form; `company.registrationNumber` is B2B-relevant but its Required cell is blank (raw lines 21–62).
- **No method-specific Drop-in configuration:** The page says Walley needs no extra Drop-in configuration steps. This concerns method-specific settings; the existing base integration and request fields still apply (raw lines 344–346).
- **Payment sample warning:** The `/payments` examples across languages set `paymentMethod.type` to an empty string, so they do not provide a copy-ready Walley method request. They show `countryCode: NO` with `EUR` and differing line-item counts/values; this page does not itself validate that combination or a particular order total. Use the applicable method type and real order/country data rather than treating these test snippets as normative (raw lines 64–343).
- **Testing scope:** Walley test scenarios are referenced through Walley's technical docs. This page says to include `CivRegNo` as `socialSecurityNumber` and gives company name/registration data for a B2B test, with verification status in test Customer Area. It does not claim that a test scenario proves live operation (raw lines 348–361).

## Detail locators

- Identity, v3.23.0 prerequisite and Sessions/Payments field tables: pinned raw lines 15–62.
- Payment examples, including blank method types: pinned raw lines 64–343.
- No-extra-configuration statement, test data and related routes: pinned raw lines 344–367.

## Related

- [[adyen-online-payments]] — provider online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-walley]] — captured Walley product overview for product and region context; this Web page supplies the Drop-in-specific fields.

## Raw Sources

- [[raw/adyen/docs/payment-methods/walley/web-drop-in/2026-09-15|Walley Web Drop-in, captured 2026-09-15]]
