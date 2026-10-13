---
title: "Adyen Machine Learning Risk Rules"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/configure-your-risk-profile/machine-learning-rules"
raw_files:
  - "adyen/docs/risk-management/configure-your-risk-profile/machine-learning-rules/2026-09-15.md"
tags: [adyen, protect, risk-management, machine-learning, fraud, bot-attacks]
---

## Overview

This Adyen Protect guide distinguishes machine-learning rules for bot-attack detection and fraud-risk classification in online payments. It explains eligibility, the fraud-risk blocking threshold, prior Allow-rule effect, and how to inspect contributing signals in Risk results.

## Key takeaways

- The guide requires an online-payments integration with risk management enabled. **Machine learning: bot attack risk** is listed for basic and premium Protect and has no configuration options; it detects and blocks unusually fast transactions with suspicious payment properties. **Machine learning: fraud risk** requires premium features. Changing that rule's settings requires a Customer Area user with **Merchant change risk settings** or **Risk admin** role.
- The premium fraud-risk rule evaluates transactions that can be disputed, such as credit- and debit-card payments. It assigns a level from **Very Low** to **Very High** before authorization and blocks a transaction when its classification exceeds the merchant's selected threshold, unless an Allow rule was triggered before authorization. The default block threshold is high risk and above. Threshold suggestions by business model are advice, not universal requirements, and the guide says the rule cannot detect every fraud case.
- The Risk results page shows influential signals derived from company transaction data, checkout/page collection for web integrations, and Adyen global transaction data. To inspect a payment's signal breakdown in live Customer Area, the guide directs the user to a merchant account using the latest risk-profile version; the breakdown can take up to two hours to appear. This page does not prove a specific merchant's premium enablement, a particular classification, or a payment's actual authorization outcome.

## Detail locators

- Opening and `## Requirements` (raw lines 15–30): online integration, enabled risk management, role, premium, and bot-rule configuration limits.
- `## How it works` (raw lines 32–52): basic/premium bot rule, premium fraud rule, pre-authorization classification and blocking, disputable transaction scope, and business-dependent threshold guidance.
- `## View or change your risk threshold` (raw lines 54–69): default threshold, prior Allow-rule exception, risk limitations, and Customer Area adjustment path.
- `## Analyze signals` (raw lines 71–96): signal sources, examples, positive/negative contributions, live merchant-account navigation, and breakdown timing.

## Related

- Company: [[adyen]]
- Concept: [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/configure-your-risk-profile/machine-learning-rules/2026-09-15|2026-09-15 Adyen machine-learning risk-rules guide]]
