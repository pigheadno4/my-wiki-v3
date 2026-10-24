---
title: "Adyen Alipay HK Flutter Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/flutter-drop-in/2026-09-15.md"
tags: [adyen, alipayhk, flutter, drop-in, redirect]
---

## Overview

This [[adyen]] guide describes Alipay HK-specific additions to an existing **Flutter Drop-in** integration, with separate **Sessions** and **Advanced** server-side sections. Both require `action.type: redirect` handling and Alipay HK added in Customer Area. The main flow guides supply the base payment and return lifecycle; a configured method or test payment-list entry is not a final authorization, capture or settlement result. [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The requirements list an existing Sessions Flutter Drop-in integration, **Checkout API v68 or later**, redirect handling and Customer Area method setup. No extra Alipay HK `/sessions` or configuration parameters are stated; this method-specific statement does not remove the base Sessions request requirements. The integration-type row's link mistakenly targets an **Advanced** flow URL, while the other Sessions step links target Sessions. See raw lines 25–48.
- **Advanced:** Its requirements list an existing Advanced Flutter Drop-in integration, redirect handling and Customer Area setup. It says no additional Alipay HK configuration or `/payments` parameters. The Advanced section does not restate the Sessions-only v68+ requirement. See raw lines 62–84.
- **TEST/LIVE:** Both sections provide a test username/PIN pair and direct readers to the test Customer Area payment list for test status; see the pinned raw for those fixture values rather than treating them as live credentials. Before accepting live Alipay HK payments, the guide says to submit a request in **live Customer Area**. Submission is not approval, current eligibility or an actual completed payment. See raw lines 50–60 and 86–96.

## Detail locators

- Sessions scope, prerequisites, method-specific request/configuration and mismatched link: raw lines 25–48.
- Advanced prerequisites, configuration and request: raw lines 62–84.
- Duplicated test fixture/status view and live request: raw lines 50–60 and 86–96.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipayhk]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/flutter-drop-in/2026-09-15|Adyen Alipay HK Flutter Drop-in guide]]
