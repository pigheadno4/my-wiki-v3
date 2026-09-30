---
title: "Braintree Marketplace: Onboarding Sub-merchants"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/braintree-marketplace/onboarding"
raw_files:
  - "braintree/articles/guides/braintree-marketplace/onboarding-2026-09-16.md"
tags: [braintree, marketplace, sub-merchants, onboarding, merchant-agreements]
---

## Overview

This collected Braintree Marketplace article explains the roles and conditions around onboarding a sub-merchant: the marketplace collects applicant and business information, submits it through the Braintree API, receives Braintree's status through a webhook, and remains responsible for sub-merchant support and lawful delivery. It is an article-level retrieval route, not the separate Node.js procedure, and the collected snapshot does not establish current Marketplace availability or eligibility.

## Key takeaways

- New merchants seeking a marketplace solution are directed to Braintree Sales. For an existing Marketplace flow, the article says sub-merchant creation uses the Braintree API and is not available through the Control Panel; Braintree verifies the submitted information and reports status by webhook.
- The marketplace is responsible for supporting its sub-merchants and ensuring that their products or services do not break laws. The onboarding information collected depends on how Marketplace is used and on the funding destination.
- The article distinguishes bank-account disbursement from a legacy Venmo route for existing Marketplace users, while explicitly stating that Venmo funding destinations are no longer supported for new merchants. Exact applicant, business and destination-dependent data fields remain in the raw locator.
- Before accepting payments, sub-merchants must accept Braintree's merchant agreements. The article instructs the marketplace to add required text to its own Terms of Service so the sub-merchant can agree to both sets of terms at once; the exact text and implementation detail are routed to the linked developer guide.

## Evidence boundaries

> [!warning] Snapshot availability and procedure boundary
> Collection of this article does not prove that Braintree Marketplace is currently available or that a merchant or applicant is eligible. Use the separate language-specific developer guide for API procedure; this article does not document a Node.js operation, request shape, or successful approval.

> [!warning] Funding and tax qualifications
> Do not generalize the existing-user Venmo example into current new-merchant support. The article's 1099-K section is expressly framed as of January 1, 2022; treat it as dated source content and verify current tax thresholds, collection duties, filing duties, and distribution duties with current authoritative guidance.

## Detail locators

- New-merchant Sales route: opening `**AVAILABILITY**`, lines 17-18.
- Applicant/business collection, API-versus-Control-Panel boundary, Braintree verification and webhook status, and marketplace support/legal responsibility: introductory paragraph, line 22.
- Funding-destination-dependent collection and bank-versus-existing-user Venmo example: `## Collecting sub-merchant data`, line 27; unsupported new-merchant Venmo destination: `**AVAILABILITY**`, lines 30-31.
- Required and conditional applicant, business and funding data: `### Sub-merchant data parameters`, lines 36-56.
- Full-SSN-or-Tax-ID collection note and the article's dated 1099-K threshold statement: lines 59-60 and `## 1099-Ks`, lines 70-78.
- Merchant-agreement acceptance through the marketplace Terms of Service and developer-doc route: `### Merchant agreement`, lines 65-67.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]
- Status-notification context: [[braintree-webhooks]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-marketplace/onboarding/node-2026-09-16|Braintree Marketplace onboarding guide - Node.js]] - separate navigation-only implementation route; no Node procedure is imported into this article source
- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]] - navigation-only webhook route; no additional event or payload behavior is imported here
- [[raw/braintree/articles/risk-and-security/compliance/ecommerce-website-requirements-2026-09-16|Braintree ecommerce website requirements]] - navigation-only Terms of Service route; no additional compliance requirements are imported here

## Raw Sources

- [[raw/braintree/articles/guides/braintree-marketplace/onboarding-2026-09-16|Braintree Marketplace onboarding article]] - complete collected article covering onboarding roles, information collection, funding-destination qualifications, merchant-agreement acceptance, and dated 1099-K guidance
