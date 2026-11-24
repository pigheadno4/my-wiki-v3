---
title: "Stripe Terminal: Tipping"
type: concept
category: technology
tags: [stripe, stripe-terminal, tipping, in-person-payments, payment-intents]
---

## Definition

Stripe Terminal’s two voluntary tip methods, on-reader and on-receipt, use the PaymentIntents API. Capture conditions are documented below. Include mandatory tips in the original `PaymentIntent` amount. Mandatory tips cannot use either voluntary flow.

## On-reader Tipping

The card reader displays suggested tip options to the customer before payment is collected. The customer selects a tip (or custom amount, or no tip) on the reader screen; the reader automatically adds it to the payment amount.

**Supported readers**: BBPOS WisePad 3, BBPOS WisePOS E, Stripe Reader S700/S710  
**Dated country availability**. The 2026-11-07 tipping overview lists 40 markets in its S700/S710 and WisePOS E on-reader tipping row, adding HK and MX to the 38 in the 2026-04-27 overview. Both overviews list the same nine WisePad 3 markets (AU, CA, FR, DE, IE, NL, NZ, SG, GB). The same-day WisePOS E reader and setup banners omit HK and MX from their 24-market lists, leaving general deployment and account eligibility in those markets unresolved. See [[source-stripe-terminal-on-reader-tipping]] for the captured evidence.\
**Merchant category**: Any  
**Card brands**: Any  
**WisePad 3 SDK minimums**: Android SDK 2.8.1+, iOS SDK 2.16.1+

### Configuration

Set via `Configuration` API object or Dashboard. Three modes:

- **Smart tips**: `smart_tip_threshold` controls the switch — below threshold shows fixed amounts; at or above shows percentages
- **Percentages**: three percentage suggestions (post-tax by default; use tip-eligible amount for pre-tax)
- **Fixed amounts**: three fixed amounts in the currency's smallest unit

