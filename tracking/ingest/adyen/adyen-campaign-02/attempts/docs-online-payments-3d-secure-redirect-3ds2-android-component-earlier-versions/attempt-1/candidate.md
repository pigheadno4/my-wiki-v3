---
title: "Adyen Docs: Android Redirect 3DS2 Component — earlier versions"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/redirect-3ds2/android-component/earlier-versions"
raw_files:
  - "adyen/docs/online-payments/3d-secure/redirect-3ds2/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, 3d-secure, android, redirect, components, earlier-versions]
---

## Overview

This earlier-version Adyen guide explains redirect 3D Secure 2 for card payments in an Android app using the Redirect Component: collect additional shopper data, send a server-side `/payments` request with Android 3DS parameters, hand a redirect `action` to the app, and submit returned details from the server. It routes to [[adyen-3d-secure]]. The page says it describes **Android Drop-in v4.x.x** even though its title and steps refer to Components; keep that wording distinction when selecting integration guidance.

## Key takeaways

- A Card Component or merchant-built card UI is a prerequisite. The page strongly recommends collecting holder name, billing address, and email in advance for authentication performance; its field table distinguishes generally required fields from conditional Visa/JCB fields. In the Card Component path it instructs `holderNameRequired=true`. See raw lines 29–72 for the specific conditions, phone-number fallback and format, `returnUrl` constraints, and browser-information fields.
- If `/payments` has no `action`, this guide calls the transaction exempt or out of scope for 3DS2 and routes to `resultCode`; this is not itself proof of authorization. A `redirect` action goes to the client Redirect Component, which returns `actionComponentData.details` after the shopper comes back.
- **Checkout API version changes the server step.** For v67+, the guide says authentication completion authorizes the payment, and the server calls `/payments/details` to obtain the result. For v66 and earlier, the server must include `paymentData` in `/payments/details` to complete the payment. The v66 action table says to store `action.paymentData` on the server, but the later details bullet describes a value stored in the client app; the snapshot is internally inconsistent about storage location. Resolve that version-specific handoff before implementing an old integration.
- Present the `resultCode` from `/payments` or `/payments/details` and handle the asynchronous payment webhook separately. If the result is `Authorised` and manual capture is configured, capture is still required. The test examples and library snippets in this older guide do not establish current SDK compatibility, live environment configuration, or a completed payment.

## Detail locators

- **Introduction and Requirements, raw lines 17–34** — Android redirect purpose, v4.x.x label, Card Component or own-UI prerequisite, and PSD2 guide route.
- **Collect additional parameters / Make a payment, raw lines 36–72** — recommended shopper data, Card Component setting, Android channel, return URL, browser info, conditional Visa/JCB fields, and phone-number handling.
- **Payment examples, raw lines 75–568** — test endpoint and version-labeled curl, Java, PHP, C#, Node, Go, Python, Ruby, and TypeScript snippets; examples are not version-independent contracts.
- **Checkout API v67+ and v66-earlier response tabs, raw lines 569–632** — no-action versus redirect branches and the older `action.paymentData` handoff.
- **Handle the redirect, raw lines 633–773** — client return, server `/payments/details`, version-dependent completion/result behavior, and response examples.
- **Present the payment result / Test and go live, raw lines 774–789** — result codes, asynchronous webhook, manual-capture follow-up, and test-card route.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[adyen-android-sdk]]
- [[adyen-3ds2-android-sdk]]

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/android-component/earlier-versions/2026-09-15|Adyen Docs — Redirect 3DS Components integration, earlier versions (2026-09-15)]]
