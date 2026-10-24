---
title: "Adyen Apple Pay Flutter Drop-in guide"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/flutter-drop-in/2026-09-15.md"
tags: [adyen, apple-pay, flutter, drop-in, online-payments]
---

## Overview

This [[adyen]] page, last modified and captured 2026-09-15, explains adding Apple Pay to an **existing Flutter Drop-in** integration using either a Sessions or Advanced server flow. It assumes Apple Pay was set up with a **merchant-owned certificate** and added in Customer Area; the live API credential needs the **API Clientside Encryption Payments role**. Route through [[adyen-online-payments]] and the separate [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-ios]] setup guide. This page does not establish certificate installation, Apple Pay capability or merchant enablement, and it shows no completed authorization, capture or settlement.

## Key takeaways

- **Prerequisites and server boundary:** the `/sessions` tab points to an existing Sessions Drop-in and the `/payments` tab to an existing Advanced Drop-in. Both call for own-certificate Apple Pay setup and Customer Area method addition. It says Apple Pay itself adds no extra fields to the respective `/sessions` or `/payments` request; the base integration still supplies its own required fields. For errors, it routes to a separate Apple Pay error-handling guide. The requirements-table links contain unexpanded `platform` template text, while the API-reference links name Flutter directly. See raw lines 21–53.
- **Flutter/iOS client configuration:** both flow sections say extra Apple Pay configuration is required. The property table names `merchantID` and `merchantName`; the Dart illustration constructs `ApplePayConfiguration(merchantId: ..., merchantName: ...)`. It also lists optional onboarding, billing/shipping, supported-country and merchant-capability settings. If summary items are supplied, the last item's value must match the amount stated for `/payments`; that wording does not define how to reconcile a Sessions request. Sessions then initializes/shows Drop-in; Advanced points to required callbacks. Consult the version-matched Flutter API before copying the illustrative constructor. See raw lines 55–106.
- **Test and live boundary:** the page sends readers to Apple's sandbox test cards and Adyen's **test** Payment list. For live processing, it repeats the API Clientside Encryption Payments role and calls for Apple Pay setup under the live Apple Developer merchant identifier. A test payment listing, configured merchant ID, wallet sheet or callback is not a live payment outcome. The guide gives no recurring-token or refund procedure. See raw lines 108–120.

> [!warning] Contradiction
> The configuration table spells the property `merchantID`, but the Flutter constructor example uses `merchantId` (raw lines 65–77). The page does not resolve the naming difference. Verify the actual Flutter configuration contract for the installed version.

## Detail locators

- Sessions/Advanced prerequisites, own-certificate and live-role conditions: raw lines 21–41.
- No-extra-Apple-Pay-server-fields and error route: raw lines 43–53.
- Required Flutter Apple Pay properties, optional fields and flow-specific launch/callback links: raw lines 55–106.
- Sandbox test and live role/merchant-ID setup: raw lines 108–120.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-ios]]
- [[source-adyen-docs-payment-methods-apple-pay-handle-apple-pay-errors]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/flutter-drop-in/2026-09-15|Apple Pay Flutter Drop-in guide — collected 2026-09-15]]
