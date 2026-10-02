---
title: "Braintree Auth Client-side Connect Flow for iOS v7"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/client-side/ios/v7"
raw_files:
  - "braintree/docs/guides/braintree-auth/client-side/ios/v7-2026-09-16.md"
tags: [braintree, braintree-auth, ios, oauth, client-side]
---

## Overview

This collected Braintree guide documents a closed-beta iOS v7 client-side Connect route for a platform to send a merchant through Braintree authorization without exposing the platform's `client_secret` in the app. It is a [[braintree-auth]] merchant-connection flow, not payment-transaction authorization: the iOS app presents the hosted authorization and handles the return, while the platform server supplies the Connect URL and performs the OAuth exchange.

## Key takeaways

- The merchant starts from a Connect button in the iOS app, which presents a server-provided `connect_url` in `SFSafariViewController`. After Braintree returns the merchant to the configured redirect URI, the server performs the OAuth exchange and redirects to a custom URL scheme captured by the app.
- The app-side example registers a notification observer, dismisses the Safari view after the return event, and configures `CFBundleURLTypes` plus an application-delegate handler for the custom URL. These are implementation examples in the collected guide, not evidence of a completed connection or current account eligibility.
- The guide prose says the application-delegate handler will ensure the URL is from a trusted source, but the displayed function does not visibly inspect `url` or `sourceApplication` before broadcasting the return event. Do not infer return authenticity or successful authorization from this sample.
- The guide warns that the server must not put sensitive information in the custom return URL because other iOS apps can intercept custom URL schemes.
- The collected page states that Braintree Auth is in closed beta. It also carries a dated Mobile SDK certificate warning: certificates were set to expire on March 30, 2026, it named iOS SDK 6.17.0+ as the upgrade floor, and it warned that traffic on affected older app versions would fail. Preserve that notice as snapshot evidence rather than inferring present availability or reconciling it with the page's v7 route.

## Detail locators

- Closed-beta availability and the Mobile SDK certificate warning: raw lines 17-24.
- End-to-end app, Braintree and server responsibility split: raw lines 26-33.
- Connect button asset and controller setup: `Button`, raw lines 36-42.
- `SFSafariViewController` setup using the server-provided Connect URL: `Send the merchant to Braintree`, raw lines 45-67.
- Notification observer and Safari dismissal example: `Prepare for the merchant's return`, raw lines 69-102.
- Custom URL scheme, application-delegate example and prose/code trust-validation conflict: `Capturing the custom URL`, raw lines 104-140.
- Sensitive-data interception warning and return completion: raw lines 142-145.

## Related

- [[braintree]] - provider overview.
- [[braintree-auth]] - provider-specific OAuth connection hub and security boundaries.
- [[source-braintree-auth-server-side-node]] - server-side Connect URL and state-handling route.
- [[source-braintree-auth-oauth-flow-node]] - authorization-code exchange and token-lifecycle route.

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/client-side/ios/v7-2026-09-16|Braintree Auth client-side Connect flow for iOS v7 (collected 2026-09-16)]]
