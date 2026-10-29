---
title: "Klarna Android Component integration | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/android-component"
raw_files:
  - "adyen/docs/payment-methods/klarna/android-component/2026-09-15.md"
tags: [adyen, klarna, android, components, checkout]
---

## Overview

This 2026-09-15 Adyen Docs page is a short add-on for an **existing Android Components Klarna integration**, scoped to Components **v5.0.0 or later** and either Sessions or Advanced server-side flow. It points earlier versions to a separate guide. See [[adyen-online-payments]], [[source-adyen-docs-payment-methods-klarna]], [[source-adyen-docs-payment-methods-klarna-android-component-earlier-versions]] and [[adyen]].

## Key takeaways

- Both flow tabs require a built Android Components base integration of at least v5.0.0 and adding Klarna in Customer Area before setup. Select the matching server-side flow; this page is an add-on rather than a full payment, return or webhook recipe (raw lines 23–39).
- In this Android add-on, Adyen says Klarna requires **no additional fields** for either the Sessions `/sessions` request or Advanced `/payments` request, and **no additional Component configuration** in either flow. This is scoped to additions on top of the linked base integration, not a statement that the underlying API requests contain no required data (lines 41–59). After configuration, Sessions creates a checkout session; Advanced launches and shows the Component (lines 61–67).
- Before live payments, the guide directs testing with Klarna's test data and checking test status in Customer Area. Its live checklist includes live Customer Area addition, legal/privacy and presentation guidance, correct invoice lines and VAT, an alternative method for shoppers rejected by Klarna, and **optional** name/address data to improve experience (lines 69–84).
- The live-testing section says to use real shopper data, an item meeting Klarna's minimum amount, and avoid repeated tests from one device/IP in a short period. Its GBP 1 Pay over time amount is explicitly an **example**, not a universal product or country minimum. Violating the conditions can produce `Refused` and an “Option Not Available” page; the guide says those checks are bypassed in test and applied live (lines 86–96). The page does not document a successful live payment, capture or settlement for any merchant.

## Detail locators

- Version/earlier-version split: opening text, lines 15–21.
- Sessions and Advanced prerequisites: `## Requirements`, lines 23–39.
- No additional Klarna-specific request fields/configuration and next base-flow links: `## API reference` and `## Klarna Configuration`, lines 41–67.
- Test and live preparation, optional name/address, refusal conditions and raw-response route: `## Test and go live`, lines 69–96.

## Related

- [[adyen-online-payments]] — provider online-payment concept and base architecture.
- [[source-adyen-docs-payment-methods-klarna]] — product and country/currency overview; this child does not establish eligibility.
- [[source-adyen-docs-payment-methods-klarna-android-component-earlier-versions]] — separate v4.x.x Android Component guide.
- [[source-adyen-docs-payment-methods-klarna-raw-responses]] — diagnostic response reference linked by this guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/android-component/2026-09-15|2026-09-15 Klarna Android Component v5.0.0+ add-on]]
