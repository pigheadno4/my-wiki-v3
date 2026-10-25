---
title: "Adyen FPX Online Banking Malaysia Android Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/fpx-online-banking-malaysia/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/fpx-online-banking-malaysia/android-drop-in/2026-09-15.md"
tags: [adyen, fpx, online-banking, malaysia, android, drop-in]
---

## Overview

This 2026-09-15 Adyen guide adds FPX Online Banking Malaysia to an existing Android Drop-in integration, with separate Sessions and Advanced server-side paths. It describes only method-specific additions; base Drop-in flow and outcome handling require their own guides. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia]] for the method overview.

## Key takeaways

- Sessions requires an existing Android Drop-in Sessions flow using Checkout API v68 or later, plus adding FPX Online Banking Malaysia in Customer Area. The guide says no additional `/sessions` parameters or FPX-specific configuration are needed.
- Advanced requires an existing Android Drop-in Advanced flow, redirect handling for `action.type: redirect`, and Customer Area setup. The guide says no FPX-specific configuration or additional `/payments` parameters are needed. These statements are limited to this Drop-in add-on, not the full base-flow request contract.
- For both paths, the test instructions refer to issuer IDs available for the Online Banking Malaysia Component for the applicable country/region and checking test payment status in the test Customer Area; this page does not enumerate those IDs. Accepting live payments requires a separate request in the live Customer Area. A test or redirect instruction does not establish a final authorization, settlement, or an actual merchant's enablement.

## Detail locators

- Sessions prerequisites, no additional `/sessions` fields, and no method-specific configuration: pinned raw lines 25–46.
- Sessions test and live instructions: lines 48–56.
- Advanced prerequisites and redirect action: lines 58–66; no extra configuration or `/payments` fields: lines 68–78.
- Advanced test and live instructions: lines 80–86.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/android-drop-in/2026-09-15|FPX Malaysia Android Drop-in, 2026-09-15]]
