---
title: "Notification and reporting to Adyen | Business Accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/compliance-guidelines/reporting-to-adyen"
raw_files:
  - "adyen/docs/business-accounts/compliance-guidelines/reporting-to-adyen/2026-09-15.md"
tags: [adyen, business-accounts, compliance, complaints, reporting, vulnerable-users]
---

## Overview

This Business Accounts compliance-guideline page (last modified 2024-01-10; captured 2026-09-15) distinguishes event notifications, daily fraud reporting and quarterly complaints reporting to Adyen for platforms offering business accounts. It expressly says it is not legal advice. Its dated timing, channels and UK/Ireland requirements are guide statements, not proof that a platform reported, met a legal obligation or holds a currently approved product. See [[adyen]], [[adyen-business-accounts]] and the broader [[source-adyen-docs-platforms-compliance-financial-products-reporting-to-adyen]].

## Key takeaways

- **Notify on events:** The page says platforms must notify Adyen immediately, framed as within 1–2 business days, when receiving a Security, Regulatory or Legal Complaint, using the dedicated complaint template. It lists distinct Customer Support Circumstances to raise through normal support lines: unresolved user requests; unauthorized credentials, fraud or suspicious activity; unauthorized-payment disputes or statement errors; material incidents, breaches or material user noncompliance. For notifications that can be made through an API request, such as blocking or terminating an account, it says no additional reporting is required. This exception concerns that API-notifiable event, not all other reports.
- **Daily fraud reporting:** When relevant instances occur for available services, the page calls for daily fraud-related incident/dispute numbers and reason codes/descriptions for Accounts and Issuing. For fraud reporting it permits integration with the Disputes API or reports to an Adyen-communicated email address. The broader financial-products sibling has an Issuing-only card report; this Business Accounts page does not list that card report, so do not import it into this page's scope.
- **Quarterly complaints:** Subject to applicable law not prohibiting disclosure, the platform must share quarterly reports of users' complaints related to Adyen products using Adyen's template. The reporting period starts with onboarding of the first user in the live environment. The page lists receipt/acknowledgment/resolution dates, status/outcome, user/legal-entity/country/product/category and resolution steps; it requires an Upheld or Not upheld determination before closure. It directs the template to complaintreports@adyen.com by 10 January, 10 April, 10 July and 10 October. These are dated guide deadlines, not a jurisdiction-specific legal opinion.
- **UK and Ireland recording versus submission:** The UK/Ireland section says quarterly complaint reporting must contain three data points: total users tagged as vulnerable, totals broken down by vulnerability category, and outcomes of users' requests for additional support. Its table also tells the platform to record individual vulnerability categories and support-request outcomes in its CRM. A later sentence says only total figures for vulnerable users are required. The table's outcomes row and the totals-only sentence leave the exact submitted detail ambiguous; do not equate individual CRM records with report contents or reduce the report to one overall count. The same quarterly deadlines and recipient apply, and specific vulnerability patterns believed to need Adyen's attention are shared annually.

## Detail locators

- Non-legal-advice notice and Business Accounts scope: pinned raw lines 15–21.
- Immediate notification triggers, routes and API-notification exception: pinned raw lines 23–37.
- Daily Accounts/Issuing fraud report and Disputes API/email choice: pinned raw lines 39–46.
- Quarterly complaints scope, fields, determinations and dates: pinned raw lines 48–90.
- UK/Ireland quarterly table data points, individual CRM recording, totals-only sentence and annual patterns: pinned raw lines 92–106.

## Related

- [[adyen-business-accounts]] — main Business Accounts concept and reciprocal source route.
- [[source-adyen-docs-platforms-compliance-financial-products-reporting-to-adyen]] — broader financial-products counterpart, including an Issuing-only card report absent here.

## Raw Sources

- [[raw/adyen/docs/business-accounts/compliance-guidelines/reporting-to-adyen/2026-09-15|Business Accounts reporting guide, captured 2026-09-15]]
