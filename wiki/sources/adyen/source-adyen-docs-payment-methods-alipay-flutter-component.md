---
title: "Adyen Alipay Flutter Component integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/alipay/flutter-component/2026-09-15.md"
tags: [adyen, alipay, flutter, component, redirect]
---

## Overview

This [[adyen]] guide describes Alipay-specific additions to an existing **Flutter Components** integration, with separate **Sessions** and **Advanced** server-side sections. Both call for `action.type: redirect` handling and Alipay added in Customer Area. The guide delegates the base integration and payment lifecycle to linked main-flow documentation; setup or return from a redirect is not a final authorization, capture or settlement result. [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The requirements table says existing Sessions Flutter Components, **Checkout API v68 or later**, redirect handling and Alipay in Customer Area. It says no additional Alipay parameters are needed for `/sessions` and no extra Alipay configuration parameters. “No additional” is method-specific and does not remove the base Sessions request or redirect requirements. See raw lines 25–46.
- **Advanced:** Its own section says existing Advanced Flutter Components, redirect handling and Alipay in Customer Area; it says no extra Alipay configuration or `/payments` parameters. It does **not** restate v68+ as an Advanced-specific requirement. See raw lines 58–80.
- **Link conflict:** Both integration-type rows label Flutter **Components** but link to `advanced-flow?...integration=Drop-in`; the Sessions row also points to Advanced rather than Sessions. The redirect and request-step links elsewhere use the corresponding Sessions/Advanced **Components** routes. Do not follow the mismatched integration-type URLs as evidence of a Drop-in prerequisite. See raw lines 31–40 and 66–80.
- **Live preparation:** In both flow sections, Adyen recommends live penny tests using an Alipay wallet app with a credit/debit card, then checking the listed payments in live Customer Area. The page separately says a request for Alipay must be submitted in live Customer Area before accepting live payments. This is documented advice and a request gate, not approval, live eligibility or a completed payment. No TEST simulator or test-environment procedure appears in this pinned page. See raw lines 48–56 and 82–90.

## Detail locators

- Sessions prerequisites, method-specific request and configuration: raw lines 25–46.
- Advanced prerequisites, method-specific configuration and request: raw lines 58–80.
- Live-test recommendation and live request: raw lines 48–56 and 82–90.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipay]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay/flutter-component/2026-09-15|Adyen Alipay Flutter Component guide]]
