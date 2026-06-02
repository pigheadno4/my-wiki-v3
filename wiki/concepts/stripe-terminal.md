---
title: "Stripe Terminal"
type: concept
category: technology
tags: [stripe, terminal, in-person, point-of-sale, card-reader, tap-to-pay, offline-payments, connect, sdks, global, payment-methods, regional]
---

## Stripe Terminal

Stripe's in-person payment product. Enables businesses to accept card payments using physical card readers and unifies in-person payments with online payments in a single Stripe Dashboard. Works with Stripe Connect platforms.

## Architecture

Every Terminal deployment has four components:

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

Five distinct ways to integrate Terminal, ranging from full custom builds to no-code options:

| Path | Description | Code required |
| --- | --- | --- |
| **Custom POS** | Build a fully custom point-of-sale using SDKs (Android, iOS, JavaScript, React Native) or the server-driven API | Yes |
| **Tap to Pay** | Accept contactless payments using a compatible iPhone or Android device — no dedicated reader hardware needed | Yes (SDK) |
| **Apps on devices** | Deploy a custom Android POS app directly onto Stripe smart readers | Yes |
| **Third-party POS** | Integrate Terminal into existing third-party POS, hardware, and commerce stacks | No code |
| **Gateway** | Combine Stripe with gateway-supported POS systems, third-party hardware, gift cards | No code |

## SDKs

| SDK | Platform | Version | Notes |
| --- | --- | --- | --- |
| JavaScript SDK v1 | Web / browser-based POS | v1 | Load from `js.stripe.com` only; Chrome 142+ needs local network permission; same-network + local DNS required |
| iOS SDK | Native iOS | ~5.0 (CocoaPods/SPM) | iOS 13+; 4 Info.plist entries required; location mandatory |
| Android SDK | Native Android | 5.4.1 | AndroidX required; Java 8 target; lifecycle-aware init |
| React Native SDK | Cross-platform mobile | latest (public preview) | `requestNeededAndroidPermissions` helper; Android 12+ needs `exported=true` |

A server-driven API is also available for any backend regardless of platform.

### Server-driven limitations

Server-driven does **not** support mobile readers (M2, WisePad 3) or offline payments. Supports any language/middleware + internet connection (not LAN).

### SDK setup: location required on iOS and Android

Both iOS and Android require location services for payments. If location access is revoked, payments are disabled until restored.

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

- Order pre-certified readers and accessories from the Stripe Dashboard; up to 10,000 units per order
- Ship to any location; Connect platforms can route readers to connected accounts' business locations
- Monitor entire reader fleet from the Dashboard
- Self-service returns (33 countries): 30-day window, original packaging, first-return shipping fee refund
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
- **Collect on-screen inputs** — display prebuilt input forms (S700/S710 + WisePOS E only); 6 types: signature, selection, email, phone, text, numeric; up to 5 per call; signature images stored 7 days; see [[stripe-terminal-collect-inputs]]
- **Collect swiped data** — private preview; reads non-PCI magstripe data (e.g. gift cards) via `collectData()`; token returned, cleartext retrieved server-side; 24h storage; S700/S710/WisePOS E/M2/Chipper2X; not offline; see [[source-stripe-terminal-collect-data]]
- **Collect NFC tapped data** — private preview; reads NFC UID from non-payment instruments (cards, wristbands); available offline; S700/S710/M2 only; UID returned directly (no server retrieval); cannot collect card payments; see [[source-stripe-terminal-collect-nfc-data]]
- **Apps on Devices** — deploy custom Android POS app on smart readers; two modes: POS on reader or POS + consumer-facing app via TCP/IP; AOSP (no Google Play Services); 200MB APK limit; 8GB storage limit; single-platform Connect requirement; see [[stripe-terminal-apps-on-devices]]
- **Send receipts** — prebuilt email (set `receipt_email` on PI → auto-sent on capture) or custom receipts with required EMV fields (`account_type`, `application_preferred_name`, `dedicated_file_name`); see [[source-stripe-terminal-receipts]]

## Global Availability

**GA (23 countries)**: AT, AU, BE, CA, CH, CZ, DE, DK, ES, FI, FR, GB, IE, IT, LU, MY, NL, NO, NZ, PT, SE, SG, US

