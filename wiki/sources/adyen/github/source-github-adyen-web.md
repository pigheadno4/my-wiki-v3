---
title: "GitHub: Adyen/adyen-web"
type: source
date_ingested: 2026-07-26
original_format: github-repo
raw_files:
  - "github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/manifest.json"
tags: [adyen, checkout, web-sdk, cards, 3d-secure, github-repository]
---

## Overview

`Adyen/adyen-web` contains Adyen's browser checkout SDK. It provides an all-in-one Drop-in and individually mounted payment-method Components, plus shared handling for sessions, payment actions, analytics, risk data, localization, and accessibility. This cumulative page begins with package-qualified release `@adyen/adyen-web@6.41.0` at exact SHA `b19eec7054340a1526c87d450fd7dfff75794ed9`.

Repository: <https://github.com/Adyen/adyen-web>

## Evidence boundary

- The snapshot proves implementation retained in `@adyen/adyen-web@6.41.0`, released on 2026-07-16. It does not replace current Adyen integration guidance or prove that a payment method is enabled for a merchant.
- Drop-in and Components are presentation and client-orchestration surfaces. Payment-method availability still comes from backend responses, merchant configuration, shopper context, and regional or product eligibility.
- Stories are retained as intended integration scenarios. Tests were excluded by collection policy, so test-only behavior is outside this capsule.
- PayPal Fastlane support in this repository depends on `@paypal/paypal-js`; this snapshot describes Adyen's adapter and configuration surface, not the delegated PayPal runtime.

## Grounding excerpts

> "Adyen Web provides you with the building blocks to create a checkout experience for your shoppers"
>
> `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/README.md:7`

> "With this integration, installments configuration must be defined when you create the session."
>
> `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Card/Card.tsx:107-113`

> "Credit: Should render CtP and installments"
>
> `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Card/stories/Card.stories.tsx:303-310`

> "Only render component if we have a valid acsURL & postMessageDomain."
>
> `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/ThreeDS2/components/Challenge/PrepareChallenge3DS2.tsx:74-84`

> "The iframe now has no role."
>
> `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Card/components/CardInput/a11y.docs.mdx:15-28`

## Integration surfaces and architecture

Drop-in is the all-in-one checkout surface. Components expose one payment method at a time for merchants that need control over layout and orchestration. The UMD bundle registers all Components, while tree-shakable integrations must register the Components they use.

The core resolves API, analytics, image, and translation endpoints from the selected environment. Initialization validates configuration, sets up an optional Checkout Session, builds the payment-method list, and creates shared risk, analytics, resources, localization, and screen-reader modules. A test or live client key must match the selected environment.

The registry maps payment-method transaction variants to native Components. For payment methods without a dedicated registered implementation, the runtime can use the generic redirect Component. Drop-in itself is not registered as a payment-method action Component.

## Sessions and advanced flow

With a Checkout Session, the SDK sends `sessionData` through setup, payment, payment-details, balance, order, cancellation, and donation service calls. Session setup returns the amount, locale, country, and payment methods that initialize the client.

The advanced flow delegates `/payments` to `onSubmit` and `/payments/details` to `onAdditionalDetails`. Responses can create redirect, 3DS2, voucher, QR-code, await, bank-transfer, or external-SDK actions. Redirect completion uses the configured details callback or the active Session; successful and failed terminal responses are routed to `onPaymentCompleted` and `onPaymentFailed`.

Session configuration is authoritative where the backend owns a setting. In `6.41.0`, Card component-level installments are hidden and a warning is emitted because the Sessions backend ignores that local configuration.

## Payment methods, stored methods, and Drop-in

The runtime processes regular and stored payment methods separately. Merchant allow/remove lists filter both groups, and stored methods are restricted to supported types with `Ecommerce` shopper interaction. Stored cards can inherit a funding source by matching their brand against the available card methods.

Drop-in creates and groups instant, stored, regular, and Fastlane elements, filters unavailable methods, tracks the active item, propagates amount changes, and mounts follow-up actions. Its payment-method list uses checked-state accessibility semantics even when the first method is not opened automatically.

## Card behavior

Card uses secured fields for sensitive input and can combine holder name, billing address, storage consent, dual-brand selection, installments, Click to Pay, Korean authentication fields, and Fastlane signup data.

Installments render only when configured options are nonempty, the amount is nonzero, and the card funding source is credit or unspecified. With split card funding sources, retained stories define the expected matrix:

| Funding source | Click to Pay | Installments |
| --- | --- | --- |
| Credit | Yes | Yes |
| Debit | Yes | No |
| Prepaid | No | No |

This is package-version implementation evidence, not a guarantee that a merchant's backend response enables each option.

## 3D Secure 2 and action safety

3DS2 device-fingerprint and challenge flows decode server tokens, create hidden or visible iframes, listen for `postMessage` completion, and enforce timeouts. The challenge path validates both the ACS URL and the origin derived from `threeDSNotificationURL` before rendering. Missing or invalid data is reported through the SDK error path instead of starting a flow that cannot complete.

The exact `6.41.0` release strengthens this boundary by detecting a challenge token whose notification URL lacks a valid domain. It also retains distinct `paymentData` and authorization-token handling between fingerprint, challenge, and redirect-derived flows.

## Accessibility

Secured-field iframes deliberately omit `role="presentation"` so assistive technology can discover their interactive content. The dual-brand selector uses buttons with keyboard handling and `aria-pressed`. A shared screen-reader panel announces validation and status messages through a polite live region, and submission errors are sorted by visual field order before focus moves to the first invalid field.

In `6.41.0`, Drop-in also restores `aria-checked` when `openFirstPaymentMethod` is false and replaces deprecated `keypress` handling with `keydown`.

## Analytics, risk, and sensitive-data boundary

The analytics layer queues component, action, error, and configuration events. Rendered-configuration analytics explicitly omit fields including `data`, holder name, shopper email, email, telephone number, and Click to Pay configuration.

The optional risk module loads a hidden device-fingerprint iframe, validates the expected message origin, applies a 20-second timeout, and encodes the resulting risk payload. This client evidence does not describe Adyen's server-side risk decisioning.

## PayPal Fastlane dependency

Adyen Web contains a PayPal Fastlane Component and Card signup path. Valid signup configuration can propagate consent and optional phone data into encoded Card payment data. The package depends on `@paypal/paypal-js@10.0.0` and augments its namespace with Fastlane types.

That dependency is an evidence boundary: questions about PayPal loader or delegated runtime behavior must also consult the independently collected `paypal/paypal-js` source rather than inferring those details from Adyen's adapter.

## `6.41.0` release findings

The release propagates the `healthcare` field to `onBinLookup`, validates the 3DS2 challenge notification domain, and replaces deprecated `keypress` events. It removes several explicit `any` types, prevents misleading component-level installments in Sessions, and fixes Drop-in checked-state accessibility.

These are patch findings. The broader architecture above is the accumulated source present at the same exact SHA.

## Related

- [[changelog-github-adyen-web]] — package-qualified release ledger
- [[adyen]] — company and knowledge-status page
- [[co-badged-cards]] — cross-provider card-network choice concept
- [[source-github-paypal-js]] — independent evidence for the delegated PayPal JS dependency

## Raw sources

- Snapshot manifest: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/manifest.json`
- Release manifest: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.0/2026-07-26/manifest.json`
- Release notes: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.0/2026-07-26/release-notes.md`
- README: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/README.md`
- Core: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/core/core.ts`
- Drop-in: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Dropin/`
- Card: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Card/`
- 3DS2: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/ThreeDS2/`
- Analytics: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/core/Analytics/`
