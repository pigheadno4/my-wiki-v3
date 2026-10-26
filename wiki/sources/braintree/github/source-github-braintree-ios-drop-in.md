---
title: "GitHub: braintree/braintree-ios-drop-in"
type: source
date_ingested: 2026-08-13
date_updated: 2026-10-27
original_format: github-repo
raw_files:
  - "github/braintree/braintree-ios-drop-in/snapshots/2026-10-27-ae66bc6/manifest.json"
  - "github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/manifest.json"
tags: [braintree, ios, mobile-sdk, drop-in, paypal, venmo, apple-pay, 3d-secure, github-repository]
---

## Overview

`BraintreeDropIn@9.14.0` is the first retained exact-SHA baseline for Braintree's prebuilt iOS payment-selection UI. It presents cards, PayPal, Venmo, and Apple Pay when the merchant configuration, device, and request permit them, and normally returns a payment-method nonce for merchant-server processing.

Repository: <https://github.com/braintree/braintree-ios-drop-in>

## Version and Dependency Boundary

The additive documentation ref `default-branch@ae66bc6` was ingested 2026-10-27. It does not replace or advance the package release `BraintreeDropIn@9.14.0`; the original implementation and dependency findings below remain that release's historical baseline.

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

## Documentation Delta: `default-branch@ae66bc6`

Approved delta `github-fce4c89c9e41ed166c99`, from `d951d104ac960188824bda191be2f57c57351a31` to `ae66bc646250711940d72834caab3c377d485879`; collected and ingested 2026-10-27. The ending commit is dated 2026-04-23, not a newly published October release. `BraintreeDropIn@9.14.0` remains the retained package release.

### Lifecycle and Migration Notice

- The exact-SHA README schedules deprecated status and no further SDK updates from September 1, 2026. It states processing remains supported for one year after that date.
- Unsupported status is scheduled for September 1, 2027, with Braintree developer/support assistance ending and processing subject to suspension at any time. This is not proof that processing automatically stops on that date, or that any merchant transaction currently succeeds.
- The stated migration target is the modular Braintree iOS SDK, not a new Drop-in release. This delta supplies no migration implementation and does not prove Drop-in compatibility with the separately versioned modular SDK.
- The versions table changes v9 from Active/TBA/TBA to Inactive/September 2026/September 2027, and fills v8's unsupported date as April 2023. The latter is retrospective documentation, not a newly unsupported v8 event in October 2026.

> [!warning] Contradiction
> The original `9.14.0` README lists v9 as Active with TBA dates; the later ref adds dated September 2026/2027 notices but still labels it Inactive and retains active-development prose. As of ingest, the September 2026 milestone has passed; stale labels do not extend the stated dates. Separately, [[source-braintree-drop-in-setup-and-integration-ios-v7]] preserves a 2026-09-16 website snapshot specifying October 1, 2026/2027 instead. The repository commit predates that website capture, but neither chronology nor this delta establishes which policy is currently authoritative. Preserve both source-specific schedules and reverify current provider guidance rather than silently selecting a date.

### Evidence and Reading Limits

Both capsules contain 203 files. Only README changes; the other 202 retained files, including payment implementation, package metadata and changelog, are identical. All 406 file sizes, SHA-256 hashes and Git blob identities were verified. The policy-bounded comparison does not inventory the whole upstream tree: repository workflow/security changes observed during online recheck are outside this capsule and are not ingested security-policy evidence.

User approved focused reading: old/new README, comparison and cumulative source/changelog read fully; manifests verified mechanically and relevant shared company/index/log sections read. All `9.14.0` history remains. No SDK build, dependency resolution, device test, payment execution, automatic upgrade, commit or push.

### Located Grounding

Under `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-10-27-ae66bc6/files/README.md`:

- Line 9: "September 1, 2026" - deprecation milestone.
- Line 11: "September 1, 2027" - unsupported milestone.
- Line 11: "Processing for unsupported SDKs can be suspended at any time."

## Related

- [[changelog-github-braintree-ios-drop-in]] - package-qualified iOS Drop-in release ledger
- [[source-github-braintree-ios]] - independently versioned modular Braintree iOS SDK
- [[braintree-ios-sdk]] - native iOS SDK and Drop-in concept boundary
- [[braintree-web-drop-in]] - independently versioned browser Drop-in
- [[braintree]] - company and knowledge-status page

## Raw Sources

- Documentation-ref snapshot: [manifest](raw/github/braintree/braintree-ios-drop-in/snapshots/2026-10-27-ae66bc6/manifest.json)
- Documentation-ref README: [exact raw](raw/github/braintree/braintree-ios-drop-in/snapshots/2026-10-27-ae66bc6/files/README.md)
- Exact ref comparison: [manifest](tracking/github/repos/braintree/braintree-ios-drop-in/comparisons/default-branch/d951d10--ae66bc6/comparison.json), [review](tracking/github/repos/braintree/braintree-ios-drop-in/comparisons/default-branch/d951d10--ae66bc6/comparison.md), [patch](tracking/github/repos/braintree/braintree-ios-drop-in/comparisons/default-branch/d951d10--ae66bc6/diff.patch)

- Snapshot manifest: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/manifest.json`
- Release manifest: `raw/github/braintree/braintree-ios-drop-in/releases/braintreedropin/9.14.0/2026-08-13/manifest.json`
- Release notes: `raw/github/braintree/braintree-ios-drop-in/releases/braintreedropin/9.14.0/2026-08-13/release-notes.md`
- README: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/README.md`
- Repository changelog: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/CHANGELOG.md`
- Package manifest: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/Package.swift`
- Public API: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/Sources/BraintreeDropIn/Public/BraintreeDropIn/`
- Payment selection: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/Sources/BraintreeDropIn/BTPaymentSelectionViewController.m`
