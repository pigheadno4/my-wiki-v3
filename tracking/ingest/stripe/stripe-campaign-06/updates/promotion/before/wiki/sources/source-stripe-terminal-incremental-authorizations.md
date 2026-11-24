---
title: "Stripe Terminal: Incremental Authorizations"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-incremental-authorizations-2025.md"
tags: [stripe, stripe-terminal, incremental-authorization, payment-intents, card-present]
---

## Summary

Guide for increasing the authorized amount on a confirmed Terminal PaymentIntent before capture. Covers eligibility by card network and MCC, the setup flow, and how to perform and capture incremental authorizations.

## Key Takeaways

- **Purpose**: increase the `amount` on a confirmed PaymentIntent before capture — useful when the total changes after initial authorization (e.g., customer adds items, tip adjustment)
- **Restrictions**:
  - Visa, Mastercard, Amex: all merchant categories
  - Discover: restricted MCCs (transportation, hospitality, food service, car rental, recreation — see source for full list)
  - Online only (POS and reader must be fully online)
  - Maximum 10 attempts per payment (including declines)
- **Cardholder experience**: depending on issuing bank, may see authorization increase in place OR each increment as a separate pending authorization; after capture, appears as one entry

## Setup

Create PaymentIntent with:
- `request_incremental_authorization_support: true` in `payment_method_options.card_present`
- `capture_method: 'manual'`

UI change: reader shows `Pre-authorization` instead of `Total` on the payment screen.

## Check Eligibility After Confirmation

After confirming the PaymentIntent, check `incremental_authorization_supported` on the latest charge. Not all PaymentIntents are eligible even if the feature was requested — eligibility depends on the card network and MCC at transaction time.

## Perform Incremental Authorization

Call `stripe.paymentIntents.incrementAuthorization('{{PAYMENT_INTENT_ID}}', { amount: <new_total> })` — pass the new **total** amount (not the increment). Stripe authorizes the **difference** between the old and new amounts.

Outcomes:
- **Success**: PaymentIntent updated with the new amount
- **Failure**: `card_declined` error; PaymentIntent remains authorized for original amount; other field updates (e.g., `application_fee_amount`) are not saved

## Capture with Auto-Increment

Capture with `amount_to_capture` higher than the currently authorized amount → Stripe attempts an automatic incremental authorization. **Exception**: if eligible for on-receipt tipping (overcapture), this auto-increment does NOT trigger — capture always succeeds regardless.

Outcomes same as manual increment: success returns captured PaymentIntent, failure returns `card_declined`.

## See Also

- [[stripe-terminal-incremental-authorizations]] — concept page
- [[stripe-terminal-tipping]] — on-receipt tipping uses overcapture instead of incremental auth

## Raw Sources

- [[stripe-terminal-incremental-authorizations-2025]] — verbatim webpage content
