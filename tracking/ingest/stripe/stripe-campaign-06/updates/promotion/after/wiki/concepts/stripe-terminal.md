---
title: "Stripe Terminal"
type: concept
category: technology
tags: [stripe, terminal, in-person, point-of-sale, card-reader, tap-to-pay, offline-payments, connect, sdks, global, payment-methods, regional]
---

## Stripe Terminal

Stripe's in-person payment product. Enables businesses to accept card payments using physical card readers and unifies in-person payments with online payments in a single Stripe Dashboard. Works with Stripe Connect platforms.

The November 2026 [[source-stripe-mx-installments|Mexico installments overview]] lists Terminal for Stripe Mexico accounts. The separate [[source-stripe-mx-installments-accept-payment|Mexico acceptance guide]] provides variant navigation. SDK, reader, and account-specific availability must be established for the integration in use.

## Architecture

A custom SDK-based Terminal deployment has four components:

1. **Your application** — web-based, mobile, or desktop POS
2. **Your backend** — server-side logic talking to the Stripe API
3. **A Stripe Terminal reader** — pre-certified hardware that encrypts card data on-device
4. **The Stripe Terminal SDK** — bridges POS app, reader firmware, and Stripe API

The SDK enables in-person payments via the same PaymentIntents flow as online Stripe payments. Readers accept EMV (chip), contactless, and swiped card details, encrypt the data, and return a token to your app — raw card data never reaches your application.

## Reader Requirements

Terminal works **only** with Stripe pre-certified readers and Tap to Pay on compatible iPhone/Android devices. No third-party reader hardware is supported. This ensures end-to-end encryption and remote firmware management.

## Connection Types

| Method | Availability |
| --- | --- |
| Bluetooth | Mobile readers |
| USB | Android + mobile readers only |
| Internet | All readers in network-enabled environments |

## Integration Paths

The April 2026 landing page lists five paths. The November 2026 capture adds Stripe’s first-party no-code Preview path as the sixth.

| Path | Description | Code required |
| --- | --- | --- |
| **Custom POS** | Build a fully custom point-of-sale using SDKs (Android, iOS, JavaScript, React Native) or the server-driven API | Yes |
| **Tap to Pay** | Accept contactless payments using a compatible iPhone or Android device — no dedicated reader hardware needed | Yes (SDK) |
| **Apps on devices** | Deploy a custom Android POS app directly onto Stripe smart readers | Yes |
| **Terminal without coding (November Preview)** | Standalone on a compatible reader (public preview) or the Stripe Terminal app on a supported iPhone or Android device (private preview). Both require internet. See [[source-stripe-terminal-overview]]. | No code |
| **Third-party POS** | Integrate Terminal into existing third-party POS, hardware, and commerce stacks | No code |
| **Gateway** | Combine Stripe with gateway-supported POS systems, third-party hardware, gift cards | No code |

## SDKs

| SDK | Platform | Version | Notes |
| --- | --- | --- | --- |
| JavaScript SDK v1 | Web / browser-based POS | v1 | Load from `js.stripe.com` only; Chrome 142+ needs local network permission; same-network + local DNS required |
| iOS SDK | Native iOS | 6.0.0 full ingest; 5.8.0/5.8.1 history retained | v6 iOS 16+; SPM updates; explicit `Terminal.initWithTokenProvider`; location mandatory |
| Android SDK | Native Android | 6.0.0 additive full; v5 history retained | API 26+; compile SDK 35+ per v6 note; lifecycle delegate; matched Tap to Pay artifacts |
| React Native SDK | Cross-platform mobile | latest (public preview) | `requestNeededAndroidPermissions` helper; Android 12+ needs `exported=true` |

A server-driven API is also available for any backend regardless of platform.

### Server-driven limitations

Server-driven does **not** support mobile readers (M2, WisePad 3) or offline payments. Supports any language/middleware + internet connection (not LAN).

### SDK setup: location required on iOS and Android

Both iOS and Android require location services for payments. If location access is revoked, payments are disabled until restored.

### Retained Android SDK baseline

The approved `stripeterminal@5.8.0` repository capsule confirms `ACCESS_COARSE_LOCATION` is sufficient for SDK location reporting, while apps needing precise location must declare it independently. A custom `Application` calls `TerminalApplicationDelegate.onCreate`, then `Terminal.init` receives the token provider, listeners, optional offline listener, and locale configuration.

Standard integrations use `com.stripe:stripeterminal`; Tap to Pay uses matching `stripeterminal-taptopay` and `stripeterminal-core` versions. Version 5 provides both split collect/confirm APIs and combined `processPaymentIntent`, `processSetupIntent`, and `processRefund` APIs. Manual capture, ConnectionToken creation, and authoritative reconciliation remain backend responsibilities.

The SDK implementation is proprietary. Generated API docs and open Java/Kotlin examples establish the public contract and integration patterns, not internal runtime behavior or merchant/device eligibility.

### Android 5.8.1 Tap to Pay update

`stripeterminal@5.8.1` announces China UnionPay support in Hong Kong for Tap to Pay on Android. This is a proprietary SDK release claim, not a new general reader/API capability or proof of merchant/device eligibility. The retained example implementation is unchanged; all 337 changed API documentation files differ only by version strings. Earlier Android 5.8.0 guidance remains preserved. See [[source-github-stripe-terminal-android]] and [[changelog-github-stripe-terminal-android]].

### Android 5.8.2 UnionPay fix

`stripeterminal@5.8.2` reports a fix for China UnionPay payment failures in Tap to Pay. It follows, rather than replaces, the 5.8.1 Hong Kong support announcement. Retained implementation is unchanged and generated API differences are version-only; runtime behavior remains an upstream proprietary-binary claim. See [[source-github-stripe-terminal-android]] and [[changelog-github-stripe-terminal-android]].

### Android 6.0.0 migration boundary

`stripeterminal@6.0.0` is an additive major ingest, preserving 5.8.0, 5.8.1 and 5.8.2. The release requires compile SDK 35+ and Kotlin 2.3.21 dependencies; the retained README/example still specify minimum Android API 26. Compile SDK 35 is not an Android 15 device minimum. Keep Terminal/core/Tap to Pay artifacts matched and supply `LocaleConfig` to `Terminal.init`.

