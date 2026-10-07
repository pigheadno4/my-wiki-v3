---
title: "Braintree PayPal Commerce iOS URL Specs"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/url-specs"
raw_files:
  - "braintree/docs/guides/paypal-commerce-ios/url-specs-2026-09-16.md"
tags: [braintree, paypal-commerce, ios, url-scheme, deep-links]
---

## Overview

This Braintree-hosted snapshot documents custom-URL shapes for deep links into the historical PayPal Commerce iOS experience. It says all such URLs use an app-specific PayPal Commerce URL scheme obtained from the PayPal Commerce Panel, then lists paths for a product, a selected product variant, a category, and search results. It is distinct from the modern modular [[braintree-ios-sdk]] and ordinary Braintree checkout or Drop-in integration.

The page was fetched on 2026-09-16 and carries source frontmatter timestamps from 2025-04-01, but identifies no SDK release, supported iOS version, environment, or runtime-validation behavior. Its example scheme and identifiers are illustrative snapshot content, not evidence of current availability, app configuration, deep-link handling, account eligibility, successful navigation, or payment execution.

## Key takeaways

- Every documented URL uses the PayPal Commerce URL scheme assigned to the app; the page illustrates this with `pypl-acme://` for an app named Acme and routes readers to the PayPal Commerce Panel for their own scheme.
- The documented path families target a product by product-linking ID, a product variant by SKU, a category by fully qualified category slug, or search results by search type and term.
- Search is described with the specific types `upc` and `name`, plus catchall `q`. The shown `q` and `upc` URLs are examples rather than proof that a current SDK, store, or app accepts or resolves them.
- This sparse page defines URL formatting only. It does not document client/server payment responsibilities, create or process a payment, identify an exact SDK version, or establish current compatibility with the separately versioned PayPal Commerce, Braintree iOS, or standalone PayPal iOS SDKs.

## Detail locators

- **Required URL scheme, illustrative `pypl-acme://` value, and Commerce Panel lookup:** raw lines 16–17.
- **Product deep-link path and example:** raw line 19.
- **Product-variant deep-link path and SKU example:** raw line 20.
- **Category deep-link path and slug example:** raw line 21.
- **Search path, `upc` / `name` / `q` types, and examples:** raw line 22.

## Related

- [[braintree]]
- [[braintree-ios-sdk]] — modern modular Braintree iOS SDK route; do not transfer this historical PayPal Commerce URL table to that package or infer exact-version handling.
- [[source-braintree-docs-guides-paypal-commerce-ios-overview]] — historical PayPal Commerce iOS product purpose, availability, use-case, platform, and requirement context.
- [[source-braintree-docs-guides-paypal-commerce-ios-setup]] — companion historical setup snapshot for Commerce Panel configuration and app URL callbacks.

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-ios/url-specs-2026-09-16|Braintree PayPal Commerce iOS URL specs snapshot (fetched 2026-09-16)]]
