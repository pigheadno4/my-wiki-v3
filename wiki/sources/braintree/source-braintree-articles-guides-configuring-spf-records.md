---
title: "Braintree Configuring SPF Records"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/configuring-spf-records"
raw_files:
  - "braintree/articles/guides/configuring-spf-records-2026-09-16.md"
tags: [braintree, spf, dns, email-receipts, recurring-billing-notifications]
---

## Overview

This collected Braintree guide describes a DNS Sender Policy Framework (SPF) configuration route for merchants whose Braintree email receipts or recurring-billing notifications send customer email on the merchant's behalf. The page says that configuring SPF records is no longer required for integration, but it also says the named email features require the listed SPF setup and Braintree verification before they can be enabled or send receipts or notifications. That unresolved tension is preserved rather than interpreted as current account policy.

## Key takeaways

- An SPF record is a DNS TXT record through which a domain owner identifies servers permitted to send email on its behalf. The page associates this with reducing the chance that mail is caught in recipient spam folders; it does not guarantee delivery, inbox placement, sender authenticity, fraud prevention or domain security.
- For the documented route, the merchant or its DNS administrator adds `include:spf.braintreegateway.com` to the domain's SPF record. If other SPF mechanisms are already present, the page says to keep them in one SPF record line separated by spaces rather than create multiple SPF-record lines.
- The examples show `v=spf1 a mx include:spf.braintreegateway.com -all` and a combined record containing both `include:otherdomain.com` and `include:spf.braintreegateway.com`. These are examples from the collected page, not universal DNS configurations; existing mail infrastructure and the domain provider's requirements remain relevant.
- After publishing the DNS change, the page directs the merchant to contact Braintree to verify the record and states that email receipts or notifications cannot be sent until that step is completed. It routes host- or registrar-specific update problems to the merchant's domain provider.

> [!warning] Requirement and assurance boundaries
> The same snapshot both says SPF configuration is no longer required for integration and describes it as a prerequisite for enabling the named Braintree email features. It does not explain how those statements reconcile, prove that a particular account or domain is enabled, or establish email-delivery, anti-spoofing, fraud-prevention or broader security guarantees.

## Detail locators

- No-longer-required note: `# Configuring SPF Records`, lines 17-18.
- SPF TXT-record purpose and spam-folder wording: `# Configuring SPF Records`, line 20.
- Named Braintree email features and setup-prerequisite wording: `# Configuring SPF Records`, line 22.
- Include mechanism and example single-line records: `# Configuring SPF Records`, lines 25-27.
- Braintree verification gate and provider-specific troubleshooting route: `# Configuring SPF Records`, lines 30-32.

## Related

- Company: [[braintree]]
- Control Panel concept: [[braintree-control-panel]]
- Related receipt configuration: [[source-braintree-control-panel-email-receipts]]
- Related recurring-billing notifications: [[source-braintree-recurring-article-email-notifications]]

## Raw Sources

- [[raw/braintree/articles/guides/configuring-spf-records-2026-09-16|Braintree Configuring SPF Records]] - complete collected guide for the SPF include value, example DNS records, Braintree verification step and domain-provider troubleshooting route
