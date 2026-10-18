---
title: "Adyen financial-product notification and reporting to Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/compliance-financial-products/reporting-to-adyen"
raw_files:
  - "adyen/docs/platforms/compliance-financial-products/reporting-to-adyen/2026-09-15.md"
tags: [adyen, platforms, financial-products, compliance, reporting]
---

## Overview

This Adyen for Platforms financial-products compliance-guideline page (last modified 2024-01-10; captured 2026-09-15) describes when a platform offering financial products is asked to notify Adyen and what it is asked to report daily or quarterly. It expressly says it is not legal advice. Its timings, channels and product or country qualifications are statements from that dated page, not proof of a platform's fulfillment, current legal duties or current Adyen policy. See [[adyen]], [[adyen-financial-products]] and [[adyen-platforms]].

## Key takeaways

- **Event notification:** The page says platforms must notify Adyen immediately, defined there as within 1–2 business days, for a Security, Regulatory or Legal Complaint, using the dedicated complaints-reporting template. It also lists support circumstances to raise through normal Adyen support lines: unresolved user support requests, unauthorized credential use or fraud/suspicious activity, disputed unauthorized payments or statement errors, material incidents or breaches, and material user non-compliance. It says an API request that itself makes a notification, such as blocking or terminating an account, needs no additional reporting. See raw lines 23–37 for exact triggers and routes.
- **Daily reports:** When relevant instances occur for an available service, the page calls for daily fraud-related incident/dispute counts and reason codes/descriptions for Accounts and Issuing. For fraud reporting it offers the Disputes API or an email address communicated by Adyen. Issuing alone has a blocked, stolen, lost or damaged cards report including instrument ID, scheme status and platform action. See raw lines 39–52; the page does not say every platform has every service.
- **Quarterly complaints:** To the extent applicable law does not prohibit it, the page asks for quarterly reporting to Adyen of users' complaints relating to Adyen products, using Adyen's template. The period starts when the first user is onboarded in the live environment. The listed fields include complaint dates/status/outcome, user and legal-entity references, country, product/category and resolution steps. It says to send the template to complaintreports@adyen.com by 10 January, 10 April, 10 July and 10 October. See raw lines 54–96.
- **UK and Ireland vulnerable-user reporting:** The page adds quarterly vulnerable-user totals and categorized counts, plus outcomes of requests for additional support, on the same complaints-reporting deadlines and recipient. It says only total figures for vulnerable users are required, and calls for an annual sharing of vulnerability patterns the platform believes may need Adyen's attention. This is a UK/Ireland section, not a global reporting recipe. See raw lines 98–112.

## Detail locators

- Non-legal-advice notice and financial-products platform scope: pinned raw lines 15–21.
- Notification triggers, support channel and API-request exception: pinned raw lines 23–37.
- Daily Accounts/Issuing fraud and Issuing-only card reports: pinned raw lines 39–52.
- Quarterly complaint fields, recipient and calendar deadlines: pinned raw lines 54–96.
- UK/Ireland vulnerable-user figures, recipient and annual pattern sharing: pinned raw lines 98–112.

## Related

- [[adyen-financial-products]] — main financial-products concept and reciprocal source route.
- [[adyen-platforms]] — parent platform context.

## Raw Sources

- [[raw/adyen/docs/platforms/compliance-financial-products/reporting-to-adyen/2026-09-15|Adyen notification and reporting guidance, captured 2026-09-15]]
