---
title: "GitHub: stripe/stripe-terminal-ios"
type: source
date_ingested: 2026-08-31
date_updated: 2026-08-31
original_format: github-repo
raw_files:
  - "github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/manifest.json"
tags: [stripe, terminal, ios, swift, mobile, sdk, card-present, tap-to-pay, offline-payments, github-repository]
---

## Overview

`stripe/stripe-terminal-ios` distributes Stripe's proprietary native iOS SDK for custom in-person checkout. This cumulative page establishes the approved `StripeTerminal@5.8.0` baseline at exact commit `c027d6dc2258c774412cb7933cbb959488c16b63` from public headers, the open-source example application, support policy, and release history.

Repository: <https://github.com/stripe/stripe-terminal-ios>

## Evidence Boundary

- Stripe states that the SDK implementation is proprietary and closed source. The retained public headers are authoritative for the exposed API contract, while the example application demonstrates integration patterns rather than internal runtime behavior.
- The capsule retains 235 files: 169 public API files, 60 example files, build metadata, documentation, license, and release history. Tests, generated binaries, assets, CI, and unrelated tooling are excluded.
- API presence does not prove merchant eligibility, country or currency availability, preview access, reader firmware compatibility, or account configuration.
- Several retained surfaces are preview-gated or conditionally compiled, including surcharging, MOTO, collect-data, Tap to Pay offline mode, and USB support.
- An SDK completion does not independently prove capture or settlement. Manual-capture integrations must synchronously notify their backend to capture, and fulfillment should follow server-side payment state.

## Package Status

| Package | Latest ingested release | Exact SHA | Evidence status |
| --- | --- | --- | --- |
| `StripeTerminal` | `5.8.0` | `c027d6dc2258c774412cb7933cbb959488c16b63` | Approved full baseline |

This table reports wiki ingest progress, not the latest release published upstream.

## Platform and Installation

- `StripeTerminal@5.8.0` requires iOS 15 or later. Its binary Swift Package target downloads `StripeTerminal.xcframework` for the exact `5.8.0` release; CocoaPods supports `pod 'StripeTerminal', '~> 5.0'`.
- Location services are mandatory for accepting payments. Bluetooth reader integrations also require the Bluetooth usage description and `bluetooth-central` background mode.
- Version 5 is built with Xcode 26 and Swift 6.2. The support policy places 5.x in active development through October 2027 and schedules its hard block for October 2028.
- Major versions follow active, maintenance, and deprecated phases; after the hard-block date, obsolete versions can no longer discover or connect readers or process payments.

## Initialization and Backend Boundary

Call `Terminal.initWithTokenProvider(...)` before accessing `Terminal.shared`. The token provider authenticates to the merchant backend, which creates a fresh Terminal ConnectionToken and returns its secret. The SDK can connect to one reader and perform one operation at a time.

The retained example backend client also owns location listing/creation, internet-reader registration, PaymentIntent capture, and other secret-key operations. Switching Stripe accounts requires disconnecting the reader, clearing cached credentials, changing the token provider's backend identity, and reconnecting with a new token.

## Reader Discovery and Connection

The API exposes Bluetooth scan and proximity discovery, internet-reader discovery, Tap to Pay discovery, and conditionally compiled USB discovery. Mobile and Tap to Pay connections require a Stripe Terminal Location ID. Internet readers can be registered and managed through the backend.

`easyConnect` combines discovery and connection for Tap to Pay and internet readers when a discovery filter identifies exactly one reader. Traditional discovery remains delegate-driven and returns a cancelable operation.

Tap to Pay connections can include a connected account in `onBehalfOf`, a cardholder-facing merchant display name, Terms of Service presentation behavior, and automatic reconnection. The app can independently check whether the relevant account has accepted Apple's Tap to Pay terms.

Modern Bluetooth, USB, and Tap to Pay configurations enable automatic reconnection by default. Integrations must handle reconnect start, success, failure, and ordinary disconnect reasons rather than inferring unexpected disconnects from the global connection status alone.

