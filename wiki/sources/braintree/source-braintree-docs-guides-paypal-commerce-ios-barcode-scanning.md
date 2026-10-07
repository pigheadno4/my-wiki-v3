---
title: "Braintree PayPal Commerce iOS Barcode Scanning"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/barcode-scanning"
raw_files:
  - "braintree/docs/guides/paypal-commerce-ios/barcode-scanning-2026-09-16.md"
tags: [braintree, paypal-commerce, ios, barcode, qr-code]
---

## Overview

This Braintree-hosted snapshot documents barcode scanning in the historical PayPal Commerce iOS SDK. For a store that supports UPC search, it describes enabling UPC and QR scanning in the configuration plist, checking device support through `PayPalCommerce deviceSupportsBarcodeScanning`, and launching the scanner through `PayPalCommerce scanForBarcodes`. It is distinct from the modern modular [[braintree-ios-sdk]] and ordinary Braintree checkout or Drop-in integration.

The page was fetched on 2026-09-16 and carries source frontmatter timestamps from 2025-04-02, but it names no SDK release, runtime environment, server behavior, or payment flow. Treat its configuration, APIs, result navigation, and QR URL examples as historical snapshot evidence, not proof of current availability, exact-package behavior, merchant enablement, device support, product-match results, or payment execution.

## Key takeaways

- The page conditions barcode and QR scanning on the store supporting UPC search, then directs the app to set `enable_barcode_scanning` to `true` in the configuration plist.
- The app can ask `PayPalCommerce deviceSupportsBarcodeScanning` whether the device supports scanning and, when it does, call `PayPalCommerce scanForBarcodes` to present the scanning interface. The captured page does not establish support on any particular device or OS version.
- When a scan finds matches, the documented interface presents a product-detail page for a match or a product list for multiple matches. This is result navigation within the historical Commerce store experience, not evidence of inventory accuracy, purchase completion, or payment processing.
- The page gives `http://m.example.com/search/ninja` and `http://m.example.com/product/123456` as the captured QR-code formats. These are examples from the snapshot, not current production endpoints or a general QR URL contract.

## Detail locators

- **UPC-search condition, plist flag, device-support check, and scan trigger:** `Barcode Scanning`, raw lines 14–17.
- **Scanning interface and single-versus-multiple-match presentation:** raw lines 17–19.
- **QR-code URL examples:** raw lines 19–21.

## Related

- [[braintree]]
- [[braintree-ios-sdk]] — modern modular Braintree iOS SDK retrieval route; do not transfer this historical PayPal Commerce SDK page's configuration, API, device-support, or navigation claims to that package.
- [[source-braintree-docs-guides-paypal-commerce-ios-initial-theming-and-configuration]] — companion historical configuration snapshot containing the scanning flag among other optional initial settings.
- [[source-braintree-docs-guides-paypal-commerce-ios-product-cards]] — companion historical product-presentation and purchase-initiation snapshot; barcode match navigation alone does not establish purchase completion.

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-ios/barcode-scanning-2026-09-16|Braintree PayPal Commerce iOS barcode-scanning snapshot (fetched 2026-09-16)]]
