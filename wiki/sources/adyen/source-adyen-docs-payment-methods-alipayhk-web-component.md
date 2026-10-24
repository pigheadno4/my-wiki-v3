---
title: "Alipay HK Web Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk/web-component"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/web-component/2026-09-15.md"
tags: [adyen, alipayhk, web, components, redirect]
---

## Overview

This 2026-09-15 Adyen guide adds Alipay HK to an **existing Web Components integration**, with separate Sessions and Advanced server-side flow sections. It states method-specific additions; the linked main guides own the base integration and redirect handling. This is a historical setup and testing guide, not evidence that a merchant is live-enabled or a payment is complete. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** requires an existing Sessions Web Components integration, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and Alipay HK added in Customer Area. No **additional Alipay HK** `/sessions` parameters are needed when creating a payment session. (raw lines 25–42)
- For Sessions, import `Redirect` from `@adyen/adyen-web`, use the `Redirect` class, and add no Alipay HK-specific configuration parameters. The initialization example passes `{ type:alipay_hk }` with an unquoted `alipay_hk` identifier and no definition in this page; do not treat the snippet as verified copy-paste code. (raw lines 44–71)
- **Advanced:** requires an existing Advanced Web Components integration, redirect handling for `action.type: redirect`, and Alipay HK added in Customer Area. The section does **not** state an API-version minimum; it says no additional Alipay HK `/payments` parameters are needed. It imports/uses `Redirect` and repeats the unquoted `type:alipay_hk` example. The explicit no-additional-configuration sentence appears in the Sessions section, not the Advanced section. (raw lines 86–124)
- Both flows provide **test** AlipayHK credentials and point to the test Customer Area payment list for checking test-payment status. Separately, the page says a request for AlipayHK must be submitted in the **live Customer Area** before live acceptance. Test credentials/status lookup and request submission do not prove live approval or any actual authorization, capture, settlement or refund. (raw lines 74–84, 126–136)

## Detail locators

- Sessions requirements, no-extra-parameters, import/configuration and initialization: raw lines 25–72.
- Test credentials/status lookup and live request gate for Sessions: raw lines 74–84.
- Advanced requirements, Redirect setup, no-extra-parameters and repeated example: raw lines 86–124.
- Test and live boundary for Advanced: raw lines 126–136.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipayhk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/web-component/2026-09-15|Adyen Alipay HK Web Component, 2026-09-15 snapshot]]
