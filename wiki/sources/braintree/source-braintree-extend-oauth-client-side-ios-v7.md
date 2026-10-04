---
title: "Braintree Extend OAuth Client-side Connect Flow for iOS v7"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/oauth/client-side/ios/v7"
raw_files:
  - "braintree/docs/guides/extend/oauth/client-side/ios/v7-2026-09-16.md"
tags: [braintree, oauth, ios, connect, client-side]
---

## Overview

This collected [[braintree]] page is an iOS v7 client-side OAuth Connect guide under the site's `extend/oauth` route. It sends a merchant from an app to Braintree-hosted authorization, leaves access-token creation on the platform server, and returns the merchant to the app through a custom URL scheme. The snapshot says OAuth was closed beta in production and open beta in sandbox. The route and OAuth terminology do not by themselves establish that this is the Braintree Extend payment-data-sharing product; [[braintree-payment-platform]] preserves the provider's separate Direct, Extend and Auth orientations, while [[braintree-auth]] owns the connected-merchant OAuth model.

## Key takeaways

- The iOS-specific sequence recommends presenting Braintree authorization in `SFSafariViewController`. After merchant authorization and server-side access-token creation, the server redirects the merchant to a custom URL captured by the app.
- The supplied Connect button is described as sending merchants to Braintree to log in and agree to requested OAuth scopes. The button assets, Safari controller, notification observer, `CFBundleURLTypes`, and application-delegate handler are implementation examples, not evidence of a completed authorization, a usable token, or payment acceptance.
- The guide prose says the application-delegate function will ensure that the custom URL comes from a trusted source, but the displayed function only posts the received URL and returns `true`; it does not visibly validate `url` or `sourceApplication`. Do not infer callback authenticity from the sample.
- The page explicitly warns against putting sensitive information in the custom return URL because multiple iOS apps can intercept custom URL schemes.
- A historical notice says Braintree Mobile SDK certificates were set to expire on March 30, 2026 and warns that affected older app versions would lose all customer traffic after that date. Its remediation sentence is malformed but names iOS SDK 6.17.0+; retain it as dated snapshot guidance, not proof of current SDK support, certificate state, or account eligibility.

## Detail locators

- Production closed-beta and sandbox open-beta availability: raw lines 17-18.
- Historical Mobile SDK certificate notice and iOS 6.17.0+ wording: raw lines 21-22.
- iOS OAuth sequence and client/server responsibility split: `iOS OAuth sequence`, raw lines 25-32.
- Connect button purpose, assets and view-controller setup: `Display the button`, raw lines 35-43.
- `SFSafariViewController` example using a server-provided Connect URL: `Send the merchant to Braintree`, raw lines 46-72.
- Notification observer and Safari dismissal example: `Prepare for the merchant to return`, raw lines 74-110.
- Custom-scheme configuration, application-delegate example and prose/code trust-validation conflict: `Capture the custom URL`, raw lines 112-151.
- Sensitive-data interception warning and return-event completion statement: raw lines 153-156.

## Related

- [[braintree]] - provider overview.
- [[braintree-auth]] - existing provider-specific connected-merchant OAuth hub.
- [[braintree-payment-platform]] - separate Direct, Extend and Auth product-orientation boundary.

## Related raw API references

The following are unread navigation targets named by this page; they are not evidence for claims above.

- [[raw/braintree/docs/guides/extend/oauth/overview-2026-09-16|Extend OAuth overview (collected 2026-09-16)]]
- [[raw/braintree/docs/guides/extend/oauth/access-tokens/node-2026-09-16|Extend OAuth access tokens for Node (collected 2026-09-16)]]

## Raw Sources

- [[raw/braintree/docs/guides/extend/oauth/client-side/ios/v7-2026-09-16|Braintree Extend OAuth client-side Connect flow for iOS v7 (collected 2026-09-16)]]
