---
title: "Adyen Alipay HK iOS Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/ios-drop-in/2026-09-15.md"
tags: [adyen, alipayhk, ios, drop-in]
---

## Overview

This [[adyen]] guide adds Alipay HK to an existing **iOS Drop-in** integration, separating method-specific additions for **Sessions** and **Advanced** server-side flows. Its “no additional parameters” wording is scoped to Alipay HK and does not replace the base integration's requests or result handling. A configured method or test payment-list entry is not evidence of authorization, capture or settlement. [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The page requires an existing iOS Drop-in Sessions flow, **Checkout API v68 or later**, and Alipay HK added in Customer Area. It says no additional Alipay HK `/sessions` or configuration parameters are needed. The Sessions requirements table does **not** separately list redirect handling; that flow's action handling belongs to the linked main guide. See raw lines 25–46.
- **Advanced:** The section requires an existing iOS Drop-in Advanced flow, explicit `action.type: redirect` handling and Alipay HK added in Customer Area. It says no additional Alipay HK configuration or `/payments` parameters are needed. It does not restate the Sessions section's v68+ requirement as an Advanced-specific minimum. See raw lines 62–84.
- **TEST/LIVE:** Both sections give a test username/PIN pair and direct readers to the test Customer Area payment list for test status; the raw lines contain the exact fixture values. Before accepting live Alipay HK payments, the page says to submit a separate request in **live Customer Area**. Test credentials are not live credentials, and submission does not establish live approval or payment success. See raw lines 48–60 and 86–98.

## Detail locators

- Sessions prerequisites and method-specific request/configuration: raw lines 25–46.
- Advanced prerequisites, redirect and method-specific request/configuration: raw lines 62–84.
- Duplicated test fixture/status and live request: raw lines 48–60 and 86–98.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipayhk]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/ios-drop-in/2026-09-15|Adyen Alipay HK iOS Drop-in guide]]
