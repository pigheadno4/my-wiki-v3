---
title: "Braintree Mitigating Risk"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/risk-factors/mitigating-risk"
raw_files:
  - "braintree/articles/risk-and-security/risk-factors/mitigating-risk-2026-09-16.md"
tags: [braintree, risk, security, fraud, chargebacks, carding, underwriting]
---

## Overview

This captured unversioned Braintree article provides general risk-mitigation guidance for merchants. It combines account-underwriting communication, fraud-tool use, chargeback preparation, CAPTCHA against carding, suspected-integration-compromise escalation, and Braintree analyst outreach; it does not promise fraud prevention or uninterrupted processing.

## Key takeaways

- If a merchant believes its Braintree integration may have been compromised, the article directs it to contact Braintree for assistance.
- Braintree says it underwrites an account for expected transaction volume. An unusually high transaction amount or dramatic volume increase may cause an account hold until review, with notification to the merchant.
- Merchants are asked to explain their business model, billing practices, and expected volume during application and to report expected significant changes, such as a sudden volume spike, to help avoid unexpected processing interruptions.
- The article recommends Basic and Premium Fraud Management Tools. It identifies configurable AVS, CVV, and risk-threshold rules for Basic Fraud Tools and describes Premium Fraud Management Tools as using anti-fraud technology.
- Chargebacks are described as a normal business concern, especially for online payments; the article recommends additional prevention measures and collecting information needed to dispute them successfully.
- A CAPTCHA is described as distinguishing human from machine input and as something that can help prevent carding attacks.
- Braintree says its analysts identify potential provider risk and will contact the merchant when strange account activity requires action, then work with the merchant to resolve the review.

## Detail locators

- General purpose and Braintree assistance: `# Mitigating Risk`, raw lines 14-16.
- Suspected integration compromise escalation: `IMPORTANT`, raw lines 19-20.
- Expected-volume underwriting, conditional account hold, notification, and change disclosure: `### Keep us informed`, raw lines 30-34.
- Basic and Premium Fraud Management Tools orientation: `### Use our fraud tools`, raw lines 37-39.
- Chargeback preparation route: `### Prevent and dispute chargebacks`, raw lines 42-44.
- CAPTCHA and carding guidance: `### Use a CAPTCHA on your site`, raw lines 47-49.
- Analyst monitoring and review outreach: `## What we do`, raw lines 52-54.

## Related

- Company: [[braintree]]
- Provider-wide context: [[braintree-payment-platform]]
- Fraud-control mechanisms: [[braintree-fraud-tools]]
- Chargeback context: [[disputes]]

## Related raw documentation

- [[raw/braintree/articles/guides/fraud-tools/basic/overview-2026-09-16|Braintree Basic Fraud Tools Overview]] - linked navigation; not read as factual evidence for this entry
- [[raw/braintree/articles/guides/fraud-tools/premium/overview-2026-09-16|Braintree Premium Fraud Management Tools Overview]] - linked navigation; not read as factual evidence for this entry
- [[raw/braintree/articles/risk-and-security/chargebacks-retrievals/reducing-chargebacks-2026-09-16|Braintree Reducing Chargebacks]] - linked navigation; not read as factual evidence for this entry

## Raw Sources

- [[raw/braintree/articles/risk-and-security/risk-factors/mitigating-risk-2026-09-16|Braintree Mitigating Risk]] - complete collected snapshot for general merchant risk-mitigation recommendations, account-review conditions, compromise escalation, and Braintree analyst outreach
