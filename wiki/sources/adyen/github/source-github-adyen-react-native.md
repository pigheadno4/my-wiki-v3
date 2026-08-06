---
title: "GitHub: Adyen/adyen-react-native"
type: source
date_ingested: 2026-08-02
original_format: github-repo
raw_files:
  - "github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/manifest.json"
tags: [adyen, react-native, mobile-sdk, drop-in, components, sessions, apple-pay, google-pay, github-repository]
---

## Overview

`Adyen/adyen-react-native` publishes `@adyen/react-native`, a React Native wrapper over the native Adyen iOS and Android checkout SDKs. It exposes prebuilt Drop-in, individual Components, Session and advanced flows, follow-up actions, embedded card UI, native wallets, client-side encryption, and React Native-to-native event routing. This cumulative page begins with `@adyen/react-native@2.12.0` at exact SHA `2912c913266b2d1df73882980303b563ea04ab63`.

Repository: <https://github.com/Adyen/adyen-react-native>

## Evidence boundary

- The complete retained capsule contains 301 public, production, configuration, documentation, example, and story files. Tests, generated output, binaries, and lockfiles are excluded by policy.
- The immutable GitHub release, tag, and package record establish `@adyen/react-native@2.12.0`. The tagged tree's `package.json` still contains the release-build placeholder `2.0.0-local.1`, so that local field is not used as the release identity.
- The wrapper delegates runtime payment behavior to Adyen iOS `5.25.1` and Adyen Android `5.19.0`. This page proves the wrapper and adapter boundary, not every behavior of the native SDKs or their delegated dependencies.
- Exported Components and payment-method models do not prove merchant enablement, regional eligibility, shopper availability, or final payment status. Backend responses and server-side verification remain authoritative.

## Grounding excerpts

> "Adyen React Native provides you with the building blocks to create a checkout experience for your shoppers"
>
> `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/README.md:22-24`

> "Drop-in" is an all-in-one native iOS and Android wrapper, while "Components" provide one Component per payment method for a merchant-owned flow.
>
> `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/README.md:26-29`

> "Call your server to make the `/payments` request" and "Call your server to make the `/payments/details` request."
>
> `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/README.md:328-337`

> "Each embedded view instance uses its reactTag (view ID) as the bus registration key, enabling multiple views of the same type to coexist."
>
> `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/docs/Architecture.md:389-397`

> "PayByBank is now available as a standalone payment component" and Apple Pay configuration supports `merchantCapabilities`.
>
> `raw/github/adyen/adyen-react-native/releases/react-native/2.12.0/2026-08-01/release-notes.md:5-9`

## Package and platform status

| Package | Latest ingested release | Exact SHA | Native baselines |
| --- | --- | --- | --- |
| `@adyen/react-native` | `2.12.0` | `2912c913266b2d1df73882980303b563ea04ab63` | iOS `5.25.1`; Android `5.19.0` |

This table reports wiki ingest progress, not the latest version currently published upstream.

The package exports React Native source from `src/index.ts`, built CommonJS and module artifacts from `lib/`, and generated TypeScript declarations. It declares React Native `>=0.76.0`, optional Expo `>=52`, and New Architecture code generation for embedded card and platform-pay views.

New Architecture support requires React Native `0.76.0` or later. Older supported applications use the old architecture or disable bridgeless mode, with extra compatibility requirements below `0.74`. Expo Go is unsupported; Expo integrations use Continuous Native Generation. Manual iOS and Android setup must register redirect return handling, and Android requires a Material Components theme.

## Integration modes and server boundary

`AdyenCheckout` supplies configuration, payment methods or a Session, lifecycle callbacks, and checkout context to child components. `useAdyenCheckout()` exposes `start(typeName)`, configuration, available methods, and readiness.

With Sessions, the merchant backend first creates a Session. The wrapper creates a native Session context and uses its payment-method response. `onComplete` receives a session result, but the README directs the merchant to query the Session result on its server before relying on the payment outcome.

In the advanced flow, the merchant provides `/paymentMethods`, sends `onSubmit` data to its server for `/payments`, sends `onAdditionalDetails` data for `/payments/details`, and passes a returned action to the Component. `PaymentMethodData` and `PaymentDetailsData` are request inputs, not proof of authorization or capture.

## Architecture and lifecycle

The TypeScript layer exports checkout components, core types and configuration, hooks, Drop-in, Apple Pay, Google Pay, instant-payment, action, and CSE modules. Native Android and iOS modules wrap their respective Adyen SDK Components and translate native callbacks into React Native events.

Modal Components follow an optional Session setup, open, event, and hide lifecycle. Shared native state tracks the Session and active module so Session completion and cleanup can reach the presented Component. Callbacks should be memoized to avoid unnecessary listener replacement.

