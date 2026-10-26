---
title: "Adyen BLIK Android Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/blik/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/blik/android-drop-in/2026-09-15.md"
tags: [adyen, blik, android, drop-in, sessions, advanced]
---

## Overview

Adyen's 2026-09-15 BLIK Android Drop-in page is a method add-on for an existing Android Drop-in integration. It identifies itself as the v5.0.0 guide, released in October 2023, and sends earlier versions to a separate guide. It covers Sessions and Advanced prerequisites, method-specific field/configuration absence, TEST-code checks and a live Customer Area gate. See [[adyen]] and [[adyen-android-sdk]].

## Key takeaways

- For either Sessions or Advanced flow, the page requires an existing Android Drop-in integration at minimum v5.0.0 and BLIK added in the Customer Area before integration. Its historical version boundary routes earlier versions to [[source-adyen-docs-payment-methods-blik-android-drop-in-earlier-versions]]; the older guide is separate authority (raw lines 21-39).
- The method adds no BLIK-specific fields to the ordinary Sessions `/sessions` or Advanced `/payments` request, and no BLIK-specific Drop-in configuration in either flow. The page then routes Sessions to checkout-session creation and Advanced to launching Drop-in (raw lines 41-67). These statements presume the base integration and do not waive its general requirements.
- For a BLIK-with-code TEST payment, the page says to use code `999000`, meet BLIK's guidelines and test end to end. Before accepting live BLIK, add it in the live Customer Area (raw lines 69-79). The test code and setup instructions do not prove current merchant eligibility or a successful payment.
- This page does not specify the shopper's BLIK code-entry/approval steps, response codes, webhook finality, capture or settlement. Those behaviors should not be inferred from the method-addition instructions or the TEST code (raw lines 15-85).

## Detail locators

- Scope, v5.0.0 and earlier-version route: raw lines 15-21.
- Sessions/Advanced prerequisites and Customer Area setup: raw lines 23-39.
- No extra method request fields/configuration, flow continuation: raw lines 41-67.
- TEST code, guideline/end-to-end check and live setup: raw lines 69-79.

## Related

- [[source-adyen-docs-payment-methods-blik-android-drop-in-earlier-versions]] — historical earlier-version route.

## Raw Sources

- [[raw/adyen/docs/payment-methods/blik/android-drop-in/2026-09-15|BLIK Android Drop-in v5.0.0 guide (2026-09-15 snapshot)]]
