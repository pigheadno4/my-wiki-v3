---
title: "Braintree Fraud Tools Overview"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/fraud-tools/overview"
raw_files:
  - "braintree/articles/guides/fraud-tools/overview-2026-09-16.md"
tags: [braintree, fraud-tools, basic-fraud-tools, premium-fraud-management-tools, gateway-rejections]
---

## Overview

This 2026-09-16 Braintree website snapshot is an umbrella comparison and navigation page for Basic Fraud Tools and Premium Fraud Management Tools. It describes fraud-risk assessment, routes account enablement and new-rule creation through the Control Panel, and gives a Control Panel search path for fraud-related transaction and verification requests with `Gateway Rejected` status. It is not evidence that a tool is enabled or currently available for a particular merchant, region, account, payment method, transaction, or verification.

## Key takeaways

- The page divides Braintree fraud protection into two levels: Basic Fraud Tools and Premium Fraud Management Tools. Its comparison table names Risk Thresholds, AVS, CVV, Fraud Protection Lite, and Fraud Protection Advanced, then compares risk-rule style, additional features, code-change level, availability, and fees. Use the raw table for the tool-specific entries rather than treating the tools as interchangeable.
- The captured table labels Risk Thresholds, AVS, and CVV as available to all merchants with no additional fee; Fraud Protection Lite as limited availability with regional restrictions and an additional fee; and Fraud Protection Advanced as available to all merchants with an additional fee. These are snapshot-scoped page labels, not proof of current or merchant-specific eligibility, pricing, provisioning, or account enablement.
- The page explicitly warns that Braintree fraud tools may not be enabled on an account by default. It says merchants can enable selected tools, if not already enabled, or create new rules in the Control Panel. This is a configuration route, not evidence that a change was authorized, applied, or effective.
- The overview says requests it identifies as fraudulent are rejected before information is sent to the processor and receive `Gateway Rejected` status, with AVS, CVV, Fraud, or Risk Threshold Exceeded as the listed reason categories. The page then provides a Control Panel search-and-CSV-filter workflow for locating those transactions or verifications.

> [!warning] Do not generalize the overview's rejection timing
> The dedicated [[source-braintree-fraud-tools-basic-avs-cvv-rules]] guide documents an issuer-approval response followed by an AVS/CVV-rule gateway rejection and void request. Therefore, this overview's broad pre-processor wording must not override the dedicated AVS/CVV flow or be treated as a universal timing model for every listed tool. A `Gateway Rejected` record also does not establish settlement, funding, liability shift, chargeback protection, or successful fraud prevention.

> [!warning] Escalate abnormal rejection rates
> The page directs merchants who believe they are seeing an abnormal number of fraud-related gateway rejections to contact Braintree. The snapshot does not define an abnormal-rate threshold or supply an automated remediation rule.

## Detail locators

- Account-default enablement warning and Control Panel enablement/rule route: `# Overview`, raw lines 17-18.
- Stated fraud purpose and the two named fraud patterns: `# Overview`, raw lines 22-28.
- Basic-versus-Premium split and the complete tool comparison: `## Fraud tool comparison`, raw lines 31-50.
- Fraud Protection Lite regional-availability qualification: raw line 54.
- `Gateway Rejected` timing statement and rejection-reason categories: `## Searching for rejected transactions`, raw lines 57-65.
- Control Panel search, CSV download and reason-filter procedure: raw lines 67-80.
- Abnormal-rejection-rate contact direction: raw lines 83-84.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-tools]]
- Control surface: [[braintree-control-panel]]
- Named Fraud Protection boundary: [[braintree-fraud-protection]]
- Fraud Protection Advanced boundary: [[braintree-fraud-protection-advanced]]

## Related raw API references

- [[raw/braintree/articles/guides/fraud-tools/basic/overview-2026-09-16|Braintree Basic Fraud Tools overview]] - linked navigation for Basic Fraud Tools; not read as factual evidence for this source
- [[raw/braintree/articles/guides/fraud-tools/premium/overview-2026-09-16|Braintree Premium Fraud Management Tools overview]] - linked navigation for the article-level Premium comparison; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/transactions/gateway-rejections-2026-09-16|Braintree Gateway Rejections article]] - linked status navigation; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/articles/guides/fraud-tools/overview-2026-09-16|Braintree Fraud Tools overview]] - complete collected snapshot covering the Basic/Premium comparison, account-enablement warning, tool-level availability and fee labels, and fraud-related gateway-rejection lookup route
