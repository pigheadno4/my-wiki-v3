---
title: "Braintree Risk Threshold Rules"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/fraud-tools/basic/risk-threshold-rules"
raw_files:
  - "braintree/articles/guides/fraud-tools/basic/risk-threshold-rules-2026-09-16.md"
tags: [braintree, fraud-tools, risk-threshold-rules, velocity-checks, carding]
---

## Overview

This collected Braintree guide documents risk threshold rules, also called velocity checks, for detecting and preventing carding attacks by reacting when specified customer information passes through the gateway repeatedly within a designated period. The documented actions are email notification or automatic rejection of the triggering verifications or transactions.

## Key takeaways

- The page limits these rules to credit-card and certain Google Pay transactions; it does not establish applicability to other payment methods.
- A custom rule is created in the Control Panel under **Fraud Management** > **Risk Thresholds** and is defined by five criteria: Action, Threshold, Operation, Field, and Window. The collected page describes repeated-value counters and time windows, not a numeric risk score or a risk-score cutoff.
- The selected Field must be present in submitted transactions for a rule that relies on it to work properly, because many listed Fields are not otherwise required by the gateway.
- The page says the only override is to temporarily disable risk threshold rules in the Control Panel and says that doing so is typically not recommended. This is a configuration-level exception route, not evidence of per-transaction approval, fraud immunity, chargeback protection, or liability shift.

## Configuration and decision boundaries

The raw guide contains the exact Control Panel creation and enable/disable steps, an Email-first testing recommendation, alert-frequency and purchase-frequency guidance, and the complete rule-field catalog. Use those locators for configuration detail rather than treating one worked example or one threshold as a general default.

The rule criteria and action descriptions are under `### Rule criteria`: use `#### Action` for email and gateway-reject behavior, `#### Threshold` for trigger counting, `#### Operation` for transaction-versus-verification monitoring, `#### Window (minutes)` for reset timing, and `#### Fields` for the complete monitored-value list and one-field-per-rule boundary.

## Detail locators

- Availability boundary: `# Risk Threshold Rules > **AVAILABILITY**`, lines 17-18.
- Carding/velocity-check purpose and email-versus-rejection outcome: `# Risk Threshold Rules`, line 22.
- Control Panel custom-rule creation: `## Creating custom rules`, lines 31-44.
- Worked notification example: `## Creating custom rules > ### Example`, lines 47-55.
- Enable/disable route and recommended testing/setup guidance: `## Enabling existing risk threshold rules`, lines 58-93.
- Required criteria, action outcomes, threshold semantics, operation scope, window behavior, complete field catalog and supporting-data prerequisite: `### Rule criteria`, lines 96-156.
- Only documented override: `## Overriding rejections`, lines 161-163.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-tools]]
- Supporting concept: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/guides/fraud-tools/basic/risk-threshold-rules-2026-09-16|Braintree Risk Threshold Rules guide]] - complete collected page covering availability, purpose, Control Panel configuration, rule criteria, recommendations, field-data prerequisite and override boundary