Multi-currency constraint: if specifying multiple currencies, must use the same config keys for each (can't mix `percentages`-only USD with `fixed_amounts` EUR).

Config propagation: WisePad 3 updates on SDK connection; WisePOS E takes up to 5 minutes.

### Tip Amount Lifecycle

- **Pre-confirmation**: tip in `amount_tip` field; not yet reflected in `amount`
- **Post-confirmation**: `amount_tip` → 0; `amount` includes tip; tip in `amount_details.tip.amount`

| Scenario | `amount_details.tip.amount` |
| --- | --- |
| On-reader tipping disabled | `null` |
| Enabled, no tip selected | `0` |
| Enabled, tip selected | The selected amount |

After capture: `amount`, `amount_authorized`, and `amount_captured` all reflect the total inclusive of tip. Customer's credit card statement shows the full amount immediately (no pending update).

### When the Tip Screen Is Skipped

1. `Configuration` missing a tipping config
2. `skipTipping` enabled in tipping configuration
3. Reader in unsupported country
4. Config can't apply to payment currency (e.g., payment in EUR, config only specifies USD)

### Per-Transaction Overrides

**Skip tipping** (`skip_tipping` or `skipTipping`). Hide the tip prompt for an individual transaction or temporarily for all transactions. The detailed guide gives server-driven, JavaScript, iOS, Android, and React Native examples.

**Tip-eligible amount** changes the base for percentage tips. The reader shows it alongside the pre-tip amount. A supplied eligible amount must be zero or higher.

- `eligible_amount: 0` → skips tipping regardless of `skip_tipping`
- `eligible_amount` = PaymentIntent amount → ignored
- `eligible_amount > 0` with `skip_tipping: true` → error

**SDK field names**: `amount_eligible` (server-driven), `eligible_amount` (JS), `setEligibleAmount()` (iOS/Android), `tipEligibleAmount` (React Native)

**SDK support**: WisePad 3 via Android/iOS/React Native SDKs; WisePOS E + S700/S710 via all SDKs (server-driven)

## On-receipt Tipping

Tips are collected after authorization via **overcapture** — capturing more than the originally authorized amount. Common in table-service restaurants where staff record tip from a printed receipt. The full captured amount appears on the customer’s statement after capture, with no new authorization to trigger an immediate statement update.

**Supported readers**: Any Terminal reader  
**Country availability**: US only  
**Merchant category**: Restricted (see eligible MCCs below)  
**Card brands**: Visa, Mastercard, American Express, Discover only

**API behavior**:

1. Create and confirm a PaymentIntent with `capture_method: manual`
2. Retrieve with `expand: ['latest_charge']`; check `latest_charge.overcapture_supported` on the Charge before attempting
3. Capture with `amount_to_capture` = authorized amount + tip
4. `amount_authorized` on the Charge retains the pre-tip value; `amount` and `amount_captured` update to the post-tip total

**Overcapture limits**: Up to 50% of the authorized `amount`, or 50 USD, whichever is greater.

- $40 authorized → max capture $90 (floor applies)
- $100 authorized → max capture $150 (50% rule applies)

**When limits are exceeded**:

- Use [[stripe-terminal-incremental-authorizations]] to raise the PaymentIntent `amount` (MCC-dependent)
- Or create a new PaymentIntent using the `generated_card` payment method from the original PaymentIntent

**Eligible MCCs** (US only):

- Taxicabs and limousines
- Eating places and restaurants
- Drinking places (alcoholic beverages)
- Fast food restaurants
- Beauty and barber shops
- Health and beauty spas

**SDK support**: All SDKs, server-driven

## iOS SDK 6.0.0 Capture Default

For `StripeTerminal@6.0.0`, explicitly call `.setCaptureMethod(.manual)` when creating a PaymentIntent for **on-receipt tipping**; the SDK builder now defaults to `.automaticAsync`. The retained example explicitly forces manual capture when a post-authorization tip is requested. This change does not itself establish new on-reader tipping eligibility or remove the requirements above. See [[source-github-stripe-terminal-ios]] and [[changelog-github-stripe-terminal-ios]].

## Android SDK 6.0.0 Capture Default

For `stripeterminal@6.0.0`, explicitly set `CaptureMethod.Manual` for on-receipt tipping: the client creation builder now defaults to `AutomaticAsync`. Do not copy the Java event example's unconditional capture call into an automatic-capture flow. Retain existing eligibility/overcapture checks and inspect payment state before backend capture. See [[source-github-stripe-terminal-android]] and [[changelog-github-stripe-terminal-android]].

## Constraints

- **One method per PaymentIntent**: once on-reader tipping is applied to a `PaymentIntent`, on-receipt tipping cannot be used on the same `PaymentIntent`
- **Capture method by tip method**. The 2026-04-27 overview described both methods as requiring manual capture. The 2026-11-07 overview documents `capture_method=automatic` or `capture_method=manual` for on-reader tipping and `capture_method=manual` for on-receipt tipping. See the dated capture-method evidence in [[source-stripe-terminal-on-reader-tipping]].
- **On-reader tipping limit**: maximum charge amount for the currency (8–9 digits depending on currency), inclusive of tip
- **On-receipt overcapture limit**: 50% of authorized amount or 50 USD, whichever is greater

## Fleet Configuration

The May 2026 fleet guide describes Dashboard location controls and the currency-keyed `tipping` field on the Configuration object. Its Dashboard section says settings apply on the reader within 10 minutes. See [[source-stripe-terminal-tipping-config]] for the fleet guide and November Dashboard/API index, and [[source-stripe-terminal-configurations]] for account defaults and location overrides.

## Sources

- [[source-stripe-terminal-collect-tips]] — overview: method comparison, country availability, API behavior tables
- [[source-stripe-terminal-on-reader-tipping]] — April and November on-reader guides with the payment flow, configuration, overrides, and dated availability.
- [[source-stripe-terminal-on-receipt-tipping]] — detailed on-receipt guide: overcapture flow, limits, eligible MCCs, fallback options
- [[source-stripe-terminal-collect-card-payment]] — notes on-receipt tip collection at capture time
- [[source-stripe-terminal-tipping-config]] — May 2026 fleet Dashboard and Configuration API settings, plus the November Dashboard/API index
