---
title: "Braintree PayPal Commerce iOS Product Cards"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/product-cards"
raw_files:
  - "braintree/docs/guides/paypal-commerce-ios/product-cards-2026-09-16.md"
tags: [braintree, paypal-commerce, ios, sdk, product-cards]
---

## Overview

This Braintree-hosted snapshot documents product presentation and purchase initiation in the historical PayPal Commerce iOS SDK. It shows two approaches: add an SDK-provided `PPCProductCardView` populated from a search term or product group ID, or fetch a `PPCProduct` and call `purchaseProduct:` after a user action in an app-owned interface. The product card is described as displaying the product name, image, description, cost, and a buy button while the SDK fetches product information from its API.

The page was fetched on 2026-09-16, carries source frontmatter timestamps from 2025-04-01, and names neither an SDK release nor an environment. Treat it as historical evidence for the PayPal Commerce iOS SDK family, distinct from the modern modular [[braintree-ios-sdk]]; it does not establish current availability, runtime behavior, or a completed purchase.

## Key takeaways

- The embedded product-card view accepts either a search term or a product group ID in the shown Objective-C factory calls, returns through a `BOOL success` / `NSError` completion block, and is then added to the app's view hierarchy.
- The card's buy button initiates a purchase; the captured page does not say that displaying or tapping the card completes one.
- For an app-owned interface, the example first calls `fetchProductWithGroupID:completion:` to obtain a `PPCProduct`, then calls `[PayPalCommerce purchaseProduct:product]` once the user initiates the purchase.

## Detail locators

- **Product-card purpose, displayed fields, buy-button action, and API-populated information:** `Embed products in your own user interface`, raw lines 17-22.
- **Search-term product-card factory and completion shape:** `Add a product card to your app`, raw lines 23-35.
- **Product-group-ID product-card alternative:** raw lines 37-47.
- **Illustrated product-card purchase-flow route:** `Purchase flow from a product card in a content-based app`, raw lines 50-52.
- **Custom-UI product fetch and purchase call:** `Display and purchase a product from your app with your own UI`, raw lines 53-67.
- **Illustrated custom-UI purchase-flow route:** `Purchase flow from your own UI in a content-based app`, raw lines 69-71.

## Related

- [[braintree]]
- [[braintree-ios-sdk]] — modern modular Braintree iOS SDK retrieval route; do not transfer this historical PayPal Commerce product-card API to that package.
- [[source-braintree-docs-guides-paypal-commerce-ios-overview]] — historical PayPal Commerce iOS SDK purpose, use cases, platform boundary, and captured requirements.
- [[source-braintree-docs-guides-paypal-commerce-ios-setup]] — companion installation, Commerce Panel configuration, app-callback, and store-presentation snapshot.

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-ios/product-cards-2026-09-16|Braintree PayPal Commerce iOS product cards snapshot (fetched 2026-09-16)]]
