---
title: "Stripe — High Risk Merchant Lists (MATCH and VMSS)"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-high-risk-lists-2026.md"
tags: [stripe, disputes, match, vmss, tmf, high-risk, chargebacks, fraud, mastercard, visa]
---

## Summary

Criteria and implications for inclusion in Mastercard's MATCH and Visa's VMSS Terminated Merchant File (TMF) databases. All processors must check and report to these databases.

## MATCH (Mastercard Alert to Control High-risk Merchants)

### Qualitative Criteria (11 codes)

| Code | Reason |
| --- | --- |
| 1 | Account Data Compromise |
| 2 | Common Point of Purchase |
| 3 | Laundering |
| 7 | Fraud Conviction |
| 8 | Mastercard Questionable Merchant Audit Program |
| 9 | Bankruptcy/Liquidation/Insolvency |
| 10 | Violation of Standards |
| 11 | Merchant Collusion |
| 12 | PCI DSS Non-Compliance |
| 13 | Illegal Transactions |
| 14 | Identity Theft |

### Quantitative Criteria (2 codes — most common)

| Code | Reason | Threshold |
| --- | --- | --- |
| 4 | Excessive Chargebacks | >1% of Mastercard transactions in a calendar month AND ≥$5,000 in chargebacks |
| 5 | Excessive Fraud | ≥8% fraud-to-sales ratio AND ≥10 fraudulent transactions AND ≥$5,000 in a calendar month |

**Key details**:
- Counts only Mastercard transactions (even though MATCH applies to all networks)
- Month = calendar month (not rolling)
- Must be added within 1 business day of termination
- Qualifies retroactively: if thresholds were met in February and relationship ends in September, still must be reported
- Chargebacks reversed or won by merchant still count

### MATCH Removal

Can only be removed if:
- Added in error, OR
- Code 12 (PCI) and business is now compliant

Records auto-purged after **5 years**.

## VMSS (Visa)

### Qualitative Criteria (13 codes, codes 23–35)

Transaction laundering, illegal transactions, Visa risk compliance, merchant collusion, CPP data compromise, fraud conviction, bankruptcy, violation of agreement, Visa rules violation, PCI/PA-DSS noncompliance, account data compromise, identity theft, Visa disqualification.

### Quantitative Criteria (2 codes — most common)

| Code | Reason | Threshold |
| --- | --- | --- |
| 21 | Excessive Fraud | $250,000 fraud amount AND 1.8% (180 bps) fraud-to-sales ratio in a single month |
| 22 | Excessive Disputes | 1,000 dispute count AND 1.8% (180 bps) dispute-to-sales ratio in a single month |

### VMSS Removal

Only if added in error. No auto-purge timeline mentioned.

## Stripe's Policy

- Cannot process for MATCH/VMSS listed businesses unless extenuating circumstances (e.g. identity theft victim)
- Cannot remove a merchant added for excessive chargebacks/fraud even if issues are remediated

## Related Pages

- [[stripe-high-risk-merchant-lists]] — concept page
- [[disputes]] — dispute rate and chargeback management
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-disputes-high-risk-lists-2026]] — verbatim MATCH and VMSS criteria page
