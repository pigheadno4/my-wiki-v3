---
title: "Stripe — Protect Yourself From Card Testing"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-card-testing-2026.md"
tags: [stripe, card-testing, fraud, carding, captcha, rate-limiting, radar, disputes]
---

## Summary

Card testing (carding/enumeration): using stolen cards to validate them before fraudulent use. Prevention requires a combination of Stripe integration choice and custom controls.

## What It Is

Also known as: carding, account testing, enumeration, card checking.

**Methods**: Card Setup (preferred — doesn't show on cardholder statements) and small Payments.

## 6 Consequences

Disputes/EFWs, higher decline rates (damages issuer reputation), additional fees, infrastructure strain, monitoring program enrollment, data quality degradation.

## Identification Symptoms

- Spike in failed/blocked payments
- Spike in 402 errors / `generic_decline` outcomes
- Suspicious small payments with nonsensical names/emails

## Prevention

### 1. Recommended Stripe Integration (Best)

Payment Element or Checkout: automated CAPTCHA, AI models, rate limiters, dynamic attack suppression → payments marked `Blocked by Stripe`.

**Most impactful risk factors to send**:
1. Advanced fraud detection (highest impact)
2. IP address
3. Customer email
4. Customer name
5. Billing address

### 2. Custom Controls

- **CAPTCHA**: server-side validation; consider visible CAPTCHA for persistent attacks
- **Require login**: reduces anonymous access to payment form
- **Rate limits**: e.g. limit new customers per IP per day; limit cards per account
- **Behavior detection**: limit purchases per product, filter by user agent
- **Radar velocity rules**: custom rules for per-IP/per-account attempt limits (Fraud Teams)

### Key Rules

- Single heuristic (IP-only) is insufficient
- Don't keep retrying cards on fraudulent customers after attack (Smart Retries handles this)
- Keep secret keys safe — leaked keys enable card testing directly

## Related Pages

- [[disputes]] — concept page (updated with card testing note)
- [[stripe-radar]] — Radar velocity rules for card testing
- [[source-stripe-disputes-fraud-types]] — fraud types overview

## Raw Sources

- [[stripe-disputes-card-testing-2026]] — verbatim card testing prevention guide
