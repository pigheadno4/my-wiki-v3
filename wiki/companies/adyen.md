---
title: "Adyen"
type: company
tags: [adyen, payments, checkout, web-sdk, ios-sdk, android-sdk, react-native-sdk, nodejs, server-sdk]
source_count: 5
---

## Overview

Adyen is represented in this wiki by independently versioned Web, iOS, Android, React Native, and Node.js checkout SDKs. The retained sources cover browser, native, and cross-platform checkout presentation plus merchant-server Checkout API v72, request transport, notifications, recurring operations, and Cloud Device API v1.

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

## React Native checkout surface

The retained `@adyen/react-native@2.12.0` baseline wraps Adyen iOS `5.25.1` and Adyen Android `5.19.0`. It exposes Drop-in, individual Components, Sessions and advanced callbacks, follow-up actions, embedded Fabric card UI, Apple Pay, Google Pay, instant payments, and client-side encryption.

The wrapper does not merge the native repositories' histories. Native behavior remains package- and version-qualified, and final payment status remains a merchant-server or Session concern. Apple Pay recurring request configuration is wallet-sheet metadata, not proof of a recurring billing engine.

## Node.js server surface

The retained `@adyen/api-library@32.0.0` baseline provides typed merchant-server clients for Checkout API v72, payment modifications, Sessions, orders, links, stored methods, notifications, and broader Adyen API families. It also introduces Cloud Device API v1 as the first-class cloud point-of-sale path with regional routing, device management, and optional Nexo message protection.

The Node library does not render shopper UI. Its broader API and webhook exports are inventory evidence where the complete generated model trees were not retained; detailed non-checkout queries should trigger focused recollection.

## Knowledge status

- Ingested cumulative GitHub repository sources: 5
- Ingested package releases: 7
- Retained package releases: `@adyen/adyen-web@6.41.0`, `@adyen/adyen-web@6.41.1`, `@adyen/adyen-web@6.42.0`; `adyen-ios@5.25.1`; `adyen-android@5.20.0`; `@adyen/react-native@2.12.0`; `@adyen/api-library@32.0.0`
- Latest ingest: `@adyen/adyen-web@6.42.0` at exact SHA `1e157f8bc62b9519d68becedd9c1267180810e77`

## Sources

- [[source-github-adyen-web]] — cumulative Adyen Web implementation baseline
- [[changelog-github-adyen-web]] — package-qualified release ledger
- [[source-github-adyen-ios]] — cumulative Adyen iOS implementation baseline
- [[changelog-github-adyen-ios]] — package-qualified native release ledger
- [[source-github-adyen-android]] — cumulative Adyen Android implementation baseline
- [[changelog-github-adyen-android]] — package-qualified native release ledger
- [[source-github-adyen-react-native]] — cumulative Adyen React Native wrapper baseline
- [[changelog-github-adyen-react-native]] — package-qualified wrapper release ledger
- [[source-github-adyen-node-api-library]] — cumulative Adyen Node.js server-library baseline
- [[changelog-github-adyen-node-api-library]] — package-qualified server-library release ledger

## Related

- [[adyen-index]] — Adyen catalog and operations links
- [[adyen-log]] — collection and ingest history
- [[co-badged-cards]] — cross-provider network-choice concept
- [[adyen-ios-sdk]] — native SDK architecture and merchant-server boundaries
- [[adyen-android-sdk]] — native Android architecture and merchant-server boundaries
- [[adyen-react-native-sdk]] — cross-platform wrapper, native dependency, and merchant-server boundaries
- [[adyen-node-api-library]] — Node.js server SDK, Checkout API, Cloud Device, and query boundaries
