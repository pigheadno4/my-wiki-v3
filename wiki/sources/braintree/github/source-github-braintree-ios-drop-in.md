---
title: "GitHub: braintree/braintree-ios-drop-in"
type: source
date_ingested: 2026-08-13
original_format: github-repo
raw_files:
  - "github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/manifest.json"
tags: [braintree, ios, mobile-sdk, drop-in, paypal, venmo, apple-pay, 3d-secure, github-repository]
---

## Overview

`BraintreeDropIn@9.14.0` is the first retained exact-SHA baseline for Braintree's prebuilt iOS payment-selection UI. It presents cards, PayPal, Venmo, and Apple Pay when the merchant configuration, device, and request permit them, and normally returns a payment-method nonce for merchant-server processing.

Repository: <https://github.com/braintree/braintree-ios-drop-in>

## Version and Dependency Boundary

The retained tag resolves to SHA `d951d104ac960188824bda191be2f57c57351a31` and was released on 2025-03-06. It supports iOS 12+, Xcode 15+, and Swift 5.9. Exact `9.14.0` only raises the underlying `braintree_ios` requirement to 5.27.0; CocoaPods constrains its Braintree modules to the 5.27 line.

This repository is independently versioned from `braintree/braintree_ios`. The separately retained `braintree-ios@7.9.0` source is newer modular-SDK evidence and must not be attributed to this Drop-in release. In particular, v7 authorization, universal-link, and module behavior require separate verification before being applied to Drop-in.

## Grounding Excerpts

> "Present `BTDropInController` to collect the customer's payment information and receive the `nonce` to send to your server."
>
> `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/README.md:61`

> "Selecting Apple Pay does not display the Apple Pay sheet or create a nonce."
>
> `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/README.md:89`

> "Drop-in does not officially support SwiftUI at this time."
>
> `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/README.md:217`

## Selection and Server Handoff

Merchants initialize `BTDropInController` with a client token or tokenization key and a `BTDropInRequest`. Drop-in loads remote merchant configuration, filters the available methods, and returns a `BTDropInResult` containing the selected type, display metadata, and usually a nonce. The merchant sends that nonce to its Braintree server integration to perform the transaction.

A customer-scoped client token lets Drop-in display saved payment methods. By default, new methods are added to that customer's vault; enabling `vaultManager` also allows the customer to delete vaulted methods. `BTDropInResult.deviceData` is collected through PayPal Data Collector and should be handed to the server as a risk input, not treated as proof that a fraud product is enabled.

## Payment Methods

- Cards use the bundled form, validation, localization, card-brand filtering, optional cardholder name, optional vaulting, and configurable card-logo visibility.
- PayPal defaults to a vault request when the merchant does not supply a request. A merchant can supply its own Braintree PayPal request to control the flow.
- Venmo is shown only when it is not disabled, the Venmo iOS app is available for app switch, and remote merchant configuration enables Venmo. If no Venmo request is supplied, Drop-in creates one with `vault = true`.
- Apple Pay is offered when enabled and device-capable, but selecting it only returns the Apple Pay method type. The merchant must present the Apple Pay sheet, tokenize the resulting `PKPayment`, and send that nonce server-side.

Source presence and a visible payment option do not prove merchant enablement, buyer eligibility, regional availability, or successful server processing.

## 3D Secure and UI Boundary

Attaching a `BTThreeDSecureRequest` makes Drop-in run 3D Secure for card selection before returning the nonce. The merchant remains responsible for constructing the request and deciding how to handle liability outcomes.

Drop-in is UIKit-based and offers UI colors, fonts, navigation styling, localized strings, and payment-method ordering through its fixed selection experience. The repository includes SwiftUI wrapper examples, but its README explicitly says SwiftUI is not officially supported.

## Release Findings

Exact `9.14.0` has no new checkout feature: it requires `braintree_ios` 5.27.0. Historical repository notes establish earlier v9 additions and fixes, including privacy manifests, card-logo hiding, no-recent-method errors, `deviceData`, and the v9 request/API migration. Those entries are historical context, not separately retained exact-SHA baselines.

## Evidence Boundaries

The capsule retains public and implementation source, demo and SwiftUI wrapper examples, localization, package metadata, and the repository changelog. Tests, fixtures, CI, and binary assets are excluded. Generated vector-art implementations were hash-audited and contain presentation-only drawing code; they do not establish payment behavior.

No prior exact-SHA Drop-in snapshot exists in the wiki. Version-to-version claims before `9.14.0` rely on the repository changelog rather than retained source comparisons.

## Related

- [[changelog-github-braintree-ios-drop-in]] - package-qualified iOS Drop-in release ledger
- [[source-github-braintree-ios]] - independently versioned modular Braintree iOS SDK
- [[braintree-ios-sdk]] - native iOS SDK and Drop-in concept boundary
- [[braintree-web-drop-in]] - independently versioned browser Drop-in
- [[braintree]] - company and knowledge-status page

## Raw Sources

- Snapshot manifest: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/manifest.json`
- Release manifest: `raw/github/braintree/braintree-ios-drop-in/releases/braintreedropin/9.14.0/2026-08-13/manifest.json`
- Release notes: `raw/github/braintree/braintree-ios-drop-in/releases/braintreedropin/9.14.0/2026-08-13/release-notes.md`
- README: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/README.md`
- Repository changelog: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/CHANGELOG.md`
- Package manifest: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/Package.swift`
- Public API: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/Sources/BraintreeDropIn/Public/BraintreeDropIn/`
- Payment selection: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/Sources/BraintreeDropIn/BTPaymentSelectionViewController.m`