Embedded `CardView` is a Fabric native component driven by React props rather than modal `open()` and `hide()` calls. Each view registers its React tag with an embedded-component bus; tagged events route actions, address updates, submission, and cleanup to the correct instance. Android disposes per-view state when React drops the view, while iOS tears down the contained view-controller hierarchy when the view is recycled.

## Components, actions, and payment data

Drop-in presents the available methods as one checkout surface. Individual wrappers select a matching payment method and open the corresponding native Component. The retained public modules also expose standalone Apple Pay, Google Pay, instant payment, follow-up action, and client-side-encryption paths.

Follow-up `PaymentAction` models cover redirects, vouchers, QR codes, 3DS2 tokens, and external SDK data. Components can handle an action returned by `/payments`; API-only integrations can use `AdyenAction.handle` and then submit the resulting details to the merchant server.

Card configuration covers holder name, billing address, address lookup, storage field, CVC, installments, and BIN callbacks. Event contracts also cover stored-method removal, balance checks, partial-payment order creation or cancellation, Session completion, and Apple Pay shipping or coupon changes. These callbacks establish client orchestration points; the merchant or Session service owns durable payment and order state.

## Wallets and configuration

The root configuration includes environment, client key, return URL, locale, amount, country, analytics, Drop-in, card, Apple Pay, Google Pay, 3DS2, and partial-payment settings. Apple Pay supports merchant identity, summary items, contacts, shipping, coupon updates, recurring-payment request metadata, and debit or credit `merchantCapabilities`; 3DS remains included.

Apple Pay recurring request configuration is presentation and token-request metadata for the native sheet. It does not establish a subscription scheduler, stored-credential lifecycle, or later merchant-initiated charging capability in this repository.

Payment-method constants distinguish native Components from explicitly unsupported methods. The presence of PayByBank, Google Pay, Apple Pay, UPI, Twint, Bizum, or another adapter does not establish account or transaction eligibility.

## Native dependency boundary

The iOS podspec pins `Adyen` `5.25.1`; Android build metadata pins `com.adyen.checkout:drop-in` `5.19.0`. The independently retained [[source-github-adyen-ios]] baseline matches `5.25.1`. The independently retained [[source-github-adyen-android]] baseline is newer at `5.20.0`, so its API 36 release change is not inherited by this wrapper.

UPI Smart Intent on both platforms and iOS Bizum are recorded in the `2.12.0` note as consequences of native dependency upgrades. Those claims establish the wrapper release boundary but require native SDK evidence for implementation-level detail.

## `2.12.0` release finding

The exact release adds standalone PayByBank and Apple Pay `merchantCapabilities`. It improves instant payments in Sessions and fixes Android Twint storage-field parity, Google Pay and instant-payment behavior during rotation, dismissal of an active-payment screen, and an iOS embedded CardView dismissal crash.

It also updates Adyen Android to `5.19.0`, Adyen iOS to `5.25.1`, and the development React Native baseline to `0.85`. These are the changes attributable to the retained release note. Broader Drop-in, Component, Session, action, card, and configuration findings describe accumulated implementation present at the exact SHA.

## Integration guidance

- Choose Drop-in for the prebuilt payment-method flow and Components when the application owns selection or layout.
- Keep Session creation, `/paymentMethods`, `/payments`, `/payments/details`, and final result verification on the merchant server according to the selected flow.
- Register redirect return handling on both platforms and use Continuous Native Generation rather than Expo Go.
- Re-test both native platforms on wrapper updates because a React Native release can change delegated iOS or Android SDK versions without changing the TypeScript API shape.
- Treat recurring Apple Pay request fields as buyer-facing wallet metadata until separate server-side recurring-payment evidence establishes later-charge behavior.

## Related

- [[changelog-github-adyen-react-native]] - package-qualified release ledger
- [[adyen-react-native-sdk]] - durable wrapper concept
- [[source-github-adyen-ios]] - independently versioned native iOS evidence
- [[source-github-adyen-android]] - independently versioned native Android evidence
- [[adyen]] - company and knowledge-status page

## Raw sources

- Snapshot manifest: `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/manifest.json`
- Release manifest: `raw/github/adyen/adyen-react-native/releases/react-native/2.12.0/2026-08-01/manifest.json`
- Release notes: `raw/github/adyen/adyen-react-native/releases/react-native/2.12.0/2026-08-01/release-notes.md`
- README: `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/README.md`
- Architecture: `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/docs/Architecture.md`
- Compatibility: `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/docs/Compatibility.md`
- Configuration: `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/docs/Configuration.md`
- Package metadata: `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/package.json`
- Public exports and checkout context: `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/src/index.ts` and `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/src/components/AdyenCheckout.tsx`
- Native bridges: `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/ios/` and `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/android/src/main/`
