---
title: "Braintree PayPal Commerce iOS Facebook Login Configuration"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/facebook-login"
raw_files:
  - "braintree/docs/guides/paypal-commerce-ios/facebook-login-2026-09-16.md"
tags: [braintree, paypal-commerce, ios, facebook-login, configuration]
---

## Overview

This [[braintree|Braintree]]-hosted snapshot documents client-side Facebook Login configuration for an app using the historical PayPal Commerce iOS SDK. It directs the app to register a Facebook App ID in both the PayPal Commerce Panel and `Info.plist`, add the Facebook URL scheme, permit the `fbauth2` query scheme, and include the page's shown App Transport Security exceptions. It belongs with the historical PayPal Commerce iOS setup route and is distinct from the modern modular [[braintree-ios-sdk]].

The page was fetched on 2026-09-16 and its source frontmatter is timestamped 2025-04-02, but it names no SDK release or runtime environment. It does not document Facebook authentication/session or token handling, merchant-server behavior, app-review requirements, account eligibility, or a payment flow. Treat its plist and transport settings as snapshot-scoped configuration, not current platform, SDK, Facebook, security, availability, login-success, or payment-execution proof.

## Key takeaways

- An app that includes Facebook Login is told to add its Facebook App ID in the PayPal Commerce Panel's General Settings and to `Info.plist` under `FacebookAppID`. The page does not establish that the app, merchant account, or Facebook integration is currently eligible or enabled.
- The app must also add the Facebook-provided URL scheme in the Xcode target's URL Types. The example scheme `fb1234567890` is illustrative, not a reusable value or evidence that a callback completed.
- The page says the `LSApplicationQueriesSchemes` array should include `fbauth2`; its XML example also lists `fbapi`, `fb-messenger-api`, and `fbshareextension`. These are captured client settings, not a complete login lifecycle or a guarantee that Facebook app switching, browser fallback, authentication, or account linking succeeds.
- The shown `NSAppTransportSecurity` configuration adds exception domains for `cloudfront.net`, `facebook.com`, `fbcdn.net`, and `akamaihd.net`, includes subdomains, and sets `NSExceptionRequiresForwardSecrecy` to `false` for each. The snapshot does not establish that these broad historical exceptions are currently necessary, sufficient, or appropriate.

> [!warning] Historical transport configuration
> Preserve the captured XML as page-specific historical evidence only. Before adopting any App Transport Security exception, verify current Apple and Facebook requirements and review the security impact; this unversioned snapshot is not current security guidance or runtime proof.

## Detail locators

- **Facebook Login setup purpose:** opening paragraph, raw line 16.
- **Commerce Panel and `Info.plist` Facebook App ID:** raw lines 17-18.
- **Xcode URL Type and illustrative Facebook URL scheme:** raw lines 19-22.
- **`LSApplicationQueriesSchemes` direction and full example list:** raw lines 25-40.
- **App Transport Security statement and captured exception-domain XML:** raw lines 42-81.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-ios-sdk]]
- Historical parent setup: [[source-braintree-docs-guides-paypal-commerce-ios-setup]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-ios/facebook-login-2026-09-16|Braintree PayPal Commerce iOS Facebook Login configuration snapshot (fetched 2026-09-16)]]
