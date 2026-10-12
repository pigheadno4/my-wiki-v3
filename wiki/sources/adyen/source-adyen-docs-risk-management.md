---
title: "Adyen Docs: Risk management"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management"
raw_files:
  - "adyen/docs/risk-management/2026-09-15.md"
tags: [adyen, risk-management, protect, fraud, disputes]
---

## Overview

This Adyen risk-management documentation overview introduces [[adyen-risk-management|Protect]], Adyen's risk engine, and routes merchants through risk settings, profiles, rules, data quality, analytics, and dispute handling. In the captured page, payment risk evaluation can lead to block, allow, or review actions based on the account's risk settings, risk profile, and rules.

## Key takeaways

- Protect is described as enabled by default, with a default risk profile available on first configuration. The basic-versus-premium feature table is at raw lines 30–47; premium access depends on enabling premium features in risk settings.
- Adyen says configuring company risk settings and at least one risk profile is needed for either tier. Profiles use risk rules to fine-tune the setup.
- The page recommends sending high-quality payment-request data and reviewing recommended and required integration options to improve Adyen Uplift and Protect evaluations. This is a recommendation in the overview, not a claim that every example field is mandatory or an outcome guarantee.
- The overview also routes merchants to risk and dispute analytics, optional case management and dynamic 3D Secure, and handling disputes through Customer Area or the Disputes API. The linked guides, rather than this overview, carry detailed procedures.

## Detail locators

- **Risk engine, raw lines 30–47** — default enablement and profile, basic/premium feature matrix, including premium-only machine-learning fraud detection, custom rules, experiments, and case management.
- **Data quality, raw lines 49–65** — Adyen Uplift relationship, data recommendations, and links to collection and field references.
- **Get started, raw lines 67–82** — required risk settings and at least one risk profile, followed by rule configuration links.
- **Customize Protect premium profiles, raw lines 84–98** — custom rule building and backtesting and the machine-learning fraud-risk rule.
- **Analytics; Extra risk management; Disputes and chargebacks, raw lines 100–130** — monitoring, experiments, case management, dynamic 3D Secure, and dispute-management routes.

## Related

- [[adyen]]
- [[adyen-risk-management]]
- [[adyen-3d-secure]]
- [[disputes]]

## Raw Sources

- [[raw/adyen/docs/risk-management/2026-09-15|Adyen Docs — Risk management (2026-09-15)]]
