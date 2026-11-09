---
title: "Stripe — Dispute & Fraud Monitoring Programs"
type: concept
category: framework
tags: [stripe, disputes, monitoring, vamp, ecp, ecm, hecm, efm, auspaynet, mastercard, visa, fraud, chargebacks, card-network]
---

## Overview

Card networks operate programs for elevated disputes, fraud, and card testing. Program consequences differ: some schedules escalate monthly fines, VAMP enumeration has no fine in Stripe's guide, VSEFP affects domestic 3DS liability shift without a fine, and MERP has conditional assessments and other possible outcomes. Failure to remediate can put card processing at risk. The May and November Stripe pages are dated general guidance, not a current network-rule or account-status determination.

**Critical rules**:
- Refunds and later dispute outcomes generally do not remove disputes from network monitoring counts; the November guide separately says one can respond after a full pre-dispute refund. The May guide's 10-day removal-request wording is historical and is not established as a current guarantee.
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
| VAMP volume | N/A | N/A outside CEMEA; 75,000 USD in CEMEA |

Excludes: pre-dispute resolved payments, CE 3.0 qualifying TC40s. A transaction in both TC15 and TC40 is counted twice.

November VAMP dashboard: Dashboard → Radar → CBMP → VAMP. Visa's monthly data determines compliance and arrives with a one-month delay; Stripe's daily computations are estimates that can differ. The May test-mode URL and older panel layout are historical.

**Enumeration** (no fines):

| Criteria | Excessive threshold |
| --- | --- |
| Count | 300,000 |
| Ratio to all authorizations | 20% |

### MERP (Visa Merchant Elevated Risk Program)

The November guide says MERP became effective October 2026 for Visa-accepting businesses in Asia Pacific. Visa combines early-life transaction, fraud, non-fraud dispute, authorization, and decline signals; it publishes no individual numeric identification threshold. A confirmed identification can lead to assessments that might be passed through, backdated fraud disputes, remediation, account closure in some circumstances, or possible VMSS listing. These are conditional outcomes, not evidence of this account's identification. See [[source-stripe-disputes-monitoring-programs]].

### VSEFP (US only)

For US-based businesses with US-based custom accounts and excessive fraud on domestic Visa 3DS-authenticated transactions on US-issued cards: both ≥75,000 USD TC40 EFW volume and ≥0.9% EFW USD volume divided by captured Visa 3DS USD volume must be met. The guide says no fines, but domestic 3DS liability shift is lost until the program is fully exited.

## Mastercard Programs

**Calendar and denominator:** Visa VAMP uses same-month captured payments. Mastercard ECP divides current-month chargeback count by the preceding month's captured-payment count; EFM divides current-month fraud chargeback count by the preceding month's e-commerce transaction count. These denominators are not interchangeable.

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
- Fraud chargebacks (codes 4837/4863) >50,000 USD volume and >0.50% count rate, or >15,000 USD and >0.20% in Australia; the rate uses current-month fraud chargeback count over prior-month e-commerce transactions
- 3DS Mastercard payment count ≤10% of total Mastercard payments in non-regulated countries, or ≤50% in regulated countries

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

- [[source-stripe-disputes-monitoring-programs]] — May and November 2026 general guide to VAMP, Asia Pacific MERP, US VSEFP, Mastercard and AusPayNet thresholds, conditional consequences, dashboard data authority, and prevention practices
- [[source-stripe-disputes-measuring]] — dispute activity vs rate metric definitions
