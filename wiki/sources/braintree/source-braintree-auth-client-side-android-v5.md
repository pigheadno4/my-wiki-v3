---
title: "Braintree Auth Client-side Connect Flow (Android v5)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/braintree-auth/client-side/android/v5-2026-09-16.md"
tags: [braintree, braintree-auth, oauth, android, connected-merchants]
---

## Overview

This collected Android v5 guide describes the mobile client portion of a Braintree Auth Connect flow for linking a merchant to a platform without exposing the platform's `clientSecret` in the app. It is an OAuth connection route for a Braintree merchant, not generic payment-transaction authorization; the snapshot labels Braintree Auth closed beta.

## Key takeaways

- The merchant starts from **Connect with Braintree** in the Android app. The app opens the server-supplied `connect_url` in an Android `Intent` and sends the merchant to Braintree for authorization.
- After authorization, Braintree first redirects to the `redirect_uri` specified by the `connect_url`. The server performs the OAuth exchange and then redirects the merchant to a URL captured by the Android app's `IntentFilter`, which launches the configured activity. This preserves the guide's client/server boundary: the app initiates and receives the browser return, while the server supplies the Connect URL and performs the OAuth exchange.
- The page provides button assets and an `ImageButton` example, a manifest `IntentFilter` example, and a `/merchant-connected` return-path example. These are implementation examples from this snapshot, not guarantees of universal configuration.

> [!warning] Closed-beta and evidence boundary
> This 2026-09-16 snapshot labels Braintree Auth closed beta. It documents an Android v5 client-side Connect route, but does not establish current availability, account eligibility, a completed OAuth connection, payment acceptance, or parity with iOS or JavaScript routes.

> [!warning] Mobile SDK certificate notice preserved from the snapshot
> The collected page says Braintree Mobile SDK SSL certificates were set to expire on March 30, 2026, warns that traffic from app versions retaining older certificates would fail, and names Android SDK 4.45.0+ or 5.0.0+ as upgrade targets. Because the page was fetched after that stated date, this is preserved as snapshot evidence rather than a claim about present certificate status or current SDK requirements.

## Detail locators

- Closed-beta label and contact route: `# Client-side Connect Flow > AVAILABILITY`, lines 17-18.
- Mobile SDK certificate-expiry notice, failure consequence and Android version targets: `# Client-side Connect Flow > IMPORTANT`, lines 21-24.
- End-to-end Android client/server Connect sequence: `# Client-side Connect Flow`, lines 26-33.
- Button assets, resource placement and `ImageButton` example: `## Button`, lines 36-53.
- Manifest activity and `IntentFilter` example: `## Intent filters`, lines 55-76.
- Snapshot wording about future Intent Filter verification: `## Intent filters > NOTE`, lines 78-79.
- `Intent`, server-supplied `connect_url` and `/merchant-connected` app return: `## Intent`, lines 82-86.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-auth]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-auth/oauth-flow/node-2026-09-16|Braintree Auth OAuth flow (Node.js)]] - navigation-only route for the OAuth exchange; not read or used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/client-side/android/v5-2026-09-16|Braintree Auth Client-side Connect Flow (Android v5)]] - complete collected guide for the Android client initiation, server exchange and app-return sequence, with closed-beta and mobile-certificate qualifications
