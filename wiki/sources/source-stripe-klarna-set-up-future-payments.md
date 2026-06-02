---
title: "Stripe: Set Up Future Klarna Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-klarna-set-up-future-payments-2025.md"
tags: [stripe, bnpl, klarna, buy-now-pay-later, subscriptions, setup-intent, recurring, on-demand]
---

## Summary

Guide for saving Klarna and charging customers off-session. Covers subscription setup with `reference` consistency requirement, on-demand metadata for underwriting, upgrade flow, and mandate revocation.

## Key Details

**Save without charging**: Checkout `mode: 'setup'` or SetupIntent API. Must attach to Customer.

**Subscription `reference`**: must use the same string when setting up and all future renewal charges. Mismatch causes error. Pass in `payment_method_options.klarna.subscriptions[].reference`.

**Send subscription details** (`payment_method_options.klarna.subscriptions`) to unlock Pay in 3/4 options and reduce Klarna customer support load.

**Off-session renewals**: `off_session: true`, `confirm: true`, `return_url` required. Include `amount_details.line_items` with subscription reference.

**On-demand metadata**: pass `payment_method_options.klarna.on_demand` with `average_amount`, `minimum_amount`, `maximum_amount`, `interval`, `interval_count` to improve Klarna underwriting.

**Upgrade flow**: re-authorize with same `reference` via PaymentIntent + `setup_future_usage` or new SetupIntent.

**Mandate revocation**: listen for `mandate.updated` webhook → call `detach PaymentMethod`. Also handle customer-initiated detach via your UI.

## Raw Sources

- [[stripe-klarna-set-up-future-payments-2025]] — verbatim webpage content (3751 lines); fixed 34 `_italic_` across 7 term types
