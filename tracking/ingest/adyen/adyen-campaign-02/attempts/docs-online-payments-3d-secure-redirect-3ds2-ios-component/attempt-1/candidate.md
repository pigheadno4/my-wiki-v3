---
title: "Adyen Redirect 3DS2 iOS Components Integration"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/redirect-3ds2/ios-component"
raw_files:
  - "adyen/docs/online-payments/3d-secure/redirect-3ds2/ios-component/2026-09-15.md"
tags: [adyen, 3d-secure, 3ds2, ios, components, redirect, checkout-api]
---

## Overview

This Adyen Docs snapshot explains redirect 3D Secure 2 authentication for card payments in an iOS app using the Redirect Component and the merchant-server Checkout API `/payments` and `/payments/details` calls. It assumes the merchant has integrated the iOS Card Component or built a card-entry UI. See [[adyen]], [[adyen-3d-secure]], and [[adyen-ios-sdk]]. This unversioned website guide is distinct from the separately versioned [[adyen-3ds2-ios-sdk]] native transaction and challenge runtime.

## Key takeaways

- The iOS card flow collects the card details and additional 3DS2 data, then the merchant server sends `/payments` with `channel: "iOS"`, an app return URL, and browser information. The page marks some fields conditionally required for Visa and JCB, including holder name and shopper IP; it requires shopper email or a qualifying phone number for those transactions. It recommends collecting billing address in advance and says the card schemes require it. The field table and test request are at the raw locator below.
- The merchant checks the `/payments` response. With no `action`, this guide describes the transaction as exempt or outside 3DS scope and routes the `resultCode` to shopper presentation. For a `redirect` action, the merchant passes it to the iOS app and the persisted Redirect Component handles the shopper handoff.
- When the shopper returns to the app, the app delegate informs the Redirect Component. After its `didProvide` callback, the client sends that data to the merchant server, which calls `/payments/details`. The guide distinguishes Checkout API v67 and later, where this call retrieves the result after authentication, from earlier versions, where the call containing payment data completes the payment. Neither the redirect nor the callback alone establishes a successful payment.
- Present the synchronous `resultCode` from `/payments` or `/payments/details`; the payment outcome also arrives asynchronously through a webhook. If manual capture is in use, an `Authorised` result still requires capture.
- For live requests in the same payment session, keep `/payments` and `/payments/details` in the same live endpoint region. The guide warns that mixing regions can cause 3DS authentication errors.

## Detail locators

- Opening and `## Requirements`, raw lines 15–32 — iOS redirect purpose, Card Component or merchant UI prerequisite, and PSD2 guide route.
- `## Collect additional information at checkout`, raw lines 34–53 — holder-name and billing-address guidance.
- `## Make a payment`, raw lines 54–594 — required and conditional 3DS2 request fields, test/API-library examples, and response routing by `action`.
- `## Handle the redirect`, raw lines 595–761 — component persistence, app-return callback, `didProvide`, server `/payments/details`, and Checkout API v67 boundary.
- `## Present the payment result`, raw lines 762–774 — synchronous result codes, webhook, and manual-capture qualification.
- `## Test and go live`, raw lines 775–782 — testing route, go-live route, and same-region live endpoint warning.

## Related

- [[adyen]] — provider page.
- [[adyen-3d-secure]] — merchant 3DS2 integration routes.
- [[adyen-ios-sdk]] — separate package-qualified iOS checkout SDK architecture.
- [[adyen-3ds2-ios-sdk]] — separate native 3DS2 transaction/challenge runtime evidence.
- [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-web-drop-in]] — Web Drop-in redirect guide with a different client return path.

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/ios-component/2026-09-15|Adyen Docs — Redirect 3DS2 iOS Components (2026-09-15 snapshot)]]
