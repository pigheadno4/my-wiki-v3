---
title: "Adyen Marketplace account-holder risk management with Score"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/manage-account-holder-risk"
raw_files:
  - "adyen/docs/marketplaces/manage-account-holder-risk/2026-09-15.md"
tags: [adyen, marketplaces, score, account-holder-risk, payouts]
---

## Overview

This Adyen Marketplace **Score** guide describes reviewing account-holder risk cases and configuring rules or actions in Customer Area after signals of possible fraud or unusual activity. Its raw metadata says last modified 2020-12-22 and it was captured 2026-09-15; the page also describes an October 31, 2026 planned Score enablement. Treat the rollout as a dated statement, not proof of access for a specific marketplace. A signal, score, queue label or example webhook does not itself establish fraud, verification, payout execution or funds receipt. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Roles and availability:** The guide assigns **Merchant Marketplace Risk** to case review and direct action, and **Merchant Marketplace Risk Admin** to risk rules and automated actions. It says Score is included by default for marketplaces created after October 2024 and describes planned enablement for Adyen for Platforms merchants beginning October 31, 2026. Verify actual access for the relevant platform rather than projecting the rollout from this snapshot.
- **Rule effects and cases:** Rules can change the risk score at a selected impact level or choose the automated action **None**, **Bump KYC tier**, or **Disable payouts**. An automated-actions log records actions for review. Flagged risk signals become open cases; the dashboard distinguishes open, reviewed and suspicious queues and shows balance-platform users, signals, volume and scores. A configured rule or log is not proof that a particular payout completed.
- **Direct actions and false positives:** A reviewer can mark a case Reviewed or Suspicious, block or re-enable payouts, suspend an account, add high-risk KYC values from **confirmed fraudulent users**, or trust linked accounts. Queue classification, payout control and account suspension are distinct. An irrelevant signal can be muted for a week, month, year or indefinitely. Excluding an irrelevant KYC value from linked-account matching is **permanent and cannot be undone**. The high-risk-list section also describes individual/CSV additions for specified KYC attributes; see the raw for exact scope.
- **Conditional webhook and identifiers:** Receiving `balancePlatform.score.triggered` requires a server that accepts webhooks, subscription to Configuration webhooks and Adyen-contact enablement. The sample payload is marked `environment: test`. Its `data.id` is a score calculation/recalculation identifier that changes each calculation, while `data.accountHolder.id` is the separate account-holder identifier. The example's score, status and `automatedActions` are illustrative.

## Detail locators

- Purpose, Customer Area roles and dated rollout: pinned raw lines 15-29.
- Rule configuration, score impact and actions log: pinned raw lines 31-62.
- Cases, direct actions and confirmed-fraud qualifier: pinned raw lines 64-99.
- Muting, irreversible linked-identity exclusion and high-risk-list additions: pinned raw lines 100-157.
- Webhook prerequisites and example identity: pinned raw lines 159-204.

## Related

- [[adyen-platforms]] — main platform concept and reciprocal route.
- [[adyen-risk-management]] — broader payment-risk concept; Score account-holder cases have their own workflow.
- [[source-adyen-docs-platforms-manage-account-holder-risk]] — separately captured Platforms-path counterpart.

## Raw Sources

- [[raw/adyen/docs/marketplaces/manage-account-holder-risk/2026-09-15|Marketplace Score account-holder risk guide, captured 2026-09-15]]
