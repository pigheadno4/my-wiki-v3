---
title: "Stripe Authorization Boost"
type: concept
category: technology
tags: [stripe, authorization-boost, adaptive-acceptance, card-account-updater, network-tokens, ic-plus, payment-optimization, cnp]
---

## Definition

Authorization Boost is Stripe's suite of AI-driven features that improve card-not-present (CNP) payment success rates and, for IC+ pricing customers, reduce network costs. Accessible via Dashboard → Optimization page.

> Stripe doesn't guarantee outcomes. Calculations are probabilistic estimates.

## Three Features

### Adaptive Acceptance

AI reformats payment requests based on card issuers' preferences. Applied before sending OR after a decline.

**Recovery mechanisms**:

- Retry declined payments in real time (false decline recovery)
- PINless network retries (US): retry on US debit network after Visa/Mastercard decline

**Cost savings (IC+ only)**:

- **Excessive retry prevention**: blocks payments that would incur network retry penalties and likely fail
- **Decline prevention**: blocks payments unlikely to succeed, avoiding scheme fees
- **Data Only 3DS**: shares transaction data with issuers via Data Only flows — reduces scheme fees without cardholder friction

### Card Account Updater

Automatically retrieves updated card information (PAN/expiry changes) from card network services before a payment attempt.

**Recovery only** — no cost savings. Particularly valuable for recurring charges with saved cards.

### Network Tokens

Substitutes raw card numbers with network-issued tokens. Tokens stay current even when underlying card data changes.

**Recovery**: higher approval rates with always-current credentials.

**Cost savings (IC+ only)**:

- **Interchange savings**: Visa discounts on consumer CNP payments in some markets (MCC-dependent)
- **Scheme fee savings**: prevents Mastercard Credential Continuity Program (CCP) fees for outdated credentials

## How Stripe Calculates Impact

**Probabilistic attribution**: Stripe estimates the likelihood each optimization caused the success (e.g., 20% chance). Recovered volume = payments × amount × probability. Multi-feature payments attributed to the most likely responsible feature.

**Example**: 100 payments × $50 × 20% likelihood = $1,000 recovered volume.

**Cost savings**: Stripe infers costs without optimization vs. with optimization using network fee rules. Note: not reconciled directly with your account fees. Visa VDCU fees for network token use may offset savings.

## Dashboard Features

- Date range + aggregation filters (weekly/monthly)
- Per-feature breakdown: recovered volume, recovered payments, success rate increase, cost savings
- "Show summary" toggle for aggregate view
- Download with per-payment detail + likelihood estimates
- Cost savings shown only if ≥ $100 USD equivalent in last 12 months (IC+ only)
- Success rate chart: raw rate (not deduplicated), blue dotted line = estimated rate without optimizations

## A/B Test Before Buying

Run a **30-day A/B test** (free; only billed for already-enabled features) to measure impact before purchasing.

- **50/50 split**: Control = current config + CAU; Treatment = current config + all non-enabled Authorization Boost features
- **CAU exception**: runs on both groups (100% coverage) — cannot be applied selectively
- **Cancel**: Admin/Developer roles; reverts to prior config; **12-month cooldown** before re-testing
- **Results**: available 37 days after start (30 test + 7 for retries); p < 5% significance threshold
- **Authorization Boost is paid**: purchase via "Enable Authorization Boost" on results page

## Stripe Recommendations (General)

Stripe surfaces up to 3 recommendations at a time on the Acceptance page, updated daily. Each includes an estimated annual revenue impact (recent month × avg increase × 12). Not professional advice.

**Five recommendation types**:

1. **NTID for MIT payments**: supply network transaction ID from prior on-session transaction to reduce 3DS triggers on off-session payments
2. **Share postal codes for Visa credit**: enables AVS → more favorable interchange rates in US
3. **Remove blunt AVS/CVC Radar rules**: replace `Block if CVC verification fails` + `Block if postal code verification fails` with risk-score variants
4. **Reduce 3DS on low-risk transactions**: unnecessary 3DS hurts success rates outside SCA regions; use Radar Authentication control for automatic targeting
5. **Fix 3DS integration**: high abandonment rate signals an integration issue

## Sources

- [[source-stripe-payments-optimization]] — primary: Authorization Boost features, probabilistic calculation methodology, IC+ cost savings, dashboard features
- [[source-stripe-authorization-boost-ab-test]] — A/B test guide: 30-day test design, CAU exception, cancel/cooldown rules, 37-day results, impact formula
- [[source-stripe-payments-recommendations]] — General recommendations: NTID, AVS/Visa, Radar rule swap, 3DS reduction, 3DS integration check
