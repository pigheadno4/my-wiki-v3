---
title: "Braintree Extend OAuth Client-side Connect Flow for Android v5"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/oauth/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/extend/oauth/client-side/android/v5-2026-09-16.md"
tags: [braintree, braintree-extend, oauth, android, connect, client-side]
---

## Overview

This collected [[braintree]] page is an Android v5 client-side Connect guide under the site's `extend/oauth` route. It describes an app sending a merchant to Braintree-hosted authorization with a server-supplied Connect URL, leaves access-token creation and the return redirect on the platform server, and captures the return in the app with an Android `IntentFilter`. The snapshot labels OAuth closed beta in production and open beta in sandbox. [[braintree-extend-oauth]] owns this Extend OAuth route; it remains distinct from the separate [[braintree-auth]] product despite overlapping connected-merchant OAuth terminology and the page's Braintree Auth contact link.

## Key takeaways

- The recommended Android sequence is described as avoiding exposure of the platform's `client_secret`: the merchant taps Connect with Braintree, the app opens the server-supplied Connect URL using an `Intent`, and, after merchant authorization and server-side access-token creation, the server redirects to a URL captured by the app's `IntentFilter`.
- The supplied Connect button is described as sending merchants to Braintree to log in and agree to the requested OAuth scopes. The downloadable assets and `ImageButton` markup are presentation examples, not evidence that consent occurred, a token was issued, or an action or payment succeeded.
- The return example uses the `/merchant-connected` path in an exported, browsable Android activity. The page says future Android SDK versions will require verification of the app's Intent Filters; it does not establish callback authenticity, successful deep-link verification, or current SDK behavior.
- A historical notice says Braintree Mobile SDK certificates were set to expire on March 30, 2026, names Android SDK 4.45.0+ or 5.0.0+ in a malformed remediation sentence, and warns that customer traffic for affected older app versions would fail unless those versions were decommissioned or force-upgraded. Preserve this as dated snapshot guidance, not proof of the present certificate state, supported versions, current availability, or account eligibility.

## Evidence boundaries

> [!warning] Environment-qualified beta snapshot
> Production closed beta and sandbox open beta are statements from the page collected on 2026-09-16. They do not prove current availability or enablement for a particular platform or merchant.

> [!warning] Client/server and product boundary
> The app launches the server-supplied Connect URL and receives the return route, while the platform server creates the access token and issues the redirect. Do not put the `client_secret` in the app, infer broader OAuth permissions than the merchant approved, or merge this Extend OAuth source into the separate Braintree Auth product route.

## Detail locators

- Production closed-beta and sandbox open-beta availability: raw lines 17-18.
- Historical Mobile SDK certificate notice, March 30, 2026 date, Android 4.45.0+/5.0.0+ wording and traffic-failure warning: raw lines 23-24.
- Android OAuth sequence and app/server responsibility split: `Android OAuth sequence`, raw lines 31-38.
- Connect button purpose, downloadable assets and `ImageButton` example: `Display the button`, raw lines 41-60.
- `Intent` launch using a server-supplied Connect URL: `Send the merchant to Braintree`, raw lines 63-65.
- `/merchant-connected` return and manifest `IntentFilter` example: `Capture the return URL with an intent filter`, raw lines 68-91.
- Future Intent Filter verification note: raw lines 93-94.

## Related

- [[braintree]] - provider overview.
- [[braintree-extend-oauth]] - main Extend OAuth merchant-consent and server credential route.
- [[braintree-payment-platform]] - provider orientation separating Direct, Extend and Auth.
- [[braintree-auth]] - separate connected-merchant OAuth product route; shared terminology does not make the products interchangeable.

## Related raw API references

The following are unread navigation targets named by this page; they are not evidence for claims above.

- [[raw/braintree/docs/guides/extend/oauth/overview-2026-09-16|Braintree Extend OAuth overview (collected 2026-09-16)]]
- [[raw/braintree/docs/guides/extend/oauth/access-tokens/node-2026-09-16|Braintree Extend OAuth access tokens for Node.js (collected 2026-09-16)]]

## Raw Sources

- [[raw/braintree/docs/guides/extend/oauth/client-side/android/v5-2026-09-16|Braintree Extend OAuth client-side Connect flow for Android v5 (collected 2026-09-16)]]
