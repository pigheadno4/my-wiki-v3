---
title: "Adyen Mobile POS"
type: concept
category: technology
tags: [adyen, point-of-sale, mobile-pos, in-person-payments]
---

## Definition

Adyen's Mobile POS documentation covers in-person payment solutions using a merchant mobile device. The 2026-09-15 Android overview describes accepting payment on an Android device such as a phone, or using the mobile device with a card reader. It names Tap to Pay on Android, Card reader on Android, and Android Payments app as distinct Android solution routes. This hub does not itself establish the implementation or eligibility conditions for any route.

## Evidence boundary

The Android overview sends readers to separate requirements, security, checklist, build, management and error guides. It does not state device/OS or regional support, SDK/API versions, account eligibility, go-live approval, or successful payment execution. Keep this mobile-device route distinct from [[adyen-android-terminals]] (apps on Adyen payment terminals), [[adyen-android-sdk]] (native online checkout), and the device-specific [[adyen-mobile-card-readers]] concept. An iOS Mobile POS overview can contribute a separate source route after its own evidence review.

## iOS Repository Baseline: `AdyenPOS@3.22.0`

The separately versioned `adyen/adyen-pos-mobile-ios` repository supplies binary SDK distribution metadata and SwiftUI/UIKit integration samples, not the SDK's internal implementation. Its 3.22.0 sample targets link `AdyenPOSTEST`; the manifest also declares LIVE products. This is merchant-device in-person payment evidence, distinct from [[adyen-ios-sdk]] for online checkout. See [[source-github-adyen-pos-mobile-ios]] and [[changelog-github-adyen-pos-mobile-ios]].

The shared model retains PaymentService and its delegate, obtains installationId, encodes a Terminal API payment request, selects tapToPay or cardReader and performs the transaction. SwiftUI uses viewModifier with transactionModal; UIKit presents from a view controller. Warm-up errors are suppressed and responses/errors are printed, not reconciled as a production payment outcome. The resolved TerminalAPIKit dependency belongs to another repository and is not part of this implementation evidence.

> [!warning] Contradiction
> The sample registration comment says to supply setupToken to the merchant backend, but the implementation does not put it in the request. It uses a placeholder URL and ignores HTTP status. Follow the backend session requirement, not this incomplete snippet as a working session integration. The exact code and evidence limits are retained in [[source-github-adyen-pos-mobile-ios]].

The 3.22.0 release notes announce language/fallback/UI corrections and an NYC1 PIN support expiry of 2027-04-13; that is not a universal Tap to Pay or all-version expiry. README links still target 3.21.0 documentation. Sample target iOS 18.4 settings, entitlement-file presence and binary checksums do not independently prove current SDK requirements, Apple provisioning, regional/live enablement or successful payments.

## Independent TEST-Only iOS Repository: `AdyenPOS@3.22.0`

The separate `adyen/adyen-pos-mobile-ios-test` release at SHA `5e2234351d6164f11911d09efed4630fe82e0050` distributes only AdyenPOSTEST and ADYPOSTEST for the Adyen TEST environment. It shares the package name/version with the main repository, not its repository identity or evidence history. Its seven retained sample Swift files match the main repository's baseline; this is not a newer payment-flow implementation. See [[source-github-adyen-pos-mobile-ios-test]] and [[changelog-github-adyen-pos-mobile-ios-test]].

This TEST snapshot adds an important configuration distinction: its SwiftUI target declares Bluetooth/camera usage descriptions and has no target deployment override, leaving project-level iOS 17.0 applicable in the retained settings; UIKit explicitly sets 18.4. The main repository's four target configurations instead explicitly set 18.4. Neither snapshot proves the SDK's actual supported OS floor, successful signing or payment execution. Declared TEST binary checksums match across the manifests, but downloaded binary contents were not compared.

> [!warning] Contradiction
> This TEST repository has the same unfinished registration contract: comments require sending setupToken to a merchant backend, while the code never forwards it, uses a placeholder URL and ignores HTTP status. Its own source [[source-github-adyen-pos-mobile-ios-test]] retains the reciprocal warning; do not treat matching sample code as a working session integration.

Release announcements and stale 3.21.0 README documentation links are preserved separately for this exact TEST release. TEST-only metadata is not live-environment enablement evidence.

## Sources

- [[source-github-adyen-pos-mobile-ios-test]] - independent TEST-only 3.22.0 binary distribution and sample/build-setting baseline.
- [[changelog-github-adyen-pos-mobile-ios-test]] - repository-qualified TEST release history, separate from the main distribution.

- [[source-github-adyen-pos-mobile-ios]] — exact-SHA AdyenPOS 3.22.0 distribution and complete integration samples, with incomplete-registration and binary-runtime boundaries.
- [[changelog-github-adyen-pos-mobile-ios]] — package-qualified initial baseline and version-specific release announcements.

- [[source-adyen-docs-point-of-sale-firmware-release-notes]] — 2026-09-15 release-note snapshot with separate iOS SDK, Android SDK and Android Payments app histories; use version-specific expiry/removal or support cutoffs, transaction-blocking notices and breaking-change locators, not this route as proof of current integration eligibility.


- [[source-adyen-docs-point-of-sale-mobile-android-requirements]] — 2026-09-15 Android Mobile device/OS/security requirements and card-reader/dock-specific NYC1, PIN, SDK and firmware gates; region and method availability remain separate.


- [[source-adyen-docs-point-of-sale-mobile-ios-build]] — 2026-09-15 iOS Mobile self-build landing page for shared SDK and conditional Tap to Pay/card-reader coexistence, server session and Terminal API tasks, and the two detailed build routes.


