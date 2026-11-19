---
title: "Stripe Docs — Recommendations"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-payments-recommendations-2025.md"
tags: [stripe, recommendations, authorization-rates, ntid, avs, radar, 3d-secure, payment-optimization]
---

## Summary

Reference for Stripe's Payments Recommendations — up to 3 actionable suggestions shown on the Acceptance Dashboard page, updated daily. Each includes an estimated annual revenue impact.

## Key Facts

- **Up to 3 recommendations** at a time; updated daily; dismissible
- **Impact estimation**: recent month × avg increase × 12 (annualized); based on other businesses that took the same action
- **Two estimation bases**: all payment volume, OR relevant volume only (excludes inapplicable payments)
- **Disclaimer**: estimates not guaranteed; may have tradeoffs (costs, fraud risk, legal terms)

## Five Recommendation Types

| Recommendation | What to do | Why |
| --- | --- | --- |
| Network transaction IDs | Supply NTID from prior on-session transaction on MIT/off-session payments | Reduces 3DS triggers, improves auth rates |
| Share postal codes for Visa credit | Collect and share billing postal code | Enables AVS → favorable interchange in US |
| Remove blunt AVS/CVC Radar rules | Disable `Block if CVC verification fails` + `Block if postal code verification fails` | Blocks legitimate payments; use risk-score variants instead |
| Reduce 3DS on low-risk | Stop requesting 3DS for low-risk outside SCA regions | 3DS hurts success rates with minimal fraud benefit |
| Fix 3DS integration | Debug 3DS flow | High abandonment rate signals integration issue |

## Notes

- Radar rule swap: replace blanket rules with `Block if CVC verification fails based on risk score` and `Block if postal code verification fails based on risk score`; the `Block if :risk_level: = 'highest'` rule always applies regardless
- Disabling 3DS does NOT affect SCA-required regions (Europe) or Credit Card Security Guidelines (Japan)

## Related Pages

- [[stripe-authorization-boost]] — payments optimization concept page (includes this content)
- [[source-stripe-payments-optimization]] — Authorization Boost features
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-payments-recommendations-2025]] — verbatim webpage content (90 lines; impact estimation table reformatted by linter)
