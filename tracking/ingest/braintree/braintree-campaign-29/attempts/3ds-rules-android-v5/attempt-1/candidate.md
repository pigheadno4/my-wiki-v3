---
title: "Braintree 3D Secure Rules Manager — Android v5 route"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/3d-secure/rules-manager/android/v5"
raw_files:
  - "braintree/docs/guides/3d-secure/rules-manager/android/v5-2026-09-16.md"
tags: [braintree, 3d-secure, rules-manager, android, authentication]
---

## Overview

This 2026-09-16 snapshot is the Android v5-routed Braintree guide to 3D Secure Rules Manager. It documents merchant policy configured in the Braintree Control Panel—rulesets, priorities, criteria, actions and merchant-account assignment—and Android request data used when `verifyCard()` evaluates that policy. The Android v5 route and Java/Kotlin examples do not establish a merchant's installed SDK version or move ruleset administration into the client.

Rules Manager controls when and how 3DS authentication is requested. It does not authorize, capture or settle a payment, guarantee issuer approval or replace the separate transaction-sale step. See [[braintree-3d-secure]] for the authentication and conditional-liability-shift boundary.

## Key takeaways

- Merchants create business-specific 3DS invocation rules in the Control Panel. The page says no developer work is required to set up Rules Manager only **once Braintree 3DS 2 is already integrated**.
- The page says Rules Manager is automatically enabled in Sandbox and Production, but that statement is about the manager, not proof that an individual account is currently eligible, compatibly configured or enrolled for 3DS. The existing collected 3DS authority says production accounts outside the EEA are not automatically enrolled.
- A ruleset can contain multiple prioritized rules and can be assigned to multiple merchant accounts, while each merchant account can have only one ruleset. The assigned ruleset is evaluated when `verifyCard()` is called. If multiple rules match, only the higher-priority rule applies; request parameters `challenge_requested` or `requested_exemption_type` override a matched rule.
- Rules Manager actions have consequential limits: requesting a challenge does not guarantee that the issuer will present one; granted low-value or Transaction Risk Analysis exemptions do not provide liability shift; TRA requires qualification; “Skip 3DS wherever applicable” has no effect in a PSD2-regulated market and forfeits 3DS benefits where skipping occurs; Data Only 3DS does not provide liability shift. These are authentication-policy outcomes, not payment authorization or settlement outcomes.
- Custom fields are defined and selected in the Control Panel, while matching field values are passed in `verifyCard()`. The Java and Kotlin snippets are examples of that Android client handoff, not universal required field names or guaranteed business outcomes.
- The page recommends grouping rulesets by geographical region and monitoring and adjusting rules over time. Those are operational recommendations, not stated platform requirements.

## Detail locators

- Product purpose, Control Panel ownership and the Braintree 3DS 2 integration condition: `## Introducing the 3D Secure Rules Manager`, lines 17-31.
- Automatic-enable statement, ruleset cardinality and `verifyCard()` evaluation: `## How 3D Secure Rules Manager Works`, lines 57-61.
- Ruleset creation and geography-grouping recommendation: `### Rulesets`, lines 73-89.
- Rule priority, monitoring advice and request-parameter override: `### Rules`, lines 92-113.
- Criteria, action semantics, exemption/liability limits, issuer-owned challenge decision and platform condition: `#### Rule Criteria` through `#### Conditions`, lines 128-160.
- Control Panel custom-field setup, Android Java/Kotlin request examples and example-only retry/travel scenarios: `### Custom Fields`, lines 163-280.
- Merchant-account assignment workflow: `### Assigning Merchant Accounts to Rulesets`, lines 283-293.
- Illustrative business-objective rulesets and continuing-maintenance advice: `### Example 3D Secure Rulesets for Business Objectives` through `### Maintaining your Rules`, lines 296-343.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-3d-secure]]

## Related raw API references

- [[raw/braintree/articles/control-panel/custom-fields-2026-09-16|Braintree Control Panel custom fields article]] - unread navigation-only route linked by this guide

## Raw Sources

- [[raw/braintree/docs/guides/3d-secure/rules-manager/android/v5-2026-09-16|Braintree 3D Secure Rules Manager — Android v5 route]] - fully read snapshot covering Control Panel rule policy, `verifyCard()` evaluation and Android custom-field examples
