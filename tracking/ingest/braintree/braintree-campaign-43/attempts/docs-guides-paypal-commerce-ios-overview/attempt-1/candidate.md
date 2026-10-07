---
title: "Braintree PayPal Commerce iOS SDK Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/overview"
raw_files:
  - "braintree/docs/guides/paypal-commerce-ios/overview-2026-09-16.md"
tags: [braintree, paypal-commerce, ios, sdk, mobile-commerce]
---

## Overview

This Braintree-hosted snapshot is an overview of the historical PayPal Commerce iOS SDK, which presented a PayPal Commerce-powered mobile store as a standalone app, an embedded store, or embedded products and buy buttons. It describes connecting an ecommerce platform while continuing ordinary product, inventory, order-processing, and fulfillment operations there. This product is distinct from the modern modular [[braintree-ios-sdk]] and ordinary Braintree checkout or Drop-in integration.

The page labels PayPal Commerce as a closed beta and links to an application form. It was fetched on 2026-09-16 and carries source frontmatter timestamps from 2025-04-02, but it identifies no SDK release or runtime environment. Its availability, platform list, iOS 8.0–10.0 range, device list, feature list, and live-store examples are historical snapshot claims, not evidence of current eligibility, enablement, exact-package support, runtime behavior, or successful payment processing.

## Key takeaways

- The page's three SDK use cases are a standalone store app, a store embedded modally or more deeply in an existing app, and products or buy buttons embedded for in-app purchasing.
- The captured overview says merchants connect an ecommerce platform and continue managing products, inventory, order processing, and shipment fulfillment through that platform, while stores, credentials, and backends are managed in the PayPal Commerce Panel. It names Magento, Bigcommerce, and Demandware as supported in this historical snapshot.
- The feature list advertises shopping without a cart, compatibility with an existing commerce solution, embedded products and buy buttons, credit-card and PayPal acceptance, UI customization, push notifications, Spotlight, 3D Touch, and barcode/QR scanning. This list does not establish configuration, buyer or merchant eligibility, runtime availability, or a completed payment.
- The historical requirements state iOS 8.0–10.0 and identify corresponding minimum Apple devices, while recommending the latest Xcode. Because the page is unversioned and environment-unspecified, these statements must not be applied as current package compatibility.
- The page routes SDK discovery and bug or feature requests to the Braintree `paypal-commerce-ios` GitHub repository, and names its Releases and `CHANGELOG.md` as release-notification routes. The overview itself does not identify an exact package version or commit.

## Detail locators

- **Closed-beta availability and application route:** `AVAILABILITY`, raw lines 17–18.
- **Mobile-commerce purpose, ecommerce-platform connection, named platforms, and release-notification routes:** raw lines 20–26.
- **SDK repository and the three store/embedding use cases:** `About the SDK`, raw lines 27–32.
- **Commerce Panel versus merchant ecommerce-platform responsibilities:** raw lines 34–35.
- **Historical iOS/device requirements and Xcode recommendation:** `Requirements`, raw lines 36–39.
- **Advertised feature list:** `Features`, raw lines 40–51.
- **Historical live-store examples and issue route:** `Live stores` and `Bugs and feature requests`, raw lines 54–64.

## Related

- [[braintree]]
- [[braintree-ios-sdk]] — modern modular Braintree iOS SDK retrieval route; do not transfer this historical PayPal Commerce SDK overview's availability, compatibility, feature, or platform claims to that package.
- [[source-braintree-docs-guides-paypal-commerce-ios-setup]] — companion historical setup snapshot for installation, Commerce Panel client configuration, app callbacks, optional integrations, and store presentation.

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-ios/overview-2026-09-16|Braintree PayPal Commerce iOS overview snapshot (fetched 2026-09-16)]]