- [[source-adyen-docs-point-of-sale-mobile-android-build]] — Android Mobile build overview (2026-09-15 snapshot) for embedded SDK Tap-to-Pay/card-reader work versus separate Payments app Terminal API and boarding route.


- [[source-adyen-docs-point-of-sale-mobile-ios-security]] — iOS Mobile security guide (2026-09-15 snapshot) for Tap to Pay MPoC/iOS-version scope, shared SDK encryption/attestation and server-key practices, and SDK 3.18.0 passcode enforcement with offline-payment loss on removal.


- [[source-adyen-docs-point-of-sale-mobile-android-security]] — Android Mobile security guide (2026-09-15 snapshot) for SDK attestation/encryption claims, server-held credentials, insecure-Wi-Fi cancellation and distinct PCI MPoC assessment scope for SDK integrations versus the Payments app.


- [[source-adyen-docs-point-of-sale-mobile-ios-requirements]] — 2026-09-15 iOS Mobile POS requirements for device/passcode and offline-data risk, iOS/SDK floors, NYC1 PIN versus NYC1-SCR, dock firmware and separate region/payment-method gates.


- [[source-adyen-docs-point-of-sale-mobile-ios-checklists]] — iOS Mobile test/go-live checklist (2026-09-15 capture) for solution availability, test and live account gates, Tap to Pay Apple entitlement, scoped reader/dock steps, live SDK/API credential roles, expiry monitoring and penny-test route.


- [[source-adyen-docs-point-of-sale-mobile-ios-understand]] — iOS Mobile SDK concept guide (2026-09-15 snapshot) for backend communication session, Terminal API transaction flow, PIN presentation and reader/dock UI boundaries.


- [[source-adyen-docs-point-of-sale-mobile-android-checklists]] — Adyen Android Mobile get-started/go-live checklists (2026-09-15 snapshot) for solution, test/live account, contract, SDK-versus-Payments-app credential, update, penny-test and optional dock gates.


- [[source-adyen-docs-point-of-sale-ipp-mobile]] — Adyen Docs Mobile POS comparison captured 2026-09-15 for Android/iOS Tap-to-Pay and card-reader interfaces, SDK versus Android Payments app, and region/method/feature matrices.


- [[source-adyen-docs-point-of-sale-mobile-ios-troubleshooting]] — 2026-09-15 iOS Mobile POS device-attestation and Swift SDK error guide for Tap to Pay and NYC1 reader paths, including offline-data loss, session backoff and stage-specific remedies.


- [[source-adyen-docs-point-of-sale-mobile-android-troubleshooting]] — 2026-09-15 Android Mobile troubleshooting table for Android Mobile SDK device attestation and separate Android Payments app UI/App Link errors, including boarding, request and after-payment stages.


- [[source-adyen-docs-point-of-sale-mobile-android-understand]] — Android Mobile solution comparison (2026-09-15 webpage snapshot): embedded SDK for Tap to Pay/card reader versus separate Tap-to-Pay-only Payments app, with distinct session, App Link, PIN, reader-UI and kiosk conditions.


- [[source-adyen-docs-point-of-sale-mobile-ios-manage]] — 2026-09-15 iOS Mobile POS management guide for Tap to Pay terms, SDK expiry/removal, minimum iOS gating, and reader/dock firmware duties, each with solution-specific scope.


- [[source-adyen-docs-point-of-sale-mobile-android-manage]] — Android Mobile management guide (2026-09-15 capture) for live app registration, scoped SDK/Payments-app expiry effects, OS and reader/dock update conditions, and notification routes.


- [[source-adyen-docs-point-of-sale-mobile-ios-build-card-reader]] — iOS POS Mobile SDK card-reader build guide (2026-09-15 snapshot): Terminal API session/payment/refund integration, NYC1 Bluetooth or USB dock management, test/live separation and simulator limits.


- [[source-adyen-docs-point-of-sale-mobile-android-build-payments-app]] — Android Payments app build guide (2026-09-15 webpage snapshot): separate app and Terminal API App Link boarding/payment route, browser short response, reboarding and revocation; distinct from POS Mobile SDK and card-reader paths.


- [[source-adyen-docs-point-of-sale-mobile-ios-build-tap-to-pay]] — 2026-09-15 iOS Mobile SDK Tap to Pay on iPhone build guide for the merchant POS app, Apple entitlement and terms, Terminal API/session setup, payment, refund, diagnosis and live-environment steps.


- [[source-adyen-docs-point-of-sale-mobile-android-build-tap-to-pay]] — Tap to Pay on Android Mobile SDK build guide (2026-09-15 snapshot): COTS Android NFC, Terminal API/session credentials, payment/refund/diagnosis/session flows, and test/live boundaries.


- [[source-adyen-docs-point-of-sale-mobile-android-build-card-reader]] — Android Mobile SDK Card reader build guide (2026-09-15 snapshot) for NYC1 reader integration, session, device management, Terminal API transactions and refunds.


- [[source-adyen-docs-point-of-sale-mobile-ios]] — 2026-09-15 Adyen iOS Mobile solutions overview for merchant iOS POS app initiation, Tap to Pay on iPhone versus paired card-reader interface, and their shared Mobile SDK with Terminal API prerequisite.


- [[source-adyen-docs-point-of-sale-mobile-android]] — Android Mobile solutions overview captured 2026-09-15; three solution routes and navigation to conditions and lifecycle guides.
