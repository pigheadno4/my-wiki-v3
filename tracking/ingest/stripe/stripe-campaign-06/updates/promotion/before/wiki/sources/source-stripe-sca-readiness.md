---
title: "Stripe Docs — Strong Customer Authentication readiness"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-sca-readiness-2025.md"
tags: [stripe, sca, psd2, 3d-secure, payment-intents, setup-intents, off-session, grandfathering, mit, eea]
---

## Summary

SCA compliance guide covering business impact assessment, SCA-ready product recommendations, grandfathering rules, off-session readiness checklist, and MIT mandate requirements.

## Who Needs SCA

All three conditions: EEA-based business + EEA customers + card payments. **Charges API is NOT SCA-ready.**

## SCA-Ready Products

- Payment Intents API (one-time + save)
- Setup Intents API (save without payment)
- Stripe Checkout (handles SCA automatically)
- Stripe Billing (subscriptions/invoicing)

## Grandfathering (Previous Authorization Agreements)

| Region | Cutoff date |
| --- | --- |
| EU customers | Dec 31, 2020 |
| UK customers | Sep 14, 2021 |

Stripe checks automatically. Bank can still decline → `requires_payment_method` → customer must complete payment again.

## Off-Session Readiness Checklist

1. Authenticate card at save time (on-session)
2. When saving during payment: `setup_future_usage: 'off_session'`
3. When saving without payment: SetupIntent with `usage: 'off_session'`
4. When charging off-session: `off_session: true` on PaymentIntent

## MIT Mandate Requirements

Customer must authorize (in writing on checkout):
- Permission to initiate payments on their behalf
- Anticipated frequency (one-time or recurring)
- How payment amount is determined

## Key Rules

- Liability shift does NOT apply when bank uses exemption (payment not authenticated via 3DS)
- `incomplete`/`requires_action` status: verify next actions are handled; set `off_session: true`
- For plugins: use `setAppInfo`; notify Stripe + customers when SCA-ready

## Related Pages

- [[stripe-3d-secure]] — 3D Secure concept page (SCA Readiness section)
- [[source-stripe-sca-exemptions]] — SCA exemption types and thresholds
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-sca-readiness-2025]] — verbatim webpage content (175 lines)
