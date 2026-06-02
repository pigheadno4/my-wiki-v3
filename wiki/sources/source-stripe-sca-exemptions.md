---
title: "Stripe Docs — Strong Customer Authentication (SCA) exemptions"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-sca-exemptions-2025.md"
tags: [stripe, sca, 3d-secure, exemptions, tra, low-value, mit, data-only, eea, uk, liability-shift]
---

## Summary

Reference for SCA exemptions that Stripe applies automatically (EEA, Switzerland, UK). Covers three exemption types, TRA fraud rate thresholds, and the Data Only authentication flow.

## Key Rule: Exemption → No Liability Shift

When the bank approves an exemption request, liability for fraudulent transactions does NOT shift to the issuer.

## Three Exemption Types

| Exemption | Thresholds |
| --- | --- |
| **Low Value** | < 30 EUR / 25 GBP. Cumulative cap: 100 EUR or 5 transactions since last SCA |
| **TRA / Low Risk** | Fraud rate < 0.13% → 100 EUR; < 0.06% → 250 EUR; < 0.01% → 500 EUR. Current Stripe: EEA ≤ 250 EUR, UK/Swiss ≤ 220 GBP |
| **MIT (off-session)** | Outside SCA scope; no challenge, no liability shift; requires mandate + auth at card save time |

## Data Only Flow

- 3DS2.2+ required; frictionless; **no liability shift** (issuer not contacted)
- Mastercard Identity Check Insights: Adaptive Acceptance / Authorization Boost users only, EEA and UK
- Stripe AI decides when to use Data Only automatically — no action required from business

## Related Pages

- [[stripe-3d-secure]] — 3D Secure concept page (SCA exemptions section)
- [[stripe-authorization-boost]] — Adaptive Acceptance (required for full TRA and Data Only access)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-sca-exemptions-2025]] — verbatim webpage content (44 lines; SCA exemption table reformatted by linter)