**Preview (15 countries)**:

- Full Terminal: JP, PL
- Tap to Pay only: BG, CY, EE, GI, HR, HU, LI, LT, LV, MT, RO, SI, SK

## Reader Hardware

| Reader | Category | Notes |
| --- | --- | --- |
| Stripe Reader S700 | sPOS | 5.5" screen, Android 10, WiFi/Ethernet, 64GB — 25 countries (all GA + CZ/PL/JP preview) |
| Stripe Reader S710 | sPOS | Same as S700 + 4G/LTE cellular — 16 countries only (US/CA/GB/IE/SG/AU/NZ/FR/BE/AT/ES/SE/NO/PT/FI/MY); min SDK: iOS v4.7.3, Android v3.8.0, RN v0.0.1-beta.28 |
| BBPOS WisePOS E | sPOS | 5" screen, Android 9, WiFi/Ethernet only (no cellular) — 24 countries (all GA + PL preview, no JP); ~8h battery; dark theme default |
| BBPOS WisePad 3 | mPOS | 2.4" screen, BLE/USB, **non-US** (25 countries, excl. US, incl. JP/PL preview); physical PIN pad for PIN-auth markets; auto-off 5min disconnected; ~600 contact/~800 contactless tx per charge |
| Stripe Reader M2 | mPOS | US only (all 50 states + Puerto Rico); screenless; BT LE/USB; iOS/Android/RN SDKs only; auto-off after 10h inactivity; reset: hold 14s; dock + mount accessories available |
| Tap to Pay on iPhone | Software | No hardware; iOS SDK + RN; GA 20 countries (not Puerto Rico); preview 17; PIN iOS 16.4+; Apple entitlement + app review required |
| Tap to Pay on Android | Software | No hardware; Android SDK + RN; GA 18 countries; preview 19 (CA/CZ/ES/PT are preview); separate `stripeterminal-taptopay` dep; Android 13+, GMS, NFC, ARM |
| Verifone V660p | sPOS | Public preview US/CA; private preview GB/IE/SG; 5.5" 580-nit; **battery** (10h active, 72h standby); 11W power; charge 8h before first use; don't go below 10%; Ethernet via Full Feature Base (optional, request separately) |
| Verifone UX700 | sPOS | Public preview US/CA; private preview GB/IE only (no SG); 5.5" 450-nit; no battery; 4-pin cable into 6-pin port; built-in Ethernet (no accessory needed) |
| Verifone P630 | sPOS | Public preview US/CA; private preview GB/IE/SG; 3.5"; no battery; power cable connects to back (remove cover); Ethernet via D0 Orange Dongle (2M cable, **included in box**); **WiFi-first** network priority (unlike other smart readers); wall/flat-surface mount supported |
| Verifone M425 | sPOS | Public preview **US/CA only** (no private preview anywhere); 3.5" tablet form; no battery; USB-C via dongle into back; power button on back left (hold 2s on, 5s off); Ethernet via D0 Orange Dongle (1M cable, **included in box**) |
| Chipper 2X BT | mPOS (legacy) | Older Bluetooth mobile reader |
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
| Custom splash screen | ✓ | ✓ | – | ✓ | – | ✓ |
| Custom POS app | ✓ (paid) | – | – | – | App-impl. | ✓ (paid) |
| Cellular | S710 only | – | – | – | – | – |

### Operational rules

- **One reader per SDK instance**: each reader connects to one SDK instance at a time — four readers need four devices.
- **Automatic updates**: smart readers update when powered on, charged, and idle; Bluetooth readers update on SDK connection. Battery must be **>50%** to install updates. Required updates block the reader until complete.
- **Simulated reader**: registration codes `simulated-wpe`, `simulated-s700`, `simulated-s710` (sandbox only).
- **Mobile reader registration**: no Dashboard/API pre-registration needed — associate with `locationId` at connection time.
- **Don't pair via device Settings**: pairing through OS Bluetooth settings makes the reader unavailable to your app.
- **Standby mode**: do NOT call `disconnectReader` to save power — reader manages power in standby.
- **Reader reboot**: M2 and WisePad 3 auto-reboot after 24h; force with `rebootReader` API.
- **Auto-reconnect on app start**: NOT automatic — store serial number persistently, re-discover on launch.
- **USB connections**: Android only; iOS uses Bluetooth.

