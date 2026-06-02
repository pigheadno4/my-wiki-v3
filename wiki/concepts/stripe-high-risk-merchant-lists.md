---
title: "Stripe — High Risk Merchant Lists (MATCH & VMSS)"
type: concept
category: framework
tags: [stripe, match, vmss, tmf, high-risk, chargebacks, fraud, mastercard, visa, merchant-risk]
---

## Overview

Terminated Merchant File (TMF) databases are maintained by card networks to track accounts closed for high chargebacks or rule violations. All processors must check these databases at onboarding and report terminated merchants who meet criteria. Being listed effectively bars a business from most processors.

The two major lists:
- **MATCH** — Mastercard Alert to Control High-risk Merchants
- **VMSS** — Visa's equivalent TMF database

## MATCH (Mastercard)

### Qualitative Criteria (11 codes)

Breaches of network rules: account data compromise, common point of purchase, laundering, fraud conviction, Mastercard audit program, bankruptcy, standards violation, merchant collusion, PCI DSS non-compliance, illegal transactions, identity theft.

### Quantitative Thresholds (most common, codes 4 & 5)

| Code | Trigger |
| --- | --- |
| 4 — Excessive Chargebacks | >1% of **Mastercard** transactions in a calendar month AND ≥$5,000 in chargebacks |
| 5 — Excessive Fraud | ≥8% fraud-to-sales ratio AND ≥10 fraudulent transactions AND ≥$5,000 in a calendar month |

**Important nuances**:
- Only Mastercard transactions count toward code 4 threshold
- Month = calendar month (not rolling 30 days)
- Qualification is retroactive: qualifying in February requires reporting even if relationship ends in September
- Reversed/won chargebacks still count toward the threshold
- Must report within 1 business day of termination

### MATCH Removal

Only two valid removal reasons:
1. Added in error
2. Code 12 (PCI non-compliance) and business achieved compliance

Records auto-purged after **5 years** by Mastercard.

## VMSS (Visa)

### Qualitative Criteria (13 codes, 23–35)

Similar to MATCH: laundering, illegal transactions, Visa risk compliance, collusion, CPP data compromise, fraud conviction, bankruptcy, agreement violation, Visa rules violation, PCI/PA-DSS noncompliance, data compromise, identity theft, Visa disqualification.

### Quantitative Thresholds (codes 21 & 22)

| Code | Trigger |
| --- | --- |
| 21 — Excessive Fraud | $250,000 fraud amount AND 1.8% fraud-to-sales ratio in a single month |
| 22 — Excessive Disputes | 1,000 dispute count AND 1.8% dispute-to-sales ratio in a single month |

**Note**: VMSS thresholds are much higher than MATCH (volume-based, not ratio-only). Removal only if added in error.

## Stripe's Position

- Cannot process for MATCH/VMSS listed businesses except for identity theft victims
- Cannot remove merchants added for quantitative criteria even after remediation
- Contact Stripe support for dispute assistance

## Sources

- [[source-stripe-disputes-high-risk-lists]] — MATCH and VMSS criteria, removal rules, Stripe policy
