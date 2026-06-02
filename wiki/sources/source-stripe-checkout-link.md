---
title: "Stripe Docs — Link with Checkout"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-checkout-link-2025.md"
tags: [stripe, link, checkout, dynamic-payment-methods, setup-intents, connect, otp]
---

## Summary

Integration guide for using Link with Stripe Checkout. Covers dynamic vs manual PM listing, OTP test codes, Connect behavior, and how to disable Link per payment method configuration.

## Key Facts

- **No additional fees** — same pricing as card payments
- **PM type on payment**: `payment_method.type = 'link'`
- **Domain registration required** — see [[source-stripe-pmd-registration]]

## Integration Options

### Dynamic payment methods (recommended)
1. Enable Link in Dashboard payment method settings
2. Remove `payment_method_types` from Checkout session code

> Exception: if using Setup Intents to save cards for future use, must list payment methods manually instead.

### Manual listing
- `payment_method_types: ['card', 'link']` — `card` must be included alongside `link`

## OTP Test Codes (Sandbox)

| Code | Outcome |
| --- | --- |
| Any 6 digits (not below) | Success |
| `000001` | Error: code invalid |
| `000002` | Error: code expired |
| `000003` | Error: max attempts exceeded |

> Sandbox Link accounts are publicly accessible (tied to publishable key) — don't store real user data.

## Connect

Link automatically available to connected accounts using Checkout via a Connect platform. Platform manages Link in its own Dashboard Link settings; connected accounts manage their own separately.

## Disable

Disable per payment method configuration in Dashboard (not globally). Takes a few minutes to propagate.

## CDN Assets

- `raw/assets/stripe-link-in-checkout.png` — Link in Checkout UI (599 KB)
- `raw/assets/stripe-link-enable-dashboard.png` — Link enabled in Dashboard (196 KB)

## Related Pages

- [[stripe-link]] — Link concept page (Checkout integration section)
- [[source-stripe-link]] — broader Link overview
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-checkout-link-2025]] — verbatim webpage content (128 lines)
