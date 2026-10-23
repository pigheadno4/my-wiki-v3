---
title: "Adyen online payment-method catalog"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods"
raw_files:
  - "adyen/docs/payment-methods/2026-09-15.md"
tags: [adyen, online-payments, payment-methods, catalog]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] catalog is a navigation and comparison entry for payment methods in **online** integrations using Drop-in, Components or API-only. It points to separate catalogs for Pay by Link, in-person payments and plugins. Its method rows describe snapshot-level type, flow, country/region, processing and settlement currencies, listed features and supported integration links where present. Use it with [[adyen-online-payments]] to find a method guide; a catalog listing alone does not establish current merchant enablement, country eligibility, payment execution or funds settlement.

## Key takeaways

- **Scope and filters:** The page's filters are Country/Region, Processing currency, Settlement currency, Feature and Supported integration. The scope sentence expressly separates this online catalog from Pay by Link, in-person and plugin support. See pinned raw lines 20–28.
- **Row-level differences:** Individual entries vary by method and may omit some fields. For example, the captured Convenience stores Indonesia row lists IDR processing and USD settlement (raw line 47), while the captured Samsung Pay row lists API-only as its supported integration (raw line 122). These are dated catalog labels, not authorization to configure either method or proof of successful processing. Consult the specific linked method and integration guide before applying a row.
- **Interpretation boundary:** A listed flow label (such as Direct, Redirect or Additional action), feature label (such as recurring or refunds), or settlement-currency field is catalog metadata. It does not define the full checkout steps, prove that a merchant account has the feature, or show authorization, capture, refund completion or recipient funds. The raw catalog is the locator for individual method rows; linked child pages were not used as behavioral evidence here.

## Detail locators

- Purpose, online integration scope and other-channel links: pinned raw lines 18–22.
- Available filter names and start of the catalog: pinned raw lines 24–30.
- Individual method rows, with their exact country, currency, feature and integration labels: pinned raw lines 30–141.

## Related

- [[adyen-online-payments]] — online integration and lifecycle context.
- [[source-adyen-docs-standard-integration-payment-method-setup]] — separate setup-route overview; this catalog does not perform setup.
- [[adyen-payment-method-variants]] — transaction variant and adding-method reference, distinct from this shopper-facing catalog.

## Raw Sources

- [[raw/adyen/docs/payment-methods/2026-09-15|Online payment-method catalog, captured 2026-09-15]]
