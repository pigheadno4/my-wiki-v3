---
title: "Braintree 3D Secure Rules Manager (JavaScript v3)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/3d-secure/rules-manager/javascript/v3"
raw_files:
  - "braintree/docs/guides/3d-secure/rules-manager/javascript/v3-2026-09-16.md"
tags: [braintree, 3d-secure, rules-manager, javascript-v3, sca, control-panel]
---

## Overview

This JavaScript v3-routed Braintree guide documents 3D Secure Rules Manager: Control Panel rulesets that determine when and how 3DS is requested when `verifyCard()` runs. The collected snapshot covers merchant-account assignment, rule priority and client-request overrides, action and liability-shift limits, custom-field matching, and illustrative business-objective rulesets.

## Key takeaways

- The snapshot says Rules Manager is automatically enabled for all merchants in Sandbox and Production. A ruleset can contain multiple prioritized rules and can be assigned to multiple merchant accounts, while each merchant account can have only one ruleset; the associated ruleset is evaluated when `verifyCard()` is called. Treat this as collected page scope, not proof of a particular merchant's current eligibility, configuration, or production behavior.
- When multiple rules match, only the higher-priority rule is applied. Supplying `challenge_requested` or `requested_exemption_type` in the `verifyCard()` request overrides any matched rule. This separates Control Panel policy from per-request JavaScript execution; it does not say the client creates or edits the ruleset.
- The actions include applying 3DS, requesting a challenge, requesting Low Value or Transaction Risk Analysis exemptions, skipping 3DS where applicable, and Data Only 3DS. Requesting a challenge does not guarantee that an issuer will present one. Granted exemptions, skipped 3DS, and Data Only 3DS do not provide liability shift under the stated conditions, and TRA requires qualification.
- `Skip 3DS wherever applicable` is described as applying outside the PSD2 region; in a regulated PSD2 market it has no effect and 3DS still occurs. A `skipped_due_to_rule` result from `verifyCard()` is an authentication-policy outcome before the separate transaction-sale step, not proof of authorization, processor approval, gateway acceptance, capture, settlement, or funding.
- Custom-field rules depend on values passed to `verifyCard()` matching fields defined in Rules Manager. The retry example passes `retry_transaction` but then describes a rule for `retryTransaction`; the snapshot does not reconcile those names, so copy neither spelling as an assured working contract without clarification.
- The geographical grouping, monitoring, maintenance, retry, travel, vaulting, and business-objective material is recommendation or example content. Its labeled expected outcomes are not guarantees of conversion, authorization, liability shift, compliance, or chargeback protection.

> [!warning] Authentication and rule evaluation are not payment completion
> Rules Manager controls how 3DS authentication or exemptions are requested when `verifyCard()` runs. Neither a rule match nor a 3DS result establishes transaction authorization, processor approval, gateway acceptance, capture, settlement, funding, or guaranteed chargeback protection.

> [!warning] Version, platform, and current-state scope
> This is a JavaScript v3-routed documentation snapshot. Its rule criteria name iOS, Android, and Web as client platforms, but the page does not establish native SDK versions or behavioral parity. The snapshot's broad enablement statement is not live account evidence, and its recommendations and examples are not mandatory configuration requirements.

## Detail locators

- Rules Manager purpose and the pre-existing Braintree 3DS 2 integration qualification: `## Introducing the 3D Secure Rules Manager`, lines 17-31.
- Collected Sandbox/Production enablement statement, ruleset assignment cardinality, and evaluation on `verifyCard()`: `## How 3D Secure Rules Manager Works`, lines 57-61.
- Geographical grouping as a recommendation rather than the only grouping method: `### Rulesets`, line 75.
- Higher-priority-rule behavior, monitoring recommendation, and `verifyCard()` request-parameter override: `### Rules > #### Creating Rules`, lines 97-111.
- Rule criteria, action semantics, issuer-controlled challenge, exemption and TRA conditions, PSD2 skip limit, `skipped_due_to_rule`, and Data Only liability boundary: `#### Rule Criteria` through `#### Available Actions`, lines 126-148.
- Client-platform conditions: `#### Conditions`, lines 151-158.
- Custom-field match condition and Control Panel setup: `### Custom Fields`, lines 161-198.
- JavaScript custom-field shape, retry/travel examples, and the unresolved `retry_transaction` versus `retryTransaction` naming mismatch: `#### Trigger a Rule with custom fields via API`, lines 201-237.
- Merchant-account assignment procedure: `### Assigning Merchant Accounts to Rulesets`, lines 240-250.
- Illustrative rulesets and provider-labeled expected outcomes: `### Example 3D Secure Rulesets for Business Objectives`, lines 253-313.
- Rule-monitoring recommendation: `### Maintaining your Rules`, lines 316-318.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-3d-secure]]
- Related concept: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/docs/guides/3d-secure/rules-manager/javascript/v3-2026-09-16|Braintree 3D Secure Rules Manager JavaScript v3 guide]] - complete collected page covering rulesets, rule priority and overrides, actions and conditions, custom fields, merchant-account assignment, examples, and maintenance advice
