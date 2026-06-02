---
title: "Stripe — Card Verification Checks (CVC and AVS)"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-verification-2026.md"
tags: [stripe, cvc, avs, verification, fraud, disputes, card-checks, radar]
---

## Summary

CVC and AVS verification checks: how they work, Radar rules to block failures, and limitations.

## CVC Check

- 3-4 digit number printed on card; only physically present cardholders have access
- Verified during authorization when collected at checkout
- Radar rule can block failures (Dashboard → Radar rules → built-in CVC rule)
- **Does NOT apply to**: wallets (Apple Pay), off-session payments
- **Cannot be stored** by businesses → effective against computer breaches; does NOT protect against physical card theft or compromised websites

## AVS Check (Postal Code + Billing Street Address)

- Verifies postal code + billing street address against card issuer's records
- Radar rule can block failures
- **Can fail for legitimate payments**: incorrect entry, customer moved without notifying issuer
- **Country support**: most US, Canada, UK cards support street address verification; others may not

## Key Rule

Always collect CVC + postal code + billing address — if not collected, card issuer cannot perform verification. Results visible on `Charge.source` and in Dashboard.

## Related Pages

- [[disputes]] — concept page (updated with CVC/AVS check note)
- [[stripe-declines]] — `Charge.outcome` and decline codes
- [[stripe-radar]] — Radar built-in CVC/AVS rules

## Raw Sources

- [[stripe-disputes-verification-2026]] — verbatim card verification checks guide
