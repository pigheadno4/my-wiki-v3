---
title: "Adyen Sessions flow integration guide"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/build-your-integration/sessions-flow"
raw_files:
  - "adyen/docs/online-payments/build-your-integration/sessions-flow/2026-09-15.md"
tags: [adyen, online-payments, sessions, drop-in, components]
---

## Overview

This 2026-09-15 snapshot of the Adyen Sessions flow guide covers Web Drop-in and Components, iOS and Android Drop-in and Components, React Native Drop-in, and Flutter Drop-in and Components. The Web Hosted Checkout tab has no substantive guide content in this raw snapshot. It is a client/server integration guide: the merchant payment server creates a Checkout API session, the client uses its `id` and `sessionData` to show payment UI and handle shopper actions, and the webhook server receives the payment outcome. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The merchant server creates a session with `/sessions`; the guide marks `merchantAccount`, `amount`, `returnUrl`, and `reference` required. `countryCode`, `channel`, `shopperLocale`, shopper identifiers, and other fields have platform or use-case qualifications. The response passes `id` and `sessionData` to the client. A session expires after one hour by default and cannot be set beyond 24 hours.
- Web v6 Drop-in or Components configure `AdyenCheckout` with session data, environment, displayed amount, country/locale and client key, then mount the payment UI. Web redirect returns append `sessionId` and `redirectResult` to `returnUrl`; the client can submit the redirect result, or an extra server endpoint can confirm it. If the shopper does not return, wait for the webhook.
- Updating a session amount is a Checkout API v72+ feature. The initial session uses `payable: false`; the merchant server supplies the final amount for PATCH `/sessions/{sessionId}`, returns updated `sessionData`, and setting `payable: true` prevents further updates. The page names `onSubmit` as required for amount changes in one Web configuration table but its amount-update procedure uses `beforeSubmit`; treat that callback choice as an unresolved version/guide inconsistency.
- iOS uses `AdyenSession` with Drop-in or method Components and app URL handlers for redirects. Android uses `CheckoutSessionProvider` with Compose or non-Compose Drop-in/Components and, for Components redirects, an activity intent filter and `handleIntent`. React Native Drop-in has platform return handlers and requires dismissing its UI from completion/error callbacks. Flutter has platform-specific return URL setup; its Components InstantComponent example calls an `advanced` method inside this Sessions guide, so do not treat that snippet alone as a verified Sessions recipe.
- Client callbacks and optional GET `/sessions/{id}?sessionResult=...` support showing the shopper a current result. The guide says the GET response's `status` is not updated, so it is not a polling endpoint. Use asynchronous `AUTHORISATION` webhooks, matched by `merchantReference`, to update the order system. An authorization outcome does not itself establish capture or settlement.
- The React Native section says Drop-in v1 and Components v1/v2 support only Advanced flow; this page's Sessions guidance is for its React Native Drop-in v2 path. The guide mixes Checkout API example versions v70, v71 and v72, server library versions, and platform environment names. Those examples establish snapshot navigation, not a universal compatible version set or current merchant availability.

## Detail locators

- Web v6 scope, prerequisites and three integration roles: lines 19–95; server API library language tabs: 119–465.
- Web `/sessions` field table, versioned examples and response: lines 466–765; Drop-in installation, configuration, events and method-specific options: 766–1064; Web Components counterpart: 2027–3015.
- Web amount update and irreversible `payable` transition: lines 1514–1613 and 3132–3231; callback wording tension: 895–903 against 1528–1570.
- Web redirects, shopper result, immutable session GET and authorization webhook: lines 1615–1963 and 3233–3581.
- iOS Drop-in and Components, app return handling and result codes: lines 3649–6217. Android Drop-in and Components, Compose/non-Compose setup and redirect intent: lines 6218–8829.
- React Native Drop-in version caveat, platform setup, callbacks and result: lines 8830–10022. Flutter Drop-in and Components setup, return URLs and result: lines 10023–12250; Flutter Components InstantComponent snippet caveat: lines 12030–12048.
- Test/live account, HTTPS for Web, region-matched API/client environments and payment-method setup: Web lines 1965–1997; corresponding mobile go-live sections follow each platform. Capture/refund are linked as next steps, not demonstrated by the session flow.

## Related

- [[source-adyen-docs-online-payments-build-your-integration]] — flow selection and Advanced comparison.
- [[source-adyen-docs-online-payments-build-your-integration-payment-result-codes]] — result-code meanings.
- [[adyen-online-payments]] — provider concept and source route.

## Raw Sources

- [[raw/adyen/docs/online-payments/build-your-integration/sessions-flow/2026-09-15|Adyen Sessions flow integration guide (2026-09-15)]]