- SDK-side PaymentIntent creation defaults to `CaptureMethod.AutomaticAsync`. Explicitly choose `Manual` for receipt tipping and incremental/extended authorization; inspect server/Intent state before capture or fulfillment. The Java event example calls capture for any successful Intent with an ID, without checking `REQUIRES_CAPTURE`; this is a static integration caution, not a reproduced SDK defect.
- `CollectSetupIntentConfiguration.Builder(allowRedisplay)` replaces the separate consent argument; demo `ALWAYS` is not proof of customer consent. `latestCharge`/`latestChargeId` replace `getCharges`; instrument and transaction card-present models separate, and refund parameters/SetupAttempt model names change.
- Mobile payment selection/QR UI uses `ReaderPaymentInteractionListener`, separate from `MobileReaderListener`, on Bluetooth/USB/external-USB connection configuration. A required interaction without that listener fails the transaction; invoke the concrete interaction callback to continue. Reader cancellation is `CANCELED_BY_READER`, distinct from SDK `CANCELED`.
- Tap to Pay adds `MODIFY_AUDIO_SETTINGS`, advisory upcoming-update notifications, non-Parcelable UX models, `Theme`/`colorScheme` naming and `SYSTEM` theme default. The update callback does not itself install updates, disconnect readers or block payments. The source does not establish the merged dependency manifest or automatic permission declaration.
- New no-collection `confirmRefund(parameters, callback)` is private preview; the removed old split-confirm overload is a different API. Successful callbacks can still require customer action, and unknown outcomes require backend reconciliation before another refund. In-person Interac rules remain.

> [!warning] Contradiction
> The Android v6 release says the client builder defaults to automatic-async capture, but retained `confirmPaymentIntent` docs still unconditionally describe authorization followed by mandatory backend capture, and the PaymentIntent capture-property text lists only automatic/manual. Treat the old description as manual-flow guidance, not the complete v6 default contract. Select capture explicitly and reconcile status; [[source-github-stripe-terminal-android]] records the reciprocal warning and exact evidence.

The v6 raw changelog retrospectively identifies 5.4.0–5.6.0 as affected by missing `generated_card`, fixed in 5.7.0; this is historical clarification, not a new v6 fix. No iOS-only MSI/Swish or SPM policy is inferred for Android. See [[source-github-stripe-terminal-android]] and [[changelog-github-stripe-terminal-android]].

### iOS 5.8.1 offline maintenance update

`StripeTerminal@5.8.1` reports a fix for offline PaymentIntents dropping merchant creation parameters, affecting Tap to Pay destination charges using `onBehalfOf`. The retained public-source delta changes only release history, binary URL/checksum and the SDK version constant; the proprietary runtime fix was not executed or independently inspected. No new payment API or general offline availability follows. See [[source-github-stripe-terminal-ios]] and [[changelog-github-stripe-terminal-ios]].

### iOS 6.0.0 migration boundary

The additive `StripeTerminal@6.0.0` ingest preserves both v5 releases. Version 6 requires iOS 16+, with Xcode 16+/Swift 6+ required for integrators; Stripe built the binary using Xcode 27/Swift 6.4. The raw changelog says new releases, including patches to earlier majors, are published through SPM only; existing CocoaPods versions continue working but receive no further updates there. The README points SPM users to `stripe/stripe-terminal-ios-spm`.

- **Capture:** `PaymentIntentParametersBuilder` defaults to `.automaticAsync`, not `.manual`. Explicitly select `.manual` for on-receipt tipping, incremental or extended authorization. Inspect the resulting Intent state and reconcile on the backend; this is a client-builder default, not a claim about every server-created Intent.
- **Consent and models:** initialize `CollectSetupIntentConfigurationBuilder(allowRedisplay: ...)` with consent-appropriate `.always` or `.limited`, and pass the configuration to collect/process. `SetupIntent.paymentMethod` is now the expanded object; use `paymentMethodId` for its ID. Use `PaymentIntent.latestCharge`/`latestChargeId` instead of `charges`. Instrument details and transaction details are separate; card brand, funding and read-method fields use strings rather than old enums, with nullable funding and nullable instrument expiry.
- **Reader UI:** migrate the five Tap to Pay lifecycle/display callbacks to shared `reader(...)` forms. Payment selection/QR UI uses a separate retained `ReaderPaymentInteractionDelegate`, configured on the connection and completed via `PaymentInteraction` subclasses. Reader-originated cancellation is `.canceledByReader` (2021), distinct from SDK `.canceled` (2020).
- **Refunds/previews:** `ProcessRefundParameters` replaces `RefundParameters`; deprecated split refund calls are removed. The new private-preview `confirmRefund(parameters)` requires a connected reader for authentication but no card collection or reader UI. Mexico MSI installments and Swish are previews, not general merchant availability. Simulator offline access is broader, not proof that live offline payments are generally available.

> [!warning] Contradiction
> The v6 creation header and release notes specify automatic-async capture by default, but `SCPTerminal.h` retains an unqualified comment saying successful confirmation only authorizes and requires synchronous backend capture. Apply that comment to a manual-capture flow, not every v6 payment; choose the capture method explicitly and inspect state. The same evidence conflict is recorded in [[source-github-stripe-terminal-ios]].

The v5 maintenance tip and v6 tip diverge from their common 5.8.0 baseline. Do not infer that the proprietary v6 binary includes or excludes the 5.8.1 offline fix from version ordering or changelog absence. See [[source-github-stripe-terminal-ios]] and [[changelog-github-stripe-terminal-ios]] for both comparisons and migration detail.

## Key Features

- **In-person payments** — physical card readers; tip adjustments supported during checkout
- **Tap to Pay** — contactless via iPhone or Android; no dedicated reader required
- **Multiple payment methods** — debit/credit cards, contactless, mobile wallets
- **Offline payments** — accepts card payments (chip/NFC, no swipe) offline; unsupported: Interac, girocard, QR payments; EEA requires card insertion + PIN; no server-driven offline; payments stored to disk, auto-forwarded on reconnect. Min SDK: iOS 3.3.0 / Android 3.2.0. Must have connected online at same Location within 30 days. Stripe max: **10,000 USD**. Offline PI has null stripeId — add metadata for reconciliation. Clearing app cache loses stored payments. `offlineBehavior`: PREFER_ONLINE/REQUIRE_ONLINE/FORCE_OFFLINE
- **Smart reader apps** — deploy Android POS apps directly to Stripe smart readers
- **Connect-compatible** — integrates with Stripe Connect for platform use cases

## Encryption Tiers

| Tier | Description | Cost |
| --- | --- | --- |
| **E2EE** (end-to-end encryption) | Default for all Terminal payments | Included |
| **P2PE** (point-to-point encryption) | PCI-audited; adds HSM decryption step before card networks; third-party validated; no extra integration needed | Paid (optional) |

