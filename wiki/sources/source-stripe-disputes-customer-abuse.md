---
title: "Stripe — Customer Abuse"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-disputes-customer-abuse-2026.md"
tags: [stripe, fraud, disputes, refund-abuse, resale-abuse, trial-abuse, sigma, radar, velocity-rules]
---

## Summary

Three customer abuse types (refund, resale, trial): detection queries, Radar velocity rules, and remediation strategies.

## 3 Abuse Types

### Refund Abuse

Customer repeatedly returns orders or falsely claims non-receipt.

**Detection**: Sigma query bucketing orders by customer refund frequency (≥10/year = high concentration signal — analyze relative to business context).

**Remediation**: Notify high-refunding customers, restrict future orders (temporary/permanent), add fee to deter repeat refunds.

### Resale Abuse

**Account sharing** (password sharing): simultaneous logins or geo-dispersed IPs in short window → add email/SMS OTP friction.

**Account transfers**: accounts sold on external marketplaces; same card/device + same promo code for multiple accounts; geo-IP mismatch shortly after creation.

**Radar rules for resale**:
```
Review if :card_funding: = 'prepaid' and :total_customers_for_card_weekly: > 3
  and not :is_off_session: and :charge_description: = "Individual Plan New Customer Discount"

Block if ::customer_count_for_card_and_coupon_yearly:: > 3  (metadata attribute)
```

Also use Stripe Sigma to investigate suspected resold accounts.

### Trial Abuse

Customers cycle through free trials with no intent to convert; or use stolen/virtual cards knowing they won't cancel.

**Detection/Prevention**: Radar trial abuse control (risk settings) detects repeated trial signup and end-of-trial payment failure.

## Related Pages

- [[disputes]] — concept page (updated with customer abuse types)
- [[source-stripe-radar-free-trial-abuse]] — Radar free trial abuse control
- [[source-stripe-radar-rules-reference]] — velocity rules for Radar

## Raw Sources

- [[stripe-disputes-customer-abuse-2026]] — verbatim customer abuse guide
