---
title: "Adyen"
type: company
tags: [adyen, payments, checkout, terminal-api, postman, web-sdk, ios-sdk, android-sdk, 3ds2-sdk, react-native-sdk, nodejs, server-sdk]
source_count: 8
---

## Overview

Adyen is represented in this wiki by independently versioned Web, iOS, Android, Android and iOS 3DS2, React Native, and Node.js SDKs plus exact-commit Postman API examples. The retained sources cover browser, native, and cross-platform checkout presentation; delegated mobile 3DS2 authentication runtimes; merchant-server Checkout API v72; and Terminal API payment and shopper-interaction messages.

## Web checkout surface

- Drop-in provides an all-in-one payment-method list and action flow.
- Components provide individually mounted payment-method experiences.
- Sessions delegate setup and payment orchestration to Adyen's Session endpoints.
- The advanced flow delegates `/payments` and `/payments/details` calls to merchant callbacks.
- Backend payment-method responses and merchant configuration determine what the SDK can present.

## Versioned implementation knowledge

The retained Adyen Web history currently runs through `@adyen/adyen-web@6.42.0`. It records funding-source-aware cards, Click to Pay and installment conditions, 3DS2 URL and message-origin checks, stored-method filtering, screen-reader behavior, and a PayPal Fastlane adapter. The retained deltas add OpenInvoice focus isolation, keyboard and IME fixes, Drop-in payment-list analytics, country-aware partial US postal validation, and internal 3DS passkey iframe permissions.

Repository evidence is not current product eligibility guidance. In particular, the PayPal dependency establishes an adapter boundary; delegated PayPal runtime behavior belongs to the separate PayPal repository history.

## Native iOS checkout surface

The retained `adyen-ios@5.25.1` baseline provides modular Drop-in, Session, Card, Components, Actions, Encryption, SwiftUI, scanner, and native wallet or app-handoff modules. Session can own payments, payment-details, partial-payment, and stored-method calls, while advanced integrations implement those server calls themselves.

Native payment details are submitted through merchant or Session delegates; card and ACH details are encrypted with an Adyen-provided public key. Apple Pay, Cash App Pay, Twint, WeChat Pay, and delegated 3DS/authentication paths each have additional platform or dependency boundaries.

## Native Android checkout surface

The retained `adyen-android@5.20.0` baseline provides View and Jetpack Compose variants of modular Drop-in, Components, Sessions, cards, actions, encryption, local payment methods, and external SDK adapters. Sessions can own setup, payments, additional details, partial-payment orders, and stored-method removal; advanced integrations implement the corresponding merchant-server calls.

Card support includes BIN lookup, dual-brand selection, installments, address fields, storage choice, scanning, and public-key encryption. Google Pay, Cash App Pay, Twint, WeChat Pay, and 3DS2 cross separately versioned runtime boundaries and require independent eligibility and dependency evidence.

## Android 3DS2 runtime

The retained `adyen-3ds2-android@2.2.27` baseline documents the delegated transaction and challenge runtime used by Adyen Android. It covers directory-server configuration, encrypted authentication request parameters, `/authorise3ds2` handoffs, Android App Link return handling, challenge outcomes, single-use transaction lifecycle, security warnings, and challenge UI customization.

The exact release claims a Data Safety Guide, challenge-button color correction, improved out-of-band issuer-app launch, and Bouncy Castle `1.84`. The guide is absent from the exact tag and the compatibility table stops at `2.2.26`, so privacy-guide contents and an explicit Android compatibility row remain evidence gaps.

## iOS 3DS2 runtime

The retained `adyen-3ds2-ios@2.4.4` baseline documents the delegated native runtime used by Adyen iOS. It covers binary framework distribution, directory-server setup, encrypted authentication parameters, `/authorise3ds2` handoffs, universal-link return handling, challenge results and errors, multi-scene lifecycle, security warnings, privacy declarations, and challenge UI customization.

The exact release adds Device Information 1.7 support and fixes memory warnings plus navigation behavior for iOS 26. The implementation is retained only as a binary framework with public headers, so code-level verification remains outside the capsule. Its privacy manifest declares non-linked coarse location for app functionality and tracking disabled.

## React Native checkout surface

The retained `@adyen/react-native@2.12.0` baseline wraps Adyen iOS `5.25.1` and Adyen Android `5.19.0`. It exposes Drop-in, individual Components, Sessions and advanced callbacks, follow-up actions, embedded Fabric card UI, Apple Pay, Google Pay, instant payments, and client-side encryption.

