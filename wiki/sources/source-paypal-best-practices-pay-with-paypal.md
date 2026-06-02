---
title: "Best Practices for Pay with PayPal"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-best-practices-pay-with-paypal.md"
tags: [paypal, checkout, best-practices, one-time-payment, recurring-payments, vault, ux]
---

## Best Practices for Pay with PayPal

Official PayPal guide introducing the next-generation Pay with PayPal experience, covering the three supported payment flows and their UX positioning.

Source URL: <https://developer.paypal.com/docs/checkout/standard/best-practices/>

## Key Takeaways

- PayPal frames its checkout experience around **three distinct flows**, each targeting a different merchant use case and UX goal.
- The overarching theme is reducing friction — fewer steps, no manual data entry, faster checkout.

## Supported Payment Flows

| Flow | Tagline | Use cases |
| ---- | ------- | --------- |
| One-time payments | Streamlined one-click checkout | Retail purchases; no manual data entry |
| Recurring payments | Frictionless checkout for recurring payments | Subscriptions, trials, auto-reloads |
| Vaulted payments | Simplified onboarding | Select use cases; listed as "coming soon" |

### One-time Payments

One-click checkout for retail. PayPal positions this as the fastest path for a buyer — no manual entry of card or address details.

See `raw/assets/paypal-best-practices-one-time-one-click.png` — 4-screen mobile flow showing the full one-click checkout journey.

### Recurring Payments

Covers subscriptions, trials, and auto-reloads. Emphasises a "more elegant" experience compared to older PayPal checkout — the Recurring Payments module (billing plan display) is the key differentiator.

See `raw/assets/paypal-best-practices-recurring-subscription.png` — 3-screen mobile flow showing subscription sign-up.

### Vaulted Payments

Onboarding-focused vault flow (save payment method for later). Marked as "coming soon" at time of publication (updated 2025-02-27), so not yet generally available.

See `raw/assets/paypal-best-practices-vault-onboarding.png` — 3-screen mobile flow showing simplified onboarding.

## Images

- `raw/assets/paypal-pay-with-paypal-best-practices-overview.png` — overview showing all three flows side by side
- `raw/assets/paypal-best-practices-one-time-one-click.png` — one-time payment one-click checkout flow (4 screens)
- `raw/assets/paypal-best-practices-recurring-subscription.png` — recurring payment subscription sign-up flow (3 screens)
- `raw/assets/paypal-best-practices-vault-onboarding.png` — vaulted payment onboarding flow (3 screens)

## Raw Sources

- [[paypal-best-practices-pay-with-paypal]] — verbatim source content + downloaded images

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[paypal-vault]] — PayPal Vault / Payment Method Tokens concept
- [[recurring-payments]] — Recurring payments concept
