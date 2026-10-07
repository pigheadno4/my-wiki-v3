---
title: "Braintree PayPal Commerce iOS Launch Checklist"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/launch-checklist"
raw_files:
  - "braintree/docs/guides/paypal-commerce-ios/launch-checklist-2026-09-16.md"
tags: [braintree, paypal-commerce, ios, sdk, launch-checklist, oauth]
---

## Overview

This Braintree-hosted snapshot is a launch checklist for the historical PayPal Commerce iOS SDK. It sorts setup and feature work into items the page labels required for basic functionality, optional but highly recommended, and totally optional, and adds a separate condition for multiple apps using one PayPal Commerce store. It is a companion to [[source-braintree-docs-guides-paypal-commerce-ios-setup]] and is distinct from the modern modular [[braintree-ios-sdk]].

The page was fetched on 2026-09-16 and carries source frontmatter timestamps from 2025-04-02, but identifies no SDK release or environment. Treat its checklist as historical snapshot guidance, not evidence of current product availability, account eligibility, merchant enablement, exact-SDK behavior, runtime configuration, or payment execution.

## Key takeaways

- Under `Required for basic functionality`, the page lists adding the PayPal Commerce SDK, including the acknowledgements attribution, configuring the SDK in the app delegate, setting up a custom URL scheme, presenting the store, enabling Spotlight Search Index, updating `Info.plist`, and implementing 3D Touch. These are the page's historical checklist labels rather than a current universal iOS baseline.
- The page gives an explicit security warning that the client ID and secret must be obfuscated to protect the store and its customers. It says the custom URL scheme supports email login, PayPal login, and deep links to products and categories.
- Push notifications and Facebook login are grouped as optional but highly recommended. Product cards and barcode UPC/QR scanning are grouped as totally optional.
- If multiple iOS apps interact with one PayPal Commerce store, the page says to create multiple OAuth clients to keep email verification functional. It directs the reader to the Commerce Panel's Channels > iOS SDK area and says each OAuth client supplies its own PayPal Commerce URL scheme, client ID, and secret.

## Detail locators

- **Checklist purpose and required-for-basic-functionality heading:** raw lines 14–18.
- **SDK installation, acknowledgements, app-delegate configuration, and credential warning:** raw lines 20–25.
- **Custom URL scheme, store presentation, Spotlight, `Info.plist`, and 3D Touch:** raw lines 27–29.
- **Recommended push notifications and Facebook login:** raw lines 30–34.
- **Optional product cards and barcode/QR scanning:** raw lines 35–40.
- **Multiple apps, separate OAuth clients, and per-client values:** raw lines 41–47.

## Related

- [[braintree]]
- [[braintree-ios-sdk]] — provider-owned route for the modern modular Braintree iOS SDK; do not transfer this checklist's historical PayPal Commerce SDK statements to that package.
- [[source-braintree-docs-guides-paypal-commerce-ios-setup]] — companion setup snapshot containing the linked installation, configuration, URL-handling, platform-integration, and store-presentation detail.

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-ios/launch-checklist-2026-09-16|Braintree PayPal Commerce iOS launch checklist snapshot (fetched 2026-09-16)]]