P2PE is designed for regulated industries (healthcare, education). It reduces PCI audit scope and cost. Consult the P2PE Instruction Manual (PIM) if enabled.

## Fleet Management

- Order pre-certified readers and accessories from the Stripe Dashboard. The guides specify up to 10,000 of each item in a single order.
- Ship to eligible physical addresses according to the destination table and territory exclusions. Terminal Connect platforms can specify connected account addresses during checkout.
- Monitor entire reader fleet from the Dashboard
- The November 2026 guide lists 32 countries for eligible Dashboard self-service returns, down from 33 in May. Gibraltar remains in the shipping table. The returns flow requires original packaging and accessories within 30 days and refunds shipping fees on the first initiated return. Use **Contact support** on the Dashboard order when self-service is unavailable.
- Hardware Orders API (preview): programmatic ordering via SKUs + shipping methods; country-specific, query dynamically
- See [[stripe-terminal-hardware-orders]] for full ordering, returns, and API details

## S700/S710 Accessories

| Accessory | Purpose | Key notes |
| --- | --- | --- |
| **Case** | Drop protection | Exposes all ports; compatible with Dock |
| **Hub** | I/O expansion | 10/100M Ethernet + 2× USB-A (1A shared, 27W); **connects peripherals to POS device, not to reader** |
| **Dock** | Countertop mount + power | Magnetic + locking nut + 3 screw points; **no payment connectivity via USB** — reader uses internet |
| **Power Adapter** | Charging | 20W; region-specific (US/UK/EU/AU); replaceable via Dashboard |
| **Stand** | Mounting | No Stripe stand — use third-party |

Hub + Dock together: complete countertop I/O solution (Dock for power/mount, Hub for Ethernet/peripherals). Dock does not include a USB-C power cable — use the reader's included cable.

## In-Person Fundamentals

Core operational capabilities:

- **Save cards at POS** — save for subscriptions, attach to online account, or defer payment; uses `generated_card` PaymentMethod for online reuse; see [[stripe-terminal-save-payment-details]]
- **Incremental authorizations** — increase authorized amount before capture; Visa/Mastercard/Amex (all MCCs), Discover (restricted MCCs); max 10 attempts; see [[stripe-terminal-incremental-authorizations]]
- **Extended authorizations** — extend capture window up to 30 days; Visa/Mastercard/Amex/Discover (category-dependent); not available on Interac/eftpos; see [[stripe-terminal-extended-authorizations]]
- **Cancel or refund payments** — cancel pre-capture (Visa/MC/Amex/Discover/girocard); refund post-capture (online all except Interac; Interac = in-person only); see [[stripe-terminal-refunds]]
- **Display cart details** — dynamically update smart reader screen with line items and totals via `setReaderDisplay` (display-only; does not control charge amount); pre-dip (US only) lets customers present card before amount is finalized; see [[source-stripe-terminal-display-cart]]
- **Collect on-screen inputs** — the 2026-05-01 guide lists Stripe Reader S700/S710 and BBPOS WisePOS E for six input types. SDK variants document up to five sequential inputs per call. The server-driven guide specifies seven-day storage for signature files. See [[stripe-terminal-collect-inputs]].
- **Collect swiped data** — the 2026-05-01 private-preview guide covers non-PCI magstripe collection, SDK tokens, backend retrieval and reader, offline and 24-hour retention limits. The 2026-11-07 capture indexes iOS, Android and React Native. See [[source-stripe-terminal-collect-data]].
- **Collect NFC tapped data** — the 2026-05-01 private-preview guide lists Stripe Reader S700/S710 and Stripe M2, documents offline NFC UID reads with the UID returned directly to the app, and excludes card payments. See [[source-stripe-terminal-collect-nfc-data]].
- **Apps on Devices** — Android POS on a smart reader or a separate POS paired with a consumer-facing app over TCP/IP. Standard Stripe API uploads are capped at 200 MB. November 2026 documents a 300 MB private preview by request. See [[stripe-terminal-apps-on-devices]] for device, DevKit, storage and Connect requirements.
- **Send receipts** — Stripe emails a prebuilt receipt at live capture when `receipt_email` is set. After checkout, update the PaymentIntent’s `receipt_email` to trigger one. For test-key payments, view or manually send receipts in the Dashboard. Custom EMV receipts require `application_preferred_name`, `dedicated_file_name`, and `account_type` (optional in the US). See [[source-stripe-terminal-receipts]].

## Global Availability

**GA (23 countries)**: AT, AU, BE, CA, CH, CZ, DE, DK, ES, FI, FR, GB, IE, IT, LU, MY, NL, NO, NZ, PT, SE, SG, US

**Preview (15 countries)**:

- Full Terminal: JP, PL
- Tap to Pay only: BG, CY, EE, GI, HR, HU, LI, LT, LV, MT, RO, SI, SK

## Reader Hardware

