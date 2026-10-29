---
title: "Adyen Klarna Android Drop-in v5 integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/klarna/android-drop-in/2026-09-15.md"
tags: [adyen, klarna, android, drop-in, online-payments]
---

## Overview

This [[adyen]] guide is a short **Android Drop-in v5.0.0** method add-on for Klarna. It routes the merchant to an existing Sessions or Advanced Android Drop-in integration and states that the ordinary request and Drop-in configuration need no extra Klarna-specific additions. The page identifies v5.0.0 as released in October 2023 and directs earlier versions to a separate guide. It does not describe the full payment, redirect, capture or recurring flow; follow the base integration and the product overview through [[adyen-online-payments]].

## Key takeaways

- **Version and base-flow gate:** This page is explicitly for Android Drop-in v5.0.0; the separate earlier-versions guide is for older integrations (raw lines 19–21). Both Sessions and Advanced tabs require the corresponding existing Android Drop-in flow at minimum v5.0.0 and Klarna added in Customer Area (raw lines 23–39).
- **Narrow method additions:** For the ordinary Sessions `/sessions` and Advanced `/payments` calls, Klarna requires no additional fields according to this guide (raw lines 41–49). For either flow, it requires no extra Drop-in configuration, then routes to creating a checkout session or launching Drop-in under the respective base guide (raw lines 51–67). This is a method-specific add-on statement, not a waiver of fields or handling required by the base flow or a Klarna product.
- **Test and live gates:** The page calls for testing with Klarna sample data, checking test payments in test Customer Area, adding Klarna in live Customer Area, reviewing legal/privacy and presentation guidance, checking invoice lines/VAT, and offering another method on rejection (raw lines 69–84). Shopper name and address are described as optional request data that improve experience and conversion, not required by this page (raw line 84).
- **Live-test refusal warning:** Its live testing section calls for real shopper data and a reasonable product amount, and warns against repeated tests from the same device or IP. It says unmet conditions can return `Refused` and show “Option Not Available,” while these checks are bypassed in test (raw lines 86–96). This is guidance about documented live checks, not evidence of a successful live transaction.

## Detail locators

- Page version and earlier-version route: pinned raw lines 15–21.
- Sessions/Advanced prerequisites: pinned raw lines 23–39.
- Ordinary request and Drop-in configuration: pinned raw lines 41–67.
- Test/live checklist and refusal conditions: pinned raw lines 69–96.

## Related

- [[adyen-online-payments]] — provider online checkout context and reciprocal route.
- [[source-adyen-docs-payment-methods-klarna]] — product-level methods and qualifications.
- [[source-adyen-docs-payment-methods-klarna-android-drop-in-earlier-versions]] — separate pre-v5 guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/android-drop-in/2026-09-15|Klarna Android Drop-in v5 guide, captured 2026-09-15]]
