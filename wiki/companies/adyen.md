---
title: "Adyen"
type: company
tags: [adyen, payments, checkout, web-sdk, ios-sdk]
source_count: 2
---

## Overview

Adyen is represented in this wiki by independently versioned Web and iOS checkout SDKs. The retained sources cover browser and native Drop-in and Components, Session and advanced checkout flows, cards, 3D Secure 2 actions, stored and partial payments, wallets, accessibility, analytics, and client-side data boundaries.

## Web checkout surface

- Drop-in provides an all-in-one payment-method list and action flow.
- Components provide individually mounted payment-method experiences.
- Sessions delegate setup and payment orchestration to Adyen's Session endpoints.
- The advanced flow delegates `/payments` and `/payments/details` calls to merchant callbacks.
- Backend payment-method responses and merchant configuration determine what the SDK can present.

## Versioned implementation knowledge

The retained `@adyen/adyen-web@6.41.0` baseline records funding-source-aware cards, Click to Pay and installment conditions, 3DS2 URL and message-origin checks, stored-method filtering, screen-reader behavior, and a PayPal Fastlane adapter.

Repository evidence is not current product eligibility guidance. In particular, the PayPal dependency establishes an adapter boundary; delegated PayPal runtime behavior belongs to the separate PayPal repository history.

## Native iOS checkout surface

The retained `adyen-ios@5.25.1` baseline provides modular Drop-in, Session, Card, Components, Actions, Encryption, SwiftUI, scanner, and native wallet or app-handoff modules. Session can own payments, payment-details, partial-payment, and stored-method calls, while advanced integrations implement those server calls themselves.

Native payment details are submitted through merchant or Session delegates; card and ACH details are encrypted with an Adyen-provided public key. Apple Pay, Cash App Pay, Twint, WeChat Pay, and delegated 3DS/authentication paths each have additional platform or dependency boundaries.

## Knowledge status

- Ingested cumulative GitHub repository sources: 2
- Ingested package releases: 2
- Retained package releases: `@adyen/adyen-web@6.41.0`; `adyen-ios@5.25.1`
- Latest ingest: `adyen-ios@5.25.1` at exact SHA `5f6779b31299e3067de3a5279a816f3b8d2fbdf3`

## Sources

- [[source-github-adyen-web]] — cumulative Adyen Web implementation baseline
- [[changelog-github-adyen-web]] — package-qualified release ledger
- [[source-github-adyen-ios]] — cumulative Adyen iOS implementation baseline
- [[changelog-github-adyen-ios]] — package-qualified native release ledger

## Related

- [[adyen-index]] — Adyen catalog and operations links
- [[adyen-log]] — collection and ingest history
- [[co-badged-cards]] — cross-provider network-choice concept
- [[adyen-ios-sdk]] — native SDK architecture and merchant-server boundaries
