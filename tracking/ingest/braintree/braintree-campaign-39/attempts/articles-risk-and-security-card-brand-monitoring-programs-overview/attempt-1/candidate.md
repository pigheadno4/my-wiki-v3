---
title: "Braintree Card Brand Monitoring Programs Overview"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/card-brand-monitoring-programs/overview"
raw_files:
  - "braintree/articles/risk-and-security/card-brand-monitoring-programs/overview-2026-09-16.md"
tags: [braintree, card-brands, monitoring-programs, chargebacks, disputes, fraud]
---

## Overview

This collected Braintree article is an overview of Visa and Mastercard chargeback- and fraud-monitoring programs. It explains the monthly threshold-to-program transition, defines the ratios and other terms used by the page, and describes a notification route limited to merchant accounts provided through Braintree. The captured page metadata reports creation and update timestamps on 2025-04-01.

## Key takeaways

- The page says card brands establish acceptable thresholds for chargebacks and reported fraud. If an account meets or exceeds a threshold in a calendar month, it can enter one or more monitoring programs and remain there until it meets the card brand's exit qualifications.
- It defines the fraud ratio as fraud amount reported in a month divided by settled-sales amount in that month. It defines the chargeback or dispute ratio as the number of chargebacks opened in a month divided by the number of settled sales in that month.
- For the chargeback-ratio calculation described here, the page says card brands count only first chargebacks; pre-arbitrations or second chargebacks and retrievals are excluded.
- Visa and Mastercard thresholds are described as similar but not identical. This overview provides no numeric threshold values and routes to separate Visa and Mastercard program articles for program-specific details.
- Only when the merchant account is provided through Braintree does the page say Braintree's Disputes team will notify the merchant if the account is identified in a card-brand monitoring program. The page also describes Braintree proactive monitoring and the Disputes team as a resource; it does not establish notification for a differently provided account or guarantee prevention, remediation, or exit.

> [!warning] Snapshot and authority boundary
> This is Braintree-hosted guidance collected on 2026-09-16, with page metadata dated 2025-04-01. It is not independent or current Visa/Mastercard rule authority, a compliance determination, account enrollment proof, or evidence that any current numeric threshold, notification, remediation, or program-exit condition applies to a particular merchant. Consult the applicable current card-brand program rules and the account's responsible provider for operational decisions.

## Detail locators

- Merchant responsibility to minimize chargebacks and fraud: raw line 16.
- Monthly threshold, possible entry into one or more programs, and exit qualification: raw line 18.
- Monitoring-program term definitions, including count, amount, merchant account ID and threshold: raw lines 20-30.
- Fraud-ratio and chargeback/dispute-ratio formulas: raw lines 31-32.
- First-chargeback-only calculation and exclusion of pre-arbitrations and retrievals: raw line 34.
- Visa/Mastercard difference and program-specific outbound routes: `## Thresholds for monitoring programs`, raw lines 37-39.
- Braintree-provided-account notification condition, proactive-monitoring statement and Disputes-team role: `## How to know if you’re in a monitoring program`, raw lines 42-46.
- Source page creation and update timestamps: frontmatter, raw lines 5-10.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]

## Raw Sources

- [[raw/braintree/articles/risk-and-security/card-brand-monitoring-programs/overview-2026-09-16|Braintree Card Brand Monitoring Programs Overview]] - complete collected snapshot covering threshold-based program entry and exit, ratio definitions, calculation exclusions, and the Braintree-provided-account notification condition
