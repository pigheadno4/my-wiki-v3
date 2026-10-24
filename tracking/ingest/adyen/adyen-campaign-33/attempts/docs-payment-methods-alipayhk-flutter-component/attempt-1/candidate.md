---
title: "Alipay HK Flutter Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/flutter-component/2026-09-15.md"
tags: [adyen, alipayhk, flutter, components, redirect]
---

## Overview

This 2026-09-15 Adyen guide describes Alipay HK-specific additions to an **existing Flutter Components integration**, split between Sessions and Advanced server-side flows. The linked main integration guides own the base flow and redirect completion. The page's setup steps and test details are not payment-outcome evidence. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** requires an existing Flutter Components Sessions flow, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and Alipay HK added in Customer Area. It states no additional Alipay HK-specific `/sessions` or configuration parameters are needed. (raw lines 25–46)
- **Advanced:** requires an existing Flutter Components Advanced flow, redirect handling for `action.type: redirect`, and Alipay HK added in Customer Area. It states no additional Alipay HK-specific configuration or `/payments` parameters are needed. Its section states no Checkout API minimum; the v68 gate appears in Sessions only. (raw lines 60–82)
- Both **Integration type** rows label Flutter **Components**, but their embedded URLs point to `integration=Drop-in`; the Sessions row additionally points to `advanced-flow`. The separate redirect and create-payment links specify Components with their respective flow. Do not use the mismatched prerequisite URLs as evidence that this is a Drop-in guide or that Sessions uses Advanced flow. (raw lines 31–40, 68–82)
- Both sections supply AlipayHK test credentials and direct readers to the **test Customer Area** payment list for test-payment status. A **live Customer Area** request for AlipayHK is separately required before live acceptance. These instructions do not establish account approval, redirect return, final webhook, authorization, capture or settlement. (raw lines 48–58, 84–94)

## Detail locators

- Sessions prerequisites, redirect, no-extra request/configuration: raw lines 25–46.
- Sessions test credentials/status and live request: raw lines 48–58.
- Advanced prerequisites, redirect, no-extra configuration/payment fields: raw lines 60–82.
- Advanced test credentials/status and live request: raw lines 84–94.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipayhk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/flutter-component/2026-09-15|Adyen Alipay HK Flutter Component, 2026-09-15 snapshot]]
