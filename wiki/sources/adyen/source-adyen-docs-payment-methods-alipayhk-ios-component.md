---
title: "Adyen AlipayHK iOS Component guide"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk/ios-component"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/ios-component/2026-09-15.md"
tags: [adyen, alipayhk, ios, components, online-payments, redirects]
---

## Overview

This [[adyen]] page, last modified and captured 2026-09-15, gives **Alipay HK-specific additions** to an existing iOS Components integration. It has separate **Sessions** and **Advanced** server-flow branches, each requiring a previously built iOS integration, redirect handling and Alipay HK added in Customer Area. The source supplies no country/currency list, tokenization procedure or final payment-outcome rule; those must not be inferred from its method name, test credentials or Component display. See [[adyen-online-payments]].

## Key takeaways

- The **Sessions** requirements specify **Checkout API v68 or later** and `action.type: redirect`. This page says no extra Alipay HK parameters are needed when creating `/sessions`, and no Alipay HK-specific Component configuration parameters are needed. These statements assume the linked main Sessions integration, not an empty payment-session request. See raw lines 23–48.
- For Sessions initialization, the snippet checks the method in `session.sessionContext.paymentMethods`, creates a Component and sets the **session** as delegate. It literally names the `None` class and passes `alipayHKConfiguration`, even though the preceding text says no extra Alipay HK configuration is required and does not define that variable. The class/variable combination is unresolved in this page; the snippet is not a verified copy-ready implementation. See raw lines 52–73.
- The **Advanced** branch also requires redirect handling and Customer Area method setup. Its requirement label says iOS Components, but its integration-type link points to `integration=Drop-in` while its redirect link points to Components. It states no extra Alipay HK configuration or `/payments` parameters, and its snippet sets the **host object** as Component delegate (`self`), again using literal `None` and an undefined `alipayHKConfiguration`. Keep that cross-link/snippet discrepancy rather than treating the Drop-in URL as an Advanced Components procedure. The page does **not** state the Sessions v68 minimum again for Advanced. See raw lines 87–133.
- Both flow branches list a test account/PIN and test Customer Area payment-list lookup, then say a **request for AlipayHK in the live Customer Area** is needed before accepting live payments. Test credentials and a submitted live request do not establish provider approval, shopper redirect return, final authorization, capture or settlement. The page does not report webhook or result-code outcomes; follow the applicable main integration for those separate steps. See raw lines 75–85 and 135–145.

## Detail locators

- **Sessions prerequisites, v68+, redirect and no added session/config fields:** raw lines 23–48.
- **Sessions Component snippet and delegate:** raw lines 52–73.
- **Advanced prerequisites, inconsistent integration link, snippet/delegate, no added `/payments` fields:** raw lines 87–133.
- **Test credentials, payment-list lookup and live Customer Area request:** raw lines 75–85 and 135–145.

## Related

- [[adyen-online-payments]]
- [[adyen-ios-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/ios-component/2026-09-15|Alipay HK iOS Component — captured 2026-09-15]]
