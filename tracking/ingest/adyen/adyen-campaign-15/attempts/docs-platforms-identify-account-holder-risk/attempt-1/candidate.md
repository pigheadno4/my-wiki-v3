---
title: "Adyen Score for platform account-holder risk"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/identify-account-holder-risk"
raw_files:
  - "adyen/docs/platforms/identify-account-holder-risk/2026-09-15.md"
tags: [adyen, platforms, score, account-holder-risk, fraud-signals]
---

## Overview

This 2026-09-15 capture introduces Adyen Score for identifying potential malicious activity among a platform’s account holders, sub-merchants or sellers. Score analyzes verification and transaction data, raises risk signals, calculates scores, and groups linked accounts; the platform reviews cases or configures actions. These are indicators and controls, not a finding that an identified user committed fraud or that a payout was actually stopped. See [[adyen-platforms]]. The raw metadata says last modified 2023-02-13 although the body refers to 2025 and 2026 events, so the chronology is internally inconsistent.

## Key takeaways

- The page says Score is enabled by default for platforms integrated after October 2024 and says Adyen will enable it for all Adyen for Platforms merchants starting October 31, 2026. In the dated capture, the latter is a future rollout statement, not current enablement proof for a given platform. The page still directs readers to access/setup information to use Score.
- Score flags possible risk when a rule or model detects unusual verification or transaction behavior. Adyen says a detected signal by itself does not disable processing or payouts; the platform is responsible for reviewing cases and choosing action or configuring automation. Described actions include disabling payouts, suspending accounts and imposing stricter KYC checks. The guide does not show any specific action executed.
- Adyen-default KYC rules are described as real-time and default transactional signals as updated daily; custom high-risk-list and custom-rule signals are described as real-time. The platform may use default rules/signals or add its own. A signal can reflect an inconsistency or possible collusion rather than proven fraud.
- Each platform user receives a weighted risk score from 0 to 100. A score of 100 signals high possibility, not confirmed malicious conduct, and triggers no automatic action merely by reaching that value. Score can link accounts based on shared KYC data, propagate a signal to the grouped identity, and assign the group the same score; the bank-account/score sequence is an illustrative scenario, not a confirmed case.
- Session-behavior and device-data inspection is marked limited availability. The page says a pilot began December 2025 for interested Score customers using hosted onboarding or components, for fraud assessment/signaling; API-only onboarding customers are directed to contact their account manager about an SDK pilot. Expansion after the pilot is a plan in the snapshot, not established current availability. The page states pilot-collected data is not shared with third parties.

## Detail locators

- Score scope, platform-user identity, enablement/rollout statements and metadata conflict: pinned raw lines 5–29.
- Detection flow, platform responsibility, candidate controls and no automatic payout block on a signal: pinned raw lines 31–43.
- Rule categories/update cadences, signal examples and weighted 0–100 score: pinned raw lines 45–62.
- Linked-account grouping and illustrative propagation scenario: pinned raw lines 64–74.
- Limited-availability device/behavior pilot, channels, use and future plan: pinned raw lines 76–91.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/platforms/identify-account-holder-risk/2026-09-15|Adyen Score platform-risk snapshot (2026-09-15)]]
