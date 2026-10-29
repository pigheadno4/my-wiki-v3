---
title: "Adyen Walley iOS Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/walley/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/walley/ios-drop-in/2026-09-15.md"
tags: [adyen, walley, ios, drop-in, sessions, advanced-flow]
---

## Overview

This 2026-09-15-captured Adyen guide adds Walley to an existing iOS Drop-in integration. It says Walley works with all iOS Drop-in versions, links a Sessions base integration, and gives required request fields in both `/sessions` and `/payments` tabs. It does not provide a complete payment lifecycle. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-walley]] for the B2C/B2B method types and regional overview.

## Key takeaways

- Build the iOS Drop-in integration first and contact Adyen Support to add Walley in the **test** Customer Area. The page says Walley works with all versions of iOS Drop-in. Its two Drop-in configuration tabs (v5.0.0 or later and v4.x.x) specify no required Walley-specific Drop-in integration. See raw lines 21–26 and 344–352.
- For both `/sessions` and `/payments`, the tables mark `telephoneNumber` and `shopperEmail` required. Collect a working mobile number including country code: the page says incorrect or missing numbers fail Walley validation. `company.name` is required **only for `walley_b2b`**; `company.registrationNumber` is relevant to B2B but is not marked required. See raw lines 30–39 and 47–56.
- Each table also marks `lineItems.id`, `description`, `amountExcludingTax`, `taxAmount`, `taxPercentage`, and `quantity` required; description has a 50-character maximum, and the amount/tax fields use minor units. See raw lines 40–45 and 57–62.
- The TEST v72 `/payments` snippets are illustrative: `paymentMethod.type` is an empty string, the sample uses `countryCode: NO`, `currency: EUR`, a `+46` telephone number, and an HTTPS `returnUrl`. Do not copy the blank type or treat that sample combination/URL as verified iOS or regional eligibility. The example line items also do not reconcile to the example `amount.value: 1000`. Use the Walley overview for distinct `walley` and `walley_b2b` types, and configure the actual iOS return path. See raw lines 64–104 and the related overview.
- For testing, the page points to Walley's test scenarios through Adyen `/payments`, maps Walley `CivRegNo` to `socialSecurityNumber`, and shows a B2B company object. It points to test Customer Area payment status; it does not document live account activation or prove a successful payment. See raw lines 354–367.

## Detail locators

- Existing iOS Drop-in and test Support setup: raw lines 21–26.
- `/sessions` and `/payments` field tables: raw lines 28–62.
- TEST `/payments` examples and blank method type: raw lines 64–343.
- Versioned Drop-in configuration tabs: raw lines 344–352.
- Test-data mapping and test Customer Area status route: raw lines 354–367.
- Base integration, webhooks, tokenization, and API Explorer navigation: raw lines 369–374. These links alone do not assert Walley-specific recurring or webhook behavior.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-walley]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/walley/ios-drop-in/2026-09-15|Fully read Walley iOS Drop-in raw]]
