---
title: "Adyen React Native SDK"
type: concept
category: framework
tags: [adyen, react-native, mobile, sdk, drop-in, components, sessions, apple-pay, google-pay, ios, android]
---

## Adyen React Native SDK

`@adyen/react-native` is Adyen's cross-platform wrapper for the native Adyen iOS and Android checkout SDKs. It offers two primary integration choices: Drop-in for a prebuilt payment-method flow and Components for payment-method-specific experiences inside a merchant-owned flow.

## Current baseline

| Field | Value |
| --- | --- |
| Package | `@adyen/react-native@2.12.0` |
| Release tag | `2.12.0` |
| Exact commit | `2912c913266b2d1df73882980303b563ea04ab63` |
| React Native peer range | `>=0.76.0` |
| Native iOS dependency | `Adyen@5.25.1` |
| Native Android dependency | `com.adyen.checkout:drop-in:5.19.0` |

The tagged repository's `package.json` contains the release-build placeholder `2.0.0-local.1`; the immutable release record, Git tag, and published package identity establish `2.12.0`. Version claims on this page use the package-qualified release identity.

This is retained repository evidence, not current merchant eligibility guidance. Account configuration, backend responses, shopper context, region, currency, device support, and separately versioned native dependencies determine what can actually be offered.

## Integration and server boundary

The Sessions flow starts from a Session created by the merchant backend. The wrapper creates a native Session context, supplies the returned payment methods to Drop-in or Components, and reports completion through `onComplete`. The merchant server should query the Session result before treating the payment as final.

The advanced flow starts from a merchant-provided `/paymentMethods` response. `onSubmit` sends payment data to the merchant server for `/payments`; `onAdditionalDetails` sends follow-up data for `/payments/details`; returned actions are passed back to the native Component. A client key configures client-side authentication but does not replace server credentials or final server-side result verification.

## Architecture and surfaces

The TypeScript layer exports `AdyenCheckout`, checkout and Component hooks, Drop-in, Apple Pay, Google Pay, instant-payment, action, and client-side-encryption modules. Native iOS and Android bridges translate Component callbacks into React Native events and route actions back to the active native module.

Modal flows follow an optional Session setup, open, native-event, and hide lifecycle. Embedded `CardView` is a Fabric component rendered inline in the React tree. Each embedded view uses its React tag as an event-bus key, which permits multiple card views while keeping callbacks and cleanup scoped to the correct instance.

Configuration covers environment, client key, locale, return URL, amount, country, analytics, Drop-in, cards, Apple Pay, Google Pay, 3DS2, and partial payments. Card options include holder name, address collection and lookup, storage choice, CVC policy, installments, and BIN callbacks. Stored-method removal, balance checks, and partial-payment orders cross merchant or Session callbacks rather than proving that backend state changed.

## Platform requirements

React Native New Architecture support requires React Native `0.76.0` or later. Older supported setups use the old architecture or disable bridgeless mode; versions below `0.74` have additional compatibility requirements. Expo Go is not supported. Expo integrations use Continuous Native Generation and can configure the Apple Pay merchant identifier and iOS framework imports through the package plugin.

iOS integrations register custom URL or universal-link return handling and separately enable Apple Pay. Android integrations register the launcher Activity, a redirect intent filter and return handler, and use a Material Components theme.

## Wallet and delegated-runtime boundary

The wrapper exposes Apple Pay and Google Pay configuration and native buttons. Apple Pay configuration includes contacts, shipping, coupon callbacks, recurring-payment request metadata, and `merchantCapabilities`; `threeDSecure` remains included even when debit or credit capabilities are restricted.

An Apple Pay recurring request describes what the native sheet presents. It is not evidence that this wrapper creates a recurring billing schedule, stores a reusable credential, or performs later merchant-initiated charges. Those server-side capabilities require separate product and API evidence.

Runtime payment behavior delegates to Adyen iOS `5.25.1` and Adyen Android `5.19.0`. The independently ingested Android page is currently `5.20.0`, so Android behavior introduced only in `5.20.0` must not be attributed to this wrapper baseline. Delegated wallet, 3DS2, and payment-method SDK behavior also needs its own version-qualified evidence.

## `2.12.0` release boundary

Release `2.12.0` adds standalone PayByBank and Apple Pay `merchantCapabilities`. It improves Sessions instant-payment reliability; fixes Android rotation behavior for Google Pay and instant payments, active-payment screen dismissal, and Twint storage-field parity; and fixes an iOS embedded CardView dismissal crash.

The release updates Adyen Android to `5.19.0`, Adyen iOS to `5.25.1`, and the development baseline to React Native `0.85`. UPI Smart Intent and iOS Bizum are described as capabilities arriving through those native SDK updates, so they remain delegated native-release findings rather than independent JavaScript implementations.

## Related

- [[source-github-adyen-react-native]] - cumulative exact-SHA wrapper evidence
- [[changelog-github-adyen-react-native]] - package-qualified release ledger
- [[adyen-ios-sdk]] - independently versioned native iOS runtime
- [[adyen-android-sdk]] - independently versioned native Android runtime
- [[adyen]] - company and knowledge-status page
