---
title: "Stripe Terminal: Collect On-Receipt Tips"
type: source
date_ingested: 2026-04-27
original_format: webpage
raw_files:
  - "stripe-terminal-on-receipt-tipping-2025.md"
tags: [stripe, stripe-terminal, tipping, on-receipt, overcapture, in-person-payments, payment-intents]
---

## Summary

Detailed integration guide for on-receipt tipping in Stripe Terminal (US only). Tips are collected via overcapture — capturing more than the authorized amount at settlement. Covers the API flow, overcapture limits, and eligible merchant categories.

## Key Takeaways

- **Mechanism**: On-receipt tipping works via **overcapture** — capturing a `amount_to_capture` greater than the original authorized amount. No additional authorization is triggered; the customer sees the full amount only at settlement.
- **Eligibility check**: Before capturing, expand `latest_charge` on the PaymentIntent and inspect `overcapture_supported` on the Charge object to confirm eligibility.
- **Overcapture limits**: Up to 50% of the authorized `amount`, or 50 USD, whichever is greater.
  - Example: $40 authorized → can capture up to $90 (50 USD floor applies)
  - Example: $100 authorized → can capture up to $150 (50% rule applies)
- **When limits are exceeded**, two options:
  1. Use [incremental authorization](https://docs.stripe.com/terminal/features/incremental-authorizations.md) to raise the PaymentIntent `amount` (MCC-dependent)
  2. Create a new PaymentIntent using the `generated_card` payment method from the original PaymentIntent to capture the tip separately

## Eligible MCCs

On-receipt tipping (overcapture) is available to US businesses with the following merchant category codes:

- Taxicabs and limousines
- Eating places and restaurants
- Drinking places (alcoholic beverages)
- Fast food restaurants
- Beauty and barber shops
- Health and beauty spas

Card brands: Visa, Mastercard, Discover, American Express only. Contact [Stripe support](https://support.stripe.com/contact) to verify MCC eligibility. Connect platforms should [set MCCs](https://docs.stripe.com/connect/setting-mcc.md) for connected accounts to match their business type.

## API Flow

1. Create and confirm a PaymentIntent with `capture_method: manual`
2. Retrieve the PaymentIntent with `expand: ['latest_charge']`; check `latest_charge.overcapture_supported`
3. Capture with `amount_to_capture` set to the authorized amount + tip
4. The PaymentIntent `amount` updates to the new total; `amount_authorized` on the Charge retains the original pre-tip value

## See Also

- [[stripe-terminal-tipping]] — concept page covering both on-reader and on-receipt methods
- [[source-stripe-terminal-collect-tips]] — overview source comparing on-reader vs on-receipt

## Raw Sources

- [[stripe-terminal-on-receipt-tipping-2025]] — verbatim webpage content
