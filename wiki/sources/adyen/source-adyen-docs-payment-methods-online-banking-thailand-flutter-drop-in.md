---
title: "Adyen Online banking Thailand Flutter Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-thailand/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-thailand/flutter-drop-in/2026-09-15.md"
tags: [adyen, online-banking, thailand, flutter, drop-in]
---

## Overview

This 2026-09-15 Adyen page gives method-specific additions for **Online banking Thailand** in an existing Flutter Drop-in integration, split into Sessions and Advanced server-side flows. Both sections require redirect handling and say no method-specific request or configuration parameters are needed. It does not constitute a complete integration or proof of an executed bank payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions requirements:** The Sessions row calls for an existing Flutter Drop-in Sessions integration, Checkout API v68 or later and handling `action.type: redirect`. Its integration-type link nonetheless points to an `advanced-flow` URL; the redirect link points to Sessions. Its setup row says to contact Adyen Support to add the method in Customer Area. No extra `/sessions` or method configuration parameters are specified. (raw lines 25–48)
- **Advanced requirements:** The Advanced section calls for an existing Flutter Drop-in Advanced integration and redirect handling. Here the setup row says to add the method in Customer Area, unlike the Sessions Support instruction. It says no extra method configuration or `/payments` parameters are needed. This section gives no Checkout API minimum. (raw lines 58–80)
- **Testing and live:** Both sections instruct use of an issuer ID available for the respective country/region, then checking test payment status in Customer Area. They separately require a request in the live Customer Area before live acceptance. The test text says “Component” even though this is a Drop-in page, and no issuer-ID list appears here. Neither test instructions nor the live request establishes merchant approval or a final authorization/settlement result. (raw lines 50–56, 82–88)

## Detail locators

- Sessions prerequisite URL mismatch, API version, redirect and Support setup: raw lines 25–36.
- Sessions request/configuration additions: raw lines 38–48.
- Advanced prerequisites and distinct Customer Area setup: raw lines 58–68.
- Advanced configuration and request additions: raw lines 70–80.
- Repeated test/live guidance: raw lines 50–56 and 82–88.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-thailand/flutter-drop-in/2026-09-15|Adyen Thailand online-banking Flutter Drop-in, 2026-09-15 snapshot]]
