---
title: "Adyen Salesforce Commerce Cloud supported payment methods"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/supported-payment-methods"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/supported-payment-methods/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, payment-methods, plugin]
---

## Overview

This Adyen webpage snapshot compares payment-method support and starting versions for two Salesforce Commerce Cloud storefront types: **Storefront Reference Architecture (SFRA)** and **Composable Storefront**. The table is an integration/version matrix, not a statement that a particular merchant, country, currency, shopper, or live order can use every listed method. See [[adyen]] and [[adyen-salesforce-commerce-cloud]].

## Key takeaways

- The page states that its **Version** column indicates the version from which each method is supported. For country/region and feature support, it routes **SFRA** readers to the Web Components-filtered payment-method overview and **Composable Storefront** readers to the Web Drop-in-filtered overview (raw lines 19–24). This page does not provide a full country/currency eligibility matrix. Its two-column comparison should not be applied to **SiteGenesis**, which has no column here.
- Before offering a method, a merchant can **request** it for the merchant account in test or live Customer Area (raw lines 28–41). That request flow is distinct from plugin compatibility and does not prove merchant enablement or a processed payment.
- Support differs by storefront and version. For example, **iDEAL** is listed at SFRA `24.3.0+` and Composable `2.0.0+` (raw line 103), while **BACS Direct Debit** is listed for SFRA `21.1.0+` and marked unsupported in the Composable column (line 90). Similar SFRA-only entries appear across cash/ATM, banking, wallets, and real-time payments; use the pinned table for a particular method rather than assuming parity.
- **Apple Pay Express** has table versions `23.1.0` for SFRA and `1.2.0` for Composable without a `+` in that row. A separate product-detail-page note gives **v25.1.0 or later** (raw lines 160–163, 193). That version number aligns with SFRA versioning, but the note does not explicitly name a storefront; do not transfer the threshold or infer product-detail-page support for Composable. Keep this distinct from generic Apple Pay and the base support row.
- Rows span cards, cash/ATM, direct debit, online banking, buy now pay later, prepaid/gift cards, wallets, and instant real-time payments (raw lines 43–202). **Provenance caution:** raw frontmatter says last modified **2025-08-04** (line 11), yet this captured table includes SFRA `26.1.0+` and `26.2.0+` rows (lines 202 and 105); the separately retained [[source-adyen-docs-plugins-salesforce-commerce-cloud]] overview places SFRA V26 in January 2026. Preserve the captured rows without inferring an exact table publication or update date. The matrix does not specify checkout capture, order, refund, or settlement behavior.

## Detail locators

- Intro and account setup, raw lines 15–41: matrix interpretation, storefront-specific feature links, and merchant-account method requests.
- Category tables, raw lines 43–202: method-by-method SFRA and Composable support flags and version thresholds.
- Apple Pay Express note, raw line 193: product-detail-page threshold with no explicit storefront label; compare the version number with the separate SFRA and Composable table columns at line 161.
- Provenance, raw lines 11, 105, 202: 2025 last-modified metadata versus SFRA V26 rows; related overview dates V26 to January 2026.

## Related

- [[adyen-salesforce-commerce-cloud]] — SFRA versus Composable integration and feature boundary.
- [[adyen-online-payments]] — provider-wide payment-method and outcome context.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/supported-payment-methods/2026-09-15|Supported payment methods, fetched 2026-09-15]]