| Reader | Category | Notes |
| --- | --- | --- |
| Stripe Reader S700 | sPOS | 5.5" screen, Android 10, WiFi/Ethernet, 64GB — 25 countries (all GA + CZ/PL/JP preview) |
| Stripe Reader T600 | sPOS | Android countertop and pole-mount reader. The 2026-11-07 smart-reader overview lists 37 markets and server-driven compatibility. The product guide documents JavaScript, iOS, Android and React Native SDKs using internet, LAN or handoff. See [[source-stripe-terminal-smart-readers]]. |
| Stripe Reader S710 | sPOS | Adds cellular connectivity. Setup SDK minimums are iOS v4.7.3, Android v3.8.0 and React Native v0.0.1-beta.28. The May and November 2026 smart-reader overviews list 10 and 24 markets, respectively. Separate April and November setup badges list 16 and 39. See [[source-stripe-terminal-smart-readers]] for the dated difference and unresolved market availability. |
| BBPOS WisePOS E | sPOS | 5" screen, Android 9, WiFi/Ethernet only (no cellular), ~8h battery, dark theme default. The November 7, 2026 device banner lists 24 markets, including SG and with no JP or HK. HK deployment remains unresolved given the firmware and feature-specific evidence in [[source-stripe-terminal-bbpos-wisepos-e]]. |
| BBPOS WisePad 3 | mPOS | 2.4" screen, BLE or Android-only USB; physical PIN pad for PIN-auth markets; auto-off 5min disconnected; ~600 contact/~800 contactless tx per charge. The reader reference [[source-stripe-terminal-bbpos-wisepad3]] and mobile-reader overview list 24 non-US markets in May 2026 and 37 in November 2026. |
| Stripe Reader M2 | mPOS | US (all 50 states and Puerto Rico, per the setup guide); screenless; BLE or Android-only USB; iOS/Android/RN SDKs; auto-off after 10h inactivity when connected; reset by holding 14s then releasing; optional dock and mount |
| Tap to Pay on iPhone | Software | No hardware; iOS SDK + RN; April 24, 2026 setup guide: GA in 20 countries (excluding Puerto Rico), public preview in 17; PIN iOS 16.4+; Apple entitlement + app review required |
| Tap to Pay on Android | Software | No hardware; Android SDK + RN; April 24, 2026 setup guide: GA in 18 countries, public preview in 19 (including CA/CZ/ES/PT); separate `stripeterminal-taptopay` dep; Android 13+, GMS, NFC, ARM |
| Verifone V660p | sPOS | Public preview US/CA; private preview GB/IE/SG; 5.5" 580-nit; **battery** (10h active, 72h standby); 11W power; charge 8h before first use; don't go below 10%; Ethernet via Full Feature Base (optional, request separately) |
| Verifone UX700 | sPOS | Public preview US/CA; private preview GB/IE only (no SG); 5.5" 450-nit; no battery; 4-pin cable into 6-pin port; built-in Ethernet (no accessory needed) |
| Verifone P630 | sPOS | Public preview US/CA; private preview GB/IE/SG; 3.5"; no battery; power cable connects to back (remove cover); Ethernet via D0 Orange Dongle (2M cable, **included in box**); **WiFi-first** network priority (unlike other smart readers); wall/flat-surface mount supported |
| Verifone M425 | sPOS | Public preview **US/CA only** (no private preview anywhere); 3.5" tablet form; no battery; USB-C via dongle into back; power button on back left (hold 2s on, 5s off); Ethernet via D0 Orange Dongle (1M cable, **included in box**) |
| Chipper 2X BT | mPOS (legacy) | US row in the May and November 2026 mobile reader overviews. Separate November device and setup guides label the reader no longer supported and say it is no longer available for purchase. |
| Verifone P400 | sPOS (legacy) | Older US countertop reader |

All Verifone models share: Android 13, quad-core Cortex A53, 2GB RAM, 32GB, E2EE + P2PE capable (individual PCI listings). Must contact Sales to order. Not all models available in every country.

### SDK compatibility

| SDK | S700/S710 | WisePOS E | M2 | WisePad 3 | Tap to Pay | Verifone |
| --- | --- | --- | --- | --- | --- | --- |
| iOS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Android | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| React Native (Preview) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Server-driven | ✓ | ✓ | – | – | – | ✓ |
| JavaScript | ✓ | ✓ | – | – | – | ✓ |

### Payment input support

| Input | S700/S710 | WisePOS E | M2 | WisePad 3 | Tap to Pay | Verifone |
| --- | --- | --- | --- | --- | --- | --- |
| Contactless / NFC wallets | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| EMV chip | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| Magstripe | ✓ | ✓ | ✓ | – | – | ✓ |
| Offline mode | ✓ | ✓ | ✓ | ✓ | – | ✓ |

### Additional features

| Feature | S700/S710 | WisePOS E | M2 | WisePad 3 | Tap to Pay | Verifone |
| --- | --- | --- | --- | --- | --- | --- |
| Tipping | ✓ on-reader+receipt | ✓ on-reader+receipt | Receipt only | ✓ on-reader+receipt | App-impl. | ✓ |
| On-screen input collection | ✓ | ✓ | – | – | App-impl. | ✓ |
| Custom splash screen | ✓ | ✓ | – | ✓ | – | P400 (May 2026, [[source-stripe-terminal-splash-screen]]) |
| Custom POS app | ✓ (paid) | – | – | – | App-impl. | ✓ (paid) |
| [[source-stripe-terminal-cellular-config]] fleet cellular settings (May 2026) | S710 only | – | – | – | – | – |

### Operational rules

