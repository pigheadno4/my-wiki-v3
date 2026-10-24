---
title: "Alipay Web Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay/web-component"
raw_files:
  - "adyen/docs/payment-methods/alipay/web-component/2026-09-15.md"
tags: [adyen, alipay, web, components, redirect]
---

## Overview

This 2026-09-15 Adyen guide adds Alipay to an **existing Web Components integration**, with separate Sessions and Advanced server-side flow sections. It covers the method-specific Redirect Component setup; the linked main integration guides own the base payment and redirect flow. The page's setup and snippets do not prove a real Alipay payment outcome. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** requires an existing Sessions Web Components integration, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and Alipay added in Customer Area. The guide says no additional `/sessions` parameters are needed for Alipay. (raw lines 25–42)
- **Advanced flow:** requires an existing Advanced Web Components integration, redirect handling for `action.type: redirect`, and Alipay added in Customer Area. Its section does **not** state a Checkout API minimum; do not extend the Sessions-only v68 requirement to Advanced from this page. It says no additional Alipay `/payments` parameters are needed. (raw lines 90–98, 136–140)
- For both flows, import `Redirect` from `@adyen/adyen-web`, use that class to initialize the Alipay Component, and add no Alipay-specific configuration parameters. The shown initialization snippets spell the constructor `newRedirect(checkout,` although the import and prose call it `Redirect`; they also refer in a comment to a configuration object despite saying none is needed. Treat the snippets as inconsistent illustrations rather than verified copy-paste code. (raw lines 44–77, 100–133)
- The page **recommends** live penny tests and checking them in live Customer Area; it separately says a request for Alipay must be submitted in live Customer Area before accepting live payments. These are historical instructions, not evidence that a live request was granted or any test or payment was performed. (raw lines 80–88, 142–150)

## Detail locators

- Sessions requirements, no extra session parameters and import/configuration: raw lines 25–60.
- Sessions Redirect initialization and snippet discrepancy: raw lines 62–78.
- Advanced requirements, import/configuration and initialization: raw lines 90–134.
- Advanced no-extra-parameters statement: raw lines 136–140.
- Recommended testing and live request gate: raw lines 80–88 and 142–150.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay/web-component/2026-09-15|Adyen Alipay Web Component, 2026-09-15 snapshot]]