The wrapper does not merge the native repositories' histories. Native behavior remains package- and version-qualified, and final payment status remains a merchant-server or Session concern. Apple Pay recurring request configuration is wallet-sheet metadata, not proof of a recurring billing engine.

## Node.js server surface

The retained `@adyen/api-library@32.0.0` baseline provides typed merchant-server clients for Checkout API v72, payment modifications, Sessions, orders, links, stored methods, notifications, and broader Adyen API families. It also introduces Cloud Device API v1 as the first-class cloud point-of-sale path with regional routing, device management, and optional Nexo message protection.

The Node library does not render shopper UI. Its broader API and webhook exports are inventory evidence where the complete generated model trees were not retained; detailed non-checkout queries should trigger focused recollection.

## Postman API examples

The retained `adyen/adyen-postman` baseline at commit `ecb2907c79a0aef2208aa2796a2bd0fc8ffd0cd7` contains generated Checkout v72, Recurring v68, BIN Lookup v54, and Test Card v1 collections plus an unversioned Terminal API collection. Checkout examples cover Sessions, payments, details, modifications, orders, links, stored methods, and utilities. Terminal examples cover 82 payment, refund, input, display, reconciliation, card-acquisition, tipping, instalment, and gift-card requests.

These examples show request shape and intended flow, not current account eligibility. The legacy Recurring collection recommends Checkout recurring endpoints when possible. Terminal capture, recurring token charges, and authorization adjustments belong to Checkout API, while fleet and store administration belong to Management API.

## Knowledge status

- Ingested cumulative GitHub repository sources: 8
- Ingested package releases: 9
- Retained package releases: `@adyen/adyen-web@6.41.0`, `@adyen/adyen-web@6.41.1`, `@adyen/adyen-web@6.42.0`; `adyen-ios@5.25.1`; `adyen-android@5.20.0`; `adyen-3ds2-android@2.2.27`; `adyen-3ds2-ios@2.4.4`; `@adyen/react-native@2.12.0`; `@adyen/api-library@32.0.0`
- Latest ingest: `adyen-3ds2-ios@2.4.4` at exact SHA `00862adbc079d0be943666a4ad2523deb31f9546`

## Sources

- [[source-github-adyen-web]] — cumulative Adyen Web implementation baseline
- [[changelog-github-adyen-web]] — package-qualified release ledger
- [[source-github-adyen-ios]] — cumulative Adyen iOS implementation baseline
- [[changelog-github-adyen-ios]] — package-qualified native release ledger
- [[source-github-adyen-android]] — cumulative Adyen Android implementation baseline
- [[changelog-github-adyen-android]] — package-qualified native release ledger
- [[source-github-adyen-3ds2-android]] — cumulative delegated Android 3DS2 runtime baseline
- [[changelog-github-adyen-3ds2-android]] — package-qualified 3DS2 release ledger
- [[source-github-adyen-3ds2-ios]] — cumulative delegated iOS 3DS2 runtime baseline
- [[changelog-github-adyen-3ds2-ios]] — package-qualified iOS 3DS2 release ledger
- [[source-github-adyen-react-native]] — cumulative Adyen React Native wrapper baseline
- [[changelog-github-adyen-react-native]] — package-qualified wrapper release ledger
- [[source-github-adyen-node-api-library]] — cumulative Adyen Node.js server-library baseline
- [[changelog-github-adyen-node-api-library]] — package-qualified server-library release ledger
- [[source-github-adyen-postman]] — cumulative Checkout, recurring, BIN lookup, test-card, and Terminal API examples
- [[changelog-github-adyen-postman]] — commit-qualified Postman collection history

## Related

- [[adyen-index]] — Adyen catalog and operations links
- [[adyen-log]] — collection and ingest history
- [[co-badged-cards]] — cross-provider network-choice concept
- [[adyen-ios-sdk]] — native SDK architecture and merchant-server boundaries
- [[adyen-android-sdk]] — native Android architecture and merchant-server boundaries
- [[adyen-3ds2-android-sdk]] — native Android 3DS2 transaction and challenge runtime
- [[adyen-3ds2-ios-sdk]] — native iOS 3DS2 transaction and challenge runtime
- [[adyen-react-native-sdk]] — cross-platform wrapper, native dependency, and merchant-server boundaries
- [[adyen-node-api-library]] — Node.js server SDK, Checkout API, Cloud Device, and query boundaries
- [[adyen-terminal-api]] — Nexo terminal messages, in-person flows, and API-family boundaries
