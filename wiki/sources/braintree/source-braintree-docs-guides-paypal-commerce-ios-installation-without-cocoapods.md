---
title: "Braintree PayPal Commerce iOS Installation without CocoaPods"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/installation-without-cocoapods"
raw_files:
  - "braintree/docs/guides/paypal-commerce-ios/installation-without-cocoapods-2026-09-16.md"
tags: [braintree, paypal-commerce, ios, sdk, dependencies, manual-installation]
---

## Overview

This [[braintree|Braintree]]-hosted snapshot documents manual installation of the historical PayPal Commerce iOS SDK without CocoaPods. It directs an integrator to copy the `PayPalCommerce` directory into an app project, install a listed set of third-party dependencies, and reference the package's acknowledgements file for licensing attribution. It belongs with the historical PayPal Commerce iOS setup route and is distinct from the modern modular [[braintree-ios-sdk]].

The page was fetched on 2026-09-16 and carries source frontmatter timestamps from 2025-04-02, but it identifies no PayPal Commerce SDK release or runtime environment. Its dependency list includes Braintree v4.3 and several other historical versions; those values are described only as versions the page's authors tested against, not as current package requirements or proof of present build compatibility. The linked dependency repositories and acknowledgements file are navigation targets that were not read as authority for their contents or current state.

## Key takeaways

- The central installation action is to copy the `PayPalCommerce` directory into the iOS project and install every dependency listed by the page. The snapshot does not identify the PayPal Commerce package version represented by that directory.
- The page says its listed dependency versions are the versions tested against. The list spans AFNetworking 2.6, Braintree 4.3, CGLMail 0.1.1, CocoaLumberjack 2.2.0, ECSlidingViewController 2.0.3, Facebook 4.7.1 with Bolts 1.4, Google Analytics 3.13.0, libPhoneNumber-iOS 0.8.8, LogglyLogger-CocoaLumberjack 2.2.0, and Mantle 1.5.6. Treat these as historical snapshot values, not current compatibility, minimum-version, security, or support claims.
- BCCKeychain, CHTCollectionViewWaterfallLayout, and Core Text Label are described as already compiled into the PayPal Commerce library rather than separate dependencies to install.
- The app must reference `PayPalCommerce-Acknowledgements.md` somewhere so the documented licensing attribution is covered. The linked GitHub file is an unread navigation target, so this snapshot does not establish its current contents or availability.

> [!warning] Historical package and dependency boundary
> Do not apply this unversioned `PayPalCommerce` directory, Braintree v4.3 dependency, or other historical tested versions to the current modular Braintree iOS SDK. This website snapshot is not exact-release or exact-commit GitHub evidence and does not prove a successful build, runtime behavior, current support, merchant enablement, or payment execution.

## Detail locators

- **Manual-copy installation action:** opening paragraph, raw line 16.
- **Tested-version qualification and complete external dependency list:** `Dependencies`, raw lines 17-29.
- **Libraries already compiled into the PayPal Commerce library:** `Other libraries already built into the SDK`, raw lines 32-37.
- **Acknowledgements-file attribution requirement and GitHub navigation:** `Acknowledgements`, raw lines 40-42.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-ios-sdk]]
- Historical parent setup: [[source-braintree-docs-guides-paypal-commerce-ios-setup]]
- Historical product overview: [[source-braintree-docs-guides-paypal-commerce-ios-overview]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-ios/installation-without-cocoapods-2026-09-16|Braintree PayPal Commerce iOS installation without CocoaPods snapshot (fetched 2026-09-16)]]
