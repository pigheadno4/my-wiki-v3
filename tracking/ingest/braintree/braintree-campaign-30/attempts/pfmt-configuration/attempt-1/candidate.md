---
title: "Braintree Premium Fraud Management Tools Configuration"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/premium-fraud-management-tools/configuration"
raw_files:
  - "braintree/docs/guides/premium-fraud-management-tools/configuration-2026-09-16.md"
tags: [braintree, premium-fraud-management-tools, configuration, device-data, sandbox]
---

## Overview

This collected Braintree configuration page is an umbrella Premium Fraud Management Tools integration checklist. It assigns three coordinated responsibilities before use: enable the feature in the Control Panel, update client-side code to collect data, and update server-side code to pass the collected data with transaction and verification requests.

This is configuration evidence from a 2026-09-16 website snapshot. It does not identify which named Premium Fraud Management Tool is enabled or establish current merchant eligibility, account enablement, a fraud decision, an exemption or bypass, processor approval, settlement, liability treatment, or chargeback protection. In particular, its umbrella wording does not establish behavior for **Fraud Protection**, **Fraud Protection Advanced**, or any chargeback-protection product, and it does not resolve conflicts documented by those named-product sources.

## Key takeaways

- The page says all three setup areas must be completed together before Premium Fraud Management Tools can be used: Control Panel enablement, client-side data collection, and server-side submission of the collected data with transaction and verification requests.
- Enabling the Control Panel feature before deploying the code changes, or deploying the code changes before enabling the feature, may cause client-side errors or declined transactions. The page therefore recommends thorough sandbox testing before production.
- The linked implementation pages contain the routine platform and SDK details; this short configuration page does not itself define a client SDK version, server SDK version, request field, response schema, supported payment method, or named-product eligibility rule.

> [!warning] Coordinate activation and deployment
> The snapshot warns that either direction of configuration/code mismatch may produce client-side errors or declined transactions. Treat Control Panel enablement and client/server deployment as a coordinated change, and test the integration thoroughly in sandbox before production.

> [!warning] Umbrella and snapshot boundary
> "Premium Fraud Management Tools" is an umbrella label here, not evidence that a particular merchant qualifies for or has enabled Fraud Protection, Fraud Protection Advanced, or a chargeback-protection product. This page provides no exemption, bypass, liability, indemnity, or chargeback-coverage rule and cannot resolve conflicting named-product documentation. Recheck current official guidance for operational decisions.

## Detail locators

- Three-part coordinated configuration prerequisite: `# Configuration`, raw lines 16-21.
- Control Panel enablement route: first checklist item, raw line 19.
- Client-side data-collector responsibility: second checklist item, raw line 20.
- Server-side transaction-and-verification submission responsibility: third checklist item, raw line 21.
- Mismatched activation/deployment failure modes and sandbox-first recommendation: `IMPORTANT`, raw lines 23-24.
- Client-side next-page navigation: raw line 26.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-tools]]

## Raw Sources

- [[raw/braintree/docs/guides/premium-fraud-management-tools/configuration-2026-09-16|Braintree Premium Fraud Management Tools configuration]] - complete collected snapshot for the coordinated Control Panel, client-side and server-side prerequisites plus the deployment-order warning
