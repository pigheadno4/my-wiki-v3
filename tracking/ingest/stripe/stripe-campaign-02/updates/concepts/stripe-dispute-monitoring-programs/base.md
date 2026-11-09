---
title: "Stripe — Dispute & Fraud Monitoring Programs"
type: concept
category: framework
tags: [stripe, disputes, monitoring, vamp, ecp, ecm, hecm, efm, auspaynet, mastercard, visa, fraud, chargebacks, card-network]
---

## Overview

Card networks operate monitoring programs that track businesses with excessive disputes or fraud. Being placed in a program triggers monthly fines that escalate until levels are sustained below thresholds. Failure to exit can result in the network refusing to process your payments.

**Critical rules**:
- Refunds and dispute outcomes are ignored — only whether a dispute occurred matters
- Disputes Stripe handles silently (no Dashboard entry) **still count** for network monitoring
- Unescalated inquiries, EFWs, and RDR movements don't count as disputes

## Visa Programs

### VAMP (Visa Acquirer Monitoring Program)

Two separate tracks — disputes+fraud and enumeration.

**Disputes and fraud** (calculated monthly, prior month data):

| Criteria | Non-compliant | Excessive |
| --- | --- | --- |
| VAMP count (TC15 disputes + TC40 EFWs) | 5 | 1,500 (150 CEMEA) |
| VAMP ratio | 0.5% | 1.5% (2.2% CEMEA) |

Excludes: pre-dispute resolved payments, CE 3.0 qualifying TC40s. A transaction in both TC15 and TC40 is counted twice.

View estimates: Dashboard → Radar → CBMP → VAMP.

**Enumeration** (no fines):

| Criteria | Excessive threshold |
| --- | --- |
| Count | 300,000 |
| Ratio to all authorizations | 20% |

### VSEFP (US only)

For excessive fraud on domestic Visa 3DS transactions: ≥$75k fraud volume AND ≥0.9% fraud rate → liability shift lost (no cash fines).

## Mastercard Programs

**Key difference from Visa**: Mastercard denominator = prior month's payments (not current month).

### ECM / HECM: Excessive Chargeback Programs

| Level | Count | Rate | Fine (escalating monthly) |
| --- | --- | --- | --- |
| ECM | 100–299 | 1.5–2.99% | $0 → $1k → $5k → $25k → $50k → $100k |
| HECM | 300+ | ≥3% | $0 → $1k → $2k → $10k → $50k → $100k → $200k |

Issuer recovery assessment: +$5/chargeback over 300 (for ECM months 4+, HECM months 4+).
Exit: 3 consecutive months below threshold.

### EFM: Excessive Fraud Merchant

All conditions must be met simultaneously:
- ≥1,000 e-commerce Mastercard payments
- Fraud chargebacks (codes 4837/4863) >$50k volume + >0.5% rate
- 3DS rate ≤10% of Mastercard payments (non-regulated)

Fine schedule: $0 → $500 → $1k → $5k → $25k → $50k → $100k.

If exceeding both EFM and ECP: placed in EFM only (but both tracked).

## AusPayNet FMP (Australia Only)

Quarterly. CNP fraud only (excludes card-present and 3DS).

Triggers: >50k AUD fraud AND ≥0.2% fraud-to-sales ratio.

Escalation: fraud controls → risk-based SCA → full SCA on all CNP → off-boarding.
Exit: below threshold for 1 quarter.

## Prevention Priorities

1. Authorize then capture — reverse suspicious auths before capture (no fraud report obligation pre-capture)
2. Easy subscription cancellation + billing reminders
3. Tracking numbers + signature on delivery for high-value
4. Third-party alert services (Ethoca, Verifi) for pre-chargeback intervention
5. Collect maximum evidence at checkout for friendly fraud defense

## Sources

- [[source-stripe-disputes-monitoring-programs]] — full program thresholds, fine schedules, prevention best practices
- [[source-stripe-disputes-measuring]] — dispute activity vs rate metric definitions
