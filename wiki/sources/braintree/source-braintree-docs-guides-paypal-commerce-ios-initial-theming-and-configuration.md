---
title: "Braintree PayPal Commerce iOS Initial Theming and Configuration"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/initial-theming-and-configuration"
raw_files:
  - "braintree/docs/guides/paypal-commerce-ios/initial-theming-and-configuration-2026-09-16.md"
tags: [braintree, paypal-commerce, ios, theming, configuration]
---

## Overview

This Braintree-hosted, unversioned PayPal Commerce iOS snapshot documents optional initial store theming and behavior configuration through `PayPalCommerce-Config.plist` and `PayPalCommerce-Assets.xcassets`. Most values are described as overridden by theme settings in the PayPal Commerce Panel. It belongs with the historical PayPal Commerce iOS setup route and is distinct from the modern modular [[braintree-ios-sdk]].

The page was fetched on 2026-09-16 and its source frontmatter is timestamped 2025-04-01. It does not name an SDK release or environment, and the capture does not establish current account eligibility, exact-SDK behavior, runtime application of a theme, asset availability, or successful payment execution.

## Key takeaways

- Initial setup is optional. Including `PayPalCommerce-Config.plist` and `PayPalCommerce-Assets.xcassets` supplies the documented initial setup, while most values are expected to be overridden by PayPal Commerce Panel theme settings.
- The configuration table covers initial-onboarding behavior, weighted font names, barcode and QR-code scanning, and application colors. With `skip_initial_onboarding` set to `YES`, the products list is initially shown, but a shopper who attempts a purchase before completing onboarding is prompted to finish onboarding at that point.
- The asset catalog lists a login background and a navigation-header logo, both subject to PayPal Commerce Panel overrides. The captured page labels 320x568 and 640x1136 as required login-background sizes, and 167x30 and 328x60 as suggested header-logo sizes. These are snapshot-scoped configuration details, not proof that a current SDK accepts or renders them.

## Detail locators

- **Panel overrides, initial configuration files, and optionality:** `Initial Theming and Configuration`, raw lines 16–19.
- **Onboarding, font, scanning, and color configuration:** `PayPalCommerce-Config.plist`, raw lines 22–37.
- **Login-background and header-logo asset roles and captured sizes:** `PayPalCommerce-Assets.xcassets`, raw lines 40–43.

## Related

- [[braintree]]
- [[braintree-ios-sdk]] — modern modular Braintree iOS SDK retrieval route; do not transfer this unversioned PayPal Commerce store configuration to that package.
- [[source-braintree-docs-guides-paypal-commerce-ios-setup]] — related historical PayPal Commerce iOS installation, OAuth-client, callback, platform-integration, and store-presentation setup.

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-ios/initial-theming-and-configuration-2026-09-16|Braintree PayPal Commerce iOS initial theming and configuration snapshot (fetched 2026-09-16)]]
