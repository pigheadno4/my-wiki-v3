---
title: "Stripe: Accept a UPI Payment"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-upi-accept-payment-2025.md"
tags: [stripe, real-time-payments, upi, india, inr, checkout, elements, direct-api, recurring, e-mandate]
---

## Summary

Integration guide for UPI via Checkout, Checkout Sessions API, Payment Intents API, and Direct API — the broadest path coverage of any real-time method reviewed. Checkout supports setup and subscription modes. QR expires in 5 minutes. Off-session/recurring notifications are delayed.

## Key Details

**Four integration paths**: Checkout, Checkout Sessions API (Elements), Payment Intents API (Elements), Direct API.

**Checkout**: `payment_method_types: ['upi']`, INR only. Setup mode and Subscription mode both supported (e-mandate). QR code expires after **5 minutes** — `payment_intent.payment_failed` sent on expiry.

**Off-session/recurring**: notification is **delayed** (unlike one-time payments which are immediate).

**Checkout Sessions API**: uses newer `initCheckoutElementsSdk` / `CheckoutElementsProvider` SDK approach (separate from standard PaymentIntents Elements flow).

**Payment Intents API**: standard `stripe.confirmPayment` with `return_url`.

**Test**: QR code → scan → Stripe-hosted UPI test page → authorize or expire.

## Raw Sources

- [[stripe-upi-accept-payment-2025]] — verbatim webpage content (1,081 lines); fixed `*prices*` ×1, `*subscriptions*` ×1, `*client secret*` ×1