### WisePad 3 Bluetooth pairing (Nov 2025 change)

Numeric comparison pairing now required for new/re-pairings: verify 6-digit code on both devices, confirm on WisePad 3, pair on POS. Only applies when pairing with a new device or re-pairing a "forgotten" device.

### Tap to Pay: iPhone vs Android

Both accept: Visa/MC/Amex/Discover contactless, NFC wallets, QR, PIN. Regional: eftpos (AU), Interac (CA), Cartes Bancaires (FR).

**Country differences:**

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
- **Internet** (server-driven integration) — recommended for S700/S710

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

**Reader availability exceptions**: DE = WisePOS E + S700 only (no S710); JP = S700 only (no WisePOS E, no S710, no Android Tap to Pay); GI = Tap to Pay Android only.

**Canada (CA) — Interac**: add `interac_present` to `payment_method_types`; Interac = automatic capture only; use `manual_preferred` for mixed; `manual` capture → Interac declined; **in-person refund mandatory** (cannot refund Interac via API/Dashboard); Interac Flash max 250 CAD; PIN after 100 CAD or 4th contactless.

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
| Smart readers (SDK) | WisePOS E, S700/S710 | LAN (SDK) | Directly (internet) |
| Smart readers (server-driven) | WisePOS E, S700/S710, Verifone | REST API (internet) | Directly (internet) |
| Tap to Pay | iPhone, Android | n/a — phone IS the reader | SDK on phone |

JavaScript SDK requires same-network LAN when used with smart readers.

## Locations

Every Terminal reader — **including the simulated reader** — requires a Location object before connecting. Create Locations via Dashboard or API. Locations represent physical places; mobile businesses can use a primary address.

**Address requirements vary by country** (4 tiers):

- AU/CA/IT/JP/ES/US: `line1`, `city`, `state`, `postal_code`, `country`
- Most EU + MY/NZ/NO: `line1`, `city`, `postal_code`, `country`
- BG/HR/CY/IE/MT/SG/SI: `line1`, `postal_code`, `country`
- GI: `line1`, `country`

**Cannot change a location's country** — create a new location and re-register readers.

**Zones** (optional): hierarchical grouping of locations; nested zones supported; one zone per location; Dashboard only (API cannot create/modify zones).

**Connection token scoping**: pass `location` to `connectionTokens.create` to restrict the token to smart readers at that location. No effect on Bluetooth readers.

**Connect**:

- Direct charges: create Location under connected account with `Stripe-Account` header
- Destination charges: Locations belong to the platform; store connected account in Location `metadata`

See [[source-stripe-terminal-locations-and-zones]] for full address requirements and API samples.

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

