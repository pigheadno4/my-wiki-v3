---
title: "Stripe Terminal: Tipping"
type: concept
category: technology
tags: [stripe, stripe-terminal, tipping, in-person-payments, payment-intents]
---

## Definition

Stripe Terminal supports two voluntary tip collection methods — on-reader and on-receipt — both built on the PaymentIntents API with manual capture. Mandatory tips (fixed amounts) must be included in the original `PaymentIntent` amount; neither voluntary method applies.

## On-reader Tipping

The card reader displays suggested tip options to the customer before payment is collected. The customer selects a tip (or custom amount, or no tip) on the reader screen; the reader automatically adds it to the payment amount.

**Supported readers**: BBPOS WisePad 3, BBPOS WisePOS E, Stripe Reader S700/S710  
**Country availability**: 38 countries for S700/S710 + WisePOS E (AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, HR, HU, IE, IT, JP, LI, LT, LU, LV, MT, MY, NL, NO, NZ, PL, PT, RO, SE, SG, SI, SK, US); WisePad 3 subset: AU, CA, FR, DE, IE, NL, NZ, SG, GB  
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

**Skip tipping** (`skip_tipping`/`skipTipping`): hides tip screen for a single transaction. Useful for mixing on-reader (takeout) and on-receipt (dine-in) in the same business. Available across all SDKs.

**Tip-eligible amount**: overrides the base amount used for percentage calculations — shown to customer alongside pre-tip total. Use case: salon calculating tips on services only, not retail products sold.

- `eligible_amount: 0` → skips tipping regardless of `skip_tipping`
- `eligible_amount` = PaymentIntent amount → ignored
- `eligible_amount > 0` with `skip_tipping: true` → error

**SDK field names**: `amount_eligible` (server-driven), `eligible_amount` (JS), `setEligibleAmount()` (iOS/Android), `tipEligibleAmount` (React Native)

**SDK support**: WisePad 3 via Android/iOS/React Native SDKs; WisePOS E + S700/S710 via all SDKs (server-driven)

## On-receipt Tipping

Tips are collected after authorization via **overcapture** — capturing more than the originally authorized amount. Common in table-service restaurants where staff record tip from a printed receipt. No new authorization is triggered; the customer sees the full amount only at settlement.

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

## Constraints

- **One method per PaymentIntent**: once on-reader tipping is applied to a `PaymentIntent`, on-receipt tipping cannot be used on the same `PaymentIntent`
- **Both require manual capture**: neither method works with automatic capture
- **On-reader tipping limit**: maximum charge amount for the currency (8–9 digits depending on currency), inclusive of tip
- **On-receipt overcapture limit**: 50% of authorized amount or 50 USD, whichever is greater

## Fleet Configuration

On-reader tip options are configured at the fleet level via the Configuration object (same account→location hierarchy). Set `tipping: { usd: { percentages, fixed_amounts, smart_tip_threshold } }` per currency. Propagation: 10 minutes. See [[source-stripe-terminal-tipping-config]].

## Sources

- [[source-stripe-terminal-collect-tips]] — overview: method comparison, country availability, API behavior tables
- [[source-stripe-terminal-on-reader-tipping]] — detailed on-reader guide: Configuration API (smart/pct/fixed), tip lifecycle, skip tipping, tip-eligible amounts, multi-currency constraints
- [[source-stripe-terminal-on-receipt-tipping]] — detailed on-receipt guide: overcapture flow, limits, eligible MCCs, fallback options
- [[source-stripe-terminal-collect-card-payment]] — notes on-receipt tip collection at capture time
- [[source-stripe-terminal-tipping-config]] — fleet configuration: tipping options via Configuration object, smart_tip_threshold, 10-min propagation