## Reader Updates

Required reader updates can run during connection and block use until complete. The app must implement update progress and completion UI and keep the device awake and near the reader. Optional updates can be installed through `installAvailableUpdate`.

Test-mode configurations can simulate available, required, required-offline, and low-battery update scenarios. Canceling a required update can make connection fail with an unsupported-reader-version error.

## Payment Lifecycle

Two supported payment patterns coexist:

1. Split flow: create or retrieve a PaymentIntent, call `collectPaymentMethod`, then `confirmPaymentIntent`.
2. Combined flow: call `processPaymentIntent`, which performs collection and confirmation as one cancelable operation.

Collection updates are initially local to the SDK. Confirmation authorizes the payment. For manual capture, the app must synchronously call its backend to capture the PaymentIntent; abandoning an intent after an unknown confirmation result without reconciliation risks duplicate charges.

Collection configuration controls tipping, customer cancellation, offline behavior, payment-method updates, and preview capabilities. Customer cancellation is enabled by default where the reader supports it. Reader-display cart data is presentation-only and does not determine the charged amount.

## Saving Payment Details

SetupIntents support split `collectSetupIntentPaymentMethod` plus `confirmSetupIntent` and combined `processSetupIntent` flows. The app must collect cardholder consent and pass `allowRedisplay`; collection alone does not persist the payment method to Stripe.

In `5.8.0`, `SCPSetupAttemptCardPresentDetails.generatedCardExpanded` and `SCPSetupIntent.paymentMethodExpanded` expose full expanded `SCPPaymentMethod` objects. This reduces follow-up retrieval for supported saving flows but does not remove consent or server-side customer-management requirements.

`readReusableCard` remains a legacy/deprecated approach. Stripe warns that it does not create a card-present transaction and therefore loses card-present pricing and liability benefits; SetupIntents are the maintained saving path.

## Offline Payments

Offline behavior is selected per collection as `preferOnline`, `requireOnline`, or `forceOffline`. A locally created offline PaymentIntent can have no Stripe ID until forwarding; `offlineDetails` supplies a local identifier and whether upload is required. Merchant-defined metadata is important for reconciliation.

The SDK reports offline status for both the app and connected smart reader, including queued counts and currency totals, and announces forwarding progress through `SCPOfflineDelegate`. Once connectivity returns, queued intents must be forwarded and then captured where required. Clearing local application state can therefore affect unresolved offline evidence.

The simulator can independently place the SDK and smart reader in immediate-failure, timeout, or intermittent offline modes. These controls are test-only and fail for live-mode readers. Tap to Pay offline processing entered private preview in 5.6.0 and must not be treated as generally available.

## Refunds

`processRefund` combines collection and confirmation for in-person refund methods such as Interac. The older split refund methods are deprecated. Ordinary refunds that do not require cardholder presence remain server-side or Dashboard operations.

Unknown outcomes require reconciliation: a timeout can leave refund status unknown, while a returned failure reason indicates a declined refund. Interac refund construction requires the original PaymentIntent client secret in version 5.

## Tap to Pay and QR Methods

Tap to Pay requires a retained delegate for reader input, display prompts, update lifecycle, and optional payment-method selection and QR display. QR processing blocks until the app invokes the delegate completion after presenting the code.

The API surface includes WeChat Pay, PayNow, PayPay, Affirm, and Klarna details or selection types. Their presence is not universal availability. QR methods can be region-, reader-, capture-mode-, or preview-constrained and are not interchangeable with offline card-present processing.

## Reader and Checkout Features

