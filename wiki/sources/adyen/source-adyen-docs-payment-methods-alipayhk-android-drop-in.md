---
title: "Alipay HK Android Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/android-drop-in/2026-09-15.md"
tags: [adyen, alipayhk, android, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen guide describes Alipay HK-specific additions to an **existing Android Drop-in integration**, in separate Sessions and Advanced server-side flow sections. The page points to main integration guides for the base payment lifecycle and gives no completed transaction result. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** requires an existing Android Drop-in Sessions flow with **Checkout API v68 or later** and Alipay HK added in Customer Area. It says no additional Alipay HK-specific `/sessions` or configuration parameters are needed. This Sessions requirements table does **not** itself include a redirect-handling row; do not attribute the Advanced row to Sessions as an explicit statement on this page. (raw lines 25–46)
- **Advanced:** requires an existing Android Drop-in Advanced flow, redirect handling for `action.type: redirect`, and Alipay HK added in Customer Area. It says no additional Alipay HK-specific configuration or `/payments` parameters are needed. This section does not state a Checkout API minimum; the v68 wording appears in Sessions only. (raw lines 62–82)
- Both sections provide AlipayHK **test** credentials and point to the **test Customer Area** payment list for test-payment status. A request for AlipayHK in the **live Customer Area** is separately needed before live acceptance. These instructions do not establish live approval or authorization, capture, settlement, refund or final webhook status. (raw lines 48–60, 84–94)
- The guide supplies no Android code, shopper return procedure or outcome handling specific to Alipay HK. The method-specific no-extra-fields statements leave the base integration's required fields and flow in the linked main guides. (raw lines 19–23, 36–46, 72–82)

## Detail locators

- Sessions requirements and no-extra request/configuration statements: raw lines 25–46.
- Sessions test credentials/status lookup and live request: raw lines 48–60.
- Advanced redirect prerequisite and no-extra request/configuration statements: raw lines 62–82.
- Advanced test credentials/status lookup and live request: raw lines 84–94.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipayhk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/android-drop-in/2026-09-15|Adyen Alipay HK Android Drop-in, 2026-09-15 snapshot]]
