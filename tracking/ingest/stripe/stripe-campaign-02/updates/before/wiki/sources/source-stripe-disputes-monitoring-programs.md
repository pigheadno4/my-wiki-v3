---
title: "Stripe — Dispute and Fraud Card Monitoring Programs"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-monitoring-programs-2026.md"
tags: [stripe, disputes, monitoring, vamp, ecp, ecm, hecm, efm, auspaynet, mastercard, visa, fraud, chargebacks]
---

## Summary

Comprehensive reference for Visa (VAMP, VSEFP), Mastercard (ECM/HECM/EFM), and AusPayNet (FMP) card network monitoring programs: thresholds, fine schedules, calculation methods, and prevention best practices.

## Key Principles

- **Refunds don't help**: monitoring programs ignore refunds and dispute outcomes — only whether a dispute occurred
- **Stripe-handled disputes still count**: some disputes Stripe handles silently (refunded before dispute, duplicates, network error) don't appear in your Dashboard but **are included in network monitoring calculations**
- **Unescalated inquiries, EFWs, and RDR movements don't count** as disputes for monitoring
- **Calendar difference**: Visa uses same-month payments; Mastercard uses prior-month payments as denominator

## Visa Programs

### VAMP (Visa Acquirer Monitoring Program)

Two separate monitoring tracks: disputes+fraud, and enumeration.

**Disputes and fraud thresholds** (previous month's data):

| Criteria | Non-compliant | Excessive (non-CEMEA) | Excessive (CEMEA) |
| --- | --- | --- | --- |
| VAMP count | 5 | 1,500 | 150 |
| VAMP ratio | 0.5% | 1.5% | 2.2% |
| VAMP volume | N/A | N/A | 75,000 USD |

VAMP count = TC15 disputes + TC40 EFWs. Excludes: pre-dispute resolved payments (e.g. Stripe dispute prevention), CE 3.0 qualifying TC40s. Same transaction can appear in both TC40 and TC15 → counted twice.

**Enumeration thresholds** (no fines, just monitoring):

| Criteria | Threshold |
| --- | --- |
| VAMP enumeration count | 300,000 |
| VAMP enumeration ratio | 20% |

View estimated VAMP metrics at: Dashboard → Radar → CBMP → VAMP.

### VSEFP (Visa Secure Excessive Fraud Program — US only)

Applies to US businesses with excessive fraud on domestic Visa 3DS-authenticated transactions.

| Fraud volume | Fraud rate | Consequence |
| --- | --- | --- |
| ≥75,000 USD | ≥0.9% | No fines, but liability shift lost on domestic 3DS until fully exited |

## Mastercard Programs

### Rate Calculation Difference

Mastercard uses **prior month's captured payments** as denominator (not current month like Visa).

### ECM: Excessive Chargeback Merchant

| Dispute Count | Rate | Fine schedule |
| --- | --- | --- |
| 100–299 | 1.5–2.99% | Month 1: $0; months 2–3: $1k; months 4–6: $5k + issuer recovery; months 7–11: $25k; months 12–18: $50k; 19+: $100k |

Issuer recovery assessment: +$5 per chargeback over 300.

### HECM: High Excessive Chargeback Merchant

| Dispute Count | Rate | Fine schedule |
| --- | --- | --- |
| 300+ | ≥3% | Month 1: $0; month 2: $1k; month 3: $2k; months 4–6: $10k; months 7–11: $50k; months 12–18: $100k; 19+: $200k |

Exit condition: below threshold for 3 consecutive months. If below HECM but still in ECM → moves to ECM level.

### EFM: Excessive Fraud Merchant Compliance Program

Applies when ALL conditions met:
- ≥1,000 e-commerce Mastercard payments
- Net fraud volume >$50k (>$15k Australia) — fraud reason codes 4837 or 4863
- Fraud chargeback rate >0.5% (>0.2% Australia)
- 3DS rate ≤10% of Mastercard payments (non-regulated) or ≤50% (regulated)

Fine schedule: Month 1: $0; month 2: $500; month 3: $1k; months 4–6: $5k; months 7–11: $25k; months 12–18: $50k; 19+: $100k.

Note: If exceeding both EFM and ECP, placed in EFM only (but both tracked separately).

## AusPayNet FMP (Australia Only)

Quarterly tracking. CNP fraud only (excludes card-present and 3DS transactions).

Triggers: Fraud amount >50k AUD AND fraud-to-sales ratio ≥0.2%.

| Quarter above threshold | Consequence |
| --- | --- |
| 1 | Implement fraud controls |
| 2 | Risk-based SCA or SCA on all CNP |
| 3 | SCA on all CNP (or off-boarding risk) |
| 4+ | May be off-boarded |

Exit: below threshold for 1 quarter. SCA exemptions: recurring (after first), trusted customer, wallet transactions.

## Prevention Best Practices

- **Subscriptions**: easy cancellation, billing reminders (7 days before annual), flexible refunds, third-party alerts (Ethoca, Verifi)
- **Unreceived products**: tracking numbers, signature on delivery for high-value, communicate delays
- **Unacceptable products**: accurate descriptions, flexible refunds, reevaluate high-dispute products
- **Friendly fraud**: collect maximum evidence at checkout, verify addresses, agree-to-terms checkboxes
- **Auth vs capture**: reverse suspicious authorizations before capture to avoid fraud reporting obligation

## Related Pages

- [[stripe-dispute-monitoring-programs]] — concept page
- [[stripe-high-risk-merchant-lists]] — MATCH/VMSS (consequence of excessive disputes)
- [[source-stripe-disputes-measuring]] — dispute activity vs rate metrics
- [[disputes]] — dispute handling

## Raw Sources

- [[stripe-disputes-monitoring-programs-2026]] — verbatim monitoring programs reference (325 lines)