- On-reader tipping can use an eligible amount; tip availability also depends on reader and Location configuration.
- Surcharge surfaces expose eligibility, maximum amount, configured amount, and customer-consent collection. The feature remains access- and reader-version-dependent.
- Smart readers can collect selection, signature, email, phone, text, and numeric inputs, with optional toggles.
- Supported readers can print content. `5.8.0` adds an explicit low-battery printing error.
- Supported mobile readers can collect non-payment magstripe or NFC data through preview APIs; this is not payment-card processing.
- Supported readers expose accessibility and buzzer settings. `5.8.0` can read current/max buzzer volume and set low, high, or a custom value from `1...maxVolume`.
- Dynamic currency conversion, MOTO, multicapture, reauthorization, overcapture, donation, and surcharge APIs require independent account, reader, and release checks.

## Errors, Logging, and Testing

The error model distinguishes integration misuse, invalid configuration, network and API errors, card declines, reader and update failures, offline failures, printer failures, and Tap to Pay conditions. Confirmation errors may carry the updated Intent and an API error, which should drive retry decisions.

Version `5.8.0` adds error, warning, and info log levels in addition to verbose and none. Log listeners are diagnostic only and may be invoked on any thread; application behavior must not depend on log text.

The simulator supports card brands, decline and PIN scenarios, input outcomes, offline failures, and reader updates. Simulated success does not replace physical-reader, account-eligibility, connectivity, capture, webhook, or settlement testing.

## Version History

### `StripeTerminal@5.8.0`

Adds buzzer-volume management, expanded SetupIntent payment methods, granular logging, an unknown-device fallback, and a printer-low-battery error. It also corrects Bluetooth disconnect reasons and a Tap to Pay collection crash.

### Version 5 Major Boundary

Version 5 raises the minimum to iOS 15, requires explicit SDK initialization, adds combined process and Swift async APIs, adds a reconnecting status, changes cancellation and connection-state semantics, defaults customer cancellation on where supported, removes P400 support, and deprecates split refund confirmation.

### Accumulated `5.1.0--5.7.0` Context

The retained upstream history adds EasyConnect; internet-reader filtering; mPOS and Tap to Pay QR methods; Tap to Pay compatibility checks; tip eligibility; richer API errors; multicapture and reauthorization previews; simulated offline/update scenarios; Tap to Pay offline private preview; localized API errors; overcapture status; and preview surcharging. These are cumulative-history findings, not independent comparisons of every release.

## Integration Guidance

- Keep secret-key operations, ConnectionToken creation, capture, and authoritative reconciliation on the backend.
- Persist enough merchant and local identifiers to reconcile unknown and offline outcomes before retrying or creating replacement Intents.
- Treat reader type, firmware, country, currency, account enablement, and preview enrollment as runtime prerequisites separate from SDK symbols.
- Implement disconnect, auto-reconnect, required-update, cancellation, and background/foreground transitions as first-class checkout states.
- Use SetupIntents with explicit consent for reusable payment details.
- Test both split and combined flows only if the application supports both; do not mix their state transitions accidentally.
- Review the migration guide and support lifecycle before every major upgrade because end-of-life versions are eventually blocked.

## Related

- Company: [[stripe]]
- Concept: [[stripe-terminal]]
- General iOS payments SDK: [[source-github-stripe-ios]]
- History: [[changelog-github-stripe-terminal-ios]]

## Raw Sources

- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/manifest.json` - exact-SHA bounded source capsule
- `raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/5.8.0/2026-08-31/manifest.json` - package-qualified release record
- `raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/5.8.0/2026-08-31/release-notes.md` - exact `5.8.0` release notes
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/README.md` - repository purpose, requirements, installation, and closed-source boundary
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/SUPPORT.md` - support lifecycle and hard-block schedule
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/CHANGELOG.md` - cumulative version history
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/PublicHeaders/SCPTerminal.h` - initialization, connection, payment, SetupIntent, refund, offline, and reader APIs
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/PublicHeaders/StripeTerminal.h` - exported public surface
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/Example/Example/APIClient.swift` - example backend boundary
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/Example/Example/PaymentViewController.swift` - payment and capture orchestration
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/Example/Example/OfflineUIHandler.swift` - offline status and forwarding UI

