---
title: "Stripe Terminal: Collect On-Reader Tips"
type: source
date_ingested: 2026-04-27
original_format: webpage
raw_files:
  - "stripe-terminal-on-reader-tipping-2025.md"
tags: [stripe, stripe-terminal, tipping, on-reader, in-person-payments, payment-intents, configuration]
---

## Summary

Detailed integration guide for on-reader tipping in Stripe Terminal. Covers configuration options (smart tips, percentages, fixed amounts), the payment collection flow, per-transaction overrides (skip tipping, tip-eligible amounts), and multi-currency constraints.

## Key Takeaways

- **Configuration**: Set up via `Configuration` API object or Dashboard. Three modes:
  - **Smart tips**: dynamically shows percentages or fixed amounts based on a `smart_tip_threshold`; if pre-tip amount is below threshold, show fixed amounts; at or above, show percentages
  - **Percentages**: three percentage-based suggestions (post-tax by default, can override with tip-eligible amount)
  - **Fixed amounts**: three fixed tip amounts in currency's smallest unit
- **Multi-currency constraint**: if specifying multiple currencies in a `Configuration`, must use the same config keys for each — can't mix `percentages`-only USD with `fixed_amounts` EUR
- **Config propagation**: WisePad 3 receives updates on SDK connection; WisePOS E takes up to 5 minutes
- **WisePad 3 SDK minimums**: Android SDK 2.8.1+, iOS SDK 2.16.1+

## Tip Amount Lifecycle

- **Pre-confirmation**: tip amount in `amount_tip` field; not yet in `amount`
- **Post-confirmation**: `amount_tip` resets to zero; `amount` includes tip; tip in `amount_details.tip.amount`

| Scenario | `amount_details.tip.amount` |
| --- | --- |
| On-reader tipping disabled | `null` |
| Enabled, no tip selected | `0` |
| Enabled, tip selected | The selected amount |

## When the Tip Screen Is Skipped

1. `Configuration` object is missing a tipping configuration
2. `skipTipping` is enabled in tipping configuration
3. Reader is in an unsupported country
4. Tipping config can't be applied to payment currency (e.g., payment in EUR but config only specifies USD)

## Per-Transaction Overrides

**Skip tipping** (`skip_tipping: true` / `skipTipping: true`): hides the tip selection screen for a specific transaction — useful when mixing on-reader and on-receipt tipping (e.g., takeout vs dine-in). Available in server-driven, JS, iOS, Android, React Native SDKs.

**Tip-eligible amount** (`amount_eligible` server-driven / `eligible_amount` JS / `setEligibleAmount` iOS+Android / `tipEligibleAmount` React Native): sets a separate amount used as the base for percentage tip calculations. Shown to customer alongside pre-tip amount. Use case: salon that sells haircuts + shampoo but only wants tips calculated on the haircut portion.

- `eligible_amount: 0` → tipping is skipped regardless of `skip_tipping`
- `eligible_amount` equal to PaymentIntent amount → ignored, tip calculated on full amount
- Setting `eligible_amount > 0` with `skip_tipping: true` → error

## Country Availability (38 countries for S700/S710 + WisePOS E)

AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, HR, HU, IE, IT, JP, LI, LT, LU, LV, MT, MY, NL, NO, NZ, PL, PT, RO, SE, SG, SI, SK, US

WisePad 3 is a subset: AU, CA, FR, DE, IE, NL, NZ, SG, GB (per overview source).

## See Also

- [[stripe-terminal-tipping]] — concept page covering both on-reader and on-receipt methods
- [[source-stripe-terminal-collect-tips]] — overview comparing on-reader vs on-receipt

## Raw Sources

- [[stripe-terminal-on-reader-tipping-2025]] — verbatim webpage content with screenshots