- [[source-stripe-terminal-overview]] — Terminal landing page: 5 integration paths, SDK list, in-person fundamentals, features, Connect support
- [[source-stripe-terminal-how-it-works]] — Architecture (4 components), connection types, encryption tiers (E2EE vs P2PE), fleet management, integration scope
- [[source-stripe-terminal-global-availability]] — 23 GA countries, 15 preview countries, payment method × reader matrix, Maestro sunset
- [[source-stripe-terminal-select-reader]] — Reader lineup, SDK/payment/feature matrices, physical specs, operational rules (1:1 SDK, auto-updates)
- [[source-stripe-terminal-setup-reader-s700-s710]] — S700 vs S710 country availability, S710 SDK minimums, network priority, Ethernet hub setup, admin passcode
- [[source-stripe-terminal-s700-s710]] — S700/S710 firmware reference: 4-component software, latest 2.41.2.0/1.00.03.00, diagnostics, payment sounds, NFC UID (1.00.00.25)
- [[source-stripe-terminal-s700-s710-accessories]] — Case/Hub/Dock/adapter lineup; Hub→POS not reader; Dock no USB payment; Hub+Dock countertop combo
- [[source-stripe-terminal-setup-wisepos-e]] — WisePOS E: 24 countries (no JP), ~8h battery, dark theme default, WiFi/Ethernet only (no cellular), Ethernet dock setup
- [[source-stripe-terminal-bbpos-wisepos-e]] — WisePOS E firmware reference: latest 2.41.2.0/5.01.03.00, tap sounds same for success+failure, both-cables-before-dock rule
- [[source-stripe-terminal-setup-reader-m2]] — M2: US+PR only, BT LE/USB, no screen/UI, auto-off 10h, reset 14s, dock+mount accessories
- [[source-stripe-terminal-stripe-m2]] — M2 firmware reference: latest 2.01.01.00, power button 4s/14s, NFC UID (2.01.00.31), LED states, version format uses hyphens
- [[source-stripe-terminal-setup-wisepad3]] — WisePad 3: non-US (25 countries), PIN pad, auto-off 5min disconnected, ~600/~800 tx per charge, language on-device
- [[source-stripe-terminal-bbpos-wisepad3]] — WisePad 3 firmware reference: software version format, latest firmware 4.01.03.00, config regions, key identifiers (490001/510001/480001)
- [[source-stripe-terminal-tap-to-pay]] — Tap to Pay iPhone (GA 20, preview 17) + Android (GA 18, preview 19); entitlement req; Android device requirements; CVM gotchas
- [[source-stripe-terminal-setup-verifone]] — Verifone V660p/UX700/P630/M425 specs; preview status by model/country; V660p only model with battery; all P2PE capable
- [[source-stripe-terminal-setup-v660p]] — V660p setup: 11W power, 8h initial charge, don't go below 10%, Full Feature Base for Ethernet
- [[source-stripe-terminal-setup-ux700]] — UX700 setup: no battery (mains-only), 4-pin/6-pin connector, built-in Ethernet (no accessory), not in SG
- [[source-stripe-terminal-setup-p630]] — P630 setup: WiFi-first priority (unique), Orange Dongle for Ethernet, wall-mount support, 110-240W, cellular mention uncertain
- [[source-stripe-terminal-setup-m425]] — M425 setup: US/CA only, power button on back left, USB-C via dongle, Orange Dongle for Ethernet, no network priority stated
- [[source-stripe-terminal-verifone-accessories]] — P630/M425 D0 Orange Dongle included in box; V660p Full Feature Base optional; cable lengths (P630=2M, M425=1M)
- [[source-stripe-terminal-design-custom-pos]] — Integration architecture types, Locations required (incl. simulated), development workflow, SDK × reader matrix
- [[source-stripe-terminal-accept-inperson-js-nodejs]] — Complete JS SDK + Node.js code sample: card_present PaymentIntent, ConnectionToken rules, JS SDK must not be bundled, setSimulatorConfiguration
- [[source-stripe-terminal-js-sdk-reference]] — JS SDK API reference: 29 methods (create, discoverReaders, collectPaymentMethod, processPayment, print, etc.), 17 error codes, changelog
- [[source-stripe-terminal-sdk-migration-guide]] — SDK v5 migration guide: unified process methods, customer cancel default on, reconnecting status, easyConnect, iOS 15 min, Android Handoff→AppsOnDevices
- [[source-stripe-terminal-sdk-v4-migration-guide]] — SDK v4 migration guide: consolidated connectReader, auto-reconnect default on, allow_redisplay, unified disconnect callbacks, iOS 14 min
- [[source-stripe-terminal-sdk-v3-migration-guide]] — SDK v3 migration guide: processPayment→confirmPaymentIntent, readReusableCard removed, DiscoveryConfig per-type, iOS 13/Android 26 min
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
- [[source-stripe-terminal-receipts]] — Receipts: prebuilt email receipts, custom receipt EMV fields, cardholder preferred_locales
- [[source-stripe-terminal-display-cart]] — Display cart details: setReaderDisplay, display-only amounts, pre-dip (US only)
- [[source-stripe-terminal-collect-inputs]] — Collect on-screen inputs: 6 input types, customization, webhooks, 7-day signature storage
- [[source-stripe-terminal-collect-data]] — Collect swiped data (private preview): magstripe gift cards, tokenization, 24h storage, disclaimer
- [[source-stripe-terminal-collect-nfc-data]] — Collect NFC tapped data (private preview): NFC UID, offline-capable, S700/S710/M2, no card payments
- [[source-stripe-terminal-apps-on-devices]] — Apps on Devices: two integration modes, AOSP differences, permissions allowlist, Connect single-platform requirement
