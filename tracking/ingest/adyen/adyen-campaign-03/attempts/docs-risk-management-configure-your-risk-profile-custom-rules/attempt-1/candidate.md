---
title: "Adyen Protect Custom Risk Rules"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/configure-your-risk-profile/custom-rules"
raw_files:
  - "adyen/docs/risk-management/configure-your-risk-profile/custom-rules/2026-09-15.md"
tags: [adyen, risk-management, protect, custom-rules, fraud, backtesting]
---

## Overview

This Adyen Docs snapshot explains how a merchant configures custom rules in a Protect risk profile to address business-specific fraud risks or complement the machine-learning fraud-risk rule. It applies to an online payments integration with risk management and Protect premium enabled, and a Customer Area user with **Merchant change risk settings** or **Risk admin** permission. See [[adyen]] and [[adyen-risk-management]].

## Key takeaways

- A custom rule is configured to run before or after authorization and takes an action when its conditions match: **Allow**, **Block**, **Review**, or **Check for 3DS**. The page defines **Allow** as not blocking due to that matching rule, **Block** as blocking the matching transaction, and **Review** as sending it to case management. This rule-level description is not a guarantee that another risk control or the issuer will approve a transaction.
- **Check for 3DS** makes no allow-or-block risk decision on the match. A pre-authorization rule with this action can be selected as a trigger for Dynamic 3D Secure rules to influence the authentication engine; that route is not itself an authorization or authentication success result.
- Conditions combine with **AND** or **OR** and compare a selected field, data-type-appropriate operator, and value. Labels classify rules. The operator matrix and Customer Area creation steps remain at the raw locators below.
- The page offers backtesting on historical data before activating a new rule or changing an existing one. Its displayed Backtest path selects a **pre-authorization** rule from the **Allow**, **Block**, or **Review** tabs; it does not establish this UI route for post-authorization or **Check for 3DS** rules. Backtesting is an assessment of prior data, not proof of a live rule's outcome.
- A rule can be copied to another risk profile while choosing the target profile, label, action, and optional name or condition edits. The page does not state the copied rule's activation state. Changes to a matching **Block** rule can block future transactions when active, so keep creation, testing, and live effect distinct.

## Detail locators

- Opening and `## Requirements`, raw lines 15–30 — custom-rule purpose, integration/risk/premium prerequisites, roles, and premium-only limit.
- `## How it works` and `## Create a custom rule`, raw lines 32–77 — pre/post-authorization choice, action meanings, labels, and condition construction.
- `### Operators`, raw lines 78–98 — supported comparisons and data-type/multiple-value limits.
- `## Backtest a rule`, raw lines 99–113 — historical-data purpose and pre-authorization Allow/Block/Review UI path.
- `## Copy a rule`, raw lines 114–124 — cross-profile copy and editable fields.

## Related

- [[adyen]] — provider page.
- [[adyen-risk-management]] — Protect configuration and risk/dispute concept.
- [[source-adyen-docs-risk-management-dynamic-3d-secure]] — separate Dynamic 3DS guide; the custom-rule page only identifies a possible trigger route.

## Raw Sources

- [[raw/adyen/docs/risk-management/configure-your-risk-profile/custom-rules/2026-09-15|Adyen Docs — Custom rules (2026-09-15 snapshot)]]