- **One reader per SDK instance**: each reader connects to one SDK instance at a time — four readers need four devices.
- **Automatic updates**: smart readers update when powered on, charged, and idle; Bluetooth readers update on SDK connection. Battery must be **>50%** to install updates. Required updates block the reader until complete.
- **Simulated reader**: registration codes `simulated-wpe`, `simulated-s700`, `simulated-s710` (sandbox only).
- **Mobile reader registration**: no Dashboard/API pre-registration needed — associate with `locationId` at connection time. See the SDK variants in [[source-stripe-terminal-register-readers#Mobile Reader Registration|Register readers]].
- **Don't pair via device Settings**: pairing through OS Bluetooth settings makes the reader unavailable to your app.
- **Standby mode**: do NOT call `disconnectReader` to save power — reader manages power in standby.
- **Reader reboot**: M2 and WisePad 3 auto-reboot after 24h; force with `rebootReader` API.
- **Auto-reconnect on app start**: NOT automatic — store serial number persistently, re-discover on launch.
- **USB connections**: General setup guidance describes USB for Android and Bluetooth for iOS. The retained iOS `5.8.0` public headers also contain conditionally compiled USB types, so do not treat iOS USB as generally available without current Stripe confirmation.

### WisePad 3 Bluetooth pairing (Nov 2025 change)

Numeric comparison pairing now required for new/re-pairings: verify 6-digit code on both devices, confirm on WisePad 3, pair on POS. Only applies when pairing with a new device or re-pairing a "forgotten" device.

### Tap to Pay: iPhone vs Android

Both accept: Visa/MC/Amex/Discover contactless, NFC wallets, QR, PIN. Regional: eftpos (AU), Interac (CA), Cartes Bancaires (FR).

**Country differences in the 2026-04-24 [[source-stripe-terminal-tap-to-pay|setup guide]] capture:**

- iPhone GA but Android preview: CA, CZ, ES, PT
- Android GA but iPhone preview: FI, MY
- iPhone not available: Puerto Rico

**iPhone-specific:**

- Apple Developer entitlement required (`com.apple.developer.proximity-reader.payment.acceptance = true`) + Apple app review
- "How to Tap" instructional overlay required before submission (ProximityReaderDiscovery API, iOS 18+)
- PIN: iOS 16.4+

**Android-specific:**

- Separate dependency: `com.stripe:stripeterminal-taptopay` (not `stripeterminal`)
- Requirements: Android 13+, NFC + ARM, not rooted, GMS certified, hardware keystore ECDH v100+, security patch <12 months, developer options disabled
- PIN: Android SDK v4.3.0+; PIN pad appears at random screen position (security)
- Custom UX via `TapToPayUxConfiguration` (colors, dark mode, tap zone)

**CVM/PIN regional gotchas (both):**

- UK: SCA may require card insertion for some issuers → `offline_pin_required` decline
- Canada & Finland: many cards are offline PIN only → Tap to Pay cannot fulfill; recommend alternate method

### Smart reader network architecture (S700/S710, WisePOS E)

Smart reader firmware communicates **directly with Stripe**. Your POS app connects to the reader via:

- **LAN** (Terminal SDK) — reader must be on the same local network as the POS
- **Internet** (server-driven integration) — recommended for S700/S710 and WisePOS E. The dated [[source-stripe-terminal-bbpos-wisepos-e]] guide recommends the Stripe API for this path. See [[source-stripe-terminal-setup-wisepos-e]] for the two WisePOS E connection legs.

**Network priority for S710**: Ethernet → WiFi → Cellular (auto-managed at Android level). Plugging in Ethernet while on WiFi automatically switches; removing from dock reverts to WiFi.

**Ethernet hub** (optional, sold separately): provides 10/100 Ethernet + 2× USB-A for peripherals (barcode scanner, printer); requires 27W power; compatible with S700/S710 Dock.

## Payment Method Availability

Terminal **requires local currency** for all in-person transactions. Readers auto-configure for their region. NFC mobile wallets (Apple Pay, Google Pay, Samsung Pay) are supported across Terminal.

| Payment method | Type | Countries | Reader constraints |
| --- | --- | --- | --- |
| Visa | Card | All Terminal countries | All readers |
| Mastercard | Card | All Terminal countries | All readers |
| American Express | Card | All except Malaysia | All readers |
| Discover & Diners | Card | US, CA, JP (preview), EMEA | Reader varies by region; Diners not in JP |
| China Union Pay | Card | US, CA | Over Discover network; WisePOS E no contactless |
| eftpos | Card | Australia | WisePad 3, WisePOS E, S700, S710, Tap to Pay |
| girocard | Card | Germany | WisePad 3, S700 only |
| Cartes Bancaires | Card | France | WisePad 3, S700, S710, Tap to Pay (preview) |
| Interac | Card | Canada | WisePad 3, WisePOS E, Verifone P400, S700, S710, Tap to Pay (preview) |
| JCB | Card | US, CA, AU, NZ, JP | Via Discover (US) or Amex (CA/AU/NZ) network |
| Maestro | Card | All non-US Terminal countries | Sunsetting: no new cards since July 2023 |
| WeChat Pay | Wallet | 20 countries | WisePOS E, S700, S710, Tap to Pay |
| Affirm | BNPL | US, CA, GB | WisePOS E, S700, S710, Tap to Pay |
| PayNow | Real-time | Singapore | WisePOS E, S700, S710, Tap to Pay |

**QR payment integration notes**: Simulated reader not supported — physical reader required for testing. No offline support. `wechat_pay` and `paynow` require automatic capture; `affirm` supports manual. Affirm requires `return_url`. WeChat Pay not available in Japan. See [[source-stripe-terminal-additional-payment-methods]].

## Example Apps and Repos

| SDK | Example repo |
| --- | --- |
| JavaScript | `github.com/stripe/stripe-terminal-js-demo` |
| iOS | `github.com/stripe/stripe-terminal-ios` (Example/Example.xcworkspace) |
| Android | `github.com/stripe/stripe-terminal-android` (Example project) |
| React Native | `github.com/stripe/stripe-terminal-react-native` (Expo) |

Shared backend: `github.com/stripe/example-terminal-backend` (Sinatra; runs locally or on Render free tier).

## Regional Integration Rules

**Universal**: Stripe account AND Location must be in the same country; local currency only.

**Regional reader listings.** The 2026-04-24 [[source-stripe-terminal-regional|regional guide]] lists WisePOS E and S700 as smart readers for Germany and S700 for Japan, with WisePad 3 as a mobile reader for both. The regional guide and the May 1 Tap to Pay readers overview list iPhone for Japan and omit Android there. The April regional table lists Android Tap to Pay as Gibraltar’s only reader option. The November 7 [[source-stripe-terminal-tap-to-pay-readers|Tap to Pay reader overview]] lists both platforms for Japan and Android alone for Gibraltar. The November S710 overview and setup badge differ in their lists for Germany and Japan. See [[source-stripe-terminal-smart-readers]] for the dated comparison. A Tap to Pay market listing leaves GA or preview status, account or device eligibility, and physical reader availability to separate evidence.

**Canada (CA) — Interac**: Add `interac_present` to `payment_method_types`. Interac authorizes and captures in one step, which can be asynchronous. The April 24, 2026 regional guide lists `automatic`, `automatic_async`, and `manual_preferred` as supported capture settings as of API `2025-03-31.basil`. With `manual_preferred`, an Interac payment still captures in one step while other cards can follow a separate capture flow. `manual` declines Interac. **In-person refunds are mandatory.** Ordinary online refunds through the Refunds API or Dashboard are unavailable. The April regional guide documents a server-driven in-person Terminal reader `refund_payment` endpoint with the original card and matching currency. Interac Flash max 250 CAD. A PIN is required above 100 CAD or on the fourth consecutive contactless transaction.

**Australia (AU) — eftpos**: automatic/manual_preferred/automatic_delayed capture only; min SDK iOS 2.20.0 / Android 2.20.0 / RN 0.0.1-beta.12.

**EEA (GB, IE, FR, DE, etc.) — SCA**: chip+PIN satisfies SCA; contactless may trigger card insertion + PIN → two-charge pattern (soft decline first, then authorized/declined). Low-value exemption <50 EUR; expires after 5 uses or >150 EUR cumulative.

See [[source-stripe-terminal-regional]] for full per-country requirements.

## Network Requirements

### Mobile readers (M2, WisePad 3)

POS device needs internet to Stripe. Avoid 2.4GHz interference (e.g., microwaves near BT readers).

### Smart readers (WisePOS E, S700/S710, Verifone)

- **IPv4 required** — IPv6-only not supported
- **WiFi 6 (802.11ax) not supported**
- WiFi + Ethernet simultaneously = unstable — use one only
- WiFi: WPA/WPA2/WPA3-Personal or WPA2/WPA3 EAP-PEAP Enterprise required; Verifone P400 = WPA/WPA2-Personal only
- Ethernet: 10/100 only
- DHCP: reader must keep same IP for a full workday minimum
- Reader and POS must be on **same local network** (SDK integrations); direct communication required; DNS must resolve local IPs

**DNS test**: `10-42-42-42.test.device.stripe-terminal-local-reader.net` → should resolve to `10.42.42.42`. If not, switch to Cloudflare (`1.1.1.1`) or Google DNS (`8.8.8.8`).

See [[source-stripe-terminal-network-requirements]] for full troubleshooting steps and browser LNA fix instructions.

## Integration Architecture by Reader Type

| Reader category | Model | POS communicates with reader via | Reader communicates with Stripe via |
| --- | --- | --- | --- |
| Mobile readers | M2, WisePad 3 | BT or USB (SDK) | SDK on POS device |
| Smart readers (local-network SDK) | WisePOS E, S700/S710 | LAN (SDK) | Directly (internet) |
| Stripe Reader T600 (SDK) | T600 | The November product guide describes internet, LAN or handoff SDK connections. See the T600 row under Reader Hardware. | See product and integration guidance |
| Smart readers (server-driven) | WisePOS E, S700/S710, Verifone, T600 (named in the November 2026 overview) | REST API (internet) | Directly (internet) |
| Tap to Pay | iPhone, Android | n/a — phone IS the reader | SDK on phone |

The JavaScript SDK local-network route requires the POS and reader to share a network. The November 7, 2026 JavaScript API reference also says to register a smart reader to the account before discovery in the app. The May 1, 2026 capture names the Verifone P400. See [[source-stripe-terminal-js-sdk-reference]].

## Locations

Every Terminal reader — **including the simulated reader** — requires a Location object before connecting. Create Locations via Dashboard or API. Locations represent physical places; mobile businesses can use a primary address.

**Address requirements (May 2026).** The historical guide lists four field groups and country-specific Beta flags. The November capture links to variants. See [[source-stripe-terminal-locations-and-zones#Required Address Fields (May 1, 2026)|the dated country lists]].

- `line1`, `city`, `state`, `postal_code`, `country` applies to six countries in the May list, including Japan (Beta).
- `line1`, `city`, `postal_code`, `country` applies to the longer May list, including Switzerland and the United Kingdom.
- `line1`, `postal_code`, `country` applies to Ireland, Singapore, and the May Beta entries for Bulgaria, Croatia, Cyprus, Malta and Slovenia.
- `line1` and `country` applies to Gibraltar (Beta in May).

**Cannot change a location's country** — create a new location and re-register readers.

**Zones (May 2026).** Optional Dashboard groups can nest, with at most one zone per Location. Remove readers before deleting a Location and clear Locations before deleting a zone. The Dashboard guide allows moving Locations with their readers to a different zone. The May API variant excludes zone creation or modification.

**Connection token scoping (May 2026).** The optional `location` in `connectionTokens.create` restricts smart-reader access to that Location. Omit it for no Location filter. The parameter has no effect on Bluetooth reader discovery.

**Connect**:

- Direct charges (May 2026): create the Location with the `Stripe-Account` header. Only the authenticated connected account can access it.
- Destination charges (May 2026): the platform owns its Locations and can add an optional connected-account reference to Location `metadata` when needed.

See [[source-stripe-terminal-locations-and-zones]] for the May 2026 functional guide and November Dashboard/API navigation.

## Development Workflow

1. **Simulated reader** — no hardware required; verify full integration
2. **Physical reader** — order reader + physical test cards; test with real hardware
3. **Production** — deploy

## Testing

**Mobile wallets (Apple Pay, Google Pay) cannot be tested in test mode.**

### Simulated test cards

SimulatorConfiguration persists for **30 minutes** across collect + confirm steps. Server-driven integrations must call `stripe.testHelpers.terminal.readers.presentPaymentMethod()` explicitly (SDKs auto-simulate).

Key simulated cards: `4242...` (Visa success), `4000...0002` (charge declined), `4000...9995` (insufficient funds), `4001007020000002` (offline PIN), `4001000360000005` (online PIN), `4000...5126` (refund fails async).

### Physical test card

Sandbox only; chip + contactless; PIN `1234`. Test outcome by **last two digits of amount**:

| Decimal | Result |
| --- | --- |
| 00 | Approved |
| 01 | `call_issuer` |
| 02 | Offline PIN flow |
| 03 | Online PIN (any 4-digit) |
| 05 | `generic_decline` |
| 55 | `incorrect_pin` |
| 65 | `withdrawal_count_limit_exceeded` |
| 75 | `pin_try_exceeded` |

Regional physical test cards: Interac (CA, no contactless) and eftpos (AU) — separate cards, order from Dashboard.

See [[source-stripe-terminal-testing]] for the full standard + error test card number tables.

## Key Integration Rules

### PaymentIntents for Terminal

`payment_method_types` must include `'card_present'`. Use `capture_method: 'manual_preferred'` in `payment_method_options.card_present` to prefer manual capture.

**Critical payment rules:**

- **Don't recreate PaymentIntent on card decline** — reuse the same PI; PI must be in `requires_payment_method` state to be processable
- **Manual capture: must capture within 2 days** — authorization expires and funds are released
- **After collectPaymentMethod: must authorize or cancel within 30 seconds**
- **On timeout: retry with the same PI** — `terminal_reader_timeout` can be a false negative (reader may have received command)
- **JS SDK: always confirm client-side** — server-side confirmation bypasses PIN prompts → failures
- **Reader offline**: Stripe considers reader offline after **2 minutes** of no signal

### ConnectionToken

- Authenticate the `/connection_token` endpoint — the secret grants access to all your readers
- **Never cache** — the SDK manages the lifecycle
- Pass `location` ID to scope reader access

### JavaScript SDK loading

```text
https://js.stripe.com/terminal/v1/
```

Must always load directly from `js.stripe.com`. **Do not bundle or self-host** — reader firmware updates can break a bundled copy without warning.

### Simulated reader testing

```javascript
terminal.setSimulatorConfiguration({testCardNumber: '4242424242424242'});
```

Call before `collectPaymentMethod` to simulate different card outcomes. Test cards: `4242...` (success), `4000...9995` (decline).

## MOTO (Mail Order / Telephone Order)

MOTO allows merchants to enter cardholder-provided card details on a Terminal smart reader. Requires Stripe support access.

- **Supported readers**: S700/S710 and WisePOS E only
- **Transaction type**: card-not-present (CNP) — no liability shifts; higher pricing than card-present
- **Reader UI**: enter card number, CVC, expiry, postal code → summary → confirm
- **Not available in Malaysia**
- **Compliance**: cardholder must NOT be present; must initiate over phone/mail; merchant verifies identity; PCI required

**Integration**: `payment_method_types: ['card']` (not `card_present`). Enable per SDK: server-driven = `process_config.moto: true`; iOS/Android = `MotoConfiguration`; JS = `config_override.moto: true`; RN = `motoConfiguration`. Must reset cart display to splash screen before MOTO collection. CVC mandatory (skipping CVC = private preview).

**Save card for future use**: use SetupIntent with `payment_method_types: ['card']` + MOTO flag + `allow_redisplay: 'always'|'limited'`. Requires written customer consent and disclosure of purpose, timing, amount, cancellation policy.

See [[source-stripe-terminal-moto]], [[source-stripe-terminal-moto-payments]], and [[source-stripe-terminal-moto-save-card]] for details.

## Terminal + Connect

Connected accounts require `card_payments` capability. Three charge type patterns:

| Charge type | Stripe-Account header | Resource ownership | Key PaymentIntent params |
| --- | --- | --- | --- |
| Direct charges | ✓ Set on all requests | Connected account owns everything | None extra (ConnectionToken scopes to connected account) |
| Destination charges | ✗ Platform key only | Platform owns locations/readers | `on_behalf_of`, `transfer_data[destination]`, `application_fee_amount` |
| Separate charges + transfers | ✗ Platform key only | Platform owns everything | `transfer_group`; create transfers separately after capture |

**`on_behalf_of`**: required when platform country ≠ connected account country; auto-settles in account's country using account's fee structure.

**`source_transaction`**: when creating transfers for separate charges, use this to tie the transfer to the charge — avoids balance timing failures; transfer executes when charge funds settle.

**Platform-owned readers (private preview)**: platform owns locations/readers, connected accounts own PaymentIntents; allows one reader to process for multiple connected accounts; server-driven + single-platform only.

See [[source-stripe-terminal-connect]] for full code samples for all three patterns.

## Relationship to Other Stripe Products

Terminal shares the same Dashboard and payment infrastructure as Stripe's online payments. This means:

- A single Dashboard view for both in-person and online transactions
- Same PaymentIntents API and webhook model as online payments
- Connect platforms can enable Terminal for their connected accounts (see Terminal + Connect section above)

## Key Players

- [[stripe]] — sole provider of this product

## Sources

- [[source-stripe-terminal-mobile-readers]] — May and November 2026 market lists, hardware-specific routes, SDK connectivity, and update and reboot behavior.
- [[source-github-stripe-terminal-android]] — exact `stripeterminal@5.8.0` Android SDK baseline: permissions, lifecycle, reader connection, payments, SetupIntents, refunds, offline forwarding, Tap to Pay, updates, and support policy
- [[changelog-github-stripe-terminal-android]] — package-qualified Android Terminal history: v5 migration boundary, `5.6.0` offline migration risk, and exact `5.8.0` permission, buzzer, printing, Keystore, update, and PIN changes
- [[source-github-stripe-terminal-ios]] — exact `StripeTerminal@5.8.0` iOS SDK baseline: initialization, reader lifecycle, payments, SetupIntents, offline mode, Tap to Pay, QR methods, updates, and support policy
- [[changelog-github-stripe-terminal-ios]] — package-qualified iOS Terminal history: v5 migration boundary, accumulated v5 milestones, and exact 5.8.0 changes
- [[source-stripe-terminal-overview]] — April and November 2026 Terminal landing pages. November adds the sixth integration path, Stripe’s no-code Preview.
- [[source-stripe-terminal-how-it-works]] — Architecture (4 components), connection types, encryption tiers (E2EE vs P2PE), fleet management, integration scope
- [[source-stripe-terminal-global-availability]] — 23 GA countries, 15 preview countries, payment method × reader matrix, Maestro sunset
- [[source-stripe-terminal-select-reader]] — Reader lineup, SDK/payment/feature matrices, physical specs, operational rules (1:1 SDK, auto-updates)
- [[source-stripe-terminal-smart-readers]] — May and November 2026 smart-reader catalogs, dated S710 lists, T600 integration routing and update versus restart guidance.
- [[source-stripe-terminal-setup-reader-s700-s710]] — S700 vs S710 country availability, S710 SDK minimums, network priority, Ethernet hub setup, admin passcode
- [[source-stripe-terminal-s700-s710]] — May and November 2026 S700/S710 reader reference covering regional software versions, separate firmware history, device specifications, diagnostics, and update behavior.
- [[source-stripe-terminal-s700-s710-accessories]] — Case/Hub/Dock/adapter lineup; Hub→POS not reader; Dock no USB payment; Hub+Dock countertop combo
- [[source-stripe-terminal-setup-wisepos-e]] — WisePOS E: 24 countries (no JP), ~8h battery, dark theme default, WiFi/Ethernet only (no cellular), Ethernet dock setup
- [[source-stripe-terminal-bbpos-wisepos-e]] — May and November 2026 WisePOS E operations and firmware tables. November lists reader app `2.46.4.0`, firmware `5.01.06.01` (AU `.eftpos`), and ROM `1.8.9.4`, with HK deployment unresolved.
- [[source-stripe-terminal-setup-reader-m2]] — M2 setup guide covering US and Puerto Rico, BLE and Android-only USB, charging, and power controls.
- [[source-stripe-terminal-stripe-m2]] — May and November 2026 M2 reader references covering the listed software strings, separate firmware changelog and key history, and LED status.
- [[source-stripe-terminal-setup-wisepad3]] — WisePad 3 setup guide covering the PIN pad, auto-off after 5 minutes disconnected, approximately 600 contact or 800 contactless transactions per charge, and device language.
- [[source-stripe-terminal-bbpos-wisepad3]] — May and November 2026 WisePad 3 reader reference covering the availability banners, regional software tables, firmware changelog, and key history.
- [[source-stripe-terminal-tap-to-pay]] — April 24, 2026 Tap to Pay setup guide: iPhone (GA 20, preview 17) and Android (GA 18, preview 19) market classifications, entitlement, device requirements, and CVM
- [[source-stripe-terminal-setup-verifone]] — Verifone V660p/UX700/P630/M425 specs; preview status by model/country; V660p only model with battery; all P2PE capable
- [[source-stripe-terminal-setup-v660p]] — V660p setup: 11W power, 8h initial charge, don't go below 10%, Full Feature Base for Ethernet
- [[source-stripe-terminal-setup-ux700]] — UX700 setup: no battery (mains-only), 4-pin/6-pin connector, built-in Ethernet (no accessory), not in SG
- [[source-stripe-terminal-setup-p630]] — P630 setup: WiFi-first priority (unique), Orange Dongle for Ethernet, wall-mount support, 110-240W, cellular mention uncertain
- [[source-stripe-terminal-setup-m425]] — M425 setup: US/CA only, power button on back left, USB-C via dongle, Orange Dongle for Ethernet, no network priority stated
- [[source-stripe-terminal-verifone-accessories]] — P630/M425 D0 Orange Dongle included in box; V660p Full Feature Base optional; cable lengths (P630=2M, M425=1M)
- [[source-stripe-terminal-design-custom-pos]] — Integration architecture types, Locations required (incl. simulated), development workflow, SDK × reader matrix
- [[source-stripe-terminal-accept-inperson-js-nodejs]] — Complete JS SDK + Node.js code sample: card_present PaymentIntent, ConnectionToken rules, JS SDK must not be bundled, setSimulatorConfiguration
- [[source-stripe-terminal-js-sdk-reference]] — JavaScript SDK API reference: reader discovery, payment operations, errors, and changelog
- [[source-stripe-terminal-sdk-migration-guide]] — SDK v5 migration guide: unified process methods, customer cancel default on, reconnecting status, easyConnect, iOS 15 min, Android Handoff→AppsOnDevices
- [[source-stripe-terminal-sdk-v4-migration-guide]] — historical iOS and Android v4 migration, including default reconnection after unexpected disconnects for mobile and Tap to Pay readers
- [[source-stripe-terminal-sdk-v3-migration-guide]] — Historical migration to SDK 3.0.0 for iOS and Android, with the November 2026 platform index linked for navigation.
- [[source-stripe-terminal-example-applications]] — Example app repos (JS/iOS/Android/RN), shared Sinatra backend, iOS Simulator location note
- [[source-stripe-terminal-testing]] — Full test card tables (20 standard + 4 PIN + 7 error), physical test card amount codes, simulated update scenarios
- [[source-stripe-terminal-setup-integration]] — SDK setup guide: versions (iOS ~5.0, Android 5.4.1), iOS plist requirements, Android lifecycle-aware init, server-driven limitations, Chrome 142+ note
- [[source-stripe-terminal-connect]] — Terminal + Connect: 3 charge types, resource ownership, on_behalf_of, source_transaction, platform-owned readers (private preview)
- [[source-stripe-terminal-connect-reader]] — Reader connection guide: BT pairing (Nov 2025), mobile reader locationId, standby mode, reboot API, update rules, USB=Android only, simulated codes
- [[source-stripe-terminal-network-requirements]] — Network requirements: IPv4 only, no WiFi 6, no WiFi+Ethernet combo, DNS test, browser LNA troubleshooting
- [[source-stripe-terminal-collect-card-payment]] — Payment collection: 2-day capture window, 30s collect-to-authorize, reuse PI on decline, JS client-side confirm, reader offline = 2min, error codes
- [[source-stripe-terminal-additional-payment-methods]] — QR code payments (WeChat Pay/Affirm/PayNow): capture rules, async flow, no simulated reader, free-reader-while-pending pattern
- [[source-stripe-terminal-offline-payments]] — Offline payments: unsupported methods (Interac/girocard/QR), EEA PIN requirement, BT vs Internet reader feature differences
- [[source-stripe-terminal-offline-collect-card-payments]] — Offline integration: SDK minimums, 30-day prerequisite, 10K USD max, null stripeId, offlineBehavior, cache-clearing risk, receipt limitations
- [[source-stripe-terminal-moto]] — MOTO: S700/S710+WisePOS E only, CNP pricing, no liability shift, not in Malaysia, compliance requirements
- [[source-stripe-terminal-moto-payments]] — MOTO integration: payment_method_types=['card'], SDK flags, CVC mandatory, cart display reset
- [[source-stripe-terminal-moto-save-card]] — MOTO save-card: SetupIntent + allow_redisplay, SDK flags, written consent + disclosure required
- [[source-stripe-terminal-regional]] — Regional: same-country rule, CA Interac mandatory in-person refund, AU eftpos SDK minimums, DE/JP reader restrictions, EEA SCA two-charge pattern
- [[source-stripe-terminal-collect-tips]] — Tipping overview: on-reader (reader-prompted, wide country support) vs on-receipt (US only, tip added at capture); mandatory tips in original amount; see [[stripe-terminal-tipping]]
- [[source-stripe-terminal-on-receipt-tipping]] — On-receipt tipping detail: overcapture flow, 50%/50 USD limit, eligible MCCs (restaurants/taxicabs/beauty/etc), fallback via incremental auth or generated_card
- [[source-stripe-terminal-on-reader-tipping]] — On-reader tipping detail: Configuration API (smart/pct/fixed), tip lifecycle, skip tipping, tip-eligible amounts, 38-country availability
- [[source-stripe-terminal-save-payment-details]] — Save payment details: generated_card mechanism, two save flows, off-session charging, card fingerprints, compliance requirements
- [[source-stripe-terminal-save-directly]] — Save directly (SetupIntent): CNP caveat, card networks, allow_redisplay consent model, SDK compatibility, mobile wallet caveats
- [[source-stripe-terminal-save-after-payment]] — Save after payment (PaymentIntent): setup_future_usage, allow_redisplay at collect, generated_card retrieval, fallback options
- [[source-stripe-terminal-incremental-authorizations]] — Incremental authorizations: availability by card/MCC, setup, incrementAuthorization API, capture auto-increment behavior
- [[source-stripe-terminal-extended-authorizations]] — Extended authorizations: capture window up to 30 days, card/MCC eligibility table, capture_before field, Amex caveat
- [[source-stripe-terminal-refunds]] — Refunds and cancellations: cancel pre-capture (card eligibility), online vs in-person refunds, Interac mandatory in-person refund
- [[source-stripe-terminal-receipts]] — Receipts: prebuilt email, manual test sends, custom EMV fields, and cardholder `preferred_locales` when provided
- [[source-stripe-terminal-display-cart]] — May 2026 cart-display guide covering setup, resetting, and US pre-dip, with the November platform index linked for navigation.
- [[source-stripe-terminal-collect-inputs]] — collect on-screen inputs guide captured 2026-05-01, with the 2026-11-07 platform variant index linked for navigation.
- [[source-stripe-terminal-collect-data]] — May 2026 private-preview non-PCI swiped-data guide with a dated November SDK variant index.
- [[source-stripe-terminal-collect-nfc-data]] — May 2026 private-preview NFC UID guide with a dated November SDK variant index.
- [[source-stripe-terminal-apps-on-devices]] — May and November 2026 Apps on Devices overviews, integration and APK scopes, DevKit requirements, permissions and single-platform Connect controls.
