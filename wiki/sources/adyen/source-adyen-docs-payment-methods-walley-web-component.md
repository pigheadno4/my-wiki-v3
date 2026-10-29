---
title: "Walley Web Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/walley/web-component"
raw_files:
  - "adyen/docs/payment-methods/walley/web-component/2026-09-15.md"
tags: [adyen, walley, web, components, payments]
---

## Overview

This 2026-09-15 capture describes adding Walley to an existing Adyen Web Components integration. The page covers request fields for `/sessions` and `/payments`, mounting a Walley Component by Web SDK version, and testing Walley payments. Read alongside [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Walley for Web requires Components v3.23.0 or later. The guide says to contact Adyen Support to add Walley in the **test Customer Area** before beginning; this is test setup, not evidence of live enablement. See raw **Requirements**, lines 21–26.
- Both the `/sessions` and `/payments` tables mark `telephoneNumber`, `shopperEmail`, and line item ID, description, amount excluding tax, tax amount, tax percentage, and quantity as required. The phone number must be a working mobile number including country code; missing or incorrect numbers fail Walley's validation. The description has a 50-character maximum. See raw **API reference**, lines 30–62.
- `company.name` is required only for `walley_b2b` payments and is prefilled on Walley's payment form. `company.registrationNumber` is relevant to B2B but not marked required in these tables. See raw **API reference**, lines 38–39 and 55–56.
- The Component configuration creates a DOM container. For v6.0.0 or later, the shown code constructs `new Redirect(checkout, { type: 'walley' })` and mounts it; for v5.x.x or earlier, it uses `checkout.create('walley').mount(...)`. Both snippets use `walley`, identified as the **B2C** method type in the linked Walley overview (raw lines 27–28); neither demonstrates a `walley_b2b` mount. These are version-specific snippets, not an all-version initialization recipe. See this raw **Component configuration**, lines 344–374.
- The test guidance says to send `CivRegNo` as `socialSecurityNumber`, supply company information for B2B tests, and inspect verification payment status in Customer Area. See raw **Test and go live**, lines 376–389.

> [!warning] Example limitations
> The `/payments` language samples leave `paymentMethod.type` empty (lines 72–341), so they do not provide a usable Walley method type. They also pair `countryCode: "NO"` with `currency: "EUR"` (for example lines 77–88). In the curl sample, two quantity-one line items total 872 minor units (331+69+400+72), while the requested amount is 1000 (lines 73–102). This sample is not copy-ready: do not infer Norway/EUR support or valid order reconciliation from it; use the method's geographic and currency rules from the relevant Walley source. The page contains no completed live-payment proof.

## Detail locators

- Required field names and per-field qualifications: raw **API reference → Tab: `/sessions`** and **Tab: `/payments`**, lines 30–62.
- Language-specific `/payments` samples: raw lines 64–342. These are examples with the limitations above.
- Web SDK mount snippets: raw **Component configuration**, lines 344–374.
- Test data and Customer Area status check: raw **Test and go live**, lines 376–389.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-walley]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/walley/web-component/2026-09-15|Walley Web Component, captured 2026-09-15]]
