---
title: "Adyen Redirect 3D Secure for iOS Routes"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/redirect-3ds2/ios"
raw_files:
  - "adyen/docs/online-payments/3d-secure/redirect-3ds2/ios/2026-09-15.md"
tags: [adyen, ios, 3d-secure, redirect, drop-in, components]
---

## Overview

This [[adyen]] iOS redirect 3D Secure landing page asks how the merchant wants to integrate and routes to **Drop-in** or **Components** instructions. It is a navigation choice within [[adyen-3d-secure]], not an implementation guide.

## Key takeaways

- The Drop-in link describes an all-in-one UI route for supporting 3D Secure redirect authentication in an iOS app.
- The Components link describes a pre-built Component route for supporting the same iOS redirect authentication. Follow the selected guide for its actual prerequisites, client/server handoffs, API version conditions, testing and result handling.
- This landing page supplies no SDK version, endpoint contract, app-return callback, issuer outcome, authorization, capture or settlement evidence. Its metadata says last modified 2019-10-08; the pinned snapshot was collected 2026-09-15.

## Detail locators

- Purpose and iOS redirect scope: raw lines 15–17.
- Integration choice and Drop-in route: `### How do you want to integrate?`, raw lines 19–23.
- Components route: raw lines 25–27.

## Related

- [[adyen]] — provider context.
- [[adyen-3d-secure]] — provider 3D Secure concept and integration routes.
- [[adyen-ios-sdk]] — separate native online-checkout SDK route; no SDK runtime behavior is established here.
- [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-ios-drop-in]] — selected Drop-in instructions.
- [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-ios-component]] — selected Components instructions.

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/ios/2026-09-15|Adyen iOS redirect 3DS route selector — collected 2026-09-15]]
