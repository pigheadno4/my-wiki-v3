---
title: "Marketplace Score account-holder risk overview"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/identify-account-holder-risk"
raw_files:
  - "adyen/docs/marketplaces/identify-account-holder-risk/2026-09-15.md"
tags: [adyen, marketplaces, score, account-holder-risk, fraud-signals]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplace page introduces **Score** for detecting possible malicious activity among account holders, sub-merchants and sellers. Score analyzes verification and transaction data, raises risk signals, calculates weighted user scores and groups linked accounts; the marketplace reviews cases or configures actions. A signal or high score is a possible-risk indicator, not a finding of fraud or evidence that a payout was stopped. [[adyen-platforms]]

## Key takeaways

- The page says Score is enabled by default for marketplaces that integrated Adyen for Platforms after October 2024, and forecasts enablement for all Adyen for Platforms merchants starting **October 31, 2026**. At this 2026-09-15 capture, the latter is a future rollout statement, not proof of enablement for any account. The raw metadata says last modified 2023-02-13 despite body references to 2025 and 2026; preserve that chronology inconsistency. See raw lines 5–11 and 19–29.
- Rules and models flag unusual verification or transaction behavior. The page expressly says a detected signal does **not** itself disable processing or payouts; the marketplace chooses action after case review or configures automation. Possible actions listed include disabling payouts, suspending accounts and stricter KYC checks. No particular action is shown as executed. See raw lines 31–43.
- Adyen-default KYC signals are described as evaluated in real time, transactional signals as updated daily; custom high-risk-list and custom-rule signals are described as real-time. Signals can indicate possible collusion or inconsistencies rather than confirmed wrongdoing. A weighted score ranges 0–100; even 100 means high possibility rather than confirmed fraud and triggers no automatic action just by reaching 100. See raw lines 45–62.
- Shared KYC data can group users as a linked identity, propagate a user's signals to that group and assign the same group score. The two-user bank-account/score sequence is illustrative, not a confirmed incident or identity determination. See raw lines 64–74.
- Device/session behavior inspection is marked **limited availability**. The page says a pilot began in December 2025 for interested Score customers using hosted onboarding or components; it describes fraud-signaling use, no third-party sharing, a planned later expansion and an account-manager route for API-only SDK pilots. These are dated pilot/plan statements, not established availability for every marketplace. See raw lines 76–91.

## Detail locators

- **Score scope, rollout wording and metadata chronology:** raw lines 5–29.
- **Signal-to-case/action boundary:** raw lines 31–43.
- **Rule categories, evaluation cadences and score meaning:** raw lines 45–62.
- **Linked-account propagation example:** raw lines 64–74.
- **Limited device-data pilot and future plan:** raw lines 76–91.

## Related

- [[adyen-platforms]]
- [[source-adyen-docs-platforms-identify-account-holder-risk|Parallel Platforms-path Score overview]]
- [[source-adyen-docs-platforms-manage-account-holder-risk|Related case management guide]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/identify-account-holder-risk/2026-09-15|Adyen Marketplace Score overview — collected 2026-09-15]]
