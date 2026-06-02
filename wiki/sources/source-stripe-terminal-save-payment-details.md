---
title: "Stripe Terminal: Collect and Save Payment Details for Future Use"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-save-payment-details-2025.md"
tags: [stripe, stripe-terminal, saved-payment-methods, generated-card, off-session, card-fingerprint, compliance, recurring-payments]
---

## Summary

Overview of how Stripe Terminal can collect and save payment methods for future online reuse. Covers the `generated_card` mechanism, off-session charging, card fingerprints for customer recognition, and compliance requirements.

## Key Takeaways

- **Can't save card-present directly**: PaymentIntent or SetupIntent with card-present can't save the PaymentMethod directly — Stripe instead creates a `generated_card` PaymentMethod representing the same card
- **Must attach to Customer/Account**: `generated_card` must be attached to a `Customer` (v1) or customer-configured `Account` (v2) to be reusable; attaching only to a PaymentIntent without a Customer/Account makes it non-reusable
- **Two save flows**: save directly (without charging) or save after payment — see sub-pages
- **Off-session charging**: set `off_session: true` when charging outside checkout flow; Terminal SDK methods can't process `generated_card` payments (they're online payments)
- **Card fingerprints**: `card_present` PaymentMethods have the same `fingerprint` attribute as `card` — use to correlate in-person and online transactions by the same card. Mobile wallet fingerprints differ from the underlying card's online fingerprint
- **Connect**: since API v2018-01-23, Connect platforms see uniform fingerprints across connected accounts

## Compliance Requirements

When saving payment details, merchants must:

1. Add checkout terms stating how payment method details will be saved and allow opt-in
2. If charging off-session, terms must cover:
   - Customer's agreement to payment initiation on their behalf
   - Timing and frequency of payments (installment, subscription, or unscheduled)
   - How the payment amount is determined
   - Cancellation policy (for subscriptions)
3. Keep a written record of customer agreement
4. Only use saved payment method for the specific purpose stated in terms
5. If combining off-session charging AND saving for future checkout presentation, must explicitly collect consent (e.g., "Save my payment method for future use" checkbox)

## See Also

- [[stripe-terminal-save-payment-details]] — concept page
- [[stripe-terminal]] — full Stripe Terminal concept page
- [[stripe-saved-payment-methods]] — online saved payment methods (non-Terminal)

## Raw Sources

- [[stripe-terminal-save-payment-details-2025]] — verbatim webpage content
